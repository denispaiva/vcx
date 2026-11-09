# Etapa 3 de `brix-llm-council`: evaluación de tooling con registro en VCX

Fecha: 2026-11-01, hora local (registro del motor en UTC: 2026-11-02). Evidencia fechada; la fuente canónica es el registro en [`brix/tooling/evaluations/`](../../tooling/evaluations/brix-llm-council.evaluation.json). Plan seguido: [plan de la etapa 3](../plans/2026-11-01-council-stage3-tool-evaluation-plan.md), procedimiento de VCX-D035.

Autoridad: el usuario autorizó la evaluación («Autorizo la evaluación»). Ante el resultado eligió «Excepción registrada», tras preguntar «Si este lo construimos nosotros por qué no lo aprobaríamos?».

## Resultado

| Dato | Valor |
|---|---|
| Puntaje | 58,0 / 100 |
| Confianza | `medium` (70,2) |
| Cobertura de evidencia | 56 |
| Riesgo | `medium`, solo por `localWriteReversible` |
| Recomendación base | `do_not_advance` (umbral de reservas: 60) |
| Por factor | `community` y `maintenance` sin evidencia por diseño; `security` 61,5; `fit` 65,6; `engineering` 41,5; `sustainability` 60,5 |
| Decisión humana | `approved_with_exception`, por Denis Paiva, `decidedAt` 2026-11-02T00:53:21Z, revisión el 2026-12-02, riesgo aceptado |
| Vencimiento de la admisión | `expiresAt` 2027-01-31: el motor fija 90 días con confianza `medium` |

**Excepción, no cumplimiento** (registrada también como nota en el [registro de decisiones](../../decisions/README.md)). Las reglas de lectura de VCX-D035, fijadas antes de puntuar, no admiten una recomendación `do_not_advance`: solo permitían `rejected` o `deferred`. El usuario admitió la skill por su autoridad. El fundamento está completo en `humanDecision.rationale`, con las reservas: no hay verificación automatizada, la corrección `ce392b1` no se reverificó con una corrida, se probó en un solo host y una sola familia de modelo, y los puntajes `rubric` los asignó el mismo modelo que escribió la skill. Los puntajes no se ajustaron después de ver el número. Lo que más baja el puntaje es `engineering`: `automatedVerification` 20, `versioningDiscipline` 20 y `compatibilityEvidence` 25. Le sigue `securityHygiene` con 35.

## Procedencia

| Campo | Valor |
|---|---|
| `evaluatedRef` | `vcx@45f961a48236d51a42106ea153578f64900d84f3:brix/.claude/skills/brix-llm-council/` |
| Árbol evaluado | `647562ec589e81dcb327e03bdfd638b590dd4bf2` |
| `precursorHead` · `cliTree` | `f86a2a7` · `889332c5d1065a3a39e25889587f503caad40195` |
| `policySha256` · `formulaVersion` | `ce6e1a31…cd5ad49161` · 1.6.0 |
| `--now` | `2026-11-02T00:50:00Z` en `evaluate` y `decide` |
| Líneas de procedencia | Dos en [`score-runs.jsonl`](../../tooling/score-runs.jsonl), una por comando |

Durante la evaluación, otra sesión reescribió el correo del historial de `vcx` con autorización del usuario. `45f961a` pasó a ser `8bbb542`, con el mismo árbol de la skill (`647562e`), y [la tabla de correspondencia](2026-11-01-vcx-noreply-rewrite.md#correspondencia-de-sha) resuelve el SHA viejo. `evaluate` corrió antes de la reescritura, así que el `evaluatedRef` era correcto al evaluar. No se reevaluó para cambiarlo, porque VCX-D035 exige el envoltorio antes de una reevaluación.

## Criterios de aceptación

| ID | Resultado | Evidencia |
|---|---|---|
| E1 | Cumplido: los archivos nuevos del motor están todos bajo `brix/tooling/`; el resto del commit son documentos de VCX, ninguno del precursor | `git status` |
| E2 | Cumplido: dos líneas, una por `evaluate` y otra por `decide`, con los diez campos de VCX-D035; el SHA-256 del archivo de `history/` coincide con el `evaluationSha256` de la primera línea | `shasum` |
| E3 | Cumplido: `git status --porcelain` del precursor con el mismo hash (`61dc1864dc54`) antes y después; `.git/index` y `.git/HEAD` sin cambio de mtime; `find -newer` vacío; procedencia del motor idéntica en las cuatro mediciones | Comandos con `--no-optional-locks` |
| E4 | Cumplido: `humanDecision` con autor, fecha y fundamento | Registro |
| E5 | No aplica: la cobertura es 56, no menor que 50. El fundamento la menciona igual | Registro |
| E6 | Cumplido: `factorScores.community` nulo, sin llamada al colector por `sourceUrl` `file:` | Registro |
| E7 | Cumplido: 23 subfactores y 12 `riskFlags` | Conteo |
| E8 | Cumplido: `observedAdoption` `unavailable`, sin corridas de prueba presentadas como adopción | Evidencia |

## Cambios derivados

- La [matriz](../../architecture/tooling-matrix.md) pasa la fila de consejo a «Asignado», porque bajo VCX-D035 la admisión es la decisión vigente en `brix/tooling/`, igual que la fila de `gmail`, aprobada con excepción. Desde `cbf0cb9` el generador lee este registro.
- SKILL.md y PROVENANCE.md cambian solo su estado y sus pendientes. Por eso la carpeta ya no está en el `evaluatedRef`; la próxima evaluación usará el último commit de la carpeta.

## Pendientes

Ordenados como pedidos en el [plan hacia la revisión](../plans/2026-11-01-council-review-backlog-plan.md).

- Revisión el 2026-12-02, o antes si hay evidencia nueva: una corrida que verifique la corrección de la etapa 2, usos reales para `observedOutcome` y un contador de uso para `observedAdoption`.

Cerrados después de esta evaluación: el envoltorio de VCX-D035, [`brix/tooling/score-run.mjs`](../../tooling/score-run.mjs) (`6b47396`), probado solo en seco; y el generador de la vista, que lee primero `brix/tooling/` y muestra la fecha de revisión (`cbf0cb9`).
