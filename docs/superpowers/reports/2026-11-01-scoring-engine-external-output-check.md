# Verificación: motor de scoring del precursor con salida fuera del precursor

Fecha: 2026-11-01. Evidencia fechada; no sustituye decisiones ni specs. Pregunta: ¿puede `brix tool score` del precursor evaluar y registrar decisiones escribiendo solo fuera de `../blends`?

**Veredicto (medido):** sí, para `evaluate` y `decide`, con `--policy`, `--output-dir` y `--narrative-doc` apuntando fuera del precursor. Hay límites de procedencia que se detallan abajo (la hipótesis se sostiene para evaluar y decidir; no para registrar en roadmaps ni para auditar con qué política/motor se calculó).

## Condiciones de la prueba

- Precursor: `/Users/denis/VibeCoding/blends`, HEAD `f86a2a7df72e55bbb97451c1a35ef3c03b961fc3`. Árbol ya sucio antes de empezar (4 líneas untracked: `.claude/settings.local.json`, `img/`, dos `.migration-*.json` de teyst); no son nuestras.
- Revisión del motor: último commit que toca `engine.mjs` = `a8f3eb7f1`; el de la política = `a41b23820` (leídos con `git log`, solo lectura).
- Comando: `node <blends>/vc/brix/packages/cli/bin/brix.js tool score <evaluate|decide> …`, cwd = directorio de prueba (en scratchpad de sesión, fuera de ambos repos), `--policy <blends>/vc/tooling/scoring-policy.json`, `--output-dir <prueba>/out`, `--narrative-doc <prueba>/narrative.md`, `--now 2026-11-01T12:00:00Z`.
- Candidatos ficticios `smoke-own-skill`, `-b`, `-c`. Evidencia: 23 subfactores con `id` (no `subfactor`); disponibles solo `sourceProvenance`, `capabilityGapCoverage`, `incrementalValue` (70 c/u); `sourceUrl: "file:brix/.claude/skills/smoke"`.
- Control de escrituras antes/después de cada caso: `git --no-optional-locks -C <blends> status --porcelain` (hash idéntico `61dc1864dc54`, 4 líneas), `find <blends> -path <blends>/.git -prune -o -newer <stamp> -print` (vacío), mtime de `.git/index` y `.git/HEAD` sin cambios (1793406015 / 1790967352), y `shasum -c` sobre los 952 `.roadmap.json` del precursor (incluye `.git-trains/*`): todos OK, 0 FAILED. No se ejecutó `npm` ni se escribió nada en el precursor.

## Caso 1 — `evaluate --dry-run` (hecho medido)

```
evaluate --input evidence.json --policy <pol> --output-dir <prueba>/out --dry-run --now 2026-11-01T12:00:00Z
```

- Score **70.0/100**, confianza **medium (54)** (`confidenceScore` 54.25), riesgo **low**, recomendación **advance_with_reservations**, cobertura de evidencia **15** (en el registro real). `community`, `maintenance`, `engineering`, `sustainability`: `unavailable`.
- Termina con `(dry-run: no se escribió nada)`; `out/` quedó vacío; precursor sin cambios.
- Sin red: **inferencia** apoyada en el código y no en una captura de tráfico. `engine.mjs` solo llama al colector si `sourceUrl` casa con `github.com/<owner>/<repo>` (`parseGithubUrl`); con `file:` community queda `unavailable` (medido). No se midió tráfico de red.
- Variante sin `--policy` ni `brix.config.json` en cwd: usa `scoring/default-scoring-policy.json` embebida y da el mismo reporte (70.0 / medium 54). Hoy su SHA-256 es idéntico al de `vc/tooling/scoring-policy.json` (`ce6e1a319f1f296c…`), `formulaVersion` 1.6.0 en ambas; puede divergir en el futuro.

## Caso 2 — `evaluate` real (hecho medido)

Mismos flags sin `--dry-run`. Archivos creados (solo bajo `--output-dir` y `--narrative-doc`):

- `out/evaluations/<id>.evaluation.json` — registro `decision_pending`.
- `out/evaluations/<id>.evidence.json` — copia del archivo de evidencia.
- `narrative.md` — sección por candidato (el archivo se crea con encabezado si no existe).
- `out/evaluations/history/<id>/<observedAt>_<evaluatedRef>_<hash8>.{evaluation,evidence}.json` — se crea cuando ya existe un registro vigente (al re-evaluar o decidir), inmutable.

Salida final: `Borrador guardado en pending: out/evaluations/smoke-own-skill.evaluation.json`. Nótese que esa ruta es relativa al cwd.

Campos que guarda el registro (`smoke-own-skill.evaluation.json`): `candidate`, `observedAt`, `overallScore`, `evidenceCoverage`, `factorScores`, **`formulaVersion` ("1.6.0")**, `confidenceScore`, `confidence`, `riskLevel`, `baselineRecommendation`, `status`, `sourceEvidence`, `evidenceInputRef`, `expiresAt`, `communityEvidenceNote`, y `humanDecision` tras decidir.

Procedencia — lo que **no** guarda (medido por inspección del registro y del código):

- No hay hash ni ruta de la política, ni revisión/versión del motor. Solo `formulaVersion`, que es un string de la política, sin garantía de que identifique su contenido.
- `evidenceInputRef` queda **relativo al cwd** de la corrida (`out/evaluations/…`), no al directorio de registro: depende de cómo se invocó.
- `sourceEvidence` es un literal heredado del layout de Blends: `../../docs/tooling/evaluations.md#<id>`; con `--narrative-doc` externo apunta a una ruta inexistente fuera del precursor (enlace colgante).
- El id de history incluye `sha256(JSON del registro)` truncado a 8 hex: identifica el contenido del registro, no la política ni el motor.

Inferencia: para auditar "con qué política y motor" hay que registrarlo fuera del motor (p. ej. en VCX: SHA de la política, `a8f3eb7f1`/HEAD del precursor y comando), o aceptar la limitación.

## Caso 3 — `decide` (hecho medido)

Flags obligatorios del CLI: `--id`, `--status`, `--by` (si falta, error y exit 1). Resto según estado (`validateHumanDecision`, confirmado ejecutando):

| status | requiere además |
| --- | --- |
| `rejected` | `--rationale` |
| `deferred` | `--rationale`, `--review-at` |
| `approved` | nada más; **bloqueado** si `riskLevel` ≥ umbral del gate de la política |
| `approved_with_exception` | `--rationale`, `--review-at`, `--accepted-risk` |

Ejecuciones:

- `decide --id smoke-own-skill --status rejected --by "Smoke Test" --rationale "prueba de humo"` → `decide: "smoke-own-skill" → rejected (vence 2027-01-30T12:00:00.000Z).` exit 0. Archiva el borrador en `history/` y reescribe `evaluation.json` con `status: rejected` y `humanDecision`; agrega subsección "Decisión" a `narrative.md`.
- `approved_with_exception` sin flags → `requiere rationale; requiere reviewAt; requiere acceptedRisk: true` (exit 1, no graba); con los tres → exit 0.
- Gate: con `networkAccess: true` (riesgo `high`), `decide --status approved` → `riesgo high: "approved" no es válido — usar approved_with_exception …`, exit 1. Con riesgo `low`, `approved` sí pasa.
- `--decided-at` opcional; por defecto `decidedAt` es el reloj real (`2026-11-02T00:28Z` UTC en la prueba), **no** respeta `--now`; `expiresAt` sí parte de `observedAt` (aquí 90 días, `2027-01-30`).
- **No toca roadmaps:** `grep -rn roadmap` sobre `scoring/` y `bin/` no devuelve nada, y los 952 `.roadmap.json` del precursor mantuvieron su SHA. `decide` del CLI solo graba la decisión; el registro en roadmap lo hacía el envoltorio `vc/tools/evaluate-tooling.mjs` (no ejecutado; así lo dice `.claude/commands/tool.md` paso 7). El flujo `/tool` completo (`--purpose`, `--scope`, etc.) **no** está cubierto por este CLI.

## Límites y riesgos encontrados

1. **Sin procedencia de política/motor** en el registro (arriba). Mitigable por VCX con un archivo adyacente, no por el motor.
2. **Rutas dependientes del cwd** en `evidenceInputRef`; y `sourceEvidence` colgante. Si VCX comparará registros, normalizarlos o ignorar esos dos campos.
3. **Decisiones sobrescribibles:** `smoke-own-skill-b` pasó `approved_with_exception` → `approved` sobre el mismo registro sin error; solo history conserva el estado anterior. Con riesgo bajo no hay bloqueo de re-decisión.
4. **Dependencia fuerte del precursor:** el comando ejecuta código y política del precursor en su estado de trabajo actual (árbol sucio, sin pin de versión); un cambio allí cambia resultados sin aviso salvo `formulaVersion`.
5. **Corrida lenta del control, no del CLI:** el `find` completo sobre el precursor (incluye `.git-trains/`) tarda ~2 min; el CLI en sí es instantáneo.
6. **Cobertura limitada de la prueba:** solo un candidato `skill` sin GitHub; no se probó el colector de GitHub, `--offline` con snapshot, ni `deferred`; el gate se verificó solo con una bandera `high`.
7. Los directorios de prueba están en el scratchpad de la sesión (efímero); este informe resume las salidas.

## Pendientes sugeridos (no ejecutados)

- Decidir dónde guardar procedencia adicional (política SHA, revisión del motor) en `brix/tooling/`.
- Decidir si VCX acepta ejecutar el CLI del precursor sin pin, o si exige commit/tag fijados antes de tratar un score como evidencia.
