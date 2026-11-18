#!/bin/sh
# Foto del estado de un repositorio de prueba. Uso: snap.sh <repo> <salida>
d=$1; out=$2
{
  echo "## refs"; git -C "$d" for-each-ref --format='%(refname) %(objectname:short)'
  echo "## status"; git -C "$d" status --porcelain --untracked-files=all
  echo "## worktrees"; git -C "$d" worktree list
  echo "## git-files"; (cd "$d/.git" && find . -type f ! -path './objects/*' | sort | while read f; do shasum -a 256 "$f"; done)
  echo "## objects"; find "$d/.git/objects" -type f | wc -l
  echo "## worktree-files"; (cd "$d" && find . -path ./.git -prune -o -type f -print | sort | while read f; do shasum -a 256 "$f"; done)
  echo "## tmp"; ls -a /tmp /private/tmp | sort | shasum -a 256
} > "$out" 2>&1
