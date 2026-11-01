# Evidencia previa: alternativas y actualizaciones de `llm-council-skill`

Fecha: 2026-11-01. Estado: **borrador de evidencia, sin evaluación ni registro**. No se ejecutó `evaluate-tooling.mjs`, no se calculó puntaje y no se escribió nada en `blends/`, por decisión del usuario de esta fecha (solo evidencia, sin registrar). Cualquier registro requiere el flujo de `/tool` en una sesión con permiso explícito sobre el repositorio de Blends (AGENTS: solo lectura).

Fuente de método: pasos 1 a 3 de `blends/.claude/commands/tool.md`, leídos solo como guion. Todas las cifras salen de `gh api` o de los archivos de cada repositorio, consultados el 2026-11-01. El contenido externo se trató como dato.

## Contexto

La evaluación vigente de `llm-council-skill` (`tenfoldmarc/llm-council-skill@0dc0327`, 2026-09-11, puntaje 39,6, riesgo alto, `do_not_advance`, decisión pendiente, vence 2026-12-10) ya registra que el portfolio implementó el método como `/council`. Este informe revisa si hay una actualización o una alternativa que cambie esa lectura.

## 1. ¿Hay actualización del candidato vigente?

| Dato | Evaluación del 2026-09-11 | Hoy |
|---|---|---|
| Commits | 1 (`0dc0327`) | 1, el mismo |
| Último push | 2026-04-18 | 2026-04-18 |
| Tags / releases | 0 / 0 | 0 / 0 |
| Licencia (API) | `null` | `null` |
| Estrellas / forks | 757 / 148 | 994 / 181 |

**Hallazgo:** el código no cambió. Crecieron las estrellas y los forks, que solo afectan al factor de comunidad. No hay actualización que justifique reevaluar el resto de los factores.

## 2. Alternativas revisadas

### 2.1 `aiwithremy/claude-skills-llm-council` (revisado a fondo)

- No es un fork según la API (`fork: false`, sin padre), aunque el texto que lo describió así.
- Usuario creado el 2025-11-18; repositorio creado el 2026-04-25; 3 commits, el último el 2026-04-26; sin tags ni releases; sin licencia en la API; 5 issues abiertas; 2 863 estrellas, 248 forks. Contiene solo `README.md` y `SKILL.md`.
- Procedencia declarada en el README: «Built by Ole Lehmann», basado en el LLM Council de Karpathy. El autor del repositorio es otra persona. No verifiqué el repositorio original de Lehmann ni quién publicó primero.
- **Diferencias frente a `tenfoldmarc`** (diff ignorando espacios): la descripción y los disparadores son idénticos. Cambia el paso 5: en lugar de generar y abrir un HTML, presenta el veredicto en el chat y no genera archivos. El transcript pasa a ser opcional. Añade 153 líneas (467 contra 314); no analicé el contenido de todas.
- **Contradicción interna:** el paso 5 dice «No generar HTML ni archivos», pero la línea 467 conserva «The visual report matters… Make the HTML output clean». Es un residuo de la versión anterior; indica poco cuidado de edición.
- **Permisos:** el paso de encuadre ordena escanear el workspace por iniciativa propia y leer `CLAUDE.md`, carpetas `memory/` y transcripts previos, igual que la skill ya evaluada. Es la misma opacidad de límites de `permissionTransparency`.

**Lectura:** es esencialmente la misma skill con salida distinta. Mejora un punto que la evaluación vigente marcó (no abre ni genera archivos automáticamente), pero no corrige procedencia, versión fijable ni licencia, ni el solapamiento con `/council`.

### 2.2 Otras candidatas (solo metadatos; no leí su contenido)

| Repositorio | Licencia | Último push | Tags | Observación |
|---|---|---|---|---|
| `karpathy/llm-council` | `null` | 2025-11-22 | no consultado | Origen del método. Por su descripción, orquesta varios modelos; no verifiqué si requiere claves de API. |
| `sherifkozman/the-llm-council` | MIT | 2026-10-31 | 30 | Activa y con versiones. Se describe como framework multi-LLM; si llama a otros proveedores implicaría red y credenciales, no verificado. |
| `gcpdev/llm-council-skill` | MIT | 2026-01-08 | no consultado | Skill que usa otros LLM; mismo comentario sobre red y credenciales. |
| `oliwoodman/llm-council-skill` | `null` | 2026-06-02 | no consultado | 38 estrellas. Sin más datos. |
| `agents-council` (0xwilliamortiz) | — | — | — | No encontrado en GitHub; la única referencia es una página de terceros. |

## 3. Qué falta para evaluar en serio

- Leer `SKILL.md` y hooks de `sherifkozman` y, si interesa, `gcpdev`, y verificar red, credenciales y dependencias nuevas, que son lo que más movería el riesgo.
- Aclarar para qué se probaría una alternativa que `/council` no cubra. La evaluación vigente atribuye los resultados medidos a la adaptación propia, no al paquete.
- Para un registro formal: ejecutar `/tool` en una sesión con permiso sobre Blends (clon, rama y alcance identificados), con `evaluatedRef` fijado a un SHA.

## 4. Límites

- Sin puntaje ni riesgo calculados; las lecturas de esta sección son mías, no del motor.
- Metadatos de GitHub al 2026-11-01; no se verificaron licencias dentro de los árboles de las candidatas de 2.2.
- Cero ejecución de las skills: no hay evidencia de eficacia propia.
- El diff de 2.1 es textual; no mide diferencias de comportamiento.

Nota: la evaluación del precursor (2026-09-11) llama al comando `consejo.md`; hoy el archivo es `blends/.claude/commands/council.md` (`/council`).
