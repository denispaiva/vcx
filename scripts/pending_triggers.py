#!/usr/bin/env python3
"""Recordatorio de pendientes con disparador: avisa, nunca decide ni bloquea.

Lee dos fuentes, sin copiarlas:
- docs/decisions/pending-triggers.json: pendientes con rutas disparadoras y fecha de revisión.
- brix/tooling/evaluations/*.evaluation.json: humanDecision.reviewAt y expiresAt.

Avisa cuando un cambio toca una ruta disparadora o cuando una fecha venció o vence
dentro de la ventana. Diseño y decisión: VCX-D058 en docs/decisions/README.md.

Salida: 0 siempre que los datos sean válidos, haya o no avisos; 2 si una fuente es
inválida. El hook pre-commit ignora el código (falla abierto); la CI lo respeta.
"""
import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
from pathlib import Path

TRIGGERS = Path("docs/decisions/pending-triggers.json")
EVALUATIONS = Path("brix/tooling/evaluations")


class DataError(Exception):
    pass


def glob_regex(pattern):
    """Glob con `**` que cruza carpetas y `*` que no; se ancla a la ruta completa."""
    out, i = "", 0
    while i < len(pattern):
        if pattern.startswith("**/", i):
            out, i = out + "(?:.*/)?", i + 3
        elif pattern.startswith("**", i):
            out, i = out + ".*", i + 2
        elif pattern[i] == "*":
            out, i = out + "[^/]*", i + 1
        elif pattern[i] == "?":
            out, i = out + "[^/]", i + 1
        else:
            out, i = out + re.escape(pattern[i]), i + 1
    return re.compile(out + r"\Z")


def parse_date(value, where):
    try:
        return dt.date.fromisoformat(str(value)[:10])
    except ValueError:
        raise DataError(f"{where}: fecha inválida {value!r}")


def load_items(root):
    items = []
    path = root / TRIGGERS
    if path.exists():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            raise DataError(f"{TRIGGERS}: JSON inválido ({e})")
        if data.get("schemaVersion") != 1 or not isinstance(data.get("items"), list):
            raise DataError(f"{TRIGGERS}: se espera schemaVersion 1 y una lista items")
        seen = set()
        for n, it in enumerate(data["items"]):
            where = f"{TRIGGERS} items[{n}]"
            for key in ("id", "decision", "title", "reviewAt"):
                if not isinstance(it.get(key), str) or not it[key].strip():
                    raise DataError(f"{where}: falta {key}")
            if it["id"] in seen:
                raise DataError(f"{where}: id repetido {it['id']}")
            seen.add(it["id"])
            paths = it.get("paths", [])
            if not isinstance(paths, list) or not all(isinstance(p, str) and p for p in paths):
                raise DataError(f"{where}: paths debe ser una lista de globs")
            items.append({
                "id": it["id"], "ref": it["decision"], "title": it["title"],
                "paths": [(p, glob_regex(p)) for p in paths],
                "dates": [("revisión", parse_date(it["reviewAt"], where))],
            })
    folder = root / EVALUATIONS
    for f in sorted(folder.glob("*.evaluation.json")) if folder.is_dir() else []:
        rel = f.relative_to(root).as_posix()
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            raise DataError(f"{rel}: JSON inválido ({e})")
        cid = (d.get("candidate") or {}).get("id") or f.name.split(".")[0]
        status = (d.get("humanDecision") or {}).get("status") or d.get("status") or "sin decisión"
        dates = []
        review = (d.get("humanDecision") or {}).get("reviewAt")
        if review:
            dates.append(("revisión", parse_date(review, rel)))
        if d.get("expiresAt"):
            dates.append(("vencimiento", parse_date(d["expiresAt"], rel)))
        if dates:
            items.append({"id": f"tooling:{cid}", "ref": rel, "title": f"evaluación de {cid} ({status})",
                          "paths": [], "dates": dates})
    return items


def changed_paths(root, staged, rng):
    if staged:
        args = ["git", "diff", "--cached", "--name-only", "-z"]
    else:
        args = ["git", "diff", "--name-only", "-z", rng]
    out = subprocess.run(args, cwd=root, capture_output=True, check=True).stdout
    return [p for p in out.decode("utf-8", "surrogateescape").split("\0") if p]


def plural(n):
    return f"{n} día" if n == 1 else f"{n} días"


def evaluate(items, paths, today, window):
    alerts = []
    for it in items:
        hits = sorted({p for p in paths for _, rx in it["paths"] if rx.match(p)})
        if hits:
            alerts.append(("disparo", it, f"el cambio toca {', '.join(hits[:5])}" + (" y más" if len(hits) > 5 else "")))
        for label, when in it["dates"]:
            days = (when - today).days
            if days < 0:
                alerts.append(("vencido", it, f"{label} vencida el {when} (hace {plural(-days)})"))
            elif days == 0:
                alerts.append(("vencido", it, f"{label} vence hoy, {when}"))
            elif days <= window:
                alerts.append(("próximo", it, f"{label} el {when} (en {plural(days)})"))
    order = {"disparo": 0, "vencido": 1, "próximo": 2}
    return sorted(alerts, key=lambda a: (order[a[0]], a[1]["id"]))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    src = ap.add_mutually_exclusive_group()
    src.add_argument("--staged", action="store_true", help="rutas del índice de Git (pre-commit)")
    src.add_argument("--range", help="rango de Git, p. ej. BASE...HEAD (CI)")
    src.add_argument("--paths", nargs="*", help="rutas explícitas (pruebas)")
    ap.add_argument("--root", type=Path, help="raíz del repositorio; por defecto la de Git")
    ap.add_argument("--today", help="fecha de referencia AAAA-MM-DD; por defecto hoy (UTC)")
    ap.add_argument("--window", type=int, default=14, help="días de anticipación para «próximo»; 0 lo desactiva")
    ap.add_argument("--github", action="store_true", help="anotaciones y resumen de GitHub Actions")
    a = ap.parse_args(argv)

    root = a.root or Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                                         capture_output=True, text=True, check=True).stdout.strip())
    today = dt.date.fromisoformat(a.today) if a.today else dt.datetime.now(dt.timezone.utc).date()
    try:
        items = load_items(root)
    except DataError as e:
        print(f"✖ pendientes: {e}", file=sys.stderr)
        if a.github:
            print(f"::error title=Pendientes con disparador::{e}")
        return 2
    paths = a.paths if a.paths is not None else (
        changed_paths(root, a.staged, a.range) if (a.staged or a.range) else [])
    alerts = evaluate(items, paths, today, a.window)

    if not alerts:
        if a.github:
            print("Sin pendientes disparados ni fechas en la ventana.")
        return 0
    lines = [f"{kind.upper():9} {it['id']} · {it['title']}: {why}. Fuente: {it['ref']}" for kind, it, why in alerts]
    if a.github:
        for kind, it, why in alerts:
            print(f"::warning title=Pendiente {kind}: {it['id']}::{it['title']}: {why}. Fuente: {it['ref']}")
        summary = os.environ.get("GITHUB_STEP_SUMMARY")
        if summary:
            with open(summary, "a", encoding="utf-8") as fh:
                fh.write("### Pendientes con disparador\n\n| Tipo | Pendiente | Motivo | Fuente |\n|---|---|---|---|\n")
                for kind, it, why in alerts:
                    fh.write(f"| {kind} | `{it['id']}` {it['title']} | {why} | `{it['ref']}` |\n")
                fh.write("\nSolo recuerda: retomar, extender o descartar se decide y se registra en la fuente.\n")
    else:
        print("ℹ Pendientes para validar (no bloquea; decidir y registrar en la fuente):", file=sys.stderr)
        for line in lines:
            print("  " + line, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
