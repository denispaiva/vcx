# Mapa de archivos y preparación de repositorios

Fecha inicial: 2026-10-30. Reformulación: 2026-10-31. Estado: secuencia documental acordada mediante VCX-D026. El 2026-10-31 se autorizó ejecutar únicamente el [commit base raíz](../superpowers/plans/2026-10-31-root-baseline-scope.md): el commit base es `f47c71f`, del 2026-10-31, con 39 documentos, y su recuperación se verificó el 2026-11-01 según el [reporte](../superpowers/reports/2026-11-01-root-baseline-verification.md). No se aplicaron exclusiones, movieron documentos ni ejecutaron migraciones. VCX-D030, ratificada el 2026-11-01, fija el [destino de las decisiones durante la transición](#destino-de-las-decisiones-durante-la-transición) y la colocación anticipada de un clon de autoría; VCX-D032, ratificada el mismo día, enmienda VCX-D026 y cambia qué es el precursor después de la migración.

La topología estable está en VCX-D025 y su transición y continuidad de Blends en VCX-D026 del [registro de decisiones](../decisions/README.md). Este mapa identifica las superficies actuales, sus destinos y la secuencia propuesta; no duplica la definición de contratos o principios.

## Inventario y destinos

El inventario de entrada comprende 37 documentos Markdown u OPML: 18 en la raíz y `docs/`, 5 en Blends, 5 en Brix, 8 en Cellar y el README de `cellars/`. Este mapa se añade después de ese inventario. Se excluyen metadatos `.DS_Store`, sin borrarlos. Ningún producto tiene todavía su repositorio Git creado en VCX.

Las rutas de las tablas son relativas a la raíz del workspace. Dentro de cada repositorio de producto se conserva la parte posterior a su nombre: por ejemplo, `cellar/docs/initiative-model.md` será `docs/initiative-model.md` en el repositorio de Cellar. Cellar puede conservar su ubicación final actual; la preparación debe respetar el congelamiento de la fuente antes de reemplazarla. Blends requiere la sustitución controlada de su carpeta documental por un clon que continúa el repositorio precursor, según la secuencia posterior; para Brix la estrategia de historial sigue pendiente.

### Repositorio documental raíz

| Archivos actuales | Destino y tratamiento |
|---|---|
| `AGENTS.md`, `README.md` | Raíz: instrucciones comunes y navegación; VCX no se convierte en producto |
| `docs/vision.md`, `docs/executive-pitch.md` | Raíz: visión del conjunto y posible mensaje comercial |
| `docs/architecture/overview.md`, `docs/architecture/responsibility-matrix.md` | Raíz: composición, fronteras y responsabilidades compartidas; conservar estados propuestos |
| `docs/architecture/interoperability.md` | Raíz: acuerdos entre productos y convenciones comunes; los contratos detallados de cada producto se mantienen con su dueño |
| `docs/architecture/current-system-mapping.md` | Raíz: evidencia histórica fechada; no actualizarla como si fuera un inventario vivo |
| `docs/architecture/repository-map.md` | Raíz: propuesta de preparación y localización de archivos, sin convertirse en backlog paralelo |
| `docs/decisions/README.md` | Raíz: decisiones del conjunto y sus fuentes de autoridad; las que afectan solo el contrato de un producto se trasladan a su repositorio según la clasificación de decisiones |
| `docs/naming.md`, `docs/references/enology-glossary-source.md` | Raíz: criterio de nombres y material histórico sin curar |
| `docs/sources.md` | Raíz: procedencia y localización de fuentes |
| `docs/superpowers/plans/2026-10-30-vcx-foundation.md`, `docs/superpowers/plans/2026-10-30-blends-cellar-curation.md` | Raíz: planes de etapas previas con su avance preservado |
| `docs/superpowers/reports/2026-10-30-vcx-foundation.md`, `docs/superpowers/reports/2026-10-30-blends-cellar-curation.md` | Raíz: evidencia de ejecución anterior, no nuevas fuentes de estado de producto |
| `docs/superpowers/specs/2026-10-30-cellar-blends-first-journey-design.md` | Raíz: diseño conjunto y ejemplo sintético; cada producto conserva sus definiciones específicas |
| `docs/exports/vcx-ecosystem.opml` | Raíz: instantánea histórica, no índice vigente de principios o decisiones |
| `docs/exports/vcx-ecosystem-2026-11-01.opml` | Raíz: vista derivada fechada con VCX-D029 aplicado; no es índice vigente de principios o decisiones |
| `docs/exports/build_portfolio_board_view.py`, `docs/exports/portfolio-board.template.html` | Raíz por ahora: generador y plantilla sin datos de la vista Tablero del portfolio, pedida por el usuario el 2026-11-02. Lee roadmaps y cola del precursor con `git show`, sin fetch. La página generada contiene datos de proyectos privados y no se versiona aquí por VCX-D032: se publica solo como artifact privado. Arrastrar o partir tarjetas registra propuestas en la base del artifact, nunca en la cola ni en los roadmaps. Replica la regla de orden del backlog y una proyección por velocidad: deuda declarada hasta el contrato de conducción de Cellar, que decidirá su ubicación |
| `cellars/README.md` | Raíz por ahora: punto de entrada informativo, no datos de una instancia real |

En el estado estable, la raíz no seguirá el contenido de los repositorios de producto ni fijará sus commits mediante submódulos. Como excepción transitoria, el commit base preservará los documentos actuales de los tres productos y se verificará su recuperación antes de transferirlos; su retirada del seguimiento se realizará por producto, no por anticipación. Cuando una decisión necesite referir versiones adoptadas, las identificará en su propio registro; no se crea ahora un catálogo duplicado de versiones.

#### Clasificación de decisiones

Un clon independiente debe contener la autoridad de sus propios contratos. Regla: una decisión cuyas consecuencias recaen solo en el contrato de un producto pasa al registro de ese producto; una decisión que afecta a varios productos o al conjunto permanece en la raíz y los productos la citan como referencia distribuida o pública. Al trasladar, el registro del producto conserva el ID `VCX-Dxxx` como procedencia y pasa a ser la fuente editable; la fila de la raíz se conserva marcada como trasladada, sin borrarse ni mantenerse como segunda fuente.

Clasificación inicial propuesta, a confirmar al preparar cada producto:

| Decisión | Clasificación | Motivo |
|---|---|---|
| VCX-D019 | Brix | Define sus comandos, equivalencias y ayuda de parámetros |
| VCX-D017 | Blends | Fija una compuerta de su proceso de ingreso; Cellar solo registra el resultado |
| VCX-D040 | Blends | Regla del método para reconsiderar la arquitectura de proyectos graduados; Cellar la aplica |
| VCX-D015, VCX-D016, VCX-D018 | Raíz | Reparten responsabilidades entre Cellar, Blends y Brix |
| Demás decisiones vigentes | Raíz | Topología, principios, nombres, instancias o conciliación del conjunto |

La clasificación no cambia el estado de ninguna decisión; un traslado se registra en la raíz con fecha y autoridad.

### Repositorios de producto

| Producto | Documentos actuales que se preservan e incorporan |
|---|---|
| Blends | `blends/README.md`, `blends/AGENTS.md`, `blends/docs/idea-intake.md`, `blends/docs/idea-to-project.md`, `blends/docs/architecture-and-finops.md` |
| Brix | `brix/README.md`, `brix/AGENTS.md`, `brix/docs/commands.md`, `brix/docs/idea-intake.md`, `brix/docs/reference-architecture.md` |
| Cellar | `cellar/README.md`, `cellar/AGENTS.md`, `cellar/docs/initiative-model.md`, `cellar/templates/cellar/README.md`, `cellar/templates/initiative/README.md`, `cellar/templates/initiative/AGENTS.md`, `cellar/templates/idea/README.md`, `cellar/templates/finops/README.md` |

Blends continuará el repositorio `denispaiva/blends`, con su historia y las referencias requeridas, incluida `queue`; no será una historia nueva ni un segundo producto respecto del precursor. Sus cinco documentos de VCX se incorporarán como cambios nuevos, fusionando `AGENTS.md` con las reglas vigentes sin sobrescribirlas a ciegas. Los destinos y colisiones se comprobarán al preparar la rama.

Las plantillas pertenecen al producto Cellar, aunque Blends coordine su uso y Brix las consuma. Para Cellar y Brix, los registros reales y datos del precursor no se trasladan por inferencia. En Blends, continuar el repositorio conserva inicialmente datos de portfolio y reglas heredadas: su coexistencia con el producto objetivo se declara deuda transitoria, no desacople completado. Su separación requiere resolver propiedad y ubicación con VCX-D009, VCX-D010 y la conciliación VCX-D011; no borrarlos por considerarlos datos de instancia.

## Preparación de enlaces y principios

La revisión previa encontró 25 enlaces Markdown que salen del directorio de Blends, 13 del de Brix y 18 del de Cellar. Estos enlaces funcionan en el workspace actual, pero no garantizan documentación utilizable desde un clon independiente.

Tratamiento propuesto por clase:

| Referencia actual | Resolución antes de declarar independencia |
|---|---|
| Producto → principios de la raíz | Recurso derivado local, con fuente y versión verificables; el AGENTS del producto lo incorpora explícitamente |
| Producto → contrato propio | Definición canónica dentro del producto; acordar su archivo cuando se detalle el contrato, sin crear documentos vacíos |
| Producto → convenciones comunes o contrato ajeno | Recurso distribuido identificado por versión o enlace público accesible; sin dependencia de la carpeta local de otro producto |
| Producto → reporte o decisión histórica de VCX | Referencia de procedencia con revisión identificable; si es necesaria para trabajar, hacerla accesible mediante una fuente publicada o evidencia distribuida, sin inventar URLs |
| Raíz → README o documento de producto | Navegación del workspace identificada como tal; para el clon raíz aislado, usar una referencia pública cuando exista o una localización textual explícita, sin presentar un destino ausente como enlace resoluble |
| Plantilla → instrucciones comunes futuras | Resolver el marcador contra los recursos realmente adoptados por el consumidor; no fijar rutas de la máquina de origen |

También hay enlaces desde documentos de raíz hacia productos que la raíz ignorará. La comprobación futura debe distinguir dos contextos: workspace completo y clon aislado. Un enlace válido en el primero puede estar roto en el segundo. Los antecedentes fechados conservan su procedencia, mientras las entradas vigentes deben explicar qué se necesita para navegar o trabajar.

Para distribuir principios propongo un recurso `docs/adopted-principles.md` en cada producto, derivado de la sección canónica de AGENTS.md. Debe identificar VCX-P1 a VCX-P9, versión documental `1.1.0`, procedencia, fecha e integridad del contenido adoptado; antes de distribuirlo se comprobará cuál es la versión vigente. Identificar la revisión del commit base raíz y el hash del contenido adoptado para cotejo; no mantener además una instantánea externa equivalente para esta garantía documental. La copia se actualiza explícitamente desde su fuente, no se edita como otra norma independiente. El nombre y este mecanismo son propuestas; todavía no se crean esos archivos.

La copia debe incluir el conjunto completo de principios, no solo sus títulos o IDs. Las reglas de dominio necesarias para un producto y sus instrucciones locales siguen siendo responsabilidad de su propio AGENTS. La incorporación debe comprobar esas referencias y la carga efectiva en el IDE utilizado; copiar principios no demuestra que se estén aplicando. Para Blends, fusionar el AGENTS vigente con el contexto de VCX y referenciar los principios adoptados desde la cadena de instrucciones que cargue su CLAUDE.md. Si se usa un import de Claude Code, debe apuntar al recurso local distribuido; conservar también instrucciones comprensibles para otras herramientas. Verificar la carga con la versión/configuración real, sin confiar en la herencia del AGENTS padre. No se cambia ahora ningún archivo del precursor.

Para Cellar y Brix, sin `CLAUDE.md`, el caso es el opuesto: según la [documentación de Claude Code](https://code.claude.com/docs/en/memory#agents-md), una sesión dentro de `vcx/` carga el AGENTS de la raíz y el del producto, y este expande sus imports. El workspace tendría así dos ejemplares de los principios en contexto. Se separan dos comprobaciones:

- **Integridad:** la copia adoptada coincide por hash con la revisión que declara haber adoptado, no con la raíz vigente. Un producto puede conservar `1.1.0` aunque la raíz avance; actualizarla es una adopción explícita del producto.
- **Carga compatible:** si en una misma sesión se cargarían versiones distintas, la verificación falla y esa configuración se detiene. Se resuelve qué versión corresponde a esa sesión; no se actualiza automáticamente el producto ni se edita la copia. Nunca importar `../AGENTS.md`: sale del producto y rompe el clon aislado.

## Exclusiones previstas de la raíz

Estado estable previsto para una futura `.gitignore`, todavía no aplicada. Las exclusiones de productos se activan por producto tras su incorporación verificada, no antes del commit base:

```gitignore
/blends/
/brix/
/cellar/
.DS_Store
/cellars/*
!/cellars/README.md
```

La regla de `cellars/` conserva solo su punto de entrada actual y evita incorporar datos de una instancia por accidente mientras su ubicación y almacenamiento estén pendientes. No resuelve esa decisión ni sustituye la revisión de archivos preparados antes del commit. No excluir por ahora todo `docs/`, las fuentes históricas o las plantillas de los repositorios que las poseen.

## Destino de las decisiones durante la transición

Estado: VCX-D030 del 2026-11-01, ratificada como decisión documental el mismo día junto con VCX-D032; fuentes en la [spec del camino de migración](../superpowers/specs/2026-11-01-migration-path-design.md) y el [diseño de visibilidad](../superpowers/specs/2026-11-01-public-visibility-design.md). El usuario fijó que las decisiones nuevas deben construirse en el destino final. El destino final es un repositorio, no una carpeta: el precursor continúa como instancia privada de Cellar en `vcx/cellars/<instancia>/` y se achica mediante extracciones; Blends es un repositorio público nuevo, exportado por rutas, en `vcx/blends/`. VCX-D036, ratificada el 2026-11-02, coloca la instancia en `vcx/cellars/` mismo, con cada proyecto extraído en `vcx/cellars/<proyecto>/`, para que cada carpeta local corresponda a un repositorio de GitHub.

| Clase de decisión | Destino | Mientras no exista el clon |
|---|---|---|
| Conjunto: topología, principios, nombres, reparto | Este registro, `VCX-Dxxx` | Igual |
| Método, kernel, proceso, gobierno, estándares | Repositorio público `blends`, checkout `vcx/blends/`; antes de su creación, rutas del kernel en el clon de la instancia, que viajan con el export | Raíz con clasificación «Blends», a trasladar |
| `queue` y trenes del portfolio | Instancia privada `solera`, checkout `vcx/cellars/` | Operador vigente `../blends` |
| Capacidades de Brix | `vc/brix/docs/decisions` en la instancia hasta la extracción a `brix` público | Igual que Blends |
| Cellar producto | Repositorio propio del paso 3 | `vcx/cellar/`, rastreado por la raíz |
| Proyectos e iniciativas | `vc/<iniciativa>/docs/decisions` en la instancia privada | Bloqueado por la regla de solo lectura |

La decisión separa dos planos: el de autoría y decisiones, que se corta al colocar un clon de autoría en `vcx/cellars/` tras los pasos 4 a 7 y 9; y el operativo, que se corta en los pasos 8 y 11 cuando el inventario de escritores lo permita. Hasta ese corte, `../blends` es el único operador de `queue`, trenes y hooks, y el clon no los ejecuta ni crea `.git-queue/` ni `.git-trains/`. El patrón es el de VCX-D027: escribir ramas en un checkout aparte, hacer push y encolar a través del operador vigente.

La deuda heredada del precursor se ordena dentro de esta misma secuencia, según el [inventario de VCX-D031](../superpowers/specs/2026-11-01-inherited-debt-design.md): lo que depende del checkout se resuelve al crear el clon (paso 5), la limpieza de Git y las reorganizaciones aprobadas se ejecutan en el único checkout que opera en cada momento, y los acoplamientos entre kernel, Brix e iniciativas se resuelven en cada extracción. Nada se corrige de paso; en el precursor solo se escribe por excepción registrada y con sus hooks activos. El movimiento de `vc/framework/` a `vc/kernel/` se ejecuta después, en el repositorio destino, por elección del usuario del 2026-11-01.

La [organización en GitHub](github-topology.md) registra, con evidencia del 2026-11-01, los ocho repositorios actuales de la cuenta, cómo fluye hoy la información y el repositorio objetivo de cada pieza, con los invariantes que la transición no rompe.

## Secuencia acordada para preservar y versionar

1. **Autorizar la ejecución concreta.** VCX-D026 aprueba estas decisiones y su documentación, pero no operaciones Git o de filesystem. Antes de ejecutar, fijar los repositorios, ubicaciones temporales, rama de incorporación, archivos y acciones permitidas. El precursor conserva la protección de solo lectura; el permiso futuro de escritura queda limitado al clon nuevo y su alcance. Conservar el gobierno de Blends y tramitar cualquier cambio a ese gobierno por separado.
2. **Crear y verificar el commit base documental raíz.** Con autorización, inicializar solo la raíz e incorporar una lista explícita de documentos actuales, incluidos los cinco de Blends, los cinco de Brix y los ocho de Cellar, además de acuerdos y navegación. Excluir metadatos, secretos, datos operativos y repositorios embebidos; no agregar indiscriminadamente el árbol. Registrar la revisión base y comprobar que permite recuperar los documentos con su integridad. Este es el mecanismo elegido de preservación documental; no añadir una instantánea externa equivalente. Git local no es respaldo fuera de la máquina. No aplicar todavía exclusiones de producto ni retirar sus documentos.
3. **Preparar cada producto con su estrategia de historial propia.** Trasladar también sus decisiones según la [clasificación de decisiones](#clasificación-de-decisiones). Cellar parte de su documentación nueva; Blends continúa el repositorio precursor y no importa una historia ajena sobre una historia vacía. Brix requiere elegir entre unir documentación de VCX con historia extraída de `vc/brix/` o comenzar documentalmente con procedencia explícita y una extracción posterior. Revisar su espejo y destino canónico antes de elegir; no resolver esa alternativa por inferencia ni bloquear por ella a Cellar o Blends. Cellar → Blends → Brix sigue siendo el orden de curación documental; extraer Brix es además un cambio coordinado dentro de Blends.
4. **Inventariar la transferencia y los escritores de Blends.** Leer referencias y SHA, ramas locales y upstreams, tags y otras referencias necesarias, incluidos `queue` y antecedentes fuera del árbol principal. La medición de solo lectura del 2026-10-31 registró 179 ramas locales, 44 sin contraparte remota o con commits sin subir y ningún stash: revalidar esos datos al transferir, no tratarlos como una constante. Inventariar por separado archivos sin seguimiento e ignorados necesarios, configuración local, hooks, tareas programadas, scripts del tren y sesiones/worktrees activos que puedan actuar sobre `queue` o el remoto. Registrar ubicación, acción, disparador, autoridad, estado y forma de suspensión/verificación de cada escritor; no incluir valores secretos en la evidencia. No ejecutar `worktree prune`, reparación, push o desactivaciones como efecto colateral. La lectura del 2026-11-01 encontró `core.hooksPath` apuntando a `/Users/denispaiva/blends/.githooks`, ruta anterior del repositorio que ya no existe: los hooks no se ejecutan en ese checkout, prueba de que mover carpetas rompe la configuración con rutas absolutas. Inventariar toda configuración local con rutas absolutas y fijarla en relativo en el clon; no corregirla en el precursor sin alcance.
5. **Ensayar el clon desde la copia local.** Con alcance autorizado, usar una ubicación temporal libre distinta de `vcx/blends/`; no hace falta vaciar esta última para ensayar. Mantener un origen local de transferencia separado del remoto GitHub; no cambiar simplemente la URL de referencias que representan al precursor como si reflejaran GitHub. No usar `--shared` ni otros objetos prestados; elegir copia autónoma de objetos. Un clon normal no reconstruye todas las ramas locales ni sus upstreams: registrar y verificar el mapeo de referencias requeridas por nombre y SHA, preservar sus objetos alcanzables y reconstruir ramas/upstreams solo conforme al plan. Comprobar integridad y estabilidad del corte frente a cambios concurrentes del origen. La ausencia de stashes no sustituye inventariar el estado no versionado. Configuración, hooks y automatizaciones requieren tratamiento explícito; no activarlos por copiar archivos. No publicar ramas ni iniciar trenes por esta transferencia.
6. **Transferir documentos y congelar su fuente.** Preparar el destino en una ubicación distinta de la carpeta documental rastreada por la raíz, también para Cellar y Brix, de modo que editar el destino no modifique la fuente congelada. Antes de copiar los documentos de un producto a su repositorio o rama, fijar la revisión y hashes de la versión fuente actual; incluir antes cualquier cambio pendiente que deba viajar. Al copiarlos, congelar esa versión rastreada por la raíz como evidencia de transición: toda edición posterior se hace únicamente en el repositorio o rama destino. Aplicar la misma regla a Cellar y Brix. Registrar origen, destino, hashes y revisiones de incorporación, incluso si la integración tarda días. Si la fuente congelada cambia, detener su retirada y conciliar la divergencia; no descartarla ni imponer la copia más reciente por fecha.
7. **Incorporar e integrar bajo el gobierno de cada producto.** En Blends, usar una rama del clon nuevo y el proceso vigente de alcances, hooks, `queue` y trenes. La autoridad futura debe permitir ejecutar ese proceso en su ámbito y mantener un solo escritor por superficie compartida; mientras el clon nuevo esté en ensayo, evitar activar automatizaciones duplicadas y coordinar cualquier uso de la cola con el operador vigente. Importar los principios adoptados en la cadena efectiva de instrucciones y fusionar AGENTS, según la [preparación de principios](#preparación-de-enlaces-y-principios); resolver enlaces y contratos sin copiar políticas enteras de raíz. Antes de integrar comprobar permisos, carga de instrucciones y lectura aislada. La mera presencia de documentos en una rama no permite sustituir la carpeta: exigir incorporación integrada y aceptada, con revisión concreta. Para Cellar y Brix, verificar la línea base correspondiente a su estrategia aprobada.
8. **Preparar el corte operativo de Blends.** Antes del cambio de copia canónica, demostrar con el inventario que la copia vieja no puede seguir operando simultáneamente: no dispone de escritura o sus automatizaciones están desactivadas y no quedan sesiones/escritores con ejecución pendiente. No basta con prometer que nadie la usará ni con ver un scheduler detenido mientras otra sesión actúa. Toda suspensión de automatizaciones o cambio de permisos del precursor necesita autorización separada; no levantar su protección global. Si no puede verificarse un único escritor autorizado, mantener pendiente el corte. La gestión de credenciales y jobs del clon nuevo debe impedir que la transferencia reactive escritores por accidente. Con los escritores del origen detenidos, volver a cotejar las referencias requeridas, especialmente `queue`, y conciliar los cambios producidos desde el clon inicial durante la incorporación. Registrar el corte final por nombre y SHA sin sobrescribir la integración aceptada ni descartar trabajo posterior; si hay divergencia no resuelta, no cambiar la canonicidad.
9. **Retirar seguimiento por producto sin borrar el contenido.** Solo después de confirmar su integración, cotejar los hashes de la fuente congelada con el registro de transferencia y comprobar que las revisiones destino contienen los cambios aceptados. El hash final de un AGENTS fusionado puede diferir legítimamente: conservar la correspondencia y el diff revisado, sin exigir identidad entre versiones distintas. Retirar del índice de raíz los documentos del producto sin borrarlos del disco y aplicar su exclusión; revisar y registrar la transición. `.gitignore` no deja de rastrear archivos por sí sola. No retirar Cellar o Brix porque Blends haya completado su incorporación. No registrar repositorios embebidos como gitlinks.
10. **Cambiar la ubicación canónica de Blends.** Respetar este orden: incorporación integrada verificada → retirada del índice raíz y exclusión → apartar la carpeta documental actual a una ubicación autorizada sin borrarla → colocar el clon nuevo en `vcx/blends/` → comprobar que la raíz lo ignora, no lo rastrea ni contiene gitlinks o una entrada de submódulo. Mantener apartada la versión congelada hasta el cierre. Comprobar también rutas operativas afectadas por el traslado del clon ensayado; la disposición de gobierno de las copias de trabajo debe respetar el proceso conservado. Si Cellar o Brix se prepararon en otra ubicación, aplicar el mismo orden de conservación de la carpeta fuente y colocación de destino, con las verificaciones que correspondan a su propia estrategia; no omitir esa colocación al retirar su seguimiento en raíz. VCX-D030, ratificada el 2026-11-01, adelanta la colocación del clon de autoría antes del corte de escritores del paso 8, manteniendo el precursor como único operador; por VCX-D032 ese clon es la instancia y, por VCX-D036, se coloca en `vcx/cellars/`, no en `vcx/blends/`. Las menciones de esta secuencia a Blends como continuación del precursor se leen con la enmienda de VCX-D026; la creación del `blends` público sigue la [secuencia de visibilidad](../superpowers/specs/2026-11-01-public-visibility-design.md#secuencia). Reescribir los pasos 3 a 11 con esa partición queda pendiente para cuando se autorice su ejecución.
11. **Verificar y declarar canonicidad.** Registrar la revisión integrada, referencias transferidas, ubicación elegida, comprobaciones de carga, estado de los escritores y autoridad que acepta la transición. Activar únicamente las operaciones autorizadas del clon nuevo, con el viejo inactivo para escritura concurrente. La raíz conserva acuerdos e historia base, mientras los productos conservan sus fuentes editables. Verificar los enlaces de la raíz hacia productos como navegación del workspace completo, marcados como tales y no como rotos, y la lectura aislada de raíz y productos; un enlace local válido no se presenta como accesible desde cualquier clon.

### Recuperación y límites

Si falla la colocación del clon en el paso 10, mantener el corte operativo y devolver la carpeta documental apartada a su ubicación, sin borrar el clon temporal o sobrescribir trabajo. La exclusión de raíz y su retirada del índice no se revierten automáticamente: registrar si se conserva esa condición o, con autorización, se restaura el seguimiento desde la revisión conocida. El commit base permite recuperar documentos; no habilita reactivar los escritores viejos. La canonicidad anterior solo se restablece mediante un retorno controlado y sin dos escritores activos.

Si aparece una divergencia de referencias, objetos faltantes, cambios en la fuente congelada o incorporación no aceptada, detener la transición del producto afectado y conservar ambas evidencias, dejando una sola fuente de edición autorizada. No ejecutar borrados, resets o cambios de historia por conveniencia.

El commit base protege documentación de VCX. La transferencia verificada de referencias y el tratamiento del estado no versionado protegen el estado del precursor: son garantías distintas. No hay un respaldo fuera de la máquina implícito en ninguna de ellas. La retirada definitiva del clon viejo, la extracción de Brix, la separación de datos de portfolio y los cambios de gobierno son alcances posteriores.

## Criterios de salida y decisiones pendientes

La reformulación deja elegidos commit base, continuidad histórica de Blends, gobierno vigente, clon desde copia local, congelamiento y orden del corte. Para ejecutar faltan el alcance autorizado, ubicaciones temporales y de recuperación, inventario actualizado de referencias y escritores, comprobaciones y autoridad de integración/canonicidad. La ejecución autorizada abarcó únicamente el commit base raíz, `f47c71f`, cuya recuperación quedó verificada el 2026-11-01. Los pasos de producto y de cambio de canonicidad siguen sin ejecutar.

La estrategia de historial de Brix sigue abierta y no bloquea Cellar o Blends. También siguen pendientes la ubicación de instancias y los cambios de gobierno o separación de datos heredados. La independencia se acepta solo con las comprobaciones de [interoperabilidad](interoperability.md#preparación-de-productos-independientes), no por completar este mapa. Los acuerdos y cambios de autoridad se registran únicamente en el [registro de decisiones](../decisions/README.md).
