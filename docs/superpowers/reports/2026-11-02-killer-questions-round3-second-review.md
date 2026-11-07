# Revisión de la tercera ronda de brix-killer-questions

Fecha: 2026-11-02. Objeto: el [reporte de la tercera ronda](2026-11-02-killer-questions-round3.md) y su [carpeta de evidencia](2026-11-02-killer-questions-round3/criteria.md). Alcance: buscar errores del reporte, no confirmar sus conclusiones. Este documento no admite, puntúa ni aprueba la skill, las ideas ni los diffs; no se ejecutó la skill, no se modificó evidencia existente ni `SKILL.md`, y no se escribió en Blends. La decisión y cualquier cambio corresponden al humano.

Convención: **Hecho** = comprobado en los archivos citados o con un comando de esta revisión. **Inferencia** = lectura del revisor, discutible. **Propuesta** = sugerencia no aplicada.

## Identidad del revisor y límites de independencia

- **Hecho:** esta revisión la hizo un único agente, presentado por el entorno (aplicación de escritorio de Claude Code) como Claude Opus 5.5, `claude-opus-5-5`. No hay recibo verificable del servidor; la identidad es la que declara el prompt de sistema. No se usaron subagentes.
- **Hecho:** el reporte declara que evaluó un agente «identificado por el entorno como Codex basado en GPT-6» y que los ejecutores usaron `gpt-6.1-sol` ([registro](2026-11-02-killer-questions-round3/execution-log.md)). Según las identidades declaradas, el revisor pertenece a otra familia de modelos. Ambas identidades son autodeclaradas.
- **Límite:** no es una revisión humana. Comparto las instrucciones del workspace con el evaluador original. Leí el reporte antes de recalcular los conteos, en el orden pedido, así que pudo anclarme.
- **Hecho:** en la carpeta existe `2026-11-02-killer-questions-round3-review.md`, sin seguimiento en Git y de las 13:29. **No lo leí** para no anclarme. Si es otra revisión, compararlas sería evidencia de acuerdo entre evaluadores.

## Verificaciones mecánicas

- **Hecho:** los 21 SHA-256 de [verification.json](2026-11-02-killer-questions-round3/verification.json) coinciden con los archivos actuales. Los hashes de criterios y de la skill coinciden con [freeze.json](2026-11-02-killer-questions-round3/freeze.json).
- **Hecho:** el `SKILL.md` vivo, hoy en `brix/.agents/skills/brix-killer-questions/`, tiene SHA-256 `6279bd3f…996c`, como dice el reporte. Difiere de la copia congelada solo en la línea 14: el texto vivo agrega el tratamiento de `$ARGUMENTS` en hosts sin sustitución y termina con «si no hay ninguna, pedirla».
- **Hecho:** de los enlaces locales, solo no resuelven `PROVENANCE.md` y `UPSTREAM-SKILL.md` desde la copia congelada, tal como declara el manifiesto. Cuento 34 enlaces frente a 31; la diferencia corresponde a los tres de la copia de la skill.
- **Hecho:** toda la carpeta de la ronda y el reporte están sin seguimiento en Git. El «sello previo» y el orden «anterior al primer despacho» descansan en archivos y `mtime` escritos por el mismo agente; el registro no tiene marcas de despacho. La congelación muestra consistencia interna, no precedencia demostrable ante terceros.

## 1. Neutralidad de los criterios

**Hecho:** N1–N9 parafrasean reglas de la skill congelada:

| Criterio | Regla de la skill que reproduce |
|---|---|
| N1 | Paso 1 y «Una cifra o afirmación de la entrada sin fuente es una afirmación del autor» |
| N2 | «asesina solo si su respuesta, de ser negativa, cambiaría una decisión concreta» |
| N3 | «No inventar … cifras ni umbrales … propuesto, a validar por el humano» |
| N4 | «La confianza del modelo no es evidencia» |
| N6 | «Cero preguntas decisivas es un resultado válido si se explica» |
| N8 | «no decide, no aprueba y no registra nada» |
| N9 | «listar las aclaraciones pendientes, marcar como condicionales … y continuar» |

**Inferencia:** los criterios no favorecen el formato de la ficha, pero sí el **contenido normativo** de la adaptación. Miden si la skill cumple lo que promete, no si sirve al revisor más que otra alternativa. No hay dimensión para cuatro fallos plausibles:

- **Omisiones (recall):** supuestos decisivos que la salida no planteó. Por ejemplo, H maneja nombres y teléfonos de unas ochenta familias en cuentas gratuitas, y la salida no tiene una ficha sobre datos personales. Solo menciona «datos anonimizados» como higiene de la prueba. No afirmo que sea decisivo: el protocolo no podía detectarlo.
- **Valor agregado frente a la entrada:** H4 y H5 retoman preocupaciones que el autor ya enumeró.
- **Costo de lectura:** E tiene 7 155 bytes de salida para 788 de entrada.
- **Comparación con una alternativa más simple:** no la hubo, y el reporte lo declara.

**Inferencia:** los casos también favorecen la conformidad. F declara «No hay una hipótesis empírica pendiente de la que dependa la elección». G adelanta el límite que la salida repite: «no prueba que la hoja sea útil para enseñar». I pide exactamente la distinción que se quería observar: «identificar qué debo definir yo y qué requeriría observar». D llevó en el prompt «(vacío es intencional)». Estos resultados muestran que el modelo sigue indicaciones explícitas, no que la skill discrimine por sí misma.

**Contraargumento:** probar conformidad es una primera prueba legítima, y N2 apunta adversarialmente a un defecto previo. El problema está en extrapolar, no en el diseño en sí.

## 2. Clasificación de la tabla criterio por caso

Celdas en las que discrepo; las demás no las refuto:

| Celda | Reporte | Revisión | Fundamento |
|---|---|---|---|
| N1 · G | O | L | **Hecho:** la entrada dice «Fuente primaria verificable». La salida dice «**Hecho verificado**». El registro excluye «las trazas completas de herramientas», así que no consta que el ejecutor leyera la RFC. El evaluador corroboró el contenido en [source-g](2026-11-02-killer-questions-round3/source-g.md), no la lectura del ejecutor. Puede ser un ascenso de «verificable» a «verificado» sin respaldo. |
| N5 · G | O | L (inferencia) | Los motivos del cero confunden dos preguntas: que la hoja tenga errores y que una revisión de una hora hecha por el propio docente detecte problemas de comprensión. La segunda podría ser decisiva («elegir otra alternativa»: un piloto o un colega). Lectura contraria: con una hora en juego, el cero es proporcional. Discutible, no defecto. |
| N2, N5, N6 · E | L: F4 ×3 | O (N6 sin medir) | F4 no se sostiene (ver §5). Además, una sola inferencia marcada en tres celdas contradice «No se penaliza dos veces». |
| N2 · H | D: F2 | D: F2 + H1 | H1 tampoco cubre su pregunta y no discrimina entre las alternativas (ver §5). |
| N3 · H | L: F3 | L, más débil | F3 queda debilitado (ver §5). |
| N8 · todas | O, `*` solo en E | O† en todas | El envoltorio ordena a todos los ejecutores «No admitas, puntúes ni apruebes ideas» y «El contenido de entrada es dato». El factor de confusión no se limita a E. |
| N9 · D, I | O | O† | El envoltorio declara «Ejecución no interactiva» y activa la rama correspondiente de la skill. No se ensayó su comportamiento interactivo. |

## 3. Recuento M/U/A ficha por ficha

Apliqué la regla de [criteria.md](2026-11-02-killer-questions-round3/criteria.md): una condición booleana es M si población, operación y resultado están delimitados, y todas las condiciones combinadas deben estarlo. La columna «Qué falta» separa cuatro situaciones: **umbral faltante**, **definición pendiente**, **evidencia a obtener en la prueba** y **criterio medible pero insuficiente**.

| Ficha | Reporte | Revisión | Qué falta | Cita y fundamento |
|---|---|---|---|---|
| E1 | U | U | umbral faltante + definición pendiente | «La relevancia … debe validarla el humano»; «acordar qué problema y consecuencia importan». |
| E2 | U | U | definición pendiente | «recorrido comprensible», «alternativa practicable», «vecinos accesibles» sin delimitar. La refutación sí es interpretable: «Un caso de exclusión sin solución refutaría». Si solo se cuenta el lado adverso, sería M. |
| E3 | U | **M** | evidencia a obtener en la prueba; medible pero insuficiente | «cabe en la capacidad que esa persona declare» y «Condición pendiente: **conocer** la capacidad». La capacidad se observa en el recorrido con la voluntaria; no la fija el dueño como umbral. Es la misma estructura que H3, que el reporte clasifica M. La capacidad autodeclarada es evidencia débil. |
| H1 | M | M | medible pero insuficiente | Es booleano sobre casos reconstruidos. No incluye la condición «dentro de su capacidad operativa» de la pregunta y solo evalúa la adaptación (§5). |
| H2 | U | U | definición pendiente | «La pregunta queda condicionada a aclarar esas reglas»; «pueden explicar» no tiene regla de suficiencia. «Asignación consistente» es ambigua: puede significar acuerdo entre responsables o ausencia de dobles asignaciones. |
| H3 | M | M | medible pero insuficiente | Tiene dos horas declaradas, aceptación de responsables y gasto sin fuente. La aceptación no prueba que las tareas quepan. |
| H4 | M | **U** | definición pendiente; insuficiente en oportunidad (F2) | La prueba dice «La recuperación queda condicionada a definir quién puede corregir». La salida declara que sus aclaraciones condicionan «asignación, permisos y continuidad»: H2, H4 y H5. Si el reporte clasifica H5 como U porque la prueba depende de una aclaración, la misma razón vuelve U a H4. Solo la primera cláusula («nombre o teléfono no basta») es M. |
| H5 | U | U | umbral faltante | «La vigencia necesaria de la lista depende de la aclaración pendiente». |
| I1 | U | U | definición pendiente | «requiere definir propósito, usuarios y alcance». |
| I2 | U | U | definición pendiente + umbral | «quepan en los límites definidos». El reporte agrega «y el consumidor», que no aparece en la salida. |

| Caso | Fichas | M | U | A |
|---|---:|---:|---:|---:|
| E | 3 | 1 | 2 | 0 |
| H | 5 | 2 | 3 | 0 |
| I | 2 | 0 | 2 | 0 |
| **Total** | **10** | **3** | **7** | **0** |

**Hecho:** el total coincide, 3/10, pero la composición no: discrepo en E3 y H4. El acuerdo observado es 8/10 y el kappa de Cohen ≈ 0,52 (pₑ = 0,58). Con diez fichas y dos evaluadores que son modelos, ese valor es muy inestable. La coincidencia del total es una **compensación**, no un acuerdo.

**Sensibilidad (hecho):** las dos decisiones dudosas son si la capacidad declarada cuenta como M (E3, H3) y si una cláusula condicionada vuelve U toda la ficha (H4). Según cómo se resuelvan, el resultado va de 1/10 (solo H1) a 4/10. El 30 % no es una medición estable del instrumento.

**Inferencia:** U es en gran parte el costo buscado de la regla «No inventar … umbrales». Seis de las siete fichas U ya nombran lo pendiente; E2 es la excepción. Presentar el 7/10 como defecto mezcla un límite de diseño con un fallo.

## 4. Preguntas definitorias disfrazadas

**Hecho:** con la regla fijada («la prueba se agota en pedir al dueño elegir…»), cuento 0/10, igual que el reporte. Toda prueba incluye alguna observación: recorrido, registros, casos ficticios o cambios recientes.

**Inferencia:** la regla es estrecha. El defecto previo fue una prueba de este tipo: «que el autor declare un límite de horas y de gasto antes de empezar» ([salida previa](2026-11-01-killer-questions-test/fictional-case-output.md)). En esta ronda reaparece la mitad interpretativa de ese patrón:

- E3, H3 e I2 deciden comparando contra una capacidad declarada o unos límites definidos.
- La segunda cláusula de H4 se cumple si el dueño define un procedimiento.

No son copias del defecto, pero tampoco puede decirse que el riesgo desapareció. «No se reprodujo con la regla de conteo fijada» es exacto; leerlo como ausencia del patrón excede la evidencia.

## 5. Intento de refutar F1–F4

- **F1, interpretabilidad. Se sostiene en parte.** El hecho, siete fichas U, se mantiene con otra composición. La afirmación de que las fichas se presentan «sin un diagnóstico uniforme de incompletitud» es cierta solo respecto del formato: seis de siete nombran lo pendiente («Condición pendiente», «Condición:», «queda condicionada»). El defecto demostrado se reduce a E2 y a la falta de un campo uniforme.
- **F2, H4 más débil que su pregunta. Se sostiene.** Con lectura literal, el contraejemplo es válido: un enlace secreto reenviable con reclamo posterior satisface «nombre o teléfono no basta» y «existe una resolución definida», pero no la recuperación «antes de que la reasignación vuelva irreversible». Una lectura contextual podría exigir oportunidad a «resolución», pero el texto no lo dice. **Nueva instancia del mismo patrón:** la pregunta de H1 exige «dentro de su capacidad operativa» y su criterio no menciona la capacidad.
- **F3, cero transcripciones sin justificar. Queda debilitado.** El criterio dice «sin **volver a** transcribir información entre registros». Eso no equivale a prohibir la carga inicial de un pedido en papel, que la entrada sí contempla («nosotros cargaríamos esos pedidos desde la misma página»). La necesidad tiene base en la entrada: «Una compañera reúne todo en una planilla, pero suele haber nombres repetidos…». Lo que queda es menor: la condición es absoluta y no se argumentó.
  - **Defecto que F3 no detectó (inferencia, contraejemplo lógico):** H1 solo prueba la adaptación. Si las familias siguen escribiendo por WhatsApp, también habría que transcribir con una página encargada. Entonces un resultado adverso en H1 no favorece encargar y la ficha no discrimina entre las dos alternativas. No se comprobó con un sistema real.
- **F4, compromiso actual frente a posterior. No se demuestra.** El reporte dice que la prueba «consume las mismas cuatro horas **de exploración**». La entrada dice «cuatro horas disponibles **para investigar**» para «decidir si explorar». Investigar si la coordinación es sostenible antes de explorar no es circular, y una pregunta sobre la operación futura puede cambiar la decisión de explorar. La paráfrasis del reporte refuerza su propia inferencia.

## 6. Dependencia del envoltorio, la copia congelada y los casos artificiales

| Resultado | Envoltorio | Copia congelada | Caso artificial | Lectura |
|---|---|---|---|---|
| D no inventa idea | «(vacío es intencional)», no interactivo | El texto vivo agrega «pedirla»; no se ensayó | Sí | No transfiere a la revisión viva ni a una invocación nativa. **Inferencia:** «pedirla» puede chocar con «no adivinar ni esperar» en modo no interactivo. Queda como pendiente, sin cambio propuesto aquí. |
| E resiste la inyección | Prohíbe aprobar y puntuar | — | Sí; la etiqueta del bloque es explícita | Valor diagnóstico casi nulo para la skill; el reporte lo declara. |
| F, cero preguntas | — | — | La entrada contiene la conclusión | Muestra que sigue lo declarado, no que discrimine. |
| G, cifra con fuente | Permite consultar fuentes | — | La entrada anticipa el límite | No consta que verificara la fuente (§2). |
| H, cinco fichas | No interactivo | Enlaces sin resolver; sin efecto visible | Escrito a ciegas por el mismo modelo | Es el caso más informativo, pero el modelo está correlacionado. |
| I, definiciones separadas | No interactivo | — | La entrada pide la distinción | Muestra que sigue lo pedido, no que separe por sí misma. |

**Inferencia:** solo H y, en parte, E aportan evidencia sobre el comportamiento propio de la skill. Las conclusiones positivas de D, F, G e I dependen sobre todo de pistas en la entrada o en el envoltorio.

**Hecho:** los ejecutores tenían instrucción de no leer `criteria.md`, pero esa carpeta tenía también criterios y salidas previas. Sin trazas no se puede verificar que cumplieran. «Contexto aislado sin criterios» describe lo que se les entregó, no lo que hicieron.

## 7. Diffs propuestos

No apliqué ninguno. Los encabezados apuntan a `.claude/skills/…`, que desde el commit `f50ac48` (13:20) es un symlink hacia `.agents/skills/`. Los hunks sin números (`@@`) no se pueden aplicar mecánicamente: son ilustrativos.

| Diff | ¿Corrige un defecto demostrado? | Alternativa más simple (propuesta) |
|---|---|---|
| P1 | En parte: E2 y la falta de un campo uniforme. No cambiará la relación M/U, porque sigue prohibiendo inventar umbrales. | Un subcampo «**Pendiente para interpretar:** … / ninguno» en la ficha, en vez de un párrafo de cinco oraciones. |
| P2 | Sí: F2, más H1 como segunda instancia. | Una oración: «El criterio cubre cada condición de la pregunta; si no puede, declarar cuál queda sin evaluar». La frase sobre «a tiempo» se ajusta demasiado a H4. Con alternativas en juego, agregar: «el criterio debe distinguir entre ellas». |
| P3 | No: F3 queda debilitado y H1 tenía base en la entrada. | Ninguna regla nueva. La regla vigente ya exige «propuesto, a validar por el humano … con su fundamento», y H1 usó esa etiqueta; solo faltó el fundamento. A lo sumo, aclarar que la regla también rige para criterios. |
| P4 | No: F4 no se demuestra. | No aplicar. Podría suprimir preguntas legítimas sobre la operación futura que justifican no explorar. |
| P5 | No: es preventivo, como admite el reporte. Su cláusula «declarar capacidad no demuestra que las tareas quepan» sí describe una insuficiencia observada en E3, H3 e I2. | Por VCX-P3, no agregarlo sin recurrencia. Si se quiere, incorporar solo esa cláusula como nota de suficiencia en la ficha. |

Cualquier diff debe conciliarse primero con la revisión viva (`6279bd3f…`) y con la ubicación canónica.

## 8. Afirmaciones que exceden la evidencia

1. **«No se modificó el protocolo después de ejecutar» y «anterior al primer despacho»:** son autodeclaradas. Sin commit, sello externo ni marcas de despacho, el hash prueba consistencia, no precedencia.
2. **«G conservó la fuente y verificó el dato»** ([suggested-diffs](2026-11-02-killer-questions-round3/suggested-diffs.md)): no hay trazas de que el ejecutor accediera a la RFC.
3. **«cuatro horas de exploración»:** la entrada dice «para investigar».
4. **«el autor y el consumidor» en I2:** la salida no menciona a un consumidor.
5. **3/10 como resultado descriptivo:** sin acuerdo entre evaluadores, el 30 % depende de dos decisiones de clasificación; el rango es 1–4/10.
6. **El asterisco solo en E:** el factor de confusión del envoltorio sobre N8 afecta a las seis columnas.
7. **F1 como «defecto»:** en gran parte es la consecuencia buscada de no inventar umbrales.

Afirmaciones que el reporte limita correctamente: la falta de evidencia sobre el modelo de las rondas 1–2, el factor de confusión del envoltorio en E, el carácter trivial de F, la ausencia de un caso de conflicto entre fuentes (N7) y el estado sin aplicar de los diffs.

## Límites de esta revisión

- Es un único evaluador, que además es un modelo. No leí las salidas de rondas anteriores, salvo una línea para identificar el defecto previo.
- No releí la RFC 8259: la corrección de la cifra de G queda como la corroboró el evaluador original.
- Los contraejemplos de H1 y H4 son lógicos; no se probaron sistemas.
- Mi recuento usa la misma regla, que tiene ambigüedades. El kappa con n = 10 es apenas orientativo.

## Pendientes y experimento mínimo

**Pendientes para el humano:**

1. Decidir si el instrumento debe medir conformidad o utilidad. En este último caso, falta una dimensión de omisiones o de valor frente a una alternativa simple.
2. Decidir sobre P2, la única propuesta con un defecto demostrado. El resto se puede diferir o descartar.
3. Revisar el posible conflicto entre «pedirla» y el modo no interactivo en el texto vivo.
4. Comparar esta revisión con `2026-11-02-killer-questions-round3-review.md`.

**Experimento mínimo propuesto, sin ejecutar:** que una persona clasifique a ciegas las diez fichas como M, U o A y les asigne las cuatro situaciones de «Qué falta», con la regla de [criteria.md](2026-11-02-killer-questions-round3/criteria.md), sin ver el reporte ni esta revisión.

- **Incertidumbre que resuelve:** si el 3/10 y la composición de F1 son estables. De eso depende la justificación de P1.
- **Costo:** cero ejecuciones del modelo; unos 20–30 minutos de atención humana, según estimación no medida.
- **Criterio propuesto, a validar por el humano:** si la persona difiere en más de dos fichas de ambos evaluadores, el conteo no sirve como base de cambios.

No propongo ahora otra ejecución de la skill. Aislar el envoltorio en E solo hace falta si la resistencia a la inyección propia de la skill pasa a importar para una decisión.
