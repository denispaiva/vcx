# Primer recorrido de VCX: una idea se prepara como proyecto

Fecha: 2026-10-30. Estado: diseño para revisión. El usuario eligió el tercer enfoque —un recorrido entre Cellar y Blends—; no se infiere aprobación de todos los detalles nuevos de este documento ni autorización para implementar o migrar el sistema existente.

## Intención

Curar gradualmente la estructura de VCX a partir de un caso que muestre cómo un equipo comienza una iniciativa con propósito y memoria propios. Comprobar primero las fronteras entre información, proceso y capacidades antes de ampliar carpetas o construir herramientas.

## Enfoques y elección

| Enfoque | Beneficio | Costo o riesgo | Resultado |
|---|---|---|---|
| Blends primero | Parte del proceso conocido | Puede trasladar supuestos y rutas del portfolio original | No elegido para esta etapa |
| Cellar completo primero | Ordena toda la información de antemano | Puede sobrediseñar sin validar uso | No elegido para esta etapa |
| Un recorrido entre ambos | Contrasta responsabilidades con un caso acotado | Exige delimitar el corte | Elegido por el usuario: «Vamos con el tercero» |

## Objetivos, límites y criterios de fallo

El resultado es un diseño documental: [modelo mínimo de Cellar](https://github.com/denispaiva/cellar/blob/main/docs/initiative-model.md), [recorrido de Blends](../../../blends/docs/idea-to-project.md), [correspondencia con lo existente](../../architecture/current-system-mapping.md) y el ejemplo sintético de este documento.

**Requisito de ingreso añadido por el usuario:** `/idea <texto o archivo>` sobre Brix aplica la plantilla de ideas e invoca las preguntas asesinas. El Markdown se revisa con el humano; se informa su envío al consejo y, con el OK, se consulta `/council <archivo.md>`. La idea ingresa en Cellar solo después de que el humano revise el reporte y confirme su aceptación. La [secuencia de ingreso](../../../blends/docs/idea-intake.md), la [capacidad de Brix](../../../brix/docs/idea-intake.md) y la [plantilla de ideas](https://github.com/denispaiva/cellar/blob/main/templates/idea/README.md) precisan ese requisito. No se implementan comandos en este corte.

**Requisito posterior al ingreso:** el siguiente entregable es FinOps, construido desde el modelo propuesto por la [capacidad de arquitectura de referencia de Brix](../../../brix/docs/reference-architecture.md). La [etapa de Blends](../../../blends/docs/architecture-and-finops.md) aplica la [plantilla FinOps](https://github.com/denispaiva/cellar/blob/main/templates/finops/README.md) y conduce la decisión de presupuesto. Modelo y estimación son propuestas; no convierten la idea en proyecto ni autorizan construcción.

**Nombres y ayuda fijados después por el usuario:** `brix idea` = `/idea` y `brix council` = `/council`. La [definición común de comandos](../../../brix/docs/commands.md) mantiene una capacidad por función, asistencia para completar parámetros y distinción entre ayuda y ejecución. El singular `/idea` reemplaza la formulación inicial `/ideas` en el diseño vivo; no se crea otro alias por inferencia.

Quedan fuera de este corte la creación de una instancia real, la implementación de una API, la asignación de nombres del glosario, la instalación de herramientas y la conexión de escritores al sistema existente. Tampoco se inicializa Git. Las capacidades concretas de Brix se elegirán por necesidad, no por completar un catálogo.

Serían fallos del diseño: duplicar un roadmap, confundir una recomendación con una aprobación, graduar por cambiar una carpeta, perder la captura original, asumir que el primer proyecto necesita todo el portfolio, o trasladar código antes de decidir su localización y autoridad.

## Fuentes y propiedad documental

| Tema | Fuente editable de este corte |
|---|---|
| Datos, identidad y referencias | Modelo mínimo de Cellar enlazado arriba |
| Preparación, dos revisiones humanas e ingreso | Secuencia de ingreso de Blends enlazada arriba |
| Entradas y resultados del instrumento de preparación | Capacidad de Brix enlazada arriba |
| Forma del documento revisable | Plantilla de ideas enlazada arriba |
| Modelo propuesto de arquitectura para estimar | Capacidad de arquitectura de referencia enlazada arriba |
| Presupuesto y escenarios posteriores al ingreso | Etapa de Blends y plantilla FinOps enlazadas arriba |
| Secuencia, condiciones y autoridad | Recorrido de Blends enlazado arriba |
| Evidencia del sistema actual y conciliación | Correspondencia enlazada arriba |
| Ejemplo y criterios de aceptación conjuntos | Este documento |
| Aprobaciones y pendientes de arquitectura | [Registro de decisiones](../../decisions/README.md) |

Los demás README y matrices enlazan estas definiciones. Las fuentes reales permanecen en blends; no se copian sus datos operativos como nuevo portfolio de VCX.

## Recorrido de referencia

Entrada de texto o archivo → preparación en Brix con plantilla y preguntas asesinas → revisión humana del Markdown → consejo informado sobre esa revisión → entrega de reporte → confirmación humana de ingreso → idea `registered` → arquitectura de referencia propuesta → documento FinOps → decisión del presupuesto de exploración → exploración → definición → decisión de graduación del PO → preparación del contexto de proyecto. En el gate de graduación también se puede diferir o archivar; sin respuesta se conserva la solicitud pendiente. La graduación prepara gobierno y contexto, no código o despliegue.

La identidad de iniciativa permanece; cambian su tipo y la etapa correspondiente una vez completada la preparación. El estado de trabajo del proyecto sigue separado de su ciclo de idea. El modelo define esa información y el recorrido define sus transiciones; este resumen no introduce reglas adicionales.

## Ejemplo sintético: coordinación de turnos

**Todos los nombres, afirmaciones, presupuestos, respuestas y aprobaciones de este ejemplo son ficticios.** No son entrevistas, resultados, evidencia o decisiones reales. `example-portfolio` y `example-initiative` son marcadores ilustrativos; no reservan identidades ni crean el primer Cellar.

| Momento | Contexto ilustrativo | Registro y resultado esperado |
|---|---|---|
| Entrada | `/idea` recibe «Quiero que un equipo pequeño coordine turnos sin perder acuerdos», en texto o archivo | Fuente original y proceso de preparación `example-submission`; todavía no hay una idea registrada |
| Preparación | Brix aplica la plantilla, formula preguntas asesinas y separa supuestos de lo informado | Documento Markdown identificable; cada sección pendiente aparece como tal |
| Propósito propuesto | Misión: facilitar acuerdos claros de turnos. Visión: un equipo conserva una agenda comprensible y el historial de sus acuerdos | Se marcan como formulaciones propuestas, no como cita del autor |
| Revisión inicial | El humano ficticio corrige el documento y da OK después de ser informado de la consulta y del presupuesto del consejo | Se registra el OK para enviar esa revisión; no equivale a ingreso o graduación |
| Consejo | `/council <archivo.md>` analiza la revisión autorizada y produce un reporte ficticio de asesoría | El humano recibe el reporte y sus límites; no se finge evidencia de entrevistas o uso real |
| Ingreso | Tras revisar documento y reporte, el humano ficticio competente confirma el ingreso en el Cellar ilustrativo | Nace la iniciativa `example-initiative`, enlazada a `example-submission`; `kind=idea`, ciclo `registered`, una fuente activa |
| Arquitectura de referencia | Brix propone un modelo orientativo: experiencia de agenda, registro de acuerdos y acceso del equipo; compara usar herramientas existentes y construir algo propio | Modelo ficticio M-01 con componentes, actividades, supuestos y revisión; no se elige proveedor ni se genera código |
| FinOps | La plantilla relaciona componentes y esfuerzo con escenarios; los costos de una operación futura quedan pendientes de fuentes y volumen. La solicitud inmediata se limita a revisión manual de exploración | Documento ficticio F-01 enlazado a M-01, con cobertura y límites explícitos; el PO ficticio puede autorizar dos horas de exploración sin servicios pagos. No aprueba construcción u operación |
| Exploración | PO ficticio autoriza hasta dos horas de revisión manual, sin servicios pagos. Pregunta decisiva: ¿una agenda simple alcanza o se necesita otro producto? | Presupuesto del ejemplo y ciclo `exploring`; respuestas con referencias sintéticas E-01 y E-02, rotuladas como tales |
| Definición | Para recorrer la rama de graduación se supone que la evidencia ficticia favorece una solución mínima; se comparan agenda existente y prototipo futuro | Definición acotada, límites, riesgos y solicitud de gate sobre revisión R-03; ciclo `gate-ready` |
| Gate | PO ficticio emite decisión D-01 sobre R-03 para graduar; explicita riesgos y excluye autorización de gasto, código y nube | Se conserva D-01. La recomendación de una herramienta no sustituye esa decisión |
| Preparación | Se establecen misión, visión, autoridad, referencias a evidencia, acta y planificación documental propia | Una fuente activa, identidad conservada, `kind=project`, ciclo `graduated`; ubicación del código declarada pendiente, sin inventar implementación |
| Continuidad | Un agente ficticio abre solo la entrada del proyecto y lee lo necesario para preparar un primer plan | Encuentra propósito, situación, autoridad, decisión y fuentes sin cargar otros proyectos; el plan de construcción se decide después |

El mismo recorrido puede terminar honestamente en diferimiento o archivo si la evidencia no justifica crear otro producto. El ejemplo no promueve construir cuando una agenda existente resuelva la necesidad.

## Casos que debe poder explicar el diseño

| Caso | Resultado observable esperado |
|---|---|
| Entrada mínima con visión pendiente | Se prepara un borrador; no se registra antes del consejo y la confirmación final, ni se inventa una visión aprobada |
| Comando sin parámetro en conversación o terminal interactiva | Se ofrece ayuda y se solicita el texto o archivo apropiado antes de ejecutar |
| Entrada ambigua o varios archivos disponibles | Se pide aclaración o selección dentro del ámbito autorizado, sin adivinar |
| Solicitud de ayuda o cancelación | No se genera documento, consulta al consejo o registro de idea |
| Entrada no válida en modo no interactivo | Se devuelve un diagnóstico accionable, sin bloquear esperando interacción |
| Archivo PDF ilegible o incompleto | Se informa el límite y se solicita completar la entrada; no se inventa contenido |
| Documento enriquecido sin OK inicial | No se envía al consejo ni se registra una idea |
| OK inicial sin reporte del consejo | No se registra una idea; el OK habilita la consulta informada, no el ingreso |
| Reporte disponible sin confirmación final | La propuesta permanece pendiente, fuera del índice de ideas aceptadas |
| Consejo propone cambios materiales | Se revisa el documento con el humano y se evalúa de nuevo la revisión que sustenta el ingreso |
| Exploración sin presupuesto declarado | Blends mantiene pendiente su inicio; una herramienta no compromete atención por el PO |
| FinOps sin revisión identificada de arquitectura | Se informa base incompleta y se solicita el modelo; no se presenta un total como sustentado |
| Tarifa o componente desconocido | Se declara incertidumbre y cobertura incompleta; desconocido no equivale a costo cero |
| Cambio material de arquitectura o volumen | Se revisan estimación y vigencia del presupuesto; no se amplía la autorización automáticamente |
| Estimación de construcción junto a presupuesto de exploración | Solo queda autorizada la fase que indica la decisión humana |
| Preparación del modelo sin límite de análisis autorizado | Se solicita el alcance permitido antes de consumir recursos no autorizados; no se usa el presupuesto futuro como permiso retroactivo |
| Pregunta decisiva sin evidencia | No pasa el gate ordinario; una excepción exige autoridad y riesgo explícitos |
| Recomendación favorable sin decisión humana | No se publica proyecto graduado |
| Decisión de otro Cellar o de actor sin autoridad | Se rechaza la aplicación sin alterar el estado publicado |
| Cambio material después de aprobar R-03 | Se solicita revisar la decisión; no se aplica a otra revisión por inferencia |
| Falla durante la preparación | Se conserva la aprobación y se informa preparación pendiente; no aparecen dos seguimientos activos |
| Reintento de la misma graduación | Se reanuda o devuelve el mismo resultado, sin nuevo proyecto o acta |
| Diferimiento | Se conserva contexto y disparador de revisión, sin crear proyecto |
| Archivo | Se conservan razón, evidencia e identidad; no se borra la exploración |
| Renombre visible o movimiento de carpetas | La identidad y referencias históricas siguen resolviendo |
| Proyecto graduado sin código | Es un resultado válido; no simula despliegue o construcción |

Estos casos son criterios de diseño, no pruebas ejecutables superadas. Un primer ensayo implementado deberá usar datos sintéticos y almacenamiento aislado; no se autoriza en esta entrega.

## Criterios para aceptar este corte documental

- El lector puede asignar cada dato a una fuente y cada acción a su responsable.
- Una propuesta pasa por plantilla, preguntas asesinas, revisión humana, consejo por archivo, reporte y confirmación de ingreso antes de `registered`.
- FinOps posterior al ingreso referencia una revisión de arquitectura y separa escenarios, presupuesto, proyección y gasto real; la autorización identifica fase y límites.
- El ejemplo se recorre sin datos reales y sin depender de rutas del portfolio actual.
- Misión, visión e identidad sobreviven a la graduación; el estado de trabajo no se confunde con el ciclo de idea.
- Se explica la autoridad, el tratamiento de excepciones y la recuperación de una preparación incompleta.
- La correspondencia conserva las decisiones aprobadas del kernel y el backlog de `queue`, señalando diferencias sin resolverlas mediante movimientos.
- Las decisiones nuevas están distinguidas de lo aprobado y los enlaces documentales resuelven.

## Criterios fijados por el autor para hacer el diseño concreto

Se propone conservar una sola identidad de iniciativa, separar `lifecycleState` de las referencias de trabajo, cargar el contexto progresivamente y tratar la preparación como una operación reanudable sobre una revisión identificada. Son criterios de diseño para revisar, no acuerdos nuevos atribuidos al usuario.

No hace falta elegir nombre del primer Cellar, backend o protocolo para aceptar este corte documental. Antes de una implementación se deberá elegir almacenamiento y formato, cerrar las interfaces y su autoridad, planificar verificaciones y definir publicación consistente o recuperación. Esas decisiones no se delegan implícitamente a una migración del sistema activo.

## Continuación

Primero revisar este diseño. Si se acepta, preparar un plan de ajustes de plantillas y casos de aceptación documentales que materialice el modelo, conservando el sistema existente en solo lectura. Una prueba ejecutable aislada, una instancia real o una migración requieren sus respectivos alcances explícitos.

## Verificación de esta entrega

La versión inicial de este diseño pasó una revisión independiente de constructor sin preguntas importantes pendientes para planificar el corte documental. El requisito posterior de ingreso mediante Brix, asesinas y consejo recibió otra revisión independiente, también sin preguntas o defectos importantes para planificar ese alcance. La segunda revisión comprobó la distinción entre propuesta, OK de envío, admisión y graduación, así como propiedad, revisiones y fuente única. Ninguna revisión aprueba las decisiones por el usuario o verifica capacidades ejecutables.

La comprobación del primer corte recorrió 27 archivos Markdown y 113 enlaces locales o anclas válidos. Es evidencia de aquella versión, no del alcance ampliado. Se verificaron los seis estados de ciclo, el carácter sintético del ejemplo y la distinción entre proceso, modelo y fuentes actuales. No se creó una instancia o repositorio Git y la copia del glosario permaneció idéntica al original aportado.

Las escrituras del primer corte se limitaron a VCX: cuatro documentos de diseño nuevos y enlaces o estados en seis documentos existentes. El requisito posterior añade una plantilla de ideas y documentos de ingreso, sin modificar las plantillas anteriores o el OPML —instantánea de la fundación inicial— ni archivos del sistema en funcionamiento. Las lecturas de Git no hicieron checkout, fetch o sincronización de `queue`.

La comprobación final de la ampliación recorrió 30 documentos Markdown y 132 enlaces locales o anclas válidos. Se verificaron los 21 marcadores de la plantilla de ideas con sustituciones sintéticas y la presencia de fuentes, preguntas asesinas, reporte y referencias de las dos decisiones humanas. No se ejecutó `/ideas`, `/council`, una extracción de PDF o un ingreso real: sus capacidades nuevas siguen siendo requisitos de diseño. El sistema existente no recibió escrituras y el glosario permanece íntegro.

La incorporación posterior de arquitectura de referencia y FinOps pasó otra revisión independiente de constructor, sin cuestiones importantes para planificar el alcance documental. Se verificaron 33 documentos Markdown, 148 enlaces locales o anclas y los 18 marcadores de la plantilla FinOps. La revisión comprobó el orden arquitectura–FinOps, las fuentes y responsabilidades, la autorización por fase y los límites previos para el análisis. No se consultaron precios reales, se generó un presupuesto operativo o se ejecutaron capacidades nuevas; los valores y aprobaciones concretos siguen correspondiendo a cada iniciativa y su autoridad.
