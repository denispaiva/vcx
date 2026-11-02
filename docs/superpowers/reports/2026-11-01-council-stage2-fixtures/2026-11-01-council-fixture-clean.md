---
document_revision: 18a243fafaf1
run_hash: fc0db1d2c971
status: partial
bindings_requested: "advisor-contrarian=claude/balanced/subagent;advisor-first-principles=claude/economy/subagent;advisor-expansionist=claude/economy/subagent;advisor-outsider=claude/economy/subagent;advisor-executor=claude/economy/subagent;reviewer-1=claude/balanced/subagent;reviewer-2=claude/balanced/subagent;reviewer-3=claude/balanced/subagent;reviewer-4=claude/balanced/subagent;reviewer-5=claude/balanced/subagent;synthesis=claude/frontier/subagent"
bindings_observed: "advisor-contrarian=claude-sonnet-5-5;advisor-first-principles=claude-haiku-5-5;advisor-expansionist=claude-haiku-5-5;advisor-outsider=cancelled;advisor-executor=claude-haiku-5-5;reviewer-1..5=not_launched;synthesis=not_launched"
invocations: 5
decorrelated: false
cost: "tokens observados: salida 36053, entrada 542015 (incluye caché); el asiento cancelado no registró uso; dinero not_measured"
new_material: null
---
Insumo de asesoramiento. No es evidencia y no autoriza nada.

# Consejo parcial sobre el fixture limpio (corrida 3 de la etapa 2, fallo inducido)

Corrida sintética de prueba de `brix-llm-council`, 2026-11-01. Documento: [`fixture-clean.md`](fixture-clean.md), revisión `18a243fafaf1`. Propósito: inducir un fallo de asiento por cancelación explícita y comprobar el comportamiento de la skill ante un parcial. No asesora sobre ningún producto real.

## Pregunta y entrada

- Pregunta: «¿Qué dato falta en la propuesta para decidir si la caché reduce o aumenta el costo total para el usuario?»
- Referencias autorizadas: ninguna además del documento, incluido en cada consigna.
- Destino autorizado: esta carpeta.

## Recursos declarados

Tope 11 asientos sin reintentos; concurrencia 5; espera por fase 600 s; 400 palabras por asesor. Consumidos: 5 invocaciones (cuatro asesores completos y uno cancelado).

## Fallo

- Asiento fallido: `advisor-outsider` (Forastero). Cancelado por el orquestador con la herramienta de detención del host a los pocos segundos del lanzamiento (registro: 2026-11-02T00:23:28Z cancelación solicitada del asiento advisor-outsider de la corrida 3). El host reportó estado «killed».
- Transcripción del asiento cancelado: cero mensajes del asistente, cero herramientas, cero tokens de salida, `finished` sin valor. No continuó tras la cancelación.
- No se reintentó el asiento. No se lanzaron revisores ni síntesis.
- Trabajo completado: cuatro respuestas de asesor, conservadas abajo.
- Consumo declarado perdido: las cinco invocaciones de esta corrida. Esta versión no reanuda; una corrida completa posterior sobre la misma entrada no queda bloqueada por este parcial y debe referenciarlo en sus antecedentes.

## Configuración usada

| Asiento | Solicitado | Observado | Herramientas | Tokens salida | Tokens entrada | Nombres en consigna | Orden | Mensajes | finished |
|---|---|---|---|---|---|---|---|---|---|
| C3 Asesor Contrarian | sonnet | `claude-sonnet-5-5` | ninguna | 8757 | 180693 | n/a |  | 3 | True |
| C3 Asesor Ejecutor | haiku | `claude-haiku-5-5` | ninguna | 10408 | 120424 | n/a |  | 2 | True |
| C3 Asesor Expansionista | haiku | `claude-haiku-5-5` | ninguna | 8846 | 120432 | n/a |  | 2 | True |
| C3 Asesor Forastero | haiku | `—` | ninguna | 0 | 0 | n/a |  | 0 | None |
| C3 Asesor Primeros Principios | haiku | `claude-haiku-5-5` | ninguna | 8042 | 120466 | n/a |  | 2 | True |

## Lecturas declaradas por asiento

Los cuatro asientos completos declararon «este mensaje y nada más»; transcripciones con cero herramientas.

## Mapeo de anonimización

Omitido: un reporte parcial no incluye el mapeo.

## Encuadre

El documento es una propuesta ficticia y sintética, creada para probar la skill; no describe ningún producto real. Propone una caché local de 24 horas para un CLI de ejemplo que consulta un servicio remoto, indexada por los parámetros de la consulta, con una opción para forzar la consulta remota. Declara tres restricciones y dos supuestos. Estado: borrador.

## Síntesis

No realizada: corrida parcial.

## Respuestas completas


### Contrarian (467 palabras)

Soy el asiento Contrarian y respondo desde el documento y el encuadre.

**Punto más fuerte: falta la frecuencia de repetición de consultas idénticas, y con ella la tasa de aciertos esperada.** El problema habla de "consultas repetidas con los mismos parámetros" (2 a 4 segundos y cuota). Pero el documento no dice qué fracción de las ejecuciones son repeticiones dentro de 24 horas. Sin ese dato, el beneficio (segundos y cuota ahorrados) es una cota superior sin multiplicador. Con tasa de aciertos cercana a cero, la caché solo agrega costo: escritura, lectura y mantenimiento del archivo.

**Datos complementarios que faltan para el "costo total":**
- No define qué es costo total. Hay tiempo (2 a 4 s), cuota (sin precio ni límite) y corrección. Solo los dos primeros aparecen como beneficio, y el tercero no figura como costo.
- Falta el costo de una respuesta obsoleta para el usuario. Un acierto tarda menos, pero si el dato cambió en el servicio, el usuario decide con información vieja o repite la consulta con `--no-cache`.

**Contradicciones y huecos entre problema y solución:**
1. El problema es la repetición de consultas, pero la solución fija 24 horas sin justificarlas con ningún dato. El plazo es un supuesto, no una medición.
2. El supuesto 1 ("los parámetros identifican por completo la respuesta") puede ser falso si la respuesta del servicio varía con el tiempo o el estado. En ese caso la clave de caché es incorrecta por construcción.
3. El supuesto 2 afirma que 24 horas sirve "para todos los usuarios" sin evidencia, y la propuesta no ofrece ajustar el plazo.
4. "Las respuestas con errores no se guardan" no define error. Una respuesta vacía, parcial o degradada pero exitosa se guardaría y se serviría durante 24 horas.
5. No dice si `--no-cache` refresca la entrada guardada. Si no lo hace, el usuario paga la consulta remota y sigue recibiendo el dato viejo en la siguiente ejecución.

**Casos en que la caché aumenta el costo:**
- Baja repetición: todas las consultas se escriben y casi ninguna se reutiliza.
- Respuestas que cambian dentro de las 24 horas: el usuario paga la lectura de caché, luego `--no-cache`, luego la consulta remota. Además paga su propio tiempo para notar el problema y aprender el flag.
- El archivo vive en el directorio del usuario, pero la propuesta no fija tamaño máximo ni política de limpieza. El costo en disco crece sin tope declarado.
- No dice cómo se comporta ante escrituras concurrentes ni ante un archivo corrupto. Una falla ahí forzaría una consulta remota más el costo de diagnóstico.

**Para decidir hacen falta, como mínimo:** la tasa de repetición medida, la frecuencia de cambio de las respuestas del servicio y el costo en cuota por consulta.

## Lecturas
Este mensaje y nada más.


### Primeros Principios (383 palabras)

**Asiento Primeros Principios: costo total para el usuario**

El documento no mide ningún término de la ecuación de costo. Sólo afirma que las consultas repetidas tardan 2 a 4 segundos y «consumen cuota del servicio». Sin la frecuencia de repetición no se puede cuantificar el ahorro, y sin el costo de cada consulta remota no se puede valorar la cuota. El dato ausente que decide el signo del efecto es la **tasa de aciertos esperada**: qué proporción de las consultas reales de cada usuario coincide con una consulta previa dentro de 24 horas.

**Componentes del costo total para el usuario, y estado en el documento**

1. Cuota o dinero del servicio: el documento dice que se consume cuota, pero no cuánto, ni si hay precio, ni si el límite es individual o compartido. No medido.
2. Tiempo: 2 a 4 segundos por consulta repetida. Es lo único cuantificado, y sólo para el caso de repetición. Parcialmente medido.
3. Costo que la caché agrega: overhead en cada fallo (clave, lectura, escritura), almacenamiento en el directorio del usuario sin política de purga declarada, y el código propio que exige la restricción de no agregar dependencias (caducidad, escritura concurrente, archivos corruptos). No medido.
4. Costo de datos incorrectos: respuestas de hasta 24 horas de antigüedad. Si el supuesto «los parámetros identifican por completo la respuesta» es falso, la caché sirve respuestas erróneas sin aviso. No medido ni discutido.
5. Costo trasladado al usuario: quien necesita datos frescos debe conocer `--no-cache`. El documento no dice si esa carga es aceptable ni cuántos la necesitarán. No medido.

**Cómo se decide**

Ahorro ≈ aciertos × (costo de la consulta remota + valor del tiempo ahorrado). Costo ≈ fallos × overhead + almacenamiento + mantenimiento + costo de datos desactualizados. Con tasa baja, el overhead y el mantenimiento pueden superar el beneficio. Con tasa alta, el término decisivo pasa a ser el riesgo de datos viejos o erróneos. El precio unitario de la consulta remota es el segundo dato necesario: sin él, la cuota no se convierte en costo.

Estas relaciones son un razonamiento sobre la estructura del costo, no cifras del documento. No se asignaron valores numéricos.

**Lecturas**

Este mensaje y nada más: el encuadre, el documento fixture-clean.md (revisión 18a243fafaf1) y la consigna. No usé herramientas ni leí archivos.


### Expansionista (344 palabras)

**Punto más fuerte.** La mayor oportunidad no declarada es revalidar las entradas vencidas en lugar de descartarlas. La propuesta trata la caché como binaria: dentro de 24 h sirve, y después se descarta y se vuelve a consultar. Si el servicio ofreciera validadores (ETag o Last-Modified) y cobrara menos cuota por una respuesta "sin cambios", el ahorro alcanzaría también a las consultas repetidas después de 24 h. El documento no dice si existen esos validadores ni cómo se cobra la cuota, así que no puedo afirmar que la oportunidad sea real.

**Dato que falta para decidir el signo del costo.** La propuesta no define en qué unidad se mide el costo del usuario. Declara tiempo (2 a 4 s) y "cuota del servicio", pero no dice si el usuario paga en tiempo, cuota, dinero o espacio en disco. Sin esa unidad no hay balance. Con ella, faltan tres datos medibles:

1. Tasa de aciertos: fracción de consultas que el mismo usuario repite con los mismos parámetros dentro de 24 h. Si es baja, el costo fijo de mantener la caché (disco, complejidad, invalidación) puede superar el ahorro.
2. Costo unitario de una consulta remota en cuota o dinero, y si es el mismo para una respuesta idéntica que para una nueva.
3. Fracción de consultas repetidas después de 24 h. Mide cuánto deja sin ahorro la propuesta actual frente a una revalidación.

**Riesgos que suben el costo y no están cubiertos.** No hay límite de tamaño ni política de expulsión para el archivo local. Las respuestas con error no se guardan, así que esas consultas siguen llegando al servicio; si este cobra por intentos fallidos, consumen cuota.

**Supuesto a verificar.** "Los parámetros identifican por completo la respuesta." Si no es cierto, la caché devuelve respuestas incorrectas y el costo pasa al usuario en forma de errores, no de ahorro.

**Balance.** La caché reduce el costo total si tasa de aciertos × costo por consulta supera el costo de mantenerla. El documento no contiene ninguno de los tres valores.

**Lecturas:** este mensaje y nada más.


### Ejecutor (448 palabras)

**Punto más fuerte.** La propuesta no tiene ninguno de los dos datos que fijan el signo del cambio de costo: la tasa de consultas repetidas dentro de 24 h (h) y el precio o umbral de cuota por consulta. Sin ellos no se puede afirmar si la caché reduce o aumenta el costo total.

**Modelo mínimo.** Con N consultas por período, c_r costo remoto por consulta, c_l costo local por consulta (lectura, escritura, serialización), F costos fijos (espacio, limpieza, mantenimiento, desarrollo amortizado) y D costo de decidir con datos de hasta 24 h de antigüedad:

Ahorro = h·N·c_r − N·c_l − F − D

La caché conviene solo si h > (c_l + (F + D)/N) / c_r. Si el servicio no cobra por consulta y no hay riesgo de superar la cuota, c_r ≈ 0 y la caché solo suma costos monetarios. Si el costo incluye el tiempo del usuario, el término que falta es el de los 2 a 4 s de espera multiplicado por las veces que ocurre.

**Datos faltantes, por prioridad.**

1. **h.** Distribución de consultas idénticas por usuario en ventanas de 24 h. Es obtenible registrando en el CLI, durante algunas semanas, solo un hash de los parámetros y la marca temporal, sin guardar respuestas. Si el servicio tiene logs de uso, sirven como fuente.
2. **c_r y umbral de cuota.** Precio por consulta o plan contratado, y consumo real frente al límite. Es obtenible del contrato, de la factura o del panel de cuota del proveedor.
3. **Latencia real.** El rango de 2 a 4 s no declara cómo se midió. Hay que medir p50 y p95 en el propio CLI.
4. **Validez de la clave.** Si la respuesta depende de tiempo, cuenta, idioma o versión del servicio, indexar solo por parámetros devuelve respuestas erróneas, y ese costo no está en el modelo. Es obtenible comparando respuestas a consultas idénticas en momentos separados y revisando el esquema de respuesta en busca de campos temporales o de identidad.
5. **c_l y F.** Tamaño por entrada, cantidad de entradas, tiempo de escritura y de limpieza. Se mide con un benchmark sobre parámetros reales.
6. **D.** Tolerancia a datos de hasta 24 h. Esto no se mide con datos técnicos. Lo decide el dueño del producto. Solo puede acotarse con la tasa de cambio de respuestas que resulte del punto 4.

**Observación.** El supuesto «24 horas es aceptable para todos los usuarios» es el que puede volver D grande. El documento no define quiénes son «todos» ni cómo se verificaría esa aceptación.

**Lecturas**
- Este mensaje, que incluye el encuadre y el documento fixture-clean.md (revisión 18a243fafaf1). No leí archivos, ni ejecuté comandos, ni busqué nada.


### Forastero

Sin respuesta: asiento cancelado.

## Revisiones cruzadas

No realizadas: corrida parcial.

## Límites

- Reporte parcial por diseño de la prueba; no tiene valor asesor.
- Límites de palabras superados: Contrarian y Ejecutor sobre 400.
- La cancelación llegó antes de la primera respuesta del modelo, así que no prueba el caso de un asiento cancelado a mitad de respuesta.
