# Maduración de ideas, preguntas asesinas y graduación

Fecha: 2026-10-31. Estado: propuesta de diseño para revisión. Recoge acuerdos de esta conversación y propone su aplicación al modelo documental; todavía no reemplaza las fuentes de proceso ni modifica el precursor.

## Acuerdos y alcance

El usuario define la idea como el estado más atómico y primitivo: madura mediante preguntas asesinas y puede descartarse o graduarse. Propone un semáforo y categorías que permitan distinguir, por ejemplo, valor de viabilidad económica.

La precisión posterior «El MVP no debe ser mandatorio, sino recomendado», confirmada con «correcto, sigamos», sustituye la formulación anterior de la conversación que lo hacía primer estado obligatorio después de graduar. Las fuentes documentales actuales lo sitúan antes del gate, como «hipótesis de MVP» en el paso 3 de Blends y en `definitionRef` de Cellar; esa exigencia también debe ajustarse. Se conserva como recomendación cuando ofrece una validación útil y proporcionada.

La propuesta concreta de categorías, colores y reglas de decisión de este documento requiere revisión. No se atribuyen al usuario sus detalles por haber autorizado continuar el diseño.

Este corte define un modelo conceptual y los cambios documentales necesarios. No define almacenamiento, API, nuevos comandos o migración; tampoco autoriza consejo, gastos, código o instancias reales.

Lectura según VCX-D029, 2026-11-01: la autoridad humana del gate mencionada en este documento es el responsable del portfolio, que al graduar asigna el PO del proyecto; desde la graduación Cellar conduce el proyecto bajo el método de Blends. Esa lectura no aprueba el cambio del criterio del gate propuesto más abajo, que sigue pendiente de aprobación y conciliación.

## Alternativas consideradas

| Alternativa | Ventaja | Límite |
|---|---|---|
| Resolver todas las preguntas antes de graduar | Gate fácil de explicar | Puede exigir construir para obtener la evidencia que impide construir |
| Graduar y exigir siempre un MVP | Ofrece una primera entrega reconocible | Puede imponer un producto cuando una prueba manual basta o la evidencia ya existe |
| Evaluar evidencia para el siguiente compromiso y recomendar MVP | Ajusta inversión y validación a la incertidumbre | Exige declarar qué preguntas bloquean ese compromiso y cuáles resolverá |

Se propone la tercera. La flexibilidad no permite llamar validación a cualquier trabajo: cada paso necesita propósito, límites y criterios observables.

## Una idea que conserva su historia

En el lenguaje de trabajo se habla de ideas y, después de graduar, proyectos. No se exige crear una entidad de negocio adicional denominada iniciativa para explicar ese recorrido.

Se conserva por ahora el identificador técnico `initiativeId` del [modelo de Cellar](../../../cellar/docs/initiative-model.md): una misma identidad desde el registro y durante la graduación. Cambiar el nombre visible o la clasificación no crea otro objeto activo ni duplica su seguimiento. Renombrar campos técnicos queda fuera de este diseño.

La preparación previa mantiene `submissionId` y su relación con el registro posterior. Esto representa procedencia y admisión, no dos ideas editables en paralelo. No se cambia la confirmación humana posterior al reporte del consejo establecida en VCX-D017 del [registro](../../decisions/README.md).

Se mantienen los estados existentes `registered`, `exploring`, `gate-ready`, `graduated`, `deferred` y `archived`. MVP es una modalidad de trabajo, no otro estado del ciclo. El seguimiento del proyecto conserva su dimensión propia; graduado no significa construido ni activo.

## Qué es una pregunta asesina

Pone a prueba un supuesto cuya refutación podría cambiar una decisión concreta: abandonar, diferir, simplificar o elegir otra alternativa. Una pregunta interesante sin consecuencias para la decisión no necesita esta categoría.

Cada pregunta registra, de forma proporcional al riesgo:

- Supuesto, alcance y revisión a los que aplica; categoría principal.
- Decisión o compromiso que podría bloquear y consecuencia de una respuesta negativa.
- Criterio observable de respuesta y evidencia disponible, con procedencia y límites.
- Resultado actual, incertidumbre y responsable de revisar la evidencia.
- Si sigue abierta: acción para resolverla, responsable, plazo o disparador y límite de recursos.

La autoridad humana del gate confirma cuáles son decisivas y su clasificación como bloqueantes o pendientes de validación, con el fundamento registrado en la revisión presentada; una lista generada por un modelo es una propuesta. No se exige una pregunta por categoría ni un número fijo. Un reporte del consejo aporta asesoría: no sustituye evidencia del mundo real ni autoridad de decisión.

### Categorías propuestas

| Categoría | Qué pone a prueba |
|---|---|
| Problema y valor | Existencia y relevancia de la necesidad; resultado que mejoraría |
| Adopción | Acceso, disposición y capacidad de las personas para usar la solución |
| Viabilidad técnica | Factibilidad, integración, rendimiento y recuperación requeridos |
| Viabilidad económica y FinOps | Costo de validar, construir y operar frente al valor y los recursos disponibles |
| Riesgos y restricciones | Seguridad, privacidad, obligaciones y límites operativos aplicables |

Las preguntas económicas referencian el escenario y las líneas del documento FinOps; no copian importes como otra fuente editable. Se elige una categoría principal y se referencian consecuencias en otras, sin duplicar la pregunta. La categoría organiza la lectura; no suma puntos ni determina por sí sola prioridad. Los criterios se concretan por idea, sin introducir un catálogo obligatorio de controles.

### Semáforo propuesto

| Señal | Significado para el supuesto y escenario evaluados |
|---|---|
| Gris · sin evaluar | Todavía no se evaluó el supuesto |
| Amarillo · incierto | Evaluado sin conclusión; registra motivo: evidencia insuficiente, contradictoria o ambas |
| Verde · sustentado | La evidencia satisface el criterio declarado dentro de sus límites |
| Rojo · refutado | La evidencia contradice el criterio declarado en ese escenario |

La señal acompaña a una afirmación explícita, por ejemplo «la operación cabe en el presupuesto», evitando que una pregunta redactada en negativo invierta el significado. No aplicable se justifica aparte y no equivale a verde.

No hay nota global ni promedio. Las vistas de categoría muestran preguntas y cantidades por señal, destacando las que bloquean el compromiso solicitado; no guardan otro estado editable. Un verde técnico no compensa un rojo económico. Aceptar un riesgo no cambia el color de la evidencia.

Cambiar materialmente el escenario o encontrar evidencia contradictoria exige revisar la clasificación antes de reutilizarla. Se conserva el resultado histórico y se muestra que su aplicabilidad está pendiente. Para el gate, una evaluación con vigencia pendiente cuenta como gris, sin reescribir su color histórico ni heredar un verde. La vista distingue «sin evaluar» de «vigencia pendiente». Un amarillo por contradicción exige identificar las fuentes en conflicto y cómo resolverlo; aceptar la incertidumbre no equivale a resolverla.

## Graduación y siguiente compromiso

### Cambio propuesto del gate y vigencia

El [recorrido actual](../../../blends/docs/idea-to-project.md) requiere preguntas decisivas respondidas con evidencia. El estándar del precursor, `vc/docs/standards/idea-lifecycle.md`, exige responder todas las asesinas antes de graduar, según lectura del 2026-10-31. Esta propuesta sustituiría ese criterio por: **todas las preguntas bloqueantes resueltas con evidencia vigente; solo pueden quedar abiertas aquellas cuya validación dependa justificadamente del compromiso de proyecto delimitado**.

Es un cambio de política, no una aclaración ni una aprobación ya obtenida. Hasta su aprobación explícita y conciliación mediante VCX-D011, bajo el gobierno de Blends conservado por VCX-D026, sigue rigiendo el gate actual. No se incorporarán dos reglas de graduación activas al mismo repositorio. Las desviaciones históricas conservan esa condición y sus actas; este diseño no las regulariza retroactivamente.

### Frontera entre exploración y proyecto

La opción por defecto para resolver una pregunta abierta es continuar la exploración acotada. Acotar el siguiente paso, necesitar código o carecer de presupuesto exploratorio no justifican por sí solos graduar: la exploración puede incluir un prototipo o una prueba técnica debidamente autorizados.

Para dejar una asesina pendiente en una graduación ordinaria propuesta deben registrarse estas condiciones comprobables:

1. Qué evidencia exige construir o usar la solución en el alcance concreto del proyecto, y por qué una investigación, simulación, prueba manual o prototipo exploratorio menor no la obtendría con fidelidad suficiente.
2. Qué entrega, usuarios o condiciones de operación hacen necesaria esa validación y qué resultado permite decidir continuar o detenerse.
3. Qué alcance, capacidad, responsables y límites de recursos hacen viable producir esa evidencia; la incertidumbre no puede impedir realizar la propia validación de forma permitida y segura.

Si no se demuestra esa dependencia, la pregunta sigue siendo bloqueante y se resuelve antes de graduar. Si hay una vía exploratoria adecuada pero no hay recursos, corresponde solicitar su autorización o diferir; no convertir la falta de recursos en una dependencia de proyecto. La clasificación y su evidencia quedan en la revisión del gate, confirmadas por su autoridad. Cada reclasificación identifica condición anterior, nueva condición, motivo y evidencia; un cambio material posterior requiere revisar la aplicabilidad de la decisión antes de actuar.

Para una graduación ordinaria, todas las preguntas bloqueantes deben estar verdes con evidencia vigente y trazable, además de cumplirse las condiciones de capacidad y ausencia de impedimentos aplicables. Las pendientes admisibles identifican la validación anterior y sus criterios de salida. Si falta cualquiera de esas condiciones, graduar requiere una excepción explícita, no renombrar la pregunta. Las excepciones conservan autoridad, motivo y riesgo, sin declarar cumplido lo exceptuado ni exceptuar obligaciones ajenas.

Las decisiones continúan siendo humanas: graduar, diferir o archivar. Un rojo no archiva automáticamente y ningún conjunto de verdes gradúa automáticamente. El semáforo informa; la decisión registra su fundamento y revisión.

Graduar autoriza preparar el contexto de proyecto. La ejecución del siguiente paso requiere además autorización de su alcance y recursos: pueden registrarse en la misma decisión si son explícitos, pero no se deducen de la graduación. Se conservan las reglas de preparación reanudable del [recorrido actual](../../../blends/docs/idea-to-project.md).

### MVP recomendado, sin obligatoriedad

La idea propone una vía de validación. Se recomienda MVP cuando entregar una versión mínima utilizable es la forma proporcionada de obtener evidencia. También puede convenir una prueba manual, prototipo, piloto o implementación directa respaldada por evidencia previa suficiente. La elección explica por qué responde a la incertidumbre relevante y por qué no basta una alternativa más simple.

El siguiente paso declara:

- Hipótesis o resultado buscado y evidencia previa que lo justifica.
- Modalidad elegida, alcance y exclusiones.
- Autoridad, responsable, revisión y recursos autorizados por fase, incluido esfuerzo humano.
- Criterios de éxito, detención y decisión posterior, con plazo o disparador.
- Preguntas pendientes que resolverá y tratamiento de los riesgos que no resolverá.

Para implementación directa ordinaria, todas las preguntas bloqueantes para construir deben estar verdes con evidencia vigente, verificable y pertinente al escenario. Se admiten fuentes primarias externas, mediciones propias reproducibles o resultados comprobados del sistema existente; exigir únicamente procedencia externa descartaría evidencia técnica válida. Un reporte del consejo o una afirmación de un modelo, por sí solos, no cumplen el umbral. La justificación identifica qué evidencia evita repetir una validación y cuáles son los riesgos residuales. Una pregunta que requiere esa construcción para responderse corresponde a la vía de construcción para validar, no a implementación directa ya validada; una bloqueante sin resolver exige excepción explícita. No habilita desplegar, contratar servicios o gastar fuera del alcance aprobado.

No se diseña un MVP ficticio para completar la plantilla cuando otra vía resulta más adecuada. Un paso experimental que pueda realizarse adecuadamente en exploración permanece allí. Graduar con validación pendiente exige satisfacer la prueba de dependencia anterior; la etiqueta MVP, piloto o proyecto no la sustituye.

La [secuencia de arquitectura de referencia y FinOps](../../../blends/docs/architecture-and-finops.md) se conserva. Una estimación autoriza solo lo expresamente aprobado; desconocido no significa costo cero. La profundidad del modelo debe corresponder al compromiso evaluado.

## Casos de contraste ficticios

| Caso | Lectura y consecuencia esperada |
|---|---|
| Problema demostrado, operación demasiado cara | Valor puede estar verde y FinOps rojo para esa arquitectura/carga. Evaluar simplificación u otro escenario; diferir o archivar requiere decisión, no promedio |
| Adopción desconocida; una prueba manual económica puede medirla | Adopción permanece amarilla o gris según la evaluación. Resolver con la prueba en exploración: en este caso no se justifica graduar con esa pregunta pendiente; hacerlo exige excepción. MVP no obligatorio |
| La adopción solo puede medirse con uso sostenido de una entrega integrada | Justificar por qué pruebas menores no bastan; solo admitirla pendiente si alcance, usuarios, permisos, capacidad y límites permiten esa validación. Sin esa justificación, sigue bloqueando |
| Evidencia contradictoria sobre adopción | Amarillo con motivo contradictoria y fuentes identificadas; si bloquea, resolver el conflicto antes del gate ordinario. Aceptar el riesgo requiere excepción y no cambia el color |
| Evidencia previa suficiente para construir | Considerar implementación directa con límites y criterios. No fabricar un MVP documental ni omitir autorización de ejecución |
| API crítica cae durante una validación | Registrar interrupción y resultados parciales; no interpretar ausencia de datos como refutación de valor. Reintentar solo dentro de permisos y presupuesto; nueva inversión requiere revisión |
| Cambia la carga y deja de servir la evidencia de costo | Conservar la evaluación anterior, revisar aplicabilidad y estimar el nuevo escenario antes del compromiso dependiente |

Estos ejemplos prueban consistencia conceptual; no aportan evidencia sobre proyectos reales.

## Aplicación documental después de aprobar el diseño

| Fuente editable | Cambio previsto |
|---|---|
| Registro de decisiones | Registrar autoridad y alcance de la adopción; precisar qué partes de los diseños previos modifica |
| Blends · recorrido de idea a proyecto | Sustituir explícitamente el criterio del gate y ajustar el paso 3: vía de validación propuesta en lugar de hipótesis de MVP obligatoria |
| Blends · estándar heredado `vc/docs/standards/idea-lifecycle.md` | Conciliar mediante VCX-D011 el cambio del criterio «todas respondidas», bajo el gobierno vigente de VCX-D026. Mientras no se apruebe e integre esa conciliación, conserva vigencia el gate actual; este trabajo no escribe en el precursor |
| Blends · ingreso de ideas | Referenciar preguntas categorizadas y propuesta de validación, preservando el consejo y la confirmación humana |
| Cellar · modelo de iniciativa | Representar preguntas, evidencia, decisión y modalidad por referencias; definición sin MVP obligatorio |
| Cellar · plantillas de idea e iniciativa | Incorporar campos proporcionales, señales y siguiente paso sin otra política editable |
| Diseño previo del primer recorrido y arquitectura/FinOps | Identificar los apartados revisados y ajustar referencias que exigieran MVP o resolver todas las preguntas |

Antes de aplicar, verificar también las interfaces documentales de Brix para no imponer otro contrato de preparación. Este diseño no decide su representación técnica ni renombra comandos.

La implementación documental se considerará coherente cuando los casos anteriores puedan expresarse sin contradicción, se mantengan identidad, fuentes únicas y decisiones separadas, y ninguna plantilla obligue a MVP. Se comprobarán enlaces y procedencia; no se agregan pruebas que solo reproduzcan el texto.

Hasta esa aplicación, las fuentes enlazadas conservan su estado documental actual. Este documento es la propuesta a validar, no un segundo registro activo de ideas ni una autorización de migración.

## Contraste de la revisión recibida

Revisión de Claude trasladada por el usuario el 2026-10-31, con veredicto «aprobar con ajustes». Se incorporan la declaración del cambio de gate, clasificación trazable, vigencia y motivos del semáforo, umbral de implementación directa, referencia económica a FinOps y casos de evidencia contradictoria.

Dos ajustes a las correcciones propuestas: necesitar código no demuestra necesidad de graduar, pues puede existir un prototipo exploratorio; exigir evidencia exclusivamente externa excluiría mediciones propias reproducibles. La frontera propuesta exige demostrar dependencia del compromiso concreto, y la evidencia exige verificabilidad y pertinencia. Estas son propuestas del asistente para revisión, no nuevos acuerdos atribuidos al usuario.
