# FinOps de {{initiative_name}}

Plantilla documental para una idea aceptada. Estado inicial: **borrador de estimación, sin autorización de gasto por sí mismo**. Resolver los marcadores con datos verificables, supuestos identificados o pendientes explícitos. No inventar importes, tarifas, facturas, aprobaciones o valores de costo cero.

## Base y revisiones

| Campo | Valor | Significado |
|---|---|---|
| `initiativeRef` | `{{initiative_ref}}` | Identidad y revisión de la idea aceptada |
| `admissionDecisionRef` | `{{admission_decision_ref}}` | Decisión humana de ingreso |
| `referenceArchitectureRef` | `{{reference_architecture_ref}}` | Modelo y revisión propuestos por la capacidad de Brix |
| `scenarioRef` | `{{scenario_ref}}` | Escenario de arquitectura y carga que se estima |
| `estimateRevision` | `{{estimate_revision}}` | Revisión de este documento |
| `period` | `{{period}}` | Período de la estimación |
| `currency` | `{{currency}}` | Moneda utilizada; explicitar conversión si corresponde |
| `ownerRef` | `{{owner_ref}}` | Responsable de preparar y mantener la estimación |
| `analysisAuthorizationRef` | `{{analysis_authorization_ref}}` | Límite previamente autorizado para este análisis |

## Objetivo y alcance que se pide autorizar

{{funding_scope_and_value_unit}}

Explicar la fase solicitada, qué resultado o aprendizaje se espera, la unidad de valor y las exclusiones. Distinguir el presupuesto solicitado de proyecciones sobre otras fases que todavía no se autorizan.

## Componentes, actividades y factores de consumo

{{architecture_components_and_cost_drivers}}

Por línea identificar: `costItemId`, referencia al componente o actividad del modelo, fase, entorno cuando aplique, `costPool`, unidad, cantidad, período, tarifa, fuente y fecha de la tarifa, fórmula o regla aplicada, incertidumbre y escenarios. Declarar los componentes sin estimación y el motivo; la cobertura incompleta no se oculta en un total.

La estructura debe cubrir agentes, cloud, tooling y servicios externos cuando correspondan. Las actividades de preparación, investigación y atención humana también se declaran; su esfuerzo puede medirse sin asignarle una tarifa monetaria inventada.

## Escenarios y supuestos

{{scenarios_assumptions_and_estimates}}

Comparar escenarios de uso y arquitectura pertinentes, con sus cantidades, supuestos y fuentes. Si se presentan bandas o porcentajes de contingencia, explicar su fundamento. Tarifas desconocidas o desactualizadas quedan pendientes, no se asumen vigentes.

## Compromisos, consumo y asignaciones

{{commitments_usage_allocations_and_credits}}

Separar costos fijos, variables y únicos. Declarar qué costos son directos y qué parte se asigna desde una fuente compartida. Una suscripción compartida conserva una única fuente y asignaciones trazables para el período, sin sumarse otra vez como costo íntegro de cada iniciativa. Los créditos y promociones se muestran aparte del compromiso contractual y del consumo.

## Presupuesto, proyección y gasto real

{{budget_forecast_and_actuals}}

Presentar por separado presupuesto propuesto, presupuesto aprobado —si existe—, proyección y gasto real comprobado. Si no hubo consumo o no se concilió, indicarlo con su estado; una factura no se deduce de una estimación. El gasto real remite a su ledger o fuente de billing canónica y a su evidencia, sin crear aquí otro registro editable de las mismas transacciones.

## Límites, alertas y recuperación

{{limits_alerts_and_exit_conditions}}

Declarar topes autorizados, alertas, revisiones, condición de pausa, autoridad para ampliar y costo de salida o cancelación cuando corresponda. Una alerta de proveedor no se presenta como límite duro si no lo es. Las reglas del perfil adoptado se referencian; no se copian como otra política particular.

## Revisión y decisión humana

{{budget_decision_ref}}

Registrar autoridad, fecha, revisión del modelo y de esta estimación, escenario, fase, monto o límites de esfuerzo, moneda y período que se autorizan. Los demás escenarios siguen siendo propuestas. La aceptación previa de la idea no sustituye esta decisión.

## Pendientes y próxima revisión

{{open_questions_and_review_trigger}}

Identificar datos faltantes y los cambios de arquitectura, uso o precios que obligan a revisar. Una actualización material no amplía el presupuesto por inferencia; enlaza la decisión que corresponda.
