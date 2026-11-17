#!/bin/bash
# Fixtures locales de health.py: repositorios desechables, sin red ni configuración del usuario.
set -eu
S="$(cd "$(dirname "$0")/.." && pwd)/health.py"
W="$(mktemp -d "${TMPDIR:-/tmp}/health-fixtures.XXXXXX")"
trap 'chmod -R u+rwX "$W"; rm -rf "$W"' EXIT
export GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL=/dev/null GIT_TERMINAL_PROMPT=0
unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE GIT_COMMON_DIR GIT_CONFIG_COUNT || true
pass=0; fail=0
ok()   { echo "PASS $1"; pass=$((pass+1)); }
bad()  { echo "FAIL $1"; fail=$((fail+1)); }
code() { if [ "$2" = "$3" ]; then ok "$1 (exit $3)"; else bad "$1: esperado exit $2, obtenido $3"; fi; }
has()  { case "$2" in *"$3"*) ok "$1";; *) bad "$1: falta «$3» en: $2";; esac; }
hasnt(){ case "$2" in *"$3"*) bad "$1: sobra «$3» en: $2";; *) ok "$1";; esac; }
run()  { rc=0; out=$(python3 -I "$S" --root "$R" "$@" 2>&1) || rc=$?; }
repo() {
  mkdir -p "$1/.githooks"
  git -C "$1" init -q
  git -C "$1" config user.email fixture@example.test
  git -C "$1" config user.name fixture
  git -C "$1" config commit.gpgsign false
  git -C "$1" config core.hooksPath .githooks
  git -C "$1" remote add origin "https://github.com/denispaiva/$2.git"
}
workspace() {
  R="$W/$1"
  repo "$R" vcx
  printf '/blends/\n/solera/\n' > "$R/.gitignore"
  {
    printf '# Instrucciones\n\n## Principios\n\nVersión documental: `1.1.0`.\n\n'
    for n in 1 2 3 4 5 6 7 8 9; do printf '%s. **VCX-P%s · Principio.** Texto %s.\n\n' "$n" "$n" "$n"; done
    printf 'Adopción y procedencia: fixture.\n'
  } > "$R/AGENTS.md"
  git -C "$R" add AGENTS.md .gitignore
  git -C "$R" commit -qm fixture
  sha=$(git -C "$R" rev-parse HEAD)
  for rel in blends solera solera/sample; do
    case "$rel" in solera/sample) name=solera-sample;; *) name=$rel;; esac
    repo "$R/$rel" "$name"
    python3 -I - "$R/AGENTS.md" "$R/$rel/AGENTS.md" "$sha" <<'PY'
from pathlib import Path
import sys
source, target, sha = sys.argv[1:]
origin = f'Copia derivada de `AGENTS.md` de [VCX](https://github.com/denispaiva/vcx/blob/{sha}/AGENTS.md), revisión `{sha[:7]}`.\n\n'
Path(target).write_text(Path(source).read_text().replace('Versión documental:', origin + 'Versión documental:'))
PY
  done
  printf '# Checkouts de proyectos\n/sample/\n/*-wt-*/\n!/docs/\n' > "$R/solera/.gitignore"
  mkdir -p "$R/blends/vendor" "$R/docs/decisions"
  printf 'tarball fixture\n' > "$R/blends/vendor/sample.tgz"
  hash=$(python3 -I -c 'import hashlib,sys; print(hashlib.sha256(open(sys.argv[1],"rb").read()).hexdigest())' "$R/blends/vendor/sample.tgz")
  printf '# Procedencia\n\n## `sample.tgz`\n\n- **sha256:** `%s`.\n' "$hash" > "$R/blends/vendor/procedencia.md"
}

workspace clean
run; code 'workspace limpio' 0 "$rc"; has 'principios comprobados' "$out" 'PRIN-TEXT'; has 'resumen limpio' "$out" '0 errores, 0 avisos'; has 'límites explícitos' "$out" 'no comprueba funcionamiento'
run --json
code 'JSON limpio' 0 "$rc"
if printf '%s' "$out" | python3 -I -c 'import json,sys; d=json.load(sys.stdin); assert d["summary"]["error"] == d["summary"]["warning"] == 0; assert len([f for f in d["findings"] if f["code"] == "PRIN-TEXT"]) == 3; assert all(set(f) == {"code","severity","repository","path","detail"} for f in d["findings"])'; then ok 'contrato JSON y tres copias'; else bad 'contrato JSON'; fi
# HEAD es la fuente, aunque el archivo raíz tenga cambios sin commit.
printf '\nCambio local fuera de los principios.\n' >> "$R/AGENTS.md"
python3 -I - "$R/AGENTS.md" <<'PY'
from pathlib import Path
import sys
p=Path(sys.argv[1]); p.write_text(p.read_text().replace('Texto 1.', 'Texto local.'))
PY
run --only PRIN-TEXT; code 'fuente raíz en HEAD' 0 "$rc"

workspace text
python3 -I - "$R/blends/AGENTS.md" <<'PY'
from pathlib import Path
import sys
p=Path(sys.argv[1]); p.write_text(p.read_text().replace('Texto 1.', 'Texto cambiado.'))
PY
run --only PRIN-TEXT; code 'PRIN-TEXT distinto' 1 "$rc"; has 'código PRIN-TEXT' "$out" 'PRIN-TEXT error'; has 'hash esperado y obtenido' "$out" 'esperado='
run --only TOPO-REMOTE; code 'only no ejecuta otros chequeos' 0 "$rc"; hasnt 'only filtra salida' "$out" 'PRIN-TEXT'
run --only NO-EXISTE; code 'código desconocido' 2 "$rc"

workspace origin
python3 -I - "$R/blends/AGENTS.md" "$sha" <<'PY'
from pathlib import Path
import sys
p=Path(sys.argv[1]); p.write_text(p.read_text().replace(sys.argv[2], 'f'*40).replace(sys.argv[2][:7], 'f'*7))
PY
run --only PRIN-ORIGIN; code 'PRIN-ORIGIN inexistente' 1 "$rc"; has 'código PRIN-ORIGIN' "$out" 'PRIN-ORIGIN error'
# Una versión sin SHA avisa; un SHA de otra sección no suple la procedencia.
cp "$R/AGENTS.md" "$R/blends/AGENTS.md"
printf '\n## Otra copia\nhttps://github.com/denispaiva/solera/blob/%s/AGENTS.md\n' "$sha" >> "$R/blends/AGENTS.md"
run --only PRIN-ORIGIN; code 'origen sin SHA' 0 "$rc"; has 'origen es aviso' "$out" 'PRIN-ORIGIN warning'

workspace vendor
printf 'alterado\n' >> "$R/blends/vendor/sample.tgz"
run --only VEND-HASH; code 'VEND-HASH distinto' 1 "$rc"; has 'código VEND-HASH' "$out" 'VEND-HASH error'
rm "$R/blends/vendor/procedencia.md"
run --only VEND-HASH; code 'procedencia ausente' 1 "$rc"
printf '# Formato desconocido\n' > "$R/blends/vendor/procedencia.md"
run --only VEND-HASH; code 'procedencia no parseable' 2 "$rc"
printf '## `other.tgz`\n- **sha256:** `%s`.\n' "$hash" > "$R/blends/vendor/procedencia.md"
run --only VEND-HASH; code 'tarball sin entrada' 1 "$rc"
# Formato de encabezado compartido con hashes por nombre.
printf '## `sample.tgz` y `other.tgz`\n- **sha256:**\n  - `sample.tgz`: `%s`\n  - `other.tgz`: `%s`\n' "$hash" "$hash" > "$R/blends/vendor/procedencia.md"
printf 'tarball fixture\n' > "$R/blends/vendor/sample.tgz"
run --only VEND-HASH; code 'procedencia con dos nombres' 0 "$rc"

workspace remote
git -C "$R/blends" remote set-url origin https://github.com/other/blends.git
run --only TOPO-REMOTE; code 'TOPO-REMOTE incorrecto' 1 "$rc"; has 'código TOPO-REMOTE' "$out" 'TOPO-REMOTE error'
git -C "$R/blends" remote set-url origin git@github.com:denispaiva/blends.git
run --only TOPO-REMOTE; code 'remoto SSH correcto' 0 "$rc"

workspace hooks
git -C "$R/blends" config --unset core.hooksPath
run --only TOPO-HOOKS; code 'hooks ausentes' 0 "$rc"; has 'hooks aviso' "$out" 'TOPO-HOOKS warning'
git -C "$R/blends" config core.hooksPath missing
run --only TOPO-HOOKS; code 'TOPO-HOOKS inexistente' 1 "$rc"; has 'hooks error' "$out" 'TOPO-HOOKS error'

workspace absent
rm -rf "$R/blends"
run; code 'checkout ausente' 0 "$rc"; has 'TOPO-ABSENT aviso' "$out" 'TOPO-ABSENT warning'
rm -rf "$R/solera"
run; code 'Solera ausente no exige su gitignore' 0 "$rc"

workspace undeclared
repo "$R/extra" extra
repo "$R/solera/extra-project" solera-extra-project
run --only TOPO-UNDECLARED; code 'TOPO-UNDECLARED' 1 "$rc"; has 'repo raíz no declarado' "$out" 'extra/.git'; has 'proyecto no declarado' "$out" 'solera/extra-project/.git'

workspace worktree
# Un worktree cubierto por /*-wt-*/ está declarado por comodín: ni error ni repo del inventario.
git -C "$R/solera/sample" commit -q --allow-empty -m base
git -C "$R/solera/sample" worktree add -q "$R/solera/sample-wt-activa"
run --only TOPO-UNDECLARED; code 'worktree cubierto por comodín' 0 "$rc"; hasnt 'worktree no es error' "$out" 'sample-wt-activa'
run --only TOPO-REMOTE; hasnt 'comodín no suma repos al inventario' "$out" 'sample-wt-activa'

workspace environment
rm -rf "$R/blends/.git"; printf 'gitdir: missing\n' > "$R/blends/.git"
run; code 'ENV checkout inválido' 1 "$rc"; has 'código ENV' "$out" 'ENV error'; has 'continúa con otras copias' "$out" 'solera/sample'

workspace pending
printf '{"schemaVersion":1,"items":[{"id":"fixture-due","decision":"DTEST","title":"Revisar fixture","reviewAt":"2000-01-01"}]}' > "$R/docs/decisions/pending-triggers.json"
run --only PEND; code 'PEND aviso' 0 "$rc"; has 'código PEND' "$out" 'PEND warning'; has 'salida del recordatorio' "$out" 'fixture-due'
has 'encabezado PEND no cuenta como aviso' "$out" '0 errores, 1 avisos'
printf '{' > "$R/docs/decisions/pending-triggers.json"
run --only PEND; code 'PEND datos inválidos' 2 "$rc"

workspace unreadable
chmod 000 "$R/.gitignore"
run; code 'gitignore ilegible' 2 "$rc"; has 'ruta ilegible' "$out" '.gitignore'
chmod 600 "$R/.gitignore"
printf '\377' > "$R/.gitignore"
run; code 'gitignore UTF-8 inválido' 2 "$rc"

workspace malformed
printf '# Principios con formato cambiado\n' > "$R/blends/AGENTS.md"
run --only PRIN-TEXT; code 'bloque no parseable' 2 "$rc"
# CRLF se normaliza, sin normalizar otros espacios del contenido.
cp "$R/solera/AGENTS.md" "$R/blends/AGENTS.md"
python3 -I - "$R/blends/AGENTS.md" <<'PY'
from pathlib import Path
import sys
p=Path(sys.argv[1]); p.write_bytes(p.read_bytes().replace(b'\n', b'\r\n'))
PY
run --only PRIN-TEXT,PRIN-ORIGIN; code 'CRLF y selección múltiple' 0 "$rc"

echo "--- $pass PASS, $fail FAIL"
[ "$fail" -eq 0 ]
