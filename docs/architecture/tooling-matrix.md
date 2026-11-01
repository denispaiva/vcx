# Matriz de skills y MCP por producto y fase

Fecha: 2026-10-31; columna de capacidad agregada el 2026-11-01. Estado: adoptada como fuente editable transitoria por VCX-D028 del [registro](../decisions/README.md); el contenido de cada fila conserva su propio estado. Esta matriz no admite, instala ni autoriza herramientas; tampoco concede permisos a agentes.

## Qué resuelve y qué no

El inventario del precursor ya registra cada skill y MCP con propósito, estado, alcance, procedencia y evaluación, y el registro de Brix agrupa comandos e instrumentos por capacidad. Ninguno indica en qué fase de qué producto se usan. Esta matriz agrega solo esa relación: **producto · fase → capacidad → necesidad → herramienta → estado de la asignación**.

Para no crear otra fuente editable, cada fila referencia el `capability` del registro y el `id` del inventario, sin copiar propósito, versión, implementación, puntaje ni evidencia de admisión:

| Dato | Fuente canónica, de solo lectura para VCX |
|---|---|
| Capacidades de Brix y Blends | `../blends/vc/tooling/brix-capabilities.json`, campo `capability` |
| Inventario de skills y MCP | Campo `tooling` de `../blends/vc/framework/.roadmap.json` y de cada `.roadmap.json` de proyecto |
| Admisión y puntaje | Política `../blends/vc/docs/standards/skills.md` y `../blends/vc/tooling/evaluations/` |
| Uso medido | `../blends/vc/tooling/usage/records/` |
| Features y backlog | `.roadmap.json` de cada producto o instancia de Cellar; cada ítem referencia las capacidades que necesita |
| Relación producto · fase → capacidad → herramienta | **Esta matriz** |

Las rutas al precursor son referencias de consulta según [AGENTS](../../AGENTS.md#fronteras); no son dependencias que un producto independiente pueda conservar.

Las features no se agrupan aquí: tienen su propio ciclo de vida en el backlog y copiarlas duplicaría su fuente. Una vista de features por herramienta se deriva del backlog más esta matriz, a través de la capacidad.

## Capacidad y herramienta

Una **capacidad** es un comando o instrumento propio de Brix o Blends, registrado con su dueño. Una **herramienta** es una skill o un MCP de terceros admitido en el inventario. Una capacidad puede apoyarse en herramientas o no necesitar ninguna; una herramienta también puede usarse sin capacidad de por medio.

| Valor de la columna Capacidad | Significado |
|---|---|
| `capability` del registro | La fase usa esa capacidad; la herramienta de la fila es la que esa capacidad o su ejecución necesita |
| Uso directo | El agente usa la herramienta en la fase sin capacidad propia de por medio |
| No registrada | La fase necesita una capacidad que todavía no existe en el registro |

## Estados de una asignación

El estado describe la relación de la herramienta con la fase, no la admisión de la herramienta ni el estado de la capacidad. Una herramienta `active` en el inventario puede estar solo propuesta para una fase.

| Estado | Significado | Base exigida |
|---|---|---|
| Observado | Uso medido en esa necesidad | Registro de uso o evidencia fechada |
| Asignado | Herramienta activa en el inventario; su uso en la fase se propone aquí | Inventario |
| Candidato | No está activa en el inventario o su evaluación no tiene decisión | Requiere la admisión vigente antes de usarse |

Una herramienta con decisión humana diferida o rechazada no es candidata, aunque el inventario la marque `planned`: prevalece la decisión registrada en su evaluación.
| Brecha | Necesidad sin herramienta o sin capacidad identificada | Explicar si conviene una herramienta o basta el proceso |
| Sin herramienta | La capacidad o el trabajo humano no necesitan skill ni MCP | Fundamento en la fila |

Al corte, el uso medido cubre 23 ramas entre el 2026-09-26 y el 2026-10-01 y solo registra el comando `tool` (capacidad `tooling-audit`), `superpowers:writing-plans`, `superpowers:subagent-driven-development` y `escasez` (alias deprecado de `scarcity-monitoring`). Por eso casi todas las filas son asignaciones o candidatos, no uso comprobado.

## Fases consideradas

Se toman de las fuentes de cada producto, sin crear fases nuevas:

- **Blends:** [ingreso](../../blends/docs/idea-intake.md#secuencia-de-ingreso) y [recorrido de idea a proyecto](../../blends/docs/idea-to-project.md#secuencia) — exploración, definición, gate (graduar, diferir o archivar) y preparación. La [maduración con preguntas asesinas](../superpowers/specs/2026-10-31-idea-maturation-design.md) sigue en revisión.
- **Brix:** capacidades invocables de [comandos](../../brix/docs/commands.md), incluida la admisión de tooling.
- **Cellar:** organización del portfolio y backlog, custodia de decisiones y evidencia, respaldo, según su [README](../../cellar/README.md) y el [modelo de iniciativa](../../cellar/docs/initiative-model.md); y, desde VCX-D029, conducción de los proyectos graduados, con planificación, implementación, revisión, integración, entrega, cierre e interfaz, según la [matriz](responsibility-matrix.md#1-método-y-conducción).

La entrega de un proyecto graduado pertenece a la conducción en Cellar según VCX-D029; el inventario actual concentra allí sus herramientas, medidas cuando Blends Kernel conducía los proyectos en el precursor.

## Matriz

| Producto · fase | Capacidad | Necesidad | Herramienta (`id`) | Tipo | Estado | Nota |
|---|---|---|---|---|---|---|
| Blends · ingreso, entrada | `idea-to-spec` | Leer ideas en PDF, DOCX u otros formatos | `markitdown` | Skill | Asignado | Alcance `task` en el inventario |
| Blends · ingreso, encuadre | `idea-to-spec` | Extraer de la idea su problema esencial (prensado) | `brainstorming` | Skill | Asignado | |
| Blends · ingreso, encuadre | No registrada | Instrumento de preguntas asesinas | `killer-questions` (adaptación de `phuryn/pm-skills` · `identify-assumptions-new`) | Skill | Candidato | Incorporada el 2026-11-01 en [`brix/.claude/skills/`](../../brix/.claude/skills/killer-questions/PROVENANCE.md), sin admisión en el inventario ni uso medido. Demostrado solo un caso ficticio ([reporte](../superpowers/reports/2026-11-01-killer-questions-instrument.md)). La capacidad sigue sin registrarse y el diseño de maduración sigue siendo propuesta: la brecha de capacidad permanece abierta |
| Blends · ingreso, consejo | `llm-council` | Reporte del consejo | `llm-council-skill` | Skill | Candidato | La capacidad está en uso; la evaluación de la skill figura `decision_pending` |
| Blends · arquitectura y FinOps | `finops-ledger` | Planilla y escenarios de costo | `xlsx`, `sheets-api` | Skill, MCP | Asignado | `sheets-api` escribe en la planilla operativa: exige alcance explícito |
| Blends · arquitectura y FinOps | `finops-ledger` | Respaldar importes con comprobantes reales | `gmail` | MCP | Asignado | Aprobado con excepción; puede enviar y borrar: limitar a lectura |
| Blends · exploración | Uso directo | Documentación vigente de bibliotecas y SDK | `context7-mcp` | MCP | Candidato | `planned` en el inventario |
| Blends · exploración | Uso directo | Investigación de mercado y alternativas con varias fuentes | — | — | Brecha | Hay skills de investigación disponibles en la sesión, ninguna evaluada |
| Blends · definición | `spec-quality-checklist` | Calidad de requisitos antes del plan | `spec-kit-checklist` | Skill | Asignado | Compuerta opcional |
| Blends · definición | `spec-consistency-analysis` | Consistencia entre diseño y plan | `spec-kit-analyze` | Skill | Asignado | |
| Blends · gate | Uso directo | Graduar, diferir o archivar | — | — | Sin herramienta | Decide la autoridad humana; el consejo asesora y no reemplaza evidencia |
| Blends · preparación | `graduation` | Aplicar una graduación autorizada | — | — | Sin herramienta | La capacidad de Brix no requiere skill ni MCP |
| Cellar · conducción, planificación | Uso directo | Plan del proyecto graduado | `writing-plans` | Skill | Observado | 21 invocaciones medidas, sin distinguir fase; figuraba en Blends · preparación antes de VCX-D029 |
| Cellar · conducción, implementación | Uso directo | Ejecutar tareas con subagentes | `superpowers:subagent-driven-development` | Skill | Observado | Medido, pero no figura en el inventario del framework: conciliar |
| Cellar · conducción, implementación | Uso directo | Código nuevo con pruebas | `test-driven-development` | Skill | Asignado | Según riesgo; VCX-P5 no impone TDD indiscriminado |
| Cellar · conducción, revisión | Uso directo | Revisión independiente | `requesting-code-review`, `skill-codex` | Skill | Asignado; candidato | `skill-codex` está `planned` |
| Cellar · conducción, revisión | Uso directo | Seguridad de cambios sensibles | `security-review` | Skill | Asignado | Alcance `task` |
| Cellar · conducción, integración | No registrada | Limitar qué rutas toca cada rama y verificar antes de entregar | — | — | Sin herramienta | Implementada en el precursor sin registro: `branch-scopes.json`, `.githooks/` y `npm run verify`, scripts propios sobre `git`. Dueño entre Brix, Blends y Cellar sin decidir |
| Cellar · conducción, integración | Uso directo | Convenciones de ramas, commits y versionado | `agent-skills` | Skill | Asignado | Subconjunto `git-workflow-and-versioning` |
| Cellar · conducción, integración | `ci-scaffolding` | Crear el CI de un proyecto | `agent-skills` | Skill | Asignado | Subconjunto `ci-cd-and-automation` |
| Cellar · conducción, entrega | No registrada | Commitear, pushear, encolar e integrar por tren con compuertas | — | — | Sin herramienta | Implementada en el precursor sin registro: `npm run entregar`, `queue`, `train`, `train-gate`, `train-merge`, `recycle` y `control-plane.json`. Es el ciclo del repositorio de Blends; cada producto independiente declara el suyo |
| Cellar · conducción, entrega | `scarcity-monitoring`, `scarcity-cycle-closure` | Controlar el costo de GitHub Actions antes de disparar CI | — | — | Sin herramienta | |
| Cellar · conducción, cierre | Uso directo | Evidencia antes de declarar éxito | `verification-before-completion` | Skill | Asignado | Transversal a todas las fases |
| Cellar · conducción, interfaz | Uso directo | Diseño y anti-patrones de UI | `impeccable`, `emilkowalski-skills` | Skill | Asignado | Solo proyectos con interfaz |
| Cellar · conducción, interfaz | Uso directo | Verificar lo renderizado | `browser` | MCP | Asignado | |
| Brix · admisión de tooling | `tooling-audit` | Evaluar y registrar una herramienta | — | — | Sin herramienta | La capacidad es el proceso propio; 42 invocaciones medidas de `/tool` |
| Brix · admisión de tooling | `tooling-audit` | Descubrir candidatas | `find-skills` | Skill | Asignado | |
| Cellar · portfolio y backlog | `backlog-and-sprint-planning` | Organizar ideas, proyectos y backlog | — | — | Sin herramienta | Capacidad de Blends sobre archivos versionados; un MCP de gestión externo crearía una segunda fuente sin necesidad demostrada |
| Cellar · custodia | Uso directo | Continuidad entre sesiones | `handoff` | Skill | Asignado | El traspaso no sustituye registros de decisión |
| Cellar · instrucciones | Uso directo | Redactar AGENTS, skills y plantillas | `mattpocock-writing-for-agents` | Skill | Asignado | |

Capacidades registradas sin fila al corte: `seeding`, `backend-inventory`, `unattended-session-run` y los instrumentos de eficiencia (`actions-minutes-per-branch`, `context-window-per-branch`, `po-attention-per-branch`, `kpi-history`). Se agregan cuando una fase las use con alguna herramienta o se decida que no necesitan ninguna.

Retiros: `orca-cli` se quitó el 2026-11-01 a pedido del usuario. Su evaluación figura `deferred` por decisión humana del 2026-08-10, con riesgo crítico y sin caso de uso, porque el harness gestiona worktrees de forma nativa; el inventario del precursor todavía la marca `planned`.

## Cómo evoluciona

- **Cuándo se edita:** al cambiar el inventario o el registro de capacidades, al aparecer uso medido que confirme o contradiga una fila, o al diseñar una fase nueva. No se revisa por calendario.
- **Cómo se agrega una fila:** con una necesidad concreta de la fase, ligada a una capacidad o declarada como uso directo. Una herramienta sin necesidad no entra; una necesidad sin herramienta o sin capacidad queda como brecha.
- **Promociones:** candidato → asignado exige admisión en el inventario; asignado → observado exige registro de uso o evidencia fechada; cualquier fila puede pasar a sin herramienta con fundamento. Una capacidad no registrada pasa a `capability` cuando su dueño la incorpora al registro.
- **Retiros:** una herramienta o capacidad retirada se marca con fecha y motivo antes de borrar la fila.

## Destino previsto

Esta tabla es transitoria, según VCX-D028. Al preparar los repositorios independientes, la relación con la fase pasa al inventario como dato de cada herramienta, por ejemplo un campo `phases`, junto con las capacidades que la usan, y esta matriz se convierte en una vista generada. El dueño de la vista corresponde a la [matriz de responsabilidades](responsibility-matrix.md): Brix mantiene el catálogo, Blends define las fases del tramo de idea y del método, Cellar define las de conducción y conserva la configuración de cada instancia. Ese cambio requiere escribir en el precursor o en los nuevos repositorios y un alcance explícito; no lo autoriza este documento.
