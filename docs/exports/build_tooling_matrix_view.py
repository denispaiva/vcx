"""Genera docs/exports/tooling-matrix.html desde docs/architecture/tooling-matrix.md.

Herramienta documental opcional: solo usa la biblioteca estándar y git. No es
dependencia de ningún producto. Exige que la matriz no tenga cambios sin commit,
para que la vista cite una revisión identificable.

Uso, desde la raíz de vcx: python3 -I docs/exports/build_tooling_matrix_view.py
"""
import html, json, re, subprocess, sys
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

section = text.split("## Matriz", 1)[1].split("\n## ", 1)[0]
lines = [l for l in section.splitlines() if l.startswith("| ")]
rows = []
for l in lines[1:]:
    if set(l.replace("|", "").strip()) <= {"-"}:
        continue
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    product, _, phase = c[0].partition(" · ")
    stage, _, sub = phase.partition(", ")
    tools = re.findall(r"`([^`]+)`", c[3])
    states = [s.strip() for s in c[5].split(";")]
    if len(states) != len(tools):
        states = [states[0]] * max(len(tools), 1)
    rows.append(dict(product=product, stage=stage, sub=sub, cap=c[1], need=c[2],
                     tools=[dict(id=t, state=s.capitalize()) for t, s in zip(tools, states)],
                     state=states[0].capitalize(), kind=c[4], note=c[6]))

unused = re.search(r"Capacidades registradas sin fila al corte: (.+?)\. Se agregan", text)
unused = re.findall(r"`([^`]+)`", unused.group(1)) if unused else []

data = json.dumps(dict(rows=rows, unused=unused, rev=rev), ensure_ascii=False)
tpl = (Path(__file__).parent / "tooling-matrix.template.html").read_text()
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(tpl.replace("/*DATA*/null", data))
print(f"{len(rows)} filas → {out} (fuente {rev})")
