# Candidatas UI/UX de Taste Skill y Kimi: evaluación en seco

Fecha: 2026-11-16 (corridas con `--now 2026-11-17T00:10:00Z`). Estado: **evaluación en seco**. No es una admisión ni una decisión: no se persistió nada en `docs/tooling/` y no hay decisión humana. Operador: Claude Opus 5.5 (Claude Code), a pedido de Denis Paiva en el chat del 2026-11-16.

Alcance: investigación, inspección estática por la API de GitHub e invocación del motor en seco. No se instaló ni se activó ninguna candidata, ni se ejecutaron sus scripts o hooks. Todo lo descargado se leyó como dato no confiable, en un scratchpad fuera del repositorio.

Fuentes de la ronda: [tasteskill.dev/docs](https://www.tasteskill.dev/docs) y [UI/UX design skills for agents de Kimi](https://www.kimi.ai/resources/ui-ux-design-skills-for-agents), con fecha de actualización 2026-11-16. Las dos se leyeron el 2026-11-16.

## Archivos

| Archivo | Qué es |
|---|---|
| `<id>.evidence.json` | Evidencia según el contrato de subfactores de Brix, fórmula 1.6.0 |
| `<id>.dry-run.out` | Salida completa de `node docs/tooling/score-run.mjs evaluate … --dry-run` |

Motor: `brix` en `131a5c2`, `cliTree` `b4c9276`, política `default-scoring-policy.json` con sha256 `ce6e1a31…`, sin cambios locales.

## Evidencia anterior

- **En `main` (`5d8467c`) no hay evaluaciones** de Frontend Design, Web Design Guidelines, UX Heuristics, Interface Design ni UI/UX Pro Max. Para `impeccable` solo está el [triage del 2026-11-02](../../plans/2026-11-02-tooling-renewal-plan.md#triage): dejar vencer la admisión del precursor, que vencía el 2026-11-08, porque la copia vendorizada no coincidía con el ref evaluado.
- **Trabajo de otra sesión, en paralelo y sin commit** (observado a las 21:05 del 2026-11-16):
  - en `docs/superpowers/reports/2026-11-16-ui-ux-design-skills-dry-run/`, evidencia de cinco de esas herramientas;
  - en `docs/tooling/`, evaluaciones y decisiones persistidas para `impeccable`, `emilkowalski-skills`, `design-accessibility-review`, `design-ux-copy` y `mobile-app-ui-design`.

  Ese trabajo no tiene una revisión fija: no se reutiliza como evidencia ni se comparan puntajes. De allí solo se toman las identidades declaradas para la comparación cualitativa: `anthropics/skills@e4bb5d9`, `vercel-labs/agent-skills@1a2c79d`, `wondelai/skills@c526558`, `Dammyjay93/interface-design@2f9be32`, `nextlevelbuilder/ui-ux-pro-max-skill@e59ff37` y `pbakaus/impeccable@skill-v4.9.1`.

## 1. Cribado

Deduplicado por repositorio y ruta. **Taste Skill** (`Leonxlnx/taste-skill`, skill `design-taste-frontend`) y **tasteful-ui-skill** (`DonkeyKing01/tasteful-ui-skill`, skill `tasteful-ui`) son repositorios, autores y contratos distintos.

| Herramienta | Identidad (SHA del 2026-11-16) | Tipo | Licencia | Cribado |
|---|---|---|---|---|
| **design-taste-frontend** | `Leonxlnx/taste-skill@f6b7657` (v2.5.1), `skills/taste-skill` | Skill con scripts, hook Stop y kit de assets | MIT el código; logos y fotos de terceros con licencias propias | Prioritaria: evaluada |
| **ui-craft**, distribución mínima | `educlopez/ui-craft@8172a86` (v1.0.21), `skills/ui-craft` | Skill solo Markdown | MIT | Prioritaria: evaluada |
| **ux-discovery-interviewer** | `JacobLinCool/ux-discovery-interviewer-skill@305a4b9`, `.agents/skills/ux-discovery-interviewer` | Skill solo Markdown | MIT | Prioritaria: evaluada |
| ui-craft-mcp, ui-craft CLI, ui-craft-detect | mismo repo: `mcp/`, `cli/`, `scripts/detect` | Servidor MCP por `npx -y ui-craft-mcp@0.9.0`, binario Go y paquete npm | MIT | Dependencias opcionales del plugin. No se evaluaron ni se atribuyen a la skill |
| taste-skill-classics | `Leonxlnx/taste-skill-classics` | 7 skills que se invocan por nombre | MIT | Retiradas del principal, sin gate. Sin necesidad que las justifique |
| imagegen-skills, unlazy | `Leonxlnx/imagegen-skills`, `Leonxlnx/unlazy` | Skills | MIT | Generación de imágenes y salida completa: fuera del objetivo UI/UX |
| TasteCode | tastecode.dev | Servicio | — | La web solo lo enlaza: sin datos para evaluarlo |
| tasteful-ui | `DonkeyKing01/tasteful-ui-skill@159ccd4` | Skill, 92 archivos y 2,3 MB | MIT | Escrita para Codex. Solapa con Taste y UI Craft; último push 2026-05-02 |
| ui-ux-agent-skill-system | `sergekostenchuk/ui-ux-agent-skill-system@ddaedd7` | Sistema de 4.184 archivos y 24 MB, con CLI y adaptadores | Apache-2.0 | Sobredimensionado para la necesidad: descartado sin evaluar |
| open-design-skill | `sugarforever/open-design-skill@c41f8ab` | Skill con scripts, compañera de «Open Design» | MIT | Depende de un producto que la página no describe: descartado |
| apple-design-skill | `dickwu/apple-design-skill@91e1566` | Skill con `scripts/pull-hig.mjs`, que descarga las HIG | **Sin licencia** | Interesante para iOS de Teyst, pero sin licencia no se puede reutilizar: bloqueo legal |
| uxuiprinciples: `uxui-evaluator`, `interface-auditor`, `ai-interface-reviewer`, `vibe-coding-advisor` | `uxuiprinciples/agent-skills@8f14fb5` | 4 skills que llaman con `curl` a `uxuiprinciples.com/api/v1` | Sin licencia SPDX; el README dice «free to use and distribute» | Sin `UXUI_API_KEY` funcionan solo con conocimiento interno del modelo. La taxonomía, las citas y `audit` exigen el plan pro (Principles Library, USD 59/año, cifra del proveedor). En modo sin clave no aportan contenido propio |
| uxuiprinciples: `flow-checker` | mismo repo | Skill | idem | **Requiere el plan pro**: sin clave, el checklist sale del conocimiento interno. No se evalúa como gratuita |
| figma-ai-bridge, agent-ready, figma-context-mcp-skill | `renfei-design/Figma-AI-Bridge`, `Owl-Listener/agent-ready`, `HowardTangOvO/Figma-Context-MCP-Skill` | Skills, plugin de Figma o MCP | MIT / sin licencia / sin licencia | Requieren Figma. No hay una necesidad registrada de Figma: descartadas |
| ui-ux-design de K-Dense | `K-Dense-AI/scientific-agent-skills@ec59a29`, `skills/ui-ux-design` | Skill | MIT | La ruta da 404 en HEAD: identidad no resoluble |
| Kimi Skills Store: design-system-builder, landing-page-scaffold, Document to skills | Plataforma Kimi | Servicio propietario | — | Solo corren dentro de Kimi, no en Codex ni en Claude Code: descartadas |

## 2. Revisión concreta y hallazgos

### Taste: reconciliación de versiones

- **Hecho:** la web documenta 2.1.5, que es el tag `v2.1.5` en `12af471`, del 2026-10-24. Sus scripts son `draw.mjs`, `lint.mjs`, `inspect.mjs`, `assets.mjs` y `scenes.mjs`, y el historial va en `~/.taste-skill/history.json`.
- **Hecho:** el `SKILL.md` de HEAD declara `tasteskill 2.5.1`, que es el tag `v2.5.1` en `f6b7657`, del 2026-11-07; los dos manifiestos dicen 2.5.1. El CHANGELOG § 2.5.0 dice que es «a complete rebuild» que reemplaza el pipeline de 2.1.x y sus cinco scripts. En v2.5.1 esos scripts ya no existen: hay `gate.mjs`, `start.mjs`, `photos.mjs`, `shoot.mjs`, `consistency.mjs` y otros, y el historial pasa a `.taste-skill/` dentro del proyecto.
- **Decisión de la ronda:** evaluar solo v2.5.1, el contrato que instala hoy cualquier canal. La web describe un contrato retirado, y se registra como defecto de documentación y de versionado: una reconstrucción completa publicada como versión menor.

### Taste: hook de cierre, según `gate.mjs` y el CHANGELOG

- **Alcance:** el frontmatter declara un hook `Stop` de Claude Code con timeout de 600 s. Busca `gate.mjs` en seis rutas, incluidas `~/.claude/skills/design-taste-frontend` y `~/.agents/skills/design-taste-frontend`, y **ejecuta la primera que exista**: puede correr otra copia instalada, de otra versión. Sin build activa termina enseguida. La excepción es una página tasteskill modificada en el último día: entonces bloquea una vez para explicar cómo armar el gate.
- **Límites de iteración:** 3 rondas por defecto, configurable de 1 a 10. Los bloqueos se cortan con rondas + 4 por build, o 30 en 6 h por carpeta. Hay timeout total de 9,5 min, un watchdog por chequeo y una lectura de stdin de 2 s como máximo. Un fallo del gate deja detenerse al agente.
- **Excepciones:**
  - `--done "<palabras del usuario>"` cierra la build;
  - el gate permite detenerse con builds activas en dos o más subcarpetas, después de 24 h de inactividad o desde otra sesión;
  - un waiver va en `.taste-skill/waivers.json`, con 5 como máximo; `kit-edited` y `checker-gaming` no admiten waiver.
- **Verificación completa frente a rápida:**
  - la completa corre el checker a 1440 y 390 con una pasada a 320, el layout a 1440×900 y 390×844, `copy-lint` y dos chequeos estáticos, y cuenta como ronda;
  - `--quick` mira el checker a 1440 y 390 y el layout solo a 1440: no cuenta ronda ni cierra la build.
  - Las dos tratan como FAIL dos WARN: `hero-enter`, sin animación de entrada del hero, y `moment-none`, sin momento animado.
- **Efectos sobre proyectos existentes:** construye en el stack del proyecto y sirve el kit desde su carpeta pública. Prohíbe editar los archivos del kit, porque `kit-edited` no admite waiver. Escribe `.taste-skill/`, `assets/` y créditos. El hook registra cada llamada en `gate.json` dondequiera que exista un `.taste-skill`.
- **Codex:** el CHANGELOG 2.5.1 dice que Codex toma el comando de «sus propios archivos de hook». La skill no los instala, así que en Codex el gate es manual.
- **Qué no cubre un `GATE: PASS`:**
  - que la página respete la marca o el contenido real del cliente;
  - que el copy en español sea correcto: `copy-lint.mjs` no tiene ninguna mención de idioma;
  - las licencias de cada foto, fuente o logo;
  - el rendimiento en dispositivos reales;
  - cualquier superficie que no sea un sitio web.

### Taste: reglas que pueden contradecir marca, contenido o usabilidad

- Pide contactos en `.example`, ningún teléfono con formato real y ningún dato inventado. En una landing con contacto real, eso choca con el contenido del cliente.
- Prohíbe el violeta en el diseño propio de la página, aunque sea el color de la marca.
- Exige un mínimo de movimiento: entrada del hero y uno o dos momentos por página. Choca con un dashboard o una página sin animación.
- Exige logos reales de marcas de terceros. El kit trae 929 SVG de marcas, y MIT no cubre las marcas registradas.
- Prohíbe pies de foto bajo cualquier imagen. La regla es editorial; si una imagen necesita leyenda, la accesibilidad depende del `alt`.

### UI Craft: skill mínima frente al paquete

- **Skill mínima:** `skills/ui-craft/`, con `SKILL.md` de 38 KB y 30 referencias, unos 550 KB de Markdown, sin scripts ni hooks.
- **Paquete del plugin:** `source: "./"` lleva el repositorio entero, de 1.403 archivos:
  - `.mcp.json` lanza `npx -y ui-craft-mcp@0.9.0`, con red y ejecución de un paquete npm;
  - `hooks/hooks.json` declara un `preToolUse` con `${CURSOR_PLUGIN_ROOT}`, pensado para Cursor; en Claude Code no se verificó qué hace;
  - suma 25 comandos, 2 agentes y un CLI Go.
- **Lo que la skill sola no trae:** `route_task`, `ux_coverage`, el score de 0 a 100, `ui-craft-detect`, `/finalize` y `/sddesign` son controles del MCP, el CLI o los comandos. La skill los menciona, pero en la distribución mínima esas referencias quedan colgadas, y no se le atribuyen.
- **Versiones:** el tag es 1.0.21, `plugin.json` dice 1.0.0 y el marketplace dice 2026.11.5.1559.
- **Accesibilidad:** prefiere APCA sobre WCAG 2. La conformidad exigible hoy es WCAG, así que la regla queda subordinada.

### UX Discovery frente a Blends

- Entrevista al «customer» que trae una idea vaga, es decir al Owner. **No es investigación con usuarios reales.** Su propia sección *Boundaries* lo reconoce: un hallazgo que sale de una conversación no queda validado.
- Blends ya cubre el encuadre de la idea con plantilla, preguntas asesinas, consejo y confirmación humana ([idea-intake](https://github.com/denispaiva/blends/blob/main/docs/idea-intake.md), leído en `6d77cd0`). Las etiquetas Known/Inferred/Unknown repiten VCX-P1.
- Lo incremental es el formato de journey, happy path, pain points y opportunities, y el ritmo de 3 a 5 preguntas por ronda.
- Escrita para ChatGPT según su frontmatter. Por defecto escribe la salida en inglés.

### Costos

- Ninguna de las tres usa servicios pagos ni claves.
- El costo es el cupo de suscripción, no medido. Para Taste, el proveedor declara «a few hundred thousand tokens» y de 30 a 45 min por build.
- El único cargo adicional identificado está fuera del alcance: el plan pro de uxuiprinciples.

## 3. Resultados del motor (en seco)

| Candidata | Score | Riesgo | Confianza | Cobertura | Recomendación base |
|---|---|---|---|---|---|
| `ui-craft-skill-minimal` | 68,3 | medium | high (85) | 75 % | `advance_with_reservations` |
| `taste-skill-design-taste-frontend` | 52,3 | high | high (85) | 75 % | `do_not_advance` |
| `ux-discovery-interviewer` | 45,6 | low | high (85) | 72,75 % | `do_not_advance` |

El reporte en seco no imprime la cobertura. Se recalculó a mano con los pesos de la política y coincide con la confianza informada: 0,45 × 75 + 0,25 × 85 + 0,15 × 100 + 0,15 × 100 = 85.

Límites del resultado:

- **Comunidad `unavailable` en las tres.** El collector de GitHub del motor no devolvió datos y no había snapshot previo. La causa no se diagnosticó. El 20 % de peso de comunidad no entra en ningún score.
- **Resultados observados: `unavailable`.** `observedAdoption` y `observedOutcome` no tienen evidencia porque no hubo piloto.
- **La confianza «high» no significa evidencia de resultado.** Sin snapshot de comunidad, la frescura y la consistencia derivadas valen 100 por construcción. La banda mide cobertura y fuente, no si la herramienta funciona en VCX.
- **Taste es riesgo high.** Lo marcan `networkAccess` y `broadScope`. Según la política, el gate de decisión exigiría una excepción.
- Los subfactores de tipo rúbrica son juicio del evaluador sobre lo leído: un evaluador distinto podría puntuar distinto.

## 4. Comparación, conjunto mínimo y piloto pendiente

Con la selección anterior es una comparación **cualitativa e hipotética**, sin puntajes de las seis herramientas en `main`:

- **Taste** es la única que trae una verificación ejecutable en navegador real: contraste, foco, tap-size, colisiones, reduced-motion y formularios. Frontend Design, Impeccable, Web Design Guidelines, UX Heuristics e Interface Design son guías de texto según sus identidades declaradas; no se verificó en esta ronda. Pero Taste solo sirve para sitios de empresa, impone una estética fija y tiene riesgo alto.
- **UI Craft mínima** solapa con Impeccable, Web Design Guidelines y UX Heuristics. Lo distinto es la completitud por arquetipo (`coverage.md`) y las perillas, que permiten densidad alta sin animación.
- **UX Discovery** no compite con esas herramientas: se superpone con Blends.

**Recomendación del agente:**

1. **No agregar nada todavía.** Ninguna tiene un resultado observado en VCX.
2. **UI Craft mínima** es la única candidata para un piloto, con reservas: subordinar APCA a WCAG y no usar las referencias al MCP.
3. **Taste no**, por alcance, riesgo y reglas estéticas fijas. Su gate en navegador es una idea a contrastar con la [checklist UX](../2026-11-09-ux-checklist-pilot.md), no una herramienta a adoptar.
4. **UX Discovery no**: Blends ya cubre el encuadre, y la investigación con usuarios reales sigue sin herramienta.

**Piloto que falta antes de proponer adopción** (sin ejecutar; requiere autorización):

- **Método:** el del piloto UX del 2026-11-09. Revisores ciegos, línea de base sin skill frente a la skill, y defectos conocidos plantados.
- **Instalación:** solo en el proyecto, nunca global, en un repositorio de prueba sin datos privados.
- **Taste, si alguna vez se pilotea:** la carpeta del proyecto y no `~/.claude/skills`, para que el hook no encuentre otras copias, y Chrome disponible.

Los contraejemplos del piloto son propuestas, no se ejecutaron:

| Caso | Qué se observa | Expectativa por hipótesis |
|---|---|---|
| Landing con marca y contacto reales: colores propios, quizá violeta; teléfono y correo reales | Que preserve tokens, contacto y textos sin reescribirlos | Taste: conflicto con «contactos en `.example`», sin violeta y teléfono no real; necesitaría waivers o rompería el contenido. UI Craft: pide el brief antes de decidir |
| Dashboard denso sin animación | Cero animaciones de entrada, densidad, tablas con `tabular-nums` | Taste: fuera de alcance; `hero-enter` y `moment-none` bloquean. UI Craft: MOTION_INTENSITY ≤ 3 y VISUAL_DENSITY ≥ 8 |
| Formulario en español: errores por campo, teclado y `prefers-reduced-motion` | Error bajo su campo y asociado, foco al primer error, Tab completo, nada se mueve con movimiento reducido, sin falsos positivos de copy en español | Taste: controla errores por campo, Tab y reduced-motion; copy-lint sin manejo de idioma. UI Craft: guía en `forms.md`, sin verificación ejecutable |

Medidas: defectos conocidos detectados, falsos positivos, cambios no pedidos a marca o contenido, tokens consumidos y tiempo.

## Artefactos de esta ronda

- Creados solo los siete archivos de esta carpeta.
- Fuera del repositorio, en el scratchpad de la sesión: descargas de las candidatas y el generador de evidencia.
- Una redirección dejó por error, unos segundos, un archivo propio en `/tmp`; se borró en el mismo comando.
- No se modificó nada de `docs/tooling/`. Los cambios sin commit que hay allí son de otra sesión.
