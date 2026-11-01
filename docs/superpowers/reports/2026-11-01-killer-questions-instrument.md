# Instrumento de preguntas asesinas: incorporación y prueba acotada

Fecha: 2026-11-01. Autorización: pedido del usuario en este chat (alcance: revisar, incorporar con adaptación mínima, documentar y probar con un caso ficticio; sin commits). Este reporte es evidencia fechada; las fuentes editables son la [matriz de tooling](../../architecture/tooling-matrix.md) y la [procedencia de la skill](../../../brix/.claude/skills/killer-questions/PROVENANCE.md).

Se separan tres cosas: **incorporación** (hecha), **prueba funcional** (una ejecución, ficticia) y **aprobación** (no existe; corresponde a la autoridad humana).

## 1. Incorporación

- Origen: `phuryn/pm-skills`, revisión `2a12295`, skill `pm-product-discovery/skills/identify-assumptions-new`. MIT. Un archivo, sin scripts, dependencias ni red; sin dependencia de pago.
- Mecanismo mínimo: un directorio `brix/.claude/skills/killer-questions/` (convención del precursor `.claude/skills/<nombre>/`), con `SKILL.md` adaptado, `UPSTREAM-SKILL.md` (original sin cambios, SHA-256 registrado), `LICENSE-pm-skills` y `PROVENANCE.md`. No se instaló el marketplace, no hay runtime ni script.
- Ajustes locales (detalle en `PROVENANCE.md`): prueba de decisividad con decisión y consecuencia; ficha de evidencia con procedencia, límites, prueba y criterio observable; eliminación de «califica la confianza»; sin cantidad ni categorías obligatorias; sin semáforo, clasificación bloqueante ni MVP.
- Compatibilidad: no cambia el gate vigente ni adopta el diseño de maduración, que sigue siendo propuesta. Lo que la skill produce es compatible con el recorrido actual (preguntas con evidencia); lo que el diseño aún no aprobó (semáforo, bloqueante/pendiente, cinco categorías) queda fuera por regla expresa.
- Documentos tocados: la fila de la matriz pasa de Brecha a Candidato; `brix/docs/idea-intake.md` registra la herramienta. No se tocó el precursor ni se marcó la brecha como resuelta.

**Descubrimiento:** no verificado. En esta sesión, iniciada en la raíz de VCX, `Skill("killer-questions")` respondió «Unknown skill». No se determinó si una sesión abierta en `brix/` la descubriría. La prueba funcional leyó el archivo por ruta, no por el mecanismo de skills.

## 2. Prueba funcional (un caso ficticio)

Entrada: [caso ficticio](2026-11-01-killer-questions-test/fictional-case-input.md) (recordatorios de riego para huertas), diseñado con una cifra sin fuente (70 %), una muestra informal de 3, ambigüedad de usuario y pagador, y dos preguntas interesantes no decisivas (balcones, nombre de marca). Salida: [salida cruda](2026-11-01-killer-questions-test/fictional-case-output.md), producida por un subagente sin contexto previo que solo siguió `SKILL.md`.

Criterios fijados antes de ejecutar y resultado:

| Criterio | Resultado |
|---|---|
| Distingue hechos, afirmaciones sin fuente e inferencias | Cumple: declara «ningún hecho verificable»; el 70 % y las charlas quedan como afirmaciones del autor |
| Cada pregunta decisiva tiene todos los campos | Cumple en las 5 fichas |
| La consecuencia nombra un tipo de decisión (abandonar, diferir, simplificar, alternativa) | Cumple |
| No inventa cifras, respuestas ni umbrales | Cumple: los umbrales se dejan al humano. Ver límite sobre vaguedad |
| Contraejemplo: pregunta interesante no decisiva queda fuera | Cumple: balcones y marca excluidas con motivo; ética/privacidad y competencia también quedan fuera con motivo |
| Ambigüedad material aclarada o marcada | Cumple: usuario y pagador listados; pregunta 3 marcada condicional |
| Sin semáforo, bloqueo, MVP ni plan | Cumple; las pruebas propuestas (registro de riegos, avisos manuales) no son un producto |

## 3. Límites y defectos observados

- **Una sola ejecución**, por un modelo, sobre un caso que diseñé conociendo los criterios. No hay réplica, no hay control con la skill original (no se puede atribuir lo observado a la adaptación frente a la capacidad del modelo) ni revisión humana de utilidad.
- Algunos criterios observables son vagos: «mayoritaria» (pregunta 1), «claramente menor» (pregunta 4). Deferir el umbral al humano evita inventarlo, pero deja el criterio parcialmente no observable hasta entonces.
- La pregunta 5 (capacidad del autor) es más una definición pedida al autor que un supuesto refutable por evidencia; es discutible que sea «asesina».
- La aclaración 4 de la salida se lista y a la vez se descarta como aclaración; incoherencia menor.
- La decisión en juego fue inferida por el modelo (señalada como propuesta). En un caso real la decide el humano.
- El caso es ficticio: no demuestra utilidad con ideas reales ni integración con la plantilla de ideas, `brix idea` o el consejo.

## 4. Réplica y control (segunda ronda, 2026-11-01)

Criterios fijados antes de ejecutar: [replication-criteria.md](2026-11-01-killer-questions-test/replication-criteria.md). Se añadieron el caso B (evidencia sólida, decisión de bajo costo y reversible) y el caso C (dos fuentes que se contradicen), y se ejecutó el original (`UPSTREAM-SKILL.md`) como control en A, B y C. Cinco ejecuciones nuevas, un subagente nuevo cada una, mismo modelo. Salidas crudas en la carpeta de pruebas (`output-adapted-b.md`, `output-adapted-c.md`, `output-control-a.md`, `output-control-b.md`, `output-control-c.md`; la adaptada en A es `fictional-case-output.md`).

| Criterio | Adaptada (A, B, C) | Control (original) |
|---|---|---|
| R1 hechos / afirmaciones / inferencias | Cumple en los tres | No cumple: no las separa; B solo añade observaciones sobre la evidencia |
| R2 decisión, consecuencia, evidencia faltante, prueba y criterio | Cumple (en C, evidencia faltante y prueba van en un mismo campo) | No cumple: solo supuesto, confianza y prueba |
| R3 sin cifras ni umbrales sin marcar | Cumple con una salvedad: C afirma «con permiso expreso» de las peluqueras, dato que la entrada no trae | Parcial: propone tamaños de muestra y plazos (5 a 8 locales, 60 a 90 días) sin marcarlos como propuestas |
| R4 sin confianza del modelo como evidencia | Cumple | No cumple: asigna Alta/Media/Baja a cada supuesto |
| R5 excluye pregunta no decisiva (A) | Cumple (balcones y marca fuera, con motivo) | No cumple del todo: los lista como supuestos G5 y G6, luego los pospone |
| R6 no rellena (B) | Cumple: 1 pregunta decisiva; 5 descartadas con motivo | No cumple: unos 23 supuestos en 8 categorías |
| R7 contradicción entre fuentes (C) | Cumple: identifica ambas cifras, no promedia, propone leer la metodología y contar ausencias reales; señala que podrían medir poblaciones distintas, rotulado como inferencia | Cumple en parte: la detecta y propone resolverla (V1), dentro de unos 30 supuestos |
| R8 sin MVP ni plan | Cumple | Cumple; añade una «secuencia sugerida» de pruebas |
| R9 ambigüedades materiales | Cumple (A y C) | No cumple: no las lista |

Cantidades: la adaptada produjo 5, 1 y 4 preguntas decisivas (A, B, C); el control, aproximadamente 35, 23 y 30 supuestos (conteo de filas de tablas).

**Lectura:** en estos tres casos la adaptación se comporta como se diseñó y el original no, en los criterios que la adaptación agrega a propósito (decisión, evidencia, no rellenar, sin confianza). Eso es esperable: los criterios los definí a partir de la adaptación, por lo que la comparación no es neutral. No prueba que las preguntas sean mejores para un humano, solo que cumplen el contrato. Siguen valiendo los límites de la sección 3, más: mismo modelo en todas las ejecuciones, criterios evaluados por mí (no por un tercero) y tres casos ficticios.

## 5. Estado de los pendientes

| Pendiente | Estado |
|---|---|
| Admisión en el precursor (`/tool`) | Abierto: decisión humana y escritura en el precursor, no autorizada aquí |
| Descubrimiento desde `brix/` | Verificado en una sesión con `brix/` como directorio de trabajo (2026-11-01, informe pegado por el usuario, no reproducido por mí): aparece en la lista de skills y `Skill("killer-questions")` la carga; invocada sin argumentos el campo de entrada llega vacío. Desde la raíz `vcx/` no se descubre (dos comprobaciones). Una sola sesión; no demuestra otros entornos. Esa sesión ejecutó la skill sobre el caso A y la salida respetó el contrato, evaluada por el mismo modelo |
| Plantilla o capacidad registrada | Abierto: decisión del dueño (Brix), fuera de este alcance |
| Regenerar vista HTML | Hecho por otro agente en los commits `4fce135`–`53ac997`; la fila nueva figura en [tooling-matrix.html](../../exports/tooling-matrix.html). La matriz committeada enlaza a archivos de la skill que siguen sin commit (enlaces rotos en esa revisión hasta que se incorporen) |
| Réplica y control | Hecho (sección 4), con los límites indicados |
| Semáforo y clasificación | Siguen pendientes del diseño de maduración |
