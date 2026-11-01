"""Genera docs/exports/tooling-matrix.html desde docs/architecture/tooling-matrix.md.

Herramienta documental opcional: solo usa la biblioteca estándar y git. No es
dependencia de ningún producto. Exige que la matriz no tenga cambios sin commit,
para que la vista cite una revisión identificable, y que cada elemento que la
matriz consume tenga ubicación en la tabla «Dónde vive cada elemento».

Si existe la carpeta hermana del precursor, incorpora de sus evaluaciones de
solo lectura la decisión, las fechas y el riesgo de cada herramienta; la vista
calcula al abrirse si la revisión venció. Sin esa carpeta, la vista se genera
igual y avisa que no tiene datos de evaluación.

Uso, desde la raíz de vcx: python3 -I docs/exports/build_tooling_matrix_view.py
"""
import json, re, subprocess, sys
from pathlib import Path

root = Path(__file__).resolve().parents[2]
src = root / "docs/architecture/tooling-matrix.md"
out = root / "docs/exports/tooling-matrix.html"
text = src.read_text()

rev = subprocess.run(["git", "-C", str(root), "log", "-1", "--format=%h %ad", "--date=short", "--", str(src)],
                     capture_output=True, text=True).stdout.strip()
dirty = subprocess.run(["git", "-C", str(root), "status", "--porcelain", "--", str(src)],
                       capture_output=True, text=True).stdout.strip()
if dirty:
    sys.exit("La matriz tiene cambios sin commit; la vista debe citar una revisión identificable.")


def table(heading):
    section = text.split(f"## {heading}", 1)[1].split("\n## ", 1)[0]
    lines = [l for l in section.splitlines() if l.startswith("| ")][1:]
    return [[x.strip() for x in l.strip().strip("|").split("|")]
            for l in lines if not set(l.replace("|", "").strip()) <= {"-"}]


ticks = lambda s: re.findall(r"`([^`]+)`", s)
unregistered = lambda s: (re.match(r"No registrada \((.+)\)", s) or [None, None])[1]

# Dónde vive: clave → ubicación; la fila sin claves de tipo «Skill o MCP» es la regla general.
homes, default_tool_home = {}, None
for c in table("Dónde vive cada elemento"):
    home = dict(home=c[2], source=c[3], note=c[4])
    keys = ticks(c[0])
    if keys:
        for k in keys:
            homes[k] = home
    elif c[1] == "Skill o MCP":
        default_tool_home = home
    else:
        homes[c[0].lower()] = home

items, loose, missing = {}, [], []


def item(key, label, kind, home):
    if home is None:
        missing.append(label)
        return None
    return items.setdefault(key, dict(id=label, kind=kind, code=kind != "Capacidad no registrada",
                                      uses=[], **home))


for c in table("Matriz"):
    product, _, phase = c[0].partition(" · ")
    tools = ticks(c[3].split("(")[0]) if c[3] != "—" else []
    states = [s.strip().capitalize() for s in c[5].split(";")]
    if len(states) != len(tools):
        states = [states[0]] * max(len(tools), 1)
    kinds = c[4].split(", ")
    if len(kinds) != len(tools):
        kinds = [c[4]] * len(tools)
    use = dict(product=product, phase=phase, need=c[2], cap=c[1], tool=c[3], note=c[6])
    touched = False
    for t, s, k in zip(tools, states, kinds):
        it = item("t:" + t, t, k, homes.get(t, default_tool_home))
        if it:
            it["uses"].append(dict(use, state=s)); touched = True
    caps = ticks(c[1]) or ([unregistered(c[1])] if unregistered(c[1]) else [])
    for k in caps:
        label_kind = "Capacidad" if ticks(c[1]) else "Capacidad no registrada"
        label = k if ticks(c[1]) else k[0].upper() + k[1:]
        it = item("c:" + k, label, label_kind, homes.get(k) or homes.get(k.lower()))
        if it:
            it["uses"].append(dict(use, state=states[0])); touched = True
    if not touched:
        loose.append(dict(use, state=states[0]))

if missing:
    sys.exit("Sin ubicación en «Dónde vive cada elemento»: " + ", ".join(sorted(set(missing))))

evals_dir = root.parent / "blends/vc/tooling/evaluations"
evals_rev = None
if evals_dir.is_dir():
    evals_rev = subprocess.run(["git", "-C", str(evals_dir), "log", "-1", "--format=%h %ad", "--date=short", "--", "."],
                               capture_output=True, text=True).stdout.strip() or "sin revisión"
    for it in items.values():
        if it["kind"].startswith("Capacidad"):
            continue
        f = evals_dir / f"{it['id']}.evaluation.json"
        if not f.exists():
            it["eval"] = None
            continue
        e = json.loads(f.read_text())
        decision = (e.get("humanDecision") or {})
        it["eval"] = dict(status=decision.get("status") or e.get("status"), decidedAt=(decision.get("decidedAt") or "")[:10],
                          expiresAt=(e.get("expiresAt") or "")[:10], score=round(e.get("overallScore") or 0, 1),
                          risk=e.get("riskLevel"), confidence=e.get("confidence"))

data = json.dumps(dict(items=list(items.values()), loose=loose, rev=rev, evalsRev=evals_rev), ensure_ascii=False)
tpl = (Path(__file__).parent / "tooling-matrix.template.html").read_text()
out.write_text(tpl.replace("/*DATA*/null", data))
print(f"{len(items)} elementos, {len(loose)} necesidades sin elemento → {out} (fuente {rev}; "
      f"evaluaciones {evals_rev or 'no disponibles'})")
