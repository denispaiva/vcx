# Brix

## Misión

Proveer capacidades e instrumentos técnicos reutilizables que ejecuten operaciones con entradas, permisos y resultados verificables.

## Visión

Que proyectos y equipos puedan adoptar capacidades de ingeniería de forma independiente, con beneficio demostrable, interfaces estables y configuración explícita, tanto dentro como fuera de Blends.

## Destinatarios y alcance

Se dirige a desarrolladores, agentes, proyectos y orquestadores. El alcance conceptual incluye scoring y evaluación de herramientas, medición, generación de especificaciones y scaffolding, motores de FinOps, validación y siembra de escenarios, diseño y operaciones Git. La disponibilidad real de cada capacidad debe verificarse en su implementación; esta lista no declara todas como implementadas.

**Entradas previstas:** solicitudes, datos, configuración y permisos explícitos, junto con drivers cuando una capacidad los requiera.

**Resultados previstos:** resultados estructurados, diagnósticos, errores y evidencia reproducible con límites claros.

Brix no prescribe el proceso de gobierno de un equipo ni adopta decisiones en su nombre. No presupone un Cellar, busca rutas históricas de Blends o accede a implementaciones privadas ajenas. Los drivers que conocen un backend particular pertenecen al producto consumidor.

Brix es el núcleo de capacidades técnicas de VCX, según VCX-D029. La denominación «kernel» queda reservada al núcleo de gobierno del sistema existente, conforme a la [arquitectura](../docs/architecture/overview.md#fronteras-y-contexto). El código específico de cada producto y de cada proyecto vive en su propio repositorio; Brix provee capacidades y no aloja ese código.

## Estado y contexto

La [capacidad de preparación de ideas](docs/idea-intake.md) documenta el requisito `/idea <texto o archivo>`: aplicar una plantilla, invocar preguntas asesinas y producir un Markdown revisable. Aún no está implementada y no equivale al generador de especificaciones `brix idea` del sistema existente.

Las [interfaces de comandos](docs/commands.md) fijan `brix idea` = `/idea` y `brix council` = `/council`, con ayuda para completar parámetros. Son capacidades objetivo compartidas entre CLI y conversación; Blends coordina su uso dentro del recorrido. Las skills propias viven en `.agents/skills/`, la carpeta del estándar abierto que Codex descubre, con un symlink en `.claude/skills/` para Claude Code; se descubren solo desde este directorio, y otro consumidor las copia con su procedencia, según VCX-D033. `brix-llm-council` sigue en `.claude/skills/` mientras el `evaluatedRef` de su evaluación bajo VCX-D035 apunte a esa ruta.

La [capacidad de arquitectura de referencia](docs/reference-architecture.md) documenta el modelo propuesto que alimentará FinOps después del ingreso de la idea. Su interfaz está por implementar; el motor de ledger existente no demuestra generación automática de arquitectura o estimaciones.

Aquí se documenta el producto objetivo. El Brix existente tiene independencia parcial y todavía contiene dependencias de rutas de blends, descritas en los antecedentes. La prueba de uso externo es una meta pendiente; no se afirma haberla superado. No se copia código ni se crea otro roadmap.

Para trabajar: leer este documento y [AGENTS.md](AGENTS.md). Consultar [interoperabilidad](../docs/architecture/interoperability.md), [matriz](../docs/architecture/responsibility-matrix.md) y [decisiones](../docs/decisions/README.md) según la tarea. Los [antecedentes](../docs/sources.md) identifican la implementación original.
