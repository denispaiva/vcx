# Etapa 1 de `brix-llm-council`: revisión del contrato en seco

Fecha: 2026-11-01. Autoridad: el usuario autorizó la etapa 1 («Sí, etapa 1») tras una revisión con siete objeciones de verificación, incorporadas aquí. Consumo: cero invocaciones de subagentes; ninguna llamada a modelos fuera de la sesión que redactó esto. Esta etapa no autoriza las 27 invocaciones de la etapa 2 ni escrituras en el precursor.

Qué es y qué no es este reporte. Sin un ejecutor, las pruebas en seco son seguimiento de instrucciones por el agente orquestador: revisan el contrato de la skill y comprueban con herramientas la mecánica que el contrato prescribe, pero no demuestran que un control se aplique en una corrida real. Cada resultado dice cuál de las dos cosas es.

## Entorno

- Skill evaluada: `brix/.claude/skills/brix-llm-council/SKILL.md` en la revisión `6041006`, más las tres correcciones de contrato de esta etapa (sin commit al redactar).
- Sesión: Claude Code en la app de escritorio, directorio de trabajo `/Users/denis/VibeCoding/vcx/brix`.
- Fixture sintético en el scratchpad de la sesión (`stage1/`): `fixture.md` (propuesta ficticia de caché, revisión `18a243fafaf1` por SHA-256 del contenido), `question.txt`, `config-complete.json` (11 asientos `subagent`, tope 11, concurrencia 5, espera 600 s, 400 palabras), `config-incomplete.json`, destino `out/`. Salidas crudas en `stage1/raw/`. El scratchpad es temporal; este reporte conserva los valores necesarios.

## Resultados

| Criterio | Resultado | Tipo de evidencia |
|---|---|---|
| Descubrible desde `brix/` | La herramienta `Skill("brix-llm-council")` cargó el contenido de SKILL.md en esta sesión | Verificado con herramienta, en esta sesión y entorno; no prueba disponibilidad general |
| No descubrible desde `vcx/` | El usuario ejecutó el 2026-11-01, en una sesión aparte de Claude Code con directorio de trabajo `/Users/denis/VibeCoding/vcx`, un prompt que pedía el listado de skills sin tocar el disco. Respuesta reportada: ninguna skill con prefijo `brix-`; `brix-llm-council` no aparece; el listado solo incluye grupos `engineering:`, `design:`, `desktop-commander:`, `anthropic-skills:` y las integradas. Hecho verificado desde esta sesión: no existe `vcx/.claude/skills/` | Verificado por el usuario en esa sesión y entorno, respuesta reportada al asistente; confirma que el descubrimiento no desciende a `brix/` |
| Hash determinista | La misma entrada dio `71eb43918703` en dos cálculos; la pregunta con mayúsculas y espacios sobrantes dio el mismo hash tras normalizar; cambiar la clase solicitada de un asiento dio `1cabde22183c` | Verificado con herramienta (`shasum`); prueba la receta, no que el orquestador la aplique |
| Configuración insuficiente → diagnóstico sin llamadas | Con `config-incomplete.json` (sin `max_invocations`, sin espera por fase, sin asiento `synthesis`) el orquestador produjo el diagnóstico `raw/case-a-diagnostic.md` y no invocó ningún agente | Seguimiento de instrucciones; la ausencia de invocaciones consta en la transcripción de la sesión |
| Pregunta ausente → diagnóstico sin llamadas | Con el documento y sin pregunta, el orquestador produjo `raw/case-b-diagnostic.md`, sin extraer preguntas de la sección «Supuestos» | Seguimiento de instrucciones |
| Repetición sin material nuevo → no ejecuta | Con un reporte preexistente `status: complete` y `run_hash: 71eb43918703` en `out/`, la búsqueda con `grep` lo encontró y el orquestador informó el existente (`raw/case-c-result.md`) | Mecánica verificada con herramienta; la decisión de no ejecutar es seguimiento de instrucciones |
| Protección de una salida existente | Con `2026-11-01-council-fixture.md` presente, el nombre siguiente calculado fue `2026-11-01-council-fixture-2.md` (`raw/case-d-next-name.txt`) | Mecánica verificada con herramienta |
| Lecturas por asiento dentro de lo autorizado | No aplicable en seco: no hubo asientos | No verificable en esta etapa |
| Ausencia de recomendación en la síntesis | No aplicable en seco | No verificable en esta etapa |

## Brechas del contrato encontradas y corregidas

Las tres aparecieron al intentar ejecutar la mecánica con herramientas y se corrigieron en SKILL.md con el alcance mínimo:

1. **Serialización de los bindings.** El hash incluía «los bindings solicitados» sin forma canónica; dos orquestadores podían serializarlos distinto y obtener hashes distintos para la misma entrada. Ahora: una línea, once asientos en orden fijo, `asiento=familia/clase/runner`, separados por `;`. También se fijó la revisión de un documento no versionado (primeros 12 hexadecimales del SHA-256 del contenido) y la normalización exacta de la pregunta.
2. **Claves del frontmatter.** No estaban nombradas, así que la guarda de repetición no tenía qué buscar. Ahora: `document_revision`, `run_hash`, `status`, `bindings_requested`, `bindings_observed`, `invocations`, `decorrelated`, `cost`, `new_material`, y la guarda se comprueba con herramienta buscando `run_hash` y `status: complete`.
3. **Nombre del reporte.** «Fecha y sufijo numérico» no fijaba el patrón. Ahora: `<fecha>-council-<nombre del documento>.md` con sufijo `-2`, `-3`.

## Ajustes a la etapa 2 por las objeciones recibidas

- **Lecturas autorizadas:** la lista que declara cada asiento no demuestra sus lecturas. Antes de la corrida 1 hay que establecer si el host expone las llamadas a herramientas de cada subagente (hipótesis: las transcripciones de subagentes quedan en el directorio de proyecto de Claude Code). Si no, el criterio se registra como no verificable, sin afirmar que pasó.
- **Recomendaciones:** la búsqueda de texto es un primer filtro; el criterio se cierra con lectura humana o revisión independiente de la síntesis.
- **Fallo inducido:** no se usa una espera mínima. Se cancela explícitamente un asiento con la herramienta de detención del host, se cuenta como invocación consumida, se verifica que no haya reintento y que ninguna llamada siga fuera del presupuesto; el procedimiento se escribe antes de ejecutar.
- **Identidad:** `evaluatedRef` es SHA más ruta de la skill, con las correcciones de esta etapa incluidas en ese commit.
- **Consumo:** 27 es un techo de invocaciones, no de tokens ni dinero. Se mantienen el límite de 400 palabras por respuesta y la espera por fase declarada; el gasto se registra como `not_measured` si el host no lo expone.

## Pendientes

- Commit de las tres correcciones de SKILL.md y de este reporte.
- Autorización del documento, la pregunta y el tope de invocaciones de la etapa 2.
