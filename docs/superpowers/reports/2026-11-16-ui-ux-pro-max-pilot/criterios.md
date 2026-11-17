# Piloto de UI/UX Pro Max: criterios fijados antes de medir

Fecha: 2026-11-16, hora local 21:3x, antes de la primera ejecución. Autorización: pedido del usuario en el chat de Claude Code: «Ejecuta el piloto propuesto de UI/UX Pro Max». Cubre los casos 1 a 6 de la [ronda de consolidación](../2026-11-16-ui-ux-tooling-consolidation-dry-run/README.md#6-piloto-propuesto-no-ejecutado). Los casos 7 a 9 son de Interface Review y quedan fuera.

**Revisión:** `nextlevelbuilder/ui-ux-pro-max-skill@e59ff376a41f7ca47b7541ad5c116495cbade3ee`, ruta `src/ui-ux-pro-max/scripts`.

**Aislamiento:**

- Se corre `python3 -E -s` desde un directorio vacío del scratchpad.
- `sandbox-exec` niega la red y toda escritura fuera del directorio del piloto y del temporal del sistema.
- No se instala nada, ni en Teyst ni en `~/.claude`.

## Hipótesis, del análisis estático, y criterio de cada caso

Un caso **confirma** si se observa lo esperado y **refuta** si se observa lo contrario. Si la salida no permite decidir, queda **indeterminado**.

| # | Entrada | Esperado | Criterio observable |
|---|---|---|---|
| 1 | `"app para catas de vino entre amigos, con ligas y ranking" --design-system --json` | Se usan defaults: `reasoning_default` true, primario #2563EB, fuente Inter | Valor de `reasoning_default`, categoría, colores y fuentes del JSON |
| 1b | Misma consulta sin `--json` (ascii) | La salida no avisa que son defaults | Ausencia de «default», «no match» o equivalente en el texto |
| 2 | `"wine tasting social app with leagues and ranking" --design-system --json` | Coincide con un producto real, quizá Brewery/Winery, y no usa defaults | `reasoning_default` false; categoría distinta de «General» |
| 3a | `"trazabilidad de barricas de roble para cooperativas"`, búsqueda simple | 0 resultados con aviso explícito | Texto «No matches…» |
| 3b | La misma con `--design-system --json` | Defaults sin aviso en ascii | Como en 1 y 1b |
| 4a | `"wine tasting app, burgundy and cream brand, rounded typography" --design-system --json` | La paleta y la tipografía salen de la industria, no de la marca | Distancia entre el primario y el burdeos de Tintum; si la fuente es redondeada |
| 4b | Dos agentes con el mismo brief de marca Tintum y los tokens de Teyst: A con la skill, B sin ella | A cambia más tokens de marca no pedidos que B | Tokens de marca conservados, cambios no pedidos y si declara la fuente de cada valor; los evalúa el agente principal con esta tabla |
| 5a | `--design-system --stack react-native` | Nota en stderr; salida idéntica a la del mismo comando sin `--stack` | Diff de stdout con y sin `--stack` |
| 5b | `--design-system --rtl full` | Error de argparse | Código de salida distinto de 0 y mensaje |
| 6a | `--persist --output-dir X` dos veces, la segunda con otra consulta y `--page p` | El MASTER no cambia; se crea `pages/p.md` con contenido de la consulta nueva: conjunto mezclado | Hash de MASTER antes y después; existencia y contenido de `pages/p.md` |
| 6b | Igual con `--force` | MASTER sobrescrito sin preguntar | Hash distinto; sin prompt |

**Medidas comunes:**

- archivos escritos, con `find -newer` sobre el directorio del piloto y `git status` del clon;
- intentos de red, que el sandbox registraría como denegaciones;
- tiempo de cada comando;
- tokens de los agentes del caso 4b.

**Límites declarados de antemano:**

- Una corrida por caso, sobre una sola revisión.
- 4b es un A/B con un agente por rama, sin ciego ni repetición. Indica una dirección, no una tasa.
