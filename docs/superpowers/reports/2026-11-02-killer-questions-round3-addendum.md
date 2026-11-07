# Adenda a la tercera ronda de brix-killer-questions

Fecha: 2026-11-02. Esta adenda consolida las correcciones que surgen al contrastar el [reporte de la tercera ronda](2026-11-02-killer-questions-round3.md) con la [primera revisión](2026-11-02-killer-questions-round3-review.md), la [segunda revisión](2026-11-02-killer-questions-round3-second-review.md) y el contraste que hizo el usuario en la conversación del 2026-11-02, que no está archivado.

**Alcance.** La adenda no reemplaza ni edita esos documentos ni la [evidencia](2026-11-02-killer-questions-round3/criteria.md); se conservan como registro fechado. No adopta reglas, no sustituye el conteo original, no aplica diffs y no admite, puntúa ni aprueba la skill. No se ejecutó la skill ni se escribió en Blends. Lo dispuso el usuario: un archivo nuevo, sin modificar los existentes. Las decisiones sobre la skill corresponden al humano.

Convención: **Hecho** = comprobado en los archivos citados. **Inferencia** = lectura discutible. **Propuesta** = pendiente de decisión humana.

## Procedencia de las revisiones

- **Hecho:** las dos revisiones declaran el mismo modelo, `claude-opus-5-5`, sin recibo del servidor. No son revisiones humanas y tampoco son independientes entre sí. Su acuerdo sobre F1, F3 y F4 no es una corroboración independiente; es la lectura coincidente de dos ejecuciones del mismo modelo, que el usuario contrastó con las salidas.
- **Hecho:** la segunda revisión no leyó la primera antes de escribirse. Las dos leyeron el reporte antes de cerrar su clasificación, así que pudieron anclarse en él.

## Correcciones consolidadas al reporte

| Tema | Afirmación del reporte | Estado tras el contraste | Fundamento |
|---|---|---|---|
| F1 · vaguedad | Siete fichas U, presentadas «sin un diagnóstico uniforme de incompletitud» | **Reducido.** Seis de las siete ya explicitan lo pendiente; solo E2 no lo hace. Hay que distinguir la incompletitud reconocida de un defecto del instrumento | Ambas revisiones, §F1; confirmado por el usuario |
| F2 · criterio más débil que la pregunta | El criterio de H4 no exige recuperar el lugar a tiempo | **Se sostiene.** La segunda revisión agrega otra instancia: el criterio de H1 omite la «capacidad operativa» que exige su pregunta | Ambas revisiones; confirmado por el usuario |
| F3 · transcripciones | El reporte parafrasea el criterio como «cero transcripciones» | **Debilitado.** El texto dice «sin volver a transcribir» y tiene base en la consolidación que describe la entrada H | Ambas revisiones; el usuario reconoce que la paráfrasis era imprecisa |
| F4 · exploración | «cuatro horas de exploración» | **No demostrado.** La entrada dice «cuatro horas disponibles para investigar». El problema es la falta de sustento, no la repetición en varias celdas: no hubo puntaje y, por tanto, no hubo penalización | Ambas revisiones; precisión del usuario |
| 3/10 interpretables | Resultado descriptivo | **No debe usarse como medida estable.** Las revisiones discrepan en la composición y en la sensibilidad | Ambas revisiones; confirmado por el usuario |
| Envoltorio protector | Factor de confusión señalado solo en E | **Afecta la atribución de N8 en los seis casos**, y también la de N9 por «Ejecución no interactiva» | Ambas revisiones; confirmado por el usuario |
| G · «Hecho verificado» | Celda O en N1 | **No sustentado.** No hay traza de que el ejecutor accediera a la RFC; la corroboración fue del evaluador | Ambas revisiones |

**Precisión metodológica, a pedido del usuario.** Los rangos de las revisiones (2–5/10 en la primera, 1–4/10 en la segunda) son análisis de sensibilidad sobre decisiones de clasificación, no intervalos estadísticos. El kappa de la segunda revisión, ≈ 0,52 con n = 10 entre dos modelos, solo describe el acuerdo observado y no permite inferir nada.

## Correcciones a la segunda revisión

- **E3.** La segunda revisión la clasificó M. **Se retira esa clasificación.** Que la capacidad declarada no demuestre capacidad real es un problema de suficiencia; además, esa capacidad es una elección de un participante y no una observación de su comportamiento. La diferencia con H3, donde las dos horas ya constan en la entrada, requiere una regla explícita (ver más abajo).
- **«Doble penalización».** La segunda revisión dijo que F4 en tres celdas contradecía «No se penaliza dos veces». La expresión es incorrecta, porque no hubo puntaje. A lo sumo es un problema de presentación; el defecto de fondo es que F4 no tiene sustento.

## Conteo M/U/A: lecturas conservadas

El conteo del reporte (**3/10**: H1, H3 y H4) se conserva como resultado original de un solo evaluador, manual y sin revisión independiente según su [manifiesto](2026-11-02-killer-questions-round3/verification.json). No se sustituye de forma retrospectiva.

**Regla propuesta, no adoptada:** un límite cuenta como definido (M) solo si consta en la entrada o en una fuente citada cuando se produce la salida. Si se obtendrá de una declaración posterior de un participante, cuenta U aunque la prueba la recoja.

| Lectura | Fuente | M/10 | Fichas M | Carácter |
|---|---|---:|---|---|
| Original | Reporte | 3 | H1, H3, H4 | Resultado registrado |
| Estricta y consistente | Primera revisión | 2 | H1, H4 | Sensibilidad |
| Laxa y consistente | Primera revisión | 5 | E3, H1, H2, H3, H4 | Sensibilidad |
| Tal como se escribió | Segunda revisión | 3 | E3, H1, H3 | Retirada en E3 |
| Con la regla propuesta | Esta adenda | **2** | H1, H3 | **Condicional** a la regla propuesta |

**Hecho:** dos lecturas dan 2/10 con fichas distintas: {H1, H4} y {H1, H3}. Que coincidan los totales no significa que coincidan las clasificaciones.

- **Estables en todas las lecturas:** H1 es M; E1, H5, I1 e I2 son U.
- **Dependen de la lectura:** E2, E3, H2, H3 y H4.

**Discrepancias abiertas entre revisiones, sin resolver aquí:**

- **H4:** la primera revisión la da M en todas sus lecturas; la segunda la da U porque la prueba dice «La recuperación queda condicionada a definir quién puede corregir».
- **H2:** la primera revisión la da M en lectura laxa, porque el acuerdo entre responsables bastaría; la segunda la mantiene U.

## Hallazgos de la primera revisión que la segunda no cubrió

Comprobados en los archivos:

- **Hecho:** hay dos textos del prompt del ejecutor. [runner-prompt.md](2026-11-02-killer-questions-round3/runner-prompt.md) dice «la skill del archivo skill-under-test.md», sin ruta. El [registro](2026-11-02-killer-questions-round3/execution-log.md), línea 22, cita como literal una versión con ruta absoluta y «de esa misma carpeta».
- **Hecho:** el sello cubre criterios y skill, pero no las entradas. Estas tienen fecha de modificación 12:35, posterior a la del sello, 12:34:50.

Inferencia de la primera revisión, no comprobada: el directorio de trabajo, los `AGENTS.md` y el catálogo de skills que cargaron los ejecutores no están registrados. Podrían aportar protecciones adicionales a E y N8.

## Diffs

**P2 en versión corta: es la propuesta mejor respaldada, pendiente de decisión humana.**

> El criterio cubre cada condición de la pregunta; si no puede, declarar cuál queda sin evaluar.

- Respaldo: F2 (H4) y la instancia de H1.
- Antes de cualquier aplicación hay que conciliarla con la revisión viva (`6279bd3f…`) y con la ruta canónica `brix/.agents/skills/brix-killer-questions/SKILL.md`.
- La primera revisión propuso además fusionarla con P3 («si agrega una restricción, indicar su fundamento»). Queda registrada como alternativa, sin recomendarla aquí.

Las dos revisiones coinciden en el resto de los diffs: P1 se reduce a un campo de una línea, P3 tiene un respaldo débil, P4 no debería aplicarse y P5 es opcional, como mucho su segunda frase. Ninguno se aplicó.

## Siguiente paso propuesto

**Único experimento propuesto para el siguiente paso, sin ejecutar:** una clasificación humana ciega de las diez fichas existentes. La persona aplica la regla de [criteria.md](2026-11-02-killer-questions-round3/criteria.md) y anota qué falta en cada ficha (umbral, definición, evidencia o suficiencia), sin ver el reporte, las revisiones ni esta adenda. No requiere ejecutar el modelo. Resuelve si M/U/A, y con ello F1 y P1, se puede reproducir. Como dice el usuario, para esto sirve más que otra ejecución del modelo.

## Pendientes históricos conservados

No se borra ninguno. Que no se propongan ahora no significa que estén resueltos.

| Pendiente | Origen | Estado |
|---|---|---|
| Identificar con evidencia el modelo de las rondas 1–2 | Reporte | Abierto |
| Revisión humana de los defectos y los conteos | Reporte | Abierto; lo atiende en parte el experimento propuesto |
| Ensayar la protección propia de la skill sin el envoltorio y con una idea de un consumidor real | Reporte | Abierto; no se propone ahora |
| Conciliar cualquier diff con la revisión viva y la ruta canónica | Reporte y ambas revisiones | Abierto |
| Obtener del harness el directorio de trabajo y las instrucciones que cargaron los ejecutores y el autor de H | Primera revisión | Abierto |
| Aclarar cuál de los dos prompts del ejecutor se envió | Primera revisión | Abierto |
| Decidir si el instrumento mide conformidad o utilidad (omisiones, valor frente a una alternativa simple) | Segunda revisión | Abierto |
| Revisar el posible conflicto entre «pedirla» y el modo no interactivo en la revisión viva | Segunda revisión | Abierto |
| Comparar las dos revisiones | Segunda revisión | Atendido por el contraste del usuario; esta adenda lo registra |
| Decidir sobre la regla propuesta para límites declarados | Esta adenda | Abierto; regla no adoptada |
