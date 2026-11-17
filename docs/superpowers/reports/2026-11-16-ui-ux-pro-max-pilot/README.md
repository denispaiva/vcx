# Piloto de UI/UX Pro Max

Fecha: 2026-11-16, entre las 21:15 y las 21:20 hora local.

Estado: **piloto ejecutado, evidencia fechada**. No es una admisión ni una decisión, y no hay commit.

**Autorización.** Pedido del usuario en el chat de Claude Code: «Ejecuta el piloto propuesto de UI/UX Pro Max». Cubre los casos 1 a 6 de la [ronda de consolidación](../2026-11-16-ui-ux-tooling-consolidation-dry-run/README.md#6-piloto-propuesto-no-ejecutado). Los casos 7 a 9 son de Interface Review y no se corrieron.

**Revisión:** `nextlevelbuilder/ui-ux-pro-max-skill@e59ff376a41f7ca47b7541ad5c116495cbade3ee`, script `src/ui-ux-pro-max/scripts/search.py`, con Python 3.15.2.

**Operador:** Claude Code (`claude-opus-5-5`). En el caso 4b, dos subagentes `sonnet`.

Los criterios se fijaron antes de la primera ejecución en [criterios.md](criterios.md).

## Aislamiento

Cada ejecución:

- corrió con `python3 -E -s` desde un directorio vacío del scratchpad;
- corrió bajo `sandbox-exec` con el perfil [salidas/sandbox.sb](salidas/sandbox.sb), que niega la red y toda escritura fuera del directorio del piloto y del temporal del sistema.

Antes de empezar se comprobó que el perfil funciona:

- una conexión a `1.1.1.1:80` y una escritura en `$HOME` dieron `Operation not permitted`;
- la escritura dentro del piloto funcionó.

No se instaló nada, ni en Teyst ni en `~/.claude`. El clon quedó sin cambios ni archivos ignorados nuevos: el sandbox tampoco dejó escribir `__pycache__`.

## Resultados por caso

Las salidas completas están en [salidas/](salidas/); los tiempos, en [salidas/runs.tsv](salidas/runs.tsv). Cada comando tardó entre 0,07 y 0,28 s.

| # | Caso | Hipótesis | Observado | Resultado |
|---|---|---|---|---|
| 1 | Consulta en español, `--design-system --json` | Defaults: `reasoning_default` true, #2563EB, Inter | Categoría «General», `reasoning_default: true`, patrón Hero + Features + CTA, estilo Minimalism & Swiss, primario #2563EB. Tipografía **Outfit + Work Sans**, no Inter: color y tipografía no abstuvieron y tomaron las filas «SaaS (General)» y «Geometric Modern» | Confirma lo central. Refuta el detalle de Inter: la tipografía salió de una coincidencia débil, no del default fijo |
| 1b | La misma consulta, salida ascii | Ningún aviso de default | Encabezado «RECOMMENDED DESIGN SYSTEM» y ninguna mención de default, fallback ni falta de coincidencia | Confirma |
| 2 | La misma consulta en inglés | Coincide con un producto real, quizá Brewery/Winery | `reasoning_default: false`, categoría **«Social Media App»** (no Brewery/Winery), estilo Vibrant & Block-based, primario #E11D48, Inter + Playfair Display | Confirma que no usa defaults. Refuta Brewery/Winery: «social» pesa más que «wine» |
| 3a | Sin coincidencias, búsqueda simple | 0 resultados con aviso | «Found: 0 results», un aviso que pide declarar la falta de coincidencia y términos sugeridos irrelevantes («mobile», «double») | Confirma |
| 3b | Sin coincidencias, `--design-system` | Defaults sin aviso en ascii | El mismo sistema que en el caso 1 (#2563EB, Outfit + Work Sans). El ascii no contiene «default» ni «no match» | Confirma |
| 4a | «wine tasting app, burgundy and cream brand, rounded typography» | Paleta y tipografía por industria, no por marca | Categoría «Luxury/Premium Brand», estilo **Liquid Glass**, primario #1C1917 (casi negro), acento #A16207. Tipografía Inter + Playfair Display, no redondeada. Ni burdeos ni crema | Confirma: la restricción de marca escrita en la consulta no llega al resultado |
| 4b | A/B de agentes con la marca Tintum y los tokens de Teyst | A, con la skill, cambia más tokens de marca no pedidos que B | Las dos ramas conservaron los tres colores de marca, con **0 cambios no pedidos** a tokens existentes. Las dos propusieron solo agregar Nunito. A recibió de la herramienta una paleta azul (#0369A1) e Inter + Playfair, y **la descartó** por contradecir la marca | **Refuta**: el agente filtró la recomendación. La herramienta no empeoró el resultado, pero aportó poco (ver abajo) |
| 5a | `--design-system --stack react-native` | Nota en stderr y salida idéntica | stderr: «--stack react-native is ignored in --design-system mode…». `diff` de stdout con y sin `--stack`: idénticos | Confirma |
| 5b | `--design-system --rtl full` | Error | Código 2: «--rtl is not supported with --design-system» | Confirma |
| 6a | Persistir dos veces; la segunda con otra consulta y `--page ligas`, sin `--force` | MASTER intacto y página nueva: conjunto mezclado | Hash de MASTER igual (`2a5111e2…`) y se creó `pages/ligas.md`. **No hay ningún aviso de que se saltó el MASTER**: la salida dice «Design system persisted» y lista solo la página. La página es una plantilla casi vacía («No overrides — use Master…») y apunta a `design-system/MASTER.md`, no a la ruta real `design-system/pilot/MASTER.md` | Confirma la mezcla y la omisión silenciosa. La mezcla de contenido es menor de lo esperado: la página casi no trae reglas |
| 6b | Igual, con `--force` | MASTER sobrescrito sin preguntar | Hash nuevo (`5634f0ae…`), sin prompt; el primario pasó de #E11D48 a #2563EB | Confirma |

Los hashes de cada paso del caso 6 están en [salidas/c6r_hashes.txt](salidas/c6r_hashes.txt). La primera corrida de ese caso, `c6a_*`, no guardó el hash intermedio y se repitió en un directorio nuevo.

## Caso 4b: medidas

**Brief ficticio:** pantalla «Acerca de» de Teyst con la firma «powered by tintum», con restricciones de marca Tintum (VCX-D061) y los tokens existentes de Teyst.

**Rama A:** con la skill, cuyo script corrió en el sandbox. **Rama B:** sin herramientas. Las dos con el mismo modelo, una corrida por rama, sin ciego.

| Medida | A, con skill | B, sin skill |
|---|---|---|
| Colores de marca conservados (3) | 3 | 3 |
| Cambios no pedidos a tokens existentes | 0 | 0 |
| Cambio propuesto a los tokens | Solo agregar Nunito | Solo agregar Nunito, en un grupo aparte |
| Evitó un token existente de nombre parecido pero valor distinto al burdeos oscuro de la marca | Sí | Sí, y lo advirtió explícitamente |
| Origen declarado por token | Sí | Sí |
| Contraste calculado | Sí, con Python local | Sí, a mano, aproximado |
| Lo que vino de la herramienta | Tocables de 44 pt / 48 dp con 8 de separación, foco visible y confirmar Nunito como familia redondeada | — |
| Recomendaciones de la herramienta descartadas | Paleta azul, Inter + Playfair, patrón «Funnel», estilo Minimalism & Swiss | — |
| Llamadas a la herramienta | 3 | 0 |
| Tokens del subagente | 93.857 | 87.570 |
| Tiempo | 81 s | 55 s |

**Lectura.** Con una restricción de marca explícita y un sistema de tokens existente, la herramienta no hizo daño, porque el agente la filtró. Tampoco agregó nada que el agente sin herramienta no obtuviera:

- los tocables de 44 pt y 48 dp ya están en la regla Mobile First de los `AGENTS.md`;
- la elección de Nunito venía dada por la marca.

Costó un 7 % más de tokens y un 47 % más de tiempo.

Lo que protegió la marca fue el agente, no el código: el generador propuso lo contrario.

Las entregas completas reproducen tokens de Teyst, que es privado. Por eso viven en la copia privada `solera/docs/initiatives/ui-ux-pro-max-pilot-2026-11-16/`, sin commit, y no en este repositorio público (VCX-D032).

## Qué cambia respecto de la evaluación en seco

**Se confirma por ejecución:** lo que la inspección estática afirmaba sobre `--stack`, `--rtl`, `--force`, la omisión de un MASTER existente y la ausencia de aviso de defaults en ascii.

**Se corrige:**

- Una consulta en español sin coincidencias no cae necesariamente en Inter. Color y tipografía pueden tomar filas por coincidencias débiles («app», «para»), que se presentan igual como recomendación.
- Una consulta en inglés sobre vino social no llega a Brewery/Winery.

**Hallazgos nuevos:**

- La página de overrides apunta a una ruta de MASTER que no existe.
- La salida de persistencia no informa los archivos que se saltaron.

**Para el piloto,** con un agente capaz y restricciones explícitas, el riesgo práctico de que la herramienta imponga una estética ajena fue bajo: el agente descartó su recomendación. Su valor incremental también fue bajo.

El `observedOutcome` de una futura evaluación de `ui-ux-pro-max-core` puede citar este piloto. No es un número del motor: una corrida por rama no da una tasa.

**La recomendación no cambia: no agregar la herramienta.**

## Límites

- Una corrida por caso, sobre una revisión y con un solo modelo en 4b.
- 4b no fue ciego: lo puntuó el agente principal, que conocía la hipótesis.
- No se probó `--preview` ni `--tokens`.
- El sandbox impidió observar si algún camino no probado intentaría usar la red. Las denegaciones no se registraron en el log del sistema.

## Artefactos

**En este repositorio:**

- `criterios.md`;
- este README;
- `salidas/`: 16 salidas no vacías, los hashes del caso 6, el perfil del sandbox y los tiempos.

**En `solera`, sin commit:** las entregas A y B.

**En el scratchpad de la sesión:** el directorio del piloto, con las carpetas `design-system/` generadas, y el clon.

**Sin cambios:** Teyst, Brix, `docs/tooling/` y el clon.

**Consumo:**

- subagentes del caso 4b: 181.427 tokens;
- agente principal: no disponible;
- costo en dinero: no disponible.
