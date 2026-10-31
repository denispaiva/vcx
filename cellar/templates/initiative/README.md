# {{initiative_name}}

Plantilla documental para idea o proyecto. Resolver los marcadores al instanciar y retirar las instrucciones de plantilla. Los campos son contexto documental; no crean un roadmap o contrato ejecutable.

## Identidad

| Campo | Valor | Significado |
|---|---|---|
| `initiativeId` | `{{initiative_id}}` | Identidad estable; independiente de movimientos o nombres visibles |
| `kind` | `{{initiative_kind}}` | `idea` o `project` |
| `cellarId` | `{{cellar_id}}` | Portfolio propietario |
| `owner` | `{{owner}}` | Responsable de propósito y decisiones |
| `status` | `{{initiative_status}}` | Estado según el proceso adoptado |
| `codeRef` | `{{code_ref}}` | Ubicación canónica del código; indicar si aún no existe o no aplica |

## Misión

{{mission}}

## Visión

{{vision}}

## Destinatarios, alcance y objetivos

{{audience_scope_and_goals}}

## Contexto de entrada

{{current_context}}

Describir la situación actual, la pregunta o resultado buscado y las dependencias necesarias para esta iniciativa. Enlazar contexto ajeno solo cuando sea pertinente.

## Fuentes de trabajo

| Tema | Referencia canónica |
|---|---|
| Roadmap y planificación | `{{planning_ref}}` |
| Backlog | `{{backlog_ref}}` |
| Arquitectura y dependencias | `{{architecture_ref}}` |
| Decisiones | `{{decisions_ref}}` |
| Evidencia | `{{evidence_ref}}` |
| Continuidad entre sesiones | `{{handoff_ref}}` |
| Gobierno y autoridad adoptados | `{{governance_ref}}` |

Las referencias pueden apuntar a fuentes existentes o almacenamientos declarados. Si algo está pendiente o no aplica, indicarlo en vez de crear archivos vacíos o una segunda fuente editable. Un cambio de estado o graduación conserva identidad y relaciones históricas.

## Preparación del contexto

Revisar también la plantilla de `AGENTS.md` y resolver sus referencias según el destino. Declarar las verificaciones apropiadas al proyecto; no copiar comandos de otro producto por similitud de estructura.
