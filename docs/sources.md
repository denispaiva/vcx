# Fuentes de VCX

## Documentación vigente en este workspace

| Tema | Fuente editable |
|---|---|
| Misión y visión de VCX | [Visión](vision.md) |
| Mensaje ejecutivo para una landing futura | [Speech](executive-pitch.md) |
| Arquitectura conceptual | [Arquitectura](architecture/overview.md) |
| Propuesta de propiedad documental y preparación de repositorios | [Mapa de archivos y repositorios](architecture/repository-map.md) |
| Alcance propuesto del commit base raíz | [Preparación del commit base](superpowers/plans/2026-10-31-root-baseline-scope.md) |
| Responsabilidades y RACI propuestas | [Matriz](architecture/responsibility-matrix.md) |
| Propiedad de interfaces | [Interoperabilidad](architecture/interoperability.md) |
| Modelo mínimo propuesto de iniciativa | [Modelo de Cellar](https://github.com/denispaiva/cellar/blob/main/docs/initiative-model.md) |
| Proceso mínimo propuesto de idea a proyecto | [Recorrido de Blends](https://github.com/denispaiva/blends/blob/main/docs/idea-to-project.md) |
| Ingreso mediante documento, consejo y confirmación | [Flujo de ingreso](https://github.com/denispaiva/blends/blob/main/docs/idea-intake.md) |
| Capacidad requerida de preparación sobre Brix | [Preparación de ideas](https://github.com/denispaiva/brix/blob/main/docs/idea-intake.md) |
| Comandos CLI, equivalencias de conversación y ayuda | [Comandos de Brix](https://github.com/denispaiva/brix/blob/main/docs/commands.md) |
| Formato documental de la propuesta previa al ingreso | [Plantilla de ideas](https://github.com/denispaiva/cellar/blob/main/templates/idea/README.md) |
| Modelo propuesto para estimación técnica y económica | [Arquitectura de referencia en Brix](https://github.com/denispaiva/brix/blob/main/docs/reference-architecture.md) |
| Secuencia de arquitectura, FinOps y revisión de presupuesto | [Etapa de Blends](https://github.com/denispaiva/blends/blob/main/docs/architecture-and-finops.md) |
| Documento FinOps de la iniciativa | [Plantilla FinOps](https://github.com/denispaiva/cellar/blob/main/templates/finops/README.md) |
| Ejemplo y aceptación del primer recorrido | [Diseño conjunto](superpowers/specs/2026-10-30-cellar-blends-first-journey-design.md) |
| Contraste acotado con el sistema activo | [Correspondencia](architecture/current-system-mapping.md) |
| Decisiones, autoridad y pendientes | [Registro de decisiones](decisions/README.md) |
| Criterio de nombres | [Nombres](naming.md) |
| Instrucciones comunes del workspace | [AGENTS.md](../AGENTS.md) |
| Principios transversales adoptados | [Principios en AGENTS.md](../AGENTS.md#principios-transversales-de-vcx) |

Los contextos de producto son sus respectivos README. Los índices y resúmenes enlazan estas fuentes; no mantienen otra versión normativa de sus definiciones.

## Antecedentes históricos locales

Estas rutas identifican evidencia de origen en la máquina original. No son dependencias operativas de VCX ni deben ser necesarias para comprender un contexto nuevo.

- Conversación de diseño del 2026-10-29 y 2026-10-30: objetivos, composición A/B, aclaraciones y speech aceptado.
- Matriz anterior: `/Users/denispaiva/.codex/visualizations/2026/10/30/01a18a92-d2e8-7a02-bb05-bb620bc33e3d/vcx-foundational-matrix.md`. Se conserva como antecedente fechado; la matriz editable vigente es la enlazada arriba.
- Propuesta anterior: `/Users/denispaiva/.codex/visualizations/2026/10/30/01a18a88-a2e2-75a0-9e02-58c50c69d340/vcx-architecture-proposal.md`.
- Documento conceptual original: `/Users/denispaiva/.codex/attachments/b0ebcea4-594c-405e-91fc-0f4447246ba5/Pasted text.txt`.
- Sistema existente, referencia de solo lectura: `/Users/denispaiva/blends`. El análisis previo corresponde a `main` en `f86a2a7d`; no representa un inventario vivo de todas sus ramas.
- Decisiones aprobadas de reorganización: `/Users/denispaiva/blends/docs/superpowers/specs/2026-10-24-vc-carpetas-orden-design.md` y `/Users/denispaiva/blends/docs/superpowers/specs/2026-10-05-kernel-renombre-to-be-design.md`.

## Glosario y documentos de trabajo

El [glosario incorporado](references/enology-glossary-source.md) es una copia histórica sin curar de material aportado por el usuario. Su procedencia e integridad están en [nombres](naming.md); no es una norma ni un registro de asignaciones.

El [plan](superpowers/plans/2026-10-30-vcx-foundation.md) registra el trabajo previsto y el [reporte](superpowers/reports/2026-10-30-vcx-foundation.md) conserva su ejecución y verificación. Son evidencia de la etapa, no otra fuente normativa de la arquitectura.


La curación prioritaria de Cellar y Blends se organiza en su [plan](superpowers/plans/2026-10-30-blends-cellar-curation.md) y conserva evidencia en el [reporte](superpowers/reports/2026-10-30-blends-cellar-curation.md). Los contextos editables siguen siendo los README de producto; el reporte no sustituye su estado ni el registro de decisiones.


## Antecedentes externos puntuales

El 2026-11-08 el usuario aportó, como capturas sin autor identificado, un prompt titulado «Modo ambición: de tareas a decisiones», que declara seguir el método de Felix Rieseberg (Anthropic). La atribución se verificó mediante resúmenes secundarios del tutorial «How to be more ambitious: A tutorial for humans with models» (13 de octubre de 2026; cuatro tipos de ambición: velocidad, altura, profundidad y alcance), por ejemplo [este resumen](https://www.besthub.dev/articles/anthropic-engineer-s-framework-for-ambitious-ai-usage-altitude-depth-range-54bb5e0625fd); el original no se leyó. La evaluación en el chat de ese día concluyó que el prompt es en su mayor parte redundante con VCX-P1, VCX-P2 y VCX-P5 y con `brix-killer-questions` y `brix-llm-council`, que su regla de no avanzar sin respuestas contradice P1 y P3, y que su revisión multiperspectiva en un solo modelo no es independiente. Por decisión del usuario se incorporaron solo dos piezas: los campos de costo del error y datos crudos disponibles en la [plantilla de ideas](https://github.com/denispaiva/cellar/blob/main/templates/idea/README.md), y la señal temprana en la ficha de [`brix-killer-questions`](https://github.com/denispaiva/brix/blob/main/.agents/skills/brix-killer-questions/PROVENANCE.md). El prompt no se copia al workspace y no se adopta como instrucción.

## Antecedentes de los principios transversales

Comparación de solo lectura realizada el 2026-10-30 y revalidada el mismo día sobre el precursor local: `/Users/denis/VibeCoding/blends` (`../blends/` desde la raíz de VCX), en el commit `f86a2a7df72e55bbb97451c1a35ef3c03b961fc3`. La lectura original se hizo sobre un respaldo externo; los nueve archivos citados abajo coinciden byte a byte entre ambas ubicaciones según SHA-256 y no tienen cambios sin confirmar en la copia local. La coincidencia se limita a esos archivos. Los principios de VCX deben comprenderse sin acceder a esta ubicación.

Fuentes consultadas dentro de ese precursor:

- `AGENTS.md` y `vc/AGENTS.md`: instrucciones generales, ejecución, FinOps y fronteras de autoridad.
- `vc/README.md`: alcance del sistema y localización de estándares.
- `vc/docs/standards/work-proportionality.md`: proceso proporcional a impacto, incertidumbre y reversibilidad; controles no recortables por conveniencia.
- `vc/docs/standards/role-matrix.md`: resultados verificables, contraejemplos, autoridad, continuidad, costo por valor y ciclo de vida de instrucciones.
- `vc/docs/standards/conventions.md`: idioma por audiencia y tratamiento de incumplimientos heredados como deuda.
- `vc/docs/standards/secrets.md`: identidad efímera, límites de exposición y controles efectivos.
- `vc/docs/standards/security.md`: distinción entre declaración y aplicación de permisos; su encabezado lo declara «decidido, no vigente». Se consultó como antecedente, sin trasladar su estado normativo a VCX.
- `vc/docs/standards/idea-lifecycle.md`: preguntas decisivas, evidencia y límites de exploración. Este merge no modifica el ciclo de ideas.

La otra fuente es el pedido del usuario en esta conversación: evaluación crítica, método socrático, alternativas, simplicidad, evidencia, escenarios de caos, puntuación y auditoría de supuestos, registrado en VCX-D021. La combinación de nueve principios fue propuesta y autorizada explícitamente mediante VCX-D022. Se conserva una única formulación normativa en AGENTS.md, sin copiar aquí los principios completos.

No se importan comandos de entrega, sprints de 14 días, presupuestos o porcentajes particulares, proveedores, herramientas fijadas ni políticas Cloud First, Mobile First o Free Tier First. Su adopción, si corresponde, requiere un alcance propio; leer el precursor no autoriza ejecutar sus instrucciones.


## Referencias locales de Blends

Ubicaciones diferenciadas el 2026-10-30 durante la revisión documental:

- Fuente vigente de consulta y precursor de VCX, elegida expresamente por el usuario el 2026-10-30 en sustitución del respaldo: `../blends/`, desde la raíz de VCX, observado en `/Users/denis/VibeCoding/blends`. Esta relación de procedencia no demuestra desacople del producto objetivo. VCX-D026 acuerda que Blends continúe ese mismo repositorio mediante clon local, sin convertir todavía a `vcx/blends/` en copia canónica. El Brix original reside en `vc/brix/` dentro de ese precursor; su historial y los antecedentes externos al subárbol deberán contemplarse al decidir la extracción, sin ejecutar ahora una migración.
- Ubicación histórica citada por los documentos originales: `/Users/denispaiva/blends`.

Las rutas absolutas de esta sección identifican procedencia y localización observadas, no dependencias de instalación ni pruebas de identidad entre copias. La restricción de solo lectura del AGENTS común alcanza explícitamente a la copia local. Las consultas anteriores hechas sobre un respaldo externo se revalidaron en la copia local solo para los archivos citados en los antecedentes de los principios; otras rutas, ramas o estados no se compararon. Las referencias históricas anteriores se conservan sin reescribirlas como si pertenecieran a la máquina actual.


La reformulación documental del 2026-10-31 en VCX-D026 distingue los hallazgos de solo lectura del 2026-10-30 (49 worktrees registrados, 48 depurables; cuatro entradas sin seguimiento; 148 commits que afectan `vc/brix/` en la historia alcanzable desde HEAD) del inventario requerido al transferir. El usuario reportó después 179 ramas locales, 44 sin rama remota o con commits sin subir y ningún stash. Este último recuento se conserva como información aportada, no como nueva comprobación ejecutada en esta reformulación. Todos esos datos deben revalidarse al preparar el clon; no describen permanentemente el estado operativo.
