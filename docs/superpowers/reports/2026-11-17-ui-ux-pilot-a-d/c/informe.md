# Caso C: el caso 8 en `2136b60`

**Revisor:** subagente `sonnet` nuevo, con la skill leída del clon en `2136b60`. Recibió `/interface-review` sin objetivo, y nada sobre los defectos.

**Consumo:** 106.181 tokens, 54,6 s, 12 llamadas a herramientas.

**Montaje:** el mismo del 2026-11-16. La base es [`../../2026-11-16-interface-review-pilot/fixtures/c8-base-LeagueHeader.tsx`](../../2026-11-16-interface-review-pilot/fixtures/c8-base-LeagueHeader.tsx) y el cambio, [`c8.diff`](c8.diff), en la rama `header-favorito`. El `origin` es un bare local.

## Resultado

| Defecto plantado | Esperado | Observado |
|---|---|---|
| `aria-label` quitado del botón de compartir | `Regression` | HIGH **Regression**, `src/LeagueHeader.tsx:17` |
| `<div onClick>` agregado | `Introduced` | HIGH **Introduced**, `:16`. Agrupa rol, foco, teclado, nombre y estado por causa |
| `<img>` sin `alt`, ya en la base | `Pre-existing` | MEDIUM **Pre-existing**, `:14`, confirmado con `git blame` |

- **Veredicto:** **Block**, como se esperaba.
- **Hallazgos falsos:** ninguno.
- **Dominios:** Layout, Typography y Colors quedaron como «Not reviewed», por falta de CSS. UI quedó como «Clear» para el diff, con los estados ausentes incluidos en el hallazgo 2.

**3 de 3 detectados y 3 de 3 bien clasificados: el resultado se transfiere a `2136b60`.**

## Comandos y escrituras

**Comandos declarados:** `status`, `branch`, `log`, `merge-base`, `rev-parse`, `diff`, `ls-files`, `show`, `grep` y `blame`. No corrió `fetch`, `gh` ni el pipeline de `removed-signals`: leyó el lado `-` del diff completo, que tenía un solo hunk.

**Desvío menor:** su bucle sobre `rev-parse --git-path` imprime las rutas sin comprobar que existan, así que no prueba que no hubiera un rebase o un merge en curso. El propio revisor lo declaró.

**Fotos de antes y después:** idénticas. No hubo refs nuevas ni cambios en `.git`, en el árbol de trabajo ni en `/tmp`. Ver [`fotos.diff`](fotos.diff), que está vacío.

**Archivos de la skill leídos:**

- `interface-review`: `SKILL.md`, `scope-resolution.md` y `removed-signals.md`;
- `better-interface`: `SKILL.md` y `review-format.md`;
- `better-accessibility`: `SKILL.md`, `semantics-and-aria.md` y `hit-areas.md`;
- `better-writing`: las primeras 60 líneas.
