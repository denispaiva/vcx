# Piloto de Projects (beta) en Teyst

Fecha: 2026-11-24. Estado: PB-1 y PB-2 hechos. PB-3 en curso desde el 2026-11-24: la preparación y las primeras dos filas de la ficha están listas, y faltan los pasos de interfaz del usuario. El piloto todavía no empezó. El 2026-11-24, en el chat con Claude, el usuario respondió «Sí, aprobar y commitear» a «¿Apruebo PB-2 así y commiteo el plan en una rama?». Con eso aprobó el piloto **solo en local**, con D-nube pospuesta y A5 sin evaluar. Al cerrarse, la decisión se registra en el [registro](../../decisions/README.md). Revisión 2: integra la crítica de Codex del 2026-11-24.

## Objetivo y preguntas

El piloto responde con evidencia dos decisiones separadas, que pueden tener resultados distintos:

- **D-local · Continuidad:** ¿Projects reemplaza parte de lo que hoy hacemos a mano para retomar trabajo en Teyst (sesiones sueltas, `resume.mjs`, memoria y `AGENTS.md`), o solo suma otro lugar donde buscar contexto?
- **D-nube · Ejecución remota:** ¿conviene habilitar hilos que trabajen en la nube sobre el repositorio de Teyst?

Un «sí» en D-local con un «todavía no» en D-nube es un resultado válido. Con unas pocas tareas, el piloto mide viabilidad, no una tasa general.

**Propuesta para PB-2**, en la que coinciden Claude y Codex el 2026-11-24: correr el piloto **solo en local**, posponer D-nube y dejar A5 sin evaluar. El motivo es que los permisos efectivos del hilo para mergear y disparar workflows siguen sin verificar (respuesta 5). La pregunta que vale la pena responder es si decir «sigamos» lleva al próximo paso correcto con menos tiempo y menos correcciones que con `resume.mjs`, y para eso alcanza con la carpeta local.

## Antecedentes

- **Qué es Projects** (verificado en la documentación oficial; ver las respuestas de PB-1): un proyecto es una conversación continua que se divide en hilos. Cada hilo conoce los repositorios, las instrucciones y lo ocurrido antes. Los hilos siguen en la nube con la laptop cerrada y también pueden trabajar en una carpeta local.
- **Continuidad actual de Teyst:** `resume.mjs` de Solera, el puntero en el `AGENTS.md` de Teyst, la memoria del agente y la cola `ci-admit` con launchd.
- **Riesgo ya conocido:** sesiones paralelas que despliegan sin conocer el estado vivo (ver la memoria «Revisar sesiones antes de desplegar»).
- **Política de Teyst:** el deploy y la CI se rigen por su `AGENTS.md`. Además, no se despliegan Functions a `dev-teyst` desde una ref parcial.
- **FinOps:** rige [Free Tier first](../../../finops-policy.md#free-tier-first-y-eficiencia-de-suscripciones). Un precio desconocido no es costo cero (VCX-P8).
- **Workflows de Teyst**, verificado el 2026-11-24 en `solera/teyst/.github/workflows/`:
  - Un push a una rama o un PR dispara solo `ci.yml`, que no referencia `secrets.*`.
  - `teyst-deploy.yml` se dispara solo con `workflow_dispatch`, desde `refs/heads/main` y con la CI en verde. Se autentica por OIDC/WIF y no guarda claves en secrets.
  - Riesgo residual: una credencial de GitHub con permiso para disparar workflows (`actions: write`) podría lanzar un deploy a `dev` desde `main` sin pasar por el chat. Por eso importa saber qué token usa un hilo en la nube (pregunta 5).

## Preguntas a resolver antes de empezar (PB-1)

Investigación del agente en la documentación oficial y en la app. Cada respuesta guarda tres cosas: la fuente oficial, la configuración efectiva en Teyst y el resultado. Para los permisos y los secretos se revisan la configuración y el alcance, sin exponer valores.

1. **Facturación:** ¿los hilos en la nube consumen el cupo de la suscripción, cupo aparte o gasto adicional? ¿Hay límites de concurrencia o de tiempo?
2. **Contexto:** ¿dónde vive la «memoria» del proyecto? ¿Se puede leer, editar o exportar? ¿Convive con la memoria de `~/.claude/projects/` o la reemplaza?
3. **Instrucciones:** ¿un hilo en la nube carga el `CLAUDE.md`/`AGENTS.md` del repositorio y el `~/.claude/CLAUDE.md` global? El global vive solo en la Mac, así que es probable que la nube no lo vea.
4. **Repositorios:** ¿un proyecto admite varios repositorios? ¿Cómo maneja repositorios anidados e ignorados por la raíz, como `vcx/solera/teyst`?
5. **Permisos:** ¿qué modo de permisos usan los hilos en la nube? ¿Pueden hacer push o abrir PR sin aprobación? ¿Qué alcance tiene su credencial de GitHub, en particular para disparar `workflow_dispatch`?
6. **Secretos:** ¿qué variables y credenciales ve un hilo en la nube? Firebase no debe estar entre ellas.
7. **Salida:** ¿se puede archivar o borrar un proyecto y llevarse su historial?

### Respuestas (2026-11-24)

Fuentes:

- [Documentación de Projects](https://code.claude.com/docs/en/claude-projects.md) (PJ).
- [Entornos en la nube](https://code.claude.com/docs/en/cloud-environments.md) (CE).
- La API de GitHub, para la configuración efectiva de Teyst, leída sin escribir.

Las dos páginas se leyeron el 2026-11-24. Projects es una beta pública para los planes Pro, Max y Ultra, todavía en despliegue gradual. Un proyecto es personal y no se puede compartir.

1. **Facturación.** Usa los límites incluidos en el plan y los consume más rápido que una sesión suelta.
   - Solo pasa esos límites si están activados los usage credits (PJ). Configuración efectiva: **verificar en PB-2 que estén apagados.**
   - Al tocar el límite, un hilo espera al reinicio y continúa solo. Ese comportamiento viene activado y se puede apagar.
   - No hay un tope de hilos concurrentes. El límite aplicado es de 500 hilos nuevos por día.
   - Un proyecto inactivo no consume. Un hilo que vigila un PR se despierta y consume cuando falla la CI o llega un comentario.
   - El consumo por hilo se ve en Project settings > Usage.
   - No está documentado un límite numérico de duración. Si el sandbox no puede reanudarse, el hilo vuelve a clonar y puede perder el trabajo sin commitear.
   - Resultado: dentro del cupo, si los usage credits están apagados.
2. **Contexto.** La memoria del proyecto son archivos con un índice `MEMORY.md`.
   - Se leen, editan y borran en Project settings > Memory.
   - Está separada de la memoria local de Claude Code y de los `CLAUDE.md`.
   - Las instrucciones del proyecto tienen hasta 16.000 caracteres.
   - Los hilos locales reciben las instrucciones pero no la memoria.
   - La conversación trabaja con los mensajes y los hilos recientes, no con todo el historial.
   - No está documentado cómo exportar el historial.
   - Resultado: es una **tercera memoria**, y la regla 1 de fuente única pasa a ser obligatoria.
3. **Instrucciones.** Un hilo en la nube carga `CLAUDE.md`, `.claude/CLAUDE.md`, `.claude/rules/` y las skills, agentes y comandos de `.claude/` del repositorio.
   - No carga `.mcp.json` ni los hooks, permisos o `env` de `.claude/settings.json`.
   - No toma nada de la configuración local, así que **no ve `~/.claude/CLAUDE.md`** (PJ).
   - Configuración efectiva: Teyst versiona un `CLAUDE.md` que solo importa `@AGENTS.md`, y no versiona `.claude/`.
   - Hipótesis por verificar en PB-3: el import carga `AGENTS.md`. La documentación no menciona `AGENTS.md`.
   - Consecuencia: las reglas globales del usuario (Brave, nombres del portfolio) no llegan a la nube. Las que haga falta se copian en las instrucciones del proyecto.
4. **Repositorios.** Un proyecto admite varios repositorios, solo de github.com, a través de la Claude GitHub App y un proxy.
   - Cada hilo en la nube clona los repositorios en su sandbox y trabaja en su propia rama.
   - No está documentado cómo trata los repositorios anidados.
   - Para Teyst es irrelevante, porque se agrega `solera-teyst` solo.
5. **Permisos.** Los hilos corren en auto mode y no aplican las reglas de permisos del repositorio. Pueden abrir PR solos y, con un PR abierto, el auto-fix empuja arreglos (PJ).
   - El proxy de GitHub cambia la credencial del hilo por **el token real del usuario** y sirve la API REST para los repositorios adjuntos (CE).
   - El proxy rechaza borrar ramas y empujar tags. No limita a qué ramas se empuja.
   - Configuración efectiva en Teyst: `main` está protegida, exige PR y los checks `secrets` y `teyst-ci-pilot (solera-ci-teyst)`, aplica también a los administradores y no admite force-push.
   - Esa protección exige **0 aprobaciones**. No hay rulesets ni environments de GitHub.
   - Resultado: un hilo no puede empujar a `main`. **Los permisos efectivos del hilo para mergear y para disparar workflows siguen sin verificar.**
   - Hipótesis, porque la documentación no lo prohíbe ni lo afirma: con el token del usuario, un hilo podría mergear por REST un PR con los checks en verde, o disparar `teyst-deploy.yml` sobre `main`.
   - GitHub no distingue al hilo del usuario. Si esa hipótesis se confirma, lo único que frena esas acciones son el clasificador de auto mode y las instrucciones, y ninguno de los dos es un control aplicado (VCX-P5).
   - Esa incertidumbre alcanza para posponer D-nube.
6. **Secretos y red.** El entorno por defecto lo aloja Anthropic, con acceso de red Limited.
   - Las variables de entorno las puede leer cualquiera que use el entorno.
   - Los «network secrets» los agrega el proxy solo para los hosts listados, y la sesión no los ve (CE).
   - Configuración efectiva: no hace falta ningún secreto para fixes, tests ni documentación. El entorno queda **sin variables ni network secrets**.
   - El deploy de Teyst usa OIDC/WIF desde GitHub Actions, no credenciales en el sandbox.
7. **Salida.** Un proyecto se puede pausar, archivar o borrar. Borrarlo es irreversible y elimina los hilos, la memoria y los archivos, pero no las ramas ni los PR que ya están en GitHub.
   - No está documentado cómo exportar el historial; solo se pueden copiar los archivos de memoria.
   - Por eso la regla 1 vuelve a importar: lo que no se registró en el repositorio se pierde al borrar el proyecto.

**Para reabrir D-nube más adelante** hay que verificar en un repositorio de prueba, no en Teyst, si un hilo en la nube puede mergear un PR o disparar `workflow_dispatch`. Después se elige entre aceptar el riesgo con instrucciones y auditoría de Actions, o agregar un environment de GitHub con aprobación. Esto último suma fricción, pero no es un control fuerte, porque el token del usuario también puede aprobar por la API.

Los checks de CI que piden la protección de `main` y la guarda de `teyst-deploy.yml` no se contradicen. La protección evalúa el PR con `teyst-ci-pilot`; la guarda evalúa el SHA de `main` y acepta `teyst` de Actions o `teyst-ci-pilot-main` de Cloud Build, siempre con `secrets` en verde. La aparente diferencia viene de un comentario de cabecera incompleto en `teyst-deploy.yml`. Verificado el 2026-11-24 en `scripts/ci/deploy-evidence.sh` y en `ci-admit.mjs` de Solera.

**Regla de corte de D-nube:** si el gasto (pregunta 1) o el alcance de los permisos (pregunta 5) siguen inciertos, o si la nube implica gasto adicional sin autorización del Owner, el piloto sigue en modo local, A5 queda **sin evaluar** y D-nube se pospone.

## Encuadre de tooling

VCX-D035 define cómo evaluar tooling, pero no establece que cada función nueva de una herramienta ya contratada deba pasar por `/tool`. Este encuadre es una propuesta y no una regla ratificada:

- **Prueba local:** el encuadre y la evidencia quedan en este plan.
- **Nube:** el acceso nuevo al repositorio y la decisión del Owner se documentan expresamente antes de habilitarla.
- **Adopción habitual:** si Projects pasa a ser parte del flujo, se actualiza la [matriz de tooling](../../architecture/tooling-matrix.md) con su uso y alcance.

## Alcance

- **Producto:** solo Teyst, con el repositorio `denispaiva/solera-teyst`.
- **Fechas:** el piloto observa del 2026-11-25 al 2026-12-09, y el 2026-12-10 es el corte de evidencia y la revisión.
- **Superposición con W49:** los gates de W49 del 2026-12-03 caen dentro del piloto. Las tareas de esos gates quedan fuera de la prueba.
- **Convivencia con el Sprint Planner:** cada tarea registra quién la eligió. Projects se mide desde que la tarea ya está elegida, o sea, el costo de retomarla. La velocidad total del sprint no se atribuye al piloto.
- **Tareas candidatas:** trabajo del backlog que termine en un PR revisable: fixes acotados, tests y documentación del repositorio.

## Fuera de alcance

- Deploys a `dev-teyst` o `prod-teyst` desde cualquier hilo, incluido disparar `teyst-deploy.yml`.
- Credenciales de Firebase u otros secretos en la nube.
- Trabajo que cruce la raíz de VCX, Solera y Teyst.
- Tareas de los gates de W49.
- Migrar la tarea `sprint-planner-manana`, retirar `resume.mjs` o borrar memorias. Eso solo pasa después de una decisión.
- Otros productos de Assemblage.

## Reglas durante el piloto

1. **Fuente única:** toda decisión que surja en un hilo se registra en su fuente canónica (registro de decisiones, `.roadmap.json`, ADR). El proyecto no es fuente de nada.
2. **Salida de la nube:** los hilos en la nube terminan en una rama o un PR. Nunca hacen merge, deploy ni `workflow_dispatch`.
3. **Sin sesiones fantasma:** mientras dure el piloto, el trabajo de Teyst va por el proyecto o por sesiones normales, pero no por ambos en la misma tarea.
4. **Bitácora mínima:** por cada tarea, una fila en la sección Resultados.

## Ficha de retoma

Hay cinco retomas reales con Projects y retomas comparables con el flujo actual (`resume.mjs`). Cada retoma ocupa **una sola fila** en la sección Resultados:

- **Antes de arrancar** se anota qué debería recuperar el agente: el último estado confirmado, el próximo paso y la restricción vigente.
- **Al terminar** se completa la misma fila con los aciertos sobre esos tres puntos, los minutos hasta poder avanzar y las correcciones que tuvo que hacer el usuario.

**Toma de datos (desde el 2026-11-25).** R1 y R2 quedaron sin medir porque los datos no llegaron después de cerrar el hilo. Para que no dependa de anotar de memoria:

1. **Al abrir el hilo**, el usuario anota la hora de inicio.
2. **Antes de cerrarlo**, le pide: «Resumí en cinco líneas: qué tarea, estado, próximo paso, restricciones y qué comandos corriste». También anota la hora de fin.
3. **Al volver a la sesión del plan**, pega ese resumen con las dos horas y el número de correcciones que hizo, o «ninguna».
4. **El agente de la sesión del plan** califica los aciertos comparando el resumen con la ficha. Anota en la misma fila los minutos, las correcciones y si el hilo corrió `resume.mjs` por su cuenta.

Sin el resumen pegado, la retoma se registra sin medir. Un dato no se reconstruye de memoria, porque contamina la comparación de A1. El resumen lo redacta el propio hilo, así que la calificación puede estar sesgada a su favor: se anota cuando el resumen contradice lo que el usuario vio.

Registrar una retoma no debe llevar más de cinco minutos; si lleva más, se simplifica la ficha. Una corrección menor cuenta como retoma fallida y la prueba sigue. Una pérdida de contexto que obliga a rehacer trabajo activa el corte anticipado.

**Qué mide A1 en modo local:** un hilo local recibe las instrucciones del proyecto, pero arranca sin cargar sus archivos de memoria ([documentación](https://code.claude.com/docs/en/claude-projects.md#run-a-thread-on-your-own-computer)). A1 mide entonces la continuidad que el usuario experimenta al trabajar desde Projects sobre el repositorio local, no la memoria del proyecto por sí sola.

## Preparación de PB-3

Datos de la [documentación de hilos locales](https://code.claude.com/docs/en/claude-projects.md#run-a-thread-on-your-own-computer), leída el 2026-11-24:

- Un hilo local es una sesión de Claude Code en la Mac, conectada por Remote Control.
- Usa la configuración local, incluidos los hooks y los permisos, y corre en auto mode.
- Al crear un proyecto solo el nombre es obligatorio. Se puede crear sin repositorios.

**Controles del modo local.** Los dos primeros son aplicados, no instrucciones:

1. **Proyecto sin repositorio adjunto.** El proxy solo sirve los repositorios adjuntos, así que un hilo en la nube que se iniciara por error no podría acceder a `solera-teyst` (respondería 403).
2. **Usage credits apagados.** Así no puede haber gasto adicional (A4).
3. **Instrucción en el proyecto:** solo hilos locales, nunca en la nube.
4. **Worktree activado** en las opciones de la carpeta. Hay otras sesiones trabajando en Teyst (por ejemplo, la que tomó #297), y dos hilos en la misma carpeta pueden pisarse los cambios.
5. **Claude GitHub App sin instalar.** Los hilos locales no la necesitan, porque usan Git y `gh` de la Mac. El 2026-11-24 el usuario la había instalado en la cuenta personal con acceso a todos los repositorios y escritura en actions, workflows, code y pull requests. Ese mismo día la desinstaló, ante la recomendación de suspenderla o desinstalarla. No se pudo verificar por la API, porque el token de `gh` no puede listar instalaciones; vale lo que el usuario vio en github.com/settings/installations. Si Projects vuelve a pedir la app para trabajar en local, no se instala: se anota como discrepancia con la documentación y se revisa el plan. Se reinstala solo al reabrir D-nube, con **Only select repositories**.

**Qué compara A1, en concreto.** El `AGENTS.md` de Teyst indica correr `resume.mjs` al retomar, así que un hilo local también lo va a usar. La comparación es entre una sesión suelta con `resume.mjs` y Projects con `resume.mjs`. La diferencia que se mide es lo que aportan la conversación del proyecto y sus instrucciones.

**Pasos de interfaz (los hace el usuario):**

1. En claude.ai, confirmar que los usage credits están apagados.
2. En la app de escritorio, ir a **Settings > Claude Code** (o **Settings > Code**). Activar **Use this computer from your phone and claude.ai** y agregar la carpeta `vcx/solera/teyst`.
3. En **Projects**, elegir **New project** y ponerle de nombre «Teyst». No agregar repositorios.
4. En **Project settings > Memory > Project instructions**, pegar las instrucciones de abajo.
5. Para cada retoma con Projects, elegir **Work locally** desde el **+**, elegir la carpeta, activar **Worktree** y hacer clic en **Allow once**. Comprobar que aparece el ícono de la laptop.

**Instrucciones del proyecto:**

```text
Proyecto Teyst. Piloto de Projects del 2026-11-25 al 2026-12-09; plan en vcx/docs/superpowers/plans/2026-11-24-projects-beta-pilot-plan.md.
- Trabajar solo en hilos locales (Work locally) sobre /Users/denis/VibeCoding/vcx/solera/teyst con Worktree activado. No iniciar hilos en la nube.
- Al retomar, correr la entrada «Retomar Teyst» del AGENTS.md (resume.mjs) antes de confiar en la memoria.
- No mergear, no desplegar, no disparar workflow_dispatch y no empujar a main. Cada tarea termina en una rama o un PR.
- Toda decisión se registra en su fuente canónica: issue de Teyst, .roadmap.json, ADR o registro de VCX. Este proyecto no es fuente de nada.
- Las tareas de los gates de W49 quedan fuera del piloto.
- Español para la comunicación; inglés para el código.
- Al cerrar cada retoma, recordarle al usuario que complete su fila en la ficha del plan.
```

## Criterios de aceptación

| ID | Decisión | Criterio | Umbral |
|---|---|---|---|
| A1 | D-local | Retomas según la ficha, comparadas con `resume.mjs` | Lo primero que se mira es si ahorra minutos y correcciones frente a `resume.mjs`. Acertar 4 de 5 es solo una señal orientativa y dice poco si el flujo actual logra lo mismo. Con menos de 5 retomas al 2026-12-09, la evidencia es insuficiente |
| A2 | Ambas | Fidelidad a las instrucciones del repositorio (flujo de PR, sin deploy, convenciones de idioma) | Cero violaciones |
| A3 | D-local | Fuente única y retoma cruzada: al cerrar una tarea hecha en Projects, una sesión nueva de Codex identifica la decisión, la evidencia y el próximo paso usando solo las fuentes canónicas | Sin pegarle nada del chat de Claude. Si hace falta, se anota qué contexto faltó registrar |
| A4 | Ambas | Costo: al inicio se confirma que los usage credits están apagados | Dentro del cupo incluido; cero gasto adicional |
| A5 | D-nube | Dos tareas independientes del backlog que llegan a un PR revisable con la Mac cerrada | 2, anotando cualquier intervención. Sin evaluar si rige la regla de corte de D-nube |
| A6 | D-local | Visibilidad antes de un despliegue real: qué tareas siguen activas, en qué rama están y si alguna afecta lo que se va a desplegar | La respuesta coincide con GitHub y con la cola `ci-admit`, incluido el trabajo iniciado fuera de Projects. No se despliega desde un hilo |

**Corte anticipado:** se suspende ante cualquier gasto adicional, cualquier acción no autorizada de un hilo (push a `main`, deploy, `workflow_dispatch`, acceso a secretos) o una pérdida de contexto que obligue a rehacer trabajo.

## Pasos

| ID | Paso | Responsable | Depende de |
|---|---|---|---|
| PB-1 | Responder las preguntas previas con su fuente, la configuración efectiva y el resultado | Agente | Ninguno |
| PB-2 | Confirmar el alcance, las fechas y los criterios, y decidir si D-nube entra al piloto. Hecho el 2026-11-24: piloto solo en local y D-nube pospuesta | Usuario | PB-1 |
| PB-3 | Confirmar que los usage credits están apagados. Crear el proyecto Teyst y elegir las cinco retomas con su ficha. Medir la línea de base con `resume.mjs`. En la primera retoma, comprobar que corre en la Mac: **Work locally** con la carpeta de Teyst y el ícono de la laptop en el encabezado del hilo. Comprobar también que el import `@AGENTS.md` carga | Usuario, con el agente | PB-2 |
| PB-4 | Correr las tareas del piloto y llevar la bitácora | Usuario y agente | PB-3 |
| PB-5 | Evaluar A1 a A6 por separado para D-local y D-nube, y proponer adoptar, ajustar o descartar cada una | Agente | PB-4 |
| PB-6 | Decidir y registrar las dos decisiones. Si se adopta, planificar qué mecanismo actual se retira, cómo recuperarlo y cómo se actualiza la matriz | Usuario | PB-5 |

## Resultados

| Fecha | Tarea | Eligió | Flujo (Projects o `resume.mjs`) | Esperado: estado / próximo paso / restricción | Aciertos (de 3) | Minutos | Correcciones | Incidentes |
|---|---|---|---|---|---|---|---|---|
| No corrida | #294 cápsula de agenda | `resume.mjs`, 2026-11-24 | Projects (R1; anulada) | **Estado:** PR #295 (`feat/home-agenda-capsule`) con el commit `c714ac3` (hora en 24 h), en espera de ci-admit por el crédito del día. **Próximo paso:** con día nuevo o reserva devuelta, relanzar `ci-admit launch --purpose pr --pr 295` con ese SHA y seguir hasta que `teyst-ci-pilot` termine en `success`. **Restricción:** no relanzar sin crédito; sin merge ni deploy | | | | |
| No corrida | #268 bienvenida por grano | `resume.mjs`, 2026-11-24 | `resume.mjs` (B1; anulada) | **Estado:** implementado en #232 (`0bf4fef`), viaja en el tren #270. **Próximo paso:** verificar iOS, Android, el lector de pantalla y el movimiento reducido en el navegador. **Restricción:** está fuera del sprint; antes de tomarla, confirmar en el issue que es un pedido «Implementá esto» | | | | |
| No corrida | #306 identidad nativa por entorno | `resume.mjs`, 2026-11-24 22:53 | Projects (R2, reemplaza a R1; anulada) | **Estado:** #306 sigue abierto en «En curso», sin toma, sin comentarios y sin PR; se creó el 2026-11-24 a las 19:15. Cuatro minutos después se creó #307, que cubre el mismo F1a (tabla de identidades y guarda de destino). A #307 lo tomó otra sesión de Claude Code, y tiene el PR #308 (`feat/release-identity`, `05ce43d`), que ya registra DU-3 y DU-5 en `publicacion-tiendas.md`; al leerlo, `teyst-ci-pilot` todavía no había terminado. **Próximo paso:** no implementar. Señalarle al PO que #306 se superpone con #307 y el PR #308, y proponerle cerrar #306 como duplicado o redefinir su alcance; esperar su respuesta. **Restricción:** no tocar #307 ni el PR #308, porque son de otra sesión. #306 está fuera del sprint y no tiene un pedido «Implementá esto». Las consolas, la distribución y el deploy quedan fuera de alcance | | | | |
| No corrida | #310 una sola etiqueta oculta por cata | `resume.mjs`, 2026-11-25 13:47 | Projects (R2; anulada) | **Estado:** el PR #312 (`feat/single-hidden-label`, cabeza `45b18f3`) está abierto, en «En revisión», con `secrets` y `teyst-ci-pilot` en verde. No tiene ningún comentario `review-pilot`, así que según el `AGENTS.md` de Teyst cuenta como no revisado. El issue no tiene toma ni comentarios. Sigue pendiente una decisión del PO: qué pasa con las catas ya creadas que tienen más de una oculta. **Próximo paso:** primero preguntarle al PO su disponibilidad de hoy, porque `resume.mjs` la marca sin informar. Después, hacer la revisión independiente del PR #312 sobre `45b18f3` y dejar el comentario `review-pilot` con el SHA, quién revisó y los hallazgos. **Restricción:** una revisión favorable no autoriza el merge ni el deploy. No resolver por cuenta propia la decisión pendiente sobre las catas existentes. #310 está fuera del sprint. No tocar #268, #307 ni #317, que son de otras sesiones | | | | |
| 2026-11-25 | #268 bienvenida: foco y contraste | `resume.mjs`, 2026-11-25 20:46Z | Projects (R2) | **Estado:** #268 está en «En revisión», fuera de sprint y con el sprint en espera. Su PR #328 (`fix/268-bienvenida-foco-contraste`, cabeza `de4e9bd`) está abierto, con `secrets` y `teyst-ci-pilot` en verde y sin comentario `review-pilot`, así que cuenta como no revisado. El PR deja al PO una elección: la línea de versión al 85 % de opacidad (4.72:1) o al 75 % que había pedido. **Próximo paso:** preguntar al PO su disponibilidad de hoy, que `resume.mjs` muestra sin informar. Después, hacer la revisión independiente del PR #328 sobre `de4e9bd` y dejar el comentario `review-pilot`. `resume.mjs` propone la clase balanced (Sonnet, esfuerzo medium). **Restricción:** una revisión favorable no autoriza merge ni deploy. No elegir la opacidad por el PO. No tocar #307 ni #317 (otra sesión) | Sin medir | Sin medir | Sin medir | Sin medir |
| 2026-11-25 | #268 bienvenida: foco y contraste | `resume.mjs`, 2026-11-25 21:17Z | Projects (R3) | **Estado:** igual que en R2, sin cambios desde entonces. #268 está en «En revisión», fuera de sprint y con el sprint en espera. Su PR #328 (`fix/268-bienvenida-foco-contraste`, cabeza `de4e9bd`) está abierto, con `secrets` y `teyst-ci-pilot` en verde, sin reseñas y sin comentario `review-pilot`, así que cuenta como no revisado. El PR deja al PO una elección: la línea de versión al 85 % de opacidad (4.72:1) o al 75 % que había pedido. **Próximo paso:** preguntar al PO su disponibilidad de hoy, que `resume.mjs` muestra sin informar. Después, hacer la revisión independiente del PR #328 sobre `de4e9bd` y dejar el comentario `review-pilot`. `resume.mjs` propone la clase balanced (Sonnet, esfuerzo medium). **Restricción:** una revisión favorable no autoriza merge ni deploy. No elegir la opacidad por el PO. No tocar #307 ni #317 (otra sesión). No relanzar ci-admit: el crédito de Cloud Build está bajo el piso (-643.22 contra -198.21) | 1 de 3, más uno parcial: estado ✗, próximo paso parcial, restricción ✓ | 1 min 47 s (21:43:10Z a 21:44:57Z) | 0 | Ninguno. Recomendó mergear el PR #328 sin `review-pilot`; ver nota R3 |
| 2026-11-25 | Propuesta del sprint siguiente a W47 | `resume.mjs`, 2026-11-25 21:54Z | `resume.mjs` (B1) | **Estado:** el sprint SP-2026-W47 no tiene tareas de agente elegibles en el Project y cierra el 2026-11-29. #268 se cerró a las 21:53Z, al mergearse el PR #328 (`de4e9bd`) sin comentario `review-pilot`. #307 y #317 los tiene tomados otra sesión. La disponibilidad del PO figura sin informar para los próximos 7 días. **Próximo paso:** preguntar al PO su disponibilidad de hoy y después preparar la propuesta del sprint siguiente: arrastres, candidatos, esfuerzo restante y decisiones del PO. **Restricción:** la propuesta es candidata, no compromiso; la decide el PO. No crear ni mover tareas en el Project sin su visto bueno. No tocar #307 ni #317. Las tareas de los gates de W49 quedan fuera del piloto. Sin merge ni deploy | 3 de 3 | 3 min 38 s (21:56:14Z a 21:59:52Z); 2 min 35 s sin contar 63 s esperando la respuesta del PO | 0 | Ninguno |

Las dos filas de arriba se completaron antes de arrancar, con `resume.mjs` y los issues del 2026-11-24. Las retomas siguientes se agregan con la misma ficha a medida que el Sprint Planner elige las tareas, alternando entre Projects y `resume.mjs` mientras las tareas sean comparables.

**R2 de #306 anulada (2026-11-25).** No se corrió. #306 se cerró el 2026-11-25 a las 11:12, como duplicado de #307. Lo cerró una sesión común de la pestaña Code, la de TestFlight (`49d3f50d`), mientras respondía a una revisión de Codex del PR #318; no fue una retoma ni un hilo de Projects. Se verificó con la línea de tiempo del issue en GitHub y con los transcripts locales. La reemplaza la fila de #310.

**R2 de #310 y B1 anuladas (2026-11-25).** Ninguna se corrió. El PR #312 se mergeó a las 19:17Z con la cuenta del usuario, con la cabeza en `4f2b605` y sin comentario `review-pilot`, y #310 se cerró. B1 (#268) la tomó una sesión de verificación que no era una retoma con ficha: liberó la tarea a las 18:39Z y dejó la corrección en el PR #328. La R2 nueva usa #268 en su estado actual; B1 queda para la próxima retoma con `resume.mjs`. Tres fichas seguidas vencieron antes de correrse, porque la tarea cambió entre la ficha y el hilo.

**R1 no corrida (corregida el 2026-11-25).** La nota anterior, «R1 sin medir», afirmaba que la retoma se había hecho con Projects. No hay evidencia de eso, y la tarea ya estaba terminada:

- Ningún transcript local de Claude Code muestra un hilo que retome #294. Entre «empiezo la R1» (01:31:18Z) y «terminé la R1» (01:31:56Z), 38 segundos después, no se abrió ninguna sesión. Un hilo local de Projects corre en esta Mac y deja su transcript. Uno en la nube no era posible, porque el proyecto no tenía repositorios y la Claude GitHub App ya estaba desinstalada.
- El PR #295 se mergeó y #294 se cerró el 2026-11-24 a las 22:12Z, unas tres horas antes. El estado esperado de la ficha ya no valía al empezar.
- La nota se escribió desde la sesión de preparación de PB-3 a partir de esos dos mensajes, sin datos de la retoma.

Límite: no se puede descartar que se haya abierto un hilo y cerrado sin escribir nada, pero en ningún caso hay una retoma que medir. No cuenta para A1. La primera retoma medible con Projects es R2.

**R2 sin medir (2026-11-25).** El usuario informó que terminó la R2, pero los datos de la ficha no llegaron. Por su decisión se registra sin medir, sin reconstruirlos, y no cuenta para A1. Tampoco hay evidencia local del hilo: entre la ficha (20:46Z) y el aviso (unos 21:02Z) no apareció ningún transcript nuevo de Claude Code; solo se escribieron la sesión que armó la ficha y la de TestFlight. No se confirmó si los hilos locales de Projects guardan su transcript en `~/.claude/projects`, así que esto no prueba que el hilo no haya corrido. Es el segundo intento con Projects sin datos, después de R1.

**R3 medida (2026-11-25).** Primera retoma que corrió de verdad en Projects. Se verificó con el transcript local `c0b857cc`, que corrió en el worktree `charming-knuth-0a4d2e` de Teyst con el ícono de laptop, y con el resumen que el usuario pegó del hilo.

- **Calificación:**
  - **Estado ✗:** dio el PR #328 por listo, «solo tu merge». No vio que, sin `review-pilot`, cuenta como no revisado, aunque esa regla del `AGENTS.md` estaba en su contexto. Tampoco vio la elección de opacidad pendiente del PO.
  - **Próximo paso, parcial:** pidió la disponibilidad del PO, pero propuso el merge en lugar de la revisión independiente.
  - **Restricción ✓:** no editó, no hizo push, no relanzó CI, respetó #307 y #317 y pidió autorización para `functions:delete`.
- **Contaminación descartada:** la nota del coordinador no traía la tarea ni las respuestas esperadas, solo las instrucciones y una pista vieja de la migración de Comunidad a Liga. El hilo no leyó el plan ni esta sesión.
  - **Qué leyó el coordinador:** según su respuesta, seis sesiones de Claude Code, de agosto a octubre: Rankmi, `remote-control` en `~/blends`, tooling de `blends/vc`, `blends/vc/pinot-index`, la migración de Comunidad a Liga y el roadmap del framework de Tintum. Ninguna del piloto.
  - **Riesgo de alcance:** el coordinador lee historial de sesiones de cualquier carpeta, incluido el precursor `~/blends` y un trabajo ajeno a Teyst (Rankmi). La pista vieja lo hizo revisar una migración ya cerrada. Es contexto viejo y fuera de alcance que entra sin pedirlo; se evalúa en A2 y A3.
- **Carga de contexto:** corrió `resume.mjs` por su cuenta. Usó Opus y lo declaró frente a la recomendación de Sonnet.

**R1 y R2: el proyecto no existía.** Al preparar R3, la pantalla de Projects estaba vacía, y el proyecto Teyst se creó recién para R3. Eso confirma que R1 y R2 no corrieron en Projects. Lo más probable es que se usara la pantalla de sesión nueva del Code tab, que no es Projects.

**B1 medida (2026-11-25).** Primera línea base medida. Sesión común del Code tab en el worktree `teyst-continuacion-70af53`, transcript local `cb6f1c2d`, con Opus.

- **Calificación:**
  - **Estado ✓:** W47 sin tareas de agente y con cierre el 29/11, y #307 y #317 en manos de otra sesión. Agregó el estado real de T-23 a T-27.
  - **Próximo paso ✓:** preguntó la disponibilidad con una pregunta de opciones, la registró como Medium con `availability --set` y armó la propuesta.
  - **Restricción ✓:** dejó la propuesta como candidata, no escribió nada en el Project ni en el roadmap, respetó #307 y #317 y no mergeó ni desplegó. La regla del piloto sobre los gates de W49 no aplica, porque una sesión común no recibe las instrucciones del proyecto.
- **Comparación con R3, débil:** B1 trabajó sobre otra tarea, porque #268 se cerró a las 21:53Z, entre la ficha de R3 y la de B1. Una planificación y una revisión no exigen lo mismo, así que la diferencia de 3/3 contra 1/3 no se atribuye a Projects. Para A1 hacen falta pares sobre la misma tarea o el mismo tipo de tarea.
