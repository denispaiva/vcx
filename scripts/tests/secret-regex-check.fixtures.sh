#!/bin/bash
# Pruebas con fixtures sintéticos del script secret-regex-check.py.
# Los valores se generan al azar en cada corrida: no son credenciales reales.
set -u
S="$(cd "$(dirname "$0")/.." && pwd)/secret-regex-check.py"
W="$(mktemp -d "${TMPDIR:-/tmp}/srx-fixtures.XXXXXX")"
pass=0; fail=0
check() { # nombre, esperado, obtenido
  if [ "$2" = "$3" ]; then echo "PASS $1 (exit $3)"; pass=$((pass+1)); else echo "FAIL $1: esperado $2, obtenido $3"; fail=$((fail+1)); fi
}
rand() { LC_ALL=C tr -dc 'A-Za-z0-9' </dev/urandom | head -c "$1"; }
GH="ghp_$(rand 36)"; AK="AKIA$(LC_ALL=C tr -dc 'A-Z0-9' </dev/urandom | head -c 16)"
ANT="sk-ant-$(rand 40)"; SLK="xoxb-$(rand 24)"

cd "$W" && git init -q repo && cd repo && git config user.email f@x.test && git config user.name fx
echo "# documento limpio" > README.md && git add . && git commit -qm init

# 1. Repositorio limpio: 0 en los tres ámbitos.
python3 -I "$S" --repo . --worktree >/dev/null; check "limpio worktree" 0 $?
python3 -I "$S" --repo . --history  >/dev/null; check "limpio history" 0 $?
python3 -I "$S" --repo . --staged   >/dev/null; check "limpio staged (índice vacío)" 0 $?

# 2. Secreto preparado en un archivo con espacios y acentos: hallazgo, sin filtración.
printf 'token = "%s"\n' "$GH" > "config año ñ.txt"; git add "config año ñ.txt"
out=$(python3 -I "$S" --repo . --staged); rc=$?; check "staged hallazgo" 1 $rc
case "$out" in *"$GH"*) echo "FAIL filtración: el valor aparece en la salida"; fail=$((fail+1));; *) echo "PASS sin filtración staged"; pass=$((pass+1));; esac
echo "$out" | grep -q "^FINDING.github-token.index:config año ñ.txt" && { echo "PASS regla y ruta con espacios/acentos"; pass=$((pass+1)); } || { echo "FAIL formato: $out"; fail=$((fail+1)); }
# El secreto entra al historial y luego se borra: history lo sigue viendo, worktree no.
git commit -qm "agrega config"; git rm -q "config año ñ.txt"; git commit -qm "quita config"
python3 -I "$S" --repo . --worktree >/dev/null; check "worktree tras borrar" 0 $?
out=$(python3 -I "$S" --repo . --history); rc=$?; check "history conserva el hallazgo" 1 $rc
case "$out" in *"$GH"*) echo "FAIL filtración history"; fail=$((fail+1));; *) echo "PASS sin filtración history"; pass=$((pass+1));; esac

# 3. Varias reglas en el árbol de trabajo, en un archivo rastreado.
# La cabecera de clave privada se arma en tiempo de ejecución: escrita literal, este archivo
# dispararía la compuerta al commitearlo, y eximirla por huella eximiría toda cabecera igual.
{ echo "aws: $AK"; echo "anthropic: $ANT"; echo "slack: $SLK"; printf -- "-----BEGIN %s PRIVATE KEY-----\n" OPENSSH; echo "ZmFrZQ=="; printf -- "-----END %s PRIVATE KEY-----\n" OPENSSH; } > multi.txt
git add multi.txt
out=$(python3 -I "$S" --repo . --worktree); rc=$?; check "worktree multi" 1 $rc
n=$(echo "$out" | grep -c '^FINDING'); [ "$n" -eq 4 ] && { echo "PASS 4 hallazgos (aws, anthropic, slack, private-key)"; pass=$((pass+1)); } || { echo "FAIL hallazgos=$n"; echo "$out"; fail=$((fail+1)); }

# 4. Excepción por huella: suprime solo ese valor y esa regla.
fp=$(printf '%s' "$AK" | shasum -a 256 | cut -c1-64)
printf '%s aws-access-key-id ejemplo sintético de fixture, revisado 2026-11-02\n' "$fp" > allow.txt
out=$(python3 -I "$S" --repo . --worktree --allow allow.txt); rc=$?; check "allow reduce a 3" 1 $rc
echo "$out" | grep -q '^ALLOWED.aws-access-key-id' && { echo "PASS excepción registrada como ALLOWED"; pass=$((pass+1)); } || { echo "FAIL sin ALLOWED"; fail=$((fail+1)); }
printf 'no-es-sha regla x\n' > bad-allow.txt
python3 -I "$S" --repo . --worktree --allow bad-allow.txt >/dev/null 2>&1; check "allow malformado es error operativo" 2 $?
git rm -q --cached multi.txt; rm multi.txt

# 5. Archivo sobre el límite de tamaño: análisis parcial, nunca éxito.
head -c 1100000 /dev/zero | tr '\0' 'a' > big.txt; git add big.txt
python3 -I "$S" --repo . --staged >/dev/null; check "archivo grande => parcial (3)" 3 $?
git rm -q --cached big.txt; rm big.txt

# 6. Binario: omitido por diseño, resultado limpio.
printf 'PK\0\0%s' "$GH" > bin.dat; git add bin.dat
python3 -I "$S" --repo . --staged >/dev/null; check "binario omitido (declarado fuera de alcance)" 0 $?
git rm -q --cached bin.dat; rm bin.dat

# 7. Errores operativos: ruta que no es repositorio, flags inválidos.
python3 -I "$S" --repo "$W" --worktree >/dev/null 2>&1; check "no repo => 2" 2 $?
python3 -I "$S" --repo . >/dev/null 2>&1; rc=$?; [ $rc -ne 0 ] && { echo "PASS sin modo => error ($rc)"; pass=$((pass+1)); } || { echo "FAIL sin modo => 0"; fail=$((fail+1)); }

echo "RESULTADO: $pass pasaron, $fail fallaron"
rm -rf "$W"
[ $fail -eq 0 ]
