# Responsabilidades y RACI de VCX

Fecha: 2026-10-30. Estado: propuesta fundacional. Fuente editable vigente, derivada de la matriz histórica identificada en [fuentes](../sources.md). Las aprobaciones y pendientes se registran en [decisiones](../decisions/README.md); esta matriz no concede nuevos permisos.

## 2. Matriz de responsabilidades técnicas propuesta

**Dueño** identifica a la pieza que mantiene una definición o información canónica; no concede autoridad humana ni permisos de ejecución. **Instancia** significa un Cellar concreto y, cuando corresponde, el contexto de la iniciativa que contiene.

| Responsabilidad | Blends | Brix | Cellar · producto | Cellar · instancia |
|---|---|---|---|---|
| Misión, visión y contexto de cada iniciativa | Facilita su elaboración y consulta | Aporta instrumentos cuando se requieren | Define cómo organizarlos y referenciarlos | Conserva la fuente propia de cada iniciativa |
| Proceso de exploración, planificación y entrega | Define el proceso y coordina su aplicación | Ejecuta capacidades solicitadas | Expone estructuras e interfaces para el estado | Conserva el perfil adoptado, parámetros y decisiones |
| Autoridad, roles y compuertas | Define y verifica las reglas del proceso adoptado | Declara y exige los permisos de cada capacidad | Representa los datos y límites de acceso de su ámbito | Conserva asignaciones y aprobaciones verificables |
| Capacidades e instrumentos reutilizables | Selecciona e invoca según el proceso | Dueño de implementación, catálogo e interfaz pública | Ofrece acceso explícito a los datos que corresponda | Conserva configuración de uso, resultados y evidencia pertinente |
| Estructura y acceso al portfolio | Consume interfaces públicas | Consume datos explícitos cuando la capacidad lo requiere | Dueño del formato y de sus interfaces públicas | Conserva identidad, localizaciones y estado del portfolio |
| Roadmap, backlog y dependencias | Coordina operaciones y seguimiento | Calcula o valida cuando se solicita | Define representación, referencias y acceso | Conserva una fuente canónica por dato, incluso en almacenamientos declarados |
| Decisiones, sesiones y evidencia | Coordina su producción y comprueba requisitos | Produce resultados verificables | Ofrece mecanismos de custodia, integridad y recuperación | Conserva los registros y referencias de cada iniciativa o del portfolio |
| FinOps | Gobierna presupuestos, revisión y escalamiento | Calcula, proyecta y valida | Organiza y expone los registros | Conserva fuentes, importes, asignaciones y decisiones sin doble conteo |
| Presentación del portfolio | Dueño de la interfaz y de la lógica de presentación | Aporta cálculos solicitados | Expone información mediante su contrato | Conserva preferencias; las vistas derivadas no sustituyen las fuentes |
| Código, configuración operativa y dependencias de una iniciativa | Coordina su ciclo de trabajo | Aporta capacidades que la iniciativa adopta | Permite declarar ubicaciones y referencias | Registra el dueño y la ubicación canónica; el proyecto conserva su contexto |
| Exportación, respaldo y recuperación del portfolio | Coordina el procedimiento cuando se usa Blends | Aporta instrumentos reutilizables que se invoquen | Define formato y mecanismos para preservar y restaurar estado | Declara almacenamientos, políticas y referencias; conserva evidencia de recuperación |
| Versiones y compatibilidad | Mantiene su versión y compatibilidades declaradas | Mantiene su versión y compatibilidades declaradas | Mantiene versiones de producto y formato explícitas | Fija las versiones adoptadas y registra sus actualizaciones |

La ubicación física del código de las iniciativas continúa abierta: pertenecer a un Cellar no decide por sí solo una carpeta o un repositorio. Los adaptadores de almacenamiento deben asignarse al dueño de la interfaz que implementan; su reparto concreto se resolverá al detallar las interfaces.

## 3. Propiedad de contratos

La fuente editable de este reparto es [interoperabilidad](interoperability.md).

## 4. Matriz RACI humana propuesta

Esta matriz complementa las responsabilidades técnicas. R = ejecuta; A = responde y decide; C = es consultado; I = es informado. Cada decisión concreta debe resolver los roles a personas y conservar un único A. Un agente puede actuar como R o C con alcance explícito; esta tabla no le otorga autoridad de aprobación.

| Decisión o actividad | R | A | C | I |
|---|---|---|---|---|
| Misión, visión y prioridades de una iniciativa | Equipo de la iniciativa | PO de la iniciativa | Usuarios y especialistas pertinentes | Responsables del portfolio |
| Roadmap, aceptación y continuidad de una iniciativa | Equipo de la iniciativa | PO de la iniciativa | Revisores y responsables de dependencias afectadas | Responsables del portfolio |
| Cambiar la implementación de un producto de A | Equipo mantenedor del producto | Responsable del producto, según gobierno adoptado | Revisión independiente cuando corresponda | Consumidores afectados |
| Cambiar un contrato público o su compatibilidad | Mantenedor del contrato | Responsable designado para ese contrato | Mantenedores y consumidores afectados | Equipos que lo adopten |
| Adoptar o actualizar herramientas y perfiles en un Cellar | Equipo del Cellar | Responsable del Cellar | Mantenedores y responsables de iniciativas afectadas | Usuarios del Cellar |
| Presupuestos, sobrecostos y excepciones de autoridad | Equipo que prepara evidencia y propuesta | PO o autoridad humana competente | Especialistas y responsables afectados | Equipos alcanzados |
| Configurar y verificar respaldo y recuperación | Operador designado | Responsable de custodia del Cellar | Responsables de almacenamientos e iniciativas | Propietario del portfolio |
| Cambiar controles compartidos del repositorio o de ejecución | Mantenedor de esos controles | Autoridad humana competente sobre ese ámbito | Responsables de las piezas afectadas | Equipos alcanzados |

La tabla propone roles para equipos nuevos; en el sistema existente prevalecen las autoridades y decisiones vigentes hasta que se concilien explícitamente. No define un procedimiento nuevo de merge o despliegue.

## 5. Invariantes de diseño

1. Cada iniciativa puede entenderse y trabajarse desde su propio contexto; las dependencias y reglas compartidas se consultan de forma explícita.
2. Blends coordina; Brix ejecuta capacidades; Cellar organiza y custodia. Ninguna pieza absorbe silenciosamente las otras responsabilidades.
3. Brix funciona sin Blends; Cellar conserva información legible y recuperable sin ejecutar Blends o Brix.
4. Un Cellar adopta versiones compatibles de A; actualizar A no actualiza silenciosamente todos los portfolios.
5. Blends, Brix y Cellar tienen contextos propios de desarrollo. Su seguimiento puede residir en un Cellar sin duplicar el código ni el estado de gestión.
6. Una iniciativa tiene un Cellar propietario de su registro canónico; otras instancias pueden referenciarla. Esta regla sigue propuesta; consultar el registro de decisiones.
7. Las políticas particulares solo modifican parámetros autorizados por el perfil adoptado; no elevan permisos ni anulan autoridad de ámbitos superiores.
8. Un monorepo no impone una versión, despliegue o contexto único. Los límites de dependencias deben ser comprobables.
9. La confidencialidad entre propietarios exige aislamiento efectivo del almacenamiento y acceso; una carpeta no es suficiente.
10. La exportación contempla los almacenamientos declarados fuera del árbol principal. Los secretos se reconectan desde sus almacenes seguros y los locks activos no se restauran como procesos vivos.


## Continuidad y límites

La matriz distribuye responsabilidades técnicas; la RACI asigna ejecución y autoridad a participantes. Las asignaciones concretas deben resolverse antes de operar. La [arquitectura](overview.md) explica la composición y el estado documental actual. La implementación y migración del sistema existente requieren sus alcances explícitos.
