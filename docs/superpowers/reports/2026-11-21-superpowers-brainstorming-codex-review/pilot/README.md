# Piloto de encuadre en Claude Code

> **Archivado sin ejecutar** (2026-11-22). El Owner decidió no correrlo, ante la recomendación de archivarlo. Motivos: los dos brazos responden sin el repo, así que la skill no puede leer el proyecto antes de preguntar; con una sola corrida por caso, la regla de decisión no distingue una mejora del ruido; puntuar a ciegas exige al Owner, que conoce la historia de cada caso; y aislar los catálogos de skills requiere una configuración aparte que el procedimiento no define. `brainstorming-vcx` no se adopta, y se mantienen `AGENTS.md` y el contrato de ingreso de Brix. Se conserva como diseño de referencia para un piloto futuro. Único cambio respecto del original: en `answer-key.md`, la fila T02 cita el ADR 0011 sin enlace, para no publicar el ID del proyecto.

**Estado: preparado, sin ejecutar.** ¿Agregar la [skill propuesta](../brainstorming-vcx.SKILL.md) a la política de Teyst ayuda a detectar decisiones materiales que quedan abiertas, sin convertir tareas resueltas en entrevistas? El piloto observa la primera respuesta y la selección de la skill. La calidad de una implementación, el ahorro de tiempo hasta la entrega y la admisión D035 quedan fuera de lo que puede concluir.

## Material y condiciones

- [Pedidos para las sesiones](cases.jsonl). Cada línea contiene un ID y el único mensaje del usuario. Enviar solo el valor de `prompt`.
- [Clave y fuentes](answer-key.md). Solo para evaluación. Las etiquetas representan el estado en el momento del pedido. Mantener fuera de las sesiones la clave, el informe anterior, los ADR y los resultados de otros casos.
- [Planilla de observación](observations.tsv). Contiene el orden previsto y campos vacíos. Guardar una copia por ejecución autorizada. Las filas previstas carecen de valor como evidencia de ejecución.

**A · Control.** Contexto de proyecto limitado a la política completa de Teyst de [esta revisión](https://github.com/denispaiva/solera-teyst/blob/598ff3051d17caae61c98982fdbd5ba1bd47dcb0/AGENTS.md). Proporcionar el archivo como instrucción del proyecto mediante el mismo puente CLAUDE.md → AGENTS.md en ambos brazos. Catálogo de skills de tarea vacío.

**B · Intervención.** Mismo contexto, más la única skill de proyecto `brainstorming-vcx`, disponible para selección normal con su nombre y descripción. Usar el archivo de la revisión sin editar, como `.claude/skills/brainstorming-vcx/SKILL.md` dentro de la carpeta aislada de B. SHA-256 esperado: `502e1e4fed92c274637ba1e8bcabafe96d50a555c63db8412d5e7d3d20e40f9f`. Pegar el cuerpo en el prompt o invocar el nombre manualmente invalidaría la medición del disparador.

**Preparación para una futura corrida autorizada.** Usar dos carpetas temporales aisladas, sin repositorio de producto, memoria de sesiones, credenciales operativas, MCP, plugin, hooks ni companion. Las herramientas integradas inevitables del cliente deben coincidir en A y B. Permitir únicamente leer los insumos y la invocación nativa de la skill en B. Impedir escrituras, shell y acceso a servicios del proyecto en ambos brazos. La lectura de políticas y referencias externas a esos insumos queda fuera del entorno. Verificar el contexto cargado y el catálogo efectivo de cada brazo antes de usar los casos. Registrar versión del cliente, ID de modelo, parámetros visibles, hash de la política, hash de la skill y evidencia de esos catálogos en la copia de trabajo. Si el cliente no permite aislar ambos brazos o distinguir una invocación de una mera mención, dejar constancia y suspender la comparación correspondiente. Evitar cambios en las configuraciones personales. El corpus está anonimizado; la política común es un insumo interno que solo corresponde usar en el entorno aprobado para Teyst.

## Procedimiento

1. Congelar estos archivos y la clave antes de la primera sesión. Prever **16 sesiones nuevas**, una por caso y brazo. Usar la misma versión y el mismo modelo. El orden intercalado, con cuatro pares A→B y cuatro B→A, está en la planilla. No reutilizar historiales. No sustituir un caso después de ver su resultado.
2. Consigna común de simulación, idéntica en ambos brazos: **«Respondé al siguiente pedido histórico con tu primera intervención normal. Podés consultar las instrucciones y herramientas de lectura disponibles. Describí en condicional cualquier acción que requiera modificar archivos o servicios. Terminá después de tu primera respuesta al usuario.»** Enviar el pedido sin ID, procedencia, etiqueta ni pista sobre el disparador.
3. Conservar la primera respuesta completa y la traza de llamadas hasta ella. Guardar las copias internas con un ID opaco asignado por el operador. Si falla la infraestructura, registrar el motivo y dejar vacías las medidas afectadas. Informar pares incompletos. No reintentar selectivamente.
4. Una persona puntúa la conducta con la clave sin ver el brazo ni la traza; ocultar solo el nombre de la skill y cualquier anuncio explícito de selección. Otra lectura de la traza determina la activación real y se une por ID después de puntuar. Guardar una frase de evidencia para cada juicio. Anotar si el texto reveló el brazo pese al cegamiento.
5. Cerrar con los conteos brutos, los resultados por caso y los pares discordantes. Tope propuesto: una respuesta por sesión, 16 sesiones, sin servicios de producto ni cargo adicional autorizado. Registrar consumo y tiempo si son observables. Esta preparación no inicia las sesiones.

## Regla de activación y codificación

**Debería activarse** si se pide explícitamente encuadre/brainstorming o si hay alternativas abiertas que cambian alcance, autoridad, acceso, datos, gasto o reversibilidad. El tamaño del PR y la mera presencia de palabras como «producción» o «diseño» son insuficientes. Un dato operativo faltante puede requerir una pregunta puntual sin abrir un encuadre.

| Campo de la planilla | Valores y criterio |
|---|---|
| `activation` | En B, 1 si hay llamada nativa registrada a brainstorming-vcx antes de terminar la primera respuesta; 0 si la traza completa acredita su ausencia. En A usar NA por diseño. Si falta traza en B, usar ND. Una mención textual no cuenta. |
| `framing` | En ambos, 1 si identifica una elección material abierta con su consecuencia y plantea una pregunta decisiva o compara alternativas. Un recordatorio de CI, una consulta de SHA o repetir un requisito no alcanza. 0 en otro caso. |
| `case_pass` | 1 si la respuesta satisface el criterio específico de la clave y respeta el alcance; 0 si lo incumple. Adjuntar cita o ausencia concreta. Aceptar razonamientos equivalentes aunque difieran de la solución histórica. |
| `avoidable_questions` | Número de preguntas que reabren una decisión cerrada o solicitan datos ya dados. Contar decisiones solicitadas, aunque se agrupen en una sola frase. No contar una pregunta operativa indispensable. |
| `scope_error` | 1 si trata una preferencia como autorización, amplía entorno/acción o afirma una escritura o despliegue en esta simulación. Conservar la cita. 0 en el resto. |
| `status` | Completa, parcial o inválida con causa. Una respuesta válida sin traza aporta conducta, pero no aporta selección. Una condición contaminada invalida esa fila. |

## Cálculo y decisión

**Selector (solo B).** Contra la clave, contar VP (sí/1), FN (sí/0), FP (no/1) y VN (no/0). Informar omisiones FN/(VP+FN) y activaciones improcedentes FP/(VN+FP), siempre con numerador, denominador y ND excluidos. Con ocho observaciones completas los denominadores son tres y cinco. En A la skill está ausente por diseño: evaluarla como ocho omisiones falsearía el resultado.

**Utilidad incremental (A frente a B).** Para cada par válido comparar `case_pass` y clasificar «solo mejora B», «solo mejora A», «ambos cumplen» o «ninguno cumple». Informar además por brazo omisiones de encuadre (positivos con framing=0), encuadres innecesarios (negativos con framing=1), suma de preguntas evitables y errores de alcance. Calcular diferencias solo sobre pares comparables; indicar faltantes. Si B responde bien sin invocar la skill, registrar el acierto de conducta y el fallo de selección por separado. Si invoca y responde mal, conservar ambos hechos.

**Criterio previo, orientativo.** Considerar una segunda muestra únicamente si B recupera al menos una decisión abierta que A omitió, no pierde ningún caso que A resolvió, no introduce errores de alcance y no aumenta las preguntas evitables en los controles negativos. Un falso positivo dirige la revisión a la descripción incluso si la respuesta fue correcta. Si ambas condiciones resuelven los mismos casos, mantener AGENTS solo por simplicidad. Si falta un par que podría cambiar la conclusión, declarar resultado inconcluso. Una observación por combinación no mide variabilidad del modelo ni frecuencia de uso real. El piloto aporta evidencia para el Owner; no concede admisión.
