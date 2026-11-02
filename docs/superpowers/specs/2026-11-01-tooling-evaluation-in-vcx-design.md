# Evaluación de tooling con registro en VCX

Fecha: 2026-11-01. Estado: **propuesta del asistente**, revisada por una sesión independiente (nota orientativa 6/10, trece hallazgos, incorporados abajo) y pendiente de aprobación del usuario. No ejecuta evaluaciones, no cambia la política de admisión ni el generador de la vista.

## Problema

El usuario fijó el 2026-11-01: «No quiero que edites nada en el precursor, todos los cambios deberían vivir en el nuevo destino vcx/» ([registro](../../decisions/README.md), precisión sobre VCX-D028). El proceso vigente de admisión, Scoring Skill con su punto de entrada `/tool`, escribe la evaluación, la evidencia, la narrativa y el inventario dentro del precursor. Sin otro procedimiento, ninguna herramienta nueva puede admitirse. En particular, `brix-llm-council` quedaría sin evaluar, aunque el usuario necesita «si o sí» una skill para Reporte de Consejo.

## Restricciones

- No escribir en `../blends`, ni siquiera en `.git`: para consultar su estado se usa `git --no-optional-locks`.
- No copiar el motor ni la política (AGENTS: no copiar implementaciones; VCX-P9: una fuente por dato).
- Mantener la separación entre el cálculo, que produce el motor, y la decisión, que es humana (VCX-P5, VCX-P7).
- Dejar registro reproducible de con qué se calculó (VCX-P1).

## Evidencia de partida

El [reporte de verificación](../reports/2026-11-01-scoring-engine-external-output-check.md) midió que el CLI público `brix tool score` del precursor evalúa y decide escribiendo solo donde indican `--output-dir` y `--narrative-doc`. Los 952 `.roadmap.json` del precursor conservaron su hash; ni el árbol de trabajo ni `.git/index` cambiaron. `decide` no registra nada en el inventario: eso lo hacía el envoltorio `vc/tools/evaluate-tooling.mjs`, que este procedimiento no usa.

El mismo reporte encontró cuatro límites que el diseño tiene que cubrir:

1. El registro guarda `formulaVersion`, pero no el hash de la política ni la revisión del motor.
2. `evidenceInputRef` depende del directorio desde el que se corre el CLI, y `sourceEvidence` apunta a una ruta de Blends que no existe fuera de él.
3. Una decisión puede sobrescribirse sin error; solo `history/` conserva la anterior.
4. El motor corre en el estado de trabajo del precursor, sin versión fijada.

## Alternativas

| Opción | A favor | En contra | Juicio |
|---|---|---|---|
| A. Copiar motor y política a `vcx/` | Independencia inmediata | Implementación copiada y segunda fuente de política; prohibido por AGENTS | Descartada |
| B. Puntuar a mano con la política como guía | Sin dependencia de código | No reproducible; el puntaje deja de ser comparable con el del motor | Descartada |
| C. Esperar a que Brix se extraiga | Sin dependencias transitorias | Bloquea la capacidad del consejo por tiempo indefinido | Descartada |
| **D. Ejecutar el CLI del precursor en solo lectura, con salida en VCX** | Sin copiar código ni escribir en el precursor; mismo motor y misma escala | Dependencia transitoria de una ruta del precursor; procedencia a completar fuera del motor | **Propuesta** |

Con D, la interfaz es la misma que tendrá Brix como repositorio propio. Al extraerlo, solo cambia la ruta del binario y el procedimiento sigue igual.

## Propuesta

### Dónde vive el registro

`brix/tooling/` es el contenedor que recibe `--output-dir`. La [matriz de responsabilidades](../../architecture/responsibility-matrix.md) asigna a Brix el catálogo, y la carpeta viajará con el producto.

- `brix/tooling/evaluations/<id>.evaluation.json` y `<id>.evidence.json`: los escribe el motor.
- `brix/tooling/evaluations/history/<id>/…`: también la escribe el motor, de forma inmutable.
- `brix/tooling/score-runs.jsonl`: procedencia, una línea por cada `evaluate` o `decide` persistido. Campos: `candidate`, `command` (subcomando y flags completos), `now` (el valor pasado a `--now`), `precursorHead`, `cliTree` (hash del árbol `vc/brix/packages/cli`, que incluye `bin/` y `src/`, no solo `scoring/`), `policySha256`, `formulaVersion`, `evaluationSha256` (hash del `evaluation.json` resultante), `previousStatus` (estado del registro antes del comando) y `operator`. `evaluationSha256` enlaza cada línea con su registro; cada archivo de `history/` debe tener su línea.

La carpeta se versiona hoy en la raíz de VCX, como el resto de `brix/`, y se traslada con el producto cuando Brix se extraiga a su repositorio (VCX-D025).

No se genera narrativa: se omite `--narrative-doc`. Los `rationale` ya están en la evidencia, y la vista de la matriz es la lectura humana; una narrativa sería un tercer lugar que mantener. El campo `sourceEvidence` del registro queda como literal heredado sin valor. El motor calcula `evidenceInputRef` relativo al directorio de trabajo (`engine.mjs`, `buildEvaluationRefs`): es determinista mientras se corra desde la raíz de VCX, pero dejará de resolver al extraer Brix. Ninguno de los dos se usa como identificador; la procedencia la da `score-runs.jsonl`.

### Procedimiento

Sigue los pasos 1 a 5 y 8 del comando `/tool` del precursor, con estas diferencias:

1. **Identificar.** En una skill propia, `evaluatedRef` es el último commit de VCX que toca su carpeta, y esa carpeta no puede tener cambios sin commit. En una de terceros se mantiene la regla vigente: tag, release o SHA.
2. **Precondiciones del motor.** `git --no-optional-locks -C ../blends status --porcelain --ignored -- vc/brix/packages/cli vc/tooling/scoring-policy.json` debe salir vacío. Si sale algo, no se corre: un motor o una política con cambios locales, o con archivos ignorados dentro de esas rutas, no son reproducibles. Inmediatamente antes de correr se calculan `precursorHead`, `cliTree` (`git --no-optional-locks -C ../blends rev-parse HEAD:vc/brix/packages/cli`) y `policySha256`, y se vuelven a calcular después. Si difieren, la corrida se invalida. Es un control de proceso a cargo del operador, no una garantía del motor.
3. **Estado previo del registro.** Antes de cualquier `evaluate` o `decide`, se lee `status` y `humanDecision` de `brix/tooling/evaluations/<id>.evaluation.json`, si existe. El motor no protege una decisión vigente: `evaluate` la archiva en `history/` y deja el registro en `decision_pending`, y `decide` acepta otra decisión sobre un registro ya decidido (solo rechaza `pending`). Reemplazar una decisión vigente exige que el usuario lo sepa antes, como pide `/tool` en su paso 1 y VCX-P7.
4. **Evidencia.** Va en el scratchpad y lleva los 23 subfactores. En una skill propia, `sourceUrl` usa el esquema `file:` con la ruta de su carpeta, nunca la URL de GitHub: con una URL de GitHub el colector consulta la API y puntúa `community` con datos de un repositorio que no es la skill. `community` y `maintenance` quedan `unavailable`, y su `rationale` explica si no aplican o si falta el dato. No se agrega un perfil nuevo: el diseño del consejo pide verificar antes qué permite el proceso vigente. La cobertura baja y se informa así; no se compensa con valores favorables.
5. **En seco.** Desde la raíz de VCX, con un `--now` fijo que se reutiliza en la corrida persistida:
   `node ../blends/vc/brix/packages/cli/bin/brix.js tool score evaluate --input <evidencia> --policy ../blends/vc/tooling/scoring-policy.json --output-dir brix/tooling --now <ISO> --dry-run`.
   Se itera hasta que el número quede firme.
6. **Decisión humana.** La pide el agente; el CLI no decide. El gate de riesgo se respeta: con un flag `high` o superior, la única aprobación posible es `approved_with_exception`, con su reserva escrita.
7. **Persistir.** Se corren el mismo `evaluate` sin `--dry-run` y luego `decide --id --status --by` con los flags que exija el estado, y se agrega una línea a `score-runs.jsonl` por cada comando. `decidedAt` usa el reloj real aunque se pase `--now`; se registra tal cual.
8. **Verificar.**
   - El estado del precursor es igual antes y después, medido con `--no-optional-locks`.
   - Solo cambiaron archivos bajo `brix/tooling/`.
   - La vista regenerada muestra la nueva decisión.
   - Cada archivo nuevo en `history/` tiene su línea en `score-runs.jsonl`.
   - Commit en VCX que incluye la evidencia y la línea de procedencia.

### Cómo se lee el resultado

Se fija antes de puntuar, para no ajustar el criterio al número; el diseño del consejo prohíbe fijar pesos para que una skill apruebe.

- `hold` no admite. La decisión posible es `rejected` o `deferred`.
- `advance_with_reservations`, o cualquier resultado con confianza `low`, admite como mucho con `approved_with_exception`, con la reserva escrita y revisión a 30 días.
- `advance` con confianza `medium` o `high` permite `approved`, si el gate de riesgo no exige excepción.
- El puntaje de una skill propia se calcula sin `community` ni `maintenance`; no se compara con el de candidatas externas como si fuera la misma escala.

### Admisión sin inventario del precursor

Desde el 2026-11-01, una herramienta queda admitida con una decisión `approved` o `approved_with_exception` **vigente** registrada en `brix/tooling/evaluations/`. Vigente significa que no pasó su `expiresAt`. El motor fija 30 días si la confianza es `low` y 90 en otro caso (`computeExpiresAt`), así que una skill propia con poca evidencia puede vencer pronto. Una admisión vencida exige una nueva evaluación y no cuenta como admitida. Las decisiones anteriores siguen leyéndose del inventario del precursor, como antecedente. El propósito, el dueño y la ubicación de cada herramienta ya están en la [matriz](../../architecture/tooling-matrix.md); no se crea otro inventario hasta la migración, como prevé VCX-D028.

Con esto, la matriz y su vista cambian así:

- **Regla de promoción de la matriz:** «candidato → asignado exige admisión» pasa a citar esta fuente.
- **Generador:** lee primero `brix/tooling/evaluations/` y, si una herramienta no tiene registro ahí, el del precursor. Una admisión vencida se muestra como sin admisión.
- **Popup:** indica de cuál de las dos fuentes viene la evaluación.

El rechazo de `llm-council-skill` sigue registrado en VCX como decisión, sin una evaluación nueva: reevaluarla solo para dejar constancia del rechazo sería gastar trabajo sin aportar información.

## Riesgos

- **El precursor cambia el motor o la política.** La precondición 2 y `score-runs.jsonl` lo hacen visible. Si cambia `policySha256`, los puntajes anteriores dejan de ser comparables, y la vista debe mostrarlo antes de que se pongan uno junto al otro.
- **El precursor se mueve o desaparece** durante la migración. Se corrige la ruta del binario, y nada más. Si Brix no está extraído para entonces, se usa el clon de autoría de VCX-D030 bajo su propio gobierno.
- **Doble fuente durante la transición.** Que la misma herramienta tenga registro en el precursor y en VCX es el caso esperado: prevalece el de VCX, que es posterior y cumple la regla del usuario. El generador lo debe señalar.
- **Ejecutar código del precursor.** Es código del propio usuario, se lee antes de correrlo y no tiene dependencias externas (`node:` y módulos locales). Solo usa la red si `sourceUrl` es de GitHub. El reporte lo infiere del código y no lo midió con captura de tráfico.

## Primera corrida: `brix-llm-council`

Se ejecuta en una autorización aparte. Dependencias que hay que resolver antes:

- **Commitear la skill.** Hoy `SKILL.md` y `PROVENANCE.md` tienen cambios sin commit de otra sesión; sin commit no hay `evaluatedRef`.
- **Obtener evidencia de comportamiento.** El diseño del consejo exige revisar las instrucciones y además una ejecución acotada con siete casos y dos criterios de hash, fijados antes de ejecutar. Si al evaluar ya existen salidas de esa ejecución (el plan de la etapa 2 la propone), son la evidencia de `automatedVerification` y `observedOutcome`. Si no existen, esos subfactores quedan `unavailable` y, según las reglas de lectura, la admisión no puede ser limpia.

Criterios de aceptación:

1. Todos los archivos nuevos o modificados están bajo `brix/tooling/`. Al regenerar la vista también cambian `docs/exports/`, pero ni la matriz ni el registro de decisiones.
2. `score-runs.jsonl` tiene una línea por cada comando persistido, con los cuatro campos de procedencia completos.
3. El estado del precursor es idéntico antes y después.
4. El registro contiene `humanDecision` con autor, fecha y fundamento. Que se vea en el popup es criterio de la etapa del generador.
5. Si `evidenceCoverage` queda por debajo de 50, el `rationale` de la decisión lo menciona con el número.
6. El registro muestra `community` sin evidencia por `sourceUrl` no GitHub, lo que indica que el colector no consultó la API.

## Qué decide el usuario

1. Aprobar el enfoque D y la ubicación `brix/tooling/`.
2. Omitir la narrativa.
3. Cuándo hacer un envoltorio delgado en `brix/` que haga cumplir las precondiciones 2 y 3 y escriba `score-runs.jsonl`. La revisión mostró que los controles manuales se omiten sin que nada lo detecte. La propuesta es correr a mano solo la primera evaluación, que no tiene registro previo en VCX que pisar, y exigir el envoltorio antes de cualquier reevaluación o de un segundo candidato.

Aprobar este documento no autoriza evaluar `brix-llm-council` ni cambiar el generador. Cada una de esas acciones se pide aparte.
