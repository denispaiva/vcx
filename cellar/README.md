# Cellar · producto

Proyecto de primer nivel de VCX, par de Blends. Primera curación documental: 2026-10-30, bajo el acuerdo VCX-D020 del [registro](../docs/decisions/README.md).

## Misión

Ofrecer una estructura y mecanismos portables para organizar y custodiar ideas, proyectos, configuración, decisiones, estado y evidencia de un portfolio.

## Visión

Que cada equipo pueda crear y conservar un portfolio propio, legible y recuperable con independencia del orquestador, preservando la identidad y el contexto de sus iniciativas.

## Destinatarios y alcance

Se dirige a propietarios y custodios de portfolios, equipos y consumidores autorizados de sus datos. El producto define organización, referencias, configuración y mecanismos de acceso y recuperación; cada instancia conserva los datos concretos del portfolio.

**Entradas previstas:** identidad, configuración, perfiles adoptados, iniciativas, decisiones y declaraciones de almacenamiento.

**Resultados previstos:** un portfolio organizado y accesible por interfaces explícitas, con estado y evidencia recuperables desde sus fuentes declaradas.

Cellar no ejecuta el gobierno de Blends ni concentra las interfaces internas de Brix. Una instancia no exige copiar todo el código, bases operativas o credenciales dentro de una carpeta. El alcance ejecutable del producto y sus interfaces deben detallarse antes de implementarlos.

## Plantillas documentales

- [Plantilla de ideas](templates/idea/README.md): propuesta enriquecida para revisión humana y consejo, anterior a su aceptación en el portfolio.
- [Plantilla FinOps](templates/finops/README.md): documento posterior al ingreso, construido desde un modelo de arquitectura de referencia de Brix, con supuestos, escenarios y decisión de presupuesto.
- [Plantilla de Cellar](templates/cellar/README.md): identidad, custodia, configuración, iniciativas y recuperación.
- [Plantilla de iniciativa](templates/initiative/README.md): contexto propio para una idea o proyecto.
- [Plantilla de instrucciones locales](templates/initiative/AGENTS.md): entrada de contexto para participantes y agentes.

Uso manual: copiar solo la plantilla requerida al destino que se haya acordado, resolver todos los marcadores `{{...}}` y comprobar las referencias desde su nueva ubicación. No copiar por defecto el portfolio o los datos de otro equipo. No existe todavía un generador, wizard o exportador implementado en esta estructura.

## Estado y contexto

El [modelo mínimo de iniciativa](docs/initiative-model.md) precisa la información del [primer recorrido Cellar–Blends](../docs/superpowers/specs/2026-10-30-cellar-blends-first-journey-design.md). Es una propuesta para revisar; las plantillas actuales aún no implementan todos esos campos o condiciones.

La propuesta de idea usa su plantilla específica durante el [ingreso](../blends/docs/idea-intake.md). El registro en Cellar ocurre después de revisar el reporte del consejo y recibir la confirmación humana; un borrador aún no aceptado no figura como iniciativa activa.

Esta carpeta contiene la definición del producto y las plantillas; [cellars/](../cellars/README.md) es el punto de entrada de sus futuras instancias. Aún no se creó una instancia ni se eligió su nombre.

Para trabajar: leer este documento y [AGENTS.md](AGENTS.md). Consultar [interoperabilidad](../docs/architecture/interoperability.md), [matriz](../docs/architecture/responsibility-matrix.md) y [decisiones](../docs/decisions/README.md) según la tarea.

## Fuentes de trabajo y dependencias

| Tema | Fuente canónica y situación |
|---|---|
| Identidad, ciclo y referencias de iniciativas | [Modelo mínimo](docs/initiative-model.md), propuesto; todavía no es un esquema ejecutable |
| Material utilizable hoy | Plantillas manuales enlazadas arriba; la plantilla general de iniciativa todavía no representa todo el modelo mínimo |
| Interfaces y responsabilidades | [Interoperabilidad](../docs/architecture/interoperability.md) y [matriz](../docs/architecture/responsibility-matrix.md), propuestas compartidas |
| Autoridad y asuntos abiertos | [Decisiones](../docs/decisions/README.md); no hay todavía una instancia propietaria de su seguimiento |
| Trabajo documental de esta etapa | [Plan de curación](../docs/superpowers/plans/2026-10-30-blends-cellar-curation.md); su evidencia se conserva en el [reporte](../docs/superpowers/reports/2026-10-30-blends-cellar-curation.md) |

Blends será consumidor de la información de Cellar para coordinar procesos; no es un requisito para leer y conservar su contexto documental. Brix recibe entradas explícitas y produce instrumentos o resultados que la instancia puede custodiar. Cellar no absorbe el gobierno de Blends ni las capacidades internas de Brix. La independencia ejecutable y el aislamiento entre instancias siguen sin demostrarse.

La autoridad sobre propósito y decisiones concretas debe asignarse explícitamente cuando se organice su seguimiento. La ubicación de primer nivel no resuelve esa asignación ni crea un roadmap. Tampoco se han elegido backend, formato persistente o versión ejecutable del producto.

## Próximo entregable propuesto

Alinear las plantillas de Cellar e iniciativa con el modelo mínimo mediante un caso sintético, antes de implementar almacenamiento. Se considerará aceptable cuando permita representar identidad estable, procedencia, revisiones, decisiones y referencias de ingreso y graduación, separando ciclo de vida y estado de trabajo, con una única fuente activa por dato.

Este entregable requiere un alcance posterior: no se ejecuta por la curación de esta entrada. El modelo y los contratos conservan su condición de propuestas. Las decisiones sobre primera instancia, propiedad canónica y ubicación del código se mantienen en el registro compartido, sin listas de estado paralelas.
