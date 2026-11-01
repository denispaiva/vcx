Salida cruda de una ejecución de control (skill original `identify-assumptions-new`) sobre un caso ficticio.

# Supuestos de riesgo: app de recordatorios de riego por WhatsApp para huertas comunitarias

Producto evaluado: app que envía recordatorios de riego por WhatsApp y asigna turnos a los integrantes de huertas comunitarias, con suscripción mensual por huerta. Autor: una persona con pocas horas semanales, sin presupuesto definido. Base de evidencia: charlas informales con coordinadores de 3 huertas, sin notas; una cifra (70 %) sin fuente.

## Paso 1. Tres perspectivas sobre por qué podría fallar

**Product Manager**
- El problema («se les secan plantas por olvidos») puede ser real pero de baja intensidad: un grupo de WhatsApp y una hoja impresa ya cubren la necesidad de forma gratuita.
- Huertas comunitarias son organizaciones voluntarias con poco o ningún presupuesto; la disposición a pagar una suscripción es dudosa.
- No está definido quién usa la app ni quién paga (coordinador, huertero o ambos).
- La muestra (3 huertas conocidas del autor) es pequeña y sesgada por cercanía.

**Designer**
- Si el recordatorio es un mensaje más en WhatsApp, puede perderse entre otros mensajes y silenciarse; el olvido podría no resolverse.
- Asignar turnos exige que alguien cargue y mantenga el calendario; si es engorroso, el coordinador vuelve a la hoja impresa.
- Los huerteros pueden tener edades y alfabetización digital muy distintas; el onboarding debe funcionar sin instalar nada.

**Engineer**
- La API de WhatsApp Business tiene reglas de plantillas, opt-in, costos por conversación y posibles restricciones; depender de ella es un riesgo de plataforma.
- Gestionar turnos, intercambios, ausencias y lluvia (no regar) añade lógica más allá de un simple recordatorio.
- Mantenimiento con pocas horas semanales: cualquier caída o cambio de API puede dejar el servicio roto.

## Paso 2 y 3. Supuestos por categoría, con confianza y prueba

Escala de confianza: baja / media / alta, según la evidencia aportada en el caso.

### Value

| # | Supuesto | Confianza | Prueba sugerida |
|---|----------|-----------|-----------------|
| V1 | El olvido de riego es una causa relevante de pérdida de plantas en las huertas (no el clima, la falta de manos o el diseño de turnos). | Baja (3 afirmaciones informales, sin registro) | Entrevistas estructuradas con notas a coordinadores y huerteros de más huertas; pedir ejemplos concretos de la última vez que ocurrió y qué causó el fallo. |
| V2 | El 70 % de los huerteros olvida regar al menos una vez por semana. | Muy baja (sin fuente) | Registro durante 2 a 4 semanas de turnos cumplidos y omitidos en las 3 huertas, o encuesta breve; reemplazar la cifra por un dato medido. |
| V3 | Un recordatorio resuelve el olvido (la persona regará al recibirlo). | Baja | Prueba manual (concierge): el autor envía los recordatorios por WhatsApp a mano durante unas semanas y se compara el cumplimiento con el periodo previo. |
| V4 | Los usuarios seguirán usando los recordatorios después de la novedad (retención). | Baja | Medir cumplimiento y respuesta a recordatorios entre la semana 1 y la 6 en la prueba manual. |
| V5 | El valor es mayor que el del grupo de WhatsApp y la hoja impresa actuales. | Baja | Preguntar qué falla hoy exactamente con esas herramientas; comparar con una variante mínima (mensaje programado en el grupo existente). |

### Usability

| # | Supuesto | Confianza | Prueba sugerida |
|---|----------|-----------|-----------------|
| U1 | Los coordinadores cargarán y mantendrán los turnos sin fricción. | Baja | Prueba de uso con 2 a 3 coordinadores cargando un mes de turnos con una hoja o formulario simple; medir tiempo y abandono. |
| U2 | Los huerteros aceptarán recibir mensajes individuales y sabrán responder (confirmar, intercambiar turno). | Media-baja | Prueba con mensajes manuales con opción de respuesta; observar tasa de respuesta y confusiones. |
| U3 | El onboarding por WhatsApp no requiere instalar nada y es suficiente para todas las edades. | Media-baja | Observar a 5 huerteros de perfiles distintos incorporándose; registrar dónde se traban. |
| U4 | Los recordatorios no se vivirán como molestos y no serán silenciados. | Baja | Medir silenciamientos y bajas durante la prueba; ajustar frecuencia y horario. |

### Viability

| # | Supuesto | Confianza | Prueba sugerida |
|---|----------|-----------|-----------------|
| B1 | Las huertas pagarán una suscripción mensual. | Muy baja (no hay evidencia; las huertas comunitarias suelen tener poco presupuesto) | Preguntar presupuesto y mecanismo de pago real; prueba de precio con compromiso (preventa, carta de intención, pago simbólico) en las 3 huertas. |
| B2 | Está claro quién paga (coordinador, huerta como organización, huertero individual). | Muy baja (no definido en el caso) | Mapear quién decide y cómo se financian gastos comunes en cada huerta. |
| B3 | El precio posible cubre el costo por mensaje y la operación. | Desconocida | Calcular costo unitario por mensaje y por huerta con tarifas vigentes del proveedor; comparar con la disponibilidad de pago de B1. |
| B4 | El mercado (cantidad de huertas comunitarias alcanzables) es suficiente para sostener un negocio. | Desconocida | Estimar número de huertas en el área y en el país con fuentes verificables; calcular ingreso potencial con un precio realista. |
| B5 | El autor puede dar soporte y mantenimiento con unas pocas horas semanales. | Baja | Estimar horas de soporte por huerta en la prueba manual y proyectar a 10 y 50 huertas. |
| B6 | Sin presupuesto definido, el proyecto no se detiene por costos. | Baja | Definir un tope de gasto y de tiempo y un criterio de abandono antes de construir. |

### Feasibility

| # | Supuesto | Confianza | Prueba sugerida |
|---|----------|-----------|-----------------|
| F1 | Se pueden enviar recordatorios por WhatsApp de forma automatizada a un costo y con reglas aceptables (plantillas, opt-in, ventana de 24 h). | Media-baja | Revisar la documentación y tarifas vigentes del proveedor oficial y prototipar un envío con un número de prueba (requiere consulta de fuentes actuales; no verificado aquí). |
| F2 | La lógica de turnos (rotación, intercambios, ausencias, clima) es manejable en pocas horas semanales. | Media-baja | Listar las reglas reales de turnos de las 3 huertas y estimar esfuerzo; construir el caso más simple primero. |
| F3 | La plataforma de mensajería no cambiará condiciones que inviabilicen el servicio. | Baja | Evaluar canales alternativos (SMS, Telegram, correo) y medir la dependencia de WhatsApp. |

### Ethics

| # | Supuesto | Confianza | Prueba sugerida |
|---|----------|-----------|-----------------|
| E1 | Almacenar teléfonos y datos de los huerteros es aceptable y cumple la normativa de datos personales aplicable. | Media-baja | Definir qué datos mínimos se guardan, obtener consentimiento explícito y revisar la normativa local (a verificar). |
| E2 | Presionar a voluntarios con recordatorios no genera culpa ni conflicto en la comunidad. | Media-baja | Preguntar a huerteros cómo se sentirían con avisos individuales y visibilidad de incumplimientos; evitar tableros públicos de fallos al inicio. |
| E3 | Cobrar a una comunidad voluntaria por una función básica no se percibe como inadecuado. | Baja | Sondear percepción con coordinadores; considerar si un modelo gratuito o de aporte voluntario es más coherente. |

### Go-to-Market

| # | Supuesto | Confianza | Prueba sugerida |
|---|----------|-----------|-----------------|
| G1 | Existe un canal alcanzable para llegar a otras huertas (redes de huertas, municipios, ONG). | Baja | Listar y contactar 5 a 10 redes o referentes; medir respuesta. |
| G2 | Los coordinadores adoptarán algo nuevo frente a un hábito establecido en WhatsApp. | Baja | Medir cuántos de los coordinadores contactados aceptan probar durante un mes. |
| G3 | El mensaje «no se te sequen las plantas» resuena con quien toma la decisión de compra. | Baja | Probar 2 o 3 mensajes distintos en conversaciones o una página simple y comparar interés. |
| G4 | Es el momento adecuado (no hay una ola o una alternativa que lo vuelva irrelevante). | Desconocida | Investigar alternativas existentes (apps de turnos, calendarios compartidos, herramientas de huertas). |
| G5 | La misma propuesta sirve para balcones de edificios (segmento adyacente). | Muy baja (sin ninguna evidencia; es otro usuario y otro pagador) | No priorizar hasta validar el segmento principal; si se explora, hacer entrevistas separadas con administradores y vecinos. |
| G6 | Se puede elegir un nombre de marca disponible y adecuado. | No evaluable con la información dada | Tratar como tarea posterior; verificar disponibilidad de dominio y marca cuando el segmento esté validado. |

### Strategy & Objectives

| # | Supuesto | Confianza | Prueba sugerida |
|---|----------|-----------|-----------------|
| S1 | Este es el mejor problema a resolver para las huertas (frente a otros como coordinación, insumos o gestión de cosecha). | Baja | Pedir a los coordinadores que ordenen sus 5 mayores dolores y ver dónde queda el riego. |
| S2 | La propuesta es difícil de copiar o tiene una ventaja defendible. | Baja (un recordatorio con turnos es fácil de replicar con herramientas existentes) | Probar si una hoja compartida con recordatorios programados reproduce el valor; identificar qué haría diferente al producto. |
| S3 | Los objetivos del autor están claros (¿proyecto social, negocio, aprendizaje?). | Muy baja (no se declaran) | Definir el objetivo y el criterio de éxito y abandono antes de invertir tiempo. |
| S4 | Los factores externos (plataformas, normativa de datos, estacionalidad del riego) no afectan la propuesta. | Baja | Revisar estacionalidad (uso en invierno), cambios de políticas de la plataforma y normativa aplicable. |

### Team

| # | Supuesto | Confianza | Prueba sugerida |
|---|----------|-----------|-----------------|
| T1 | Una persona con pocas horas semanales puede construir, vender y dar soporte. | Baja | Estimar horas de construcción, ventas y soporte; recortar el alcance a lo que cabe o sumar una persona. |
| T2 | El autor tiene las capacidades técnicas y de venta necesarias. | Desconocida | Autoevaluar brechas (integración con WhatsApp, cobros, ventas) y decidir qué comprar o delegar. |
| T3 | El autor mantendrá el compromiso a lo largo del tiempo necesario para validar. | Desconocida | Fijar un plazo corto de validación (por ejemplo 6 a 8 semanas) con un hito claro. |
| T4 | Hay herramientas disponibles para desarrollo y operación sin presupuesto definido. | Baja | Listar herramientas necesarias y su costo; usar opciones gratuitas para la prueba inicial. |

## Prioridad sugerida de los supuestos

Los supuestos que, si fallan, invalidan la idea y tienen menor evidencia:

1. **B1 y B2**: disposición a pagar y quién paga.
2. **V1, V2 y V3**: que el olvido sea la causa y que el recordatorio lo resuelva.
3. **V5 y S2**: ventaja frente al grupo de WhatsApp y la hoja actuales, y facilidad de copia.
4. **U1**: que los coordinadores mantengan los turnos.
5. **F1**: viabilidad y costo del envío por WhatsApp.

## Pruebas baratas recomendadas (en orden)

1. Registrar durante 2 a 4 semanas los turnos cumplidos y omitidos en las 3 huertas para medir el problema real.
2. Enviar los recordatorios a mano (sin construir nada) y comparar el cumplimiento.
3. Preguntar quién pagaría y cuánto; pedir un compromiso concreto (preventa o carta de intención).
4. Probar una alternativa mínima: mensajes programados en el grupo de WhatsApp existente.
5. Posponer la exploración de balcones y de la marca hasta validar el segmento principal.

## Notas

- Este análisis se basa solo en el texto del caso; no se consultaron fuentes externas ni se verificaron tarifas, normativa o alternativas existentes.
- Las confianzas son juicios cualitativos sobre la evidencia descrita, no mediciones.
