# Skills de diseño UI/UX: evaluación en seco

Fecha: 2026-11-16, con `--now 2026-11-17T00:15:00Z` fijo para la ronda. Estado: **evidencia de evaluación en seco**. No es una admisión, no registra decisiones humanas y no instaló, activó ni ejecutó ninguna candidata. Operador: Claude Code (`claude-opus-5-5`), a pedido del usuario. Inspección de Impeccable y UI/UX Pro Max delegada a dos subagentes `sonnet` de solo lectura; el agente principal verificó sus afirmaciones de mayor peso contra el repositorio.

Origen: [artículo de Pasquale Pillitteri](https://pasqualepillitteri.it/es/news/578/claude-code-skills-design-uiux-guia), tomado como pista, no como evidencia. Las estrellas que cita no coinciden entre sí ni con la API, y no se usan como evidencia de eficacia.

## Contexto que cambió durante la ronda

Entre 00:02 y 00:04 UTC del 2026-11-17, **otra sesión** persistió en `docs/tooling/evaluations/` evaluaciones con decisión del PO, todavía sin commitear: `design-accessibility-review` y `design-ux-copy` aprobadas (`anthropics/knowledge-work-plugins@c71b6f3`); `impeccable`, `emilkowalski-skills` y `mobile-app-ui-design` rechazadas, con vencimiento el 2027-02-15. Esta ronda no las tocó. Las evidencias de abajo tratan las dos aprobadas como tooling existente.

## Cribado del artículo

| Candidata | Tipo | Estado en esta ronda |
|---|---|---|
| `anthropics/skills` · frontend-design | Skill | Evaluada. El artículo la ubica en `anthropics/claude-code/plugins/frontend-design`, ruta que hoy da 404 |
| `pbakaus/impeccable` | Plugin: skill, hooks y engine | Evidencia preparada; bloqueada por la decisión `rejected` vigente |
| `vercel-labs/agent-skills` · web-design-guidelines | Skill de un paquete | Evaluada, con sus reglas remotas |
| `wondelai/skills` · ux-heuristics | Skill de un paquete | Evaluada |
| `Dammyjay93/interface-design` | Skill y comandos | Evaluada |
| `nextlevelbuilder/ui-ux-pro-max-skill` | Plugin de 7 skills con datos | Evaluada |
| `emilkowalski/skills` | Paquete | Para después: decisión `rejected` del 2026-11-17; animate-expo y break-ui, solo por SHA y por separado |
| `Leonxlnx/taste-skill` | Paquete | Para después: requiere navegador y Node 22; solo con una necesidad de dirección visual que frontend-design no cubra |
| `nutlope/hallmark`, `garrytan/gstack` | Skills anti-slop o de puntaje | Para después: se solapan con frontend-design y con la nota orientativa de VCX-P2 |
| `Owl-Listener/designer-skills`, `bencium/bencium-marketplace` | Paquetes | Para después: alcance amplio; revisar solo una skill concreta ante una necesidad |
| `wondelai/skills` · hooked-ux, design-sprint | Skills | Para después: retención y sprints no son una necesidad declarada |
| `rshankras/claude-code-apple-skills` (iOS HIG) | Skill | Para después: justificable si hay trabajo de UI nativa iOS fuera de Expo |
| `LovroPodobnik/refactoring-ui-skill` | Skill | Para después: autoría pequeña; `wondelai` tiene otra refactoring-ui |
| `accesslint/claude-marketplace` | Plugin con MCP | Para después: se solapa con design:accessibility-review |
| `ParthJadhav/app-store-screenshots` | Skill | Para después: solo al preparar una publicación en tiendas |
| `oso95/scroll-world`, `nateherkai/scroll-craft`, `img2threejs` | Skills de landing 3D | Fuera de necesidad; scroll-world usa servicios pagos |
| `claudekit/frontend-design-pro-demo`, `rohitg00/awesome-claude-design` | Demo y referencia | Material de lectura, no herramienta |
| Claude Design, Figma MCP, Lazyweb, Mobbin, Refero, Playwright MCP | Servicios o MCP | Fuera de alcance: servicios, cuentas o red; se evalúan aparte con su propio costo |
| Directorios: BehiSecc, travisvn, VoltAgent, Smithery, clskills, agentskills.io | Listas | Referencias, no candidatas |

Antecedentes: `impeccable` y `emilkowalski-skills` tuvieron admisión del precursor hasta el 2026-11-08 y se dejaron vencer sin uso ([plan de renovación](../../plans/2026-11-02-tooling-renewal-plan.md)). La necesidad «Diseño y anti-patrones de UI» de la [matriz](../../../architecture/tooling-matrix.md) quedó sin herramienta vigente. La [checklist v1](../2026-11-09-ux-checklist-pilot/checklist-v1.md) sigue bajo VCX-D060.

## Resultados del motor

Política `ce6e1a31…` (formulaVersion 1.6.0), Brix `131a5c2`, cliTree `b4c92762`.

| ID | Revisión evaluada | Score | Recomendación base | Riesgo | Confianza |
|---|---|---|---|---|---|
| `anthropic-frontend-design` | `anthropics/skills@e4bb5d9` | 59,0 | do_not_advance | medium | high (86) |
| `wondelai-ux-heuristics` | `wondelai/skills@c526558` | 59,5 | do_not_advance | low | high (86) |
| `interface-design` | `Dammyjay93/interface-design@2f9be32` | 52,7 | do_not_advance | medium | high (85) |
| `vercel-web-design-guidelines` | `vercel-labs/agent-skills@1a2c79d` + reglas `web-interface-guidelines@434b7f9` | 50,5 | do_not_advance | high | high (86) |
| `ui-ux-pro-max` | `nextlevelbuilder/ui-ux-pro-max-skill@e59ff37` | 62,8 | advance_with_reservations | high | high (84) |
| `impeccable` | `pbakaus/impeccable@d41d986` | — | Bloqueada por la precondición 3 | — | — |

**Límite común:** `community` quedó `unavailable` en las cinco. La API pública de GitHub sin token tenía el cupo agotado (`remaining: 0`) y no había snapshot reutilizable. No se pasó un token para forzarlo. Por eso la cobertura excluye ese factor, y la confianza alta mide la cobertura del resto, no la eficacia.

## Piloto propuesto

El [diseño del piloto](pilot-design.md) mide si `frontend-design` y las reglas web fijadas aportan algo en uso real. El piloto A se ejecutó el mismo día: [resultado](pilot-a-results.md), que pasa a evaluación formal con el tope de tokens excedido. El piloto B también se ejecutó: [resultado](pilot-b-results.md). Las reglas web fijadas se archivan como antecedente, porque aportaron 1 hallazgo único relevante de los 3 que exigía la regla.

## Evaluación formal y decisión

Después del piloto A, a pedido del PO, `anthropic-frontend-design` se evaluó en forma persistida con el envoltorio, a partir de [`anthropic-frontend-design.formal.evidence.json`](anthropic-frontend-design.formal.evidence.json). Respecto de la evidencia en seco cambian dos cosas: `observedOutcome` pasa a 62, respaldado por el piloto, e `incrementalValue` sube de 45 a 55.

El motor dio 63,3, `advance_with_reservations`, riesgo medium y confianza high (97). Esta vez el envoltorio del PR #46 sí obtuvo la comunidad: 76,7, medida sobre el repositorio entero, no sobre la skill.

El PO decidió `approved` con cuatro reservas, registradas en `humanDecision.rationale` de [`docs/tooling/evaluations/anthropic-frontend-design.evaluation.json`](../../../tooling/evaluations/anthropic-frontend-design.evaluation.json). La aprobación vence el 2027-02-15.

## Reproducir

Desde la raíz de VCX, una candidata por vez:

```bash
node docs/tooling/score-run.mjs evaluate --input docs/superpowers/reports/2026-11-16-ui-ux-design-skills-dry-run/<id>.evidence.json --now 2026-11-17T00:15:00Z --operator "Claude Code (claude-opus-5-5); evaluación en seco solicitada por el usuario" --dry-run
```

Las salidas están en `<id>.dry-run.out`. Con red o token, `community` puede tomar valor y el score cambiar.

## Comprobación de lo que no cambió

Antes y después de las corridas coinciden el SHA-256 de la política (`ce6e1a31…`), de `score-runs.jsonl` (`0ec91462…`), de `score-run.mjs` (`481e27d3…`), de la matriz (`6114d062…`) y del conjunto de `docs/tooling` (`3deff7b3…`). Brix: `git status --ignored -- packages/cli` vacío. La ronda en seco solo creó los archivos de esta carpeta. La evaluación formal y la decisión posteriores escribieron en `docs/tooling/` el registro de `anthropic-frontend-design`, su historial y dos líneas en `score-runs.jsonl`.
