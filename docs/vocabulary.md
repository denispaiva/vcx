# Vocabulario de VCX

Fecha: 2026-11-01. Estado: vocabulario de trabajo pedido por el usuario el 2026-11-01 para evitar interpretaciones equivocadas. No crea definiciones nuevas: resume las de sus fuentes y las enlaza. Si una entrada y su fuente difieren, rige la fuente y esta entrada se corrige.

No confundir con el [banco de candidatos de nombres](references/enology-glossary-source.md), que es material sin curar para elegir nombres y no define conceptos.

Cada entrada indica su estado:

- **Vigente:** acordado y aplicado en las fuentes de VCX.
- **D029:** acordado en VCX-D029; las fuentes todavía no se actualizaron, según el [plan de aplicación](superpowers/plans/2026-11-01-product-model-application.md).
- **Propuesto:** pendiente de aprobación.
- **Precursor:** describe el sistema existente en `../blends/`, que sigue rigiendo allí hasta conciliar por VCX-D011.

## Organización

| Término | Qué es | Qué no es | Estado y fuente |
|---|---|---|---|
| **VCX · VibeOS** | Raíz organizativa y marca del conjunto de productos: «Vibe Coding for X projects» | Un producto, servicio central o dependencia ejecutable | Vigente como raíz (VCX-D024); VibeOS como marca, D029 |
| **Tintum** | Dominio web y marca comercial paraguas, `tintum.app`: VCX y todo lo que vive debajo forman parte de ella; firma `powered by tintum` | Un producto, otro nombre de VCX o VibeOS, ni el grupo de proyectos de vino (Assemblage) | Vigente (VCX-D061; [recursos](../assets/tintum/README.md)) |
| **Producto comercial** | Producto de un proyecto que se ofrece al público bajo Tintum y muestra `powered by tintum`; hoy Teyst | Blends, Brix o Cellar | Vigente (VCX-D061; [lista](../assets/tintum/README.md#productos-comerciales)) |
| **Producto** | Una de las tres piezas reutilizables: Blends, Brix o Cellar. Se versiona, distribuye y evoluciona por separado, en su propio repositorio | Lo que construye un proyecto; para eso ver *producto de un proyecto* | Vigente ([arquitectura](architecture/overview.md#dos-grupos-y-tres-productos), VCX-D025) |
| **Producto de un proyecto** | Lo que un proyecto construye y entrega a sus usuarios, decidido por su PO | Blends, Brix o Cellar | D029 ([modelo de productos](superpowers/specs/2026-10-31-product-model-design.md)) |
| **Cellar · producto** | Define la estructura y los mecanismos para custodiar y, desde D029, conducir | Un portfolio concreto | Vigente; conducción, D029 |
| **Cellar · instancia** | Un portfolio concreto: conserva sus iniciativas, configuración, decisiones y memoria | El producto Cellar ni una carpeta cualquiera | Vigente ([modelo de iniciativa](https://github.com/denispaiva/cellar/blob/main/docs/initiative-model.md#qué-corresponde-a-cada-nivel)) |
| **Portfolio** | El conjunto de iniciativas que custodia una instancia de Cellar | Todo VCX | Vigente |
| **Iniciativa** | Una idea o un proyecto, con una sola identidad durante todo su ciclo | Una propuesta todavía no admitida | Vigente ([modelo de iniciativa](https://github.com/denispaiva/cellar/blob/main/docs/initiative-model.md#estados-y-relaciones)) |
| **Propuesta** | Lo que se prepara antes del ingreso; queda fuera del portfolio activo hasta la confirmación humana | Una idea registrada | Vigente (VCX-D017, [ingreso](https://github.com/denispaiva/blends/blob/main/docs/idea-intake.md)) |
| **Idea** | Iniciativa registrada que todavía no se graduó | Un proyecto | Vigente |
| **Proyecto** | Iniciativa graduada; conserva la misma identidad que tenía como idea | Una iniciativa nueva | Vigente; conducción por Cellar, D029 |
| **Graduar** | Decisión humana del gate que convierte una idea en proyecto y, desde D029, asigna su PO | Un cambio de estado automático | Vigente; asignación del PO, D029 |

## Responsabilidades

| Término | Qué es | Qué no es | Estado y fuente |
|---|---|---|---|
| **Método** | Reglas que valen para cualquier proyecto de cualquier Cellar: etapas, compuertas, criterios de evidencia, plantillas de proceso. Dueño: Blends | Decidir sobre un proyecto concreto | D029; definición detallada, propuesto |
| **Conducción** | Acciones y decisiones sobre un proyecto concreto después de graduar: planificar, priorizar, entregar, evolucionar. Dueño: Cellar, con el PO como autoridad | Redefinir las reglas del método | D029; definición detallada, propuesto |
| **Custodia** | Conservar los datos de las iniciativas, legibles y recuperables sin ejecutar Blends ni Brix. Dueño: la instancia de Cellar | Admitir una propuesta ni conducir un proyecto | Vigente (invariante 3 de la [matriz](architecture/responsibility-matrix.md#5-invariantes-de-diseño)) |
| **Tramo de idea** | Desde la propuesta hasta graduar. Coordina Blends, custodia la instancia y decide el responsable del portfolio | El tramo de proyecto | D029 |
| **Capacidad** | Algo que un producto sabe hacer, con entradas, permisos y resultados verificables. Las técnicas y reutilizables son de Brix | Un producto, una funcionalidad del roadmap ni una unidad de trabajo | Vigente ([Brix](https://github.com/denispaiva/brix/blob/main/README.md)); reparto, D029 |
| **Dueño** | La pieza que mantiene una definición o un dato canónico | Una autoridad humana ni un permiso de ejecución | Vigente ([matriz](architecture/responsibility-matrix.md#2-matriz-de-responsabilidades-técnicas-propuesta)) |
| **Contrato** | Interfaz pública por la que un producto ofrece datos u operaciones a otro, con dueño y versión | Leer archivos o ramas internas de otro producto | Vigente ([interoperabilidad](architecture/interoperability.md)) |

Prueba rápida, propuesta en el plan de aplicación: si la frase vale para todos los proyectos, es **método**; si nombra a un proyecto, es **conducción**; si describe cómo se calcula o integra algo, es **capacidad**.

## Autoridad

| Término | Qué es | Qué no es | Estado y fuente |
|---|---|---|---|
| **Responsable del portfolio** | Persona dueña de una instancia de Cellar. Decide sobre las ideas y conserva las decisiones del portfolio después de graduar | El PO de cada proyecto | D029 |
| **PO del proyecto** | Persona asignada al graduar. Decide sobre su proyecto: prioridades, alcance y aceptación | Una pieza de software ni un agente | D029 |
| **Autorización** | Aprobación con autoridad, objeto, revisión y alcance identificados | Una recomendación, un reporte favorable ni el silencio | Vigente (VCX-P7 en [AGENTS](../AGENTS.md#principios-transversales-de-vcx)) |

Ninguna pieza es autoridad: Blends propone y verifica, Brix calcula y asesora, Cellar organiza y conserva la decisión. Un agente que cumple una función de PM o de PO no adquiere su autoridad.

## Piezas ejecutables

| Término | Qué es | Ejemplo |
|---|---|---|
| **Comando** | Punto de entrada que una persona o un agente invoca | `npm run backlog`, `/idea` |
| **Subcomando** | Una operación concreta dentro de un comando | `board`, `add`, `triage`, `promote` |
| **Vista** | Lo que se presenta a una persona a partir de los datos. Es derivada: no reemplaza la fuente | La vista Backlog, `roadmap/backlog.html`, en una rama sin integrar del precursor |
| **Snapshot** | Copia fechada de datos para alimentar una vista; se regenera y no se edita | `roadmap/backlog-snapshot.js`, en la misma rama |

«Feature» no se usa en la documentación: es ambiguo entre una capacidad que existe y una unidad de trabajo del roadmap. Se dice **capacidad** para lo primero y **épica** o **tarea** para lo segundo.

## Trabajo y seguimiento

| Término | Qué es | Qué no es | Estado y fuente |
|---|---|---|---|
| **Roadmap** | Plan de trabajo de un producto o de un proyecto: épicas, tareas, sprints y entregables | El backlog | Vigente; en el precursor, un `.roadmap.json` por proyecto |
| **Épica** | Agrupación de tareas con un objetivo común dentro de un roadmap | Un producto ni una capacidad | Precursor |
| **Tarea** | Unidad de trabajo de un roadmap, asignada a un sprint e identificada como `<proyecto>/T-nn` | Un pedido del backlog | Precursor |
| **Sprint** | Período de 14 días con ID `SP-AAAA-Www` | Una fecha de entrega comprometida | Precursor |
| **Backlog** | Pedidos que todavía no son tareas porque nadie les asignó sprint | El roadmap | Precursor (rama `queue`) |
| **Pedido** | Una entrada del backlog, con ID `BL-…`. Pasa por `open`, `triaged` y termina `promoted`, `declined` o `withdrawn` | Una tarea | Precursor |
| **Prioridad confirmada** | P0, P1 o P2 fijada por la autoridad humana en el triage | La prioridad sugerida | Precursor |
| **Prioridad sugerida** | La que propone una sesión o agente; se muestra marcada como sugerida | Una decisión | Precursor |
| **Promover** | Convertir un pedido en tarea de un sprint, por decisión humana | Un paso automático | Precursor |

Hay dos clases de roadmap con el mismo formato. El de **cada producto** (Blends, Brix, Cellar) registra la evolución de sus capacidades y lo decide su responsable. El de **cada proyecto** vive en una instancia de Cellar y lo decide su PO. Una vista como Backlog puede presentar cualquiera de los dos.

## Sistema precursor

| Término | Qué es | Qué no es |
|---|---|---|
| **Precursor** | El sistema existente en `../blends/`, fuente de consulta y de solo lectura salvo excepción registrada | La carpeta `blends/` de VCX, que contiene documentos objetivo |
| **Blends Kernel** | Núcleo de gobierno del precursor; retirado como entidad objetivo por VCX-D045, sigue como nombre histórico | Brix. Por eso «kernel» no se usa para Brix: se dice «núcleo de capacidades» |
| **Tren** | Mecanismo del precursor que integra ramas en `main` | Una regla de VCX |
| **Clon de autoría** | Checkout del repositorio de Blends que se colocaría en `vcx/blends/` para escribir ramas y decisiones; propuesto en VCX-D030, sin ratificar | El operador: no ejecuta `queue`, trenes ni hooks hasta el corte operativo |
| **Operador** | El checkout que ejecuta `queue`, trenes y hooks; hoy `../blends` | Un lugar donde escribir decisiones nuevas |
| **Espejo** | Repositorio separado que recibe una subcarpeta de `blends` exportada con `brix graduate`, sin commits propios; hoy `brix`, `pinot-index` y `teyst-blends` | Una fuente editable; convertirlo en canónico es una decisión de la extracción |
| **Superficie publicable** | Rutas de un repositorio que pueden salir al público, declaradas explícitamente; por defecto, ninguna. Regla del precursor que VCX-D032 adopta para publicar los productos | Todo lo que no tiene secretos: importes, identificadores de facturación y datos de proyectos vivos tampoco se publican |

## Caso de referencia: `board`

`board` es un **subcomando** de la capacidad de backlog, invocado como `npm run backlog -- board`. Genera la **vista** Backlog a partir de un **snapshot**. No es un producto ni una feature, y no gestiona datos: no escribe en la cola ni en los roadmaps. Sí escribe el snapshot derivado y, salvo con `--offline`, actualiza con un fetch la ref remota de `queue`.

Estado verificado el 2026-11-02 en el precursor, solo con lectura: `board` existe únicamente en la rama `feat/framework-backlog-view` (`6510adb9`), creada bajo VCX-D027 y encolada para el tren según la ref local de `queue`, consultada sin fetch. No está en `main` (`f86a2a7d`): allí la capacidad `instrument.backlog` está registrada, pero su comando no ofrece ese subcomando.

| Pregunta | En el precursor, hoy | En el modelo objetivo de D029 |
|---|---|---|
| ¿Dónde está implementado? | En el repositorio de Blends: la capacidad `instrument.backlog`, con dueño `blends`, en `main`; `board`, solo en la rama sin integrar | Sin decidir; depende del contrato de conducción |
| ¿De quién son los datos que lee? | Del repositorio de Blends: rama `queue` y `.roadmap.json` | De la instancia de Cellar, por su contrato |
| La regla de orden: prioridad confirmada, luego sugerida, luego antigüedad | Regla del backlog de Blends | Vale para todos los proyectos: **método**, Blends |
| Mostrar el backlog de un proyecto concreto | Lo hace `board`, en la rama sin integrar | Uso en la **conducción**, Cellar |
| Calcular la proyección a partir de los datos | Lógica de `board`, en la misma rama | Si se reutiliza, **capacidad**, Brix |

Mientras no exista el contrato de Cellar, `board` lee en esa rama la ref de `queue` y `roadmap/data.js` directamente. Es deuda declarada y se resuelve al definir ese contrato.
