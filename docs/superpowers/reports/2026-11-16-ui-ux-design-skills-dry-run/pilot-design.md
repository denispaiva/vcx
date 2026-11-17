# Piloto de utilidad: frontend-design y reglas web fijadas

Fecha: 2026-11-16. Estado: **diseño propuesto, sin ejecutar.** Pedido del usuario en el chat de Claude Code («Sí, diseñar el piloto»), sobre la [evaluación en seco](README.md) de la misma fecha. Este documento no autoriza ejecutar el piloto, gastar tokens del presupuesto, instalar candidatas ni registrar decisiones.

## Qué tiene que responder

La evaluación en seco dejó dos preguntas que solo el uso puede contestar:

- **A.** ¿`frontend-design` mejora el diseño de una pantalla nueva frente a lo que ya existe —brief, tokens del proyecto y checklist v1—, sin romper la fuente única de tokens ni la marca?
- **B.** ¿Las reglas de `web-interface-guidelines`, fijadas por SHA y sin red, encuentran problemas reales que `design:accessibility-review`, aprobada el 2026-11-17, no encuentra?

Si la respuesta es no, la recomendación queda en no incorporar nada (VCX-P3). Un empate no alcanza para incorporar.

## Condiciones comunes

- **Disparador.** El de VCX-D060: un proyecto necesita revisar o diseñar una interfaz para tomar una decisión. Hoy lo cumple el encargo de diseño del evento en vivo de Teyst (brief v4, con pantallas en curso). El PO confirma el caso antes de empezar.
- **Dónde se ejecuta.** Los materiales, salidas y puntuaciones viven en una copia privada (`solera/docs/initiatives/ui-design-pilot-<fecha>/`), igual que el piloto de la checklist. `vcx` recibe solo un resumen sin código, rutas ni textos del proyecto (VCX-D032).
- **Sin instalar.** Cada candidata entra como un archivo de texto fijado por SHA y copiado con su licencia en la carpeta privada: `frontend-design` `e4bb5d9` (Apache-2.0) y `command.md` de `web-interface-guidelines` `434b7f9` (MIT). Nada se agrega a `.claude/`, `.agents/` ni a la configuración del agente. Ningún brazo usa red.
- **Revisores.** Subagentes `sonnet` sin conocimiento del piloto, con los mismos materiales en ambos brazos salvo la candidata. Solo pueden leer lo entregado. Si el entorno carga memoria o `AGENTS.md` del proyecto, la cargan los dos brazos por igual.
- **Puntuación independiente.** Otro agente, que no generó nada y no sabe qué brazo es cuál, puntúa contra criterios fijados en este documento. El PO decide.
- **Criterios congelados.** Los umbrales de abajo se fijan antes de medir. Si hace falta cambiarlos, se registra el cambio y la razón antes de ver resultados.
- **Corte.** Se detiene un brazo si supera su tope de tokens o si un revisor intenta instalar, usar red o escribir fuera de su carpeta.

## Piloto A: frontend-design

**Caso.** Una pantalla del brief que todavía no tenga diseño aprobado. La elige un agente que no conoce la skill, entre las que el PO marque como abiertas.

**Brazos.**

| Brazo | Entradas |
|---|---|
| Control | Brief v4, tokens del tema del proyecto, piezas de marca vigentes y checklist v1 |
| Skill | Lo mismo, más el texto de `frontend-design` |

**Salida pedida a cada corrida.** Un plan de diseño breve y un artboard HTML autocontenido de la pantalla, que use solo los tokens entregados, a 320, 375 y 1280 px. Es el mismo formato de los artboards del proyecto, así que se compara con lo que ya produce el flujo.

**Repeticiones.** Tres corridas por brazo, para no decidir con una sola como en el primer piloto de la checklist.

**Medidas.**

| Tipo | Medida | Cómo se obtiene |
|---|---|---|
| Primaria | Preferencia del PO | Pares ciegos X/Y, uno por repetición, con el orden sorteado. El PO elige o declara empate, sin saber el brazo |
| Primaria | Adherencia a tokens | Valores literales de color, tipografía y espaciado fuera de los tokens entregados. Se cuentan en el HTML; menos es mejor |
| Primaria | Piso de calidad | Seis ítems de `mobile-check`: sin scroll horizontal a 320 px, objetivos de 24 CSS px, foco visible, `prefers-reduced-motion`, contraste comprobado con herramienta y texto en español sin restos en inglés. Pasa o no pasa, sobre el render |
| Secundaria | Costo | Tokens e iteraciones por corrida |
| Secundaria | Notas del puntuador | Jerarquía, ajuste al brief y coherencia con la marca, con justificación escrita |

**Sesgo conocido.** La lista de «rasgos de UI generada» de la skill no se usa como medida: favorecería al brazo que la leyó. Por eso la medida principal es la preferencia ciega del PO.

**Regla de decisión.**

- **Pasa a evaluación formal** si el brazo con la skill gana la preferencia del PO en al menos 2 de 3 pares, y además no queda peor en adherencia a tokens (mediana) ni en el piso de calidad, y no supera en 1,5 veces el costo del control. Pasar significa solo que se prepara una evaluación persistida con evidencia de uso para la decisión del PO; no significa instalar.
- **Se archiva como antecedente** en cualquier otro caso, incluido el empate.

**Tope.** 400.000 tokens, con generación y puntuación incluidas. El piloto de la checklist costó unos 424.000.

## Piloto B: reglas web fijadas frente a design:accessibility-review

**Caso.** Una superficie web real con HTML o JSX: uno de los artboards HTML del proyecto o una página del build web. La elige un agente que no conoce las reglas.

**Brazos.** `design:accessibility-review` sola, y las reglas fijadas solas. Las dos revisiones son de solo lectura y no crean tickets: la reserva (2) de la aprobación de `design:accessibility-review` se respeta.

**Medidas.**

- Hallazgos clasificados por el puntuador contra el código: correctos, hipótesis bien marcadas o incorrectos (el mismo criterio del piloto 2 de la checklist).
- Hallazgos correctos únicos de cada brazo.
- Choques con las convenciones del español, por ejemplo Title Case o comillas inglesas, contados aparte. No cuentan como hallazgos.
- Tokens por brazo.

**Regla de decisión.**

- **Las reglas fijadas pasan a documento de Brix como checklist, no como skill,** si aportan al menos 3 hallazgos correctos únicos de severidad media o mayor y como mucho el 25 % de sus hallazgos son incorrectos. En ese caso se excluyen las reglas que chocan con el español y se registra la revisión fijada.
- **Se archivan** si no cumplen esas dos condiciones.

**Tope.** 200.000 tokens.

## Qué queda al terminar

- **En la copia privada:** materiales, salidas, puntuaciones y la tabla de preferencia del PO.
- **En `vcx`:** un resumen público con las medidas, la regla aplicada y sus límites, junto a esta carpeta.
- **Si alguna candidata pasa:** una evaluación persistida con `score-run.mjs evaluate`, ahora con `observedOutcome` respaldado, y la decisión del PO con `decide`. Las dos son acciones aparte.

## Antes de ejecutar hace falta

1. Que el PO confirme el caso, los dos topes de tokens y el modelo de los revisores.
2. Una autorización para copiar los dos textos fijados en la carpeta privada.
3. Que el PO reserve tiempo para los tres pares ciegos del piloto A (estimado: unos 15 minutos, sin medir).

## Límites

- Tres pares miden la preferencia de una persona en una pantalla; no generalizan.
- Un artboard HTML no prueba la implementación en React Native ni el comportamiento con red lenta.
- El puntuador es un modelo y puede compartir sesgos con los revisores.
