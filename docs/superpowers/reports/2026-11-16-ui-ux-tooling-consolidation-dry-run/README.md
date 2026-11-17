# Tooling UI/UX: consolidación y evaluación en seco

Fecha: 2026-11-16, con `--now 2026-11-17T00:20:00Z` fijo para la ronda. Las corridas fueron a las 00:12 UTC, así que ese `--now` queda 8 minutos adelantado; con frescura de 7 días no cambia ningún número.

Estado: **evaluación en seco**. No es una admisión. No se registraron decisiones humanas, no se escribió en `docs/tooling/` y no se hizo commit.

No se instaló ni se activó ninguna candidata, ni se ejecutaron sus scripts, hooks o MCP. Todo lo descargado se leyó como dato no confiable, en el scratchpad de la sesión.

**Quién la hizo.** El operador fue Claude Code con `claude-opus-5-5`. Tres subagentes de solo lectura inspeccionaron las candidatas. El agente principal verificó contra los clones las afirmaciones de mayor peso: `--stack` y `--rtl` en `search.py:150-165`, la ruta de escritura en `design_system.py:1236-1251`, `interface-review/SKILL.md:97,101-103` e `improve-ui/SKILL.md:12-13`.

**Fuentes de esta ronda:**

- [agenticskills.io/category/design](https://agenticskills.io/category/design);
- [skillselion.com/design](https://skillselion.com/design);
- [github.com/topics/ui-skills](https://github.com/topics/ui-skills);
- [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill).

**Motor:** Brix `131a5c2`, `cliTree` `b4c92762`, política `ce6e1a31…`, fórmula 1.6.0.

## Archivos

| Archivo | Qué es |
|---|---|
| `<id>.evidence.json` | Evidencia según el contrato de subfactores de Brix: 23 subfactores, con `unavailable` donde falta el dato |
| `<id>.dry-run.out` | Salida completa de `node docs/tooling/score-run.mjs evaluate … --dry-run` |

**Redacción para publicar.** Antes del commit se quitó de las evidencias, de las salidas y de este README la ruta del archivo de tokens de Teyst, que es privado. La frase quedó como «tokens propios». Ese texto vive en `rationale` y `evidenceRefs`, que no entran en el cálculo: ningún score, riesgo ni confianza cambia. Las salidas `.dry-run.out` llevan esa misma redacción y no se volvieron a generar.

## 1. Consolidación

**Selección anterior, que se conserva:**

- La ronda [`2026-11-16-ui-ux-design-skills-dry-run`](../2026-11-16-ui-ux-design-skills-dry-run/README.md), sin commit.
- La ronda «Taste Skill y Kimi», commit `87b2f46` en la rama de otra sesión. Su carpeta ya no está en este checkout.
- Las decisiones del PO que otra sesión persistió el 2026-11-17 a las 00:02 UTC en `docs/tooling/evaluations/`, sin commit:
  - `design-accessibility-review` y `design-ux-copy`: `approved`.
  - `impeccable`, `emilkowalski-skills` y `mobile-app-ui-design`: `rejected`, vencen el 2027-02-15.

Esta ronda no tocó nada de eso.

**Regla de identidad:** una candidata es origen + ruta + revisión. Aparecer en varios catálogos no es evidencia independiente.

**Las métricas de los catálogos no son evidencia por skill:**

- Las estrellas son del repositorio fuente y en un monorepo las comparten todas sus skills. La metodología de agenticskills.io lo dice.
- Los installs de skillselion vienen de skills.sh y nadie los verifica. agenticskills.io no los publica.

| Origen, ruta y SHA | Tipo | Catálogos | Tratamiento |
|---|---|---|---|
| `nextlevelbuilder/ui-ux-pro-max-skill@e59ff37`: plugin, 7 skills | Colección más instalador (CLI `uipro`) | aS, sS | Ronda anterior: 62,8, riesgo high |
| Mismo SHA, ruta `.claude/skills/ui-ux-pro-max` + `src/ui-ux-pro-max`, copia manual | Skill con biblioteca local (Python stdlib, CSV) | — | **Esta ronda**: `ui-ux-pro-max-core` |
| `jakubkrehel/skills@6c21201`: `interface-review` + `better-interface` + 6 `better-*` | Conjunto mínimo de una colección de 14 | aS ×2 | **Esta ronda**: `interface-review-minset` |
| `ibelick/ui-skills@65cc0ed`: `skills/improve-ui` | Skill de una colección que además trae sitio, CLI y MCP remoto | gT | **Esta ronda**: `ui-skills-improve-ui` |
| `ibelick/ui-skills`: las otras 8 skills | Skills | gT | Criba (abajo) |
| `ehmo/platform-design-skills@dc2be82` | Colección de 8 plataformas | aS | **Esta ronda**, condicionada: `platform-design-skills` |
| `shadcn-ui/ui@e62c943`: `skills/shadcn` | Skill que envuelve un CLI e instalador, con MCP | aS | No evaluada: no hay consumidor con React DOM y Tailwind |
| `anthropics/skills`: frontend-design | Skill | aS, sS | Ronda anterior: 59,0 |
| `vercel-labs/agent-skills`: web-design-guidelines | Skill | aS, sS | Ronda anterior: 50,5 |
| `pbakaus/impeccable`, `emilkowalski/skills` | Skill / colección | aS, sS | Rechazadas por el PO, vigentes |
| `Leonxlnx/taste-skill`, `educlopez/ui-craft` | Skills | aS, sS / — | Ronda Taste y Kimi: 52,3 y 68,3 |
| `anthropics/knowledge-work-plugins/design` | Colección y plugin | aS | `accessibility-review` y `ux-copy` aprobadas; el resto no evaluado |
| `openai/skills` (figma), `heygen-com/hyperframes`, `Owl-Listener/designer-skills`, repos chicos del topic | Servicio o colección | aS, sS, gT | Fuera de necesidad o sin necesidad declarada |

aS = agenticskills.io, sS = skillselion.com, gT = topic de GitHub.

**Criba de `ibelick/ui-skills`, herramienta por herramienta:**

| Skill | Por qué queda fuera |
|---|---|
| `baseline-ui` | Tailwind es MUST, más `motion/react` y DOM. Edita código |
| `fixing-accessibility` | HTML y ARIA del DOM. Edita código. Se solapa con `design:accessibility-review`, ya aprobada |
| `fixing-metadata` | SEO y metadatos: no es UI/UX |
| `fixing-motion-performance` | CSS, WAAPI y GSAP sobre el DOM |
| `create-design-md` | Ejecuta `npx @google/design.md` (red y código externo) |
| `component-canvas` | Rutas web y DOM. Crea código |
| `create-canvas` | Rutas web y DOM. Crea código |
| `ui-skills-root` | Ejecuta `npx ui-skills` y descarga del registro sin versión fija |
| **`improve-ui`** | **No queda fuera.** Es la única que no depende del stack. Solo escribe en `design-plans/`: evaluada |

**shadcn y ehmo, condicionadas.** No se inventó ninguna necesidad.

- **shadcn** exige React DOM, Tailwind y `components.json`.
  - Al cargarse ejecuta `!npx shadcn@latest info --json`, sin versión fija, y pre-autoriza `npx shadcn@latest *`.
  - Teyst, el único consumidor con interfaz, usa Expo y React Native.
  - Se reabre solo si aparece un consumidor web con ese stack.
- **ehmo** se evaluó porque Teyst publica en iOS y Android. Aun así, hoy ninguna decisión de plataforma está abierta.

## 2. Respuestas específicas

### UI/UX Pro Max (`e59ff37`), según el código leído y sin ejecutarlo

**Búsqueda y datos: es recuperación.**

- Un BM25 propio, con k1 = 1,5 y b = 0,75, sobre 13 CSV de dominio y 22 de stacks, en inglés (`core.py:291-356`).
- Hay 192 productos, 89 estilos, 192 paletas y 120 guías UX.
- Si el mejor puntaje no supera un piso por dominio, se abstiene y sugiere términos (`core.py:212-222,500-519`).
- La procedencia de los datos es parcial: `data-provenance.json` cubre 31 de 192 reglas, y 62 de sus 117 referencias apuntan a otros CSV del mismo repositorio.

**Generación.**

1. Hace una búsqueda top-1 en `product`.
2. Toma la regla de `ui-reasoning.csv` por igualdad de categoría.
3. Aplica condiciones `if_*` sobre subcadenas en inglés.
4. Hace búsquedas multidominio; la prioridad canónica de la regla gana sobre BM25.
5. Elige la paleta y completa con defaults fijos (`design_system.py:478-636`).

**Calidad.**

- El evaluador de relevancia usa 90 casos curados por los mantenedores y da P@1 0,816.
- Sus umbrales se declaran «provisional-baseline-regression-gate», no objetivos de calidad.
- **No hay evidencia de calidad visual ni de usabilidad del resultado.**

**`--design-system` con `--stack` y `--rtl`** (`search.py:150-165`, verificado):

- `--stack` se ignora: solo se imprime una nota en stderr y no se pasa al generador.
- `--rtl` aborta con error.
- `--rtl` no hace layout RTL: filtra filas por la columna `rtl_level` y exige `--domain style|product`.

**Persistencia** (`design_system.py:1189-1251`):

- Sin `--output-dir`, escribe `design-system/<slug>/MASTER.md` y crea `pages/` en el cwd.
- Sin `--force`, crea cada archivo de forma exclusiva y salta los que ya existen. Puede quedar un conjunto mezclado: `pages/` nuevas o `tokens.json` junto a un MASTER viejo.
- Con `--force`, `os.replace` sobrescribe sin preguntar. El resguardo es solo texto, en `SKILL.md:112-114`.

**Tokens:** DTCG JSON o variables CSS `:root`. Las secciones `primitive`, `component` y `dark` quedan vacías: el formateador las busca, pero el generador no las produce.

**Overrides de página:** salen del dict en memoria, no del MASTER en disco.

**Sistema de diseño existente: no lo conserva por código.**

- No lee el MASTER previo ni los tokens del proyecto; solo comprueba si el archivo existe.
- Para Teyst, sus tokens propios y la marca Tintum quedarían fuera del cálculo. Preservarlos depende de que el agente lo haga.

**Español y casos sin coincidencias.**

- No hay folding de acentos, stemming ni stopwords en español.
- «modo oscuro» no activa el modo oscuro.
- Sin coincidencias en `--design-system`, la categoría queda en «General» y no existe regla para ella. Entra el reasoning por defecto (Hero, Features, CTA y Minimalism) con colores #2563EB, #3B82F6 y #F97316 e Inter.
- El indicador `reasoning_default` aparece solo con `--json`. En ascii, markdown y MASTER.md los defaults se ven como recomendación (`design_system.py:394-408,557-608`).

**Marca contra industria:** no hay entrada de marca ni prioridad sobre la regla de industria. La sub-skill `brand` es otro camino, que reescribe `assets/design-tokens.json`.

**Accesibilidad.**

- **Lo que verifica:** `validate_data.py` calcula el contraste WCAG real de cada paleta del CSV, y corre en CI.
- **Lo que no verifica:** el sistema generado solo valida el ring y el texto del botón outline.
- **Lo que solo informa:** la preview muestra insignias AA y AAA.
- **Lo que no existe:** auditoría de teclado, foco o ARIA.

Recomendar contraste no es cumplimiento probado.

**Fuera de la ruta núcleo.** Esto es lo que lleva a la ronda anterior a riesgo high.

- `design/logo` llama a Gemini, AtlasCloud, MuAPI y UberLLM, todas APIs pagas, y lee `.env` de `~/.claude`.
- El CLI usa `GITHUB_TOKEN` del entorno, borra instalaciones anteriores con `rm -rf` y se actualiza solo con `npm install -g`.
- `stack/.claude/settings.json` declara `Read(//home/**)` y `enableAllProjectMcpServers: true`, con MCP `@latest`.

Todo esto se registra como hallazgo; no se siguió ninguna de esas instrucciones.

### Interface Review (`jakubkrehel/skills@6c21201`)

**Conjunto mínimo funcional** (verificado):

- 8 carpetas: `interface-review`, `better-interface`, `better-accessibility`, `better-layout`, `better-writing`, `better-typography`, `better-colors` y `better-ui`.
- 38 archivos `.md`, 3.810 líneas, unos 199 KB.
- Sin `better-interface` se detiene después del inventario (`SKILL.md:97`).
- Si falta una `better-*`, ese dominio queda «Not reviewed».
- Los `agents/openai.yaml` son solo para Codex.

**Resolución del diff.**

- Sin objetivo explícito revisa `merge-base origin/<default>..HEAD` más lo no commiteado. Si no hay ninguno de los dos, pregunta y nunca cae en `HEAD~1`.
- Acepta `working`, `staged`, `branch`, `pr <n>`, una ref y rangos con dos o tres puntos. Se detiene si hay un rebase o un merge en curso.

**Clasificación causal.**

- Cada hallazgo es `Introduced`, `Regression` o `Pre-existing`, comprobado con `git blame`.
- Severidad HIGH, MEDIUM o LOW, tope de 15 hallazgos y veredicto Block o Approve, que cuenta solo Introduced y Regression.
- Cita `ruta:línea` contra la ref de head.

**Cobertura.**

- Excluye corrección, tests, seguridad y rendimiento.
- **Es revisión estática.** La verificación renderizada es opcional y no nombra herramienta: ni Playwright, ni MCP, ni axe.
- No calcula contraste: exige no informar valores que no se midieron, y deja la medición al agente.
- **Solo web.** Sus señales son HTML, CSS, ARIA y Tailwind. No menciona React Native, Expo, StyleSheet ni `accessibilityLabel`.

**Git y permisos, frente a las reglas locales.**

- **Compatible:**
  - No usa `add -A`, `--ours` ni `--theirs`, `--force`, `commit`, `push` ni `--no-verify`.
  - Prohíbe `checkout`, `switch`, `stash` y `gh pr checkout`.
- **Escrituras en `.git` sin preguntar:** `git remote set-head origin --auto`, `fetch --deepen` y `fetch` de refs de PR.
- **Escritura fuera del repositorio:** `git worktree add /tmp/review-<n>`, solo para verificación renderizada.
- **Red:** `gh` usa red con la sesión del usuario.
- `afk`, de la misma colección pero fuera del conjunto mínimo, hace commits sin que se los pidan: no se adoptaría.

## 3. Resultados del motor (en seco)

**Esta ronda:**

| ID | Revisión | Score | Riesgo | Confianza | Cobertura | Recomendación base |
|---|---|---|---|---|---|---|
| `ui-ux-pro-max-core` | `e59ff37` | 56,2 | medium | high (85) | 75 % | do_not_advance |
| `ui-skills-improve-ui` | `65cc0ed` | 53,2 | medium | high (83) | 72,75 % | do_not_advance |
| `interface-review-minset` | `6c21201` | 50,3 | high | high (85) | 75 % | do_not_advance |
| `platform-design-skills` | `dc2be82` | 39,6 | low | high (81) | 72,75 % | do_not_advance |

**Límites:**

- **`community` quedó `unavailable` en las cuatro.** La API de GitHub sin token tenía el cupo agotado (`remaining: 0`) y no se pasó un token. Además, en tres de las cuatro las estrellas serían de una colección, no de la skill.
- **`observedAdoption` y `observedOutcome` son `unavailable`:** no hubo piloto.
- **La confianza alta mide cobertura y fuente, no eficacia.** Sin snapshot de comunidad, la frescura y la consistencia valen 100 por construcción.
- **Los subfactores de rúbrica son juicio de este evaluador.** Las puntuaciones entre rondas no son del todo comparables.
- **Ejemplo de esa diferencia:**
  - El plugin `ui-ux-pro-max` sacó 62,8 y la ruta núcleo 56,2. La diferencia no es solo de alcance.
  - Esta ronda bajó `releaseContinuity` de 75 a 50, porque la release está detenida desde agosto y el workflow falla, y `fit`, porque `--stack` se ignora y en español cae en defaults.
  - El núcleo sale con riesgo medium, no high, porque no incluye `broadScope`.

## 4. Comparación por necesidad

Los puntajes de las rondas anteriores se citan tal como se informaron.

| Necesidad | Existente | Candidatas, con score, riesgo y base | Solapamientos | Pendiente |
|---|---|---|---|---|
| Dirección visual y sistemas de diseño | Ninguna vigente desde que `impeccable` y `emilkowalski-skills` se rechazaron. Teyst tiene tokens propios y marca Tintum | `ui-craft-skill-minimal` 68,3 medium awr · `ui-ux-pro-max` plugin 62,8 high awr · `ui-ux-pro-max-core` 56,2 medium dna · `anthropic-frontend-design` 59,0 medium dna · `interface-design` 52,7 · `taste` 52,3 high | Todas recomiendan estilo genérico. Ninguna lee el sistema existente por código | Piloto con marca real (§6) |
| Usabilidad y accesibilidad | `design:accessibility-review` y `design:ux-copy` aprobadas (61,7 y 63,3, low, sin commit); checklist v1 (VCX-D060) | `wondelai-ux-heuristics` 59,5 low · `ui-skills-improve-ui` 53,2 medium · `vercel-web-design-guidelines` 50,5 high | `improve-ui` y `wondelai` repiten la checklist v1 y `accessibility-review`. Ninguna prueba cumplimiento: recomiendan | Disparador de VCX-D060 |
| Regresiones de interfaz | `browser` MCP (asignado) para lo renderizado; `code-review`; checklist v1 | `interface-review-minset` 50,3 high dna | La clasificación causal es única. La detección se solapa con `accessibility-review` | Un consumidor web con PR |
| Especialización por plataforma | Ninguna; `mobile-app-ui-design` rechazada | `platform-design-skills` 39,6 low dna. `apple-design-skill`, bloqueada por no tener licencia (ronda Taste y Kimi). shadcn excluida por stack | Las HIG y Material oficiales son la alternativa directa | Una decisión de UI nativa en Teyst |

awr = advance_with_reservations; dna = do_not_advance.

**Dependencias y costos de las cuatro de esta ronda:**

- Ninguna usa servicios pagos ni claves en la ruta evaluada.
- **`ui-ux-pro-max-core`** necesita `python3` y escribe en el cwd.
- **`interface-review-minset`** necesita `git` y `gh` autenticado para PRs, y carga unos 199 KB de contexto.
- **`improve-ui`** y **ehmo** no tienen dependencias.
- **Costo de cupo de suscripción:** no medido (no disponible).

**No agregar nada** es la línea de base: lo existente cubre usabilidad y accesibilidad por recomendación, y lo renderizado con `browser`.

## 5. Recomendación

**Conjunto mínimo hoy: no agregar herramientas.**

- Seguir con `design:accessibility-review`, `design:ux-copy`, `browser` y la checklist v1 bajo VCX-D060.
- Ninguna de las cuatro candidatas de esta ronda alcanza `advance_with_reservations`.
- Ninguna tiene un resultado observado.
- La única necesidad sin herramienta, dirección visual, no tiene hoy un consumidor con decisión pendiente.

**Al activarse el disparador de VCX-D060:**

- **Dirección visual:** pilotar primero `ui-craft-skill-minimal` (recomendación de la ronda Taste y Kimi). UI/UX Pro Max queda como alternativa secundaria y solo en modo consulta (`--domain ux`, sin `--persist`), porque no conserva sistemas existentes ni entiende español.
- **Regresiones:** `interface-review-minset` solo si aparece un consumidor web con React DOM y flujo de PR. En Teyst la mayoría de sus señales no aplican.
- **Plataforma:** consultar las HIG y Material oficiales antes que una destilación estancada que redistribuye el PDF de Apple.

**Evidencia que cambiaría esta recomendación:**

- Un piloto donde UI/UX Pro Max, con un brief en español y la marca Tintum, preserve los tokens propios de Teyst y supere a la línea de base sin skill.
- Un consumidor web con Tailwind o shadcn: reabre shadcn y las skills de ibelick.
- Una decisión de UI nativa en Teyst: justifica pilotar reglas de plataforma.
- Datos de comunidad cambiarían el score, pero no la eficacia.

## 6. Piloto propuesto (no ejecutado)

**Requiere autorización:** ejecutar los scripts de Python de UI/UX Pro Max y copiar skills en un repositorio de prueba, nunca globalmente ni en `~/.claude`.

**Método:** el del piloto UX del 2026-11-09. Revisores ciegos, línea de base sin skill y criterios fijados antes de medir.

**Medidas:**

- defectos detectados;
- falsos positivos;
- cambios no pedidos a marca o tokens;
- escrituras observadas (`git status` y `find -newer` antes y después; refs de `.git`);
- tokens consumidos;
- tiempo.

| # | Candidata | Caso | Qué se observa |
|---|---|---|---|
| 1 | UI/UX Pro Max | «App para catas de vino entre amigos, con ligas y ranking», en español, con `--design-system --json` | Si `reasoning_default` es true y si el agente lo declara o presenta los defaults como recomendación |
| 2 | UI/UX Pro Max | La misma consulta en inglés | Línea de base: ¿coincide con la fila Brewery/Winery? |
| 3 | UI/UX Pro Max | Sin coincidencias: «trazabilidad de barricas de roble para cooperativas» | Abstención en la búsqueda simple; defaults en `--design-system` |
| 4 | UI/UX Pro Max | Marca Tintum (burdeos sobre crema, letras redondeadas) contra la recomendación por industria | Diferencias con los tokens propios de Teyst; si el agente conserva la marca sin que se lo pidan dos veces |
| 5 | UI/UX Pro Max | `--design-system --stack react-native` y `--design-system --rtl full` | Nota en stderr y error, como dice el código |
| 6 | UI/UX Pro Max | MASTER.md previo; correr sin `--force` y con `--force` en un directorio temporal | Conjunto mezclado sin `--force`; sobrescritura con `--force` |
| 7 | Interface Review | Diff de Teyst que quita un `accessibilityLabel` | Esperado: no lo detecta |
| 8 | Interface Review | Diff web equivalente que quita un `aria-label`, más un defecto previo plantado | Detección y clasificación Introduced o Pre-existing |
| 9 | Interface Review | Alcance `working` con árbol limpio y rama al día | Que pregunte en vez de revisar `HEAD~1`; refs de `.git` antes y después |

## 7. Juicio orientativo de 1 a 10 (VCX-P2)

Separado del motor y no comparable entre evaluaciones.

| Candidata | Nota | Motivo |
|---|---|---|
| `interface-review-minset` | 5 | Diseño cuidadoso: alcance del diff, causalidad y lectura sola. Descuentos: solo web, sin CI ni versiones, 8 carpetas para una función |
| `ui-ux-pro-max-core` | 4 | Recuperación determinista y bien probada como recuperación. Descuentos: ignora `--stack`, no lee el sistema existente, defaults silenciosos en español y release detenida |
| `ui-skills-improve-ui` | 4 | Mínima y con permisos claros. Descuento: solapa con lo ya aprobado y la checklist |
| `platform-design-skills` | 3 | Estancada, sin React Native, redistribuye el PDF de Apple |

## Reproducir

Desde la raíz de VCX, una candidata por vez:

```bash
node docs/tooling/score-run.mjs evaluate --input docs/superpowers/reports/2026-11-16-ui-ux-tooling-consolidation-dry-run/<id>.evidence.json --now 2026-11-17T00:20:00Z --operator "Claude Code (claude-opus-5-5); evaluación en seco solicitada" --dry-run
```

## Comprobación de lo que no cambió

Antes y después de las corridas coinciden estos SHA-256:

- política: `ce6e1a31…`;
- `score-runs.jsonl`: `0ec91462…`;
- `score-run.mjs`: `481e27d3…`;
- matriz: `6114d062…`;
- conjunto de `docs/tooling`: `3deff7b3…`.

En Brix, `git status --porcelain --ignored -- packages/cli` sale vacío.

Esta ronda creó solo los 9 archivos de esta carpeta. Fuera del repositorio quedaron los clones, las notas y el generador de evidencia, en el scratchpad de la sesión.

**Consumo:** 437.690 tokens de los tres subagentes, según el harness. El consumo del agente principal y el costo en dinero no están disponibles.
