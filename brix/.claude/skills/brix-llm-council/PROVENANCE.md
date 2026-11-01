# Procedencia de `brix-llm-council`

Fecha: 2026-11-01. Estado: herramienta candidata de Brix, creada a partir de un diseño aprobado por el usuario el 2026-11-01; sin evaluación con `/tool`, sin admisión y sin uso medido.

## Origen

| Dato | Valor |
|---|---|
| Método | LLM Council de Andrej Karpathy (https://github.com/karpathy/llm-council): asesores independientes, revisión cruzada anónima y presidente que sintetiza. No se copió su código. |
| Adaptación base | Comando `/council` del precursor: `blends/.claude/commands/council.md`, lectura de solo lectura |
| Revisión del precursor | `f86a2a7df72e55bbb97451c1a35ef3c03b961fc3` (`HEAD` del precursor al leer); último commit que tocó el archivo: `f9237df9f384c5acf09644943ce97fe3524cc714` (2026-10-11) |
| SHA-256 del comando leído | `bcc70adc5edaccf849754b6763ade9a9bfdf57ddbca26a6e6069371bb7885004` |
| Licencia | Sin archivo de licencia propio todavía; pendiente de decidir por el dueño del repositorio de Brix. No se incorpora texto de terceros sin licencia declarada |

## Qué no se usó

`tenfoldmarc/llm-council-skill` (evaluación del precursor: 39,6, `do_not_advance`, sin licencia en archivo) y `aiwithremy/claude-skills-llm-council` se leyeron el 2026-11-01 solo para revisar su evidencia ([informe](../../../../docs/superpowers/reports/2026-11-01-llm-council-alternatives-evidence.md)), no como base de esta adaptación. No se copió su texto.

## Diferencias frente a `/council`

| Elemento | `/council` | Esta skill |
|---|---|---|
| Entrada | Slug de `ideas/<slug>/`, ficha y `.roadmap.json` | Documento Markdown con revisión identificada y pregunta suministrada |
| Lecturas | El orquestador lee la ficha y trazas previas; los asesores leen el repo | Solo el documento y una lista cerrada de referencias autorizadas |
| Modelos | Tabla de bindings, resolver y runner del precursor | Configuración declarada por el consumidor; sin resolvers privados |
| Recursos | Costo anotado si se puede medir | Máximo de invocaciones, concurrencia, espera y presupuesto declarados antes de ejecutar |
| Salida | Traza en la carpeta de la idea | Reporte Markdown en destino autorizado, vinculado a la revisión de entrada |
| Repetición | Guarda por hash de pregunta | Identidad derivada de documento, pregunta y configuración |
| Fallos | Se explican en la traza | Salida parcial conservada, asientos fallidos y consumo conocido |

## Qué falta

- Un runtime o driver público: esta skill describe el procedimiento y no está implementada como comando.
- Evaluación con `/tool` y decisión humana. Ver el [diseño](../../../../docs/superpowers/specs/2026-11-01-council-skill-design.md) para las validaciones previstas.
- Licencia del producto.

## Actualización

El comando original no se sincroniza solo. Para actualizar: leer la nueva revisión, comparar contra el SHA-256 anterior y registrar la revisión aquí. Para retirar: marcar con fecha y motivo en la matriz de tooling antes de borrar.
