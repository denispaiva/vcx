Salida cruda de una ejecución de control (skill original) sobre un caso ficticio.

# Supuestos de riesgo: asistente conversacional de turnos para peluquerías

Producto evaluado: asistente conversacional que gestiona turnos de peluquerías pequeñas y reduce las ausencias sin aviso (alternativa: recordatorio por SMS). Tope declarado: 40 horas del autor, presupuesto 0.

## 1. Tres perspectivas sobre por qué podría fracasar

**Product Manager**
- El problema puede ser menor al percibido: las dos fuentes de ausencias se contradicen (más de 20 % según la encuesta propia, 8 % según el informe sectorial).
- Una peluquería pequeña puede no pagar por reducir ausencias si el costo por turno perdido es bajo o si ya tiene lista de espera.
- El competidor real es el mensaje manual por WhatsApp, gratuito, y las agendas existentes con recordatorios incluidos.

**Designer**
- Los dueños de peluquerías pequeñas trabajan con las manos ocupadas; un asistente que exige configuración o supervisión puede no usarse.
- Los clientes finales pueden ignorar o desconfiar de un asistente conversacional que reprograma turnos solo.
- Primera experiencia: cargar agenda, horarios y servicios puede ser una barrera mayor que el beneficio.

**Engineer**
- Reprogramar turnos solo exige leer y escribir la agenda real (a menudo papel, cuaderno o WhatsApp), sin API.
- Un asistente conversacional puede equivocarse (doble turno, turno en horario cerrado) con costo directo para el local.
- Construir buy vs. build: un recordatorio por SMS se resuelve con servicios existentes; el asistente agrega complejidad sin evidencia de que se necesite.

## 2. Supuestos por categoría

Confianza: Alta / Media / Baja (según la evidencia ficticia del caso). Prioridad de prueba: A (probar primero) a C.

### Value

| # | Supuesto | Confianza | Prueba sugerida | Prioridad |
|---|---|---|---|---|
| V1 | Las ausencias sin aviso son un problema grave para peluquerías pequeñas (tasa real entre 8 % y más de 20 %). | Baja: fuentes contradictorias; la encuesta tiene sesgo de autoselección y el informe no se leyó completo. | Leer la metodología del informe; pedir a 5 a 8 locales el conteo real de ausencias de las últimas 4 semanas (agenda, no memoria). | A |
| V2 | Una ausencia cuesta lo bastante como para que el dueño pague por evitarla. | Baja: no hay datos de ingreso perdido por turno. | Preguntar a 5 locales cuánto vale el turno promedio y qué hacen hoy con el hueco; calcular pérdida mensual. | A |
| V3 | Los recordatorios reducen ausencias de forma medible. | Media-baja: las dos peluqueras dicen que «ayudó», sin números. | Con esas dos peluqueras, medir 4 semanas con y sin recordatorio (ausencias / turnos). | A |
| V4 | Un asistente conversacional que reprograma recupera ingresos más que un recordatorio simple. | Baja: es suposición del autor sin evidencia. | Comparar en el mismo piloto: recordatorio simple versus recordatorio con opción de responder «reprogramar»; medir huecos rellenados. | A |
| V5 | Los locales seguirán usándolo pasadas las primeras semanas. | Baja | Revisar uso a las semanas 2 y 4 del piloto. | B |

### Usability

| # | Supuesto | Confianza | Prueba sugerida | Prioridad |
|---|---|---|---|---|
| U1 | Un dueño puede cargar su agenda y empezar en pocos minutos. | Baja | Observar a 3 dueños haciendo la configuración inicial sin ayuda, con cronómetro. | B |
| U2 | Los clientes finales responden a un asistente por mensaje y lo entienden. | Media-baja | Enviar mensajes de prueba a clientes de las dos peluqueras y medir tasa de respuesta. | B |
| U3 | La reprogramación autónoma no genera confusión (turnos duplicados, cambios no esperados). | Baja | Prueba de escritorio con 10 escenarios de reprogramación contra una agenda simulada. | B |

### Viability

| # | Supuesto | Confianza | Prueba sugerida | Prioridad |
|---|---|---|---|---|
| Vi1 | Hay disposición a pagar y un precio que cubra costos (mensajería, alojamiento, soporte). | Baja: no se preguntó. | Preguntar a 8 a 10 locales precio máximo aceptable; pedir un compromiso de pago simbólico antes de construir. | A |
| Vi2 | El costo operativo (SMS o mensajería, modelo de lenguaje, soporte) queda por debajo del ingreso por local. | Baja: presupuesto declarado 0, costos recurrentes sin estimar. | Estimar costo por local y por mes con precios publicados de mensajería. | A |
| Vi3 | Se puede dar soporte a locales pequeños con las horas del autor. | Baja | Registrar horas de soporte durante el piloto. | B |
| Vi4 | El uso de datos personales de clientes (nombre, teléfono) cumple la normativa de datos y de mensajería aplicable. | Media-baja | Revisar la normativa local de datos personales y consentimiento para mensajes comerciales. | B |

### Feasibility

| # | Supuesto | Confianza | Prueba sugerida | Prioridad |
|---|---|---|---|---|
| F1 | Se puede integrar con la forma en que los locales llevan hoy su agenda (papel, cuaderno, WhatsApp, agendas varias). | Baja | Relevar qué agenda usa cada uno de 8 a 10 locales. | A |
| F2 | Un piloto funcional cabe en 40 horas del autor con presupuesto 0. | Media-baja | Estimar horas por componente (envío, respuesta, agenda); si el asistente solo no cabe, el recordatorio simple sí. | A |
| F3 | El asistente interpreta respuestas libres con precisión suficiente. | Baja | Lista de 30 respuestas reales o simuladas y tasa de interpretación correcta. | B |
| F4 | Servicios gratuitos alcanzan para el piloto (mensajería sin costo por mensaje). | Baja | Revisar límites y condiciones de los canales gratuitos. | B |

### Ethics

| # | Supuesto | Confianza | Prueba sugerida | Prioridad |
|---|---|---|---|---|
| E1 | Enviar mensajes a clientes finales en nombre del local es aceptable para ellos. | Media | Incluir consentimiento y opción de baja; consultar a algunos clientes. | C |
| E2 | Un asistente que reprograma solo no perjudica a clientes (cambios sin su acuerdo). | Media-baja | Exigir confirmación del cliente antes de cualquier cambio; revisar casos de error en la prueba de escritorio. | B |
| E3 | Tratar los datos de contacto de clientes del local es seguro y proporcionado. | Media-baja | Limitar a nombre, teléfono y turno; definir retención y borrado. | C |

### Go-to-Market

| # | Supuesto | Confianza | Prueba sugerida | Prioridad |
|---|---|---|---|---|
| G1 | Existe un canal alcanzable: el grupo de mensajería del rubro basta para llegar a clientes de pago. | Media-baja: sirvió para la encuesta, no se probó para vender. | Ofrecer el piloto en el grupo y contar cuántos aceptan sin insistencia. | A |
| G2 | El mensaje «menos ausencias» convence más que «asistente conversacional». | Baja | Probar dos textos de oferta y comparar respuesta. | B |
| G3 | Los locales confían en una herramienta de un desconocido. | Baja | Medir cuántos aceptan el piloto gratis y cuántos lo mantienen después. | B |
| G4 | Es buen momento (los locales sienten el problema hoy). | Baja | Preguntar cuándo fue la última ausencia y qué hicieron. | C |

### Strategy & Objectives

| # | Supuesto | Confianza | Prueba sugerida | Prioridad |
|---|---|---|---|---|
| S1 | Las ausencias son el problema más valioso a resolver en estos locales (frente a captación de clientes, cobros, etc.). | Baja | Preguntar a 8 locales su principal dolor y ordenarlo. | A |
| S2 | La ventaja no es copiable: agendas con recordatorios y bots de mensajería ya existen. | Baja | Listar 5 a 10 alternativas existentes y qué hacen en recordatorios y reprogramación. | B |
| S3 | Un recordatorio simple no basta; justifica el paso a asistente. | Baja: es el punto central de la decisión. | Resultado del piloto comparado (V3 y V4). | A |
| S4 | Las 40 horas son el tope adecuado para aprender lo necesario. | Media | Fijar un hito a las 15 horas: continuar solo si V1 a V3 se confirman. | B |

### Team

| # | Supuesto | Confianza | Prueba sugerida | Prioridad |
|---|---|---|---|---|
| T1 | Un solo autor tiene las habilidades (conversación, integración, ventas, soporte). | Media-baja | Listar tareas del piloto y marcar las que no domina. | B |
| T2 | El autor mantendrá el tiempo y la motivación más allá de las 40 horas. | Media | Definir criterio de parada al llegar al tope. | C |
| T3 | Hay herramientas gratuitas suficientes para un piloto. | Media-baja | Ver F4; confirmar con un prototipo mínimo. | C |

## 3. Supuestos más riesgosos (prueba primero)

1. V1/V2: tamaño real del problema (8 % versus más de 20 %) y valor económico de cada ausencia.
2. V3/V4/S3: si el recordatorio simple ya logra el efecto, el asistente conversacional no se justifica.
3. Vi1/Vi2: disposición a pagar y costo recurrente frente a presupuesto 0.
4. F1/F2: integración con agendas reales y alcance dentro de 40 horas.
5. G1/S1: canal alcanzable y que este sea el dolor principal del rubro.

## 4. Secuencia sugerida

1. Con pocas horas: leer la metodología del informe y recolectar conteos reales de ausencias de 5 a 8 locales.
2. Medir con las dos peluqueras un recordatorio simple con números (con y sin recordatorio).
3. Preguntar precio y disposición a pagar.
4. Solo si lo anterior confirma un problema de tamaño suficiente y el recordatorio simple deja un hueco medible, probar la reprogramación conversacional en una escala mínima.

Nota: todo el contenido deriva del caso ficticio; las confianzas son juicios sobre la evidencia descrita en él.
