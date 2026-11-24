# Piloto A a D: UI/UX Pro Max e Interface Review

Fecha: 2026-11-17, entre las 22:15 y las 23:00 hora local (UTC−3).

Estado: **piloto ejecutado, evidencia fechada**. No es una admisión ni una decisión, y no hay commit.

**Autorización:** pedido del usuario en el chat de Claude Code, «Ejecuta el piloto propuesto, casos A a D». Son los casos de la [segunda ronda en seco](../2026-11-17-ui-ux-tooling-consolidation-dry-run/README.md#6-piloto-propuesto-no-ejecutado). Los criterios se fijaron antes de la primera ejecución, en [criterios.md](criterios.md).

**Revisiones:**

- UI/UX Pro Max: `nextlevelbuilder/ui-ux-pro-max-skill@e59ff37`.
- Interface Review: `jakubkrehel/skills@2136b60`, conjunto mínimo de 8 carpetas.

Las dos se leyeron desde clones del scratchpad, sin instalarlas. Los dos clones quedaron sin cambios.

**Operador:** Claude Code (`claude-opus-5-5`). Diez subagentes:

- seis diseñadores `sonnet`;
- un revisor ciego `opus`;
- tres revisores de Interface Review `sonnet`.

## Resultados

| Caso | Pregunta | Resultado según el criterio fijado |
|---|---|---|
| A | ¿UI/UX Pro Max mejora una dirección visual nueva frente a no usarla? | **«Supera», justo en el umbral**: posición media 3,0 con skill y 4,0 sin skill. Los totales de puntaje favorecen a la rama sin skill. Ver la lectura abajo |
| B | ¿Fue correcto el descarte de `accessibilityLabel` en React Native? | **Correcto en web:** el nombre accesible es el mismo en base y rama, en reposo y cargando. Nativo sin probar |
| C | ¿El resultado del caso 8 se transfiere a `2136b60`? | **Sí:** 3 de 3 detectados y 3 de 3 bien clasificados, veredicto Block |
| D | ¿Las escrituras en `.git` que la skill permite respetan las reglas locales? | **Sí:** corrió `fetch` de la ref del PR y `remote set-head`, y solo escribió refs bajo `refs/remotes/` y `FETCH_HEAD` |

## Caso A: dirección visual con y sin UI/UX Pro Max

**Montaje:**

- Un [brief](a/brief.md) en inglés para una app ficticia: una biblioteca de herramientas entre vecinos, sin marca previa.
- Seis corridas `sonnet`, tres por rama.
- La rama con skill usó `search.py` en un sandbox sin red y con escritura solo en `runs/`, mediante [`herramientas/uupm`](herramientas/uupm) y [`herramientas/sandbox.sb`](herramientas/sandbox.sb). Antes de empezar se comprobó que el sandbox niega la red y las escrituras fuera de esa carpeta.
- Las entregas están en [`a/corridas/`](a/corridas/).

**Uso de la herramienta.** Las tres corridas con skill corrieron `--design-system` con la misma consulta y una búsqueda `--domain ux`. S3 repitió `--design-system`, una vez con `--tokens dtcg`. Ninguna usó `--persist`, así que no escribieron archivos de la skill.

**Qué tomaron:**

- el par verde primario y naranja de acción;
- 44 px y 8 px de separación entre objetivos táctiles;
- íconos SVG en lugar de emoji;
- foco visible.

**Qué descartaron:** Inter, el patrón «Funnel», el estilo Minimalism & Swiss y el fondo menta. Dos de las tres corridas oscurecieron el naranja para que pasara el contraste.

### Revisión ciega y contraste

La revisión completa está en [`a/revision-ciega.md`](a/revision-ciega.md), las capturas en [`a/ciego/`](a/ciego/) y las medidas en [`a/medidas.tsv`](a/medidas.tsv) y [`a/contraste/`](a/contraste/).

| Corrida | Rama | Posición | Total (de 25) | Fallas de contraste | No medibles | Tokens | Tiempo |
|---|---|---|---|---|---|---|---|
| S3 | con skill | 1 | 22 | 0 de 36 | 6 | 105.625 | 73,3 s |
| S2 | con skill | 2 | 21 | 0 de 30 | 0 | 96.862 | 52,4 s |
| N2 | sin skill | 3 | 21 | 0 de 30 | 0 | 84.879 | 43,5 s |
| N3 | sin skill | 4 | 20 | 0 de 30 | 0 | 84.531 | 40,8 s |
| N1 | sin skill | 5 | 20 | 0 de 28 | 0 | 83.936 | 38,0 s |
| S1 | con skill | 6 | 16 | 0 de 32 | 0 | 96.972 | 57,0 s |

| Rama | Posición media | Total medio | Fallas de contraste | Tokens medios | Tiempo medio |
|---|---|---|---|---|---|
| Con skill | **3,0** | 19,7 | 0 | 99.820 (+18 %) | 60,9 s (+49 %) |
| Sin skill | 4,0 | **20,3** | 0 | 84.449 | 40,8 s |

**Los 6 «no medibles» de S3** son textos sobre un patrón de puntos (`radial-gradient`). Ignorando el patrón, con la variante [`contrast-sin-patron.js`](herramientas/contrast-sin-patron.js), los 36 textos pasan. La regla fijada los cuenta como «no medibles».

**Por el criterio fijado, el resultado es «supera»:** la posición media mejora exactamente 1,0 y las fallas de contraste no aumentan.

### Lectura

**El resultado está en el umbral y es frágil:**

- Con tres corridas por rama, intercambiar las posiciones de S2 y N2 (2.º y 3.º, con el mismo total de 21) lo convierte en empate.
- El total medio favorece a la rama sin skill, 20,3 contra 19,7.
- La rama con skill es la más dispersa: tiene la mejor entrada (S3) y la peor (S1). S1 quedó última por defectos de construcción del CSS: enlaces sin reiniciar y un atajo `font` inválido. Esos defectos no vienen de la herramienta.

**La herramienta no cambió la dirección visual.** Las seis corridas convergieron en la misma paleta: fondo crema, verde pino y naranja. Las corridas sin skill llegaron solas al mismo par verde y naranja que la herramienta recomendó. El revisor señaló que dos corridas sin skill (N1 y N3) son casi duplicados.

**Lo que sí distingue a S3**, la mejor, es la tipografía slab, el contorno con sombra y una semántica cuidada. Su informe atribuye a la herramienta solo el par de colores, la estructura de tokens y la lista de comprobación. Esa lista ya cubren `design:accessibility-review` y `mobile-check`.

**Costo:** la skill sumó un 18 % de tokens y un 49 % de tiempo por corrida.

**Conclusión del caso A:**

- El criterio fijado de antemano da «supera», y se informa así.
- La evidencia no muestra un mecanismo por el que la herramienta haya mejorado el resultado.
- Una diferencia de una posición con n = 3 está dentro de lo que cambia un solo intercambio.
- El criterio resultó débil para su propósito: no pedía ventaja en los totales ni consistencia entre corridas. Una próxima prueba debería fijar ambas cosas.

## Caso B: el caso 7 con render

El detalle usa código privado de Teyst y está en `solera/docs/initiatives/ui-ux-pilot-a-d-2026-11-17/`, sin commit.

**B1, revisión en `2136b60`:**

- Vio la eliminación con el grep de `removed-signals` y no la confirmó como regresión, porque el texto hijo da el nombre.
- Esta vez declaró la condición: si la plataforma no compone el texto hijo, sería un HIGH.
- Recomendó leer el árbol de accesibilidad.
- Veredicto **Approve**, sin escrituras.

**B2, render** con react-native-web 0.21.2 del `node_modules` de Teyst, sin modificarlo. Se leyó el árbol de accesibilidad de Chrome por el protocolo de DevTools ([`herramientas/cdp.mjs`](herramientas/cdp.mjs)).

- El botón tiene el mismo nombre en base y rama, en reposo y cargando. En la base sale de `aria-label`; en la rama, del contenido.
- El indicador de carga (`progressbar`) y el ícono SVG no aportan texto.

**El descarte de la skill fue correcto en web.** VoiceOver y TalkBack quedan sin probar.

## Caso C: el caso 8 en la revisión nueva

Ver [`c/informe.md`](c/informe.md).

- Detectó y clasificó los tres defectos: aria-label quitado como **Regression**, `div` clicable como **Introduced** e `img` sin `alt` como **Pre-existing**.
- Veredicto **Block**, sin hallazgos falsos y sin escrituras.
- **El resultado del 2026-11-16 se transfiere a `2136b60`.**

## Caso D: escrituras permitidas en `.git`

Ver [`d/informe.md`](d/informe.md).

- Con `pr 7`, sin `origin/HEAD` y sin un remoto de GitHub, corrió `git fetch origin "pull/7/head:refs/remotes/pr/7"`. Después `gh pr view` falló y corrió `git remote set-head origin --auto`.
- **Escrituras:** `refs/remotes/pr/7`, `refs/remotes/origin/HEAD`, sus logs y `FETCH_HEAD`.
- **Sin escrituras en:** el árbol de trabajo, worktrees y `/tmp`.
- La revisión fue correcta: HIGH **Regression** y **Block**.

**Las escrituras que la ronda en seco marcaba como sin probar quedan observadas.** Son compatibles con las reglas locales de Git: no tocan el árbol del autor ni ramas locales.

## Qué cambia en la recomendación

| Candidata | Antes | Con este piloto |
|---|---|---|
| UI/UX Pro Max | No agregar | **El criterio fijado da «supera», en el umbral.** Recomiendo no admitir con esta evidencia y, si se quiere decidir, replicar con más corridas y un criterio que también pida ventaja en los totales. La decisión es del PO |
| Interface Review | Solo con un consumidor web con flujo de PR | **Sin cambio, y con más respaldo:** C y D confirman alcance, causalidad y escrituras. B muestra que en React Native su juicio fue correcto en web, pero que solo lo sostiene un render |

**Para `observedOutcome` de una reevaluación:**

- UI/UX Pro Max: el resultado de A, con su fragilidad.
- Interface Review: B, C y D sobre `2136b60`, que reemplazan el supuesto de transferencia.

## Límites

- **Caso A:** tres corridas por rama, un revisor y un brief. Las corridas no se renderizaron durante el diseño, porque así lo pedía el brief a ambas ramas por igual.
- **Casos B a D:** una corrida por caso, y los puntuó el operador, con criterios fijados antes.
- **B2:** solo prueba web. El render usó una leyenda de prueba y el ícono `PlayKeyIcon`.
- **Fotos de `/tmp` en C y D:** cubren solo el listado, no el contenido de archivos que ya existían.
- **Sandbox:** sus denegaciones no se registraron. Solo se observó que no quedaron archivos fuera de `runs/`, salvo `probe-ok.txt` de la comprobación inicial.

## Artefactos

**En este repositorio:**

- `criterios.md` y este README;
- `a/`: brief, seis corridas, seis capturas ciegas, la correspondencia del ciego, la revisión ciega, las medidas y el contraste;
- `c/` y `d/`: informes, diffs y fotos;
- `herramientas/`: el envoltorio y el sandbox, el cliente de DevTools, el script de contraste y el de ciego, y el de fotos.

**En `solera`, sin commit:** el detalle de B, con la entrada del render y el árbol de accesibilidad.

**En el scratchpad:** clones, repositorios de prueba y el bundle del render.

**Sin cambios:** Teyst (`git status` limpio salvo `.claude/`, que ya estaba), Brix, `docs/tooling/` y los dos clones.

**Consumo de los subagentes:** 987.378 tokens.

| Grupo | Tokens |
|---|---|
| Diseño con skill | 299.459 |
| Diseño sin skill | 253.346 |
| Revisión ciega | 120.273 |
| B1 | 106.295 |
| C | 106.181 |
| D | 101.824 |

El consumo del agente principal y el costo en dinero no están disponibles.
