# Piloto A a D: criterios fijados antes de medir

Fecha: 2026-11-17, 22:15 hora local (UTC−3), antes de la primera ejecución.

Autorización: pedido del usuario en el chat de Claude Code, «Ejecuta el piloto propuesto, casos A a D». Son los casos de la [segunda ronda en seco](../2026-11-17-ui-ux-tooling-consolidation-dry-run/README.md#6-piloto-propuesto-no-ejecutado).

**Revisiones:**

- UI/UX Pro Max: `nextlevelbuilder/ui-ux-pro-max-skill@e59ff376a41f7ca47b7541ad5c116495cbade3ee`.
- Interface Review: `jakubkrehel/skills@2136b60ecf0078f1556623f8b6d26a1563c03512`, conjunto mínimo de 8 carpetas.

Las dos se leen desde clones del scratchpad. No se instalan en `~/.claude` ni en ningún proyecto.

**Operador:** Claude Code (`claude-opus-5-5`), que monta los casos, mide y puntúa lo objetivo. No juzga la preferencia del caso A.

## Caso A: dirección visual con y sin UI/UX Pro Max

**Brief, en inglés y sin marca previa:** la pantalla de inicio de una app móvil para una biblioteca de herramientas entre vecinos. Es un producto ficticio, sin datos de Teyst.

**Entrega de cada corrida:**

- un HTML autocontenido para un viewport de 390 × 844, sin recursos externos ni JavaScript;
- un `tokens.json` con los colores y la tipografía.

**Ramas.** Seis corridas, tres por rama, todas con el mismo modelo (`sonnet`) y el mismo brief.

- **Rama S, con skill:** recibe el `SKILL.md` de la skill y un comando que corre `search.py` en un sandbox sin red, con escritura solo en su carpeta.
- **Rama N, sin skill:** sin herramientas de diseño.

**Ciego.** Antes de la revisión, el operador:

1. renombra las seis entregas con identificadores al azar y guarda la correspondencia aparte;
2. quita los comentarios de los HTML;
3. no entrega ningún texto de las corridas, solo el HTML y una captura de 390 × 844 hecha con Brave sin interfaz.

El revisor es un subagente `opus` nuevo, que no sabe que hay dos ramas ni qué herramienta se prueba. Ordena las seis del 1 al 6 y puntúa cada una de 1 a 5 en jerarquía, claridad, calidad visual, ajuste al brief y accesibilidad aparente.

**Contraste medido con herramienta.** Sobre el render en Brave, por script: para cada nodo de texto visible, su color contra el primer fondo opaco de sus ancestros, con la fórmula de WCAG 2.2. Cuenta como falla el texto bajo 4,5:1, o bajo 3:1 si es grande. Los fondos con degradado o imagen se informan como «no medible», no como aprobados.

**Medidas:** posición media de cada rama, puntajes medios, fallas de contraste por corrida, tokens y tiempo por corrida.

**Criterio de decisión:**

- **La skill supera a la línea de base** si se cumplen las dos condiciones:
  - la posición media de S es al menos 1,0 mejor que la de N;
  - S no tiene más fallas de contraste en total que N.
- **La skill empeora el resultado** si la posición media de N es al menos 1,0 mejor que la de S, o si S tiene más fallas de contraste en total que N.
- Cualquier otro resultado es un **empate**.

Solo el primer resultado cambiaría la recomendación de no agregarla.

## Caso B: el caso 7 con render

**Fixture:** el mismo del piloto del 2026-11-16, `components/key-button.tsx` de Teyst, privado. La rama quita `accessibilityLabel={label}` del `Pressable`.

**B1, revisión.** Un subagente `sonnet` nuevo corre `/interface-review` sin objetivo, con la skill en `2136b60`. El montaje es el mismo del 2026-11-16.

**B2, render.** El componente se monta con react-native-web 0.21.2, tomado del `node_modules` de Teyst, que no se modifica. Se renderizan cuatro estados:

- base y rama;
- cada uno en reposo y cargando.

La página se sirve en localhost y se abre en Brave. Por cada estado se lee el nombre accesible y el rol del botón en el árbol de accesibilidad de Chrome.

**Criterio:**

- **El descarte de la skill es correcto, en web,** si el nombre accesible coincide entre base y rama en los dos estados.
- **El descarte es incorrecto** si difiere en alguno: nombre vacío, otro texto o hijos concatenados.

En los dos casos, el resultado no dice nada de VoiceOver ni de TalkBack, que este piloto no prueba.

## Caso C: el caso 8 en la revisión nueva

**Fixture:** el del 2026-11-16, que está en este repositorio. Un subagente `sonnet` nuevo, con la skill en `2136b60`.

**Criterio, el mismo de antes:** detectar los tres defectos y clasificarlos así, con veredicto `Block`:

| Defecto | Clasificación |
|---|---|
| `aria-label` quitado | `Regression` |
| `div` clicable | `Introduced` |
| `img` sin `alt` | `Pre-existing` |

**El resultado se transfiere** si se cumplen 3 de 3 detecciones y 3 de 3 clasificaciones.

## Caso D: escrituras permitidas en `.git`

**Montaje.**

- Un repositorio de prueba cuyo `origin` es un bare local. El bare tiene `refs/pull/7/head` con un cambio web: un botón de ícono sin `aria-label`.
- El clon no tiene `refs/remotes/origin/HEAD` ni la ref del PR.
- Un subagente `sonnet` nuevo corre `/interface-review pr 7`.

**Medidas, antes y después:**

- `git for-each-ref`;
- el hash de cada archivo de `.git`;
- `git worktree list`;
- `git status --porcelain`;
- el listado de `/tmp`.

**Hipótesis:** busca la ref del PR con `git fetch` hacia `refs/remotes/pr/7` y quizá corre `remote set-head`.

**Criterio de compatibilidad con las reglas locales:** las únicas escrituras son refs bajo `refs/remotes/`, objetos y `FETCH_HEAD`. No hay cambios en el árbol de trabajo, ni worktrees, ni archivos en `/tmp`.

## Límites declarados de antemano

- **Caso A:** tres corridas por rama y un solo revisor. Indica una dirección, no una tasa con intervalo.
- **Casos B a D:** una corrida por caso. Los puntúa el operador, que conoce los defectos; para compensar, los criterios quedan fijados arriba.
- El render de B2 es web. La composición del nombre en iOS y Android puede ser distinta.
- Los fixtures privados de Teyst no entran en este repositorio. Sus resultados van a `solera/docs/initiatives/`, sin commit.
