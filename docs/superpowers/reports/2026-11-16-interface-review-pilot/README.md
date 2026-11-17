# Piloto de Interface Review

Fecha: 2026-11-16, entre las 21:2x y las 21:3x hora local.

Estado: **piloto ejecutado, evidencia fechada**. No es una admisión ni una decisión, y no hay commit.

Autorización: pedido del usuario en el chat de Claude Code, «Ejecuta el piloto de Interface Review, casos 7 a 9». Los criterios se fijaron antes de ejecutar, en [criterios.md](criterios.md).

**Revisión.** `jakubkrehel/skills@6c2120103600407a1a9986afd834e73144ef8998`, con el conjunto mínimo de 8 carpetas. Se leyó desde el clon del scratchpad, sin instalarlo.

**Revisores.** Tres subagentes `sonnet`, uno por caso. Recibieron la skill y la invocación `/interface-review` sin objetivo, y nada sobre los defectos.

**Repositorios de prueba.** Locales, cada uno con un `origin` bare local, así que no hubo red. La verificación renderizada no se pidió.

**Operador:** Claude Code (`claude-opus-5-5`).

## Resultados

| # | Caso | Hipótesis | Observado | Resultado |
|---|---|---|---|---|
| 7 | React Native: la rama quita `accessibilityLabel={label}` de un `Pressable` con rol `button` y texto visible | No lo detecta, porque las señales de la skill son web | **Vio** la eliminación: la trató como el equivalente RN de `aria-label`, según `removed-signals.md`. La **descartó** como reemplazo equivalente, porque el nombre saldría del `<Text>{label}</Text>` hijo. Declaró el nombre efectivo como «Not verified». Veredicto **Approve**, sin hallazgos | Hipótesis **refutada en la forma**: la skill alcanzó la señal. Detección **no**, según el criterio fijado: no hubo hallazgo. Si el descarte es correcto queda **indeterminado** sin renderizar (ver abajo) |
| 8 | Web: se quita un `aria-label` (botón solo con ícono), se agrega un `<div onClick>` y ya había un `<img>` sin `alt` | 3 detecciones: Regression, Introduced y Pre-existing; Block | `aria-label` quitado → HIGH **Regression**. `div` clicable → HIGH **Introduced**, con teclado, rol, nombre y estado ausente agrupados por causa. `img` sin `alt` → **Pre-existing**, en su sección aparte. Veredicto **Block**. Sin hallazgos falsos. Layout, Typography y Colors quedaron «Not reviewed» por falta de CSS | **Confirma**: 3 de 3 detectados y 3 de 3 bien clasificados |
| 9 | Árbol limpio, la rama en `origin/main` y sin `origin/HEAD` | Pregunta, no revisa `HEAD~1` y no da veredicto. Quizá corre `remote set-head` | Reunió los hechos (rama, 0 commits por delante, último commit, `gh pr status` fallido) y formuló la pregunta con las rutas de la skill, sin veredicto. **No corrió** `remote set-head`: tomó `origin/main` como base por ser la única rama remota | **Confirma** lo central. El desvío respecto del orden de `scope-resolution.md` es inocuo aquí, pero es un desvío |

## Escrituras y permisos

Se tomó una foto antes y otra después de cada caso, de `git for-each-ref`, `git worktree list`, el hash de cada archivo de `.git`, `git status` y `ls /tmp`. **No cambió nada en ninguno de los tres casos:**

- no hubo refs nuevas;
- `.git` no se tocó, ni siquiera el index;
- no se crearon worktrees;
- el árbol quedó limpio;
- `/tmp` quedó igual.

**Comandos declarados:** solo de lectura.

- Los de git: `status`, `branch`, `log`, `merge-base`, `diff`, `show`, `grep`, `ls-files`, `rev-parse --git-path` (para detectar un rebase o un merge en curso) y `blame`.
- `gh pr status`, que falló sin remoto de GitHub.

**Ninguno usó** `add`, `commit`, `checkout`, `switch`, `stash`, `push`, `--force`, `--ours` ni `--theirs`. Es compatible con las reglas locales de Git.

**Fuera del alcance probado:**

- Las escrituras que la skill sí permite: `remote set-head`, `fetch --deepen`, `fetch` de PR y `worktree add` en `/tmp`. No se dispararon en estos casos.
- `gh` contra un remoto real de GitHub.

## Caso 7: por qué queda indeterminado

**Lo que hace bien el descarte.** Es razonado: la skill reconoce que una eliminación es regresión solo si nada la reemplaza, y en React Native el texto hijo da nombre al botón.

**Lo que no cubre.** No es equivalente al resguardo original:

- un `accessibilityLabel` explícito fija el nombre y no concatena otros hijos accesibles, como el indicador de carga;
- tampoco depende de cómo cada plataforma componga el nombre.

**Un límite del montaje.** El fixture se armó sin comentarios. El original documentaba que esa propiedad es un resguardo deliberado, así que el revisor no tenía esa intención a la vista.

**Qué haría falta para decidirlo:** leer el árbol de accesibilidad renderizado, en VoiceOver, TalkBack o react-native-web.

El detalle y el fixture son código privado de Teyst. Están en `solera/docs/initiatives/interface-review-pilot-2026-11-16/`, sin commit.

## Medidas

| Caso | Tokens | Tiempo | Llamadas a herramientas |
|---|---|---|---|
| 7 | 97.062 | 52 s | 8 |
| 8 | 98.882 | 52 s | 10 |
| 9 | 87.272 | 24 s | 6 |

**Total de subagentes:** 283.216 tokens. El consumo del agente principal y el costo en dinero no están disponibles.

**Cuánto de la skill se leyó.** Los revisores no leyeron completas todas las `better-*`. En el caso 8 se leyeron `better-interface`, `better-accessibility` y dos de sus referencias. Las otras cinco solo se listaron, porque el alcance no traía evidencia de esos dominios. Las 199 KB del conjunto mínimo no se cargan enteras en la práctica.

## Qué cambia respecto de la evaluación en seco

**Se confirma por ejecución:**

- la resolución del alcance;
- la regla de no caer en `HEAD~1`;
- la clasificación causal (Regression, Introduced, Pre-existing);
- el veredicto;
- la operación de solo lectura, en los caminos probados.

En una revisión web, el caso 8 es un resultado limpio.

**Se corrige:** «en React Native la mayoría de las señales no se dispararían» era demasiado fuerte. El revisor mapeó `accessibilityLabel` a `aria-label`. Lo que no garantiza es el juicio sobre la equivalencia, que sin renderizar queda abierto.

**Para `observedOutcome`:** este piloto puede citarse como resultado observado en una reevaluación de `interface-review-minset`. Tres corridas no dan una tasa.

**La recomendación no cambia.** Interface Review solo tendría sentido con un consumidor web con flujo de PR. Para Teyst, el caso 7 muestra que su revisión estática no sustituye la comprobación del árbol de accesibilidad.

## Límites

- Una corrida por caso, con un modelo.
- La puntuación la hizo el agente principal, que conocía los defectos; el criterio estaba fijado antes.
- Fixtures mínimos: un archivo por caso, sin consumidores ni CSS, así que la expansión de superficies y los dominios visuales no se ejercitaron.
- No se probaron PRs reales, `gh` con red, clones superficiales ni la verificación renderizada.

## Artefactos

**En este repositorio:** `criterios.md`, este README y `fixtures/` (el diff y la base del caso 8, y el log del caso 9).

**En `solera`, sin commit:** el diff, el bundle y el informe del caso 7.

**En el scratchpad:** los tres repositorios de prueba con sus fotos.

**Sin cambios:** Teyst, Brix, `docs/tooling/` y el clon de la skill.
