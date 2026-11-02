# Renovación de admisiones de tooling que vencen en noviembre de 2026

Fecha: 2026-11-02. Estado: propuesta; nada ejecutado ni autorizado. Aplica el procedimiento de [evaluación de tooling en VCX](../specs/2026-11-01-tooling-evaluation-in-vcx-design.md) acordado por VCX-D035 a las admisiones heredadas del precursor que la [matriz](../../architecture/tooling-matrix.md) consume y que vencen entre el 2026-11-06 y el 2026-12-23.

## Hechos comprobados el 2026-11-02

Fuente: los 69 registros `*.evaluation.json` de `../blends/vc/tooling/evaluations/`, de solo lectura, y el único de VCX en `brix/tooling/evaluations/`; comparados con la fecha de hoy y con la regla de la [vista](../../exports/build_tooling_matrix_view.py), que calcula el vencimiento al abrirse.

- Ninguna admisión tiene `expiresAt` pasado hoy. Lo que la vista marca como «vencida» son dos revisiones humanas con fecha pasada: `agent-skills` (2026-09-09) y `gmail` (2026-10-24).
- El motor fija `expiresAt` en `observedAt` más 90 días, o 30 si la confianza es `low` (`computeExpiresAt`). Por eso el lote evaluado en agosto vence entre el 6 y el 8 de noviembre.
- `decide` no renueva: `recordHumanDecision` recalcula `expiresAt` desde `observedAt`, no desde la fecha de la decisión. Renovar una admisión exige un `evaluate` nuevo, que por VCX-D035 pasa por [`brix/tooling/score-run.mjs`](../../../brix/tooling/score-run.mjs) con `--replace-decision` si hay decisión humana previa, y por una autorización de corrida persistida.
- El precursor no se escribe. Cada renovación crea un registro nuevo en `brix/tooling/evaluations/`, que el generador lee antes que el del precursor. El `evaluate` no consume modelo; el colector de comunidad usa la API de GitHub con el token de `gh auth token`.
- No hay uso medido que sirva para priorizar. Los registros de `../blends/vc/tooling/usage/records/` cubren solo `writing-plans` y `subagent-driven-development`, con último día 2026-09-28; VCX no mide uso. La única evidencia de uso en VCX es documental: `docs/superpowers/` existe por las skills de superpowers.

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

Fixtures reutilizables de evidencia: [`2026-11-02-finops-orchestration-repos-tool-dry-run-fixtures`](../reports/2026-11-02-finops-orchestration-repos-tool-dry-run-fixtures/). El envoltorio exige `--now` y `--operator`, y que el hash del registro vigente coincida con la última línea de `score-runs.jsonl`; todo subfactor `rubric` necesita `evidenceRefs` aunque quede `unavailable`.

## Triage

Se completa en TR-2. Hasta entonces, las salidas son hipótesis.

| Herramienta | Uso en VCX | Ref coincide | Reserva abierta | Salida propuesta |
|---|---|---|---|---|
| `brainstorming` | Documental, `docs/superpowers/specs/` | Por verificar | Ninguna | Renovar |
| `writing-plans` | Documental, `docs/superpowers/plans/` | Por verificar | Ninguna | Renovar |
| `verification-before-completion` | Por verificar | Por verificar | Ninguna | Por decidir |
| `test-driven-development` | Por verificar; VCX casi no tiene código ejecutable | Por verificar | Ninguna | Por decidir |
| `requesting-code-review` | Por verificar | Por verificar | Ninguna | Por decidir |
| `security-review` | Asignada con alcance `task`; uso por verificar | Por verificar | Ninguna | Renovar |
| `find-skills` | Por verificar | Por verificar | Instala más skills; salida tratada como sugerencia | Por decidir |
| `xlsx` | Por verificar | Por verificar | Ninguna | Por decidir |
| `handoff` | Por verificar | Por verificar | Ninguna | Por decidir |
| `impeccable` | Por verificar | Por verificar | Ninguna | Por decidir |
| `emilkowalski-skills` | Por verificar | Por verificar | Ninguna | Por decidir |
| `markitdown` | Por verificar | Por verificar | Riesgo high: red y dependencias locales | Por decidir |
| `agent-skills` | Por verificar | Por verificar | Alcance: solo el subconjunto sin solapamiento con superpowers | Por decidir |
| `gmail` | Lectura de recibos del ledger, en el precursor | Por verificar | Riesgo critical aceptado sobre buzón personal | Decisión 3 |

## Qué no autoriza este plan

Ninguna corrida persistida del motor, ninguna escritura en el precursor, ningún cambio en el generador de la vista ni en la política de scoring, ninguna instalación o actualización de skills. Cada corrida persistida requiere su autorización, como fija VCX-D035; la regla de triage, si se generaliza, requiere registro propio.
