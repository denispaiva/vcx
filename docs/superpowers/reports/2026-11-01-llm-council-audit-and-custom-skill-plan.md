# Auditoría de `llm-council-skill` y plan para `vcx-llm-council-skill`

Fecha: 2026-11-01. Estado: **propuesta**, sin implementar, sin evaluar y sin registro en Blends (AGENTS: solo lectura). Fuente: `llm-council-skill.evaluation.json` y `.evidence.json` (evaluación del 2026-09-11, puntaje 39,6, riesgo alto, `do_not_advance`), leídos el 2026-11-01; los puntajes por subfactor son juicios de modelo (`claude-opus-5`) con rationale, no mediciones.

## 1. Qué bajó el puntaje y quién puede corregirlo

| Subfactor (puntaje) | Causa registrada | ¿Corregible en una skill propia? | Cómo |
|---|---|---|---|
| activityRecency (10), commitContinuity (0), releaseContinuity (0), responseHealth (15) | 1 commit, sin releases ni tags, sin mantenedor | Sí | Repositorio propio con historial, etiqueta de versión y responsable (VCX-P9) |
| versioningDiscipline (0) | Sin versión en ningún lugar | Sí | Campo de versión en el frontmatter y tag por release |
| sourceProvenance (20) | Autor sin verificar, sin LICENSE, instalación desde `main` | Sí, con una condición | Archivo LICENSE propio, `PROVENANCE.md` y SHA fijado; el método se atribuye a Karpathy |
| securityHygiene (10) | Sin CI, sin política de seguridad | Parcial | Un chequeo mínimo proporcional al riesgo; no justifica infraestructura nueva (VCX-P3) |
| permissionTransparency (40) | Escanea el workspace y lee CLAUDE.md, memoria y transcripts por iniciativa propia; abre el HTML solo | Sí | Lista cerrada de lecturas y escrituras; ningún escaneo implícito; sin apertura automática |
| automatedVerification (0) | Sin pruebas ni suite de evaluación | Parcial | Un caso ficticio con criterios observables, como se hizo con `killer-questions` |
| compatibilityEvidence (10) | No declara compatibilidad | Sí | Declarar con qué entorno se probó y la fecha |
| technicalCompatibility (45) | Disparadores amplios («should I X or Y»), inglés | Sí | Disparadores acotados al pedido explícito; español, identificadores en inglés |
| capabilityGapCoverage (55) | La síntesis termina en «la recomendación» y «la única cosa que hacer primero», lo que choca con la invariante 44 de Blends | Sí | La síntesis entrega pendientes y decisiones para el humano, sin recomendar ni decidir |
| incrementalValue (30), observedAdoption (25) | El portfolio ya tiene `/council`; adopción interna cero | Solo en parte | Si la skill propia reemplaza a `/council` como fuente única, el valor incremental depende de lo que aporte el empaquetado; la adopción debe medirse en uso real |
| community (37,9) | 757 estrellas contra referencias de 100 000 | **No** | No hay comunidad en una skill propia; este factor será bajo o indisponible y no debe maquillarse |

Lo que ya estaba bien y hay que conservar: documentación (80), sin dependencias (95), portabilidad (95), reversibilidad (100), costo predecible (70: 11 invocaciones por corrida).

## 2. Riesgo

Banderas de la evaluación: `localWriteReversible` y `broadScope`. Con los límites de lectura y escritura cerrados, `broadScope` debería poder retirarse. Eso lo decide la evaluación, no este plan.

## 3. Reglas de diseño propuestas

1. **Partir de `/council` y del método de Karpathy, no del texto de `tenfoldmarc`.** Esa skill no declara licencia en archivo. Copiarla heredaría ese problema; no he comprobado qué partes de `/council` provienen de ella.
2. Una sola fuente editable: si `vcx-llm-council-skill` reemplaza a `/council`, uno de los dos se retira con trazabilidad (VCX-P9). Dos copias vivas no.
3. Entradas, lecturas, escrituras y salida explícitas; en ejecución no interactiva, listar aclaraciones pendientes en lugar de adivinar.
4. Sin recomendar ni decidir: la salida del consejo es insumo, no autoridad.

## 4. Límite honesto de este camino

El puntaje de una skill propia mide principalmente el cuidado de quien la mantiene. No demuestra que sirva. La evidencia de eficacia sale solo del uso medido y de la comparación con corridas anteriores de `/council`.

## 5. Pendientes

- Definir qué debe entregar «Reporte del consejo» (formato, archivo o chat) y su criterio de aceptación.
- Elegir ubicación y dueño de la skill (¿Brix, por el catálogo de instrumentos?).
- Leer `council.md` de Blends para fijar qué se conserva; no se hizo en esta revisión.
- Evaluar con `/tool` en una sesión con permiso explícito sobre Blends.

Nota: la evaluación del precursor (2026-09-11) llama al comando `consejo.md`; hoy el archivo es `blends/.claude/commands/council.md` (`/council`).
