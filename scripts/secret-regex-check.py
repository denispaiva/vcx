#!/usr/bin/env python3
"""Búsqueda interina de secretos por expresiones regulares para un repositorio Git.

Mitigación limitada: no reemplaza un scanner dedicado. Solo biblioteca estándar.
Uso:  python3 -I secret-regex-check.py --repo <ruta> (--staged | --worktree | --history) [--allow <archivo>]

Salida: una línea por hallazgo con regla, ubicación y metadatos seguros (longitud y
huella SHA-256 truncada del valor). Nunca imprime el valor ni la línea completa.
Códigos de salida: 0 limpio y completo; 1 hallazgos; 2 error operativo; 3 análisis
incompleto sin hallazgos (objetos omitidos por tamaño).
"""
import argparse
import hashlib
import re
import subprocess
import sys

MAX_BYTES = 1024 * 1024  # objetos mayores se omiten y el análisis se declara parcial
BINARY_PROBE = 8192

# Reglas propuestas (no son las del reporte del 2026-11-01, que no se conservaron).
RULES = [
    ("github-token", re.compile(rb"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{36,}\b")),
    ("github-fine-grained-pat", re.compile(rb"\bgithub_pat_[A-Za-z0-9_]{22,}\b")),
    ("anthropic-api-key", re.compile(rb"\bsk-ant-[A-Za-z0-9_-]{20,}")),
    ("openai-api-key", re.compile(rb"\bsk-(?!ant-)(?:proj-|svcacct-)?[A-Za-z0-9_-]{32,}")),
    ("aws-access-key-id", re.compile(rb"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
    ("google-api-key", re.compile(rb"\bAIza[0-9A-Za-z_-]{35}\b")),
    ("slack-token", re.compile(rb"\bxox[abprs]-[0-9A-Za-z-]{10,}\b")),
    ("stripe-key", re.compile(rb"\b[sr]k_(?:live|test)_[0-9A-Za-z]{16,}\b")),
    ("jwt", re.compile(rb"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b")),
    ("private-key-block", re.compile(rb"-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP )?PRIVATE KEY(?: BLOCK)?-----")),
    ("generic-assignment", re.compile(
        rb"(?i)\b(?:password|passwd|secret|api[_-]?key|access[_-]?token|auth[_-]?token)\s*[:=]\s*['\"][^'\"\s]{8,}['\"]")),
]


def die(msg, code=2):
    sys.stderr.write("error: %s\n" % msg)
    sys.exit(code)


def git(repo, *args, data=None):
    try:
        p = subprocess.run(["git", "-C", repo, *args], input=data, capture_output=True, check=False)
    except OSError as e:
        die("no se pudo ejecutar git: %s" % e)
    if p.returncode != 0:
        die("git %s falló: %s" % (" ".join(args[:2]), p.stderr.decode("utf-8", "replace").strip()))
    return p.stdout


def fingerprint(value):
    return hashlib.sha256(value).hexdigest()


def load_allow(path):
    allowed = {}
    if not path:
        return allowed
    try:
        with open(path, "rb") as f:
            for n, raw in enumerate(f, 1):
                line = raw.strip()
                if not line or line.startswith(b"#"):
                    continue
                parts = line.split(None, 2)
                if len(parts) < 3 or not re.fullmatch(rb"[0-9a-f]{64}", parts[0]):
                    die("%s:%d: formato esperado '<sha256> <regla> <justificación>'" % (path, n))
                allowed[(parts[0].decode(), parts[1].decode())] = parts[2].decode("utf-8", "replace")
    except OSError as e:
        die("no se pudo leer el archivo de excepciones: %s" % e)
    return allowed


def scan_blob(content, label, allowed, findings, suppressed):
    if b"\0" in content[:BINARY_PROBE]:
        return "binary"
    for rule, rx in RULES:
        for m in rx.finditer(content):
            value = m.group(0)
            fp = fingerprint(value)
            line_no = content.count(b"\n", 0, m.start()) + 1
            key = (fp, rule)
            if key in allowed:
                suppressed.append((rule, label, line_no, fp[:16]))
                continue
            findings.append((rule, label, line_no, len(value), fp[:16]))
    return "scanned"


def iter_staged(repo):
    out = git(repo, "diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z")
    for path in out.split(b"\0"):
        if path:
            yield path, git(repo, "show", b":" + path), "index:" + path.decode("utf-8", "replace")


def iter_worktree(repo):
    out = git(repo, "ls-files", "-z")
    full = git(repo, "rev-parse", "--show-toplevel").strip().decode("utf-8", "surrogateescape")
    for path in out.split(b"\0"):
        if not path:
            continue
        p = path.decode("utf-8", "surrogateescape")
        try:
            with open(full + "/" + p, "rb") as f:
                content = f.read(MAX_BYTES + 1)
        except OSError as e:
            die("no se pudo leer %r: %s" % (p, e))
        yield path, content, "worktree:" + path.decode("utf-8", "replace")


def iter_history(repo):
    # Todos los blobs alcanzables desde cualquier ref (ramas, tags, stashes, remotos).
    objs = git(repo, "rev-list", "--objects", "--all")
    blobs = {}
    for line in objs.splitlines():
        parts = line.split(b" ", 1)
        if len(parts) == 2:
            blobs.setdefault(parts[0], parts[1])
    if not blobs:
        return
    ids = list(blobs)
    out = git(repo, "cat-file", "--batch", data=b"\n".join(ids) + b"\n")
    pos = 0
    while pos < len(out):
        nl = out.index(b"\n", pos)
        header = out[pos:nl].split()
        pos = nl + 1
        if len(header) == 2 and header[1] == b"missing":
            die("objeto faltante %s" % header[0].decode())
        oid, otype, size = header[0], header[1], int(header[2])
        body = out[pos:pos + size]
        pos += size + 1
        if otype != b"blob":
            continue
        name = blobs[oid].decode("utf-8", "replace")
        yield blobs[oid], body, "blob:%s:%s" % (oid.decode()[:12], name)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repo", required=True, help="ruta explícita del repositorio")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--staged", action="store_true", help="índice preparado para commit")
    mode.add_argument("--worktree", action="store_true", help="archivos rastreados del árbol de trabajo")
    mode.add_argument("--history", action="store_true", help="todos los blobs alcanzables desde cualquier ref")
    ap.add_argument("--allow", help="archivo de excepciones: '<sha256> <regla> <justificación>' por línea")
    args = ap.parse_args()

    if git(args.repo, "rev-parse", "--is-inside-work-tree").strip() != b"true":
        die("%s no es un árbol de trabajo de Git" % args.repo)
    allowed = load_allow(args.allow)
    it = iter_staged(args.repo) if args.staged else iter_worktree(args.repo) if args.worktree else iter_history(args.repo)
    scope = "staged" if args.staged else "worktree" if args.worktree else "history"

    findings, suppressed, skipped = [], [], []
    scanned = binary = 0
    for _path, content, label in it:
        if len(content) > MAX_BYTES:
            skipped.append(label)
            continue
        if scan_blob(content, label, allowed, findings, suppressed) == "binary":
            binary += 1
        else:
            scanned += 1

    for rule, label, line_no, length, fp in sorted(findings):
        print("FINDING\t%s\t%s\tline=%d\tlen=%d\tfp=%s" % (rule, label, line_no, length, fp))
    for rule, label, line_no, fp in sorted(suppressed):
        print("ALLOWED\t%s\t%s\tline=%d\tfp=%s" % (rule, label, line_no, fp))
    for label in skipped:
        print("SKIPPED\tsize>%d\t%s" % (MAX_BYTES, label))
    print("SUMMARY\tscope=%s\tscanned=%d\tbinary=%d\tskipped=%d\tfindings=%d\tallowed=%d\trules=%d"
          % (scope, scanned, binary, len(skipped), len(findings), len(suppressed), len(RULES)))
    if findings:
        sys.exit(1)
    if skipped:
        sys.exit(3)
    sys.exit(0)


if __name__ == "__main__":
    main()
