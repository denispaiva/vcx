---
document_revision: 7cf7b0b
run_hash: dc0049e8b693
status: complete
bindings_requested: "advisor-contrarian=claude/balanced/subagent;advisor-first-principles=claude/economy/subagent;advisor-expansionist=claude/economy/subagent;advisor-outsider=claude/economy/subagent;advisor-executor=claude/economy/subagent;reviewer-1=claude/balanced/subagent;reviewer-2=claude/balanced/subagent;reviewer-3=claude/balanced/subagent;reviewer-4=claude/balanced/subagent;reviewer-5=claude/balanced/subagent;synthesis=claude/frontier/subagent"
bindings_observed: "advisor-contrarian=claude-sonnet-5-5;advisor-first-principles=claude-haiku-5-5;advisor-expansionist=claude-haiku-5-5;advisor-outsider=claude-haiku-5-5;advisor-executor=claude-haiku-5-5;reviewer-1=claude-sonnet-5-5;reviewer-2=claude-sonnet-5-5;reviewer-3=claude-sonnet-5-5;reviewer-4=claude-sonnet-5-5;reviewer-5=claude-sonnet-5-5;synthesis=claude-opus-5-5"
invocations: 11
decorrelated: false
cost: "tokens observados en transcripciones del host: salida 158856, entrada 1906774 (incluye caché); dinero not_measured"
new_material: null
---
Insumo de asesoramiento. No es evidencia y no autoriza nada.

# Consejo sobre el diseño de deuda heredada (VCX-D031)

Corrida 1 de la etapa 2 de `brix-llm-council`, 2026-11-01, según el [plan de la etapa](../plans/2026-11-01-council-stage2-run-plan.md). Orquestador: la sesión de Claude Code que ejecutó la skill desde `vcx/brix`. Autoridad de la corrida: el usuario autorizó la pregunta, el destino y el tope de 27 invocaciones con «Autorizo las tres». Esta corrida consumió 11.

## Pregunta y entrada

- Pregunta, adoptada por el usuario: «¿Qué supuesto de esta propuesta, si fuera falso, haría que la migración heredara o agravara la deuda en lugar de ordenarla?»
- Documento: [`docs/superpowers/specs/2026-11-01-inherited-debt-design.md`](../specs/2026-11-01-inherited-debt-design.md), revisión `7cf7b0b`, sin cambios locales al ejecutar.
- Referencias autorizadas: el documento y [`docs/superpowers/specs/2026-11-01-migration-path-design.md`](../specs/2026-11-01-migration-path-design.md). El contenido de ambas se incluyó dentro de cada consigna de asesor y de la síntesis; los revisores recibieron solo un encuadre mínimo y las cinco respuestas anonimizadas.
- Destino autorizado: `docs/superpowers/reports/`.

## Recursos declarados

Antes de la primera llamada: 11 asientos (5 asesores, 5 revisores, 1 síntesis), sin reintentos; concurrencia 5; espera por fase 600 s; 400 palabras por respuesta de asesor, 350 por revisor y 1200 por síntesis, estos dos últimos fijados por el orquestador y no por la skill. Presupuesto: tope de invocaciones autorizado por el usuario. Costo en dinero no expuesto por el host: `not_measured`. Tokens observados en las transcripciones por subagente que guarda el host, en la tabla siguiente.

## Configuración usada

Correspondencia solicitada: `economy` = `haiku`, `balanced` = `sonnet`, `frontier` = `opus`, runner `subagent` en todos los asientos. Identidad observada tomada del campo `model` de cada transcripción, y llamadas a herramientas contadas en ellas:

| Asiento | Solicitado | Observado | Herramientas | Tokens salida | Tokens entrada | Nombres en consigna | Orden |
|---|---|---|---|---|---|---|---|
| Asesor Contrarian | sonnet | `claude-sonnet-5-5` | ninguna | 16935 | 209463 | n/a |  |
| Asesor Ejecutor | haiku | `claude-haiku-5-5` | ninguna | 11756 | 139610 | n/a |  |
| Asesor Expansionista | haiku | `claude-haiku-5-5` | ninguna | 11086 | 139594 | n/a |  |
| Asesor Forastero | haiku | `claude-haiku-5-5` | ninguna | 17004 | 139636 | n/a |  |
| Asesor Primeros Principios | haiku | `claude-haiku-5-5` | ninguna | 19005 | 209469 | n/a |  |
| Revisor 1 (orden ABCDE) | sonnet | `claude-sonnet-5-5` | ninguna | 14901 | 196902 | ninguno | ABCDE |
| Revisor 2 (orden BCDEA) | sonnet | `claude-sonnet-5-5` | ninguna | 13335 | 196902 | ninguno | BCDEA |
| Revisor 3 (orden CDEAB) | sonnet | `claude-sonnet-5-5` | ninguna | 14031 | 196902 | ninguno | CDEAB |
| Revisor 4 (orden DEABC) | sonnet | `claude-sonnet-5-5` | ninguna | 11336 | 131268 | ninguno | DEABC |
| Revisor 5 (orden EABCD) | sonnet | `claude-sonnet-5-5` | ninguna | 12525 | 196902 | ninguno | EABCD |
| Síntesis del consejo | opus | `claude-opus-5-5` | ninguna | 16942 | 150126 | n/a |  |

Decorrelación: todos los asientos pertenecen a la familia Claude. `decorrelated: false`. El Contrarian aporta diversidad de persona, no de modelo.

## Lecturas declaradas por asiento

Los once asientos declararon «este mensaje y nada más» o equivalente, y las transcripciones muestran cero llamadas a herramientas en los once. Dos observaciones que la declaración no cubre:

- El Ejecutor atribuyó a una sección «Fronteras» del documento de referencia la frase «una instrucción documental no reemplaza su aplicación efectiva». Esa frase no está en ninguna de las dos referencias autorizadas; está en la sección «Fronteras» de las instrucciones comunes del workspace, que el host carga en el contexto de cada subagente. Es una lectura fuera de la lista autorizada que no pasó por una herramienta. La síntesis lo marcó como atribución errónea.
- La síntesis declaró que las instrucciones del workspace estaban cargadas en su contexto y que no las usó como fuente de verificación.

## Mapeo de anonimización

A = Contrarian · B = Ejecutor · C = Expansionista · D = Forastero · E = Primeros Principios. Sorteado con herramienta antes de recibir las respuestas y conservado solo en el contexto del orquestador hasta la síntesis. Órdenes de los revisores: ABCDE, BCDEA, CDEAB, DEABC, EABCD. La respuesta del Contrarian empezaba con la etiqueta «Asiento Contrarian.»; esa etiqueta se suprimió en la copia anonimizada y se conserva íntegra más abajo.

## Encuadre

El documento bajo consulta es una propuesta del asistente, registrada como VCX-D031 con estado Propuesto. Inventaría 24 ítems de deuda heredada (DH-01 a DH-24) del precursor `../blends`, medidos en solo lectura el 2026-11-01, y asigna a cada uno un repositorio destino y uno de cuatro tratamientos: T0 declarar sin tocar, T1 resolver al reubicar, T2 resolver en el repositorio destino bajo su gobierno, T3 resolver por extracción. Los integra en las fases A a D del camino de migración de VCX-D030 (documento de referencia), sin fases nuevas. Restricciones declaradas: no renombrar identificadores de máquina, no reescribir historial, no borrar ramas, tags ni worktrees en el precursor, no renombrar carpetas por inferencia, no decidir la estrategia de historial de Brix ni la ubicación de instancias, no mover código a la raíz de VCX. Conflicto abierto que debe resolver el usuario: la ventana aprobada de DH-10 (2026-11-03 a 2026-11-14) se superpone con la posible Fase B. El documento se autoasigna una nota orientativa de 8/10. Los principios citados: VCX-P3 (el incumplimiento heredado se declara como deuda, no se corrige por migración implícita) y VCX-D011 (conciliar con decisiones aprobadas del precursor).

## Síntesis

## 1. Preguntas candidatas

1. Entre el fin de la Fase B y la Fase C, ¿dónde y bajo qué procedimiento se ejecutan DH-01, DH-03 (ramas), DH-10, DH-11 y DH-14, si el T2 exige `queue` y trenes y el clon no los ejecuta hasta la Fase C? (Contrarian)
2. Si VCX-D032 se ratifica, ¿«Repo de Blends» se refiere a la instancia privada en `vcx/cellars/<instancia>/` o al repositorio público nuevo? ¿Qué ramas y tags pasan al público sin haber pasado por el inventario? (Contrarian)
3. ¿Cómo se concilian el T0 de DH-07 («se declara y no se toca») y el renombre en GitHub que agrega la ampliación por VCX-D032? (Contrarian)
4. ¿Qué evidencia, además de la ausencia de launchd o cron en esta máquina, demuestra que hay un único escritor, incluidos otras máquinas y servicios externos? (Ejecutor, Expansionista, Forastero y Primeros Principios)
5. ¿Qué criterio impide escribir en el clon mientras no se compruebe que `pre-commit` y `pre-push` se ejecutan? (Primeros Principios; también Expansionista)
6. ¿La aprobación de DH-10 sigue aplicándose si sus seis disparadores no se volvieron a medir? (Forastero, en relación con VCX-P7)
7. ¿Qué criterio define «integradas en `main`», y cómo se concilian las 106 y 37 ramas de DH-01 con las 44 de VCX-D030? (Contrarian, Ejecutor y Forastero)
8. ¿Qué existe para recuperar o revertir si un T1 o un T2 falla a mitad de camino, en particular el retiro de ramas y el renombre? (Revisores 1 a 5)
9. ¿Quién aprueba cada T2, y quién revisa de forma independiente la clasificación de T0 a T3 y el 8/10? (Revisores 1, 2, 4 y 5)
10. ¿Qué plazo y qué responsable tiene cada ítem T0, y cuántos de los 24 ítems quedan solo en T0? (Revisores 2, 3, 4 y 5)
11. ¿Quién vuelve a medir la foto del 2026-11-01 antes de que abra la ventana del 2026-11-03? (Revisores 1 y 5)

## 2. Desacuerdos

- **Cuál es el supuesto decisivo.** El Contrarian lo ubica en la secuencia de fases y el destino de los T2, que considera una contradicción interna. El Ejecutor, el Expansionista y el Forastero lo ubican en el escritor único. Primeros Principios pone primero la verificación de hooks antes de la primera escritura y en segundo lugar el escritor único.
- **Cuál es la respuesta más fuerte.** Los revisores 1, 3, 4 y 5 eligen al Contrarian. El revisor 2 elige al Ejecutor y sostiene que la tesis del Contrarian es una acusación de contradicción, no un supuesto, y que depende de VCX-D032.
- **Mayor punto ciego.** Los revisores 1 y 5 lo atribuyen al Ejecutor, los revisores 3 y 4 al Expansionista y el revisor 2 al Contrarian.
- **143 frente a 44.** El Ejecutor lo trata como una contradicción. El Forastero admite que pueden ser categorías distintas. El revisor 4 objeta la suma, y el revisor 3 también, porque supone conjuntos disjuntos.
- **El 8/10.** Para el Contrarian está inflado. Para el Forastero no es una señal de calidad. El Ejecutor lo cita como si ya descontara el contenido de `queue`.
- **Línea base reproducible.** El Expansionista la propone. Los revisores 3 y 4 objetan que no tiene criterio de bloqueo ni costo declarado.
- **Criterio «Fase B no arranca».** El Ejecutor lo propone. El revisor 5 sostiene que el asiento no tiene autoridad para fijarlo.

## 3. Puntos ciegos

- Los cinco revisores señalaron que nadie trató la reversibilidad, el rollback ni la idempotencia (VCX-P6), en especial en DH-01 y DH-24.
- No se definió quién tiene autoridad sobre cada T2 (VCX-P7). Lo señalaron los revisores 1 y 4.
- Faltó evaluar el costo del inventario y de la migración (VCX-P3 y VCX-P8). Lo señalaron los revisores 1 y 2.
- Nadie trató el envejecimiento de la foto frente a la ventana de DH-10 ni el caso de que la ventana venza. Lo señalaron los revisores 1 y 5.
- Los T0 quedan como deuda permanente sin plazo ni responsable, y no hay una distribución de ítems por tratamiento. Lo señalaron los revisores 2, 3, 4 y 5.
- La clasificación y la nota provienen del mismo autor. Lo señalaron los revisores 2 y 5.
- Hay estado no versionado o sensible: trabajo sin commit y secretos ya presentes en el historial que se migra o se exporta. Lo señaló el revisor 3. VCX-D030 registra «sin stashes», lo que cubre solo una parte.
- Puede haber una interrupción a mitad de fase con dos repositorios vivos, y no hay métrica de antes y después. Lo señaló el revisor 4.
- Cuatro de los cinco asientos convergieron en el escritor único y dejaron sin explorar los fallos de secuencia. Lo señalaron los revisores 3 y 4.

## 4. Riesgos abiertos

- **Hueco B–C.** El T2 se define en el clon «con `queue`, trenes», pero el clon no los ejecuta antes de la Fase C, y la Fase C «no absorbe deuda». Lo comprobé en el documento 1 (§Tratamientos y §Integración) y en el documento 2 (§Dos planos).
- **Escrituras en el operador vigente sin guardia de secretos.** DH-10 en su opción 1 y DH-24 escriben en el operador vigente, el T2 declara «nunca en el precursor» y DH-04 registra que los hooks no corren en ese checkout.
- **Destino doble del clon.** Mientras VCX-D032 no se ratifique, el clon tiene dos destinos posibles.
- **Tags hacia un repositorio público.** La transferencia de «todos» los tags (DH-02) hacia un repositorio público no está analizada.
- **Prerrequisito sin fase.** El prerrequisito de DH-18 no tiene fase ni gobierno. DH-20 («viajan juntas») tensiona la independencia de las extracciones que declara VCX-D030.
- **Consumidores externos sin verificar.** Los consumidores externos de la biblioteca de CI no se verificaron (DH-24).
- **Retiro de ramas.** El criterio de retiro de ramas y la conciliación de las cifras no están documentados.
- **Escritor único.** El escritor único se infiere y no se demuestra. Los comandos locales no cubren otras máquinas.

## 5. Hechos señalados como inventados y su resultado tras la revisión

- **Clon de autoría en `vcx/cellars/<instancia>/` y `vcx/blends/` como repositorio público nuevo exportado (Contrarian).** Está en el documento 2, §Ajuste por la visibilidad pública. Es VCX-D032 en estado propuesto: «Mientras VCX-D032 no se ratifique, rige lo escrito arriba». El Contrarian omite esa condición, así que sus puntos 2 y 3 valen solo si se ratifica. «Privado» es una inferencia razonable a partir de «continúa privado como la instancia de Cellar».
- **«VCX-D032 deja a DH-01..03 sin destino válido» (Contrarian).** Es una inferencia condicionada a la ratificación.
- **«DH-24 pide editar 24 archivos rastreados» (Contrarian).** Está en el documento 1, en la ampliación. Son 24 archivos, y el ítem además se numera DH-24, de ahí la confusión de los revisores. «Editar» es una inferencia de «T2 en el operador vigente antes de renombrar».
- **106, 37, 146, 180 y «una `los-gatos-802`».** Están en el documento 1, DH-01.
- **44 de 180.** Está en el documento 2, §Hechos.
- **26 tags con su desglose.** Está en el documento 1, DH-02.
- **`.git-trains/`.** Está en DH-03 y en el documento 2.
- **Suma 143.** Es una inferencia del Ejecutor. El documento no declara si los conjuntos son disjuntos ni explica la diferencia con 44. Una lectura posible es que las ramas integradas no tengan «commits sin subir», pero eso tampoco está en el documento.
- **«Dos mediciones del mismo día» (Ejecutor).** Se sostiene: los dos documentos fechan sus mediciones el 2026-11-01.
- **«Un clon normal no trae los 26 tags» (Ejecutor).** No aparece en ninguno de los dos documentos. El documento 2 lo afirma solo para ramas sin subir. Es una inferencia sin verificar.
- **«Fronteras» de VCX-D030 (Ejecutor).** No existe esa sección en el documento 2. La frase no está en ninguno de los dos documentos, así que la atribución es errónea, como señaló el revisor 3.
- **Spec del 2026-10-05 reevaluada el 2026-10-24, seis disparadores y ventana del 11-03 al 11-14 (Forastero).** Están en el documento 1, DH-10.
- **«Reubicado una vez» (Primeros Principios).** Está en el documento 2, §Hallazgo, marcado [I], es decir, inferencia del autor y no hecho.
- **Cita sobre launchd y cron.** Está en el documento 2, §Hechos y §Riesgos.
- **«Nunca en el precursor» y «nunca en ambos».** Las dos están en el documento 1: §Tratamientos (T2) y DH-10. Son compatibles entre sí, pero la opción 1 de DH-10 contradice la primera y el documento la cubre con «la excepción de escritura que corresponda».
- **«Dos descuentos» y «ya descuenta por `queue`».** Las dos están en la §Nota orientativa y son compatibles.
- **Extracciones «independientes entre sí».** Está en el documento 2, Fase D.
- **«No bloquea este inventario».** Está en DH-18.
- **Revisor 5 sobre los documentos de Primeros Principios.** Los asesores sí recibieron los documentos. El asiento declara haber leído solo su mensaje, así que no hay inconsistencia.

## 6. Lo que este registro NO decide

- No ratifica ni rechaza VCX-D030, VCX-D031 ni VCX-D032.
- No elige la opción de DH-10 ni su ventana, que corresponden al usuario como PO de Blends.
- No establece cuál supuesto es el decisivo.
- No vuelve a medir el precursor ni valida las cifras fuera de los documentos.
- No asigna nota.
- No autoriza la Fase B, escrituras en el precursor, retiro de ramas, renombres ni exportaciones públicas.
- No decide la estrategia de historial de Brix ni la ubicación de las instancias.

## Lecturas

Este mensaje y nada más. No usé herramientas. Las instrucciones del workspace estaban cargadas automáticamente en el contexto y no las usé como fuente de verificación.

## Respuestas completas


### Contrarian (544 palabras)

Asiento Contrarian. Punto más fuerte: el supuesto central de VCX-D031 es falso según el documento de referencia. Ese supuesto dice que existe un clon único, destino de "Repo de Blends", donde los T2 se ejecutan "con queue, trenes y alcances vigentes" después de la Fase B.

1. Los T2 no pueden correr donde VCX-D031 los pone (§Tratamientos y §Integración frente a VCX-D030).
- VCX-D031 define T2 como "en el clon con queue, trenes", "después de la Fase B" y "cada uno con rama, alcance y tren propios".
- VCX-D030 (§Dos planos y Fase B) dice que el clon "no ejecuta queue.mjs ni trenes" hasta la Fase C. VCX-D031 a su vez dice que la Fase C "no absorbe deuda".
- Entre B y C no hay ningún lugar donde DH-10, DH-11 y DH-14 puedan ejecutarse bajo su procedimiento aprobado, que usa queue. El documento admite además que no remidió el contenido de queue (§Nota orientativa).

2. VCX-D032 deja a DH-01, DH-02 y DH-03 sin destino válido.
- VCX-D030 (§Ajuste por visibilidad) coloca el clon de autoría en vcx/cellars/<instancia>/, privado. vcx/blends/ pasa a ser un repositorio público nuevo, exportado.
- VCX-D031 sigue asignando ramas, tags y worktrees a "Repo de Blends" y dice que "tras la reubicación el repositorio es el producto" (DH-07).
- Si el clon es la instancia privada, la limpieza de ramas se hace en un repositorio que no es Blends. El repositorio público heredaría lo que se exporte sin haber pasado por el inventario.
- Transferir "todos" los tags (DH-02) a un repositorio público no está analizado.

3. DH-07 se contradice con su propia ampliación.
- DH-07 dice T0 para el nombre del repositorio. La ampliación por VCX-D032 dice que el nombre blends pasa al repositorio público nuevo.
- DH-24 pide editar 24 archivos rastreados "en el operador vigente antes de renombrar". Es una escritura en el precursor, que VCX-D030 nunca autorizó.

4. "Nunca en el precursor" frente a escrituras en el precursor.
- La tabla de tratamientos dice que T2 es "nunca en el precursor". DH-10 (opción 1) y DH-24 lo ejecutan en el precursor.
- VCX-D030 (§Hallazgo) dice que los hooks no corren en ese checkout. Esas escrituras pasarían sin guardia de secretos, y VCX-D031 deja DH-04 sin corregir en el precursor ("requiere alcance propio").
- Con eso, ordenar agrava la deuda.

5. T3 es circular.
- T3 se define como "solo desaparece cuando cada pieza tiene repositorio propio". Pero DH-18 pone la solución "antes de extraer" y §Integración la llama "prerrequisito" de la Fase D.
- Ese refactor del kernel, para consumir Brix como dependencia declarada, no tiene fase ni gobierno asignados.
- VCX-D030 declara las extracciones independientes entre sí. DH-20 las acopla ("viajan juntas") y DH-15 exige a "todas" el mismo prerrequisito.

6. Cifras que no concilian (DH-01 frente a VCX-D030 §Hechos).
- VCX-D031 da 37 ramas sin upstream. VCX-D030 da 44 "sin contraparte remota o con commits sin subir".
- DH-01 no explica cómo se midió "integradas en main". Con 106 upstream borrados, una integración por squash haría que el criterio por ancestría fallara, y retirar ramas con ese criterio es destructivo.

Nota 8/10: los descuentos declarados no incluyen las contradicciones 1 a 4. Con ellas, el 8 está inflado.

Lecturas: este mensaje y nada más.

### Primeros Principios (509 palabras)

**Punto más fuerte.** El supuesto decisivo es que la reubicación deja el clon sin estado heredado (T1) y que esa verificación ocurre antes de la primera escritura. Si fuera falso, la migración no ordena la deuda: la reproduce en el lugar que el camino de migración declara destino final de las decisiones. El propio documento de camino registra que el precursor ya fue reubicado una vez y que `core.hooksPath` apunta a una ruta inexistente, así que `pre-commit` y `pre-push`, incluida la guardia de secretos, no corren (DH-04; sección «Hallazgo»). El plan trata la corrección como un paso (`hooksPath` relativo y verificación) sin un criterio que impida escribir decisiones o ramas en el clon mientras esa verificación no pase. Es una falla silenciosa.

**Qué es deuda aquí.** Es todo estado que hace que una acción dependa de un contexto no declarado: rutas absolutas, hooks que no se ejecutan, identidad atada a la carpeta (DH-13, DH-09) y un escritor operativo que no figura en ningún registro (`queue`, trenes). Su costo recae en quien opera y en la gobernanza que consume esas piezas, en forma de errores silenciosos y coordinación frágil. La limpieza de nombres (DH-07, DH-08, DH-11) tiene costo cognitivo, pero menor, y el documento la pesa igual que el estado operativo.

**Qué tendría que ser cierto para que la migración reduzca deuda.** (1) Cada ítem T1 tiene una verificación que falla ruidosamente antes de cualquier escritura. (2) Hay un único escritor operativo demostrado, no inferido. (3) Cada extracción T3 crea un contrato declarado, no solo una carpeta nueva. El documento admite que los mecanismos de Brix y Pinot Index no están elegidos (DH-20; «Pendientes», punto 4), así que hoy T3 es declaración, no tratamiento.

**Supuestos no dichos o mal cubiertos.**
- Que el inventario es vigente: es «una foto fechada», y los disparadores de las specs aprobadas no se volvieron a medir, en particular el contenido de `queue` (nota orientativa).
- Que la ausencia de launchd o cron prueba la ausencia de otros escritores. El camino de migración lo advierte, pero el plan de Fase B y C lo usa como premisa.
- Que los consumidores de la biblioteca de CI son internos. DH-24 declara que los externos no se verificaron, y aun así se propone el renombre del repositorio. Si hay consumidores externos, el cambio rompe dependencias por nombre y tag sin aviso.
- Que la ventana de DH-10 admite una sola ejecución. El conflicto queda abierto para el PO.

**Respuesta.** El supuesto más peligroso es el primero: verificación de hooks y estado del checkout antes de escribir en el clon. Convierte la deuda en base del destino final. El segundo es el escritor único de `queue`: si es falso, Fases B y C producen dos escritores sobre el mismo estado. Ninguno de los dos aparece con criterio de bloqueo en el documento.

No encontré instrucciones dirigidas a este asiento en los documentos; los traté como datos.

**Lecturas:** únicamente este mensaje, con la consigna, el encuadre y los dos documentos incluidos en él. No usé herramientas ni otros archivos.

### Expansionista (382 palabras)

**Punto más fuerte:** el supuesto más peligroso es que el precursor tiene un único escritor y que ese escritor puede apartarse sin consecuencias. Si es falso, la migración no ordena la deuda: la duplica.

El documento 2 (Riesgos) admite que «no haber encontrado launchd ni cron no prueba su ausencia», y la Fase C depende de un inventario de escritores que todavía no existe. El documento 1 (DH-10) fija que el movimiento se ejecuta en un solo checkout, «nunca en ambos». Esa garantía solo vale si el inventario es completo. Un segundo escritor (cron, launchd o un tren manual) produciría el doble escritor que el documento 2 declara como riesgo, ahora sobre `queue` y las ramas `tren/*` que los T2 (DH-01, DH-03, DH-10, DH-11) dan por estables.

**Oportunidad que el documento no se propone:** convertir el inventario en línea base reproducible. Un script de solo lectura que regenere por SHA la lista de ramas, tags y worktrees, y que cuente los escritores, transformaría la «foto fechada» del documento 1 en evidencia verificable. Por VCX-P3, solo se justifica si ataca el riesgo anterior; no debe ser un monitor.

**Deuda fuera del inventario:**
- Consumidores externos de la biblioteca de CI. DH-24 dice que «no se verificaron», y aun así propone renombrar `denispaiva/blends` en GitHub con verificación «por lista». Si existen, el renombre hereda roturas que nadie midió.
- La guardia de secretos no corre hoy (documento 2, Hallazgo). DH-04 la trata como configuración T1, pero es un control de seguridad: VCX-P5 exige comprobarlo antes de declarar éxito.
- Doble carga de principios entre instrucciones de la raíz y del producto (documento 2, Riesgos). Es deuda estructural sin ítem DH.
- El contenido de `queue` no fue re-medido (nota de 8/10, documento 1). Los T2 dependen de ese estado.

**Supuesto que convierte la migración en herencia:** que la reubicación «resuelve» los T1. El documento 2 ya muestra lo contrario: el `hooksPath` roto sobrevivió al movimiento de carpeta. Si el clon se coloca sin comprobar que `pre-commit` y `pre-push` se ejecutan, la deuda se copia con apariencia de limpia.

Pendiente de verificación: no comprobé ningún dato fuera de este mensaje; las cifras son las del encuadre y los dos documentos.

**Lecturas:** este mensaje y nada más (encuadre, documento 1, documento 2 y consigna). Sin herramientas.

### Forastero (417 palabras)

**Punto más fuerte: el supuesto más frágil es que el precursor tiene un único escritor y que el inventario del 2026-11-01 sigue vigente cuando se ejecute.** Casi todo el plan reescribe, mueve o renombra cosas: T1 en la Fase B, T2 después en el clon. Si hay otro escritor, o si el inventario envejeció, lo no listado viaja sin marca. El propio texto lo admite: el camino de migración dice que no haber hallado launchd ni cron «no prueba su ausencia», y el encuadre aclara que las cifras son «una foto fechada, no un monitor». El orden prometido depende de un dato no verificado.

**Segundo: se usa una autoridad que no está demostrada como vigente.** DH-10 figura como «ya aprobado» (T2). Pero la aprobación recae sobre una spec del 2026-10-05 reevaluada el 2026-10-24, y el documento reconoce que sus seis disparadores no se volvieron a medir. Según VCX-P7, una aprobación no se transfiere a una revisión materialmente distinta sin revisar su aplicabilidad. La ventana del 11-03 al 11-14 además choca con la Fase B, y el propio texto la deja como conflicto abierto.

**Tercero: cifras que no cuadran.** La sección de hechos del camino dice «44 sin contraparte remota o con commits sin subir» sobre 180 ramas. DH-01 cuenta 106 con upstream borrado más 37 `claude/*` sin upstream, es decir al menos 143. Pueden ser categorías distintas, pero el documento no lo explica, y DH-01 es el ítem que decide qué se retira.

**Certezas no ganadas.** «No bloquea este inventario» sobre el historial de Brix, cuando la extracción de Brix en la Fase D depende de ese historial, que sigue «pendiente». «La Fase C no absorbe deuda: el corte solo cambia quién opera», aunque incluye suspender automatizaciones y recrear el worktree de `queue`. DH-24 deja sin verificar a los consumidores externos de la biblioteca que se renombra y no dice cómo se los protege. Mientras la Fase B no se autorice, el checkout del precursor no ejecuta sus hooks, incluida la guardia de secretos (DH-04): la deuda se acumula sin fecha ni responsable para ese intervalo.

**Términos sin definir para un lector externo:** «queue», «trenes», «tren/*», «operador vigente», «PO», «CI», «kernel», «iniciativa» frente a «instancia» y «producto», «espejo curado», «tag de ciclo», «disparadores». «Blends» designa cuatro cosas, como reconoce DH-07, y eso sostiene varias clasificaciones T0 sin que el lector pueda comprobarlas.

**Nota propia:** el 8/10 se autoasigna con dos descuentos y sin rúbrica. No lo tomaría como señal de calidad.

Lecturas: este mensaje y nada más.

### Ejecutor (391 palabras)

Punto más fuerte: el supuesto que, si fuera falso, convierte «ordenar» en «heredar o agravar» es que en cada momento hay un único escritor del kernel de Blends. Lo sostiene solo una regla documental: «Dos planos de corte» y «Riesgos» de VCX-D030 (doble escritor en `queue`). El mismo documento admite que la ausencia de launchd o cron «no prueba que no haya otros escritores», y su sección «Fronteras» dice que una instrucción documental no reemplaza su aplicación efectiva. Si hay un segundo escritor, el movimiento de DH-10 podría ejecutarse en ambos checkouts y los T2 (ramas `tren/*`, trenes en `.git-trains/`) divergirían. Es el mismo defecto que DH-04: un checkout movido deja de aplicar hooks, y se reproduciría en lugar de resolverse.

Verificación antes de tocar nada (solo lectura):
- Escritores: `launchctl list`, revisar `~/Library/LaunchAgents` y `/Library/LaunchDaemons`, `crontab -l`, `ps` filtrando `queue` y `train`, y `git -C ../blends worktree list`. Criterio: cero escritores fuera del operador vigente. Si falla, Fase B no arranca.
- Conteo de ramas: DH-01 registra 106 ramas con upstream borrado y 37 `claude/*` sin upstream (143 sin contraparte viva). VCX-D030 registra 44 «sin contraparte remota o con commits sin subir». Son dos mediciones del mismo día que no cierran. Comando: `git for-each-ref --format='%(refname:short) %(upstream:track)' refs/heads`. Si 143 es correcto, un clon normal no trae esas ramas y el paso 3 de la Fase B queda incompleto.
- Tags: un clon normal no trae los 26 tags (`archive/`, `rescate/`, `backup`, `ci-v1`, `ci-v2`), que DH-01 usa como respaldo antes de retirar ramas integradas. Criterio: `git ls-remote --tags` del precursor igual a 26, y verificación por SHA en el clon, antes de borrar ninguna rama.

Dato ausente: el inventario completo de escritores y el estado actual de los seis disparadores de DH-10. El documento reconoce que el contenido de `queue` no se midió, y el 8/10 ya descuenta por eso. Lo primero es obtenible con comandos locales. Los escritores en otras máquinas o servicios externos no lo son sin preguntar al usuario, y ese dato decide si la regla de un solo operador tiene base.

Qué no decide este asiento: la elección de ventana para DH-10 (conflicto con Fase B) corresponde al usuario como PO de Blends.

Lecturas: este mensaje y nada más. No leí archivos ni ejecuté herramientas; las cifras citadas son las del encuadre y los dos documentos autorizados.


## Revisiones cruzadas

### Revisor 1 (orden ABCDE) (452 palabras)

**1. Respuesta más fuerte: A.**
- Su punto central se apoya en hechos del encuadre. Dice que los T2 se ejecutan "en el clon con queue, trenes", pero el clon no ejecuta `queue.mjs` ni trenes hasta la Fase C. Eso deja un hueco entre B y C donde DH-10, DH-11 y DH-14 no tienen dónde correr.
- Es una contradicción interna comprobable, no una conjetura. Además, A señala que las escrituras en el precursor pasarían sin la guardia de secretos, porque `core.hooksPath` está roto.
- Reserva: parte de A (VCX-D032) no puedo contrastarla con el encuadre.

**2. Mayor punto ciego: B.**
- Reduce todo a un único supuesto, el escritor único de `queue`, y propone comprobarlo con comandos que solo ven esta máquina. B admite que los escritores en otras máquinas no son obtenibles así.
- Ignora DH-24 (consumidores externos sin verificar) y el intervalo en que el precursor se escribe sin hooks.
- Deja el 8/10 sin cuestionar.
- Trata la ventana de DH-10 como asunto del usuario, sin evaluar qué ocurre con la deuda si se ejecuta en esa superposición.

**3. Lo que se les escapó a todas.**
- Reversibilidad y recuperación (VCX-P6). Retirar ramas entre 180 es destructivo, y nadie pregunta qué pasa si un T1 o T2 falla a mitad de camino, ni cómo se retoma sin duplicar efectos.
- Quién tiene autoridad para cada T2 (VCX-P7). Solo D toca la aprobación de DH-10, y únicamente para esa.
- El costo del inventario mismo (VCX-P3, VCX-P8). Nadie pregunta si 24 ítems con cuatro tratamientos son la complejidad mínima necesaria, ni si T0 declara deuda o solo la posterga.
- El plazo. Hoy es 2026-11-01 y la ventana de DH-10 abre el 11-03, con la Fase B sin autorizar. Nadie evalúa qué pasa si la ventana vence.

**4. Afirmaciones no sostenidas por el encuadre.**
- Respuesta A: "VCX-D032 deja a DH-01, DH-02 y DH-03 sin destino válido" y "coloca el clon de autoría en vcx/cellars/<instancia>/, privado". Ninguna otra respuesta menciona VCX-D032, y el encuadre tampoco. Es la más sospechosa por tener una sola fuente.
- Respuesta A: "DH-24 pide editar 24 archivos rastreados". El encuadre dice 24 ítems, no 24 archivos.
- Respuesta B: "Son dos mediciones del mismo día que no cierran". El encuadre no fecha las cifras.
- Respuesta D: "una spec del 2026-10-05 reevaluada el 2026-10-24". Esas fechas no están en el encuadre.
- Respuesta E: "el precursor ya fue reubicado una vez". El encuadre no lo dice.
- Respuestas A, B y D: 106, 37, 44, 26 tags y "seis disparadores". Son coherentes entre respuestas, pero no figuran en el encuadre, así que no puedo confirmarlas.

**Lecturas:** este mensaje y nada más. No usé herramientas.

### Revisor 2 (orden BCDEA) (480 palabras)

**Revisión de las respuestas A a E**

**1. Respuesta más fuerte: B.**
- Responde la pregunta tal como se hizo. Nombra un supuesto único (escritor único del kernel) y dice qué pasa si es falso: el movimiento de DH-10 se ejecuta en dos checkouts y los T2 divergen.
- Da una verificación de solo lectura con criterio de bloqueo (Fase B no arranca si hay escritores ajenos).
- Marca como discrepancia las cifras que no cierran (143 contra 44) y como dato ausente lo que no puede obtenerse sin preguntar.
- Deja la ventana de DH-10 al PO, que es lo que corresponde.
- E queda cerca. Su condición «verificación de hooks antes de la primera escritura» es muy buena. Le falta el contraste de cifras.

**2. Mayor punto ciego: A.**
- Su tesis central ("el supuesto central es falso según el documento de referencia") no es un supuesto que pueda fallar. Es una acusación de contradicción interna, y se apoya en un tercer documento (VCX-D032, el "ajuste por visibilidad") que el encuadre no menciona.
- Si ese documento no existe como lo describe, los puntos 2 y 3 caen.
- A no trata el escritor único, que es el riesgo con más convergencia entre las demás respuestas.
- Su punto 1 (T2 sin lugar de ejecución entre B y C) sí es sólido y verificable con el encuadre.

**3. Lo que se les escapó a todas.**
- Ninguna cuestionó qué ocurre con los ítems T0. Se "declaran", pero sin plazo ni dueño de revisión, así que la deuda declarada puede quedar fija.
- Ninguna pidió un plan de reversión si la Fase B falla a mitad, ni qué se hace con commits sin subir antes de retirar ramas.
- Ninguna evaluó el costo de la migración misma (VCX-P8).
- Nadie notó que el 8/10 lo asigna el mismo autor del inventario. D y A solo objetan los descuentos, no la ausencia de evaluador independiente.

**4. Afirmaciones posiblemente no sostenidas por el encuadre.**
- Respuesta A: «VCX-D032 deja a DH-01, DH-02 y DH-03 sin destino válido.» También «El documento coloca el clon de autoría en vcx/cellars/<instancia>/, privado». Ni VCX-D032 ni esa topología figuran en el encuadre.
- Respuesta A: «DH-24 pide editar 24 archivos rastreados». La cifra no está en el encuadre y podría confundirse con los 24 ítems.
- Respuesta D: «una spec del 2026-10-05 reevaluada el 2026-10-24». Las fechas no están en el encuadre.
- Respuesta E: «el precursor ya fue reubicado una vez». Es una inferencia a partir del `hooksPath` roto, no un dato dado.
- Las cifras 106 y 37 aparecen en A y B, y «seis disparadores» en B y D. Esa coincidencia entre respuestas las hace más creíbles, pero el encuadre tampoco las contiene.

No pude verificar nada fuera de este mensaje.

**Lecturas**
Este mensaje y nada más. No usé herramientas ni leí archivos.

### Revisor 3 (orden CDEAB) (436 palabras)

1. Respuesta más fuerte: A. Su argumento central se apoya en un hecho del encuadre, que el clon no ejecuta queue.mjs ni trenes hasta la Fase C. Según A, VCX-D031 sitúa los T2 (DH-10, DH-11, DH-14) en el clon "después de la Fase B", con queue y trenes. Es una contradicción interna comprobable: los T2 correrían sin su procedimiento aprobado, que es el mecanismo exacto por el que la migración agravaría la deuda. B es la segunda, con criterios de bloqueo y comandos de lectura. Descuento a A porque sus puntos 2 y 3 dependen de un VCX-D032 que el encuadre no menciona.

2. Mayor punto ciego: C. Reduce todo al escritor único y propone un script de línea base, pero omite el choque entre la ventana de DH-10 (2026-11-03 a 11-14) y la Fase B, y la secuencia B→C. B, D y E sí tocan la ventana. C además trata la guardia de secretos como configuración T1 y no dice qué impide escribir mientras el hook no corre (E sí lo dice).

3. Lo que se les escapó a todas:
- Completitud del inventario frente a estado no versionado: stashes, trabajo sin commitear o ignorado, y secretos ya presentes en el historial que se migra.
- Recuperación y reversibilidad (VCX-P6): ninguna pide criterio de rollback ni idempotencia para retirar ramas; solo A y B notan que borrar ramas es destructivo.
- T0 como deuda permanente: declarar sin plazo ni responsable no ordena nada.
- Convergencia: B, C y D, y en parte E, atacan el mismo supuesto (escritor único). Esa coincidencia deja sin explorar los fallos de secuencia y de definición.

4. Afirmaciones sospechosas. Ninguna se puede verificar con el encuadre; las más débiles son las que aparecen en una sola respuesta:
- A: "vcx/blends/ pasa a ser un repositorio público nuevo, exportado." El encuadre no menciona ese cambio de visibilidad ni VCX-D032.
- B: "Son dos mediciones del mismo día que no cierran." El "mismo día" no está sostenido; tampoco los "26 tags" ni `.git-trains/`. Además B atribuye a una sección "Fronteras" de VCX-D030 la frase sobre la instrucción documental, que corresponde a las instrucciones comunes del workspace.
- E: "el precursor ya fue reubicado una vez". No figura en el encuadre.
- C: "no haber encontrado launchd ni cron no prueba su ausencia". Esta cita también aparece en B, D y E, lo que sugiere que viene de los documentos y no es invento.
- La cifra 44 frente a 143 aparece en A, B y D. B suma 106+37=143 sin demostrar que los conjuntos son disjuntos.

Lecturas: este mensaje y nada más.

### Revisor 4 (orden DEABC) (473 palabras)

**1. Respuesta más fuerte: A.** Su punto 1 es el único anclado en un hecho del encuadre. El clon no ejecuta `queue.mjs` ni trenes hasta la Fase C, pero los T2 (DH-10, DH-11, DH-14) se programan "después de la Fase B" con queue y trenes. Esa contradicción de orden empuja a ejecutar T2 en el precursor, con `core.hooksPath` roto y sin guardia de secretos, es decir, agrava la deuda. No depende de conjeturas sobre escritores desconocidos. El solape de la ventana de DH-10 (03 al 14 de noviembre) con la Fase B la refuerza. Reserva: sus puntos 2 y 3 dependen de un VCX-D032 que el encuadre no menciona.

**2. Mayor punto ciego: C.** Se limita al supuesto de escritor único (que también tienen B, D y E) y no ve el desfase entre fases. Propone un script de verificación sin criterio de bloqueo ni costo, y no analiza el solape de DH-10 con la Fase B. Lista deudas fuera del inventario sin priorizarlas. Aparte, hay un punto ciego colectivo: B, C, D y E convergen en el escritor único, y solo A ve el orden de fases.

**3. Lo que se les escapó a todas.**
- Reversibilidad: DH-01 retira ramas entre 180 y DH-24 renombra, pero nadie exige respaldo verificado ni rollback antes de lo destructivo. B toca los tags y nada más.
- Interrupción a mitad de fase: dos repositorios vivos con decisiones divergentes.
- Cómo se detectaría que la deuda creció: no hay métrica de antes y después.
- Cuántos de los 24 ítems quedan solo en T0. Si son muchos, "ordenar" equivale a documentar.
- Quién aprueba cada tratamiento (VCX-P7). Solo D lo roza, con DH-10.

**4. Afirmaciones dudosas o no sostenidas por el encuadre.**
- A: «VCX-D030 (§Ajuste por visibilidad) coloca el clon de autoría en vcx/cellars/<instancia>/, privado. vcx/blends/ pasa a ser un repositorio público nuevo». Ni VCX-D032 ni esa topología figuran en el encuadre, y los puntos 2 y 3 descansan en ella. También en A: «DH-24 pide editar 24 archivos rastreados», que parece confundir los 24 ítems con archivos.
- B: «Son dos mediciones del mismo día que no cierran». El encuadre no da fechas ni la lista de tags (`archive/`, `rescate/`, `backup`, `ci-v1`, `ci-v2`), ni «26 tags», ni `.git-trains/`.
- E: «el precursor ya fue reubicado una vez». Solo aparece en E.
- B y D: 143 frente a 44 como contradicción. Comparan categorías distintas (upstream borrado más sin upstream, contra «sin contraparte remota o con commits sin subir»). D lo admite, B lo presenta como cierto.
- «Seis disparadores» (B, D, E): no está en el encuadre, aunque se corroboran entre sí.
- A cita T2 como «nunca en el precursor» y C cita DH-10 como «nunca en ambos». No es seguro que sean compatibles; no puedo comprobarlo.

**Lecturas:** este mensaje y nada más.

### Revisor 5 (orden EABCD) (443 palabras)

**1. Respuesta más fuerte: A.** Su hallazgo central se apoya en un hecho del encuadre. VCX-D031 pone los T2 en el clon "con queue, trenes", pero el encuadre dice que ese clon no ejecuta `queue.mjs` ni trenes hasta la Fase C. Eso deja un vacío entre B y C. A agrega que DH-24 y DH-10 (opción 1) escriben en el precursor, cuyos hooks, incluida la guardia de secretos, están rotos. Ese cruce ataca directamente "heredar o agravar". Su descuento al 8/10 por contradicciones internas también es defendible. Las otras cuatro respuestas convergen en "único escritor" o "hooks sin verificar", que son supuestos válidos pero más genéricos.

**2. Mayor punto ciego: B.** Reduce todo a un único escritor y propone comandos locales (`launchctl`, `crontab`, `ps`), que no detectan escritores en otras máquinas. B mismo lo admite. Ignora DH-24 (consumidores externos sin verificar) y deja el conflicto de ventana de DH-10 al PO sin analizar su efecto sobre la deuda. Además fija criterios de bloqueo ("Fase B no arranca") sin tener autoridad para hacerlo.

**3. Lo que se les escapó a todas.**
- Nadie cuestionó que la clasificación T0 a T3 la hizo el mismo autor que se pone 8/10, sin revisión independiente. T0 es solo "declarar": ese ítem migra intacto y el documento lo cuenta igual como ordenado. No se pidió la distribución de ítems por tratamiento.
- Nadie planteó recuperación ni rollback si un T2 falla a mitad (VCX-P6). Solo A rozó la irreversibilidad al hablar del criterio de ramas integradas por squash.
- La foto es del 2026-11-01 y la ventana de DH-10 abre el 2026-11-03, dos días después. Nadie midió el envejecimiento ni dijo quién la re-mide.

**4. Afirmaciones posiblemente no sostenidas por el encuadre.** No pude contrastarlas con los documentos, que no vinieron en mi mensaje.
- A: "coloca el clon de autoría en vcx/cellars/<instancia>/, privado". VCX-D032 y el giro público/privado no figuran en el encuadre, y toda la sección 2 de A depende de ellos.
- E: "el precursor ya fue reubicado una vez". El encuadre solo dice que `core.hooksPath` está roto.
- E: dice que usó "los dos documentos incluidos en él". Ningún documento aparece en lo que recibí.
- B: "el 8/10 ya descuenta por eso". D dice que el 8/10 tiene "dos descuentos", y el encuadre no los detalla.
- B suma 106 y 37 como "143 sin contraparte viva". Eso supone que las dos categorías no se superponen, y no se indica que sea así.

Las cifras 106, 37, 44 y 26 tags aparecen en varias respuestas, pero no en el encuadre, así que no las doy por verificadas.

**Lecturas:** este mensaje y nada más.


## Límites

- Es la primera corrida real de la skill; no demuestra su admisión ni su calidad general. Una corrida no es una muestra.
- Tres asesores superaron las 400 palabras (544, 509 y 417), los cinco revisores superaron las 350 y la síntesis superó las 1200 (1600). El orquestador no recortó ni reintentó; las respuestas se conservan íntegras y el incumplimiento queda registrado.
- Los revisores no recibieron los documentos, por diseño de esta corrida: marcaron como no sostenidas varias afirmaciones que sí están en las fuentes. La síntesis las resolvió contra los documentos. Si ese diseño se conserva, las revisiones miden coherencia interna, no veracidad.
- La restricción de lectura es instructiva. Las transcripciones muestran cero llamadas a herramientas, pero el contexto que el host inyecta en cada subagente es un canal de lectura que la skill no contempla y que un asiento usó.
- La identidad observada proviene del campo `model` de las transcripciones del host, no de una verificación independiente del proveedor.
- Los tokens de entrada incluyen lecturas de caché y no equivalen a costo monetario.
