# Reescritura del correo del historial de `vcx`

Fecha: 2026-11-01. Autoridad: el usuario eligió «Reescribir a noreply» y respondió «Autorizo el alcance» a la propuesta de ejecución presentada en el chat con Claude. Antecedente: la [revisión del historial](2026-11-01-vcx-public-history-review.md) previa a publicar `denispaiva/vcx`.

## Qué se hizo

- Se clonó la raíz en una carpeta temporal, sin tocar el checkout compartido, y se reescribió `main` con `git filter-branch`, incluido en Git, sin dependencias nuevas.
- En los 49 commits, el correo de autor y committer pasó a la dirección `noreply` de la cuenta en GitHub. Nombres, fechas y mensajes no cambiaron.
- En todas las versiones de `docs/decisions/README.md`, la mención del correo en la autorización del commit base pasó a «su dirección personal de correo». Es la única línea que cambia en cada árbol.
- En la raíz, `main` se movió de `75f0880` a `7ddfbe1` con una actualización atómica condicionada a que siguiera en `75f0880`; no hubo carrera con otras sesiones. Los cambios sin commit de todas las sesiones quedaron intactos; solo se alineó el índice de `docs/decisions/README.md`.
- El `main` anterior queda solo en local como `refs/backup/main-pre-noreply`, fuera de `refs/heads` y `refs/tags`, para recuperación. Contiene el correo: no debe subirse.
- `user.email` de la raíz quedó configurado con la dirección `noreply`, solo en este repositorio.

## Verificación

- 49 commits antes y después, emparejados en orden.
- Cada par difiere en un solo archivo, `docs/decisions/README.md`, con una línea quitada y una agregada; nombres, fechas y mensajes son idénticos.
- El correo no aparece en los metadatos ni en ninguna versión de ningún archivo del historial nuevo. Las menciones restantes de «gmail» son la herramienta MCP `gmail` de la matriz de tooling.
- Ningún SHA corto nuevo coincide con uno viejo.

## Correspondencia de SHA

Los SHA citados en documentos de `vcx` que figuran en la columna «Antes» se resuelven con esta tabla; no se reescribieron las citas. Al revisar, 14 SHA viejos aparecían citados en el árbol, entre ellos `f47c71f`, el commit base, en 13 archivos.

| Antes | Después | Asunto |
|---|---|---|
| `f47c71f` | `b4611bc` | docs: preserva la base documental de VCX |
| `c4d2dc1` | `76f5d53` | docs: registra VCX-D027 a D029, matriz de tooling, specs y vocabulario |
| `5058c2e` | `4ddb84b` | docs: aplica el modelo de productos de VCX-D029 |
| `1a728bd` | `fc39c98` | docs: ajusta el pitch y exporta el mapa OPML al 2026-11-01 |
| `57095c9` | `24f8f7f` | docs: etiqueta prensado en la matriz de tooling y amplía el banco de nombres |
| `0cc27ec` | `b48b0b4` | docs: exporta la vista HTML de la matriz de tooling |
| `4fce135` | `0e70774` | docs: agrega el ciclo de vida Git a la matriz de tooling |
| `d07b387` | `99d1545` | docs: regenera la vista HTML de la matriz de tooling |
| `9ff808e` | `66d139f` | docs: retira orca-cli de la matriz de tooling |
| `53ac997` | `622e0df` | docs: regenera la vista HTML de la matriz de tooling |
| `1d9b5c4` | `245d95c` | docs: retira skill-codex de la matriz de tooling |
| `a918f9f` | `b0b29fa` | docs: regenera la vista HTML de la matriz de tooling |
| `5d481ed` | `8498927` | docs: propone VCX-D030 y verifica la recuperación del commit base |
| `ef13623` | `da4ea57` | docs: agrega dónde vive cada elemento a la matriz de tooling |
| `4eefecc` | `f9ff51d` | docs: regenera la vista HTML de la matriz de tooling |
| `c0eabe0` | `e9e4f6d` | docs: agrega búsqueda con resaltado a la vista de la matriz de tooling |
| `b17adcc` | `2bb671e` | docs: regenera la vista HTML de la matriz de tooling |
| `c9d1b22` | `dda0991` | docs: muestra el estado de evaluación en la vista de la matriz de tooling |
| `0219e18` | `520af3e` | docs: regenera la vista HTML de la matriz de tooling |
| `bba8047` | `ffab498` | docs: adapta la vista de la matriz de tooling a márgenes seguros y tema oscuro |
| `9387921` | `1f7775a` | docs: regenera la vista HTML de la matriz de tooling |
| `6a07b02` | `e3ccf8f` | docs: inventaría la deuda heredada y la organización en GitHub |
| `7cf7b0b` | `a282fcf` | docs: propone VCX-D032, productos públicos con historial filtrado |
| `aaa332d` | `cca99b0` | docs: muestra el reemplazo de llm-council-skill por brix-llm-council |
| `e811e59` | `d25f0a5` | docs: regenera la vista HTML de la matriz de tooling |
| `33f1548` | `06aa579` | docs: crea brix-llm-council, renombra brix-killer-questions y agrega reportes de evidencia |
| `a72d585` | `02e080c` | docs: regenera la vista HTML de la matriz de tooling |
| `eb14ae6` | `4a1abeb` | docs: inventaría los controles de seguridad y privacidad |
| `6041006` | `438a734` | docs: aplica las decisiones VCX-D033 en brix-llm-council |
| `6a543a4` | `66aed79` | docs: regenera la vista HTML de la matriz de tooling |
| `5f73163` | `9285571` | docs: revisa el inventario de controles tras la crítica cruzada |
| `78bba31` | `2d650ef` | docs: propone VCX-D034, responsables del inventario de controles |
| `b9bb57f` | `b44a0ed` | docs: cierra la etapa 1 en seco de brix-llm-council |
| `588fba2` | `9785622` | docs: registra en VCX las decisiones de tooling sin escribir en el precursor |
| `9f022eb` | `dbee007` | docs: regenera la vista HTML de la matriz de tooling |
| `c4a78d5` | `bb16192` | docs: marca con un badge las herramientas construidas por VCX en la matriz de tooling |
| `8d8d21c` | `485969f` | docs: regenera la vista HTML de la matriz de tooling |
| `ac91f4e` | `af09133` | docs: verifica que el motor de scoring del precursor escribe solo fuera de él |
| `81b5c9d` | `f696540` | docs: cierra la etapa 2 de brix-llm-council con tres corridas |
| `6934489` | `0d1bd7a` | docs: revisa VCX-D031 tras el consejo de brix-llm-council |
| `8adb4c0` | `736c8d4` | docs: propone VCX-D035, evaluación de tooling con registro en VCX |
| `ce392b1` | `6bc0530` | docs: corrige brix-llm-council por los hallazgos de la etapa 2 |
| `2c2a3ab` | `7ffaaaf` | docs: acuerda VCX-D035 y actualiza la regla de admisión de la matriz |
| `2f38ef6` | `a44da6e` | docs: regenera la vista HTML de la matriz de tooling |
| `74c9db5` | `157a1b5` | docs: planifica la etapa 3 de brix-llm-council sin ejecutarla |
| `45f961a` | `8bbb542` | docs: alinea la procedencia de brix-llm-council con VCX-D035 |
| `5d8d5de` | `f12eb24` | docs: replantea la etapa 3 de brix-llm-council según VCX-D035 |
| `4b8d1de` | `a433606` | docs: regenera la vista HTML de la matriz de tooling |
| `75f0880` | `7ddfbe1` | docs: registra la política FinOps de orquestación y rechaza cinco repos propuestos |

## Límites y pendientes

- No se creó el repositorio en GitHub ni se hizo push. Antes del push siguen pendientes un scan real del historial y la revisión con el mismo criterio de los cambios que entren después de este reporte.
- Las sesiones abiertas pueden seguir citando SHA viejos; se resuelven con esta tabla.
- El reflog y `refs/backup/main-pre-noreply` conservan el historial anterior en esta máquina. Borrarlos es una decisión aparte.
