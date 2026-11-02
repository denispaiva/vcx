# Reconsideración arquitectónica por eventos en proyectos graduados

Fecha: 2026-11-02. Estado: **propuesta del asistente**, registrada como VCX-D040 en el [registro de decisiones](../../decisions/README.md), sin ratificar. Autoridad: en el chat con Claude del 2026-11-02, a «¿Redacto la propuesta VCX-D de reconsideración arquitectónica con los cinco elementos?» el usuario respondió «Sí, redactala». Autoriza redactar y registrar la propuesta. No autoriza ratificarla, escribir en `../blends`, adoptar herramientas, corregir la numeración de ADR existentes ni commitear.

Etiquetas: [H] hecho medido el 2026-11-02 en solo lectura; [D] hecho documentado en una fuente que se enlaza o identifica; [I] interpretación; [P] propuesta; [U] dicho por el usuario.

## 1. Problema

[H] Después de graduar no hay un procedimiento que conecte un cambio de supuestos con una evaluación de la arquitectura vigente y su resultado. La búsqueda acotada en VCX y en el precursor, revisión `f86a2a7d`, no encontró «revisión de arquitectura», «ciclo de arquitectura» ni equivalentes. Una búsqueda acotada no demuestra que no exista en ninguna otra fuente.

[D] Lo que sí existe:

- En el tramo de idea, cambiar arquitectura, carga, tarifas o período exige actualizar FinOps y revisar si la aprobación sigue cubriendo el escenario ([arquitectura y FinOps](../../../blends/docs/architecture-and-finops.md#autorización-y-cambios)).
- En el precursor, `vc/docs/standards/work-proportionality.md` fija cuándo documentar: sin ADR en N1; ADR en N2 solo si la decisión ata trabajo futuro; decision record obligatorio en N3. Dice cuándo registrar una decisión, no cuándo reconsiderarla. Es referencia de consulta según [AGENTS](../../../AGENTS.md#fronteras), no regla vigente en VCX hasta conciliar por VCX-D011.
- La [matriz](../../architecture/responsibility-matrix.md#1-método-y-conducción) asigna el método a Blends y la conducción del proyecto graduado a Cellar con su PO.

## 2. Alcance

[P] Aplica a la arquitectura vigente de un proyecto con `lifecycleState` `graduated` ([modelo de iniciativa](../../../cellar/docs/initiative-model.md#estados-y-relaciones)). El tramo de idea sigue rigiéndose por [arquitectura y FinOps](../../../blends/docs/architecture-and-finops.md); esta propuesta no lo modifica.

Fuera de alcance: el formato de los ADR, la adopción de herramientas, la numeración heredada, las revisiones periódicas y su aplicación a los productos del grupo A (§7).

## 3. Regla propuesta

### 3.1 Disparadores

[P] Se reconsidera la arquitectura cuando hay **evidencia de que un supuesto declarado de la arquitectura vigente dejó de cumplirse** o **cambia una frontera** que esa arquitectura fija. Ejemplos, no exhaustivos:

| Clase | Ejemplos |
|---|---|
| Supuesto refutado | Carga, volumen de datos o latencia fuera del rango supuesto; fin de soporte, cambio de licencia o retiro de un servicio del que depende; requisito nuevo de seguridad, privacidad o regulación |
| Cambio de frontera | Aparece un segundo consumidor de un componente, como en el ADR 0008 de Brix del precursor; se extrae un repositorio; cambia un contrato público |
| Riesgo | Una decisión de nivel N3 toca la arquitectura: secretos, permisos, datos, migraciones o publicación |
| Incidente | Un incidente cuya causa identificada es arquitectónica |
| Pedido | El PO lo solicita con un motivo |

[P] **Tarifas y costos.** Un cambio de tarifa exige actualizar FinOps y comprobar la cobertura del presupuesto. Solo dispara una reconsideración si afecta la viabilidad del proyecto o la elección entre alternativas de arquitectura.

[P] No son disparadores una preferencia, la novedad de una herramienta ni una desviación aislada sin evidencia. Proponer una alternativa sigue siendo posible; no obliga a evaluar.

[I] La regla depende de que la arquitectura vigente declare sus supuestos. Si no los declara, la primera reconsideración los documenta a partir del disparador; no se exige reconstruirlos para los proyectos existentes antes de que ocurra uno (VCX-P3: la deuda heredada se declara, no se corrige por migración implícita).

### 3.2 Qué se registra

[P] Cada reconsideración registra cinco elementos:

| Elemento | Contenido |
|---|---|
| Disparador | Qué supuesto dejó de cumplirse o qué frontera cambió, con su fuente y fecha |
| Evaluador | Quién evaluó y con qué alcance; si es un agente, quién lo encargó |
| Resultado y fundamento | La arquitectura **sigue adecuada**, **se ajusta** o **se reemplaza**, con la evidencia que lo sostiene y lo que no pudo verificarse |
| Revisión evaluada | Sobre qué revisión de la arquitectura, del modelo de referencia y de FinOps se evaluó |
| Autoridad | Quién autoriza ejecutar las consecuencias y qué no queda autorizado |

[P] «Sigue adecuada» también se registra: sin ese registro no hay evidencia de que la evaluación ocurrió ni de contra qué revisión.

### 3.3 Dónde se registra, proporcional al resultado

[P] Para no crear un archivo por evaluación:

- **Sigue adecuada**, o **se ajusta** sin atar trabajo futuro: una entrada fechada con los cinco elementos en una sección «Reconsideraciones» al final del ADR de arquitectura vigente. La sección solo agrega entradas; no altera la decisión aceptada, que conserva su historia (VCX-P7).
- **Se reemplaza**, o se ajusta de un modo que ata trabajo futuro o es N3: un ADR nuevo que sustituye al anterior, con enlace en ambos sentidos. El anterior cambia su estado a sustituido; su número no se reutiliza.

### 3.4 Evaluación y autoridad

[P] Siguiendo la [matriz](../../architecture/responsibility-matrix.md#4-matriz-raci-humana-propuesta):

| Rol | Quién |
|---|---|
| R · evalúa | Equipo del proyecto, o un agente con alcance explícito |
| A · autoriza las consecuencias | PO del proyecto; el responsable del portfolio cuando el resultado afecta presupuesto del portfolio u otros proyectos |
| C · consultado | Brix, con sus instrumentos de arquitectura de referencia y FinOps; responsables de dependencias afectadas |
| I · informado | Responsable del portfolio |

[P] Si el disparador es de la clase Riesgo, o el resultado es «sigue adecuada» ante un disparador de seguridad o datos, el evaluador no puede ser quien escribió la arquitectura evaluada (VCX-P5). Evaluar no autoriza ejecutar: un agente puede ser R o C, nunca A, y un resultado favorable no es aprobación (VCX-P7).

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

Nota orientativa según VCX-P2: 7 de 10. Descuentos: dos puntos porque depende de que la arquitectura declare sus supuestos, ausentes en los proyectos existentes, y porque no se probó todavía sobre un caso; un punto porque es una regla de trabajo sin control ejecutable que la aplique. No es aprobación ni medición objetiva.

## 6. Verificación

Criterios observables para aceptar la regla, a comprobar con un caso sintético antes de ratificarla:

1. Un disparador de la clase Supuesto refutado produce un registro con los cinco elementos.
2. Un cambio de tarifa sin efecto sobre la viabilidad ni sobre la elección entre alternativas produce solo la actualización de FinOps.
3. Un resultado «sigue adecuada» deja una entrada en «Reconsideraciones» con la revisión evaluada.
4. Un reemplazo produce un ADR nuevo enlazado en ambos sentidos, con el anterior marcado como sustituido y sin número reutilizado.
5. Ningún registro presenta a un agente como A ni trata el resultado como autorización.

Contraejemplo a buscar en esa prueba: un disparador real que no encaje en ninguna clase. Si aparece, la clase genérica de §3.1 debe cubrirlo; si no lo cubre, la regla se corrige antes de ratificarse.

## 7. Pendientes separados

- **Numeración de ADR heredada.** Brix tiene dos `0007` y Pinot Index dos `0001` en el precursor, y `conventions.md` pide `ADR-NNN-kebab-case.md` mientras los archivos usan `NNNN-kebab.md`. El [inventario de deuda heredada](2026-11-01-inherited-debt-design.md) no lo registra. Se trata aparte, conservando referencias e historia; no bloquea esta regla.
- **Productos del grupo A.** Decidir si la regla se aplica a Blends, Brix y Cellar como proyectos, con su responsable como A según la matriz.
- **Formato del ADR.** MADR, una plantilla propia o una skill, con admisión en la [matriz de tooling](../../architecture/tooling-matrix.md).
- **Primer caso.** La arquitectura nativa de Teyst, propuesta del 2026-11-02 en `docs/superpowers/specs/2026-11-02-teyst-native-architecture-design.md` y sin commitear al redactar esta spec, podría ser el primer documento que declare sus supuestos explícitamente; no se asume que lo haga.
