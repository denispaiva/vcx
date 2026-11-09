#!/bin/bash
# Pruebas con fixtures del recordatorio scripts/pending_triggers.py (VCX-D058).
# Cada caso arma un repositorio desechable con sus propias fuentes y fija la fecha con --today.
set -u
S="$(cd "$(dirname "$0")/.." && pwd)/pending_triggers.py"
W="$(mktemp -d "${TMPDIR:-/tmp}/pending-fixtures.XXXXXX")"
pass=0; fail=0
ok()   { echo "PASS $1"; pass=$((pass+1)); }
bad()  { echo "FAIL $1"; fail=$((fail+1)); }
code() { [ "$2" = "$3" ] && ok "$1 (exit $3)" || bad "$1: esperado exit $2, obtenido $3"; }
has()  { case "$2" in *"$3"*) ok "$1";; *) bad "$1: falta «$3» en: $2";; esac; }
hasnt(){ case "$2" in *"$3"*) bad "$1: sobra «$3» en: $2";; *) ok "$1";; esac; }
run()  { python3 -I "$S" --root "$R" "$@" 2>&1; }

newrepo() {
  R="$W/$1"; mkdir -p "$R/docs/decisions" "$R/brix/tooling/evaluations"
  git -C "$R" init -q && git -C "$R" config user.email f@x.test && git -C "$R" config user.name fx
}
triggers() { printf '%s' "$1" > "$R/docs/decisions/pending-triggers.json"; }
ITEM='{"schemaVersion":1,"items":[{"id":"cfg","decision":"VCX-DTEST","title":"Revisar configuración","paths":["**/.claude/settings*.json","docs/*.md"],"reviewAt":"2026-12-09"}]}'

# 1. Sin fuentes: nada que avisar.
newrepo vacio
out=$(run --today 2026-11-09); code "sin fuentes" 0 $?; [ -z "$out" ] && ok "sin fuentes, sin salida" || bad "sin fuentes con salida: $out"

# 2. Datos inválidos: exit 2 con diagnóstico, nunca un silencio que parezca limpio.
newrepo invalido
triggers '{"schemaVersion":1,"items":[' ; out=$(run --today 2026-11-09); code "JSON roto" 2 $?; has "JSON roto nombra el archivo" "$out" "pending-triggers.json"
triggers '{"schemaVersion":2,"items":[]}'; run --today 2026-11-09 >/dev/null; code "schemaVersion desconocida" 2 $?
triggers '{"schemaVersion":1,"items":[{"id":"x","decision":"D","title":"T"}]}'; out=$(run --today 2026-11-09); code "falta reviewAt" 2 $?; has "nombra el campo" "$out" "reviewAt"
triggers '{"schemaVersion":1,"items":[{"id":"x","decision":"D","title":"T","reviewAt":"2026-13-40"}]}'; run --today 2026-11-09 >/dev/null; code "fecha imposible" 2 $?
triggers '{"schemaVersion":1,"items":[{"id":"x","decision":"D","title":"T","reviewAt":"2026-12-09"},{"id":"x","decision":"D","title":"T","reviewAt":"2026-12-09"}]}'; run --today 2026-11-09 >/dev/null; code "id repetido" 2 $?
triggers '{"schemaVersion":1,"items":[{"id":"x","decision":"D","title":"T","reviewAt":"2026-12-09","paths":"docs/*.md"}]}'; run --today 2026-11-09 >/dev/null; code "paths no es lista" 2 $?

# 3. Globs: ** cruza carpetas e incluye la raíz; * no cruza carpetas.
newrepo globs; triggers "$ITEM"
out=$(run --today 2026-11-09 --window 0 --paths .claude/settings.json); has "settings en la raíz dispara" "$out" "DISPARO"
out=$(run --today 2026-11-09 --window 0 --paths a/b/.claude/settings.local.json); has "settings anidado dispara" "$out" "DISPARO"
out=$(run --today 2026-11-09 --window 0 --paths docs/a/b.md .claude/other.json xclaude/settings.json); [ -z "$out" ] && ok "* no cruza carpetas y no hay coincidencias falsas" || bad "coincidencia falsa: $out"

# 4. Fechas: vencida, hoy, próxima dentro de la ventana, fuera de ella y ventana 0.
out=$(run --today 2026-12-10); has "vencida" "$out" "hace 1 día)"
out=$(run --today 2026-12-09); has "vence hoy" "$out" "vence hoy"
out=$(run --today 2026-11-30); has "próxima en ventana" "$out" "en 9 días"
out=$(run --today 2026-11-09); [ -z "$out" ] && ok "fuera de la ventana no avisa" || bad "avisó fuera de ventana: $out"
out=$(run --today 2026-11-30 --window 0); [ -z "$out" ] && ok "ventana 0 calla las próximas" || bad "ventana 0: $out"

# 5. Evaluaciones de tooling: se leen reviewAt y expiresAt; sin fechas no aparecen.
newrepo tooling
printf '%s' '{"candidate":{"id":"skill-a"},"expiresAt":"2027-01-31T00:50:00.000Z","humanDecision":{"status":"approved_with_exception","reviewAt":"2026-12-02"}}' > "$R/brix/tooling/evaluations/skill-a.evaluation.json"
printf '%s' '{"candidate":{"id":"skill-b"},"humanDecision":{"status":"rejected"}}' > "$R/brix/tooling/evaluations/skill-b.evaluation.json"
out=$(run --today 2026-12-03); has "revisión de tooling vencida" "$out" "tooling:skill-a"; has "con su estado" "$out" "approved_with_exception"; hasnt "sin fechas no aparece" "$out" "skill-b"
out=$(run --today 2027-02-01); has "expiresAt vencido" "$out" "vencimiento vencida el 2027-01-31"
printf '%s' '{"candidate":{"id":"skill-c"},"expiresAt":"mañana"}' > "$R/brix/tooling/evaluations/skill-c.evaluation.json"
run --today 2026-12-03 >/dev/null; code "expiresAt inválido" 2 $?

# 6. Modo --staged en un repositorio real, con espacios y acentos en la ruta.
newrepo staged; triggers "$ITEM"
echo x > "$R/README.md"; git -C "$R" add README.md docs && git -C "$R" commit -qm init
out=$(cd "$R" && python3 -I "$S" --staged --today 2026-11-09 --window 0 2>&1); [ -z "$out" ] && ok "staged sin cambios disparadores" || bad "staged vacío: $out"
mkdir -p "$R/sub año/.claude"; echo '{}' > "$R/sub año/.claude/settings.json"; git -C "$R" add -A
out=$(cd "$R" && python3 -I "$S" --staged --today 2026-11-09 --window 0 2>&1); code "staged con disparo sale 0" 0 $?; has "staged ruta con espacios y acentos" "$out" "sub año/.claude/settings.json"

# 7. Modo --range y salida de GitHub Actions con resumen.
git -C "$R" commit -qm cfg
SUM="$W/summary.md"; : > "$SUM"
out=$(cd "$R" && GITHUB_STEP_SUMMARY="$SUM" python3 -I "$S" --range HEAD~1...HEAD --today 2026-11-09 --window 0 --github 2>&1)
has "range dispara" "$out" "::warning title=Pendiente disparo: cfg::"
grep -q '| disparo | `cfg`' "$SUM" && ok "resumen del job escrito" || bad "resumen: $(cat "$SUM")"
triggers '{"schemaVersion":1,"items":['; out=$(cd "$R" && python3 -I "$S" --range HEAD~1...HEAD --github 2>&1); code "github con datos inválidos" 2 $?; has "anotación de error" "$out" "::error title=Pendientes con disparador::"

rm -rf "$W"
echo "--- $pass PASS, $fail FAIL"
[ "$fail" -eq 0 ]
