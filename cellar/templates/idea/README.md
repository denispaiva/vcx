# {{idea_name}}

**Propuesta en preparación; todavía no aceptada como idea del portfolio.** Plantilla de documento para `/idea` y posterior revisión humana. Resolver los marcadores con datos o indicar explícitamente lo pendiente. Los marcadores son guía documental, no un esquema ejecutable o valores aprobados.

## Identificación y procedencia

| Campo | Valor documental | Significado |
|---|---|---|
| `submissionId` | `{{submission_id}}` | Proceso de preparación de la propuesta |
| `documentRevision` | `{{document_revision}}` | Revisión presentada al humano o al consejo |
| `authorRef` | `{{author_ref}}` | Autor de la explicación original |
| `sourceRefs` | `{{source_refs}}` | Texto o archivos de origen y páginas/secciones utilizadas |
| `templateRevision` | `{{template_revision}}` | Versión o revisión verificable de la plantilla aplicada |
| `intendedCellarRef` | `{{intended_cellar_ref}}` | Destino propuesto; puede estar pendiente durante la preparación |
| `extractionNotes` | {{extraction_notes}} | Límites, contenido ilegible y partes no procesadas |

## Explicación original

{{original_explanation}}

Conservar las palabras del autor y su procedencia. No atribuirle las interpretaciones posteriores.

## Marco de la propuesta

- Problema u oportunidad: {{problem_or_opportunity}}
- Personas involucradas y beneficiarias: {{audience}}
- Misión propuesta: {{proposed_mission}}
- Visión propuesta: {{proposed_vision}}
- Alcance y límites iniciales: {{initial_scope}}
- Alternativas conocidas: {{known_alternatives}}
- Costo del error: {{failure_cost}} (qué se pierde si la idea avanza y resulta equivocada: dinero, personas afectadas, tiempo; «sin estimar» si no se sabe)
- Datos crudos disponibles hoy: {{raw_data_available}} (registros, mediciones o documentos existentes que permitirían verificar el problema, con ubicación y límites; «ninguno» si no hay)
- Primera validación posible: {{first_validation}}

Las formulaciones añadidas por el instrumento se marcan como propuestas. Se puede declarar que una sección no tiene respuesta todavía; no se inventa precisión para completar el formato.

## Preguntas asesinas

{{killer_questions}}

Para cada pregunta: qué supuesto pone a prueba, por qué una respuesta negativa podría invalidar la idea, qué se sabe, qué falta, qué evidencia permitiría responder y qué señal temprana avisaría de que el supuesto falla. Distinguir preguntas candidatas de las confirmadas por el humano.

## Supuestos, preguntas abiertas y evidencia disponible

{{assumptions_open_questions_and_evidence}}

Separar evidencia verificable de opiniones, hipótesis y asesoría. Una síntesis de agentes no demuestra por sí misma que un supuesto del mundo real sea cierto.

## Revisión humana y envío al consejo

{{human_review_ref}}

Registrar la referencia al OK y a la revisión evaluada, sin autoaprobar campos. Informar al humano qué se enviará mediante `/council <archivo.md>` y que obtendrá un reporte antes de confirmar el ingreso. Si pide cambios, preparar otra revisión y conservar la procedencia.

## Consejo y decisión de ingreso

| Referencia | Valor |
|---|---|
| Reporte y revisión de entrada analizada | `{{council_report_ref}}` |
| Decisión humana posterior al reporte | `{{admission_decision_ref}}` |

Antes de la ejecución y decisión, estas referencias se declaran pendientes; no se inventan resultados. El reporte es otro artefacto: aquí se enlaza, no se mantiene una segunda síntesis editable como reemplazo.

## Al confirmar el ingreso

Actualizar la identificación de este contexto para enlazar la iniciativa aceptada y su decisión, conservando la historia y una única fuente activa. La transferencia o reclasificación se realizará conforme al almacenamiento declarado; la plantilla no ejecuta ese cambio. El estado del ciclo comienza como `registered`; una idea aceptada todavía no es un proyecto graduado.
