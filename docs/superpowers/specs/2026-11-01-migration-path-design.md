# Camino de migración del precursor a VCX: destino de las decisiones y clon de autoría

Fecha: 2026-11-01. Estado: propuesta del asistente, registrada como VCX-D030 en el [registro de decisiones](../../decisions/README.md) y ratificada por el usuario como decisión documental el 2026-11-01, con la colocación del clon que fija el [ajuste por la visibilidad pública](#ajuste-por-la-visibilidad-pública); la ejecución sigue requiriendo autorización. El usuario preguntó en el chat con Claude cómo se imagina la migración desde `../blends` hacia `vcx/` y fijó una restricción: «es importante que las nuevas decisiones se vayan construyendo en el destino final». Aprobó registrar esta propuesta y cerrar la verificación del commit base; no autorizó clonar, mover carpetas, inicializar Git en productos ni escribir en el precursor. No sustituye VCX-D025 ni VCX-D026 ni el [mapa](../../architecture/repository-map.md); propone un reordenamiento y una regla, para que el usuario decida.

Enmienda por VCX-D045, 2026-11-05: Blends Kernel deja de ser entidad objetivo; donde este documento dice «rutas del kernel» como destino rige la superficie publicable de Blends, según el [diseño del retiro](2026-11-05-kernel-retirement-design.md). El texto siguiente se conserva como historia.

Etiquetas: [U] definición o respuesta del usuario; [H] hecho comprobado con referencia; [I] interpretación del asistente; [P] propuesta pendiente de revisión.

## Hechos comprobados el 2026-11-01

Lecturas de solo lectura sobre ambos repositorios; ningún comando escribió en `../blends`.

| Ámbito | Observación |
|---|---|
| Raíz `vcx/` | [H] Cinco commits en `main` desde el commit base `f47c71f` del 2026-10-31; 49 archivos rastreados, entre ellos los 5 de Blends, 5 de Brix y 8 de Cellar bajo la excepción transitoria de VCX-D026; sin remoto; sin `.gitignore`. La recuperación del commit base quedó verificada el 2026-11-01 según el [reporte](../reports/2026-11-01-root-baseline-verification.md) |
| Precursor `../blends` | [H] `main` en `f86a2a7d`; `origin` es GitHub `denispaiva/blends`; 180 ramas locales, 44 sin contraparte remota o con commits sin subir; tres worktrees: principal, `feat/framework-backlog-view` de VCX-D027 y `queue`; `.git` de 144 MB; sin stashes |
| Escritores del precursor | [H] Hooks en `.githooks` (`pre-commit`, `pre-push`, `commit-msg`), `vc/tools/queue.mjs`, trenes en `.git-trains/`. No se detectaron tareas de launchd ni cron que lo nombren; la ausencia no prueba que no haya otros escritores |
| Hallazgo | [H] `core.hooksPath` vale `/Users/denispaiva/blends/.githooks`, ruta anterior del repositorio que ya no existe. [I] El repositorio ya fue reubicado una vez moviendo la carpeta, y los hooks, incluida la guardia de secretos del estándar, no se ejecutan hoy en ese checkout. No se corrige: el precursor es de solo lectura y el cambio requiere alcance propio |
| Contenido del precursor | [H] Kernel de Blends (`vc/tools`, `vc/tooling`, `vc/docs/standards`, rama `queue`, trenes); Brix en `vc/brix/` con `docs/decisions` 0001 a 0007; cuatro iniciativas graduadas en `vc/teyst`, `vc/melquisedec`, `vc/pinot-index` y `vc/salmanazar`, cada una con `docs/decisions`; `ideas/`, `roadmap/` y `vc/finops` |

## Idea central: reubicar primero, extraer después

[I] El precursor no «migra hacia» VCX. Se reubica como `vcx/blends/` continuando el mismo repositorio, como acuerda VCX-D026, y después se achica: Brix sale de `vc/brix/`, las iniciativas van a `cellars/<instancia>` cuando VCX-D009 y VCX-D010 lo resuelvan, y Cellar producto nace nuevo. La migración es una inversión de contención: hoy `blends` contiene todo; mañana `vcx/` es una carpeta que organiza repositorios independientes y no los rastrea.

**El destino final es un repositorio, no una carpeta.** Esto cambia la lectura de la restricción del usuario.

### Destino de cada clase de decisión

| Clase de decisión | Destino final | Dónde se escribe hoy | Estado |
|---|---|---|---|
| Conjunto: topología, principios, nombres, reparto entre productos | `vcx/docs/decisions` con IDs `VCX-Dxxx` | Ahí mismo | Correcto |
| Método, kernel, proceso, gobierno, `queue` y trenes de Blends | Repositorio `denispaiva/blends`, cuyo checkout futuro es `vcx/blends/` | En la raíz con clasificación «Blends» (VCX-D017, VCX-D019) o en ninguna parte, por la regla de solo lectura del precursor | Provisorio; es lo que el usuario quiere evitar |
| Capacidades de Brix | `vc/brix/docs/decisions` dentro del repositorio de Blends hasta la extracción; viaja con el subárbol | Ídem | Provisorio |
| Cellar producto: modelo de iniciativa, plantillas | Repositorio propio nuevo, paso 3 del mapa | `vcx/cellar/`, rastreado por la raíz | Provisorio, sin precursor que lo frene |
| Proyectos e iniciativas | `vc/<iniciativa>/docs/decisions` en el repositorio de Blends hasta reubicar la instancia | Precursor, solo lectura | Bloqueado |

[I] Lo que hoy impide escribir en el destino para Blends, Brix e iniciativas no es la secuencia del mapa. Son dos cosas: la regla de solo lectura del precursor y que el clon todavía no existe. VCX-D027 ya probó el patrón que lo resuelve: un checkout aparte escribe ramas, hace push y el operador vigente encola.

## Dos planos de corte, no uno

[H] El mapa trata el cambio de canonicidad como un único corte, el paso 10, posterior al corte de escritores del paso 8. [P] Propongo separar dos planos:

1. **Plano de autoría y decisiones.** Se corta temprano. El clon se coloca en `vcx/blends/` en cuanto está verificado; desde ese momento toda decisión de Blends, Brix e iniciativas se escribe ahí, en ramas, y se integra por el proceso vigente. El precursor deja de recibir decisiones nuevas.
2. **Plano operativo.** Se corta después. `queue`, trenes, hooks y automatizaciones siguen corriendo en `../blends` hasta que el inventario de escritores del paso 4 demuestre que puede haber un único escritor en el clon, pasos 8 y 11. Un solo operador por superficie compartida, como exige VCX-D026.

El clon es, en la práctica, un worktree grande con la disciplina de VCX-D027: escribe ramas, no ejecuta `queue.mjs` ni trenes, no crea `.git-queue/` ni `.git-trains/` hasta el corte operativo.

## Secuencia propuesta

### Fase A · Documental en la raíz

Ejecutada el 2026-11-01 con la aprobación del usuario: esta spec, la fila VCX-D030, la sección de destino de decisiones y las notas en el mapa, la verificación y el reporte del commit base, y las entradas de vocabulario. No toca `../blends`, no clona, no inicializa Git en productos, no crea `.gitignore`.

### Fase B · Clon de autoría

Corresponde a los pasos 4 a 7 y 9 del mapa, más la colocación anticipada del paso 10. Requiere una autorización propia que fije ubicación temporal, rama, documentos y acciones permitidas.

1. Inventario de referencias por nombre y SHA, ramas sin subir, worktrees, archivos sin seguimiento (`img/`, manifiestos de migración de Teyst, `.claude/settings.local.json`), configuración local con rutas absolutas, hooks y scripts del tren.
2. Cerrar o registrar el trabajo en vuelo del worktree de VCX-D027; su push ya está autorizado.
3. Clon autónomo desde `../blends` a una ubicación temporal, sin objetos prestados; remoto `precursor` local de transferencia separado de `origin` GitHub; verificación de las referencias requeridas, `queue` incluida, por SHA.
4. Configuración explícita del clon: `core.hooksPath` relativo (`.githooks`), dependencias instaladas, sin `.git-queue/` ni `.git-trains/`; comprobar que los hooks se ejecutan.
5. Incorporar los cinco documentos objetivo de `vcx/blends/` en una rama del clon, fusionando `AGENTS.md` y resolviendo sus enlaces a `../docs` según la [preparación de enlaces](../../architecture/repository-map.md#preparación-de-enlaces-y-principios); congelar la versión rastreada por la raíz.
6. Colocación: apartar `vcx/blends/` a una ubicación autorizada sin borrarla; colocar el clon en `vcx/blends/`; `.gitignore` de la raíz con `/blends/`; retirar del índice raíz los cinco documentos; comprobar que la raíz no los rastrea y no contiene gitlinks ni submódulos.
7. Comprobar la carga de instrucciones: en `vcx/blends/` una sesión carga `vcx/AGENTS.md` y el `CLAUDE.md` del producto, que importa su `AGENTS.md`; fijar el recurso de principios adoptados y verificar con la versión real de la herramienta que no hay dos versiones en contexto.

Desde entonces: decisiones de Blends, Brix e iniciativas en `vcx/blends/`; push de ramas; encolado a través del operador en `../blends`.

### Fase C · Corte operativo

Pasos 8 y 11 del mapa. Con el inventario de escritores: suspender automatizaciones del precursor con autorización separada, recrear el worktree de `queue` en el clon, cotejar referencias y declarar canonicidad. `../blends` queda apartado e inactivo, sin borrarse.

### Fase D · Extracciones

Independientes entre sí y de la Fase C.

- Cellar producto: inicializar su repositorio en `vcx/cellar/`, paso 3; no depende del precursor y puede adelantarse.
- Brix: extracción de `vcx/blends/vc/brix/` con historia; la elección entre subtree y filtrado de historia sigue pendiente y no bloquea. Sus decisiones ya están en la ruta que viaja.
- Iniciativas e `ideas/`: a `cellars/<instancia>` cuando VCX-D009 y VCX-D010 se resuelvan; cada extracción deja un puntero en el repositorio de origen.

## Deuda heredada

[U] El usuario pidió aprovechar la migración para ordenar la deuda técnica heredada: desacoples, conflictos de nombres de carpetas, orden de Git y jerarquías de carpetas. [P] El [inventario de deuda heredada](2026-11-01-inherited-debt-design.md), propuesta VCX-D031, mide 23 ítems y asigna a cada uno un repositorio destino y uno de cuatro tratamientos: se resuelve al reubicar (Fase B), se resuelve en el repositorio destino bajo su gobierno (después de la Fase B), se resuelve por extracción (Fase D) o se declara sin tocar. Ninguna fase nueva; ninguna corrección implícita durante el clon.

## Ajuste por la visibilidad pública

[U] El usuario pidió después que VCX, Blends, Brix y Cellar sean públicos, que la CI no consuma cuota de Actions y que los proyectos vivos sigan privados. [P] El [diseño de visibilidad](2026-11-01-public-visibility-design.md), propuesta VCX-D032, concluye que el precursor no puede volverse público porque contiene esos proyectos y su historial, y que continúa privado como la instancia de Cellar. En consecuencia, el clon de autoría de la Fase B se coloca en `vcx/cellars/<instancia>/` y no en `vcx/blends/`; `vcx/blends/` pasa a ser el checkout de un repositorio público nuevo, exportado y revisado. La separación de planos y la regla de un solo operador no cambian. VCX-D032 y esta colocación se ratificaron el 2026-11-01: las menciones anteriores a `vcx/blends/` como lugar del clon se leen como `vcx/cellars/<instancia>/` y se conservan como antecedente. VCX-D036, ratificada el 2026-11-02, cambia esa colocación a `vcx/cellars/` como repositorio de la instancia, sin nivel intermedio. [I] Hasta que exista el `blends` público, las decisiones del kernel se escriben en sus rutas dentro del clon de la instancia y viajan con el export por rutas; desde su creación se escriben solo en el público.

## Alternativas evaluadas

| Opción | Costo | Evaluación |
|---|---|---|
| (a) Mantener el orden del mapa: decisiones de Blends en la raíz con clasificación y traslado al final | Doble escritura y traslado masivo | Acumula lo que el usuario quiere evitar |
| (b) Clon de autoría temprano, corte operativo después | Dos checkouts del mismo repositorio; disciplina de un solo operador | Recomendada: satisface la restricción, reutiliza el patrón de VCX-D027 y avanza la reubicación |
| (c) Puente: excepciones de escritura por rama en `../blends`, como VCX-D027, sin clon | Mínimo | Perpetúa el precursor como lugar de trabajo; sirve solo como puente hasta la Fase B |

Nota orientativa de (b), según VCX-P2: 8 de 10. Descuentos: un punto por el riesgo de doble escritor hasta el corte operativo; un punto porque reordena un paso de VCX-D026 y requiere decisión del usuario. No es aprobación ni medición objetiva.

## Riesgos y contraejemplos

- **Doble escritor en `queue`.** El clon nunca ejecuta `queue.mjs` ni trenes antes de la Fase C; verificar que no existe `.git-queue/` en el clon.
- **Ramas sin subir.** Un clon normal las trae como referencias remotas del origen de transferencia, no como ramas locales; reconstruir solo según el plan y verificar por SHA.
- **Rutas absolutas.** El `hooksPath` roto demuestra que mover carpetas rompe configuración; en el clon, toda configuración relativa y verificada.
- **Enlaces de los cinco documentos objetivo.** Hoy apuntan a `../docs`; resolverlos al incorporarlos.
- **Doble carga de principios.** Comprobar con la versión real de Claude Code, sin presumir herencia.
- **Trabajo en vuelo en el worktree de VCX-D027.** Cerrarlo o recrearlo antes de colocar el clon.
- **Inventario incompleto de escritores.** No haber encontrado launchd ni cron no prueba su ausencia; el paso 4 debe revisar sesiones activas, scripts del tren y configuración de credenciales.

## Pendientes

1. Ratificación o rechazo de VCX-D030 por el usuario; hasta entonces rige el orden del mapa.
2. Alcance autorizado de la Fase B: ubicación temporal, rama, documentos y acciones.
3. Tratamiento del `hooksPath` roto en el precursor: hoy sin guardia de secretos activa en ese checkout; corregirlo requiere alcance separado.
4. Estrategia de historial de Brix y ubicación de instancias, ya pendientes en el mapa.

## Verificación de esta entrega

Enlaces relativos y anclajes de los archivos de la Fase A comprobados con el script del [plan de aplicación de VCX-D029](../plans/2026-11-01-product-model-application.md#comprobaciones). Recuperación del commit base verificada y registrada en el [reporte](../reports/2026-11-01-root-baseline-verification.md). Ningún comando escribió en `../blends`.
