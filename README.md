# VCX · VibeOS, Vibe Coding for X projects

VCX, con VibeOS como nombre de marca según VCX-D029, puede identificar la propuesta comercial de un conjunto de productos desacoplados que ayudan a convertir ideas en resultados verificables. En el workspace, `vcx/` es su carpeta raíz de organización. VCX no se desarrollará como producto.

**Estado:** fundación documental establecida el 2026-10-30. Esta carpeta reúne sobre todo definiciones y plantillas, además de las skills propias de Brix y el envoltorio de evaluación de tooling de VCX-D035; las capacidades ejecutables de los productos se implementarán en trabajos posteriores. El sistema existente no fue migrado.

## Cómo se organiza

| Grupo | Propósito | Entradas |
|---|---|---|
| A · Base reutilizable | Ayudar a nuevos equipos a comenzar y evolucionar proyectos | [Blends](blends/README.md), [Brix](brix/README.md) y [Cellar](cellar/README.md) |
| B · Ideas y proyectos | Evolucionar con misión, visión, decisiones y contexto propios | [Solera](solera/README.md) |

Blends define el método y coordina cada idea hasta graduarla; Brix aporta capacidades e instrumentos; Cellar custodia los desarrollos y su memoria y conduce los proyectos graduados con sus Product Owners, según el reparto de VCX-D029 fijado en la [matriz](docs/architecture/responsibility-matrix.md#1-método-y-conducción). VCX es la raíz organizativa: no es una aplicación, un servicio central ni una dependencia de ejecución de esos productos. Cada producto debe poder distribuirse y evolucionar con independencia de esta carpeta.

El repositorio hermano `../blends/` es el precursor, según la aclaración del usuario del 2026-10-30. `blends/` dentro de VCX contiene hoy documentos objetivo. VCX-D026, enmendada por VCX-D032 y ajustada por VCX-D036, acuerda que el precursor continúe privado, con su historial, como primera instancia de Cellar en `vcx/solera/`, y que el Blends público sea un repositorio nuevo, sin modificar la carpeta original por inferencia. El [registro de decisiones](docs/decisions/README.md) conserva el alcance de esta separación; la migración todavía no se ejecutó.

## Repositorios previstos

La raíz tendrá un repositorio documental propio y Blends, Brix y Cellar tendrán repositorios independientes bajo esta carpeta, ignorados por el repositorio raíz y sin submódulos. Esta topología está acordada en VCX-D025. VCX-D026 añade un commit base documental transitorio antes de excluir los productos; el commit base `f47c71f` existe en `main` y su recuperación se verificó el 2026-11-01. Todavía hay enlaces documentales entre directorios que deben resolverse antes de un clon independiente. Los [requisitos de desacople](docs/architecture/overview.md#repositorios-y-desacople) fijan su preparación y comprobación.

El [alcance del commit base documental](docs/superpowers/plans/2026-10-31-root-baseline-scope.md) concreta los archivos, comandos y verificaciones propuestos para los pasos 1–2 del mapa. Fue autorizado en este chat con Codex el 2026-10-31. Su ejecución produjo el commit `f47c71f`; la [verificación de recuperación](docs/superpowers/reports/2026-11-01-root-baseline-verification.md) del 2026-11-01 cierra ese alcance. El [camino de migración](docs/superpowers/specs/2026-11-01-migration-path-design.md), VCX-D030, ratificada como decisión documental el 2026-11-01 y con ejecución pendiente, describe cómo seguiría: colocar un clon de autoría del precursor en `vcx/solera/` y extraer después. El [inventario de deuda heredada](docs/superpowers/specs/2026-11-01-inherited-debt-design.md), VCX-D031, ratificada el mismo día y con ejecución pendiente, asigna a cada ítem de desacople, nombres, Git y jerarquía su destino y su fase. La [organización en GitHub](docs/architecture/github-topology.md) muestra los repositorios de hoy y el objetivo de cada pieza, con lo que la transición no rompe. El [diseño de visibilidad](docs/superpowers/specs/2026-11-01-public-visibility-design.md), VCX-D032, ratificada el mismo día y con ejecución pendiente, hace públicos los productos y privados las instancias y proyectos, con CI sin cuota de Actions.

## Curación prioritaria

La siguiente preparación está detallada en el [mapa de archivos y repositorios](docs/architecture/repository-map.md): propiedad documental, enlaces entre repositorios, principios distribuibles, preservación y secuencia de versionado. Su transición fue reformulada mediante VCX-D026; la ejecución requiere alcance explícito antes de inicializar Git o mover archivos.

Blends y Cellar son proyectos pares de primer nivel. Se prioriza su curación documental en orden Cellar → Blends, según el [plan aprobado](docs/superpowers/plans/2026-10-30-blends-cellar-curation.md). Sus contextos están en los README de cada producto; el [reporte](docs/superpowers/reports/2026-10-30-blends-cellar-curation.md) conserva evidencia de esta etapa. Brix mantiene su lugar en la base reutilizable y `solera/` es la instancia de este workspace.

## Por dónde empezar

- Para entender el propósito: [misión y visión](docs/vision.md) y [speech ejecutivo](docs/executive-pitch.md).
- Para diseñar conexiones: [arquitectura](docs/architecture/overview.md), [responsabilidades](docs/architecture/responsibility-matrix.md) e [interoperabilidad](docs/architecture/interoperability.md).
- Para saber qué controles de seguridad y privacidad existen, cuáles están inactivos y cuáles solo propuestos: [inventario de controles](docs/architecture/security-controls-inventory.md), propuesta del 2026-11-01 con mediciones fechadas; no activa controles ni asigna responsables.
- Para entender el reparto entre método, conducción y capacidades: [modelo de productos](docs/superpowers/specs/2026-10-31-product-model-design.md), acordado en VCX-D029, con su [plan de aplicación](docs/superpowers/plans/2026-11-01-product-model-application.md) y el [reporte de ejecución](docs/superpowers/reports/2026-11-01-product-model-application.md).
- Para saber qué skills y MCP usa o propone cada fase: [matriz de tooling](docs/architecture/tooling-matrix.md), fuente transitoria según VCX-D028 que referencia el inventario del precursor sin copiarlo. Su [vista HTML por ubicación](docs/exports/tooling-matrix.html), con los consumidores de cada elemento en un popup, es una instantánea derivada con la revisión fuente indicada; no se edita a mano. Tras commitear la matriz, se regenera con `python3 -I docs/exports/build_tooling_matrix_view.py`, herramienta documental opcional sin dependencias externas.
- Para continuar la curación gradual: [primer recorrido Cellar–Blends](docs/superpowers/specs/2026-10-30-cellar-blends-first-journey-design.md), diseño propuesto con ejemplo ficticio y correspondencia con el sistema actual.
- Para preparar el ingreso de una idea: [flujo de documento, consejo y confirmación humana](blends/docs/idea-intake.md), con capacidad de Brix y plantilla de ideas; todavía sin comandos nuevos implementados.
- Para consultar las interfaces objetivo: [comandos de Brix y ayuda de parámetros](brix/docs/commands.md), con equivalencias `brix idea` ↔ `/idea` y `brix council` ↔ `/council`.
- Después del ingreso: [arquitectura de referencia y FinOps](blends/docs/architecture-and-finops.md), para estimar escenarios y decidir presupuesto con trazabilidad al modelo propuesto por Brix.
- Para explorar la jerarquía en un mapa mental: [mapa de VCX en OPML al 2026-11-01](docs/exports/vcx-ecosystem-2026-11-01.opml), vista derivada con VCX-D029 aplicado y las iniciativas del portfolio precursor; la [instantánea de la fundación](docs/exports/vcx-ecosystem.opml) del 2026-10-30 se conserva como histórica. Ninguna se actualiza automáticamente.
- Para iniciar un contexto: [plantillas de Cellar e iniciativas](cellar/README.md#plantillas-documentales).
- Para elegir nombres: [criterio de nombres](docs/naming.md) y [banco de candidatos sin curar](docs/references/enology-glossary-source.md).
- Para retomar decisiones: [registro de decisiones](docs/decisions/README.md), [fuentes](docs/sources.md) y [registro de ejecución](docs/superpowers/reports/2026-10-30-vcx-foundation.md).

Las instrucciones de trabajo están en [AGENTS.md](AGENTS.md). La [propuesta de fundación](docs/superpowers/plans/2026-10-30-vcx-foundation.md) delimita esta etapa.
