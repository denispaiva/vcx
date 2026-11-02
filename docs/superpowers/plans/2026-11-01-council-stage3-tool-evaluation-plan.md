# Etapa 3 de `brix-llm-council`: plan de la evaluación con `/tool`

Fecha: 2026-11-01. Estado: propuesta; nada ejecutado. Continúa el [reporte de la etapa 2](../reports/2026-11-01-council-stage2-runs.md). Marco: VCX-D033, decisiones 3 y 4, en el [registro de decisiones](../../decisions/README.md).

## Autoridad requerida y no otorgada todavía

La evaluación escribe en el precursor, que está en solo lectura por VCX-D026. VCX-D033 decisión 4 acota esa escritura a dos archivos y exige una autorización explícita posterior, que este plan pide y no presupone. Sin ella no se corre ningún paso que escriba; el paso en seco no escribe y tampoco se corre antes de que el usuario apruebe este plan.

## Hecho que cambia el alcance de VCX-D033 decisión 4

El guion `/tool` del precursor (`.claude/commands/tool.md`) no escribe dos archivos, sino más (lectura del 2026-11-01, precursor en `f86a2a7`):

| Paso de `/tool` | Escribe en el precursor |
|---|---|
| 6, `evaluate-tooling.mjs evaluate` | `vc/tooling/evaluations/<id>.evaluation.json`, `<id>.evidence.json` y una sección nueva en `vc/docs/tooling/evaluations.md` |
| 7, `decide` | Reescribe `<id>.evaluation.json`, crea `vc/tooling/evaluations/history/<id>/` y agrega la decisión a `evaluations.md`; con `approved*` el envoltorio además registra la herramienta en un `.roadmap.json` y regenera `roadmap/data.js` |
| Cierre | Rama `tooling/<id>-evaluation`, commit y validadores (`npm run lint` incluido) |

La [verificación del motor](../reports/2026-11-01-scoring-engine-external-output-check.md) midió que `brix tool score` acepta `--policy`, `--output-dir` y `--narrative-doc`, y que los flags prevalecen sobre `brix.config.json` (`engine.mjs`, resolución de rutas). Con `--output-dir <blends>/vc/tooling` y `--narrative-doc` fuera del precursor, `evaluate` escribe exactamente los dos archivos de VCX-D033 decisión 4. `history/` solo se crea si ya existe un registro del mismo id; hoy no existe (`ls vc/tooling/evaluations/brix-llm-council.*` sin coincidencias). Por eso este plan usa el motor directo y no el envoltorio, y no corre `decide` en el precursor.

## Entrada fijada

| Campo | Valor |
|---|---|
| `id` | `brix-llm-council` |
| `type` | `skill` |
| `evaluatedRef` | `vcx@ce392b1f6909d0a46a96b9bf58cc4c7567d50cfe:brix/.claude/skills/brix-llm-council/SKILL.md`: SHA de la raíz de VCX que contiene la corrección de la etapa 2, más la ruta de la skill |
| `sourceUrl` | Ausente (`null`): no existe repositorio público de Brix que contenga la skill. Por VCX-D033 decisión 3 se vuelve a comprobar el día de la corrida; si existiera, se declara aunque comunidad puntúe bajo. Sin `sourceUrl` el motor no llama al colector y `community` queda `unavailable`, que es el comportamiento correcto |
| Comparador de `incrementalValue` | `/council` del precursor en `f86a2a7`, SHA-256 `bcc70adc…7885004`, con la tabla de diferencias de [PROVENANCE.md](../../../brix/.claude/skills/brix-llm-council/PROVENANCE.md#diferencias-frente-a-council) |
| Procedencia del cálculo | Política `vc/tooling/scoring-policy.json`, SHA-256 `ce6e1a31…cd5ad49161`, último commit `a41b2382`; motor `engine.mjs`, último commit `a8f3eb7f`. El registro del motor no guarda ninguno de los dos, así que se anotan en el reporte de VCX |

## Subfactores

Los 23 van en el archivo de evidencia. Los puntajes se fijan al correr, con su `rationale` y `evidenceRefs` fechados; aquí se fija solo disponibilidad y fuente para que no se ajusten después de ver el número.

| Factor | Subfactor | Disponibilidad | Fuente y método |
|---|---|---|---|
| maintenance | `activityRecency` | available | `git log` de la ruta en VCX; metric |
| maintenance | `releaseContinuity` | available | Sin tags ni releases: cero, como el precedente `llm-council-skill`; metric |
| maintenance | `commitContinuity` | available | Commits de la ruta, todos del 2026-11-01; metric |
| maintenance | `responseHealth` | unavailable | Sin repositorio público ni gestor de issues |
| security | `vulnerabilityStatus` | unavailable | Sin código ejecutable propio ni base de avisos aplicable |
| security | `sourceProvenance` | available | Autoría propia, PROVENANCE.md con SHA del comando de origen, sin texto de terceros; rubric |
| security | `securityHygiene` | available | VCX sin CI ni escaneo de secretos; contenido incrustado tratado como dato y probado en la corrida 2 (C11, C12); rubric |
| security | `permissionTransparency` | available | SKILL.md declara lecturas, contexto del host, escritura, tope de invocaciones y runner; rubric |
| fit | `capabilityGapCoverage` | available | Consejo sobre cualquier documento con pregunta explícita, frente a `/council` atado a `ideas/<slug>/`; rubric |
| fit | `technicalCompatibility` | available | Corrió en Claude Code con subagentes en las etapas 1 y 2; rubric |
| fit | `incrementalValue` | available | Diferencias medidas frente a `/council`, con los costos que agrega (verificación manual del orquestador); rubric |
| fit | `observedOutcome` | unavailable | Sin fuente de resultado observado; las corridas de las etapas 1 y 2 fueron pruebas, no uso, y no se reutilizan |
| fit | `adoptionSimplicity` | available | Copia de una carpeta por consumidor; metric |
| fit | `observedAdoption` | unavailable | Sin registro de uso: no está en ningún roadmap del precursor ni en `vc/tooling/usage/records/`, y las corridas de prueba no cuentan |
| engineering | `automatedVerification` | available | Cero pruebas automatizadas; las etapas fueron verificación manual; metric |
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

Los 12 presentes. Verdaderos: `localWriteReversible`, porque la skill crea un reporte nuevo en el destino autorizado y nunca sobrescribe. Falsos los once restantes. `networkAccess` es falso porque la versión evaluada solo usa el runner `subagent`: las llamadas al modelo son las del host, no un canal que la skill abra; el runner `command` queda reservado y su evaluación deberá declararlo. `scopedLocalReadOnly` es falso porque escribe. `broadScope` es falso porque las lecturas son una lista cerrada; el contexto del host es un canal declarado, no un alcance que la skill amplíe.

## Pasos

1. **Precondiciones**, sin escribir: HEAD del precursor y SHA-256 de política y motor iguales a los de la tabla; si difieren, se registra y se pregunta antes de seguir. Ningún `brix-llm-council.*` en `vc/tooling/evaluations/`; si apareció, parar, porque `evaluate` escribiría en `history/`. Foto de control: `git status --porcelain` del precursor y una marca de tiempo para `find -newer`.
2. **Evidencia** en el scratchpad de la sesión, con los valores de este plan.
3. **En seco**: `node <blends>/vc/brix/packages/cli/bin/brix.js tool score evaluate --input <evidencia> --policy <blends>/vc/tooling/scoring-policy.json --output-dir <blends>/vc/tooling --narrative-doc <vcx>/docs/superpowers/reports/<fecha>-tool-evaluation-brix-llm-council.md --dry-run`, con el directorio de trabajo en la raíz del precursor para que `evidenceInputRef` quede como en el resto del registro. No escribe nada.
4. **Reporte al usuario** con puntaje, confianza, riesgo y recomendación base. Se itera solo sobre `fit` con información del usuario, como prevé `/tool`.
5. **Corrida real**, solo con la autorización escrita: el mismo comando sin `--dry-run`. Controles después: `git status --porcelain` del precursor igual a la foto más exactamente dos rutas nuevas, y `find -newer` sin otros archivos. Cualquier otra escritura se reporta como incidente.
6. **Decisión humana** con `approved`, `approved_with_exception`, `rejected` o `deferred`, registrada en VCX según VCX-D033 decisión 4. No se corre `decide` en el precursor: su registro queda `decision_pending` y eso se declara.

## Criterios de aceptación, fijados antes de ejecutar

| ID | Criterio | Cómo se verifica |
|---|---|---|
| E1 | El archivo de evidencia tiene los 23 subfactores y los 12 `riskFlags` | Conteo con herramienta |
| E2 | `observedAdoption` y `observedOutcome` son `unavailable`; ningún `rationale` cita las corridas de prueba como uso | Lectura del archivo |
| E3 | `sourceUrl` ausente y comprobado el día de la corrida | Registro de la comprobación |
| E4 | La corrida en seco no escribe | `git status` y `find -newer` iguales |
| E5 | La corrida real escribe exactamente dos archivos en el precursor | Mismos controles, diferencia de dos rutas |
| E6 | La narrativa queda en VCX con política, motor y comando registrados | Lectura del reporte |
| E7 | La decisión humana queda en VCX con autoridad, objeto, revisión y alcance | Registro de decisiones |

## Riesgos y límites

- Los dos archivos quedan sin commitear en el precursor, cuyo árbol ya tiene cambios ajenos sin seguimiento: un `git add -A` de otra sesión podría arrastrarlos. Commitearlos exigiría rama y commit en el precursor, fuera del alcance de VCX-D033.
- El precursor no tendrá la decisión humana; su `validate-tooling` verá un `decision_pending`, que es un estado válido.
- La evaluación la hace un asistente de la misma familia de modelo que escribió la skill: no es una revisión independiente y los puntajes `rubric` lo llevan como sesgo declarado.
- Con muchos subfactores indisponibles y sin `community`, la cobertura y la confianza saldrán bajas. Es el dato correcto para una herramienta de un día, no un defecto que haya que compensar.
- El motor del precursor corre en su estado de trabajo, sin pin de versión; la tabla de procedencia permite detectar un cambio, no impedirlo.

## Alternativas que el usuario puede elegir en vez de este alcance

1. **Sin escribir en el precursor**: `--output-dir` también fuera del precursor, con los dos archivos en VCX. Cero escrituras en el precursor, pero contradice el lugar fijado por VCX-D033 decisión 4 y exige revisar esa decisión.
2. **`/tool` completo**: envoltorio, `decide`, rama y commit en el precursor. Sigue el guion al pie de la letra, pero escribe narrativa, `history/`, rama y, si se aprueba, roadmap; excede VCX-D033 decisión 4 y exige revisarla.
