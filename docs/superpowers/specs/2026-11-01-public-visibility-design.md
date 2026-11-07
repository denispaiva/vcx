# Visibilidad pública de los productos y CI sin cuota de Actions

Fecha: 2026-11-01. Estado: propuesta del asistente, registrada como VCX-D032 en el [registro de decisiones](../../decisions/README.md) y ratificada por el usuario como decisión documental el 2026-11-01, con la opción B y la salida B'; ningún paso de la secuencia queda autorizado para ejecutar. El usuario pidió en el chat con Claude: «Algo que quisiera cambiar es que VCX, BLENDS, BRIX y CELLAR, quisiera hacerlos públicos en Github y no consumir quota de actions en el proceso CI. Si dejaría en private a los proyectos vivos bajo cellars, ej. teyst». Este documento evalúa el pedido, verifica sus supuestos y propone cómo cumplirlo sin romper el precursor. No cambia la visibilidad de ningún repositorio ni crea repositorios.

Enmienda por VCX-D045, 2026-11-05: Blends Kernel deja de ser entidad objetivo; donde este documento dice «rutas del kernel» como destino rige la superficie publicable de Blends, según el [diseño del retiro](2026-11-05-kernel-retirement-design.md). El texto siguiente se conserva como historia.

Enmienda por VCX-D053, 2026-11-05: la carpeta local de la instancia pasa de `vcx/cellars/` a `vcx/solera/`; las menciones siguientes se conservan como historia.

Etiquetas: [U] pedido del usuario; [H] hecho verificado con referencia; [I] interpretación; [P] propuesta.

## Hechos verificados el 2026-11-01

| Tema | Hecho |
|---|---|
| Costo de Actions | [H] Según la [facturación de GitHub Actions](https://docs.github.com/en/billing/managing-billing-for-your-products/about-billing-for-github-actions), los runners estándar alojados por GitHub en repositorios públicos son gratuitos y no reducen el uso incluido; los runners grandes se facturan también en públicos; los autoalojados son gratuitos. En privados, el plan Free incluye un equivalente aproximado a 2000 minutos Linux por mes y Pro unos 3000 |
| Plan de la cuenta | [H] No se leyó: la API de facturación exige el scope `user`, que el token actual no tiene. La política de escasez del precursor ya trata el cupo como uno por cuenta |
| Cambio de visibilidad | [H] Según la [documentación de visibilidad](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility), al volver público un repositorio el código queda visible para cualquiera, el historial y los logs de Actions se hacen públicos y cualquiera puede hacer fork |
| Regla del precursor | [H] Invariante 38 de `role-matrix.md`: ningún repositorio privado se vuelve público; la apertura es por espejo curado con superficie publicable declarada e historia propia. Nunca son publicables importes, identificadores de facturación ni comprobantes |
| Contenido del precursor | [H] 2220 commits; 1088 tocan rutas del kernel. Contiene el código vivo de Teyst, Melquisedec, Pinot Index y Salmanazar, `vc/finops/` con ledgers, 14 IDs de entorno en `environment-ids.json`, y 131 archivos de rutas del kernel que mencionan importes o facturación, en su mayoría estándares y changelogs. Los scanners `betterleaks` y `gitleaks` actúan como compuerta de commit, no como prueba sobre el historial |
| Renombrar un repositorio | [H] Según la [documentación de renombre](https://docs.github.com/en/repositories/creating-and-managing-repositories/renaming-a-repository), Git y web redirigen al nombre nuevo; las referencias `uses:` de Actions no se redirigen; y la redirección deja de funcionar si se crea otro repositorio con el nombre viejo. En el precursor, 24 archivos rastreados que no son documentación citan `denispaiva/blends`, entre ellos `deliver.mjs`, `train-actions.mjs`, tests y datos |
| Biblioteca de CI | [H] Los workflows reutilizables viven en `blends/.github/workflows/` y los consumidores los citan por nombre y tag (`denispaiva/blends/.github/workflows/ci-node.yml@ci-v2`); los tags `ci-v1` y `ci-v2` existen en GitHub. Hoy ningún archivo rastreado del precursor los consume por nombre; consumidores externos no se verificaron |
| Nombres ocupados | [H] `blends` y `brix` existen como privados; `brix`, `pinot-index` y `teyst-blends` son espejos detenidos; `vcx` y `cellar` están libres |
| Repositorio raíz | [H] `vcx/` local: 22 commits; una dirección de correo en el registro de decisiones; 31 rutas locales absolutas en documentos históricos; sin importes; sin secretos detectados por búsqueda, que no es un scan |

## Lectura del pedido con el modelo de productos

[I] El pedido coincide con la partición que el [README](../../../README.md#cómo-se-organiza) ya hace: el grupo A, base reutilizable (VCX, Blends, Brix, Cellar), sería público; el grupo B, ideas y proyectos vivos en instancias de Cellar, seguiría privado. Lo público es el método, las capacidades y las plantillas; lo privado son los datos, el código de los proyectos y su infraestructura.

[P] Regla de visibilidad: los repositorios del grupo A nacen públicos a partir de un export revisado de su superficie publicable; los del grupo B nacen privados y nunca se vuelven públicos. El invariante 38 del precursor se conserva íntegro para el grupo B y se precisa para el A: la publicación nunca es un cambio de visibilidad de un repositorio existente, es un repositorio nuevo con contenido e historia revisados.

## Por qué el precursor no puede volverse público

[I] Tres razones, cada una suficiente:

1. Contiene el código de Teyst y de los demás proyectos vivos, que el usuario quiere privados. Hacer público `blends` tal cual publicaría exactamente lo que se pide mantener privado.
2. Su historial de 2220 commits incluye ledgers, IDs de entorno, datos de uso y evidencia con referencias de facturación. Lo publicado queda expuesto para siempre; reescribir el historial sobre 180 ramas, `queue` y trenes rompería el sistema que opera hoy.
3. Viola el invariante 38 bajo el cual se construyó todo el precursor.

Conclusión: Blends público es un repositorio nuevo, y el precursor sigue privado. Lo que cambia es qué es el precursor después de la migración: deja de ser Blends y pasa a ser la instancia privada de Cellar, el portfolio con sus proyectos vivos, ideas, FinOps, backlog y evidencia.

## Opciones

| Opción | Qué hace | Costo | Evaluación |
|---|---|---|---|
| A. Cambiar la visibilidad de `blends` y `brix` | Lo literal del pedido | Expone proyectos vivos y datos; rompe el invariante 38; exige reescribir historial operativo | Rechazada |
| **B. Blends público como repositorio nuevo con historial filtrado por rutas** | Export de las rutas del kernel conservando sus commits; scan completo del historial exportado; revisión del PO sobre importes en estándares; repositorio público nuevo | Un export con `git filter-repo` o equivalente, un scan y una revisión; conserva el blame de 1088 commits | Recomendada si el scan y la revisión salen limpios |
| B'. Blends público con historial nuevo | Igual que B pero el export se aplana en un commit inicial, como exige la letra del invariante 38 | Pierde el blame público; el historial completo sigue en la instancia privada | Alternativa de respaldo si B no pasa el scan, o por simplicidad |
| C. Canónico privado y espejo público | El estándar actual del precursor | La CI sigue en el repositorio privado y consume cuota | No cumple el pedido de CI sin cuota |

[U] El 2026-11-01 el usuario eligió «Historial filtrado», la opción B, en el chat con Claude; la elección no ratifica el resto de este diseño ni autoriza ejecución. [P] Recomendación que esa elección confirma: B, con B' como regla de salida fijada de antemano: si el scan del historial exportado encuentra un solo hallazgo real, se publica con historial nuevo y no se intenta limpiar commit por commit. Nota orientativa de B: 8 de 10 según VCX-P2; descuentos de un punto porque el scan y la revisión de importes están pendientes, y un punto porque convierte VCX-D009, el nombre de la instancia, en bloqueante del nombre `blends`.

## Estructura objetivo

[P] Reemplaza la tabla de objetivo de la [organización en GitHub](../../architecture/github-topology.md) en lo que respecta a visibilidad y origen.

| Repositorio | Visibilidad | Contenido | Origen | Checkout local |
|---|---|---|---|---|
| `vcx` | Público | Raíz documental: principios, visión, arquitectura, decisiones, nombres | El repositorio local actual, tras revisar la dirección de correo y las rutas locales históricas | `vcx/` |
| `blends` | Público, nuevo | Producto Blends: kernel, método, estándares, biblioteca de CI con sus tags `ci-v*` | Export revisado de las rutas del kernel del precursor | `vcx/blends/` |
| `brix` | Público, nuevo | Producto Brix: núcleo de capacidades | Export revisado de `vc/brix/`, sin `data/` ni `finops/` | `vcx/brix/` |
| `cellar` | Público, nuevo | Producto Cellar: modelo de iniciativa, plantillas, contrato de conducción | `vcx/cellar/` | `vcx/cellar/` |
| Instancia de Cellar, `solera` por VCX-D009 | Privado | El precursor continuado: proyectos vivos, `ideas/`, `vc/finops/`, IDs de entorno, historial de evaluaciones, `queue` del portfolio, despliegues | Renombre del repositorio `blends` actual, con su historial íntegro | `vcx/cellars/`, por VCX-D036 |
| Un repositorio por proyecto, cuando VCX-D010 lo decida | Privado | Código de cada proyecto | Extracción desde la instancia | `vcx/cellars/<proyecto>/`, por VCX-D036 |
| `Teyst`, `syrah`, `merlot`, `TintumHero` | Sin cambio | Heredados y ajenos | Sin cambio | Ninguno |

VCX-D036, ratificada el 2026-11-02 en el [registro](../../decisions/README.md), cambia esta colocación a `vcx/cellars/` como repositorio de la instancia, con cada proyecto en `vcx/cellars/<proyecto>/`, para que la estructura local replique la de GitHub; lo siguiente queda como antecedente. Consecuencia local: el clon de autoría de VCX-D030 no se coloca en `vcx/blends/` sino en `vcx/cellars/<instancia>/`, porque el precursor continuado es la instancia; `vcx/blends/` pasa a ser el checkout del repositorio público nuevo. Cada carpeta local corresponde a un repositorio y a un producto o instancia, sin excepciones.

## CI sin cuota

[P] Lo que se obtiene y lo que no:

- Los workflows del kernel y de Brix (`Blends CI`, `CI Node`, `Brix Vibe Coding CI`, `train-notice`, `escasez-monitor`, `Renovaciones próximas`) pasan a repositorios públicos y dejan de consumir cuota, siempre que usen runners estándar. Los runners grandes se facturan también en público y quedan prohibidos en el grupo A.
- Los despliegues de proyectos (`teyst-deploy`, `melquisedec-deploy` y los futuros) siguen en la instancia privada y consumen cuota como hoy. La política de escasez del precursor sigue rigiendo ahí; el cupo es uno por cuenta y más repositorios no lo amplían. El consumo privado baja porque la CI del kernel sale de él.
- La biblioteca de CI pública puede consumirse desde repositorios privados sin el permiso de acceso por API que hoy exige el estándar entre privados.
- Los logs de Actions de los repositorios públicos son visibles: la verificación sin credenciales que ya fija el invariante 42 pasa de buena práctica a requisito.
- La verificación local previa al tren sigue siendo la primera línea; publicar no es razón para mover más trabajo a Actions.

## Secuencia

[P] Ajusta las fases de VCX-D030; cada paso requiere su autorización.

0. Ratificar VCX-D032 y elegir B o B': hecho el 2026-11-01, B con salida B'. Resolver VCX-D009, el nombre de la instancia, bloqueante del paso 3: resuelto el 2026-11-01 con `solera`.
1. `vcx` público: revisar la dirección de correo y las rutas locales en el historial, crear el repositorio público vacío y subir `main`. No depende de nada más y no toca el precursor.
2. Renombrar el precursor a la instancia: actualizar primero, en el operador y con su gobierno, los 24 archivos que citan `denispaiva/blends`, `brix.config.json`, remotos de clones y worktrees y tareas programadas; después renombrar en GitHub y verificar que `queue`, trenes y despliegues siguen funcionando con el nombre nuevo. Mientras no exista otro `blends`, la redirección protege lo que quede sin actualizar.
3. `blends` público: declarar la superficie publicable por rutas, exportar según B o B', correr el scan sobre todo el historial exportado, revisar los importes de estándares y changelogs, crear el repositorio público con ese nombre, lo que termina la redirección del paso 2, subir `main` y los tags `ci-v*`, configurar protección y CI. Desde ese momento las decisiones de Blends se escriben ahí; las rutas del kernel en la instancia quedan congeladas con un puntero.
4. `brix` público: apartar el espejo actual con otro nombre o archivarlo, exportar `vc/brix/` sin `data/` ni `finops/`, scan, repositorio público nuevo, y que el kernel lo consuma como dependencia declarada según DH-18.
5. `cellar` público: al inicializar el producto, paso 3 del mapa.
6. Proyectos: siguen en la instancia privada hasta VCX-D010; su extracción es privada.

## Qué cambia en las decisiones vigentes

- **VCX-D026.** La continuidad del repositorio del precursor con su historial íntegro se conserva, pero en la instancia privada, no en el producto Blends; Blends público recibe el historial exportado. Enmendada por el usuario el 2026-11-01.
- **VCX-D030.** La colocación del clon de autoría cambia a `vcx/cellars/<instancia>/`; el principio de escribir las decisiones en el destino no cambia. Ratificada con esa colocación el 2026-11-01.
- **VCX-D031.** DH-07 suma el renombre del repositorio, no solo de la carpeta; se agrega la deuda de las 24 referencias por nombre y de los consumidores externos de la biblioteca de CI.
- **VCX-D009.** Deja de ser un pendiente de diseño y pasa a bloquear el nombre público `blends`. El usuario eligió `solera` el 2026-11-01.
- **Organización en GitHub.** La tabla de objetivo y su frase «todos privados al nacer» quedan sustituidas por la regla de visibilidad por grupo.

## Riesgos y contraejemplos

- **Exposición irreversible.** Un hallazgo que el scan no detecte queda público para siempre. Mitigación: scan sobre todo el historial exportado con dos herramientas, revisión humana de los 131 archivos con importes, y B' como salida fijada de antemano.
- **Pérdida de redirección.** Crear el `blends` público termina la redirección del renombre; todo clon, worktree y tarea que no se haya actualizado en el paso 2 apunta al repositorio equivocado sin error visible. Mitigación: verificación por lista antes del paso 3.
- **Consumidores de la biblioteca de CI.** Si un repositorio fuera del precursor consume `denispaiva/blends/...@ci-v2`, seguirá funcionando solo si el `blends` público conserva los workflows y los tags. Verificar en `syrah` y `merlot` antes del paso 3.
- **Dos `blends` durante la transición.** Entre los pasos 2 y 3 no hay ninguno; entre el 3 y el congelamiento, el privado renombrado y el público coexisten. La regla de un solo escritor por superficie se aplica por rutas: el kernel se escribe solo en el público.
- **Rutas absolutas.** El renombre se hace en el operador vigente y reproduce el riesgo de DH-04; el inventario de configuración local es prerrequisito.
- **Plan de la cuenta sin leer.** No cambia la conclusión: en público, los runners estándar son gratuitos en todos los planes.

## Qué no autoriza esta propuesta

No cambia la visibilidad de ningún repositorio, no renombra, no crea repositorios, no exporta historial, no corre scans sobre el precursor ni modifica sus archivos. Cada paso de la secuencia se autoriza por separado con alcance, autoridad y verificación propios.

## Verificación de esta entrega

Tres documentos de GitHub leídos el 2026-11-01 y citados; mediciones de solo lectura sobre `../blends` y la cuenta con la CLI autenticada; búsqueda de correo, importes y rutas en el árbol rastreado de `vcx/`. Enlaces relativos comprobados contra el árbol del 2026-11-01. Ningún repositorio ni archivo del precursor cambió.
