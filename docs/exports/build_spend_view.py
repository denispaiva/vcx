"""Genera los datos del tablero «Gasto y consumo VCX» desde los ledgers de la instancia y sus proyectos y los registros locales de tokens.

Herramienta documental opcional: solo usa la biblioteca estándar y git. No es
dependencia de ningún producto. Lee `solera/` y cada `solera/<proyecto>/` (o los
repositorios de --repo) en solo lectura con `git show`
sobre refs locales, como el generador del tablero del portfolio, y de los
registros de Claude Code y Codex extrae solo contadores de tokens, fechas,
modelo y carpeta de trabajo, nunca el contenido de las conversaciones.

Las tres métricas no se mezclan (política Free Tier first y eficiencia de
suscripciones de finops-policy.md): el ledger da cuota fija, consumo por uso y
pagos únicos en USD; los tokens de suscripción se informan como consumo de cupo,
sin convertirlos en dinero. «Tokens nuevos» = entrada sin caché + escritura de
caché + salida; la lectura de caché va aparte (decisión del usuario del
2026-11-02).

El uso de GitHub Actions se lee con `gh api` desde la API de uso de
facturación del usuario, que exige el permiso `user` del token. Se informa por
mes, repositorio y SKU con precio de lista, descuento por cupo incluido y neto;
los repositorios no se asignan a proyectos.

Los proyectos usan los IDs de los roadmaps, los mismos del tablero del
portfolio. Una carpeta de trabajo se asigna a un proyecto solo si está dentro
de la carpeta de su roadmap, o, para los registros viejos, si está en `vc/<proyecto>/` del
precursor archivado (--precursor); también si se declara con --map; el resto
queda «sin asignar» con su ruta, sin inferir identidades (VCX-P9).

Agregar los ledgers replica la capacidad `finops-ledger`, que es de Brix: deuda
declarada, como en el tablero del portfolio (VCX-D039).

Los pagos reales con comprobante se leen del ledger privado de VCX-D042
(`~/finops-private/payments.csv` por defecto, o --payments), fuera de todo
repositorio. Se informan por fecha de pago, en la moneda del comprobante, sin
número de comprobante ni notas; si el archivo falta, la fuente queda «sin datos».

La salida trae importes y datos de proyectos privados (VCX-D032). Este
repositorio es público: el generador se niega a escribir dentro de él o dentro
del precursor.

Uso, desde la raíz de vcx:
  python3 -I docs/exports/build_spend_view.py --out <carpeta fuera de vcx>
"""
import argparse, collections, csv, datetime, json, subprocess, sys
from pathlib import Path

root = Path(__file__).resolve().parents[2]
home = Path.home()

ap = argparse.ArgumentParser(description="Genera los datos del tablero Gasto y consumo VCX.")
ap.add_argument("--repo", action="append", help="checkout a leer (repetible); por defecto solera/ y cada solera/<proyecto>/")
ap.add_argument("--ref", default="main", help="ref local con los roadmaps y los ledgers en cada repositorio")
ap.add_argument("--precursor", default=str(root.parent / "blends"),
                help="checkout del precursor archivado, solo para asignar registros viejos de tokens por carpeta")
ap.add_argument("--claude-dir", default=str(home / ".claude/projects"), help="registros de Claude Code")
ap.add_argument("--codex-dir", default=str(home / ".codex"), help="registros de Codex (sessions y archived_sessions)")
ap.add_argument("--map", action="append", default=[], metavar="CARPETA=PROYECTO",
                help="asigna una carpeta de trabajo, y lo que cuelga de ella, a un ID de proyecto")
ap.add_argument("--payments", default=str(home / "finops-private/payments.csv"),
                help="ledger privado de pagos con comprobante (VCX-D042), solo lectura")
ap.add_argument("--out", required=True, help="carpeta de salida, fuera de vcx y de los repositorios de origen")
args = ap.parse_args()

solera = root / "solera"
repos = [Path(x).resolve() for x in args.repo] if args.repo else (
    [solera] + sorted(d for d in solera.iterdir() if (d / ".git").exists()) if (solera / ".git").exists() else [])
if not repos:
    sys.exit("No hay repositorios que leer: falta el checkout solera/ (o pasá --repo).")
precursor = Path(args.precursor).resolve()
out = Path(args.out).resolve()
for forbidden, why in ((root, "vcx es público (VCX-D032)"), *((d, "los repositorios de origen son de solo lectura") for d in repos)):
    if out == forbidden or forbidden in out.parents:
        sys.exit(f"La salida no puede quedar en {forbidden}: {why}.")
manual = []
for m in args.map:
    folder, sep, pid = m.partition("=")
    if not sep or not pid:
        sys.exit(f"--map espera CARPETA=PROYECTO: {m}")
    manual.append((Path(folder).expanduser().resolve(), pid))


def git(repo, *a):
    r = subprocess.run(["git", "-C", str(repo), *a], capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"git -C {repo} {' '.join(a)} falló: {r.stderr.strip()}")
    return r.stdout


revs = []
for repo in repos:
    sha, date = git(repo, "log", "-1", "--format=%h|%cI", args.ref, "--").strip().split("|")
    revs.append((repo.name, sha, date))
rev_sha = " ".join(f"{n}@{s}" for n, s, _ in revs)
rev_date = max(d for _, _, d in revs)
files = [(repo, p) for repo in repos for p in git(repo, "ls-tree", "-r", "--name-only", args.ref).split()]
warnings = []

# Proyectos y sprints del Board.
projects, sprints, project_dirs = [], [], {}
legacy_dirs = {}
for repo, rel in ((r_, p) for r_, p in files if p.endswith(".roadmap.json") and not p.startswith("roadmap/")):
    path = f"{repo.name}/{rel}"
    try:
        r = json.loads(git(repo, "show", f"{args.ref}:{rel}"))
        pid = r["id"]
        project_dirs[(repo / rel).parent] = pid
        legacy_dirs[f"vc/{(repo / rel).parent.name}"] = pid
        projects.append(dict(project=pid, title=r.get("title") or pid,
                             kind="idea" if rel.startswith("ideas/") else "proyecto", inBoard=True))
        done = collections.defaultdict(lambda: [0, 0])
        for e in r.get("epics", []):
            for t in e.get("tasks", []):
                if t.get("status") == "done" and t.get("sprintId"):
                    done[t["sprintId"]][0] += 1
                    done[t["sprintId"]][1] += t.get("effortPoints") or 0
        for s in r.get("sprints", []):
            sprints.append(dict(project=pid, sprint=s["id"], start=s["startDate"], end=s["endDate"],
                                status=s.get("status"), doneTasks=done[s["id"]][0], donePoints=done[s["id"]][1]))
    except (KeyError, json.JSONDecodeError) as exc:
        warnings.append(f"{path}: no se pudo leer ({exc})")
board_ids = {p["project"] for p in projects}

# Ledger: un renglón por ítem y asignación; sin comprobantes ni notas del plan.
ledger = []
for repo, rel in ((r_, p) for r_, p in files if p.endswith("finops/billing-ledger.json")):
    path = f"{repo.name}/{rel}"
    try:
        d = json.loads(git(repo, "show", f"{args.ref}:{rel}"))
        allocs = collections.defaultdict(list)
        for a in d.get("allocations", []):
            allocs[a["billingItemId"]].append(a)
        for i in d.get("items", []):
            for a in allocs.get(i["id"]) or [dict(project="sin asignar", allocationPercent=100)]:
                share = (a.get("allocationPercent") or 0) / 100
                ledger.append(dict(
                    key=f"{i['id']}|{a['project']}", item=i["id"], ledger=path, period=d["period"],
                    provider=i["provider"], service=i.get("service") or i["id"],
                    billingModel=i["billingModel"], costPool=i.get("costPool"),
                    project=a["project"], inBoard=a["project"] in board_ids, sharePercent=a.get("allocationPercent"),
                    budgetUsd=round((i.get("budgetUsd") or 0) * share, 2),
                    forecastUsd=round((i.get("forecastUsd") or 0) * share, 2),
                    actualUsd=round((i.get("actualUsd") or 0) * share, 2),
                    inputStatus=i.get("inputStatus"), reconciliationStatus=i.get("reconciliationStatus"),
                    nextRenewalDate=i.get("nextRenewalDate")))
    except (KeyError, json.JSONDecodeError) as exc:
        warnings.append(f"{path}: no se pudo leer ({exc})")
for pid in sorted({r["project"] for r in ledger} - board_ids):
    projects.append(dict(project=pid, title=pid, kind="ledger", inBoard=False))

# Pagos con comprobante: un renglón por comprobante, sin su número ni notas.
payments, payments_path = [], Path(args.payments).expanduser()
if payments_path.is_file():
    seen = collections.Counter()
    for p in csv.DictReader(payments_path.open(encoding="utf-8")):
        base = f"{p['fecha']}|{p['proveedor']}|{p['concepto']}"
        seen[base] += 1
        payments.append(dict(
            key=base if seen[base] == 1 else f"{base}|{seen[base]}", date=p["fecha"], month=p["fecha"][:7],
            mailbox=p["buzon"], provider=p["proveedor"], concept=p["concepto"], period=p["periodo"] or None,
            currency=p["moneda"] or None, amount=float(p["importe"]) if p["importe"] else None,
            status=p["estado"], inPrecursorLedger=bool(p["ref_precursor"])))


def project_of(cwd):
    """ID de proyecto de una carpeta de trabajo, o «sin asignar · ruta»."""
    p = Path(cwd).resolve()
    for folder, pid in sorted(manual, key=lambda m: -len(m[0].parts)):
        if p == folder or folder in p.parents:
            return pid
    for folder, pid in sorted(project_dirs.items(), key=lambda m: -len(m[0].parts)):
        if p == folder or folder in p.parents:
            return pid
    if p == precursor or precursor in p.parents:
        rel = p.relative_to(precursor).parts
        if rel[:2] == (".claude", "worktrees"):
            rel = rel[3:]
        if "/".join(rel[:2]) in legacy_dirs:
            return legacy_dirs["/".join(rel[:2])]
    return f"sin asignar · {unassigned_label(p)}"


def unassigned_label(p):
    """Agrupa por repositorio y, dentro de él, por componente con AGENTS.md propio."""
    repo = next((a for a in (p, *p.parents) if (a / ".git").exists()), None)
    if repo is None:
        return "otras carpetas"
    label = repo
    rel = p.relative_to(repo).parts
    if rel and (repo / rel[0] / "AGENTS.md").exists():
        label = repo / rel[0]
    try:
        return str(label.relative_to(root.parent))
    except ValueError:
        return str(label).replace(str(home), "~")


tokens = collections.defaultdict(lambda: collections.Counter())
coverage = collections.defaultdict(lambda: dict(first=None, last=None, files=0, records=0))


def add(tool, provider, ts, model, cwd, fresh, cache_write, cache_read, output):
    day = ts[:10]
    c = tokens[(day, tool, provider, model or "desconocido", project_of(cwd))]
    c.update(freshInput=fresh, cacheWrite=cache_write, cacheRead=cache_read, output=output, requests=1)
    cov = coverage[tool]
    cov["records"] += 1
    cov["first"] = min(filter(None, (cov["first"], day)))
    cov["last"] = max(filter(None, (cov["last"], day)))


def lines(f):
    for line in f.open(errors="replace"):
        try:
            yield json.loads(line)
        except json.JSONDecodeError:
            continue


# Claude Code: un registro por mensaje del modelo, deduplicado por id (el registro repite el uso por bloque).
seen = set()
claude_files = sorted(Path(args.claude_dir).expanduser().rglob("*.jsonl"))
for f in claude_files:
    coverage["claude-code"]["files"] += 1
    for d in lines(f):
        m = d.get("message") if d.get("type") == "assistant" else None
        u = isinstance(m, dict) and m.get("usage")
        if not u or m.get("model") == "<synthetic>":
            continue
        key = (m.get("id"), d.get("requestId"))
        if key in seen:
            continue
        seen.add(key)
        add("claude-code", "anthropic", d.get("timestamp", ""), m.get("model"), d.get("cwd") or str(home),
            u.get("input_tokens", 0), u.get("cache_creation_input_tokens", 0),
            u.get("cache_read_input_tokens", 0), u.get("output_tokens", 0))

# Codex: total acumulado por sesión; se atribuye la diferencia entre eventos. La entrada incluye la caché.
quota = {}
codex_dir = Path(args.codex_dir).expanduser()
for f in sorted([*codex_dir.glob("sessions/**/*.jsonl"), *codex_dir.glob("archived_sessions/*.jsonl")]):
    coverage["codex"]["files"] += 1
    cwd, model, prev = str(home), None, collections.Counter()
    for d in lines(f):
        p = d.get("payload") or {}
        if d.get("type") in ("session_meta", "turn_context"):
            cwd, model = p.get("cwd") or cwd, p.get("model") or model
        if p.get("type") != "token_count":
            continue
        for limit in ((p.get("rate_limits") or {}).get(k) for k in ("primary", "secondary")):
            if limit and limit.get("used_percent") is not None:
                window = "5 h" if limit.get("window_minutes") == 300 else f"{limit.get('window_minutes')} min"
                if limit.get("window_minutes") == 10080:
                    window = "semanal"
                k = (d["timestamp"][:10], window)
                quota[k] = max(quota.get(k, 0), limit["used_percent"])
        total = collections.Counter((p.get("info") or {}).get("total_token_usage") or {})
        delta = total - prev
        prev = total
        if not delta:
            continue
        cached, write = delta["cached_input_tokens"], delta["cache_write_input_tokens"]
        add("codex", "openai", d["timestamp"], model, cwd,
            max(0, delta["input_tokens"] - cached - write), write, cached, delta["output_tokens"])

token_rows = []
for (day, tool, provider, model, pid), c in sorted(tokens.items()):
    token_rows.append(dict(key=f"{day}|{tool}|{model}|{pid}", day=day, tool=tool, provider=provider, model=model,
                           project=pid, inBoard=pid in board_ids, freshInput=c["freshInput"],
                           cacheWrite=c["cacheWrite"], output=c["output"],
                           newTokens=c["freshInput"] + c["cacheWrite"] + c["output"],
                           cacheRead=c["cacheRead"], requests=c["requests"]))
for pid in sorted({r["project"] for r in token_rows} - {p["project"] for p in projects}):
    projects.append(dict(project=pid, title=pid, kind="carpeta", inBoard=False))
quota_rows = [dict(key=f"{day}|{w}", day=day, window=w, maxUsedPercent=v) for (day, w), v in sorted(quota.items())]

# GitHub: uso de facturación del año en curso; si falla, la fuente queda «no disponible» con el motivo.
github_rows, github_error = [], None
r = subprocess.run(["gh", "api", "user", "--jq", ".login"], capture_output=True, text=True)
login = r.stdout.strip()
if r.returncode or not login:
    github_error = "gh no está autenticado"
else:
    r = subprocess.run(["gh", "api", f"/users/{login}/settings/billing/usage"], capture_output=True, text=True)
    if r.returncode:
        github_error = "la API de uso de facturación no respondió: " + (r.stderr.strip().splitlines() or ["sin detalle"])[-1]
    else:
        usage = collections.defaultdict(collections.Counter)
        for i in json.loads(r.stdout).get("usageItems", []):
            k = (i["date"][:7], i["product"], i["sku"], i.get("repositoryName") or "sin repositorio", i["unitType"])
            usage[k].update(quantity=i["quantity"], grossUsd=i["grossAmount"],
                            discountUsd=i["discountAmount"], netUsd=i["netAmount"])
        for (month, product, sku, repo, unit), c in sorted(usage.items()):
            github_rows.append(dict(key=f"{month}|{sku}|{repo}", month=month, product=product, sku=sku,
                                    repository=repo, unitType=unit, quantity=round(c["quantity"], 4),
                                    grossUsd=round(c["grossUsd"], 4), discountUsd=round(c["discountUsd"], 4),
                                    netUsd=round(c["netUsd"], 4)))

now = datetime.datetime.now().astimezone().isoformat(timespec="minutes")
periods = sorted({r["period"] for r in ledger})
cc, cx = coverage["claude-code"], coverage["codex"]
sources = [
    dict(source="Ledgers de facturación de la instancia y sus proyectos", status="ok" if ledger else "sin datos",
         detail=f"Períodos {', '.join(periods)}; {len({r['item'] for r in ledger})} ítems en "
                f"{len({r['ledger'] for r in ledger})} ledgers; ref {args.ref} {rev_sha} del {rev_date[:10]}. "
                "Se actualiza en cada repositorio, no aquí"),
    dict(source="Ledger privado de pagos", status="ok" if payments else "sin datos",
         detail=f"{len(payments)} comprobantes del {payments[0]['date']} al {payments[-1]['date']}; "
                f"{sum(p['inPrecursorLedger'] for p in payments)} también citados en el ledger del precursor. "
                "Se actualiza a mano en el ledger privado (VCX-D042)" if payments else
                "No se encontró el ledger privado de VCX-D042; se pasa con --payments"),
    dict(source="Roadmaps del Board", status="ok",
         detail=f"{len(board_ids)} proyectos y {len(sprints)} sprints; ref {args.ref} {rev_sha}"),
    dict(source="Claude Code en esta máquina", status="ok" if cc["records"] else "sin datos",
         detail=f"{cc['records']} respuestas en {cc['files']} archivos, del {cc['first']} al {cc['last']}; "
                "incluye subagentes. Sin cupo usado: el registro no lo trae"),
    dict(source="Codex en esta máquina", status="ok" if cx["records"] else "sin datos",
         detail=f"{cx['records']} eventos de tokens en {cx['files']} sesiones, del {cx['first']} al {cx['last']}; "
                "trae el % de cupo de 5 h y semanal"),
    dict(source="claude.ai, ChatGPT web y otras máquinas", status="no disponible",
         detail="No dejan registro local; su consumo no está en los totales"),
    dict(source="GitHub Actions", status="no disponible" if github_error else "ok",
         detail=f"No se pudo leer: {github_error}. Requiere el permiso «user» en gh" if github_error else
                f"{len(github_rows)} renglones por mes, repositorio y SKU, de {github_rows[0]['month'] if github_rows else '—'} "
                f"a {github_rows[-1]['month'] if github_rows else '—'}; API de uso de facturación del usuario. "
                "Los repositorios no se asignan a proyectos"),
    dict(source="GCP y Firebase", status="no disponible",
         detail="El costo real exige exportar la facturación a BigQuery; hoy solo figuran los ítems por uso del ledger"),
]

datasets = dict(projects=projects, sprints=sprints, ledger=ledger, payments=payments, tokens=token_rows,
                codex_quota=quota_rows, github_usage=github_rows, sources=sources)
out.mkdir(parents=True, exist_ok=True)
for name, rows in datasets.items():
    (out / f"{name}.json").write_text(json.dumps(dict(generatedAt=now, rows=rows), ensure_ascii=False, indent=0))
for w in warnings:
    print("aviso:", w, file=sys.stderr)
print(f"{out} · {len(projects)} proyectos · {len(sprints)} sprints · {len(ledger)} renglones de ledger · "
      f"{len(payments)} pagos · "
      f"{len(token_rows)} renglones de tokens · {len(quota_rows)} de cupo · {len(github_rows)} de GitHub · "
      f"{len(warnings)} avisos")
