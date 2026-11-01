Salida cruda de una ejecución de prueba de la skill `killer-questions` sobre un caso ficticio (caso C); no es un análisis de una idea real.

# Preguntas asesinas: asistente de turnos para peluquerías (caso ficticio C)

Estado de todo lo que sigue: propuesta. Confirmar cuáles preguntas son decisivas corresponde al humano.

## Aclaraciones pendientes (ejecución no interactiva)

1. Canal del piloto: no se indica si sería SMS, mensajería u otro. Afecta el costo con tope de 0 de presupuesto. Las preguntas 3 y 4 dependen de esto: **condicionales**.
2. Qué significa «piloto de bajo costo» dentro del tope de 40 horas y 0 de presupuesto (si incluye tarifas de mensajes o de modelo de lenguaje). Condiciona la pregunta 4.
3. Definición de «ausencia sin aviso» en la encuesta y en el informe sectorial (¿incluye cancelaciones tardías?). Condiciona la comparabilidad de las dos cifras (pregunta 1).
4. Valor de un turno recuperado y si la peluquería puede reocupar el hueco. Sin esto no se puede dimensionar el beneficio. Condiciona la pregunta 1.

## Material separado

**Hechos citados (con límites)**
- Encuesta propia, n=40, respondida en un grupo de mensajería del rubro donde el autor es miembro: 60 % de los encuestados dice que más de 1 de cada 5 turnos se pierde por ausencia. Datos crudos guardados. Límite: muestra autoseleccionada y declarativa; no es representativa de las peluquerías en general.

**Afirmaciones del autor sin fuente verificada**
- Informe «Observatorio del Servicio Personal 2025» (muestra de 300 locales): ausencias del 8 % de los turnos. El autor leyó solo el resumen, no la metodología.
- Dos peluqueras conocidas probaron un mes de recordatorios manuales y dicen que «ayudó», sin números.
- Un asistente conversacional permitiría reprogramar turnos solo y recuperar ingresos.

**Inferencias propias (propuesta)**
- Las dos cifras de ausencia (más de 20 % en el grupo encuestado, 8 % en el informe) no son contradictorias per se: miden poblaciones y definiciones distintas, y la primera es una percepción declarada. No sirven para estimar la tasa real de un local concreto.
- El beneficio de los recordatorios y el beneficio de la conversación son hipótesis separadas; la evidencia, aun anecdótica, solo toca a la primera.

**Datos ausentes**
- Tasa medida de ausencias en turnos reales, con registros.
- Efecto medido de un recordatorio sobre las ausencias.
- Proporción de clientes que reprograman en vez de simplemente no presentarse, y su disposición a hacerlo por conversación.
- Costo del canal y del asistente frente al tope de 0 de presupuesto.
- Si el hueco liberado se llena.

## Decisión en juego

Continuar la exploración con un piloto de bajo costo, o simplificar a un recordatorio por SMS. Tope declarado: 40 horas del autor, 0 de presupuesto. (Hay un tercer desenlace implícito: abandonar o diferir si el problema no es lo bastante grande.)

## Fichas de preguntas decisivas

### 1. ¿Las ausencias sin aviso son lo bastante frecuentes en los locales objetivo como para justificar cualquier solución?

- **Supuesto:** la tasa de ausencias es alta (más de 20 %) en peluquerías pequeñas.
- **Pregunta refutable:** ¿en los registros reales de turnos de una muestra de locales pequeños, la proporción de ausencias sin aviso supera un nivel que justifique actuar?
- **Decisión afectada:** continuar (piloto o SMS) frente a diferir o abandonar.
- **Consecuencia de refutación:** si la tasa real es baja, diferir o abandonar ambas opciones; el problema no paga ni el recordatorio.
- **Evidencia disponible:** encuesta propia (n=40, autoseleccionada, declarativa) que dice más de 20 %; informe citado (sin metodología revisada) que dice 8 %. Las dos difieren más de dos veces y ninguna es una medición sobre turnos.
- **Evidencia faltante y prueba proporcionada:** conteo real de turnos y ausencias de un periodo reciente en pocos locales, pidiendo la agenda o el cuaderno de turnos a las peluqueras ya conocidas. Además, leer la metodología del informe sectorial si está accesible. Costo orientativo: pocas horas dentro del tope.
- **Criterio observable (propuesto, a validar por el humano):** el umbral debe fijarse a partir del valor de un turno y del costo de la solución; sin ese dato no se propone un número. Referencia mínima: si los registros reales se parecen al 8 % del informe o menos, preguntarse si el ingreso recuperable cubre el esfuerzo.
- **Estado:** propuesta. Condicional a la aclaración 3 y 4.

### 2. ¿El recordatorio por sí solo reduce las ausencias?

- **Supuesto:** un recordatorio simple reduce las ausencias de forma apreciable.
- **Pregunta refutable:** ¿los locales que envían recordatorio tienen menos ausencias que antes o que turnos sin recordatorio?
- **Decisión afectada:** si la opción simple (SMS) vale la pena, y por tanto si hay una línea base sobre la cual medir el aporte del asistente.
- **Consecuencia de refutación:** si el recordatorio no mueve la tasa, la opción «simplificar a SMS» pierde su justificación y el problema pide otra causa o se abandona; el asistente no puede sostenerse con la hipótesis de que reprogramar es el mecanismo.
- **Evidencia disponible:** dos peluqueras dicen que «ayudó», sin números ni comparación. Es anecdótica y no distingue efecto de coincidencia.
- **Evidencia faltante y prueba proporcionada:** repetir el recordatorio manual con las mismas peluqueras llevando conteo antes y después (o alternando días con y sin recordatorio). Es la prueba más simple y sin presupuesto.
- **Criterio observable (propuesto, a validar por el humano):** diferencia en la proporción de ausencias con y sin recordatorio, fijada por el humano antes de mirar los resultados. Con muestras de dos locales la conclusión será débil; declararlo.
- **Estado:** propuesta.

### 3. ¿La conversación aporta algo sobre el recordatorio simple?

- **Supuesto:** el asistente conversacional (reprogramar solo) recupera ingresos que un recordatorio no recupera.
- **Pregunta refutable:** ¿una parte relevante de las ausencias evitables se convierte en reprogramaciones cuando el cliente puede responder y mover el turno, y esa parte no se obtiene ya con un recordatorio que permita responder «cancelo» o «cambio»?
- **Decisión afectada:** piloto del asistente frente a simplificar a recordatorio por SMS.
- **Consecuencia de refutación:** si el incremento sobre el recordatorio es marginal, simplificar a SMS (o a un recordatorio con respuesta mínima).
- **Evidencia disponible:** ninguna. Es solo una suposición del autor.
- **Evidencia faltante y prueba proporcionada:** simulación manual con las mismas peluqueras: el recordatorio incluye la invitación a responder para mover el turno; se cuenta cuántos responden, cuántos reprograman y cuántos huecos se reocupan, sin construir ningún asistente. Si la mayoría responde con una palabra, una conversación abierta no se necesita.
- **Criterio observable (propuesto, a validar por el humano):** número de turnos reprogramados y reocupados atribuibles a la respuesta, frente a los que ya habría evitado el recordatorio solo.
- **Estado:** propuesta. Condicional a la aclaración 1.

### 4. ¿Se puede hacer el piloto con 0 de presupuesto y 40 horas?

- **Supuesto:** existe un piloto del asistente viable dentro del tope declarado.
- **Pregunta refutable:** ¿hay un canal y un esquema de operación para enviar y recibir mensajes con clientes reales sin costo, y construible en el tiempo disponible?
- **Decisión afectada:** hacer el piloto frente a diferir o reducirlo a una simulación manual o a la prueba de la pregunta 3.
- **Consecuencia de refutación:** si el canal o el modelo tienen costo y el presupuesto es 0, el piloto del asistente no es ejecutable; queda la simulación manual, o se requiere una decisión humana sobre el presupuesto. Nótese que incluso el SMS suele tener costo por mensaje: no se asume gratuito.
- **Evidencia disponible:** ninguna sobre costos; solo el tope declarado.
- **Evidencia faltante y prueba proporcionada:** listar el costo real por mensaje y por interacción de cada canal candidato (consulta de tarifas, sin contratar nada) y estimar horas con un desglose.
- **Criterio observable (propuesto, a validar por el humano):** el piloto sigue solo si el costo estimado es 0 o si el humano autoriza explícitamente un presupuesto; una estimación de horas por encima de 40 lleva a reducir el alcance.
- **Estado:** propuesta. Condicional a las aclaraciones 1 y 2.

## Preguntas no decisivas para esta decisión

- **¿Pagarían las peluquerías por el servicio y cuánto?** Importa para un paso posterior, pero no cambia la decisión actual (piloto o SMS) dentro de un tope de 0 de presupuesto. Pasaría a ser decisiva si se decidiera inversión o salida al mercado.
- **¿Hay competidores o herramientas de agenda que ya lo resuelvan?** Relevante para la estrategia; no cambia la elección entre piloto y SMS en esta fase, aunque una búsqueda breve puede ahorrar horas. Si resultara que ya existe una solución gratuita, la pregunta pasaría a ser decisiva (abandonar). Sin evidencia, no se afirma.
- **Privacidad y consentimiento de los datos de clientes (teléfonos).** Importa para la ética y la legalidad, pero a escala de dos locales con permiso expreso no cambia la decisión actual; sí cambiaría el diseño al crecer. No se verificó la normativa aplicable.
- **Facilidad de uso para el personal de la peluquería.** No cambia la decisión mientras la prueba sea manual.
- **Equipo y capacidad.** El tope de 40 horas ya delimita el esfuerzo; no hay evidencia de que algo adicional cambie la decisión.

## Límites de este análisis

- No se verificó la existencia ni el contenido del informe sectorial citado; se trata como afirmación del autor.
- No se pudo evaluar la representatividad de la encuesta más allá de lo descrito (muestra autoseleccionada en un grupo donde el autor es miembro).
- No se consultaron tarifas de canales ni normativa de protección de datos (sin acceso a internet).
- Los umbrales y criterios están sin cifras propias porque la entrada no los aporta; los fija el humano.
- No se asignó prioridad ni clasificación de bloqueo a las preguntas; esa confirmación corresponde al humano.
