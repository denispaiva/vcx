# Piloto de Projects (beta) en Teyst

Fecha: 2026-11-24. Estado: PB-1 y PB-2 hechos. Siguiente paso: PB-3. El piloto todavía no empezó. El 2026-11-24, en el chat con Claude, el usuario respondió «Sí, aprobar y commitear» a «¿Apruebo PB-2 así y commiteo el plan en una rama?». Con eso aprobó el piloto **solo en local**, con D-nube pospuesta y A5 sin evaluar. Al cerrarse, la decisión se registra en el [registro](../../decisions/README.md). Revisión 2: integra la crítica de Codex del 2026-11-24.

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

Registrar una retoma no debe llevar más de cinco minutos; si lleva más, se simplifica la ficha. Una corrección menor cuenta como retoma fallida y la prueba sigue. Una pérdida de contexto que obliga a rehacer trabajo activa el corte anticipado.

**Qué mide A1 en modo local:** un hilo local recibe las instrucciones del proyecto, pero arranca sin cargar sus archivos de memoria ([documentación](https://code.claude.com/docs/en/claude-projects.md#run-a-thread-on-your-own-computer)). A1 mide entonces la continuidad que el usuario experimenta al trabajar desde Projects sobre el repositorio local, no la memoria del proyecto por sí sola.

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

Sin datos todavía.
