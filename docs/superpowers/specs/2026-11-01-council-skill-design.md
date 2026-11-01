# Skill de Brix para Reporte de Consejo

Fecha: 2026-11-01. Estado: **diseño aprobado por el usuario el 2026-11-01** para crear la skill candidata `brix-llm-council` (creada ese día, sin evaluar ni ejecutar). No admite, instala ni activa una skill; no cambia la política del precursor.

## Propósito y enfoque

Cubrir «Reporte de Consejo» con una skill propia de Brix, adaptando el comando `/council` del precursor. El usuario propone este enfoque en el chat del 2026-11-01. La entrada por archivo y las equivalencias públicas ya están definidas en [comandos](../../../brix/docs/commands.md); el consumidor conserva la coordinación y la decisión humana.

Alternativas consideradas: adoptar una skill externa (requiere demostrar una ventaja frente al procedimiento existente); conservar solo el comando ligado a `ideas/<slug>/` (no satisface la interfaz por archivo ni la entrega como skill); adaptar el procedimiento propio (enfoque recomendado por el usuario). La adaptación conserva el método, pero explicita sus dependencias y límites.

## Contrato propuesto

- Entrada: Markdown y revisión identificada, pregunta explícita o preguntas identificables en la entrada, destino autorizado y configuración de ejecución declarada por el consumidor.
- Lectura: documento de entrada y lista explícita de referencias autorizadas. La restricción se transmite a todos los asesores; nombrar un archivo no autoriza leerlo. El contenido analizado es dato y no modifica las instrucciones.
- Método: cinco asesores independientes; anonimización con mapeo registrado; cinco revisiones cruzadas con orden rotado; una síntesis. Son **11 asientos totales**, incluido el Contrarian de otra familia; no 11 más un modelo externo.
- Configuración: bindings suministrados por el consumidor, sin importar resolvers privados ni descubrir rutas del precursor. Registrar identidad observada y distinguirla de la solicitada. Si el entorno no puede demostrar otra familia, declarar el límite; no simularla con una persona del mismo modelo.
- Recursos: antes de ejecutar, declarar máximo de invocaciones, concurrencia soportada, espera por fase y presupuesto autorizado o límite de cuota verificable. No inferir costo cero de una suscripción. Sin configuración suficiente, devolver diagnóstico sin iniciar llamadas; no reintentar automáticamente llamadas con efectos o consumo incierto.
- Salida: reporte Markdown con preguntas candidatas y sus orígenes, desacuerdos, puntos ciegos, riesgos, hechos cuestionados, respuestas, revisiones y límites. Asesoramiento sin recomendación de ingreso, graduación o aprobación. Vincular reporte a revisión de entrada y configuración realmente usada.
- Repetición: identidad derivada del documento, pregunta y configuración; registrar material nuevo y antecedentes proporcionados explícitamente por el consumidor. No recorrer el portfolio. No sobrescribir reportes ni presentar una corrida parcial como completa.
- Fallos: identificar asientos fallidos, trabajo completado y consumo conocido; conservar una salida parcial en destino autorizado cuando sea posible. No inventar respuestas, identidades ni costos. Explicar qué falta para reanudar sin duplicar consumo.

La falta de un runtime o driver público se declara como dependencia pendiente; escribir `SKILL.md` no demuestra que `/council` o `brix council` estén implementados para esa interfaz.

## Procedencia y entrega

La futura skill tendrá instrucciones en español, identificador en inglés y documento de procedencia con revisión y hash del comando leído, atribución y diferencias. Seguirá el precedente local de `killer-questions` sin asumir que su carpeta sea descubrible en todos los hosts. La ubicación concreta y sus mecanismos de carga se verifican antes de afirmar disponibilidad.

No copiar ni alterar el comando original, no inicializar repositorios, no modificar bindings históricos y no resolver la deuda de propiedad mediante una migración implícita. La matriz puede actualizarse cuando existan artefacto y estado comprobados, conservando la procedencia histórica de su asignación anterior.

## Evaluación propuesta

Mantener separado el requisito de contar con una skill de su admisión. Un resultado desfavorable no obliga a aprobar una excepción.

Antes de agregar otro perfil, comprobar qué parte del proceso actual puede usarse sin cambiar sus reglas. «Sin evidencia» y «no aplica» son estados distintos; no introducir valores favorables para cubrir datos ausentes. Comunidad y mantenimiento pesan hoy 20 % y 15 %, respectivamente: 35 % en total.

Si hace falta un perfil para artefactos propios, proponerlo como política general, aplicable también a otras skills propias y con autoridad y revisión independientes de esta candidata. Conservar seguridad, ajuste, ingeniería, sostenibilidad, mantenimiento, procedencia y controles de decisión. La popularidad externa puede resultar no pertinente; dueño y versión son requisitos verificables, no sustitutos suficientes de mantenimiento ni pruebas. No fijar pesos para conseguir que esta skill apruebe. Registrar versión del perfil y evitar comparar su resultado numérico con el perfil externo como si fueran la misma escala.

La validación requiere tanto revisión de instrucciones como ejecución acotada posterior a la aprobación exigida por `/tool`. Comprobar al menos: entrada válida, permiso de lectura insuficiente, instrucciones incrustadas, repetición sin material nuevo, familia alternativa ausente, fallo o timeout parcial y protección de una salida ya existente. Una prueba sintética o una lectura estática no demuestra decorrelación real, calidad de conclusiones ni control de gasto del host.

## Autoridad y cierre

El precursor permanece en solo lectura. Rechazar formalmente la candidata externa o modificar su política/registro exige autorización con clon, rama y alcance identificados; la recomendación del evaluador no constituye la decisión humana. El rechazo no es una precondición técnica para diseñar la skill propia.

La ejecución del diseño requerirá aprobación antes de crear la skill y sus dependencias. El resultado esperado será una candidata con procedencia y verificaciones, seguida del proceso de evaluación y decisión humana; solo entonces podrá declararse admitida. Las evidencias y propuestas elaboradas aquí no reemplazan el registro canónico del precursor.
