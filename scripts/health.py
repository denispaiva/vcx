#!/usr/bin/env python3
"""Chequeo local de coherencia de VCX: solo lectura, sin red ni correcciones.

Inventario declarado en .gitignore y solera/.gitignore. Compara principios,
procedencia, tarballs, remotos y hooks; delega los pendientes al recordatorio.
Salida: 0 sin errores (puede haber avisos), 1 con errores, 2 con datos inválidos.
"""
import argparse
import fnmatch
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

CODES = ("PRIN-TEXT", "PRIN-ORIGIN", "VEND-HASH", "TOPO-REMOTE", "TOPO-HOOKS",
         "TOPO-ABSENT", "TOPO-UNDECLARED", "ENV", "PEND")
LIMITS = ("Solo coherencia local: no comprueba funcionamiento de proyectos ni que los hooks "
          "bloqueen secretos; no revisa skills, ledgers FinOps ni enlaces.")
TIMEOUT = 15


class DataError(Exception):
    pass


class EnvironmentError(Exception):
    pass


def read_text(path):
    # También detecta permisos 000 cuando los fixtures corren como root.
    if not path.stat().st_mode & 0o444:
        raise DataError("archivo sin permisos de lectura")
    return path.read_text(encoding="utf-8")


def git(repo, *args):
    # Evita heredar un índice/checkout ajeno o activar fetch de objetos prometidos.
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    for key in ("GIT_CONFIG_NOSYSTEM", "GIT_CONFIG_GLOBAL"):
        if key in os.environ:
            env[key] = os.environ[key]
    env.update(GIT_OPTIONAL_LOCKS="0", GIT_TERMINAL_PROMPT="0", GIT_NO_LAZY_FETCH="1")
    try:
        return subprocess.run(["git", "-C", str(repo), *args], capture_output=True,
                              text=True, encoding="utf-8", errors="replace",
                              timeout=TIMEOUT, env=env, check=False)
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise EnvironmentError(f"git no disponible o no respondió en {TIMEOUT}s: {exc}")


def declarations(path):
    """Directorios literales anclados de primer nivel y, aparte, los patrones con comodín.

    Los literales forman el inventario; los comodines (por ejemplo /*-wt-*/ de los
    worktrees) no suman repos, pero declaran lo que cubren. Nunca descubre repos.
    """
    text = read_text(path)
    if "\0" in text:
        raise DataError(".gitignore contiene NUL")
    names, patterns = [], []
    for line in text.splitlines():
        if not line or line.startswith(("#", "!")):
            continue
        if any(c in line for c in "*?["):
            match = re.fullmatch(r"/([^/]+)/?", line)
            if match:
                patterns.append(match[1])
            continue
        match = re.fullmatch(r"/([^/]+)/", line)
        if match:
            name = match[1]
            if name in (".", "..") or "\\" in name or name.strip() != name:
                raise DataError(f"directorio literal inválido: {line!r}")
            if name not in names:
                names.append(name)
        elif line.startswith("/") and line.endswith("/"):
            raise DataError(f"declaración fuera del primer nivel: {line!r}")
    return names, patterns


def principles(text):
    lines = text.replace("\r\n", "\n").replace("\r", "\n").splitlines(keepends=True)
    starts = [i for i, line in enumerate(lines) if line.startswith("1. **VCX-P1")]
    if len(starts) != 1:
        raise DataError("se espera un único bloque desde '1. **VCX-P1'")
    start = starts[0]
    end = next((i for i in range(start + 1, len(lines))
                if lines[i].startswith(("## ", "Adopción y procedencia"))), len(lines))
    block = "".join(lines[start:end])
    ids = re.findall(r"^(\d+)\. \*\*VCX-P(\d+)\b", block, re.M)
    if ids != [(str(n), str(n)) for n in range(1, 10)]:
        raise DataError("se esperan VCX-P1 a VCX-P9, una vez y en orden")
    # La procedencia corresponde a la introducción de esta sección, no a otras copias.
    section = max((i for i in range(start) if lines[i].startswith("## ")), default=0)
    intro = "".join(lines[section:start])
    return hashlib.sha256(block.encode("utf-8")).hexdigest(), intro


def origin_shas(intro):
    shas = re.findall(r"github\.com/denispaiva/vcx/blob/([0-9a-fA-F]{7,40})/AGENTS\.md", intro)
    for line in intro.splitlines():
        if "vcx" in line.lower():
            shas.extend(re.findall(r"(?:SHA|commit|revisión)\s+`([0-9a-fA-F]{7,40})`", line, re.I))
    # Una revisión corta y su enlace largo son la misma declaración.
    values = sorted(set(s.lower() for s in shas), key=len, reverse=True)
    return [s for s in values if not any(other != s and other.startswith(s) for other in values)]


def vendor_hashes(text):
    """Formatos vigentes: un tarball por sección o varios con hashes por nombre."""
    result = {}
    sections = re.split(r"(?m)^## ", text)[1:]
    if not sections:
        raise DataError("procedencia.md: faltan secciones '## `archivo.tgz`'")
    for section in sections:
        heading, _, body = section.partition("\n")
        names = re.findall(r"`([^`/]+\.tgz)`", heading)
        if not names:
            raise DataError(f"encabezado de procedencia no reconocido: {heading}")
        for name in names:
            matches = re.findall(r"^\s*- `" + re.escape(name) + r"`: `([0-9a-fA-F]{64})`", body, re.M)
            if len(names) == 1:
                matches += re.findall(r"^- \*\*sha256:\*\* `([0-9a-fA-F]{64})`", body, re.M)
            if len(matches) != 1 or name in result:
                raise DataError(f"{name}: se espera un único sha256 de 64 dígitos hexadecimales")
            result[name] = matches[0].lower()
    return result


def remote_name(url):
    match = re.fullmatch(r"(?:https://github\.com/|git@github\.com:|ssh://git@github\.com/)"
                        r"(denispaiva/[^/\s]+?)(?:\.git)?/?", url)
    return match[1] if match else None


class Health:
    def __init__(self, root, selected):
        self.root = root
        self.selected = selected
        self.findings = []
        self.invalid = False

    def add(self, code, severity, repo, path, detail):
        # ENV siempre informa fallas de dependencias de los chequeos seleccionados.
        if code not in self.selected and code != "ENV":
            return
        self.findings.append({"code": code, "severity": severity,
                              "repository": repo.relative_to(self.root).as_posix(),
                              "path": path.relative_to(self.root).as_posix(), "detail": detail})

    def attempt(self, code, repo, path, action):
        try:
            return action()
        except EnvironmentError as exc:
            self.add("ENV", "error", repo, path, str(exc))
        except (DataError, OSError, UnicodeError) as exc:
            self.invalid = True
            self.add(code, "error", repo, path, f"datos inválidos o ilegibles: {exc}")
        return None

    def inventory(self):
        repos = [self.root]
        parents = [self.root]
        for parent in parents:
            declared = self.attempt("ENV", parent, parent / ".gitignore",
                                    lambda: declarations(parent / ".gitignore"))
            if declared is None:
                continue
            names, patterns = declared
            for name in names:
                repo = parent / name
                if not repo.is_dir() or not (repo / ".git").exists():
                    self.add("TOPO-ABSENT", "warning", repo, repo / ".git", "checkout declarado ausente")
                    continue
                repos.append(repo)
                if parent == self.root and name == "solera":
                    parents.append(repo)
            if "TOPO-UNDECLARED" in self.selected:
                def scan():
                    for child in sorted(parent.iterdir()):
                        covered = child.name in names or any(fnmatch.fnmatchcase(child.name, p) for p in patterns)
                        if child.is_dir() and (child / ".git").exists() and not covered:
                            self.add("TOPO-UNDECLARED", "error", child, child / ".git",
                                     f"checkout no declarado en {(parent / '.gitignore').relative_to(self.root)}")
                self.attempt("ENV", parent, parent, scan)
        return repos

    def valid_repo(self, repo):
        # config puede funcionar fuera de un repo; --local exige un checkout propio.
        # --git-dir impide que Git ascienda y use por accidente el repositorio padre.
        result = git(repo, "--git-dir", str(repo / ".git"), "config", "--local", "--get", "core.repositoryformatversion")
        if result.returncode != 0:
            self.add("ENV", "error", repo, repo / ".git", "checkout no es un repositorio Git válido")
            return False
        return True

    def check_principles(self, repo, expected, root_valid):
        path = repo / "AGENTS.md"
        parsed = self.attempt("PRIN-TEXT" if "PRIN-TEXT" in self.selected else "PRIN-ORIGIN",
                              repo, path, lambda: principles(read_text(path)))
        if parsed is None:
            return
        actual, intro = parsed
        if "PRIN-TEXT" in self.selected and expected is not None:
            self.add("PRIN-TEXT", "info" if actual == expected else "error", repo, path,
                     f"sha256 esperado={expected}, obtenido={actual}")
        if "PRIN-ORIGIN" not in self.selected:
            return
        shas = origin_shas(intro)
        if not shas:
            self.add("PRIN-ORIGIN", "warning", repo, path, "copia sin SHA de vcx; versión documental no acredita revisión")
        elif root_valid:
            for sha in shas:
                result = git(self.root, "cat-file", "-e", sha + "^{commit}")
                self.add("PRIN-ORIGIN", "info" if result.returncode == 0 else "error", repo, path,
                         f"SHA de vcx {sha}: " + ("existe localmente" if result.returncode == 0 else "no existe en la historia local"))

    def check_vendor(self, repo):
        folder = repo / "vendor"
        if not folder.exists():
            return
        tarballs = sorted(p for p in folder.iterdir() if p.name.endswith(".tgz"))
        if not tarballs:
            return
        path = folder / "procedencia.md"
        if not path.exists():
            for tarball in tarballs:
                self.add("VEND-HASH", "error", repo, tarball, "falta vendor/procedencia.md")
            return
        hashes = vendor_hashes(read_text(path))
        for tarball in tarballs:
            if tarball.name not in hashes:
                self.add("VEND-HASH", "error", repo, tarball, "sin entrada en vendor/procedencia.md")
                continue
            digest = hashlib.sha256()
            with tarball.open("rb") as stream:
                for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                    digest.update(chunk)
            actual, expected = digest.hexdigest(), hashes[tarball.name]
            self.add("VEND-HASH", "info" if actual == expected else "error", repo, tarball,
                     f"sha256 esperado={expected}, obtenido={actual}")

    def check_remote(self, repo):
        name = "vcx" if repo == self.root else repo.name
        if repo.parent == self.root / "solera":
            name = "solera-" + name
        expected = "denispaiva/" + name
        result = git(repo, "remote", "get-url", "origin")
        actual = result.stdout.strip()
        self.add("TOPO-REMOTE", "info" if result.returncode == 0 and remote_name(actual) == expected else "error",
                 repo, repo / ".git", f"origin esperado={expected}, obtenido={actual or '(ausente)'}")

    def check_hooks(self, repo):
        result = git(repo, "config", "--get", "core.hooksPath")
        if result.returncode not in (0, 1):
            raise EnvironmentError("no se pudo leer core.hooksPath")
        value = result.stdout.strip()
        if not value:
            self.add("TOPO-HOOKS", "warning", repo, repo / ".git", "core.hooksPath no definido")
            return
        path = Path(value).expanduser()
        if not path.is_absolute():
            path = repo / path
        self.add("TOPO-HOOKS", "info" if path.is_dir() else "error", repo, repo / ".git",
                 f"core.hooksPath={value}: " + ("ruta existente" if path.is_dir() else "ruta inexistente o no es directorio"))

    def check_pending(self):
        # Ejecuta solo el script confiable que acompaña health.py, nunca código del fixture/proyecto.
        script = Path(__file__).resolve().with_name("pending_triggers.py")
        try:
            result = subprocess.run([sys.executable, "-I", str(script), "--root", str(self.root), "--window", "14"],
                                    capture_output=True, text=True, encoding="utf-8", errors="replace",
                                    timeout=TIMEOUT, check=False)
        except (OSError, subprocess.TimeoutExpired) as exc:
            raise EnvironmentError(f"pending_triggers.py no pudo ejecutarse: {exc}")
        lines = (result.stdout + result.stderr).strip().splitlines()
        if result.returncode != 0:
            self.invalid = True
        severity = "error" if result.returncode != 0 else "warning"
        for line in lines:
            level = "info" if result.returncode == 0 and line.startswith("ℹ ") else severity
            self.add("PEND", level, self.root, self.root / "scripts/pending_triggers.py", line.strip())
        if not lines:
            self.add("PEND", severity if result.returncode else "info", self.root,
                     self.root / "scripts/pending_triggers.py",
                     f"exit {result.returncode}" if result.returncode else "sin pendientes en la ventana de 14 días")

    def run(self):
        repos = self.inventory()
        needs_git = bool(self.selected & {"PRIN-TEXT", "PRIN-ORIGIN", "TOPO-REMOTE", "TOPO-HOOKS", "ENV"})
        valid = {}
        if needs_git:
            for repo in repos:
                valid[repo] = self.attempt("ENV", repo, repo / ".git", lambda: self.valid_repo(repo))
        expected = None
        if "PRIN-TEXT" in self.selected and valid.get(self.root):
            def reference():
                # Lectura de blob autorizada por el usuario el 2026-11-16.
                result = git(self.root, "cat-file", "blob", "HEAD:AGENTS.md")
                if result.returncode != 0:
                    raise DataError("no se pudo leer HEAD:AGENTS.md")
                return principles(result.stdout)[0]
            expected = self.attempt("PRIN-TEXT", self.root, self.root / "AGENTS.md", reference)
        for repo in repos:
            if repo != self.root and self.selected & {"PRIN-TEXT", "PRIN-ORIGIN"}:
                self.attempt("PRIN-TEXT" if "PRIN-TEXT" in self.selected else "PRIN-ORIGIN", repo, repo / "AGENTS.md",
                             lambda: self.check_principles(repo, expected, valid.get(self.root)))
            if "VEND-HASH" in self.selected:
                self.attempt("VEND-HASH", repo, repo / "vendor/procedencia.md", lambda: self.check_vendor(repo))
            if valid.get(repo):
                for code, check in (("TOPO-REMOTE", self.check_remote), ("TOPO-HOOKS", self.check_hooks)):
                    if code in self.selected:
                        self.attempt(code, repo, repo / ".git", lambda: check(repo))
        if "PEND" in self.selected:
            self.attempt("PEND", self.root, self.root / "scripts/pending_triggers.py", self.check_pending)
        return 2 if self.invalid else int(any(f["severity"] == "error" for f in self.findings))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent,
                    help="raíz del workspace; por defecto la que contiene este script")
    ap.add_argument("--json", action="store_true", help="reporte estructurado")
    ap.add_argument("--only", help="códigos separados por comas: " + ", ".join(CODES))
    args = ap.parse_args(argv)
    selected = set(CODES) if args.only is None else {s.strip() for s in args.only.split(",")}
    if not selected <= set(CODES) or not selected:
        ap.error("--only contiene códigos vacíos o desconocidos")
    health = Health(args.root.resolve(), selected)
    status = health.run()
    summary = {severity: sum(f["severity"] == severity for f in health.findings)
               for severity in ("error", "warning", "info")}
    if args.json:
        print(json.dumps({"findings": health.findings, "summary": summary, "limitations": LIMITS}, ensure_ascii=False, indent=2))
    else:
        for f in health.findings:
            print(f"{f['code']} {f['severity']} {f['repository']} · {f['path']}: {f['detail']}")
        print(LIMITS)
        print(f"Resumen: {summary['error']} errores, {summary['warning']} avisos, {summary['info']} comprobaciones informativas.")
    return status


if __name__ == "__main__":
    sys.exit(main())
