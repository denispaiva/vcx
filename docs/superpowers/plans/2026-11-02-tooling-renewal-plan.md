# Renovación de admisiones de tooling que vencen en noviembre de 2026

Fecha: 2026-11-02. Estado: en ejecución. El 2026-11-02 se completaron TR-1 a TR-5, con las decisiones del usuario registradas abajo; quedan TR-6 y TR-7. Avance en [Ejecución](#ejecución). Aplica el procedimiento de [evaluación de tooling en VCX](../specs/2026-11-01-tooling-evaluation-in-vcx-design.md) acordado por VCX-D035 a las admisiones heredadas del precursor que la [matriz](../../architecture/tooling-matrix.md) consume y que vencen entre el 2026-11-06 y el 2026-12-23.

## Hechos comprobados el 2026-11-02

Fuente: los 69 registros `*.evaluation.json` de `../blends/vc/tooling/evaluations/`, de solo lectura, y el único de VCX en `brix/tooling/evaluations/`; comparados con la fecha de hoy y con la regla de la [vista](../../exports/build_tooling_matrix_view.py), que calcula el vencimiento al abrirse.

- Ninguna admisión tiene `expiresAt` pasado hoy. Lo que la vista marca como «vencida» son dos revisiones humanas con fecha pasada: `agent-skills` (2026-09-09) y `gmail` (2026-10-24).
- El motor fija `expiresAt` en `observedAt` más 90 días, o 30 si la confianza es `low` (`computeExpiresAt`). Por eso el lote evaluado en agosto vence entre el 6 y el 8 de noviembre.
- `decide` no renueva: `recordHumanDecision` recalcula `expiresAt` desde `observedAt`, no desde la fecha de la decisión. Renovar una admisión exige un `evaluate` nuevo, que por VCX-D035 pasa por [`brix/tooling/score-run.mjs`](../../tooling/score-run.mjs) con `--replace-decision` si hay decisión humana previa, y por una autorización de corrida persistida.
- El precursor no se escribe. Cada renovación crea un registro nuevo en `brix/tooling/evaluations/`, que el generador lee antes que el del precursor. El `evaluate` no consume modelo; el colector de comunidad usa la API de GitHub con el token de `gh auth token`.
- No hay uso medido que sirva para priorizar. Los registros de `../blends/vc/tooling/usage/records/` cubren solo `writing-plans` y `subagent-driven-development`, con último día 2026-09-28; VCX no mide uso. La evidencia de uso en VCX sale de los transcripts, relevados en TR-1: la carpeta `docs/superpowers/` es una convención heredada y no prueba por sí sola que la skill haya corrido.

## Qué vence y cuándo

Solo las herramientas que alguna fila de la matriz referencia. Las once revisiones vencidas del precursor que ninguna fase de VCX usa quedan fuera de este plan.

| Fecha | Qué ocurre | Herramientas | Decisión vigente |
|---|---|---|---|
| Vencidas | Revisión humana pasada | `agent-skills` (2026-09-09), `gmail` (2026-10-24) | `approved_with_exception`, riesgo high y critical |
| 2026-11-04 | Revisión | `find-skills` | `approved_with_exception`, riesgo high |
| 2026-11-06 | Admisión vence | `brainstorming`, `find-skills`, `verification-before-completion`, `xlsx` | `approved` salvo `find-skills` |
| 2026-11-08 | Admisión vence | `emilkowalski-skills`, `handoff`, `impeccable`, `markitdown`, `requesting-code-review`, `security-review`, `test-driven-development`, `writing-plans` | `approved` salvo `markitdown`, con excepción y revisión el mismo día |
| 2026-11-29 a 2026-12-23 | Revisión o vencimiento | `context7-mcp`, `brix-llm-council`, `mattpocock-writing-for-agents`, `spec-kit-analyze`, `spec-kit-checklist`, `llm-council-skill`, `browser`, `sheets-api`, `gmail` | Varias; `llm-council-skill` sigue `decision_pending` |

A partir del 2026-11-06 la vista muestra las vencidas como «Sin admisión». No hace falta regenerarla para eso: el cálculo ocurre al abrirla.

## Regla propuesta y alternativas

Reevaluar las doce herramientas en una semana es la opción cara en atención y no aporta información sobre las que VCX no usa. La propuesta es un triage por herramienta con tres salidas, y correr el motor solo para las que lo merezcan:

| Salida | Cuándo | Qué se escribe |
|---|---|---|
| Renovar | Una fase de la matriz la usa hoy en VCX y la reserva sigue aceptable | Registro nuevo en `brix/tooling/evaluations/` vía el envoltorio; nota en la fila de la matriz |
| Dejar vencer como antecedente | Ninguna fase la usa hoy, o su uso es hipotético | Nota en la fila de la matriz: «sin admisión vigente; antecedente del precursor», deuda declarada conforme a VCX-P3 |
| Retirar | Reemplazada o con reserva que ya no se acepta | Fila en la tabla de reemplazos de la matriz; si tiene registro en VCX, `decide` con `rejected` |

Alternativas descartadas, con su costo: renovar todo exige doce evidencias de 23 subfactores y doce autorizaciones, sin nueva información; no hacer nada deja la vista mostrando «Sin admisión» para skills que VCX usa a diario, y la matriz dejaría de reflejar la admisión real.

Decisiones que corresponden al usuario antes de ejecutar:

1. Adoptar la regla de triage con «dejar vencer» como valor por defecto, salvo uso comprobado en VCX. Si se adopta como regla general para admisiones heredadas, es una decisión nueva para el [registro](../../decisions/README.md), no una nota al pie.
2. Aceptar la revisión ligera: cuando el ref instalado coincide con `evaluatedRef`, reusar la evidencia del precursor como insumo del `evaluate` nuevo, con `observedAt` de hoy y nota de procedencia. Sin esto, cada renovación es una evaluación completa.
3. `gmail`: confirmar o retirar la excepción crítica, que acepta un conector con treinta herramientas sobre un buzón personal para leer recibos del ledger. La revisión lleva nueve días vencida.

Respuestas del usuario el 2026-11-02, con la evidencia de TR-1 a la vista:

1. Regla de triage adoptada **solo en este plan**, para TR-3, TR-4 y TR-7. No es regla general ni lleva entrada en el registro; se generaliza si el lote de diciembre la repite.
2. Revisión ligera **no adoptada por ahora**: no aplica a ninguna renovación de este lote. Se decide cuando una renovación la necesite.
3. `gmail`: **retirar la excepción**. La fila pasa a Rechazado en la matriz, con fecha y motivo; si el ledger lo necesita, se reevalúa con acceso de solo lectura.

## Pasos

| ID | Paso | Depende de | Fecha límite | Costo |
|---|---|---|---|---|
| TR-1 | Fijar dónde se verifica el ref instalado de cada skill de terceros: el precursor o el plugin de Claude. Solo lectura | Ninguna | 2026-11-04 | Una sesión corta |
| TR-2 | Triage de las catorce herramientas de la tabla: uso en VCX con evidencia, ref instalado contra `evaluatedRef`, reserva abierta. Salida en la tabla de triage de este documento | TR-1 y decisiones 1 y 2 | 2026-11-05 | Una sesión; sin consumo de modelo |
| TR-3 | Lote 1: `find-skills`, `brainstorming`, `verification-before-completion`, `xlsx`, más `agent-skills` y `gmail`. Para cada «renovar»: evidencia en el scratchpad, `--dry-run`, corrida persistida con autorización | TR-2 y decisión 3 | 2026-11-06 | Por renovación, una evidencia y dos corridas; dinero `not_measured`, esperado 0 |
| TR-4 | Lote 2: las ocho del 2026-11-08, con el mismo circuito | TR-2 | 2026-11-08 | Igual que TR-3 |
| TR-5 | Anotar las salidas en la matriz, commitear, regenerar la vista y republicar el artifact | TR-3 y TR-4 | 2026-11-09 | Bajo |
| TR-6 | Cerrar `llm-council-skill` como retirada sin reevaluar, como prevé el diseño de VCX-D035 | Ninguna | 2026-12-10 | Bajo |
| TR-7 | Diciembre: `context7-mcp`, `mattpocock-writing-for-agents`, `spec-kit-*`, `browser`, `sheets-api`, con el triage de TR-2 ya hecho. `brix-llm-council` sigue su [plan propio](2026-11-01-council-review-backlog-plan.md) | TR-5 | Según fecha de cada una | Según triage |

## Resultado de TR-1

El ref instalado no se verifica en un solo lugar. Hay tres orígenes, cada uno con su método de solo lectura:

| Origen | Herramientas | Cómo se verifica | Resultado al 2026-11-02 |
|---|---|---|---|
| Vendorizadas en el precursor, `.agents/skills/` con `skills-lock.json` y `.claude/skills/` | `agent-skills`, `security-review`, `emilkowalski-skills`, `handoff`, `impeccable`, `markitdown` | SHA del árbol local (`git --no-optional-locks rev-parse HEAD:<carpeta>`) contra el de la misma carpeta en el `evaluatedRef` de GitHub (`gh api .../git/trees/<ref>`). Igual SHA es igual contenido byte a byte | Ninguna cambió desde su commit de instalación del 2026-08-09, y `status` está limpio. Contra el ref evaluado: **coinciden** `security-review` (`24fdb83`) y `handoff` (`v1.2.3`). **No coinciden** `impeccable`, con 18 de 147 archivos distintos del tag `skill-v4.0.4` aunque su `SKILL.md` declara 4.0.4, y `agent-skills`, copia de `main` del 2026-08-09 con 5 de 12 skills distintas del tag `0.6.6`. **Sin ref verificable**: `emilkowalski-skills`, evaluada sobre `main`, rama móvil que hoy difiere en las 9 skills, y `markitdown`, cuya carpeta es un envoltorio propio sin el CLI evaluado instalado, sin `markitdown` ni `pipx` en el PATH |
| Plugins del harness | `brainstorming`, `writing-plans`, `verification-before-completion`, `test-driven-development`, `requesting-code-review`, `xlsx` | Versión en el `plugin.json` o el manifiesto de la copia que carga el harness | Superpowers no está instalado para Claude en esta máquina; en Codex hay `7.0.1` en caché y `6.3.0` en el catálogo, y `6.2.0` en ningún lugar: **no coincide**. `xlsx` llega por el plugin `anthropic-skills` 1.0.0 de Claude Desktop (`updatedAt` 2026-10-27): sin ref comparable con `bundled@claude-code` |
| Conectores | `gmail` | Inventario de herramientas: nombres y conteo | Sin versión: `gmail-connector@2026-09-24` no es verificable. Expone 30 herramientas, igual que la evidencia |

`find-skills` no está instalada en ningún lugar relevado; la única búsqueda de skills en VCX usó otra, `wquguru/skills` · `skills-finder`, leída desde GitHub el 2026-11-01. Las skills del precursor son de proyecto: una sesión de Claude en `vcx/` no las carga, y la `/security-review` de esta sesión es la integrada de Claude Code.

La comparación por árbol, el detalle por herramienta y las reglas siguientes provienen de una sesión lateral de solo lectura del 2026-11-02, a pedido del usuario. Corrigen una primera lectura de este plan, que tomaba la ausencia de cambios desde la instalación como prueba de coincidencia. Reglas para próximas verificaciones, propuestas sin adoptar:

1. Vendorizadas en git: comparar el SHA del árbol local con el del ref evaluado. `evaluatedRef` debe ser un tag o un SHA, nunca una rama; al renovar `emilkowalski-skills`, registrar el SHA.
2. Plugins del harness: comparar la versión del `plugin.json` de la copia que carga el harness con la de `evaluatedRef`.
3. Sin copia instalada (`find-skills`, CLI de `markitdown`): «sin ref verificable» hasta que se instale; no se instala para verificar.
4. `xlsx` y conectores remotos: registrar como ref observable el `updatedAt` del manifiesto o el inventario de herramientas, y comparar eso.

Uso en VCX: las invocaciones de `Skill` en los 17 transcripts de Claude del proyecto, desde el 2026-10-31, y las lecturas de `SKILL.md` en llamadas de herramienta de las 16 sesiones de Codex que tocan `VibeCoding/vcx`, desde el 2026-10-30. No cuenta el catálogo que Codex carga en cada sesión. Cobertura: sesiones anteriores o de otros harness no quedan incluidas.

Consecuencia para la decisión 2: según el triage, el ref coincide solo en `security-review` y `handoff`, y ninguna de las dos tiene uso en VCX. Las tres con uso comprobado están en `7.0.1` y necesitan evaluación completa aunque se adopte la revisión ligera.

Fixtures reutilizables de evidencia: [`2026-11-02-finops-orchestration-repos-tool-dry-run-fixtures`](../reports/2026-11-02-finops-orchestration-repos-tool-dry-run-fixtures/). El envoltorio exige `--now` y `--operator`, y que el hash del registro vigente coincida con la última línea de `score-runs.jsonl`; todo subfactor `rubric` necesita `evidenceRefs` aunque quede `unavailable`.

## Triage

Evidencia relevada en TR-1, con el método y la cobertura de la sección anterior. La salida se lee con la regla de la decisión 1; si no se adopta, sigue siendo hipótesis.

| Herramienta | Uso en VCX | Ref coincide | Reserva abierta | Salida con la decisión 1 |
|---|---|---|---|---|
| `brainstorming` | Sí: 8 lecturas en Codex, del 2026-10-30 al 2026-11-02 | No coincide | Ninguna | Renovar sobre `7.0.1`, antes del 2026-11-06 |
| `verification-before-completion` | Sí: 4 lecturas en Codex, 2026-10-30 y 2026-10-31 | No coincide | Ninguna | Renovar sobre `7.0.1`, antes del 2026-11-06 |
| `writing-plans` | Sí: 3 lecturas en Codex, 2026-10-30 | No coincide | Ninguna | Renovar sobre `7.0.1`, antes del 2026-11-08 |
| `test-driven-development` | No | No coincide | Ninguna | Dejar vencer |
| `requesting-code-review` | No | No coincide | Ninguna | Dejar vencer |
| `security-review` | No; instalada solo en el precursor. La `/security-review` de Claude Code es otra herramienta | Coincide | Ninguna | Dejar vencer |
| `find-skills` | No; no está instalada | Sin ref verificable | Instala más skills; salida tratada como sugerencia | Dejar vencer |
| `xlsx` | No | Sin ref verificable | Ninguna | Dejar vencer |
| `handoff` | No | Coincide | Ninguna | Dejar vencer |
| `impeccable` | No | No coincide | Ninguna | Dejar vencer |
| `emilkowalski-skills` | No | Sin ref verificable | Ninguna | Dejar vencer |
| `markitdown` | No | Sin ref verificable | Riesgo high: red y dependencias locales | Dejar vencer |
| `agent-skills` | No | No coincide | Alcance: solo el subconjunto sin solapamiento con superpowers | Dejar vencer |
| `gmail` | No para el ledger. Una búsqueda general en la bandeja de entrada desde Codex el 2026-10-31, con el conector de Codex | Sin ref verificable | Riesgo critical aceptado sobre buzón personal | Decisión 3 |

Las tres renovaciones comparten repositorio y ref, así que la evidencia común de los 23 subfactores se arma una vez y se ajusta por skill. El uso medido es de Codex; la matriz no distingue harness, y Claude no tiene superpowers instalado.

## Ejecución

2026-11-02, con el pedido del usuario «Ejecutemos el plan» y sus respuestas a las decisiones 1 a 3 y a cada renovación.

- **TR-1 y TR-2:** resultado y triage arriba.
- **TR-3 y TR-4, renovaciones:** la evidencia de las tres skills la armó un subagente sobre la copia instalada y la API de GitHub; está en `brix/tooling/evaluations/`. Antes de correr se verificó la anomalía principal en `skills/brainstorming/scripts/server.cjs`: el companion visual carga una imagen de `primeradiant.com` con la versión en la URL, salvo que se defina `SUPERPOWERS_DISABLE_TELEMETRY`. La evaluación de 6.2.0 no lo había visto. Hubo una corrida en seco por skill y, con autorización del usuario para cada una, `evaluate` y `decide` persistidos por el envoltorio, todos con `--now 2026-11-02T15:30:00Z`.

  | Herramienta | Puntaje | Recomendación | Riesgo | Decisión del usuario | Revisión o vencimiento |
  |---|---|---|---|---|---|
  | `verification-before-completion` | 76,6 | `advance` | low | `approved` | Vence el 2027-01-31 |
  | `brainstorming` | 76,4 | `advance` | high (`networkAccess`) | `approved_with_exception`; reserva de telemetría | Revisión el 2026-12-02 |
  | `writing-plans` | 74,6 | `advance_with_reservations` | medium | `approved_with_exception`; sin pruebas automáticas | Revisión el 2026-12-02 |

  `evaluatedRef` es `openai-curated-remote/superpowers@7.0.1`. Los archivos de las tres skills coinciden con el tag `v7.0.1`, pero el marketplace agrega `agents/openai.yaml` y modifica `plugin.json`. El primer `decide` de `writing-plans` falló sin escribir nada, porque el motor exige `--accepted-risk` en toda `approved_with_exception`, y se repitió con ese flag. Se verificó que el estado del precursor y el de VCX fuera de `brix/tooling/` quedaron iguales, y que hay seis líneas nuevas en `score-runs.jsonl`, una por comando persistido.
- **Diez que se dejan vencer y `gmail` rechazado:** anotados en la [matriz](../../architecture/tooling-matrix.md#matriz). Su estado sigue en Asignado, porque el triage solo prevé una nota en la fila. Pasarlas a Candidato al vencer queda como pregunta para la próxima edición de la matriz.
- **TR-5:** matriz y registros commiteados, vista regenerada y artifact republicado.
- **TR-6:** sin ejecutar a propósito. Retirar `llm-council-skill` antes de la revisión de su reemplazo, el 2026-12-02, adelantaría esa decisión; sigue con fecha límite el 2026-12-10.

## Qué no autoriza este plan

Ninguna corrida persistida del motor, ninguna escritura en el precursor, ningún cambio en el generador de la vista ni en la política de scoring, ninguna instalación o actualización de skills. Cada corrida persistida requiere su autorización, como fija VCX-D035; la regla de triage, si se generaliza, requiere registro propio.
