# Deuda heredada del precursor: inventario y tratamiento en la migración

Fecha: 2026-11-01. Estado: propuesta del asistente, registrada como VCX-D031 en el [registro de decisiones](../../decisions/README.md) y ratificada por el usuario como decisión documental el 2026-11-01 en la revisión `6934489`; la ejecución de cada tratamiento sigue requiriendo su autorización. Complementa el [camino de migración](2026-11-01-migration-path-design.md) de VCX-D030. El usuario pidió en el chat con Claude: «Se debe aprovechar el momento para ordenar aquella deuda técnica heredada. Desacoples, conflictos de nombres de carpetas, orden de git, jerarquías de carpetas, etc.».

Revisión del 2026-11-01, autorizada por el usuario con «Sí, revisar D031»: incorpora los hallazgos del [consejo de `brix-llm-council`](../reports/2026-11-01-council-inherited-debt-design.md) sobre la revisión `7cf7b0b` de este documento, la deuda que declara VCX-D033 y la autoridad que propone VCX-D034. El consejo es insumo de asesoramiento, no autoridad: cada hallazgo se aceptó o descartó contra las fuentes, y las cifras se volvieron a medir en solo lectura. Lo que cambia: dónde se ejecutan los T2 antes del corte operativo, la condición de hooks activos para toda escritura en el precursor, el destino de los tags bajo VCX-D032, la conciliación de las cifras de ramas, la reversibilidad por tratamiento, la autoridad por repositorio y el responsable de los T0.

Etiquetas: [U] pedido o respuesta del usuario; [H] hecho medido con referencia; [I] interpretación del asistente; [P] propuesta pendiente de revisión.

## Qué significa «ordenar» bajo los principios

[H] VCX-P3 fija que «el incumplimiento heredado se declara como deuda, no se extiende ni se corrige mediante una migración implícita». [H] VCX-D011 exige conciliar con las decisiones aprobadas del precursor antes de reemplazar destinos o controles. [I] Ordenar la deuda durante la migración significa, entonces: inventariarla con evidencia, asignar a cada ítem un repositorio destino y una fase, y ejecutar cada corrección con alcance propio y bajo el gobierno del repositorio donde se resuelve. No significa corregir cosas de paso mientras se clona.

[P] Cuatro tratamientos, uno por ítem:

| Tratamiento | Qué es | Cuándo |
|---|---|---|
| **T1 · Se resuelve al reubicar** | Estado por checkout que el clon no hereda o que se fija al crearlo: configuración con rutas absolutas, hooks, worktrees, archivos sin seguimiento, caches | Fase B del camino de migración |
| **T2 · Se resuelve en el repositorio destino, bajo su gobierno** | Limpieza de Git y reorganizaciones de carpetas que el precursor ya aprobó o que corresponden a Blends; se ejecutan con `queue`, trenes y alcances vigentes en el único checkout que los opera en ese momento | Antes del corte operativo, en el operador vigente `../blends`, solo con una excepción de escritura registrada y con sus hooks activos; después del corte, en el clon. Nunca en los dos |
| **T3 · Se resuelve por extracción** | Acoplamientos entre kernel, Brix e iniciativas que solo desaparecen cuando cada pieza tiene repositorio propio con dependencias declaradas | Fase D, por producto o instancia |
| **T0 · Se declara y no se toca** | Identificadores de máquina, historial inmutable, repositorios heredados fuera del portfolio | Permanente, con procedencia y con un responsable que vuelve a comprobar la declaración en cada puerta de transición |

[I] La versión anterior de T2 decía «en el clon» y «nunca en el precursor», pero el clon no ejecuta `queue` ni trenes hasta la Fase C. Eso dejaba sin lugar de ejecución a DH-01, DH-03, DH-10, DH-11 y DH-14 entre las fases B y C, como señaló el consejo. La regla corregida sigue el precedente de VCX-D027: el checkout que opera es uno solo, y escribir en el precursor exige excepción registrada.

## Inventario medido el 2026-11-01

Lecturas de solo lectura sobre `../blends` en `main` `f86a2a7d`. Las cifras son una foto fechada, no un monitor.

### Orden de Git

| ID | Evidencia [H] | Destino | Tratamiento [P] |
|---|---|---|---|
| DH-01 | 180 ramas locales, medidas de nuevo el 2026-11-01 sobre `f86a2a7d`. «Integrada» significa incluida en `git branch --merged main`, sin contar `main`: 146 (el comando devuelve 147 con `main`). Por estado de upstream: 106 con upstream borrado en GitHub, 42 sin upstream (37 `claude/*`, `los-gatos-802`, `tren/2026-09-08` y tres de Teyst) y 32 con upstream vivo. Cruce: 105 borradas e integradas, 40 sin upstream e integradas, 1 viva e integrada (`claude/blends-code-audit-550e5a`); sin integrar quedan 1 borrada (`tooling/cloudflare-security-audit-install`), 2 sin upstream (`experiment/teyst-dev-integracion-ligas-etiquetas`, `tren/2026-09-08`) y 30 vivas, entre ellas `queue`, los tres trenes de octubre y la rama de VCX-D027; `main` es la viva restante. Las «44 sin contraparte o sin subir» de VCX-D030 son las 42 sin upstream más 2 vivas con commits adelante; no se suman a las 106 porque son conjuntos distintos | Repo de Blends | T2. En el paso 4 del mapa, inventario por nombre y SHA. Retiro en el checkout que opera, según la regla de T2: las 145 integradas y sin upstream vivo se retiran; las 3 sin integrar y sin upstream vivo se revisan una a una y se conservan como tag `archive/<rama>/<fecha>` si tienen valor, convención ya usada; las 32 con upstream vivo, incluidas `main` y la integrada, no se tocan. Retirar una rama no exige tren ni CI. Reversibilidad: antes de borrar una rama sin integrar se crea su tag `archive/`; las integradas se recuperan desde `main`; el reflog local conserva 90 días. Idempotencia: la lista por SHA se vuelve a ejecutar sin efecto sobre ramas ya retiradas |
| DH-02 | 26 tags locales: 19 `archive/`, 4 `rescate/`, `backup`, `ci-v1`, `ci-v2`. Solo `ci-v1` y `ci-v2` apuntan a commits de `main`; los otros 24 conservan ramas retiradas fuera de `main`. En GitHub hay 22: los 4 `rescate/` del 2026-08-29 son solo locales | Instancia privada; repo público de Blends solo para la CI | T1. Se transfieren los 26 a la instancia privada, el precursor continuado, y se verifican por SHA; son la convención de conservación que usa DH-01. Bajo VCX-D032 ningún tag `archive/`, `rescate/` ni `backup` pasa al repositorio público, porque apuntan fuera de la superficie publicable; `ci-v1` y `ci-v2` se recrean sobre los commits exportados solo si la biblioteca de CI forma parte del export, y los consumidores que fijan `@ci-v2` cambian de repositorio en DH-24. Los 4 tags solo locales se suben o se descartan con registro en el inventario del paso 4 |
| DH-03 | 32 ramas `tren/*` locales, 3 en GitHub; worktrees de `queue` y trenes en `.git-queue/` y `.git-trains/`, ignorados | Repo de Blends | T1 para los worktrees: no se copian, el clon no los crea hasta el corte operativo. T2 para las ramas `tren/*` integradas, con la misma regla y reversibilidad de DH-01 |
| DH-04 | `core.hooksPath` apunta a `/Users/denispaiva/blends/.githooks`, ruta anterior inexistente; los hooks no corren en ese checkout. Es el control SEC-08 del [inventario de controles](../../architecture/security-controls-inventory.md) | Checkout | T1 en el clon: `hooksPath` relativo y verificación de que `pre-commit` y `pre-push` se ejecutan bloqueando un secreto de prueba. En el precursor es condición previa de toda escritura por excepción: se corrige primero, con alcance propio del PO de Blends, y se comprueba de la misma forma. Reversibilidad: restaurar el valor anterior de `core.hooksPath` |
| DH-05 | Cuatro carpetas de worktrees bajo `vc/teyst/.claude/worktrees/`, sin seguimiento y no registradas en este repositorio | Checkout | T1. Se inventarían y no se copian al clon; su valor se decide antes de apartar el precursor |
| DH-06 | Sin seguimiento: `img/`, dos manifiestos de migración de Teyst, `.claude/settings.local.json`; ignorados: `outputs/` con 597 entradas, `graphify-out/`, `node_modules/` | Checkout o instancia | T1. Inventario del paso 4; cada uno con destino explícito o descarte registrado. Lo ignorado no se transfiere |

### Nombres de carpetas

| ID | Evidencia [H] | Destino | Tratamiento [P] |
|---|---|---|---|
| DH-07 | «blends» nombra cuatro cosas: el repositorio GitHub del precursor completo, la carpeta `../blends`, el producto Blends y la carpeta `vcx/blends/` de documentos objetivo; además «Blends Kernel» nombra el núcleo de gobierno | Vocabulario de la raíz; repo de Blends | T0 para el nombre del repositorio mientras rija VCX-D026 sin enmienda: la continuidad lo conserva y tras la reubicación el repositorio es el producto. Si VCX-D032 se ratifica, el nombre deja de ser T0 y el renombre en GitHub es T2 en el operador, según la ampliación de abajo. T2 para apartar la carpeta del precursor en la Fase C con un nombre que no sea `blends`, por ejemplo con sufijo de fecha y «precursor»; se decide al autorizar esa fase |
| DH-08 | `vc/` («Vibe Coding») contiene kernel, Brix e iniciativas como hermanos: `teyst` 564 archivos, `tooling` 369, `tools` 237, `melquisedec` 180, `brix` 82, `pinot-index` 62, `docs` 51, `finops` 12, `salmanazar` 5, `framework` 1 | Repo de Blends | T3 primero: al extraer Brix e iniciativas, `vc/` queda con kernel, registros y estándares. T2 después: el nombre final de esa carpeta se decide en Blends, sin renombrar por inferencia |
| DH-09 | Tres carpetas «brix»: `ideas/brix` (etapa de idea), `vc/brix` (código graduado) y `vcx/brix/` (documentos objetivo). `brix.config.json` en la raíz del precursor ya declara `graduate.remote` `denispaiva/brix` y `graduate.defaultPath` `vc/brix` | Repo de Brix | T3. La extracción usa el destino que el precursor ya anticipó, previa comprobación de que ese remoto existe y de su contenido. `ideas/brix` es historia de la idea y viaja con los datos de instancia, no con Brix |
| DH-10 | `vc/framework/` contiene solo `.roadmap.json`; su movimiento a `vc/kernel/` está aprobado por el PO (spec del precursor del 2026-10-05, reevaluada el 2026-10-24) con seis disparadores y ventana estimada 2026-11-03 a 2026-11-14. Los identificadores `framework`, `frameworkVersion`, `framework#<id>` y `blends-framework` no cambian | Repo de Blends | T2, como ya está aprobado y bajo ese procedimiento. T0 para los identificadores. La ventana coincidía con la posible Fase B; el usuario eligió el 2026-11-01 ejecutarlo después, en el repositorio destino, y nunca en el precursor |
| DH-11 | `vc/tools/` (código) y `vc/tooling/` (registros) conviven con `vc/docs/tooling/` y el prefijo de rama `tooling/*`; el precursor aprobó separar la configuración del kernel hacia `vc/kernel/registry/` como Fase 2 de la misma spec, y descartó renombrar `tooling/` | Repo de Blends | T2, como está aprobado. VCX no propone otro nombre |
| DH-12 | `ideas/trasiego` existe; Trasiego es candidato para las convenciones compartidas en VCX-D008 | Raíz | T0. Sigue pendiente; no se asigna por inferencia |
| DH-13 | Una misma iniciativa aparece en `ideas/<slug>` y en `vc/<slug>` según su etapa, por ejemplo `pinot-index`; la identidad hoy depende de la ruta y del tag de ciclo | Instancia de Cellar | T3. Al reubicar una instancia, la identidad se conserva por el modelo de iniciativa, no por la carpeta; ambas carpetas viajan juntas |

Ampliación por VCX-D032, 2026-11-01: DH-07 incluye también el renombre del repositorio en GitHub, no solo de la carpeta, porque el nombre `blends` pasa al repositorio público nuevo. Se agrega **DH-24**: 24 archivos rastreados del precursor que no son documentación citan `denispaiva/blends` por nombre, entre ellos `vc/tools/deliver.mjs`, `vc/tools/lib/train-actions.mjs`, tests y datos, y la biblioteca de CI se consume por nombre y tag; tratamiento T2 en el operador vigente antes de renombrar, con verificación por lista y después de DH-04, porque es una escritura en el precursor. Reversibilidad: un solo commit, revertible mientras el renombre no se ejecute; después del renombre la redirección de GitHub cubre `git` y la web pero no `uses:` de Actions, de modo que revertir exige deshacer el renombre primero. Los consumidores externos de la biblioteca no se verificaron: se verifican en el paso 4 buscando `denispaiva/blends/.github/workflows` en los demás repositorios de la cuenta antes de fijar la fecha del renombre.

### Jerarquía de carpetas

| ID | Evidencia [H] | Destino | Tratamiento [P] |
|---|---|---|---|
| DH-14 | En la raíz del precursor: `idea` (script), `roadmap.html` y `role-matrix.html` (vistas generadas), `roadmap/` (constructor del dashboard), `SCOPE-EXCEPTION.md`, `brix.config.json`, `skills-lock.json` | Repo de Blends; Brix para su configuración | T2 para vistas y constructor: el dashboard lee `vc/*/.roadmap.json`; tras la extracción debe leer las fuentes declaradas por el contrato de conducción de Cellar. T3 para `brix.config.json`, que pertenece al consumidor de Brix y se reescribe por repositorio |
| DH-15 | `.claude/` con 258 archivos rastreados (186 skills, 63 agentes, 8 comandos) y `.agents/` con 48, en la raíz del precursor, para todo el portfolio | Cada producto e instancia | T3. Cada repositorio extraído recibe solo el subconjunto que usa, según la [matriz de tooling](../../architecture/tooling-matrix.md) de VCX-D028; no se copia la carpeta entera |
| DH-16 | Workflows de proyectos en la raíz: `melquisedec-deploy.yml`, `teyst-deploy.yml`; `vc/brix/.github/workflows/ci.yml` anidado, que GitHub no ejecuta en esa posición | Cada repositorio | T3. Cada extracción lleva sus workflows; el cupo de Actions es de la cuenta y rige la política de escasez del precursor |
| DH-17 | Datos de portfolio dentro del kernel: `vc/finops/` (ledger central, proyectos heredados), `vc/tooling/environment-ids.json`, `vc/tooling/evaluations/history/` inmutable | Instancia de Cellar; registro inmutable permanece | T3 con VCX-D009 y VCX-D010. T0 para `evaluations/history/`, que no se reescribe |

### Desacoples

| ID | Evidencia [H] | Destino | Tratamiento [P] |
|---|---|---|---|
| DH-18 | Kernel → Brix: 39 imports desde `vc/tools/` y `roadmap/` hacia `vc/brix/`; 72 archivos fuera de `vc/brix/` citan esa ruta. Brix → kernel: un solo import, desde un test de FinOps hacia `validate-versions.mjs` | Repos de Blends y Brix | T3. Antes de extraer: el kernel consume Brix como dependencia declarada del paquete `packages/cli`, no por ruta; el import inverso se elimina. La estrategia de historial de Brix sigue pendiente y no bloquea este inventario |
| DH-19 | Registro de capacidades de Brix dentro del kernel: `vc/tooling/brix-capabilities.json` y `vc/docs/tooling/brix-capabilities.md` | Repo de Brix | T3. El registro de capacidades es contrato de Brix; el kernel conserva solo lo que consume |
| DH-20 | Teyst consume `scoring` de Pinot Index en proceso: 30 archivos de `vc/teyst/` lo citan; la decisión 0002 de Pinot Index (2026-08-21) lo define como librería por contrato con mecanismo de empaquetado sin elegir | Instancias de Cellar | T3. La extracción de ambas iniciativas exige elegir ese mecanismo; hasta entonces viajan juntas o se declara la dependencia |
| DH-21 | Enlaces documentales en VCX hacia fuera del directorio del producto: Blends 27, Brix 18, Cellar 20, `cellars` 4; de la raíz hacia productos 32. Crecieron desde la medición del 2026-10-30 (25, 13, 18) | Cada producto en VCX | T2 por producto, según la [preparación de enlaces](../../architecture/repository-map.md#preparación-de-enlaces-y-principios); los cinco documentos de Blends se resuelven al incorporarlos al clon |
| DH-25 | El comando `/council` del precursor implementa el consejo dentro del kernel; VCX-D033, acordado el 2026-11-01, fija que la skill `brix-llm-council` de Brix es la fuente canónica y que `/council` «pasará a adaptador delgado al migrar Blends», deuda declarada sin tocar el precursor | Repos de Blends y Brix | T3 con Brix: el adaptador se escribe cuando el kernel consume Brix como dependencia declarada (DH-18), no antes; hasta entonces conviven dos implementaciones y la de Brix es la canónica. No se agrega por este inventario ninguna escritura en el precursor |

### Declarado, sin acción

| ID | Evidencia [H] | Tratamiento |
|---|---|---|
| DH-22 | Repositorios heredados fuera del portfolio: `syrah`, `merlot` y el Teyst original, bajo el estándar de mantenimiento mínimo del precursor | T0. Fuera del alcance de la migración; el estándar sigue rigiendo en Blends |
| DH-23 | Convención «todo repositorio nace privado y se abre por espejo curado», del `vc/README.md` del precursor | T0. Rige para cada repositorio extraído; VCX no la cambia |

## Integración con el camino de migración

[P] El inventario se incorpora a las fases de VCX-D030 sin agregar fases nuevas:

- **Antes de la Fase B**, en el operador vigente y solo por excepción registrada: DH-04 en el precursor, que es condición de las demás; luego DH-24 antes del renombre de VCX-D032. DH-10 ya no figura aquí: el usuario eligió no ejecutarlo en el precursor. Cada una con rama, alcance y tren propios, según la sección siguiente.
- **Fase B** ejecuta los T1: DH-02, DH-03 (worktrees), DH-04 en el clon, DH-05 y DH-06 forman parte del inventario del paso 4 y de la configuración del clon del paso 5. El paso 4 vuelve a medir la foto de este inventario; si pasaron más de siete días o `main` cambió, las cifras se reemplazan antes de ejecutar nada.
- **Entre las fases B y C** no se ejecuta ningún T2 en el clon: el clon escribe ramas y hace push, y el operador vigente sigue siendo el único que corre `queue` y trenes. Un T2 urgente en ese intervalo se ejecuta en el operador por excepción, como los anteriores, o espera.
- **Después de la Fase C**, en el clon y bajo el gobierno de Blends, se ejecutan los T2 restantes: DH-01, DH-03 (ramas), DH-11, DH-14 y lo que no se haya ejecutado antes. DH-10 y DH-11 siguen sus specs aprobadas en el precursor; el único cambio es el checkout donde se ejecutan.
- **Fase D** usa los T3 como prerrequisitos de cada extracción: Brix requiere DH-09, DH-18, DH-19 y DH-25; cada instancia requiere DH-13, DH-16, DH-17 y DH-20; todas requieren DH-15.
- **Fase C** no absorbe deuda: el corte operativo solo cambia quién opera. Si la Fase C se interrumpe con dos checkouts vivos, el operador sigue siendo `../blends` hasta que el cotejo de refs del paso 11 se complete; el clon no asume la operación por inferencia.

Conflicto resuelto por el usuario el 2026-11-01: la ventana aprobada para DH-10, 2026-11-03 a 2026-11-14, se superponía con la posible Fase B. Entre ejecutar el movimiento en el operador vigente con excepción de escritura y DH-04 corregido antes, o hacerlo después en el destino, el usuario respondió «Después, en el destino». [I] La ventana vence sin ejecución; según VCX-P7 la aprobación del 2026-10-24 se conserva y, antes de ejecutar, el PO revisa su aplicabilidad y vuelve a medir sus seis disparadores, sin borrarla.

[I] Con VCX-D032 ratificada, «el clon» de esta sección es la instancia privada, el precursor continuado. Los T2 sobre rutas del kernel que el export lleve al repositorio público `blends`, entre ellas DH-10, se ejecutan ahí una vez creado por el paso 3 de la [secuencia de visibilidad](2026-11-01-public-visibility-design.md#secuencia), porque desde entonces esas rutas quedan congeladas en la instancia. Los T2 de Git, DH-01 y DH-03, siguen en la instancia, que conserva las ramas y los tags.

## Escrituras en el precursor antes del corte operativo

[H] La regla general del precursor es solo lectura, pero ya hay excepciones acordadas o previstas, cada una con alcance propio:

| Excepción | Autoridad | Alcance | Estado |
|---|---|---|---|
| VCX-D027 | Usuario, 2026-10-31 | Worktree aparte, rama `feat/framework-backlog-view`, push; el operador encola | Precedente, ejecutado |
| VCX-D033, punto 4 | Usuario, 2026-11-01; ejecución bajo autorización posterior | Evaluación con `/tool`, escritura acotada a dos archivos de evaluación | Acordado, sin ejecutar |
| DH-10, opción 1 | PO de Blends, spec del 2026-10-05 reevaluada el 2026-10-24 | Movimiento `vc/framework/` → `vc/kernel/` en su ventana | Descartada por el usuario el 2026-11-01: se ejecuta después, en el destino |
| DH-24 | Pendiente, con VCX-D032 | 24 archivos que citan `denispaiva/blends`, antes del renombre | Propuesto |
| DH-04 en el precursor | PO de Blends | `core.hooksPath` y comprobación de hooks | Propuesto como condición de las anteriores |

[P] Reglas para estas escrituras: DH-04 se corrige y se comprueba antes de cualquier otra, porque hoy el precursor no ejecuta su guardia de secretos y la compuerta de CI actúa recién al integrar, cuando el contenido ya llegó al remoto; cada excepción escribe en una rama, hace push y encola por el operador, nunca directamente en `main` ni en `queue`; una excepción no se extiende a otra; el inventario del paso 4 las lista con su rama y su SHA de cierre. [I] Con estas excepciones, «nunca en el precursor» ya no describe lo acordado; la regla vigente es «en el precursor solo por excepción registrada, con hooks activos y por el proceso de trenes».

## Autoridad, reversibilidad y costo por tratamiento

[P] Autoridad según la [RACI](../../architecture/responsibility-matrix.md#4-matriz-raci-humana-propuesta) y la propuesta VCX-D034, pendiente de ratificación: el PO de Blends sobre el precursor, la instancia que lo continúa y los T2 del repositorio de Blends; el responsable del portfolio sobre la raíz y los productos en `vcx/`, incluidos los T3 de Brix y Cellar; el PO de cada proyecto sobre su extracción. Hasta ratificar, cada corrección requiere autorización puntual del usuario con alcance explícito. La clasificación T0–T3 y la nota de este documento provienen del mismo autor; el consejo del 2026-11-01 fue una lectura independiente que no las validó ni puntuó, y la ratificación de VCX-D031 es la revisión que cuenta.

| Tratamiento | Identidad de la operación | Reversibilidad | Costo principal |
|---|---|---|---|
| T1 | Clon identificado por SHA de `main` y lista de refs cotejada | Total hasta la colocación: el clon se descarta y el precursor no cambió. Tras colocar, se revierte apartando el clon y restaurando los cinco documentos de `vcx/blends/` desde la raíz | Tiempo del operador; sin CI |
| T2 de Git (DH-01, DH-03) | Lista de ramas por nombre y SHA, fechada | Tag `archive/` antes de borrar lo no integrado; reflog 90 días; lo integrado se recupera de `main` | Sin trenes ni cuota de Actions |
| T2 de carpetas y archivos (DH-10, DH-11, DH-14, DH-24) | Rama y tren por ítem; SHA de cierre | Revertir el commit del tren; DH-24 solo antes del renombre | Un tren por ítem: corridas de CI en repositorio privado, bajo la política de escasez |
| T3 | Export con hash del historial exportado y tag en el origen | Antes de borrar en el origen, el repositorio nuevo debe tener CI verde y recuperación comprobada; el origen conserva un puntero y un tag | Repositorios nuevos, CI por repositorio, tiempo de revisión del scan |
| T0 | Declaración con procedencia | No aplica | Revisión en cada puerta |

[H] Escritor único: en esta máquina no hay launchd ni cron que escriban en el precursor, y el token de la CLI es uno con alcance `repo`. [I] Eso no demuestra que no exista otra máquina u otro servicio con acceso al repositorio; `syrah` muestra que hay escritores automáticos en la cuenta. Antes de la Fase C el inventario del paso 4 lista los pushes recientes por actor con la API de eventos de GitHub y las ramas vivas con commits adelante; lo que no se pueda demostrar queda declarado como límite, no como supuesto cumplido.

## Distribución y vigencia

[H] Por tratamiento principal, 25 ítems: T1 5 (DH-02, DH-03, DH-04, DH-05, DH-06), T2 7 (DH-01, DH-07, DH-10, DH-11, DH-14, DH-21, DH-24), más la parte de ramas de DH-03, T3 10 (DH-08, DH-09, DH-13, DH-15 a DH-20, DH-25), T0 3 (DH-12, DH-22, DH-23), más partes T0 en DH-07, DH-10 y DH-17. Los T0 no tienen plazo porque declaran identificadores, historial inmutable o repositorios ajenos; tienen responsable: la autoridad del repositorio donde viven, que vuelve a comprobar la declaración en cada puerta de transición del inventario de controles. DH-12 es una decisión pendiente del usuario, VCX-D008, no una deuda permanente.

[P] Vigencia de la foto: medida el 2026-11-01 sobre `f86a2a7d`, que seguía siendo `main` al revisar. Antes de abrir la ventana de DH-10 o de iniciar la Fase B, quien ejecute el paso 4 repite las mediciones listadas en la verificación y reemplaza las cifras; una diferencia de ramas o tags no invalida el inventario, pero sí la lista por SHA que se use para retirar.

## Qué no hace esta propuesta

- No renombra identificadores de máquina ni reescribe historial.
- No borra ramas, tags ni worktrees en el precursor.
- No cambia nombres de carpetas por inferencia; las reorganizaciones ya aprobadas conservan su procedimiento y su autoridad.
- No decide la estrategia de historial de Brix ni la ubicación de instancias.
- No mueve código a la raíz de VCX, que no es producto.

## Nota orientativa

7 de 10 tras la revisión, según VCX-P2; no es aprobación. La versión anterior se puntuó 8 y tenía una contradicción interna, el lugar de ejecución de los T2, que el consejo detectó y esta revisión corrige. Descuentos: un punto porque los disparadores de las specs aprobadas del precursor no se volvieron a medir aquí, en particular el contenido de `queue`; un punto porque los mecanismos de extracción de Brix y de Pinot Index siguen sin elegir y condicionan los T3; un punto porque el escritor único no se puede demostrar con medios locales y la regla de T2 depende de excepciones de escritura cuya disciplina no tiene control ejecutable. Sin sobrediseño: no se proponen carpetas, herramientas ni fases nuevas.

## Verificación de esta entrega

Mediciones repetibles con `git for-each-ref` con `%(upstream)` y `%(upstream:track)`, `git branch --merged main`, `git tag` con `git merge-base --is-ancestor`, `git ls-remote --tags origin`, `git ls-files`, `git grep` y `git worktree list` sobre `../blends`, sin escribir. Las cifras de DH-01 y DH-02 se repitieron el 2026-11-01 en la revisión; las sumas cierran: 106 + 42 + 32 = 180, 105 + 40 + 1 = 146 sin `main`, y 1 + 2 + 30 + `main` = 34 no integradas o `main`; 146 + 34 = 180. Enlaces relativos de este documento comprobados contra el árbol del 2026-11-01. El precursor no recibió ningún cambio.
