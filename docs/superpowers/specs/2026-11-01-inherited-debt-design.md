# Deuda heredada del precursor: inventario y tratamiento en la migración

Fecha: 2026-11-01. Estado: propuesta del asistente, registrada como VCX-D031 en el [registro de decisiones](../../decisions/README.md) con estado Propuesto. Complementa el [camino de migración](2026-11-01-migration-path-design.md) de VCX-D030. El usuario pidió en el chat con Claude: «Se debe aprovechar el momento para ordenar aquella deuda técnica heredada. Desacoples, conflictos de nombres de carpetas, orden de git, jerarquías de carpetas, etc.».

Etiquetas: [U] pedido o respuesta del usuario; [H] hecho medido con referencia; [I] interpretación del asistente; [P] propuesta pendiente de revisión.

## Qué significa «ordenar» bajo los principios

[H] VCX-P3 fija que «el incumplimiento heredado se declara como deuda, no se extiende ni se corrige mediante una migración implícita». [H] VCX-D011 exige conciliar con las decisiones aprobadas del precursor antes de reemplazar destinos o controles. [I] Ordenar la deuda durante la migración significa, entonces: inventariarla con evidencia, asignar a cada ítem un repositorio destino y una fase, y ejecutar cada corrección con alcance propio y bajo el gobierno del repositorio donde se resuelve. No significa corregir cosas de paso mientras se clona.

[P] Cuatro tratamientos, uno por ítem:

| Tratamiento | Qué es | Cuándo |
|---|---|---|
| **T1 · Se resuelve al reubicar** | Estado por checkout que el clon no hereda o que se fija al crearlo: configuración con rutas absolutas, hooks, worktrees, archivos sin seguimiento, caches | Fase B del camino de migración |
| **T2 · Se resuelve en el repositorio destino, bajo su gobierno** | Limpieza de Git y reorganizaciones de carpetas que el precursor ya aprobó o que corresponden a Blends; se ejecutan en el clon con `queue`, trenes y alcances vigentes | Después de la Fase B; nunca en el precursor |
| **T3 · Se resuelve por extracción** | Acoplamientos entre kernel, Brix e iniciativas que solo desaparecen cuando cada pieza tiene repositorio propio con dependencias declaradas | Fase D, por producto o instancia |
| **T0 · Se declara y no se toca** | Identificadores de máquina, historial inmutable, repositorios heredados fuera del portfolio | Permanente, con procedencia |

## Inventario medido el 2026-11-01

Lecturas de solo lectura sobre `../blends` en `main` `f86a2a7d`. Las cifras son una foto fechada, no un monitor.

### Orden de Git

| ID | Evidencia [H] | Destino | Tratamiento [P] |
|---|---|---|---|
| DH-01 | 180 ramas locales: 146 ya integradas en `main`, 106 con upstream borrado en GitHub, 37 `claude/*` sin upstream, una `los-gatos-802` fuera de convención. Ninguna anterior a 2026-09-08 | Repo de Blends | T2. En el paso 4 del mapa, inventario por nombre y SHA. En el clon, tras la reubicación: integradas y sin upstream se retiran; sin integrar y sin upstream se revisan una a una y se conservan como tag `archive/` si tienen valor, convención ya usada. Nada se borra en el precursor |
| DH-02 | 26 tags: 19 `archive/`, 4 `rescate/`, `backup`, `ci-v1`, `ci-v2` | Repo de Blends | T1. Se transfieren todos y se verifican por SHA; son la convención de conservación que usa DH-01 |
| DH-03 | 32 ramas `tren/*` locales, 3 en GitHub; worktrees de `queue` y trenes en `.git-queue/` y `.git-trains/`, ignorados | Repo de Blends | T1 para los worktrees: no se copian, el clon no los crea hasta el corte operativo. T2 para las ramas `tren/*` integradas, con la misma regla de DH-01 |
| DH-04 | `core.hooksPath` apunta a `/Users/denispaiva/blends/.githooks`, ruta anterior inexistente; los hooks no corren en ese checkout | Checkout | T1 en el clon: `hooksPath` relativo y verificación de que `pre-commit` y `pre-push` se ejecutan. La corrección en el precursor requiere alcance propio |
| DH-05 | Cuatro carpetas de worktrees bajo `vc/teyst/.claude/worktrees/`, sin seguimiento y no registradas en este repositorio | Checkout | T1. Se inventarían y no se copian al clon; su valor se decide antes de apartar el precursor |
| DH-06 | Sin seguimiento: `img/`, dos manifiestos de migración de Teyst, `.claude/settings.local.json`; ignorados: `outputs/` con 597 entradas, `graphify-out/`, `node_modules/` | Checkout o instancia | T1. Inventario del paso 4; cada uno con destino explícito o descarte registrado. Lo ignorado no se transfiere |

### Nombres de carpetas

| ID | Evidencia [H] | Destino | Tratamiento [P] |
|---|---|---|---|
| DH-07 | «blends» nombra cuatro cosas: el repositorio GitHub del precursor completo, la carpeta `../blends`, el producto Blends y la carpeta `vcx/blends/` de documentos objetivo; además «Blends Kernel» nombra el núcleo de gobierno | Vocabulario de la raíz; repo de Blends | T0 para el nombre del repositorio: la continuidad de VCX-D026 lo conserva, y tras la reubicación el repositorio es el producto. T2 para apartar la carpeta del precursor en la Fase C con un nombre que no sea `blends`, por ejemplo con sufijo de fecha y «precursor»; se decide al autorizar esa fase |
| DH-08 | `vc/` («Vibe Coding») contiene kernel, Brix e iniciativas como hermanos: `teyst` 564 archivos, `tooling` 369, `tools` 237, `melquisedec` 180, `brix` 82, `pinot-index` 62, `docs` 51, `finops` 12, `salmanazar` 5, `framework` 1 | Repo de Blends | T3 primero: al extraer Brix e iniciativas, `vc/` queda con kernel, registros y estándares. T2 después: el nombre final de esa carpeta se decide en Blends, sin renombrar por inferencia |
| DH-09 | Tres carpetas «brix»: `ideas/brix` (etapa de idea), `vc/brix` (código graduado) y `vcx/brix/` (documentos objetivo). `brix.config.json` en la raíz del precursor ya declara `graduate.remote` `denispaiva/brix` y `graduate.defaultPath` `vc/brix` | Repo de Brix | T3. La extracción usa el destino que el precursor ya anticipó, previa comprobación de que ese remoto existe y de su contenido. `ideas/brix` es historia de la idea y viaja con los datos de instancia, no con Brix |
| DH-10 | `vc/framework/` contiene solo `.roadmap.json`; su movimiento a `vc/kernel/` está aprobado por el PO (spec del precursor del 2026-10-05, reevaluada el 2026-10-24) con seis disparadores y ventana estimada 2026-11-03 a 2026-11-14. Los identificadores `framework`, `frameworkVersion`, `framework#<id>` y `blends-framework` no cambian | Repo de Blends | T2, como ya está aprobado y bajo ese procedimiento. T0 para los identificadores. La ventana coincide con la posible Fase B: el movimiento se ejecuta en un solo checkout, el operador vigente antes de reubicar o el clon después, nunca en ambos |
| DH-11 | `vc/tools/` (código) y `vc/tooling/` (registros) conviven con `vc/docs/tooling/` y el prefijo de rama `tooling/*`; el precursor aprobó separar la configuración del kernel hacia `vc/kernel/registry/` como Fase 2 de la misma spec, y descartó renombrar `tooling/` | Repo de Blends | T2, como está aprobado. VCX no propone otro nombre |
| DH-12 | `ideas/trasiego` existe; Trasiego es candidato para las convenciones compartidas en VCX-D008 | Raíz | T0. Sigue pendiente; no se asigna por inferencia |
| DH-13 | Una misma iniciativa aparece en `ideas/<slug>` y en `vc/<slug>` según su etapa, por ejemplo `pinot-index`; la identidad hoy depende de la ruta y del tag de ciclo | Instancia de Cellar | T3. Al reubicar una instancia, la identidad se conserva por el modelo de iniciativa, no por la carpeta; ambas carpetas viajan juntas |

Ampliación por VCX-D032, 2026-11-01: DH-07 incluye también el renombre del repositorio en GitHub, no solo de la carpeta, porque el nombre `blends` pasa al repositorio público nuevo. Se agrega **DH-24**: 24 archivos rastreados del precursor que no son documentación citan `denispaiva/blends` por nombre, entre ellos `vc/tools/deliver.mjs`, `vc/tools/lib/train-actions.mjs`, tests y datos, y la biblioteca de CI se consume por nombre y tag; tratamiento T2 en el operador vigente antes de renombrar, con verificación por lista. Los consumidores externos de la biblioteca no se verificaron.

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

### Declarado, sin acción

| ID | Evidencia [H] | Tratamiento |
|---|---|---|
| DH-22 | Repositorios heredados fuera del portfolio: `syrah`, `merlot` y el Teyst original, bajo el estándar de mantenimiento mínimo del precursor | T0. Fuera del alcance de la migración; el estándar sigue rigiendo en Blends |
| DH-23 | Convención «todo repositorio nace privado y se abre por espejo curado», del `vc/README.md` del precursor | T0. Rige para cada repositorio extraído; VCX no la cambia |

## Integración con el camino de migración

[P] El inventario se incorpora a las fases de VCX-D030 sin agregar fases nuevas:

- **Fase B** ejecuta los T1: DH-02, DH-03 (worktrees), DH-04, DH-05 y DH-06 forman parte del inventario del paso 4 y de la configuración del clon del paso 5.
- **Después de la Fase B**, en el clon y bajo el gobierno de Blends, se ejecutan los T2: DH-01, DH-03 (ramas), DH-10, DH-11 y DH-14, cada uno con rama, alcance y tren propios. DH-10 y DH-11 siguen sus specs aprobadas en el precursor; el único cambio es el checkout donde se ejecutan.
- **Fase D** usa los T3 como prerrequisitos de cada extracción: Brix requiere DH-09, DH-18 y DH-19; cada instancia requiere DH-13, DH-16, DH-17 y DH-20; todas requieren DH-15.
- **Fase C** no absorbe deuda: el corte operativo solo cambia quién opera.

Conflicto a resolver con el usuario como PO de Blends: la ventana aprobada para DH-10, 2026-11-03 a 2026-11-14, se superpone con la posible Fase B. Las dos opciones son ejecutar el movimiento en el operador vigente antes de reubicar, con la excepción de escritura que corresponda, o posponerlo al clon tras la reubicación. No se ejecuta en los dos.

## Qué no hace esta propuesta

- No renombra identificadores de máquina ni reescribe historial.
- No borra ramas, tags ni worktrees en el precursor.
- No cambia nombres de carpetas por inferencia; las reorganizaciones ya aprobadas conservan su procedimiento y su autoridad.
- No decide la estrategia de historial de Brix ni la ubicación de instancias.
- No mueve código a la raíz de VCX, que no es producto.

## Nota orientativa

8 de 10, según VCX-P2; no es aprobación. Descuentos: un punto porque los disparadores de las specs aprobadas del precursor no se volvieron a medir aquí, en particular el contenido de `queue`; un punto porque los mecanismos de extracción de Brix y de Pinot Index siguen sin elegir y condicionan los T3. Sin sobrediseño: no se proponen carpetas, herramientas ni fases nuevas.

## Verificación de esta entrega

Mediciones repetibles con `git for-each-ref`, `git ls-files`, `git grep` y `git worktree list` sobre `../blends`, sin escribir. Enlaces relativos de este documento comprobados contra el árbol del 2026-11-01. El precursor no recibió ningún cambio.
