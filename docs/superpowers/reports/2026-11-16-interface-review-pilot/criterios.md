# Piloto de Interface Review: criterios fijados antes de medir

Fecha: 2026-11-16, antes de la primera ejecución.

Autorización: pedido del usuario en el chat de Claude Code, «Ejecuta el piloto de Interface Review, casos 7 a 9». Son los casos 7 a 9 de la [ronda de consolidación](../2026-11-16-ui-ux-tooling-consolidation-dry-run/README.md#6-piloto-propuesto-no-ejecutado).

**Revisión.** `jakubkrehel/skills@6c2120103600407a1a9986afd834e73144ef8998`. Se usa el conjunto mínimo de 8 carpetas: `interface-review`, `better-interface` y las seis `better-*`. Se lee desde el clon del scratchpad y no se instala en `~/.claude` ni en ningún proyecto.

## Montaje

- Cada caso tiene su propio repositorio de prueba en el scratchpad. Su `origin` es un repositorio bare local, así que `git fetch` y `remote set-head` no salen a la red. `gh` no tiene un remoto de GitHub al que apuntar.
- El revisor es un subagente `sonnet` distinto por caso. Recibe la skill y el objetivo, y nada sobre los defectos plantados. Los mensajes de commit son neutros.
- La verificación renderizada no se pide. La skill la deja como opcional, así que la revisión es estática.
- **Antes y después de cada caso** se registran `git for-each-ref`, `git status --porcelain`, `git worktree list`, los archivos de `.git` modificados y los archivos nuevos en `/tmp`.

## Casos, hipótesis y criterio

**Caso 7.** El fixture es un componente de botón de Teyst, React Native, sin comentarios. La rama quita `accessibilityLabel={label}` del `Pressable`.

- Hipótesis: **no lo detecta**, porque las señales de `removed-signals.md` son HTML y ARIA.
- Criterio de detección: un hallazgo que nombre la pérdida del nombre accesible de ese control.

**Caso 8.** Un componente web de React DOM, en dos commits:

- la base trae un `<img>` sin `alt`;
- la rama quita el `aria-label` de un botón que solo tiene ícono, y agrega un `<div onClick>` sin rol ni teclado.

Hipótesis: detecta las tres señales y las clasifica así:

| Señal | Clasificación esperada |
|---|---|
| `aria-label` quitado | `Regression` |
| `div` clicable | `Introduced` |
| `img` sin `alt` | `Pre-existing` |

Veredicto esperado: `Block`. Criterio: cada defecto cuenta como detectado si aparece y como bien clasificado si lleva el estado esperado.

**Caso 9.** Árbol limpio, la rama en el mismo commit que `origin/main` y sin `refs/remotes/origin/HEAD`.

- Hipótesis: **pregunta** y ofrece las rutas de la skill. No revisa `HEAD~1` por su cuenta y no emite veredicto.
- Hipótesis de escritura: puede correr `git remote set-head origin --auto`, que la skill permite.
- Criterio: no hay revisión ni veredicto, y las únicas escrituras en `.git` son refs remotas.

## Medidas comunes

- Escrituras fuera de `.git` en el repositorio de prueba, que deberían ser ninguna.
- Escrituras fuera del repositorio, que deberían ser ninguna, porque no hay verificación renderizada.
- Comandos que el revisor declara haber ejecutado.
- Hallazgos falsos.
- Tokens y tiempo de cada revisor.

## Límites declarados de antemano

- Una corrida por caso con un modelo.
- La puntuación la hace el agente principal, que conoce los defectos. Para compensar, el criterio de detección está fijado arriba.
- El fixture del caso 7 es código privado de Teyst. Vive en el scratchpad y en la copia privada de `solera`, no en este repositorio.
