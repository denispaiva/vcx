"""Genera la vista «Tablero del portfolio» desde los roadmaps de la instancia y sus proyectos.

Herramienta documental opcional: solo usa la biblioteca estándar y git. No es
dependencia de ningún producto. Lee `solera/` y cada checkout `solera/<proyecto>/`
(o los repositorios que se pasen con --repo) en solo lectura con `git show`
sobre refs locales, sin fetch, checkout ni sincronización, como pide el mapeo
del sistema actual. Las refs se fijan por argumento y la vista cita sus
revisiones, para que se note si los datos quedaron viejos.

La salida contiene datos de proyectos privados (VCX-D032). Este repositorio es
público: el generador se niega a escribir dentro de él o de los repositorios de origen.
Publicarla solo como artifact privado.

La plantilla calcula en el navegador el orden del backlog (prioridad
confirmada, luego sugerida, luego antigüedad) y una proyección por velocidad.
Es deuda declarada: replica una regla de Blends y una capacidad que el modelo
asigna a Brix, hasta que exista el contrato de conducción de Cellar
(vocabulario, caso de referencia `board`). Arrastrar o partir tarjetas solo
registra propuestas en la base del artifact; nunca escribe en la cola ni en
los roadmaps.

Uso, desde la raíz de vcx:
  python3 -I docs/exports/build_portfolio_board_view.py --out <ruta fuera de vcx>/portfolio-board.html
"""
import argparse, datetime, json, subprocess, sys
from pathlib import Path

root = Path(__file__).resolve().parents[2]
template = root / "docs/exports/portfolio-board.template.html"
PLACEHOLDER = "/*DATA*/null/*END*/"

ap = argparse.ArgumentParser(description="Genera la vista Tablero del portfolio.")
ap.add_argument("--repo", action="append", help="checkout a leer (repetible); por defecto solera/ y cada solera/<proyecto>/")
ap.add_argument("--roadmap-ref", default="main", help="ref local con los .roadmap.json en cada repositorio")
ap.add_argument("--queue-repo", help="checkout con la rama de cola y backlog/ (opcional; la cola quedó en el precursor archivado)")
ap.add_argument("--queue-ref", default="queue", help="ref local con la carpeta backlog/ en --queue-repo")
ap.add_argument("--today", default=datetime.date.today().isoformat(), help="fecha de referencia AAAA-MM-DD")
ap.add_argument("--out", required=True, help="archivo HTML de salida, fuera de vcx y de los repositorios de origen")
args = ap.parse_args()

solera = root / "solera"
repos = [Path(x).resolve() for x in args.repo] if args.repo else (
    [solera] + sorted(d for d in solera.iterdir() if (d / ".git").exists()) if (solera / ".git").exists() else [])
if not repos:
    sys.exit("No hay repositorios que leer: falta el checkout solera/ (o pasá --repo).")
queue_repo = Path(args.queue_repo).resolve() if args.queue_repo else None
out = Path(args.out).resolve()
for forbidden, why in ((root, "vcx es público (VCX-D032)"), *((d, "los repositorios de origen son de solo lectura") for d in repos)):
    if out == forbidden or forbidden in out.parents:
        sys.exit(f"La salida no puede quedar en {forbidden}: {why}.")
try:
    datetime.date.fromisoformat(args.today)
except ValueError:
    sys.exit("--today debe tener formato AAAA-MM-DD.")


def git(repo, *a):
    r = subprocess.run(["git", "-C", str(repo), *a], capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"git -C {repo} {' '.join(a)} falló: {r.stderr.strip()}")
    return r.stdout


def revision(repo, ref):
    sha, date = git(repo, "log", "-1", "--format=%h|%cI", ref, "--").strip().split("|")
    return dict(ref=f"{repo.name}:{ref}", sha=sha, date=date)


def clip(s, n):
    s = (s or "").strip()
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


warnings = []
projects, sprints, tasks, deliverables = [], [], [], []
paths = [(repo, p) for repo in repos for p in git(repo, "ls-tree", "-r", "--name-only", args.roadmap_ref).split()
         if p.endswith(".roadmap.json") and not p.startswith("roadmap/")]
for repo, rel in paths:
    path = f"{repo.name}/{rel}"
    try:
        r = json.loads(git(repo, "show", f"{args.roadmap_ref}:{rel}"))
        pid = r["id"]
        projects.append(dict(id=pid, title=r.get("title") or pid, status=r.get("status"),
                             kind="idea" if rel.startswith("ideas/") else "proyecto",
                             updatedAt=r.get("updatedAt"), path=path))
        for s in r.get("sprints", []):
            sprints.append(dict(project=pid, id=s["id"], start=s["startDate"], end=s["endDate"],
                                status=s.get("status"), goal=clip(s.get("goal"), 400)))
        for e in r.get("epics", []):
            for t in e.get("tasks", []):
                tasks.append(dict(project=pid, id=t["id"], title=clip(t.get("title"), 300),
                                  status=t.get("status"), points=t.get("effortPoints"),
                                  sprintId=t.get("sprintId"), epicId=e.get("id"), epic=e.get("title")))
        for d in r.get("deliverables", []):
            deliverables.append(dict(project=pid, id=d["id"], title=clip(d.get("title"), 200),
                                     status=d.get("status"), sprintId=d.get("sprintId"),
                                     epicId=d.get("epicId"), version=d.get("version")))
    except (KeyError, json.JSONDecodeError) as exc:
        warnings.append(f"{path}: no se pudo leer ({exc})")

backlog = []
if queue_repo is None:
    warnings.append("Sin cola: quedó en el precursor archivado. Pasá --queue-repo para leerla.")
for f in (git(queue_repo, "ls-tree", "--name-only", args.queue_ref, "backlog/").split() if queue_repo else []):
    if not f.endswith(".json"):
        continue
    try:
        i = json.loads(git(queue_repo, "show", f"{args.queue_ref}:{f}"))
        backlog.append(dict(id=i["id"], project=i["project"], kind=i.get("kind"), status=i["status"],
                            title=clip(i.get("title"), 300), summary=clip(i.get("summary"), 700),
                            priority=i.get("priority"), suggestedPriority=i.get("suggestedPriority"),
                            points=i.get("effortPoints"), requestedAt=i.get("requestedAt"),
                            decideBy=i.get("decideBy"), sourceRef=i.get("sourceRef"),
                            recommendation=clip(i.get("recommendation"), 400),
                            promotedTo=i.get("promotedTo"), epicId=i.get("epicId")))
    except (KeyError, json.JSONDecodeError) as exc:
        warnings.append(f"{f}: no se pudo leer ({exc})")

known = {p["id"] for p in projects}
for pid in sorted({b["project"] for b in backlog} - known):
    warnings.append(f"El backlog tiene pedidos de «{pid}», que no tiene roadmap en {args.roadmap_ref}.")
    projects.append(dict(id=pid, title=pid, status=None, kind="proyecto", updatedAt=None, path=None))

def roadmap_sources():
    revs = [revision(repo, args.roadmap_ref) for repo in repos]
    return dict(ref=f"{args.roadmap_ref} de {len(revs)} repositorios",
                sha=" ".join(f"{x['ref'].split(':')[0]}@{x['sha']}" for x in revs),
                date=max(x["date"] for x in revs))


data = dict(today=args.today, generatedAt=datetime.datetime.now().astimezone().isoformat(timespec="minutes"),
            sources=dict(roadmaps=roadmap_sources(), queue=revision(queue_repo, args.queue_ref) if queue_repo
                         else dict(ref="sin cola", sha="—", date=args.today)),
            projects=projects, sprints=sprints, tasks=tasks, deliverables=deliverables,
            backlog=backlog, warnings=warnings)
payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
html = template.read_text()
if html.count(PLACEHOLDER) != 1:
    sys.exit("La plantilla debe contener una sola marca de datos.")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(html.replace(PLACEHOLDER, payload))
print(f"{out} · {len(projects)} iniciativas · {len(sprints)} sprints · {len(tasks)} tareas · "
      f"{len(deliverables)} hitos · {len(backlog)} pedidos · {len(warnings)} avisos")
