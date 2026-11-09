# Interoperabilidad de VCX

Estado: reparto de interfaces propuesto. Este documento es la fuente editable de esa propuesta; todavía no define esquemas ejecutables ni una nueva API implementada.

## Propiedad de contratos

| Contrato | Dueño propuesto | Consumidores | Frontera |
|---|---|---|---|
| Identidad, estructura y operaciones de portfolio | Cellar · producto | Blends y consumidores autorizados | No define la implementación interna de capacidades |
| Operaciones de conducción de proyecto | Cellar · producto | PO, equipos de proyecto e integraciones autorizadas | Aplica el método publicado por Blends sin redefinirlo; fila derivada de VCX-D029, contenido pendiente de diseño |
| Invocación de capacidades, resultados, errores y permisos | Brix | Blends, proyectos y consumidores independientes | No exige Blends ni un Cellar implícito |
| Operaciones de orquestación y gobierno | Blends | Interfaces, agentes e integraciones | Consume las interfaces públicas de las otras piezas |
| Convenciones comunes de referencias e intercambio | Fuente compartida, con responsable designado por contrato | Las piezas que adopten la convención | No copia esquemas de dominio ni importa implementaciones internas |
| Declaraciones de compatibilidad | Cada producto mantiene sus restricciones; una matriz conjunta se deriva de ellas | Consumidores y verificadores | No obliga a compartir versión o calendario de lanzamiento |

Cada pieza mantiene su interfaz pública. Los acuerdos comunes tienen una sola fuente y responsable; concentrar todos los contratos en Cellar lo haría dependiente de cambios ajenos a su misión.

Las [interfaces de comandos de Brix](https://github.com/denispaiva/brix/blob/main/docs/commands.md) definen los instrumentos `idea` y `council` y sus equivalentes de conversación, con una sola lógica de entrada y ayuda. Blends consume esas capacidades y coordina las decisiones del proceso; la ubicación del consejo existente en Blends se conserva hasta una adaptación explícita.

La ubicación y distribución de la fuente compartida siguen pendientes. **Trasiego** es un candidato para nombrarla y ya identifica una iniciativa existente. Consultar [nombres](../naming.md) y [decisiones](../decisions/README.md) antes de adoptar un nombre o crear otra pieza.

## Información que deberá fijar cada interfaz

- Propósito, dueño, consumidores y versión pública.
- Entradas, resultados y errores, con referencias estables.
- Efectos, permisos y autoridad requerida para leer o modificar estado.
- Procedencia de la evidencia y límites de lo que el resultado permite concluir.
- Compatibilidad, deprecación y actualización de consumidores.

La interfaz declara permisos; la implementación debe verificarlos al ejecutar. Una recomendación de Brix no equivale a una decisión de la autoridad humana competente, responsable del portfolio o PO según el tramo; conservar una aprobación en Cellar no crea esa aprobación.

## Ejemplo conceptual: graduación de una idea

El [diseño del primer recorrido](../superpowers/specs/2026-10-30-cellar-blends-first-journey-design.md) detalla este caso, con un modelo de datos de Cellar y un proceso de Blends propuestos, sin una API ejecutable nueva.

Blends coordina el tramo de idea según el método adoptado. Brix ejecuta las evaluaciones necesarias. El responsable del portfolio toma la decisión conforme a las reglas vigentes y asigna el PO del proyecto. Cellar conserva la decisión, las referencias y la evidencia, manteniendo identidad e historia de la iniciativa, y desde la graduación conduce el proyecto con su PO; el traspaso concreto sigue pendiente de diseño, según la [frontera](responsibility-matrix.md#1-método-y-conducción).

La transición debe dejar una única fuente activa de seguimiento; las referencias históricas continúan siendo resolubles. Este ejemplo explica responsabilidades, no autoriza una operación sobre el portfolio actual.


## Distribución de principios a instancias externas

Estado de esta sección: disparador acordado mediante VCX-D023; el mecanismo continúa sin elegir. No cambia el estado propuesto de los contratos anteriores.

Antes de activar la primera instancia de Cellar en otro repositorio, su responsable debe resolver y registrar cómo recibirá los principios compartidos. La decisión debe identificar la fuente canónica y revisión o versión adoptada, el mecanismo de entrega accesible desde el repositorio consumidor, quién actualiza y aprueba cambios y cómo se verifica la carga e integridad del contenido. Debe explicitar también qué ocurre si la fuente no está disponible, sin omitir reglas silenciosamente.

Una referencia local a un archivo fuera del repositorio no demuestra distribución ni disponibilidad. No mantener dos fuentes normativas editables; si se elige una copia distribuida, debe quedar identificada como derivada de una revisión concreta. El mecanismo puede ser simple y debe responder a la necesidad de esa primera instancia, sin construir ahora una plataforma de distribución.

El asunto se vincula con VCX-D008 en el [registro](../decisions/README.md), sin exigir que se resuelva el nombre Trasiego para adoptar un mecanismo. VCX-D009 sigue pendiente: este disparador no crea ni selecciona una instancia.


## Preparación de productos independientes

Estado: requisitos previos acordados mediante VCX-D025; mecanismos de entrega e implementación pendientes. Se aplican antes de declarar un producto independiente o cambiar su copia canónica, aunque se aloje habitualmente bajo `vcx/`. VCX-D026 permite preparar primero un clon de transferencia de Blends y resolver en su rama las instrucciones y documentos, antes de aceptarlo como producto independiente.

- Resolver la ubicación canónica y distribución de los contratos que posee cada producto. Su documentación y contratos propios pertenecen al repositorio del producto; la raíz conserva acuerdos entre productos y convenciones compartidas, sin una segunda definición editable de esos contratos. Este reparto no ratifica por sí solo los detalles de contratos todavía propuestos.
- Declarar la versión y fuente de los principios adoptados. Una copia distribuida es válida si identifica su origen, versión o revisión verificable y carácter derivado; sus actualizaciones deben ser explícitas y no crear otra fuente normativa independiente. Si se elige una fuente publicada, comprobar acceso y comportamiento ante indisponibilidad. La mera versión en una ruta inaccesible no resuelve la distribución.
- Eliminar dependencias documentales de trabajo sobre la carpeta padre o productos hermanos. Usar recursos propios o referencias públicas o distribuidas accesibles desde el consumidor. Conservar antecedentes históricos identificados sin convertirlos en requisitos de uso.
- Revisar los archivos de instrucciones heredados, incluidos `CLAUDE.md`, imports y ajustes específicos del IDE. Comprobar en la versión y configuración utilizadas qué instrucciones se cargan; no presumir herencia de AGENTS.md por la disposición local de carpetas. En Blends, la fusión del AGENTS heredado debe incorporar el recurso local de principios adoptados a la cadena de instrucciones que carga su CLAUDE.md; verificarlo antes de la integración y del cambio de copia canónica.
- Ensayar la lectura y las verificaciones del producto en una ubicación aislada, sin VCX como padre ni el precursor disponible como dependencia implícita. Registrar fallos y límites antes de declarar portabilidad.

VCX-D008 continúa abierto para convenciones compartidas; resolver el mecanismo requerido no depende de adoptar el nombre Trasiego. El disparador previo para instancias externas se conserva y se complementa con este requisito para productos.
