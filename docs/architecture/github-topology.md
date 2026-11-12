# Organización en GitHub: hoy y objetivo

Fecha: 2026-11-01. Estado: la sección «Hoy» es evidencia medida en solo lectura con la CLI de GitHub autenticada como `denispaiva`; la sección «Objetivo» deriva de VCX-D025 y VCX-D029 y de VCX-D030, VCX-D031 y VCX-D032, ratificadas como decisiones documentales el 2026-11-01; ningún paso en GitHub está autorizado. El usuario pidió «más precisión con cómo se organiza la información hoy en github y cómo se estructurará en el futuro, sin romper nada». Este documento no crea, renombra ni modifica repositorios; cada cambio en GitHub figura abajo con la fase y la autorización que requiere.

Etiquetas: [H] hecho medido; [I] interpretación; [P] propuesta.

## Hoy

### Repositorios de la cuenta

[H] Ocho repositorios, todos privados, ninguno archivado, ninguno fork. No existen `vcx` ni `cellar`. Actualización del 2026-11-02: existe `denispaiva/vcx`, público, creado con autorización del usuario y con `main` en `4b01168`; `cellar` sigue sin existir. Actualización del 2026-11-09: existe `denispaiva/cellar`, público, con `main` en `ca00822`, creado con autorización del usuario según VCX-D059; la raíz lo ignora y su checkout es `vcx/cellar/`.

| Repositorio | Rol hoy | Rama por defecto | Último push | Observación |
|---|---|---|---|---|
| `blends` | Precursor completo: kernel de Blends, Brix, iniciativas, ideas, FinOps, instrucciones y skills | `main` | 2026-11-01 | Única fuente de verdad del portfolio; 29 ramas remotas, 22 tags, un PR abierto (`tren/2026-10-29`, 11 vagones), ocho workflows activos |
| `brix` | Espejo de solo lectura de `vc/brix` | `main` | 2026-09-14 | Su descripción dice que la fuente es `vc/brix` en `blends` y que no se commitea ahí; `brix.config.json` del precursor lo declara como `graduate.remote` |
| `pinot-index` | Espejo de `vc/pinot-index`, resguardo del código de producción | `main` | 2026-09-12 | Detenido desde septiembre |
| `teyst-blends` | Repositorio canónico de Teyst desde el 2026-11-05, según VCX-D049; antes, espejo de `vc/teyst` | `main` | 2026-11-05 | Migración en curso; el deploy sigue en `blends`. Es distinto del `Teyst` heredado |
| `Teyst` | Repositorio heredado, anterior a `vc/teyst` | `main` | 2026-08-20 | Bajo el estándar de mantenimiento mínimo del precursor |
| `syrah` | Repositorio heredado, deprecado | `pilot` | 2026-10-31 | Recibe commits automáticos de «baseline diario»: hay un escritor activo fuera de `blends` |
| `merlot` | Repositorio heredado, deprecado | `main` | 2026-02-18 | Sin actividad |
| `TintumHero` | Web oficial de Tintum | `main` | 2026-02-05 | Fuera del portfolio y de esta migración |

### Cómo fluye la información hoy

- [H] Todo entra a `blends` por ramas con prefijo de alcance, se integra por trenes (`tren/<fecha>`, un PR por tren) y `main` está protegida: `enforce_admins` activo y cuatro checks obligatorios, `base / verify`, `governance`, `lint` y `teyst`. No hay rulesets.
- [H] El backlog vive en la rama `queue` del mismo repositorio, cuyo tip remoto coincide con el local al 2026-11-01.
- [H] Los tags `archive/<rama>/<fecha>` conservan ramas retiradas; `backup/`, `ci-v1` y `ci-v2` son marcas puntuales.
- [H] Los tres espejos se generan desde `blends` con `brix graduate`, que extrae una subcarpeta mediante `git subtree`, hacia un repositorio separado. No reciben commits propios y hoy van siete semanas detrás de `blends`.
- [H] Los workflows de despliegue de Teyst y Melquisedec corren en `blends`; `vc/brix/.github/workflows/ci.yml` existe anidado y GitHub no lo ejecuta en esa posición. El cupo de Actions es de la cuenta y lo administra la política de escasez del precursor.
- [H] Convenciones vigentes del precursor que esta migración conserva: todo repositorio nace privado y se abre solo por espejo curado con superficie publicable declarada (invariante 38); `main` se integra por PR con CI verde y biblioteca de CI con versión fijada (invariante 42); guardia de secretos en commit y push (invariante 39).
- [H] La raíz `vcx/` local tiene Git sin remoto. Nada de VCX está en GitHub.

## Objetivo

Un repositorio por producto y por proyecto, organizados localmente bajo `vcx/` y sin submódulos, según VCX-D025 y VCX-D029. La visibilidad y el origen de cada uno los fija VCX-D032, ratificada el 2026-11-01 y detallada más abajo; la tabla siguiente ya la incorpora.

| Repositorio objetivo | Contenido | De dónde sale | Cómo nace | Fase |
|---|---|---|---|---|
| `vcx` | Repositorio documental raíz: principios, visión, arquitectura, decisiones, nombres | `vcx/` local, ya con historia desde `f47c71f` | Crear vacío y hacer push de `main`. Público, elegido por el usuario el 2026-11-01 conforme a VCX-D032, tras la [revisión del historial](../superpowers/reports/2026-11-01-vcx-public-history-review.md); falta decidir si el correo del autor se reescribe antes del primer push. No afecta a ningún otro repositorio | A o B, con autorización propia |
| `blends` | Producto Blends: método, estándares, validadores, dashboard, biblioteca de CI | Export revisado de la superficie publicable de Blends (VCX-D045), con historial filtrado por rutas (VCX-D032, opción B) | Repositorio público nuevo, con historial nuevo si el scan encuentra un hallazgo real (B'). El nombre se libera al renombrar el precursor a `solera` (VCX-D009). Checkout `vcx/blends/` | Paso 3 de la secuencia de VCX-D032 |
| `brix` | Producto Brix: núcleo de capacidades | `vc/brix/` de `blends`, con la historia del subárbol | Repositorio público nuevo; el espejo actual se aparta y archiva por VCX-D056. Hasta ese día sigue siendo espejo y conserva su descripción | Etapas de VCX-D056, antes de `blends` público |
| `cellar` | Producto Cellar: modelo de iniciativa, plantillas, contrato de conducción | `vcx/cellar/`, documentación nueva | Crear vacío y público cuando el paso 3 del mapa se autorice | D, adelantable |
| Un repositorio por proyecto: `solera-teyst`, `solera-melquisedec`, `solera-pinot-index`, `solera-salmanazar` | Código de cada proyecto | `vc/<proyecto>/` de `blends`, con historia del subárbol | Prefijo `solera-` por VCX-D057, con checkout `vcx/solera/<proyecto>/`. `teyst-blends` es el canónico de Teyst por VCX-D049 y se renombra a `solera-teyst`; `pinot-index` es candidato a canónico por el mismo criterio que `brix` y, si se reutiliza, se renombra; Melquisedec y Salmanazar nacen nuevos con el prefijo. Cada uno lleva sus workflows de despliegue | D, por proyecto |
| Un repositorio por instancia de Cellar | Custodia del portfolio: proyectos vivos, iniciativas, decisiones, evidencia, FinOps, `queue` del portfolio, despliegues | La primera es el precursor `blends`, continuado y renombrado con su historial íntegro (VCX-D026 enmendada) | Privado; no nace, se renombra en el paso 2 de la secuencia de VCX-D032. Nombre `solera` por VCX-D009, elegido el 2026-11-01; checkout `vcx/solera/`, por VCX-D036; A desde el renombre, el responsable del portfolio por VCX-D034 | B, renombre en el paso 2 |
| `Teyst`, `syrah`, `merlot` | Heredados | Sin cambio | No se tocan; el estándar de mantenimiento mínimo sigue rigiendo desde Blends | Ninguna |
| `solera-tintum` | Web oficial de Tintum (`hello/`), pitch y roadmap de la empresa | `TintumHero`, renombrado el 2026-11-12 | Proyecto de Solera por VCX-D068, privado, con checkout `vcx/solera/tintum/`. Antes estaba fuera del portfolio; desde el 2026-11-11 versiona el deck de `hello.tintum.app` (VCX-D061). Los enlaces viejos a `TintumHero` redirigen | Ejecutada el 2026-11-12 |

[I] Los espejos existentes ya materializan en GitHub la frontera que VCX-D025 pide: una subcarpeta de `blends`, exportada con historia propia, en un repositorio separado. La extracción canónica repite ese mecanismo con dos diferencias: el repositorio destino pasa a ser fuente editable y `blends` deja de contener la carpeta, dejando un puntero.

[I] VCX-D043, del 2026-11-05, adelanta la extracción de Teyst respecto de la colocación de la instancia y resuelve VCX-D010 solo para ese proyecto. La tabla anterior conserva el destino de cada repositorio; el orden de Teyst se rige por esa decisión.

## Visibilidad objetivo

VCX-D032, ratificada como decisión documental el 2026-11-01; fuente en el [diseño de visibilidad](../superpowers/specs/2026-11-01-public-visibility-design.md). Lo reutilizable es público; lo vivo es privado.

| Repositorio | Visibilidad | Cómo nace |
|---|---|---|
| `vcx`, `blends`, `brix`, `cellar` | Público | Repositorio nuevo a partir de un export revisado de su superficie publicable, con historial filtrado por rutas según eligió el usuario el 2026-11-01, y historial nuevo si el scan falla; nunca por cambio de visibilidad de uno existente |
| Instancia de Cellar, `solera` | Privado | El precursor continuado y renombrado, con su historial íntegro; nombre elegido en VCX-D009 el 2026-11-01 |
| Repositorios de proyecto | Privado | Extracción desde la instancia cuando VCX-D010 lo decida; nunca se vuelven públicos |
| Heredados y ajenos | Sin cambio | Sin cambio |

[H] Los runners estándar de GitHub en repositorios públicos no consumen la cuota de Actions; los grandes se facturan también en público. La CI de Blends y Brix deja de consumir cuota al publicarse; la del tren sigue en la instancia (VCX-D045); los despliegues de proyectos siguen en privado y consumen como hoy.

[I] Por esta decisión el precursor no se reubica como `vcx/blends/` sino como `vcx/solera/`, por VCX-D036 y VCX-D053, y `blends` público es un repositorio nuevo cuyo checkout ocupa `vcx/blends/`; la tabla de objetivo ya lo refleja. VCX-D036, ratificada el 2026-11-02, hace que la estructura local replique la de GitHub repositorio por repositorio: `vcx/solera/` es la instancia y cada proyecto vive en `vcx/solera/<proyecto>/` con repositorio propio.

## Qué no se rompe

[P] Invariantes de la transición, verificables en cada fase:

1. El precursor `blends` conserva historia, rama `queue`, tags, PR abierto, protección de `main` y workflows hasta que cada extracción retire lo suyo; conserva también el nombre hasta su renombre como instancia en el paso 2 de VCX-D032. Nunca se reescribe historia ni se borra en GitHub lo que el inventario de VCX-D031 marca como conservado.
2. Un solo operador escribe en `queue` y lanza trenes; el clon de autoría solo hace push de ramas, exactamente lo que hoy hacen las sesiones.
3. Ningún repositorio privado se vuelve público. Los públicos de VCX-D032 nacen como repositorios nuevos a partir de un export revisado, con scan del historial y aprobación humana; las instancias y los proyectos nacen privados.
4. Los espejos no reciben commits mientras sean espejos. Convertir uno en canónico es una decisión registrada en la extracción, con su descripción y protección cambiadas en ese momento.
5. Cada extracción deja `blends` verde: los checks obligatorios de `main` se ajustan en la misma entrega que retira el código que verifican. El check `teyst` es el primer caso.
6. Los despliegues no cambian de repositorio hasta que el repositorio nuevo tenga CI con la biblioteca fijada, credenciales del builder y una corrida verde; hasta entonces el workflow sigue en `blends`.
7. El cupo de Actions sigue siendo uno por cuenta: más repositorios no amplían el cupo, y la política de escasez se aplica al conjunto.
8. `syrah` sigue recibiendo su baseline automático; es un escritor conocido fuera de `blends` y no se detiene por esta migración.

## Riesgos observados

- [H] El check obligatorio `teyst` en `main` de `blends` acopla la protección del repositorio al proyecto: extraer Teyst sin ajustar la protección dejaría `main` sin poder integrarse.
- [H] Los espejos están detenidos desde septiembre; quien los lea como actuales se equivoca. Hasta la extracción, su único valor es resguardo.
- [I] Reutilizar un espejo como canónico hereda su historia exportada; si la extracción se hace con otro corte, habrá dos historias del mismo subárbol. Se elige una y se archiva la otra con tag, no se fusionan.
- [I] `brix.config.json` declara la rama `graduation-export`; el tag `archive/graduation-export/2026-10-15` muestra que ya se usó y se archivó. Toda extracción nueva verifica primero qué contiene el remoto.

## Decisiones que esto deja al usuario

1. Crear `denispaiva/vcx` y subir `main`: hecho el 2026-11-02, público, con `main` en `4b01168` tras la reescritura del correo y el scan de secretos; queda como antecedente. Era el único cambio en GitHub posible en la Fase A. La visibilidad quedó decidida el 2026-11-01: público, con la [revisión del historial](../superpowers/reports/2026-11-01-vcx-public-history-review.md) hecha; resta elegir si se reescribe el correo del autor antes del push. El [inventario de controles](security-controls-inventory.md) habla de «remoto privado» para SEC-01; rige esta decisión.
2. Reutilizar `brix`, `teyst-blends` y `pinot-index` como repositorios canónicos en su extracción, o crear nuevos y archivar los espejos. Para `brix` lo resuelve VCX-D056, ratificada el 2026-11-07: no se reutiliza, se aparta y archiva. Ver el [diseño de la extracción](../superpowers/specs/2026-11-07-brix-extraction-design.md#5-espejo).
3. Nombre de los repositorios de los proyectos sin espejo; la instancia ya tiene nombre, `solera`, por VCX-D009, con el [criterio de nombres](../naming.md).
