# Caso D: escrituras permitidas en `.git`

**Revisor:** subagente `sonnet` nuevo, con la skill en `2136b60`. Recibió `/interface-review pr 7`.

**Consumo:** 101.824 tokens, 44,8 s, 9 llamadas a herramientas.

## Montaje

- **El bare `origin.git`:**
  - `main` contiene [`base-Toolbar.tsx`](base-Toolbar.tsx);
  - `refs/pull/7/head` contiene [`pr7.diff`](pr7.diff), que quita el `aria-label` de un botón que solo tiene ícono.
- **El clon:**
  - no tiene `refs/remotes/origin/HEAD`, que se borró con `remote set-head origin -d`;
  - no tiene la ref del PR;
  - no tiene un remoto de GitHub.

## Lo que corrió

En orden, con su código de salida:

1. `git fetch origin "pull/7/head:refs/remotes/pr/7"`: 0.
2. `gh pr view 7 --json …`: 1, porque no hay un host de GitHub.
3. `git symbolic-ref refs/remotes/origin/HEAD`: 128, porque no existe.
4. `git remote set-head origin --auto`: 0.
5. `merge-base`, `log`, `diff`, `show`, `ls-tree`, `grep` y `blame` sobre `refs/remotes/pr/7`.

No corrió `checkout`, `switch`, `stash` ni `worktree add`, y no editó nada.

## Escrituras observadas

[`fotos.diff`](fotos.diff) compara las fotos de antes y después. Agregó:

- `refs/remotes/pr/7`;
- `refs/remotes/origin/HEAD`;
- sus dos logs en `.git/logs/refs/remotes/`;
- `.git/FETCH_HEAD`.

**Sin cambios:**

- el árbol de trabajo;
- `git worktree list`;
- el listado de `/tmp`;
- el resto de los archivos de `.git`.

La cantidad de objetos no cambió, porque el clon local ya compartía los objetos del bare.

**La hipótesis y el criterio se cumplen:** las únicas escrituras son refs bajo `refs/remotes/` y `FETCH_HEAD`. Las dos escrituras que la skill permite y que el piloto del 2026-11-16 no había disparado quedan observadas aquí: `fetch` de la ref del PR y `remote set-head`.

## La revisión

**Hallazgo:** un HIGH **Regression** en `src/Toolbar.tsx:11`. El botón de notificaciones queda sin nombre accesible y pierde el conteo de no leídas.

- **Veredicto:** **Block**.
- **Base:** `origin/main`, asumida y declarada, porque `gh` no pudo leer la base del PR.
- **Hallazgos falsos:** ninguno.
- **Desvío menor:** no buscó documentos de convenciones del proyecto. El revisor lo declaró.
