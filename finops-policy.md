# Política FinOps de orquestación local

Fecha: 2026-11-01, reformulada el mismo día. Estado: semilla documental solicitada por el usuario; reformulada para consultar las fuentes del precursor en vez de mantener una matriz paralela. Ámbito: trabajo del agente en este workspace; no crea un producto VCX, un servicio central ni una dependencia ejecutable de sus productos. Principios y autoridad: [AGENTS.md](AGENTS.md). Reparto de responsabilidades: [matriz](docs/architecture/responsibility-matrix.md).

## Fuente y aplicación

Consultar este archivo antes de procesar nuevos requerimientos cuando esté accesible. Su existencia no demuestra carga automática en otros chats o herramientas. La instrucción del usuario que lo originó es la fuente de los tres roles y de las reglas de ajuste; no implica una aprobación transversal de método para los productos. Su ubicación en la raíz responde a esa instrucción y no tiene decisión registrada; ver pendientes.

## Free Tier first y eficiencia de suscripciones

Política fijada explícitamente por el usuario en este chat el 2026-11-01. Son dos criterios distintos:

1. **Herramientas: Free Tier first.** Antes de usar una herramienta, verificar si ofrece una opción gratuita aplicable al uso previsto, sus límites y las condiciones que podrían generar cargos. Tener Free Tier en el catálogo no demuestra que la operación concreta esté cubierta. Si la opción requiere pago, desafiarla con una alternativa gratuita que satisfaga los requisitos y explicar sus diferencias. Si no hay una alternativa gratuita adecuada, solicitar autorización explícita del Owner competente antes de usar la opción paga, identificando herramienta, operación, alcance, importe o límite y posibles cargos adicionales. Una autorización vigente que cubra esa misma operación no se solicita de nuevo. Un costo desconocido no se considera gratuito. Reutilizar verificaciones vigentes para el mismo alcance; revalidar al cambiar plan, condiciones, operación o límites.
2. **Modelos bajo suscripción mensual existente: eficiencia del cupo incluido.** Según declaración del usuario, las suscripciones se pagan se utilicen o no. El objetivo es obtener más resultados aceptados con la misma bolsa de tokens y el mismo plan, reduciendo contexto innecesario, delegación sin valor, reintentos y retrabajo. El uso incluido ya autorizado no exige una nueva aprobación de gasto por invocación. No atribuirle un cargo marginal por token usando tarifas de API. El cupo sigue siendo limitado y su consumo no equivale a costo cero del servicio. Pago por uso, overages, upgrades y suscripciones adicionales quedan fuera de esta excepción y requieren autorización explícita del Owner.

Comparar herramientas gratuitas por adecuación y costo total, sin rebajar requisitos de seguridad, privacidad, calidad o recuperación. Si la alternativa gratuita no cumple, explicar el impedimento y presentar la opción paga para decisión del Owner; no contratarla por inferencia. Separar en los reportes la cuota fija de suscripción, el consumo de cupo y los cargos variables. Afirmar eficiencia o ahorro solo con evidencia comparable; cuando falten contadores, declarar el límite de medición.

Esta sección es la fuente editable de ambas reglas; las instrucciones comunes la enlazan. Es una política documental, no un control automático de facturación. La fórmula de costo por token de este archivo aplica únicamente a consumos facturados por uso con tarifas verificadas, no a convertir el cupo incluido en un gasto variable ficticio.

## Fuentes de consulta en el precursor

El precursor ya resolvió el enrutamiento de modelos por clase, riesgo y costo. Según [AGENTS](AGENTS.md#fronteras) es de solo lectura y sus rutas son referencias de consulta, no dependencias. Esta política no copia sus valores: los enlaza y registra solo lo que difiere en este entorno.

| Dato | Fuente en el precursor | Qué aporta |
|---|---|---|
| Clases, perfiles de tarea, pisos por riesgo, motivos de elevación | [`model-routing-policy.json`](../blends/vc/tooling/lifecycle/model-routing-policy.json) | Orden `economy` < `balanced` < `frontier`; 16 perfiles de tarea; piso `balanced` para P0; auditoría P0/P1 en `frontier`; decorrelación del revisor por linaje |
| Modelos contratados, clase, costo relativo medido, base de costo | [`contracted-models.json`](../blends/vc/tooling/lifecycle/contracted-models.json) | Catálogo con evidencia de recibo y llamadas reales; `relativeCost` fable 4 : sonnet 1, medido el 2026-09-14 |
| Algoritmo, techo de costo, acta, fase 2 | [`model-resolver.md`](../blends/vc/docs/tooling/model-resolver.md) | Regla: el modelo menos costoso que cumpla la clase requerida; subir exige motivo declarado, bajar nunca |
| Decisiones y ejecuciones registradas | [`model-resolution-acta.jsonl`](../blends/vc/tooling/model-resolution-acta.jsonl) | 27 líneas al 2026-11-01, todas del perfil `conventional-implementation` con `claude-sonnet-5`; evidencia real pero de un solo perfil |
| Revisión de fallbacks por umbral | [`fallback-review.mjs`](../blends/vc/tools/fallback-review.mjs) | Cuenta fallbacks por binding y pide revisión al superar el umbral declarado |
| Validación de la clasificación de tareas | [`task-profile-benchmark.mjs`](../blends/vc/tools/task-profile-benchmark.mjs) | Set etiquetado por el PO y modo `--gate` |
| Tabla clase por tipo de tarea y presupuesto de tokens por complejidad | [`role-matrix.md`](../blends/vc/docs/standards/role-matrix.md) | Estándar que la política JSON refleja |
| Ledger de costos: presupuesto, proyección y real separados | [`engine.mjs`](../blends/vc/brix/packages/cli/finops/engine.mjs) y su schema | Modelo para informar costo sin mezclar estimación y factura |

Ninguna de estas fuentes figura todavía en la [matriz de tooling](docs/architecture/tooling-matrix.md), que registra `finops-ledger` pero no el resolver; ver pendientes.

## Roles solicitados y su equivalencia

Los tres roles pedidos por el usuario se mantienen como vocabulario de este chat. Cada uno equivale a una clase del precursor; ante diferencia entre esta tabla y la política JSON, rige la política JSON.

| Rol solicitado | Clase del precursor | Perfiles de tarea del precursor que cubre |
|---|---|---|
| Arquitecto | `frontier` | `architecture`, `high-ambiguity`, `security`, `migration`, `integration`, `destructive`, `audit`, `ui-design` |
| Operador | `balanced` | `conventional-implementation`, `ui-implementation` |
| Validador | `economy` | `inventory`, `bounded-search`, `mechanical-edit`, `derived-docs`, `deterministic-test`, `ui-adjustment` |

La clase requerida sale del perfil de tarea y de los pisos por riesgo, no solo del rol. Una tarea P0 nunca baja de `balanced`; una auditoría P0/P1 va a `frontier`. Los modelos nombrados en la instrucción original (`claude-3-5-sonnet`, `claude-3-5-haiku`, `gpt-4o`, `gpt-4o-mini`, `o1/o3`, `gpt-6-1-terra`) no están en el catálogo contratado; se reemplazan por el catálogo, sin conservarlos como alternativa.

## Disponibilidad en este entorno

Instantánea del 2026-11-01 en Claude Code dentro de la app de escritorio. No es una afirmación sobre catálogos comerciales, precios ni capacidades medidas.

| Clase | Catálogo del precursor | Despachable aquí | Estado de la verificación |
|---|---|---|---|
| `frontier` | `claude-fable-5-1`, `gpt-6-astra` | `fable` (subagente) y el agente principal | El agente principal se identifica como `claude-fable-5-1`; el subagente `fable` no fue ejercitado |
| `frontier` | no contratado | `opus` (subagente) | Fuera del catálogo contratado; no usar sin decisión del PO. Ejercitado el 2026-11-02 por decisión del usuario (F003): se identificó como `claude-opus-5-5` |
| `balanced` | `claude-sonnet-5`, `gpt-5.6-terra` | `sonnet` (subagente) | Ejercitado el 2026-11-02 (F003): se identificó como `claude-sonnet-5-5`, no como el `claude-sonnet-5` del catálogo; la equivalencia de clase es una hipótesis razonable, sin medición de costo relativo |
| `economy` | `gpt-5.6-luna`; Anthropic sin modelo economy en Max 5x | `haiku` (subagente) | Sin verificar que exista bajo el plan actual ni su costo relativo; hasta entonces, tratar `economy` como `balanced` con sustitución hacia arriba, igual que el alias `anthropic-economy-model` del precursor |
| cualquiera | `gpt-*`, `gemini-*`, `ollama/*` | No | Esta sesión no despacha modelos de OpenAI, Google ni Ollama; el canal `claude -p` del precursor no está disponible desde aquí |

Si falta un modelo de la clase requerida, declarar la sustitución o el bloqueo antes del despacho y registrarlo en la tabla de ejecución.

## Pesos, confianza y presupuesto

- Herramientas, posición del Owner del 2026-11-01, refinada el mismo día: preferir herramientas gratuitas que satisfagan los requisitos y verificar sus condiciones de uso. Toda opción paga debe contrastarse con una alternativa gratuita adecuada y requiere autorización vigente del Owner para el gasto adicional. Precisiones:
  - Gratuito y adecuado, no solo gratuito: primero cumplir los requisitos; después comparar el costo total, incluidos mantenimiento, exposición de datos y retrabajo.
  - Verificar al incorporar y cuando cambien las condiciones, no en cada invocación. Mantener evidencia fechada de plan, límites y operaciones cubiertas; revalidar ante cambios o proximidad al límite.
  - Distinguir Free Tier permanente, prueba que vence y créditos promocionales que se agotan. Registrar si hay cobro automático al superar el cupo.
  - Una autorización del Owner cubre herramienta, operación, duración y gasto máximo, coherente con VCX-P7. No se pide de nuevo dentro de ese alcance ni se extiende fuera de él.
- Tokens de suscripción, misma fecha: las suscripciones mensuales se pagan igual se usen o no. En ellas se optimiza el consumo total por resultado aceptado, manteniendo calidad y aprovechando el mismo plan. Medir por tarea completada: consumo total, calidad, retrabajo y tiempo, no tokens de un intento aislado; ahorrar en un intento que provoca tres correcciones no es eficiencia. Observar también cuota y límites de uso cuando sean visibles. Clase mínima que cumple, elevación solo con motivo declarado y contexto acotado por despacho. El `relativeCost` del catálogo mide consumo de cupo, no un cobro.
- Pesos numéricos de selección: no proporcionados; no inventarlos. La única relación de costo con evidencia es el `relativeCost` del catálogo del precursor.
- Confianza por categoría y modelo: sin medir. Los deltas `+0.10` y `-0.15` pedidos por el usuario son heurísticas sin base numérica; no aplicarlos hasta definir una. El mecanismo con evidencia disponible es el conteo de fallbacks contra umbral del precursor.
- Presupuesto monetario: no proporcionado; no interpretar como ilimitado. Esta política no autoriza compras, upgrades, APIs pagadas ni ampliaciones. El catálogo del precursor fija `allowPayPerToken: false`; se adopta el mismo criterio.
- Contadores: esta sesión expone porcentaje de uso del plan y ocupación de la ventana de contexto, no tokens por modelo con tarifa. El costo de subagentes no es medible aquí; declararlo «no disponible».
- Concurrencia: cuatro sesiones totales, incluido el agente principal; hasta tres subagentes simultáneos. Usar menos cuando no haya caminos independientes útiles.
- Acotar contexto, trabajo y criterios de aceptación por despacho. Evitar duplicación de investigación y reintentos sin diagnóstico.

## Ejecución y consolidación

1. Antes de editar, mostrar una tabla con ID único, tarea, rol y clase, modelo concreto, riesgo y dependencias. Si el entorno no expone el modelo, indicar la sustitución.
2. Despachar en paralelo las subtareas independientes dentro del límite, con alcance acotado. Las dependientes esperan los resultados necesarios. El agente principal integra y conserva la responsabilidad.
3. Verificar con los comandos pertinentes al comportamiento y riesgo. En documentación, comprobar enlaces, coherencia, procedencia y fuente única; no ejecutar compilaciones ajenas al cambio ni crear tests que reproduzcan texto. Este workspace no tiene suite ejecutable; las reglas basadas en `npm test` o `pytest` no se disparan aquí.
4. Informar evidencia, pendientes y costo. Con contadores y tarifas verificadas, estimar por modelo: `(input_uncached × rate_input + input_cached × rate_cached + output × rate_output) / 1_000_000`, con tarifas por millón de tokens, moneda, fecha y cargos adicionales; sumar cada consumo una sola vez. Sin contadores o tarifas, declarar «no disponible»; nunca cero ni una cifra inventada. Separar estimación, proyección y factura como hace el ledger del precursor.

## Ajustes por evidencia

- Elevar de clase solo por uno de los motivos del precursor: dos fallos equivalentes, ambigüedad de contrato, criticidad superior o retrabajo que supera el ahorro. Registrar el motivo.
- Éxito económico: si un `balanced` resuelve una tarea de perfil `frontier` y supera los criterios, registrar la evidencia y la revisión evaluada. Sin comparación de costo, registrar éxito técnico sin afirmar ahorro.
- Falla: diagnosticar si es atribuible al cambio, a una prueba previa o al entorno. Ante un cambio defectuoso, retirar solo los cambios identificados, registrar evidencia y escalar dentro del alcance autorizado. Un fallo externo no demuestra incapacidad del modelo. Cuando el conteo de fallbacks supere el umbral, pedir revisión en lugar de ajustar un número.
- Categoría nueva: si el requerimiento no encaja en un perfil del precursor, registrarla aquí como candidata con clase `balanced` en «Fase de Pruebas» y criterios observables. Proponer el perfil al benchmark del precursor solo mediante un pedido explícito, porque ese repositorio es de solo lectura.
- Al cierre de cada sesión, actualizar solo con evidencia nueva: categoría, modelo, revisión evaluada, resultado, comprobaciones y motivo. Conservar antecedentes; los ajustes no amplían autoridad ni presupuesto.

## Registro

| ID | Categoría | Modelo | Estado | Confianza y ajuste | Evidencia |
|---|---|---|---|---|---|
| F001 | Configuración documental de orquestación | Principal no expuesto en el entorno de origen | Fase de Pruebas | Sin medir; sin delta | Creación solicitada por el usuario el 2026-11-01; sin ejecución de código de producto |
| F002 | Reformulación de esta política sobre las fuentes del precursor | Agente principal, `claude-fable-5-1` | Cerrada | Sin medir; sin delta | Lectura en solo lectura de las fuentes enlazadas el 2026-11-01; sin subagentes; costo no disponible |
| F003 | Evidencia de evaluación de tooling, perfil `audit` (dos candidatos) e `inventory`/`bounded-search` (tres) | Subagentes `opus` (se identificaron como `claude-opus-5-5`) y `sonnet` (`claude-sonnet-5-5`); `opus` fuera del catálogo contratado, por decisión del usuario en el chat del 2026-11-02 | Cerrada | Sin medir; sin delta. Éxito técnico: los cinco archivos cumplieron el contrato del motor, uno tras agregar referencias a subfactores sin evidencia | [Reporte](docs/superpowers/reports/2026-11-02-finops-orchestration-repos-tool-dry-run.md): 580.294 tokens de subagentes informados por el harness, 3 simultáneos como máximo, costo en dinero no disponible |

## Pendientes

- Decidir dónde vive este archivo: la raíz responde a la instrucción original, pero no hay decisión registrada; una alternativa es `docs/` con entrada en el registro de decisiones.
- Registrar el resolver del precursor en la matriz de tooling si se adopta como consulta, y comprobar si `brix-capabilities.json` tiene entrada para él.
- Verificar qué versión resuelven `sonnet` y `haiku` en esta sesión y si `haiku` existe bajo el plan actual.
- Obtener contadores y tarifas antes de afirmar costos o ahorros. Definir base de confianza y presupuesto numérico cuando una decisión los requiera.
- El mensaje original quedó truncado al anunciar el formato de respuesta; la tabla del punto 1 adopta sus cuatro campos explícitos más riesgo.
