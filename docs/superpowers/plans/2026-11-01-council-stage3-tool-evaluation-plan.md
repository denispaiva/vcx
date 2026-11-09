# Etapa 3 de `brix-llm-council`: plan de la evaluación de tooling

Fecha: 2026-11-01. Estado: propuesta; nada ejecutado. Continúa el [reporte de la etapa 2](../reports/2026-11-01-council-stage2-runs.md). Marco: VCX-D033 y VCX-D035 en el [registro de decisiones](../../decisions/README.md); procedimiento en el [diseño de evaluación con registro en VCX](../specs/2026-11-01-tooling-evaluation-in-vcx-design.md).

## Autoridad requerida y no otorgada todavía

VCX-D035 aprueba el procedimiento, pero «no autoriza evaluar `brix-llm-council`»: esta corrida exige una autorización aparte, que este plan pide. Cubre la corrida en seco, la persistida, la decisión humana, la línea de procedencia, el commit en VCX y la regeneración de la vista. No se pide escritura en el precursor: el usuario fijó el 2026-11-01 que nada se edita allí, y VCX-D035 lo aplica a la evaluación. Por eso este plan no sigue la vía de VCX-D033 decisión 4, que preveía escribir dos archivos en el precursor.

## Entrada fijada

| Campo | Valor |
|---|---|
| `id` | `brix-llm-council` |
| `type` | `skill` |
| `evaluatedRef` | `vcx@45f961a48236d51a42106ea153578f64900d84f3:brix/.claude/skills/brix-llm-council/`. VCX-D035 fija el último commit de VCX que toca la carpeta; `74c9db5` y `45f961a` solo cambian PROVENANCE.md (enlace a este plan y alineación con VCX-D035), y SKILL.md no cambia desde `ce392b1`, que corrige los hallazgos de la etapa 2. La carpeta no tiene cambios sin commit (comprobado el 2026-11-01). Si vuelve a cambiar antes de correr, se usa el nuevo último commit y se registra |
| `sourceUrl` | `file:brix/.claude/skills/brix-llm-council`, según VCX-D035. No existe repositorio público que contenga la skill; si existiera al correr, VCX-D033 decisión 3 obliga a declararlo, y se consulta al usuario antes de seguir. Con `file:` el motor no consulta GitHub y `community` queda `unavailable` |
| Comparador de `incrementalValue` | `/council` del precursor en `f86a2a7`, SHA-256 `bcc70adc…7885004`, con la tabla de diferencias de [PROVENANCE.md](https://github.com/denispaiva/brix/blob/main/.agents/skills/brix-llm-council/PROVENANCE.md#diferencias-frente-a-council) |
| `--now` | Fijado al correr en seco y reutilizado en la corrida persistida |

## Precondiciones del motor, medidas el 2026-11-01

| Dato | Valor |
|---|---|
| `git --no-optional-locks -C ../blends status --porcelain --ignored -- vc/brix/packages/cli vc/tooling/scoring-policy.json` | Vacío |
| `precursorHead` | `f86a2a7df72e55bbb97451c1a35ef3c03b961fc3` |
| `cliTree` | `889332c5d1065a3a39e25889587f503caad40195` |
| `policySha256` | `ce6e1a319f1f296cdf491fe38dfa32ee08306f9ba6dedcadac21f9cd5ad49161`, `formulaVersion` 1.6.0 |

Se vuelven a medir inmediatamente antes y después de correr. Si difieren de esta tabla, se registra y se pregunta antes de seguir; si difieren entre antes y después, la corrida se invalida.

## Subfactores

Los 23 van en el archivo de evidencia. Aquí se fija solo disponibilidad y fuente; los puntajes se asignan al correr, con `rationale` y `evidenceRefs` fechados, y no se ajustan para que la skill apruebe.

| Factor | Subfactor | Disponibilidad | Fuente y método |
|---|---|---|---|
| maintenance | los cuatro | unavailable | VCX-D035: no aplican a una skill propia de un día, sin repositorio público, releases ni gestor de issues |
| security | `vulnerabilityStatus` | unavailable | Sin código ejecutable propio ni base de avisos aplicable |
| security | `sourceProvenance` | available | Autoría propia, PROVENANCE.md con SHA del comando de origen, sin texto de terceros; rubric |
| security | `securityHygiene` | available | VCX sin CI ni escaneo de secretos; contenido incrustado tratado como dato y probado en la corrida 2 (C11, C12); rubric |
| security | `permissionTransparency` | available | SKILL.md declara lecturas, contexto del host, escritura, tope de invocaciones y runner; rubric |
| fit | `capabilityGapCoverage` | available | Consejo sobre cualquier documento con pregunta explícita, frente a `/council` atado a `ideas/<slug>/`; rubric |
| fit | `technicalCompatibility` | available | Corrió en Claude Code con subagentes en las etapas 1 y 2; rubric |
| fit | `incrementalValue` | available | Diferencias frente a `/council`, con los costos que agrega (verificación manual del orquestador); rubric |
| fit | `observedOutcome` | available | Solo la corrida 1 de la etapa 2, sobre un documento real: tras leerla, el usuario autorizó revisar VCX-D031. Una observación, sin grupo de control; las corridas 2 y 3 son sintéticas y no cuentan, ni las trazas de `/council` del precursor; rubric |
| fit | `adoptionSimplicity` | available | Copia de una carpeta por consumidor; metric |
| fit | `observedAdoption` | unavailable | Sin registro de uso: la skill no está en `vc/tooling/usage/records/` ni hay otro contador; las corridas de prueba no son adopción |
| engineering | `automatedVerification` | available | VCX-D035 toma como evidencia las salidas de la etapa 2: 16 criterios fijados antes de ejecutar y verificados con herramientas sobre las transcripciones. No es una suite automatizada repetible, y el puntaje lo refleja; metric |
| engineering | `documentationQuality` | available | SKILL.md, PROVENANCE.md, diseño y reportes de etapa; rubric |
| engineering | `versioningDiscipline` | available | Sin versión semántica ni tags; solo SHA de Git; metric |
| engineering | `compatibilityEvidence` | available | Un host y una familia de modelo, 27 invocaciones medidas; metric |
| engineering | `dependencySimplicity` | available | Sin dependencias propias; requiere subagentes del host y `shasum`; metric |
| sustainability | `costPredictability` | available | Tope de 11 invocaciones y tokens medidos en la etapa 2 (36 a 159 mil de salida por corrida); dinero `not_measured`, que no es costo cero; rubric |
| sustainability | `portability` | available | Atada al formato de skills de Claude Code y a subagentes; rubric |
| sustainability | `reversibility` | available | Borrar la carpeta; la skill solo crea reportes nuevos sin sobrescribir; metric |
| sustainability | `operatingOverhead` | available | El orquestador cuenta palabras, anonimiza, recorta y calcula el hash a mano; rubric |

`confidenceInputs.sourceReliability` se fija al correr y declara que las fuentes son el Git local y reportes propios, sin verificación externa.

## `riskFlags`

Los 12 presentes. Verdadero solo `localWriteReversible`: la skill crea un reporte nuevo en el destino autorizado y nunca sobrescribe. `networkAccess` es falso porque la versión evaluada solo usa el runner `subagent`: las llamadas al modelo son las del host, no un canal que la skill abra; el runner `command` queda reservado y su evaluación deberá declararlo. `scopedLocalReadOnly` es falso porque escribe. `broadScope` es falso porque las lecturas son una lista cerrada; el contexto del host es un canal declarado, no un alcance que la skill amplíe. Los ocho restantes, falsos. Con esta configuración el riesgo es `medium` y el gate no exige excepción.

## Pasos

Los del [procedimiento de VCX-D035](../specs/2026-11-01-tooling-evaluation-in-vcx-design.md#procedimiento), sin envoltorio: es la primera evaluación y no hay registro previo en `brix/tooling/` que pisar (la carpeta no existe).

1. Repetir las precondiciones y guardar la foto de control del precursor: `git --no-optional-locks status --porcelain` y una marca de tiempo para `find -newer`.
2. Escribir la evidencia en el scratchpad de la sesión.
3. En seco, desde la raíz de VCX: `node ../blends/vc/brix/packages/cli/bin/brix.js tool score evaluate --input <evidencia> --policy ../blends/vc/tooling/scoring-policy.json --output-dir brix/tooling --now <ISO> --dry-run`.
4. Reportar puntaje, confianza, riesgo y recomendación base. Iterar solo con información nueva del usuario, sobre `fit`.
5. Pedir la decisión humana con las reglas de lectura fijadas en el diseño: `hold` no admite; `advance_with_reservations` o confianza `low` admiten como mucho `approved_with_exception`, con reserva escrita y revisión a 30 días; `advance` con confianza `medium` o `high` permite `approved`.
6. Persistir: el mismo `evaluate` sin `--dry-run`, luego `decide` con los flags del estado elegido, y una línea por comando en `brix/tooling/score-runs.jsonl`.
7. Verificar, commitear en VCX y regenerar la vista de la matriz con `python3 -I docs/exports/build_tooling_matrix_view.py`. El cambio del generador para leer `brix/tooling/` es otra autorización de VCX-D035; si todavía no se hizo, la vista no mostrará esta decisión y se declara.

## Criterios de aceptación, fijados antes de ejecutar

Los seis del diseño de VCX-D035 para esta corrida, más dos de este plan:

| ID | Criterio | Cómo se verifica |
|---|---|---|
| E1 | Todo archivo nuevo o modificado está bajo `brix/tooling/`, salvo `docs/exports/` al regenerar la vista | `git status` de VCX |
| E2 | `score-runs.jsonl` tiene una línea por comando persistido, con la procedencia completa | Conteo y lectura |
| E3 | El precursor queda igual antes y después | `git --no-optional-locks status --porcelain` y `find -newer` |
| E4 | El registro contiene `humanDecision` con autor, fecha y fundamento | Lectura del registro |
| E5 | Si `evidenceCoverage` queda bajo 50, el fundamento de la decisión lo menciona con el número | Lectura |
| E6 | `community` sin evidencia por `sourceUrl` no GitHub | Lectura del registro |
| E7 | La evidencia tiene los 23 subfactores y los 12 `riskFlags` | Conteo con herramienta |
| E8 | `observedAdoption` es `unavailable` y ningún `rationale` presenta corridas de prueba como adopción | Lectura |

## Riesgos y límites

- La evaluación la hace un asistente de la misma familia de modelo que escribió la skill: no es una revisión independiente y los puntajes `rubric` lo llevan como sesgo declarado.
- Sin `community` ni `maintenance`, la cobertura y la confianza saldrán bajas, y la admisión vencerá a los 30 días si la confianza es `low`. Es el dato correcto para una herramienta de un día; no se compensa.
- El puntaje no es comparable con el de candidatas externas, que sí tienen `community` y `maintenance`.
- El motor corre en el estado de trabajo del precursor, sin versión fijada; las precondiciones detectan un cambio, no lo impiden.
- Los controles son manuales hasta que exista el envoltorio que pide VCX-D035 antes de una reevaluación o de un segundo candidato.
