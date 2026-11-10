# Reconsideración arquitectónica por eventos en proyectos graduados

Fecha: 2026-11-02. Estado: **propuesta del asistente**, registrada como VCX-D040 en el [registro de decisiones](../../decisions/README.md), sin ratificar. Autoridad: en el chat con Claude del 2026-11-02, a «¿Redacto la propuesta VCX-D de reconsideración arquitectónica con los cinco elementos?» el usuario respondió «Sí, redactala». Autoriza redactar y registrar la propuesta. No autoriza ratificarla, escribir en `../blends`, adoptar herramientas ni corregir la numeración de ADR existentes. El usuario autorizó después el commit `fcc3bce`. Revisión del mismo día, tras una revisión pegada en el chat que la mantuvo propuesta: el disparador cubre cambios anunciados y supuestos implícitos, un reemplazo queda propuesto hasta su aceptación, la independencia depende del riesgo del trabajo actual y la autoridad se limita a cada ámbito.

Etiquetas: [H] hecho medido el 2026-11-02 en solo lectura; [D] hecho documentado en una fuente que se enlaza o identifica; [I] interpretación; [P] propuesta; [U] dicho por el usuario.

## 1. Problema

[H] En las fuentes revisadas no se encontró un procedimiento que, después de graduar, conecte un cambio de supuestos con una evaluación de la arquitectura vigente y su resultado. La búsqueda, acotada a VCX y al precursor en la revisión `f86a2a7d`, buscó «revisión de arquitectura», «ciclo de arquitectura» y equivalentes. No demuestra que no exista en otra fuente.

[D] Lo que sí existe:

- En el tramo de idea, cambiar arquitectura, carga, tarifas o período exige actualizar FinOps y revisar si la aprobación sigue cubriendo el escenario ([arquitectura y FinOps](https://github.com/denispaiva/blends/blob/main/docs/architecture-and-finops.md#autorización-y-cambios)).
- En el precursor, `vc/docs/standards/work-proportionality.md` fija cuándo documentar: sin ADR en N1; ADR en N2 solo si la decisión ata trabajo futuro; decision record obligatorio en N3. Dice cuándo registrar una decisión, no cuándo reconsiderarla. Es referencia de consulta según [AGENTS](../../../AGENTS.md#fronteras), no regla vigente en VCX hasta conciliar por VCX-D011.
- La [matriz](../../architecture/responsibility-matrix.md#1-método-y-conducción) asigna el método a Blends y la conducción del proyecto graduado a Cellar con su PO.

## 2. Alcance

[P] Aplica a la arquitectura vigente de un proyecto con `lifecycleState` `graduated` ([modelo de iniciativa](https://github.com/denispaiva/cellar/blob/main/docs/initiative-model.md#estados-y-relaciones)). El tramo de idea sigue rigiéndose por [arquitectura y FinOps](https://github.com/denispaiva/blends/blob/main/docs/architecture-and-finops.md); esta propuesta no lo modifica.

Fuera de alcance: el formato de los ADR, la adopción de herramientas, la numeración heredada, las revisiones periódicas y su aplicación a los productos del grupo A (§7).

## 3. Regla propuesta

### 3.1 Disparadores

[P] Se reconsidera la arquitectura cuando hay **evidencia fechada y con fuente que cuestiona la vigencia actual o futura de un supuesto relevante** de la arquitectura vigente, declarado o implícito, o cuando **cambia, o se anuncia que cambiará, una frontera** que esa arquitectura fija. Un supuesto es relevante si su incumplimiento cambiaría la viabilidad, la elección entre alternativas o un contrato. Un cambio anunciado y todavía no efectivo alcanza: el retiro programado de un servicio dispara la evaluación al anunciarse, no cuando deja de funcionar. Ejemplos, no exhaustivos:

| Clase | Ejemplos |
|---|---|
| Supuesto cuestionado | Carga, volumen de datos o latencia fuera del rango supuesto, o una tendencia medida que lo superará; fin de soporte, cambio de licencia o retiro de un servicio del que depende, ya efectivo o anunciado; requisito nuevo de seguridad, privacidad o regulación, vigente o con fecha de entrada en vigor |
| Cambio de frontera | Aparece o se compromete un segundo consumidor de un componente, como en el ADR 0008 de Brix del precursor; se extrae un repositorio; cambia un contrato público |
| Riesgo | Una decisión de nivel N3 toca la arquitectura: secretos, permisos, datos, migraciones o publicación |
| Incidente | Un incidente cuya causa identificada es arquitectónica |
| Pedido | El PO lo solicita con un motivo |

[P] **Tarifas y costos.** Un cambio de tarifa exige actualizar FinOps y comprobar la cobertura del presupuesto. Solo dispara una reconsideración si afecta la viabilidad del proyecto o la elección entre alternativas de arquitectura.

[P] No son disparadores una preferencia, la novedad de una herramienta ni una desviación aislada sin evidencia. Proponer una alternativa sigue siendo posible; no obliga a evaluar.

[I] La regla funciona mejor si la arquitectura vigente declara sus supuestos, pero no lo exige: un supuesto implícito también puede quedar cuestionado. En ese caso, la reconsideración lo declara a partir del disparador. No se exige reconstruir los supuestos de los proyectos existentes antes de que ocurra uno (VCX-P3: la deuda heredada se declara, no se corrige por migración implícita).

### 3.2 Qué se registra

[P] Cada reconsideración registra cinco elementos:

| Elemento | Contenido |
|---|---|
| Disparador | Qué evidencia cuestiona la vigencia actual o futura de un supuesto relevante, o qué frontera cambia o se anuncia que cambiará, con fuente y fecha |
| Evaluador | Quién evaluó y con qué alcance; si es un agente, quién lo encargó |
| Resultado y fundamento | La conclusión del evaluador: la arquitectura **sigue adecuada**, conviene **ajustarla** o conviene **reemplazarla**, con la evidencia que lo sostiene y lo que no pudo verificarse. Es una recomendación hasta que la autoridad la acepte |
| Revisión evaluada | Sobre qué revisión de la arquitectura, del modelo de referencia y de FinOps se evaluó |
| Autoridad | Quién autoriza cada consecuencia según su ámbito (§3.4) y qué no queda autorizado, o «sin acciones que autorizar» cuando la conclusión no requiere ejecutar nada |

[P] «Sigue adecuada» también se registra: sin ese registro no hay evidencia de que la evaluación ocurrió ni de contra qué revisión.

### 3.3 Dónde se registra, proporcional al resultado

[P] Para no crear un archivo por evaluación:

- **Sigue adecuada**, o un ajuste que no ata trabajo futuro y no es N3: una entrada fechada con los cinco elementos en una sección «Reconsideraciones» al final del ADR de arquitectura vigente. La sección solo agrega entradas; no altera la decisión aceptada, que conserva su historia (VCX-P7).
- **Ajuste que ata trabajo futuro o es N3:** una decisión complementaria, en un ADR nuevo que enlaza al vigente sin sustituirlo. El vigente sigue rigiendo en lo que el complemento no cambia.
- **Reemplazo recomendado:** un ADR nuevo en estado propuesto, enlazado en ambos sentidos con el vigente. El vigente conserva su estado mientras la autoridad no acepte la sustitución. Si la acepta, el nuevo pasa a aceptado y el anterior a sustituido; si la rechaza, el nuevo queda rechazado con su fundamento. En ningún caso se reutiliza un número.

### 3.4 Evaluación y autoridad

[P] Siguiendo la [matriz](../../architecture/responsibility-matrix.md#4-matriz-raci-humana-propuesta):

| Rol | Quién |
|---|---|
| R · prepara y evalúa | Equipo del proyecto, o un agente con alcance explícito. Quien escribió la arquitectura vigente puede preparar la evaluación y aportar contexto |
| A · autoriza las consecuencias | Según el ámbito de cada consecuencia, como fija la matriz: el PO dentro de su proyecto; el responsable del portfolio para presupuesto o prioridades del portfolio; el responsable de otro producto, de un contrato público o de controles compartidos para lo que toque ese ámbito |
| C · consultado | Brix, con sus instrumentos de arquitectura de referencia y FinOps; responsables de dependencias afectadas |
| I · informado | PO del proyecto cuando no es A; responsable del portfolio |

[P] **Límites de autoridad.** Que una consecuencia afecte otro producto, un contrato o un control compartido no da autoridad sobre él al PO ni al responsable del portfolio: pueden pedir el cambio, no autorizarlo. Una consecuencia sin autoridad identificada queda pendiente, no autorizada.

[P] **Independencia proporcional al riesgo.** Preparar, evaluar y verificar son pasos distintos (VCX-P5). Si el trabajo actual es N3, sea por el disparador o por las consecuencias que recomienda, la conclusión la verifica alguien que no la preparó. Nadie verifica una evaluación que preparó; haber escrito la arquitectura vigente no excluye por sí solo de ningún paso.

[P] Evaluar no autoriza ejecutar: un agente puede ser R o C, nunca A, y una conclusión favorable no es aprobación (VCX-P7).

### 3.5 Reparto

[I] Coincide con la matriz: Blends define esta regla como parte del método, Cellar la aplica en cada proyecto con su PO y Brix aporta los instrumentos de evaluación.

## 4. Transición

- [P] **Dónde vive la regla.** En el registro raíz con clasificación «Blends», pendiente de traslado al repositorio de Blends, como fija el [mapa](../../architecture/repository-map.md#destino-de-las-decisiones-durante-la-transición).
- [D] **Dónde se escriben las reconsideraciones.** En `docs/decisions` de cada proyecto (VCX-D030). Para los proyectos del precursor ese destino está bloqueado hasta el clon de autoría.
- [P] **Mientras tanto.** Si ocurre un disparador antes del clon, la reconsideración se prepara como propuesta y se escribe cuando el destino exista, o mediante una excepción de escritura registrada como VCX-D027. No se escribe en la raíz: `vcx` es público y los proyectos son privados por VCX-D032.
- [P] **Sin retroactividad.** Los proyectos graduados no deben evaluarse ahora; la regla se aplica desde el primer disparador posterior a su ratificación.

## 5. Alternativas consideradas

| Alternativa | Por qué no se elige |
|---|---|
| Revisión periódica por calendario | Tiene costo fijo y no hay hoy una necesidad que lo justifique. VCX-P3 no la prohíbe: puede adoptarse si aparece esa necesidad |
| Solo la proporcionalidad N1–N3 | Dice cuándo documentar una decisión, no cuándo reconsiderar una ya tomada |
| Adoptar `skillrecordings/adr-skill` | [H] Sin licencia declarada; es una herramienta de redacción y no define disparadores, evaluador ni autoridad |
| Tomar como base `Alexandre-LPZ/avant-garde` o el ADR-0003 de `devantler-tech/agent-plugins` | [H] Ninguno cubre la reconsideración posterior. Se conservan como antecedentes: preguntas de verificación y un juez distinto del autor en el primero; contrato de configuración con fallo cerrado ante configuración ausente en el segundo |
| **Disparadores por evento con registro de cinco elementos** | Recomendada |

Nota orientativa según VCX-P2: 7 de 10. Descuentos: dos puntos porque no se probó todavía sobre un caso, incluidos los contraejemplos de §6; un punto porque «supuesto relevante» y «evidencia que cuestiona» dejan margen de juicio, sobre todo con supuestos implícitos. No se descuenta por la falta de un control ejecutable: primero habría que demostrar que aporta valor proporcional. No es aprobación ni medición objetiva.

## 6. Verificación

Criterios observables para aceptar la regla, a comprobar con un caso sintético antes de ratificarla:

1. Un disparador de la clase Supuesto cuestionado produce un registro con los cinco elementos.
2. **Cambio anunciado, todavía no efectivo:** el proveedor anuncia el cierre futuro de un servicio que hoy funciona, sin cambio de frontera. La regla dispara la evaluación al anunciarse.
3. Un cambio de tarifa sin efecto sobre la viabilidad ni sobre la elección entre alternativas produce solo la actualización de FinOps.
4. Una conclusión «sigue adecuada» deja una entrada en «Reconsideraciones» con la revisión evaluada y «sin acciones que autorizar».
5. **Reemplazo recomendado, no aprobado:** el ADR nuevo queda propuesto y el vigente conserva su estado. Solo la aceptación de la autoridad marca el anterior como sustituido; ningún número se reutiliza.
6. Un ajuste que ata trabajo futuro produce una decisión complementaria y no sustituye al ADR vigente.
7. Una consecuencia sobre otro producto, un contrato público o un control compartido identifica como A a la autoridad de ese ámbito, no al PO del proyecto.
8. Ningún registro presenta a un agente como A ni trata una conclusión como autorización, y en trabajo N3 quien verifica no es quien preparó la evaluación.

[D] Recorrido de escritorio del 2026-11-02, pegado en el chat por el usuario, sobre un caso ficticio (arquitectura A1, modelo M1, FinOps F1, ADR 0010 aceptado): siete criterios conformes y el 1 parcial, porque el campo Disparador de §3.2 conservaba la redacción anterior. Encontró además que un ajuste N3 que no ata trabajo futuro, como una intervención temporal sobre permisos que luego restaura la configuración, encajaba en dos destinos de §3.3. Ambos puntos se corrigieron. Es una comprobación de escritorio, no evidencia de aplicación real.

Contraejemplo adicional a buscar en esa prueba: un disparador real que no encaje en ninguna clase. Si aparece, la condición general de §3.1 debe cubrirlo; si no lo cubre, la regla se corrige antes de ratificarse.

## 7. Pendientes separados

- **Numeración de ADR heredada.** Brix tiene dos `0007` y Pinot Index dos `0001` en el precursor, y `conventions.md` pide `ADR-NNN-kebab-case.md` mientras los archivos usan `NNNN-kebab.md`. El [inventario de deuda heredada](2026-11-01-inherited-debt-design.md) no lo registra. Se trata aparte, conservando referencias e historia; no bloquea esta regla.
- **Productos del grupo A.** Decidir si la regla se aplica a Blends, Brix y Cellar como proyectos, con su responsable como A según la matriz.
- **Formato del ADR.** MADR, una plantilla propia o una skill, con admisión en la [matriz de tooling](../../architecture/tooling-matrix.md).
- **Primer caso.** Un documento de arquitectura de referencia en preparación, como el que otra sesión redactaba para Teyst al escribir esta spec, podría ser el primero en declarar sus supuestos explícitamente; no se asume que lo haga.
