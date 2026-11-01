# Responsabilidades y RACI de VCX

Fecha: 2026-10-30. Estado: propuesta fundacional. Fuente editable vigente, derivada de la matriz histórica identificada en [fuentes](../sources.md). Las aprobaciones y pendientes se registran en [decisiones](../decisions/README.md); esta matriz no concede nuevos permisos. Reparto por tramo de idea y de proyecto aplicado el 2026-11-01 a partir de VCX-D029; no rige en el sistema existente hasta conciliar por VCX-D011.

## 1. Método y conducción

Reparto derivado de VCX-D029; fuente única de esta frontera, que las demás páginas enlazan sin copiar. Su redacción es propuesta del asistente sobre el modelo acordado.

- **Método, dueño Blends.** Toda regla que aplique a cualquier proyecto de cualquier Cellar: etapas, compuertas, criterios de evidencia, qué registra una decisión, roles y plantillas de proceso. Blends la publica versionada y la verifica; no ejecuta el proyecto.
- **Conducción, dueño Cellar.** Toda acción o decisión sobre un proyecto concreto después de graduar: planificar, priorizar, entregar, evolucionar y registrar, con el Product Owner (PO) del proyecto como autoridad humana. Cellar conduce aplicando el método adoptado; no redefine sus reglas.
- **Tramo de idea, coordina Blends.** Desde la propuesta hasta la graduación, Blends coordina actividades e hitos y la instancia de Cellar custodia. Decide el responsable del portfolio.
- **Capacidad, dueño Brix.** Todo cálculo, instrumento o integración reutilizable, invocado desde cualquiera de los dos tramos con permisos explícitos.

Prueba de pertenencia: si la frase vale para todos los proyectos, es método; si nombra a un proyecto, es conducción; si describe cómo se calcula o integra algo, es capacidad.

| Ejemplo ficticio, un directorio de talleres de cerámica | Pertenece a |
|---|---|
| «Cada decisión registra autoridad, revisión, alcance y qué no autoriza» | Método, Blends |
| «El directorio prioriza horarios antes que fotos en la primera entrega» | Conducción, Cellar; decide el PO |
| «Estimar el costo mensual del hosting del directorio» | Capacidad, Brix, invocada por Cellar bajo la plantilla FinOps del método |
| «Confirmar qué preguntas asesinas bloquean el gate» | Tramo de idea, coordina Blends; decide el responsable del portfolio |
| «Un Cellar debe poder leerse sin ejecutar Blends ni Brix» | Custodia, responsabilidad de Cellar; invariante conservado |
| «La propuesta del directorio está en preparación y todavía no eligió instancia» | Custodia previa al ingreso, fuera del portfolio activo hasta la confirmación de VCX-D017 |

Custodia y conducción son dos responsabilidades de Cellar, no dos módulos ni servicios; su separación ejecutable no tiene necesidad demostrada. El traspaso concreto al graduar, quién prepara el contexto, cuándo lo recibe Cellar, cómo acepta el PO su responsabilidad y qué ocurre si la preparación falla, sigue pendiente de diseño.

## 2. Matriz de responsabilidades técnicas propuesta

**Dueño** identifica a la pieza que mantiene una definición o información canónica; no concede autoridad humana ni permisos de ejecución. **Instancia** significa un Cellar concreto y, cuando corresponde, el contexto de la iniciativa que contiene.

| Responsabilidad | Blends | Brix | Cellar · producto | Cellar · instancia |
|---|---|---|---|---|
| Misión, visión y contexto de cada iniciativa | Facilita su elaboración y consulta durante el tramo de idea | Aporta instrumentos cuando se requieren | Define cómo organizarlos, referenciarlos y mantenerlos durante la conducción | Conserva la fuente propia de cada iniciativa |
| Proceso del tramo de idea: ingreso, exploración, definición, gate y preparación | Define el método y coordina su aplicación | Ejecuta capacidades solicitadas | Expone estructuras e interfaces para el estado | Conserva el perfil adoptado, parámetros y decisiones |
| Conducción del proyecto: planificación, entrega y evolución | Define el método que se aplica; no conduce | Ejecuta capacidades solicitadas | Define cómo se conduce bajo ese método: estructura de planificación, decisiones y entrega | Conduce el proyecto con su PO y custodia su estado |
| Autoridad, roles y compuertas | Define y verifica las reglas del proceso adoptado | Declara y exige los permisos de cada capacidad | Representa los datos y límites de acceso de su ámbito | Conserva asignaciones y aprobaciones verificables, incluidos el responsable del portfolio y el PO de cada proyecto |
| Capacidades e instrumentos reutilizables | Selecciona e invoca según el proceso | Dueño de implementación, catálogo e interfaz pública | Ofrece acceso explícito a los datos que corresponda | Conserva configuración de uso, resultados y evidencia pertinente |
| Estructura y acceso al portfolio | Consume interfaces públicas | Consume datos explícitos cuando la capacidad lo requiere | Dueño del formato y de sus interfaces públicas | Conserva identidad, localizaciones y estado del portfolio |
| Roadmap, backlog y dependencias | Coordina el seguimiento de las ideas; en proyectos solo mantiene el método de planificación | Calcula o valida cuando se solicita | Define representación, referencias y acceso | Conserva una fuente canónica por dato, incluso en almacenamientos declarados; en proyectos conduce roadmap y backlog |
| Decisiones, sesiones y evidencia | Coordina su producción y comprueba requisitos en ideas; define qué debe registrarse en proyectos | Produce resultados verificables | Ofrece mecanismos de custodia, integridad y recuperación | Conserva los registros y referencias de cada iniciativa o del portfolio; en proyectos conduce sesiones y decisiones con su PO |
| FinOps | Define el método FinOps; gobierna presupuestos, revisión y escalamiento de las ideas | Calcula, proyecta y valida | Organiza y expone los registros | Conserva fuentes, importes, asignaciones y decisiones sin doble conteo; en proyectos conduce presupuesto y revisión bajo ese método |
| Presentación del portfolio | Dueño de la interfaz y de la lógica de presentación | Aporta cálculos solicitados | Expone información mediante su contrato, incluido el estado de conducción de cada proyecto | Conserva preferencias; las vistas derivadas no sustituyen las fuentes |
| Código, configuración operativa y dependencias de una iniciativa | Mantiene el método; no coordina el ciclo de trabajo del proyecto | Aporta capacidades que la iniciativa adopta; no aloja su código | Permite declarar ubicaciones y referencias | Registra el dueño y la ubicación canónica y conduce el ciclo de trabajo; el proyecto conserva su contexto y su código en repositorio propio |
| Exportación, respaldo y recuperación del portfolio | Coordina el procedimiento cuando se usa Blends | Aporta instrumentos reutilizables que se invoquen | Define formato y mecanismos para preservar y restaurar estado | Declara almacenamientos, políticas y referencias; conserva evidencia de recuperación |
| Versiones y compatibilidad | Mantiene su versión y compatibilidades declaradas | Mantiene su versión y compatibilidades declaradas | Mantiene versiones de producto y formato explícitas | Fija las versiones adoptadas y registra sus actualizaciones |

El código de cada producto y de cada proyecto vive en su propio repositorio, según VCX-D029; pertenecer a un Cellar registra su ubicación canónica sin alojarlo. Los adaptadores de almacenamiento deben asignarse al dueño de la interfaz que implementan; su reparto concreto se resolverá al detallar las interfaces.

## 3. Propiedad de contratos

La fuente editable de este reparto es [interoperabilidad](interoperability.md).

## 4. Matriz RACI humana propuesta

Esta matriz complementa las responsabilidades técnicas. R = ejecuta; A = responde y decide; C = es consultado; I = es informado. Cada decisión concreta debe resolver los roles a personas y conservar un único A. Un agente puede actuar como R o C con alcance explícito; esta tabla no le otorga autoridad de aprobación.

| Decisión o actividad | R | A | C | I |
|---|---|---|---|---|
| Misión, visión y prioridades de una idea | Equipo de la idea | Responsable del portfolio | Usuarios y especialistas pertinentes | Participantes del Cellar |
| Exploración, presupuesto de exploración y gate de una idea | Equipo de la idea | Responsable del portfolio | Consejo, revisores y especialistas pertinentes | Participantes del Cellar |
| Graduar una idea y asignar el PO del proyecto | Equipo de la idea prepara el caso | Responsable del portfolio | PO propuesto y revisores | Participantes del Cellar |
| Misión, visión y prioridades de un proyecto | Equipo del proyecto | PO del proyecto | Usuarios y especialistas pertinentes | Responsable del portfolio |
| Roadmap, aceptación y continuidad de un proyecto | Equipo del proyecto | PO del proyecto | Revisores y responsables de dependencias afectadas | Responsable del portfolio |
| Cambiar la implementación de un producto de A | Equipo mantenedor del producto | Responsable del producto, según gobierno adoptado | Revisión independiente cuando corresponda | Consumidores afectados |
| Cambiar un contrato público o su compatibilidad | Mantenedor del contrato | Responsable designado para ese contrato | Mantenedores y consumidores afectados | Equipos que lo adopten |
| Adoptar o actualizar herramientas y perfiles en un Cellar | Equipo del Cellar | Responsable del Cellar | Mantenedores y responsables de iniciativas afectadas | Usuarios del Cellar |
| Presupuestos, sobrecostos y excepciones de autoridad | Equipo que prepara evidencia y propuesta | Responsable del portfolio en ideas y en el ámbito del portfolio; PO en el ámbito de su proyecto | Especialistas y responsables afectados | Equipos alcanzados |
| Configurar y verificar respaldo y recuperación | Operador designado | Responsable de custodia del Cellar | Responsables de almacenamientos e iniciativas | Propietario del portfolio |
| Cambiar controles compartidos del repositorio o de ejecución | Mantenedor de esos controles | Autoridad humana competente sobre ese ámbito | Responsables de las piezas afectadas | Equipos alcanzados |

Asignar el PO al graduar no retira la autoridad del responsable del portfolio sobre el portfolio: ambas asignaciones coexisten y se conservan. Qué decisiones concretas corresponden a cada uno después de graduar se precisa al diseñar el traspaso, pendiente. La tabla propone roles para equipos nuevos; en el sistema existente prevalecen las autoridades y decisiones vigentes hasta que se concilien explícitamente. No define un procedimiento nuevo de merge o despliegue.

## 5. Invariantes de diseño

1. Cada iniciativa puede entenderse y trabajarse desde su propio contexto; las dependencias y reglas compartidas se consultan de forma explícita.
2. Blends define el método y coordina el tramo de idea; Brix ejecuta capacidades; Cellar custodia en todas las etapas y conduce los proyectos bajo ese método. Ninguna pieza absorbe silenciosamente las otras responsabilidades.
3. Brix funciona sin Blends; Cellar conserva información legible y recuperable sin ejecutar Blends o Brix. Esta prueba corresponde a la custodia; conducir un proyecto requiere además el método adoptado disponible como recurso versionado, no una ejecución de Blends.
4. Un Cellar adopta versiones compatibles de A; actualizar A no actualiza silenciosamente todos los portfolios.
5. Blends, Brix y Cellar tienen contextos propios de desarrollo. Su seguimiento puede residir en un Cellar sin duplicar el código ni el estado de gestión.
6. Una iniciativa tiene un Cellar propietario de su registro canónico; otras instancias pueden referenciarla. Esta regla sigue propuesta; consultar el registro de decisiones.
7. Las políticas particulares solo modifican parámetros autorizados por el perfil adoptado; no elevan permisos ni anulan autoridad de ámbitos superiores.
8. Un monorepo no impone una versión, despliegue o contexto único. Los límites de dependencias deben ser comprobables.
9. La confidencialidad entre propietarios exige aislamiento efectivo del almacenamiento y acceso; una carpeta no es suficiente.
10. La exportación contempla los almacenamientos declarados fuera del árbol principal. Los secretos se reconectan desde sus almacenes seguros y los locks activos no se restauran como procesos vivos.


## Continuidad y límites

La matriz distribuye responsabilidades técnicas; la RACI asigna ejecución y autoridad a participantes. Las asignaciones concretas deben resolverse antes de operar. La [arquitectura](overview.md) explica la composición y el estado documental actual. La implementación y migración del sistema existente requieren sus alcances explícitos.
