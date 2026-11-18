# Tooling UI/UX: segunda ronda de consolidación en seco

Fecha: 2026-11-17, con `--now 2026-11-18T00:00:00Z` fijo para la ronda. Las corridas fueron a las 01:02 UTC del 2026-11-18, así que ese `--now` queda una hora atrasado; con frescura de 7 días no cambia ningún número.

Estado: **evaluación en seco**. No es una admisión. No se registraron decisiones humanas, no se escribió en `docs/tooling/` y no se hizo commit.

No se instaló ni se activó ninguna candidata, ni se ejecutaron sus scripts, hooks o MCP. Lo descargado se leyó como dato no confiable, en el scratchpad de la sesión.

**Quién la hizo.** Claude Code con `claude-opus-5-5`, sin subagentes.

**Motor:** Brix `591c25f`, `cliTree` `af14043f`, política `ce6e1a31…` (sin cambios), fórmula 1.6.0.

## Por qué hay una segunda ronda

La consigna es la misma que originó la [ronda del 2026-11-16](../2026-11-16-ui-ux-tooling-consolidation-dry-run/README.md). Esta ronda no repite esa inspección: la conserva y mide solo lo que cambió desde entonces. Cambiaron tres cosas:

1. **El motor.** Brix pasó de `131a5c2` a `591c25f`. El commit `9eafbf1` hace que `evaluate` falle si no puede reunir comunidad, en vez de dejarla en `null` en silencio. La ronda anterior corrió sin token y las cuatro candidatas quedaron sin comunidad. Esta corrió con el token de `gh` y las cuatro la tienen.
2. **Los pilotos.** Los de [UI/UX Pro Max](../2026-11-16-ui-ux-pro-max-pilot/README.md) y de [Interface Review](../2026-11-16-interface-review-pilot/README.md) se ejecutaron después de la ronda anterior. Ahora alimentan `observedOutcome`.
3. **Un origen.** `jakubkrehel/skills` avanzó 8 commits el 2026-11-17, de `6c21201` a `2136b60`, y tocó 39 archivos del conjunto mínimo de Interface Review.

## 1. Consolidación

**Selección anterior, que se conserva sin cambios:** la tabla de identidad, la criba de `ibelick/ui-skills` y el tratamiento condicionado de shadcn y ehmo de la [ronda anterior](../2026-11-16-ui-ux-tooling-consolidation-dry-run/README.md#1-consolidación). Las decisiones del PO registradas en `docs/tooling/evaluations/` siguen como estaban.

**Origen por origen, al 2026-11-17** (API de GitHub, con token):

| Origen | SHA evaluado | ¿Cambió? | Licencia | Estrellas del repositorio |
|---|---|---|---|---|
| `nextlevelbuilder/ui-ux-pro-max-skill` | `e59ff37` | No | MIT | 150.898 |
| `jakubkrehel/skills` | `6c21201` → **`2136b60`** | **Sí**, 8 commits del 2026-11-17 | MIT | 12.323 |
| `ibelick/ui-skills` | `65cc0ed` | No | MIT | 11.156 |
| `ehmo/platform-design-skills` | `dc2be82` | No | MIT | 644 |
| `shadcn-ui/ui` | `968d8cb` (HEAD; no evaluada) | — | MIT | 128.425 |

**Las estrellas son del repositorio, no de la skill.** En los tres primeros son de una colección: 7 skills, 14 y 9. No miden la eficacia de la ruta evaluada. Ver la sección 3 sobre cómo pesan en el motor.

**Catálogos revisados de nuevo.** Aparecen cinco orígenes que la ronda anterior no nombraba. Se cribaron así:

| Origen | Qué es | Tratamiento |
|---|---|---|
| `sigmastudioz/agent-skills@58c61ad`: `ui-foundation-reuse` | Skill que trae un tarball de 2,1 MB con una biblioteca de efectos React (shaders, scroll, Three) y un script que la copia en la app | Fuera: no conserva sistemas de diseño, como sugiere su nombre. Distribuye código compilado y escribe en la app |
| `elayadesign/ai-design-skills` | 2 skills: Figma y landing pages | Fuera: Figma necesita `/mcp`; landing web se solapa con `anthropic-frontend-design`, aprobada |
| `MengTo/Skills` | 183 skills, en su mayoría efectos 3D y visuales | Fuera: sin necesidad declarada |
| `ConardLi/garden-skills` | 6 skills; `web-design-engineer` es la única de UI | Fuera: web, se solapa con `anthropic-frontend-design` |
| `alexiseverage/aesthetic-frontend-skills` (topic) | 2 skills experimentales de estética web, 58 estrellas | Fuera: web, sin señales de mantenimiento |

skillselion.com no agrega orígenes nuevos. El topic `ui-skills` tiene 9 repositorios; fuera de `ibelick/ui-skills`, ninguno pasa de 61 estrellas.

## 2. Respuestas específicas: qué cambió

Las respuestas de fondo están en la [ronda anterior](../2026-11-16-ui-ux-tooling-consolidation-dry-run/README.md#2-respuestas-específicas) y los pilotos las verificaron por ejecución. Aquí van solo los cambios.

### UI/UX Pro Max (`e59ff37`, sin cambios de código)

**Lo que el piloto confirmó por ejecución:**

- `--stack` se ignora en `--design-system`;
- `--rtl` da error en ese modo;
- `--force` sobrescribe sin preguntar;
- sin `--force`, un MASTER existente se saltea sin aviso;
- la salida ascii no avisa cuando usa defaults.

**Lo que el piloto corrigió:**

- En español y sin coincidencias, la tipografía no cae en Inter: sale de coincidencias débiles (Outfit + Work Sans). Esta ronda corrige ese texto en `fit.capabilityGapCoverage`.
- La página de overrides apunta a `design-system/MASTER.md`, aunque el MASTER real esté en `design-system/<slug>/`.

**Cómo conserva un sistema existente.** Por código, no lo conserva. En el A/B con la marca Tintum, la rama con la skill no cambió tokens, pero porque el agente descartó la recomendación: la herramienta propuso una paleta azul e Inter + Playfair. No aportó nada que la rama sin skill no obtuviera, y costó 7 % más de tokens y 47 % más de tiempo.

**Recuperación frente a calidad.** Sigue igual: hay evidencia de recuperación (P@1 0,816 sobre 90 casos de los mantenedores) y ninguna de calidad del resultado.

### Interface Review (`2136b60`)

**Qué cambió en el conjunto mínimo**, leído en el diff `6c21201...2136b60`:

- Cada `better-*` pasó su escala de severidad y su formato a un `reporting.md` nuevo. Ahora son 44 archivos, 3.731 líneas y unos 195 KB.
- `scope-resolution.md` define cada objetivo: `working` incluye lo no rastreado y `staged` se lee con `git show :ruta`.
- `SKILL.md:103` aclara que una eliminación sin reemplazo leída del diff es un hallazgo de fuente y no necesita render.
- `removed-signals.md` agrega `<label`, `<button`, `<a`, `<nav`, `<main`, `<ul`, `motion-safe` y `motion-reduce` al grep de eliminaciones. Sigue sin patrones de React Native (`accessibilityLabel`, `accessibilityRole`).
- Los disparadores de escalamiento quedan exentos del tope de 15 hallazgos.

**Lo que no cambió:**

- las reglas de Git: sin `checkout`, `switch` ni `stash`;
- las escrituras en `.git`: `remote set-head`, `fetch --deepen` y refs de PR;
- `git worktree add /tmp/review-<n>` para el render.

Siguen siendo compatibles con las reglas locales en lo que prohíben. Las escrituras permitidas no se dispararon en el piloto y siguen sin probarse.

**Fuera del conjunto mínimo.** La colección sumó `upskill`, que lee el historial completo de sesiones del agente. Es de invocación manual y su texto prohíbe enviar el historial afuera, pero no se adoptaría: lee datos privados por diseño.

**El piloto fue sobre `6c21201`.** Los archivos que ejercitó cambiaron después. Los cambios son aclaraciones y no tocan la resolución del alcance ni las reglas de Git, así que se cita como resultado observado. Que se transfiera a `2136b60` es un supuesto, declarado en la evidencia.

## 3. Resultados del motor (en seco)

| ID | Revisión | Score | Comunidad | Fit | Riesgo | Confianza | Cobertura | Recomendación base |
|---|---|---|---|---|---|---|---|---|
| `ui-ux-pro-max-core` | `e59ff37` | **62,3** | 87,6 | 31,4 | medium | high (95) | 98 % | **advance_with_reservations** |
| `ui-skills-improve-ui` | `65cc0ed` | 54,5 | 59,4 | 40,3 | medium | high (92) | 93 % | do_not_advance |
| `interface-review-minset` | `2136b60` | 51,3 | 54,2 | 36,1 | high | high (95) | 98 % | do_not_advance |
| `platform-design-skills` | `dc2be82` | 38,7 | 35,2 | 32,0 | low | high (90) | 93 % | do_not_advance |

La cobertura es un cálculo propio: la suma de pesos de los subfactores `available` más comunidad, según la política. El motor no la imprime.

**`ui-ux-pro-max-core` sube a `advance_with_reservations` solo por las estrellas.**

- Su comunidad es 87,6 porque el repositorio tiene 150.898 estrellas, que comparten sus 7 skills.
- Su `fit` es el más bajo de las cuatro con datos propios: 31,4.
- Sin comunidad, renormalizando los pesos, daría unos 56,0, y quedaría en `do_not_advance` como en la ronda anterior (56,2). El cálculo es aritmética propia sobre la salida del motor, no una corrida.
- El resultado observado del piloto le baja el `fit`: `observedOutcome` 30.

**Esta subida no se trata como evidencia de eficacia.** Es el caso que la consigna pide no confundir: la popularidad del monorepo no es eficacia de la ruta núcleo. Advertir esto no cambia pesos ni política, y el número del motor se informa tal cual.

**Cambios frente a la ronda anterior:**

| ID | 2026-11-16 | 2026-11-17 | Qué lo movió |
|---|---|---|---|
| `ui-ux-pro-max-core` | 56,2 dna | 62,3 awr | Entra la comunidad (+); `observedOutcome` 30 y `reversibility` de 65 a 60 (−) |
| `ui-skills-improve-ui` | 53,2 dna | 54,5 dna | Solo la comunidad |
| `interface-review-minset` | 50,3 dna | 51,3 dna | La comunidad, `observedOutcome` 50 y la revisión nueva: `commitContinuity` de 75 a 70, `operatingOverhead` de 45 a 40 |
| `platform-design-skills` | 39,6 dna | 38,7 dna | Solo la comunidad, que pesa en contra: 644 estrellas y estancada |

dna = do_not_advance, awr = advance_with_reservations.

**Límites:**

- La confianza alta mide cobertura y fuente, no eficacia.
- Los subfactores de rúbrica son juicio de este evaluador. Los no medidos de nuevo llevan la nota «Medida el 2026-11-16 en la ronda anterior».
- `observedAdoption` sigue `unavailable` en las cuatro: nadie las usa en VCX.
- Los pilotos son de una corrida por caso. `observedOutcome` es una rúbrica sobre esas corridas, no una tasa.

## 4. Comparación por necesidad

Los puntajes de otras rondas se citan tal como se informaron. Ninguno se volvió a correr con el motor nuevo, salvo los cuatro de esta ronda.

| Necesidad | Existente | Candidatas: score, riesgo y base | Solapamientos | Dependencias y costos | Pendiente |
|---|---|---|---|---|---|
| Dirección visual y sistemas de diseño | `anthropic-frontend-design`, aprobada con reservas tras un piloto (`6d259c4`): web, sin React Native. Tokens propios de Teyst y marca Tintum | `ui-ux-pro-max-core` 62,3 medium awr (por comunidad) · `ui-craft-skill-minimal` 68,3 medium awr · `interface-design` 52,7 · `taste` 52,3 high | Todas recomiendan estilo genérico por industria. Ninguna lee el sistema existente por código. El piloto mostró que lo que protege la marca es el agente | Pro Max: `python3`, escribe en el cwd. Las demás: Markdown | Una pantalla nueva de Teyst con dirección por resolver |
| Usabilidad y accesibilidad | `design:accessibility-review` y `design:ux-copy` aprobadas; checklist v1 (VCX-D060); `mobile-check` | `wondelai-ux-heuristics` 59,5 low · `ui-skills-improve-ui` 54,5 medium dna · `vercel-web-design-guidelines` 50,5 high | `improve-ui` repite la checklist y `accessibility-review`. Ninguna prueba cumplimiento: recomiendan | `improve-ui`: ninguna; escribe en `design-plans/` | Disparador de VCX-D060 |
| Regresiones de interfaz | `browser` MCP para lo renderizado; `code-review`; checklist v1 | `interface-review-minset` 51,3 high dna | La clasificación causal es única. La detección se solapa con `accessibility-review` | `git`; `gh` autenticado para PRs; unos 195 KB de contexto, cargado en parte | Un consumidor web con flujo de PR |
| Especialización por plataforma | Ninguna. `mobile-app-ui-design` rechazada | `platform-design-skills` 38,7 low dna. shadcn excluida por stack | Las HIG y Material oficiales | Ninguna; incluye un PDF de Apple redistribuido | Una decisión de UI nativa en Teyst |

**Costo de cupo de suscripción:** no medido (no disponible). Ninguna ruta evaluada usa servicios pagos ni claves.

**No agregar nada** sigue siendo la línea de base. El piloto de Pro Max la puso a prueba directamente: la rama sin skill igualó a la rama con skill, con menos costo.

## 5. Recomendación

**Conjunto mínimo hoy: no agregar herramientas.** Se sigue con lo que ya está aprobado:

- `anthropic-frontend-design`, para dirección visual en web;
- `design:accessibility-review` y `design:ux-copy`;
- `browser` MCP para lo renderizado;
- la checklist v1 bajo VCX-D060.

**Por qué, aunque Pro Max ahora dé `advance_with_reservations`:**

- La subida viene solo de las estrellas del monorepo.
- El único resultado observado muestra valor incremental bajo y una recomendación que contradice la marca.
- Agregarla sumaría `python3`, escrituras en el cwd y una superficie que el agente tiene que filtrar.

**Al activarse el disparador de VCX-D060** no cambia el orden de la ronda anterior:

- **Dirección visual:** pilotar primero `ui-craft-skill-minimal`. Pro Max queda como consulta sin `--persist` y solo para ideas en inglés.
- **Regresiones:** Interface Review, solo con un consumidor web y flujo de PR.
- **Plataforma:** las HIG y Material oficiales, antes que una destilación.

**Evidencia que cambiaría esta recomendación:**

- **Para Pro Max:** un piloto ciego con varias corridas donde la rama con skill supere a la línea de base en una tarea de dirección visual nueva, no de conservación de marca.
- **Para Interface Review:** que el caso 7 se resuelva leyendo el árbol de accesibilidad renderizado y que la skill acierte el juicio de equivalencia en React Native; o que aparezca un consumidor web.
- **Para cualquiera:** una métrica de comunidad por skill y no por repositorio. Movería los puntajes de las colecciones, pero no su eficacia.

## 6. Piloto propuesto (no ejecutado)

Completa lo que los pilotos del 2026-11-16 dejaron abierto. **Requiere autorización:** ejecutar scripts de las candidatas y copiar skills en repositorios de prueba, nunca globalmente ni en `~/.claude`.

**Método:** el mismo, con criterios fijados antes de medir. Agrega dos cosas: revisor ciego distinto del operador y tres corridas por rama.

| # | Candidata | Caso | Qué se observa |
|---|---|---|---|
| A | UI/UX Pro Max | Dirección visual para una pantalla nueva sin marca previa, en inglés: con skill frente a sin skill, tres corridas por rama | Preferencia del revisor ciego, defectos de contraste medidos con herramienta, tokens consumidos y tiempo |
| B | Interface Review `2136b60` | Repetir el caso 7 y renderizar en react-native-web para leer el árbol de accesibilidad | Si el nombre efectivo cambia al quitar `accessibilityLabel`; si el descarte de la skill fue correcto |
| C | Interface Review `2136b60` | Repetir el caso 8 en la revisión nueva | Que el resultado de `6c21201` se transfiera: 3 de 3 detectados y bien clasificados |
| D | Interface Review `2136b60` | Repositorio sin `origin/HEAD`, con remoto local, y objetivo `pr <n>` simulado con refs | Si corre `remote set-head` o `fetch` de refs de PR, con fotos de `.git` antes y después |

Las medidas son las de la ronda anterior. El caso A es el que podría cambiar la recomendación sobre Pro Max; B a D solo afinan Interface Review.

## 7. Juicio orientativo de 1 a 10 (VCX-P2)

Separado del motor y no comparable entre evaluaciones.

| Candidata | Nota | Cambio | Motivo |
|---|---|---|---|
| `interface-review-minset` | 5 | = | El piloto confirmó el diseño en web. Los descuentos siguen: solo web, sin CI ni versiones, alta rotación |
| `ui-ux-pro-max-core` | 4 | = | El piloto confirmó los defectos y mostró valor incremental bajo. La subida del motor viene de las estrellas, no de la herramienta |
| `ui-skills-improve-ui` | 4 | = | Sin evidencia nueva |
| `platform-design-skills` | 3 | = | Sin evidencia nueva |

## Archivos

| Archivo | Qué es |
|---|---|
| `<id>.evidence.json` | Evidencia según el contrato de subfactores de Brix. Parte de la ronda anterior y aplica solo los cambios medidos hoy |
| `<id>.dry-run.out` | Salida completa de `score-run.mjs evaluate … --dry-run` |

El generador de la evidencia quedó en el scratchpad de la sesión. Lo que cambia, candidata por candidata:

- **`ui-ux-pro-max-core`:**
  - `observedOutcome` pasa a `available`, con 30;
  - `reversibility` baja a 60, por la ruta de la página de overrides y la omisión silenciosa;
  - se corrige el texto de `capabilityGapCoverage`.
- **`interface-review-minset`:**
  - `evaluatedRef` pasa a `2136b60`;
  - `observedOutcome` pasa a `available`, con 50;
  - `activityRecency` queda en 95 y `commitContinuity` baja a 70;
  - `adoptionSimplicity` queda en 45, con el tamaño nuevo;
  - `documentationQuality` queda en 75 y `operatingOverhead` baja a 40;
  - se corrige el texto de `capabilityGapCoverage`.
- **`ui-skills-improve-ui` y `platform-design-skills`:** sin cambios de puntaje.

En las cuatro, los subfactores que no se midieron de nuevo llevan la nota «Medida el 2026-11-16 en la ronda anterior».

## Reproducir

Desde la raíz de VCX, una candidata por vez, con `gh` autenticado:

```bash
node docs/tooling/score-run.mjs evaluate --input docs/superpowers/reports/2026-11-17-ui-ux-tooling-consolidation-dry-run/<id>.evidence.json --now 2026-11-18T00:00:00Z --operator "Claude Code (claude-opus-5-5); evaluación en seco solicitada" --dry-run
```

La comunidad depende de la API de GitHub en el momento de la corrida. Repetirla otro día puede mover las estrellas y el score.

## Comprobación de lo que no cambió

Antes y después de las corridas coinciden estos SHA-256:

- política: `ce6e1a31…`;
- `score-runs.jsonl`: `46ae0560…`;
- `score-run.mjs`: `edace44e…`;
- matriz: `f09b0840…`;
- conjunto de `docs/tooling`: `c5fd86ce…`.

En Brix, `git status --porcelain --ignored -- packages/cli` sale vacío.

Esta ronda creó solo los 9 archivos de esta carpeta. Fuera del repositorio quedaron los clones, los catálogos descargados y el generador, en el scratchpad de la sesión.

**Consumo:** sin subagentes. El consumo del agente principal y el costo en dinero no están disponibles. El contador de la API de GitHub pasó de 84 a 149 consultas usadas durante la sesión, con el token del usuario; el cupo es de 5.000 por hora. El contador es de la cuenta: puede incluir consultas de otras sesiones.
