# Modelo de productos de VCX: método en Blends, conducción en Cellar

Fecha: 2026-10-31. Estado: modelo conceptual acordado por el usuario en el chat con Claude del 2026-10-31 y registrado como VCX-D029 en el [registro de decisiones](../../decisions/README.md). La aplicación a las fuentes documentales está identificada más abajo, pero no se ejecutó: requiere un alcance propio, separado del commit base autorizado. Este documento no modifica el precursor, no crea instancias, comandos ni código, y no concede autoridad a ningún agente. La revisión externa trasladada por el usuario el 2026-11-01 se incorporó en «Contraste de la revisión recibida»; el [plan de aplicación](../plans/2026-11-01-product-model-application.md) dimensiona los cambios documentales, todavía sin autorizar.

Etiquetas: [U] definición o respuesta del usuario; [H] hecho documental con referencia; [I] interpretación del asistente; [P] propuesta del asistente pendiente de revisión.

## Acuerdos y alcance

El usuario pidió validar en solo lectura su definición conceptual de VCX y sus productos antes de modificar la documentación. La validación contrastó esas definiciones con [README](../../../README.md), [AGENTS](../../../AGENTS.md), [visión](../../vision.md), [arquitectura](../../architecture/overview.md), [matriz de responsabilidades](../../architecture/responsibility-matrix.md), [interoperabilidad](../../architecture/interoperability.md), las decisiones VCX-D011, D017 y D020 a D028, los README de [Blends](../../../blends/README.md), [Cellar](https://github.com/denispaiva/cellar/blob/main/README.md), [instancias](../../../solera/README.md) y [Brix](../../../brix/README.md), el [ingreso de ideas](../../../blends/docs/idea-intake.md), el [recorrido de idea a proyecto](../../../blends/docs/idea-to-project.md), el [modelo de iniciativa](https://github.com/denispaiva/cellar/blob/main/docs/initiative-model.md) y la [spec de maduración de ideas](2026-10-31-idea-maturation-design.md). No se leyó el precursor `../blends/`.

Siete preguntas ordenadas por impacto se resolvieron de a una. Respuestas literales del usuario, en orden: «Cellar conduce», «Todo el proyecto», «Responsable del portfolio», «Raíz: principios», «Repos propios», «Confirmo», «Solo marca». La autorización para escribir este documento y registrar la decisión fue «Aprobar, escribir spec».

Las respuestas fijan el modelo conceptual. No aprueban cada cambio documental derivado, que se planifica y autoriza aparte, ni cambian las reglas vigentes del precursor, que siguen sujetas a conciliación por VCX-D011 bajo el gobierno conservado por VCX-D026.

## Definiciones expresadas por el usuario

Transcripción de las definiciones de partida, sin reformular.

1. VCX / VibeOS
- «vcx = VibeOS, Vibe Coding for X projects».
- Es el nombre del conjunto de productos donde se desarrolla el ciclo de vida de ideas y proyectos.
- VCX no se convertirá en un producto propio.

2. Blends
- Es el wizard para que las actividades del conjunto sucedan.
- Es la parte blanda, responsable de coordinar actividades e hitos.
- Cumple la función de Project Manager.
- Provee lógica y organización.
- Los principios, las metodologías y las directrices son su responsabilidad.

3. Cellar
- Recibe una idea graduada y conduce su desarrollo como proyecto.
- Ese desarrollo puede realizarse mediante un Minimum Viable Product o Producto Mínimo Viable, pero no es obligatorio.
- Se concibe como un grupo de Product Owners de productos.
- Se nutre de las metodologías y principios que gobierna Blends.
- Esta definición supera la descripción anterior que lo reducía principalmente a organizar y custodiar información. No está resuelto todavía cómo se redistribuye esa responsabilidad de custodia.

4. Brix
- Es el kernel técnico.
- Allí viven los desarrollos de ingeniería, las integraciones y las habilidades técnicas.
- Nutre al resto con capacidades para diseño, ingeniería, arquitectura, FinOps, Git y otras necesidades técnicas.
- Sigue sin resolverse si contiene también el código específico de cada producto o si provee capacidades reutilizables mientras cada producto conserva su implementación en su propio repositorio.

## Modelo consolidado

**VCX / VibeOS.** [U] Nombre y marca del conjunto de productos donde se desarrolla el ciclo de vida de ideas y proyectos: «Vibe Coding for X projects». VibeOS es solo marca; no es producto, servicio central ni dependencia ejecutable. [I] Conforme a VCX-D024 y VCX-D025; cambia el título y la mención de marca, nada más.

**Blends.** [U] Wizard para que las actividades sucedan; parte blanda; función de Project Manager (PM); provee lógica y organización. Es dueño del método: metodologías y directrices de ingreso, maduración, gate, preparación del contexto de proyecto y conducción de proyectos. Aplica los principios comunes de VCX, que siguen en la raíz. Coordina actividades e hitos del ciclo de idea hasta la graduación. [I] Blends no conduce proyectos; define cómo se conducen. «Wizard» describe una función conceptual de guía; no afirma un asistente implementado.

**Cellar, producto.** [U] Define estructura y mecanismos para dos responsabilidades: custodiar y conducir. Recibe la idea graduada y conduce todo el proyecto, es decir decisión de producto, planificación, entrega y evolución, bajo el método que define Blends. El MVP es una vía de validación recomendada, no obligatoria, como propone la [spec de maduración](2026-10-31-idea-maturation-design.md#mvp-recomendado-sin-obligatoriedad). Es la pieza donde actúan los Product Owners (PO) de los productos. [P] Dos responsabilidades distinguibles, no dos módulos: la custodia, recuperable sin ejecutar nada, que conserva la prueba de independencia vigente; y la conducción, que es nueva. Separarlas en paquetes, servicios o módulos no tiene necesidad demostrada; la independencia se comprobará después mediante comportamientos concretos.

**Cellar, instancia.** [U] Un portfolio concreto. Custodia íntegra en todas las etapas, desde la propuesta en preparación hasta el proyecto vivo; Blends y Brix no guardan otra copia editable. Registra dónde vive el código de cada proyecto, sin alojarlo. [I] Custodiar no es admitir: la preparación previa al ingreso se conserva fuera del portfolio activo hasta la confirmación humana de VCX-D017, y puede iniciarse sin haber elegido todavía la instancia de destino, como ya define el [ingreso](../../../blends/docs/idea-intake.md#custodia-previa-al-registro).

**Brix.** [U] Núcleo de capacidades técnicas reutilizables: diseño, ingeniería, arquitectura, FinOps, Git y otras necesidades técnicas. Las integraciones y habilidades viven ahí como capacidades. El código específico de cada producto y de cada proyecto vive en su propio repositorio. [P] Usar «núcleo de capacidades», ya escrito en la [arquitectura](../../architecture/overview.md#fronteras-y-contexto), en lugar de «kernel», porque «Blends Kernel» nombra hoy el núcleo de gobierno del precursor y esa denominación no se reasigna.

**Autoridad humana.** [U] Antes de graduar decide el responsable del portfolio, dueño de la instancia de Cellar. [I] Puede delegar con autoridad, objeto y alcance explícitos, conforme a VCX-P7. Al graduar se asigna el PO del proyecto en la misma decisión. El responsable del portfolio conserva su autoridad sobre el portfolio; el PO asume la del proyecto. Son dos asignaciones que coexisten, no una sustitución. Ninguna pieza es autoridad: Blends propone y verifica, Brix calcula y asesora, Cellar organiza la decisión y la conserva. Una función de PM o de PO no concede autoridad a un agente.

## Preguntas resueltas y alternativas descartadas

| Pregunta | Respuesta [U] | Alternativa descartada y su costo |
|---|---|---|
| ¿«Grupo de PO» nombra a Cellar como pieza o a personas registradas en Cellar? | Cellar conduce, como pieza | Personas en Cellar: habría dejado la definición actual casi intacta, pero no representaba la intención del usuario |
| Tras graduar, ¿Cellar conduce solo la decisión de producto o todo el proyecto? | Todo el proyecto | Decisión de producto, recomendada por el asistente: mantenía a Blends con planificación y entrega; el usuario eligió concentrar la conducción en Cellar |
| ¿Quién decide sobre una idea antes de graduarse? | Responsable del portfolio | PO por idea, lo escrito hoy: obliga a asignar PO a ideas que quizá no gradúen. Intervención de Cellar desde el ingreso: contradice «recibe una idea graduada» |
| ¿Dónde viven los principios? | Raíz: principios; Blends dueño del método | Blends dueño de todo: revertía VCX-D022 y VCX-D025 y hacía a Brix y Cellar dependientes de Blends |
| ¿Dónde vive el código de productos y proyectos? | Repos propios; Brix provee capacidades | Brix aloja el código: reabría VCX-D025 y convertía a Brix en concentrador. Dejarlo abierto: suspendía la fila de código de la matriz |
| ¿La custodia queda íntegra en la instancia de Cellar? | Confirmo | Custodia en Blends: rompía la prueba de Cellar legible sin ejecutar. Custodia en Brix: rompía «no presupone un Cellar» |
| ¿VibeOS es solo marca? | Solo marca | Algo que corre: reabría VCX-D024 y creaba la dependencia central que AGENTS prohíbe |

## Transferencia de autoridad al graduar

[H] El [modelo de iniciativa](https://github.com/denispaiva/cellar/blob/main/docs/initiative-model.md#información-mínima-y-aparición-progresiva) define `ownerRef` como autoridad responsable del propósito y decisiones, y deja fuera solo los cambios de propietario entre Cellars. [I] Mientras la iniciativa es idea, `ownerRef` referencia al responsable del portfolio. [P] Al graduar no se sobrescribe: la decisión de graduar agrega una referencia propia al PO del proyecto, por ejemplo `productOwnerRef`, con la decisión que lo asigna, y ambas asignaciones se conservan como historia. Desde entonces el PO responde por las decisiones del proyecto; el responsable del portfolio conserva las del portfolio: prioridades entre proyectos, presupuesto del portfolio y excepciones de su ámbito. Qué decisiones concretas pasan a cada uno se precisa al diseñar el traspaso. La identidad de la iniciativa no cambia. Si la graduación no asigna PO, el proyecto no tiene autoridad y la preparación queda pendiente, conforme al tratamiento de interrupciones del [recorrido](../../../blends/docs/idea-to-project.md#cambios-e-interrupciones).

## Recorrido de referencia: «Mapa de talleres de cerámica del barrio»

Ejemplo ficticio. Una vecina propone un directorio de talleres de cerámica con horarios.

| Paso | Quién interviene | Fuente actual | Qué cambia con este modelo |
|---|---|---|---|
| Propuesta | Brix prepara documento y preguntas asesinas; Blends conduce la revisión humana y coordina el consejo; el responsable del portfolio confirma el ingreso | [Ingreso](../../../blends/docs/idea-intake.md), VCX-D017 | La autoridad que confirma se nombra: responsable del portfolio |
| Registro, arquitectura de referencia y FinOps | La instancia registra `registered`; Brix propone el modelo; Blends coordina FinOps; el responsable del portfolio autoriza el presupuesto de exploración | [Recorrido, pasos 1 y 1.1](../../../blends/docs/idea-to-project.md#secuencia) | «PO» pasa a responsable del portfolio |
| Exploración y maduración | Blends aplica el método de preguntas asesinas y semáforo; la instancia conserva evidencia; el responsable del portfolio confirma cuáles bloquean | [Spec de maduración](2026-10-31-idea-maturation-design.md), propuesta sin aprobar | Sin cambio conceptual; la autoridad del gate se nombra |
| Gate | Decisión humana: graduar, diferir o archivar | [Recorrido, paso 4](../../../blends/docs/idea-to-project.md#gate-y-alternativas) | La graduación asigna el PO del proyecto |
| Graduación y conducción | Blends prepara el contexto y lo entrega; Cellar conduce el proyecto con la vía de validación elegida, por ejemplo un listado estático con tres talleres como MVP | [Recorrido, paso 5 y siguiente límite](../../../blends/docs/idea-to-project.md#siguiente-límite) | Llena el vacío: hoy el primer plan de trabajo «pertenece a recorridos posteriores» sin dueño. El traspaso concreto, quién prepara, cuándo recibe Cellar, cómo acepta el PO y qué pasa si falla, está pendiente de diseño |
| Evolución | Cellar conduce roadmap, backlog, entrega y decisiones del proyecto bajo el método de Blends; la instancia custodia todo | [Matriz](../../architecture/responsibility-matrix.md) | Las filas posteriores a la graduación pasan de Blends a Cellar |

## Contraste con la documentación actual

- **PO ya es un rol humano por iniciativa.** [H] La RACI de la [matriz](../../architecture/responsibility-matrix.md#4-matriz-raci-humana-propuesta) asigna «PO de la iniciativa» como A en misión, roadmap y presupuesto; el [recorrido](../../../blends/docs/idea-to-project.md#alcance-y-responsabilidades) dice que el PO competente decide graduar. [U] Cellar es la pieza donde actúan los PO y recibe la idea graduada. Se resuelve partiendo el A por tramo: responsable del portfolio en ideas, PO en proyectos.
- **Principios.** [H] [AGENTS](../../../AGENTS.md#principios-transversales-de-vcx): los contextos locales los incorporan por referencia, sin versiones paralelas; VCX-D025 exige adoptarlos con versión declarada. [U] Resuelto: los principios siguen en la raíz; Blends es dueño de metodologías y directrices.
- **Cellar pasivo.** [H] Invariante 2: «Blends coordina; Brix ejecuta capacidades; Cellar organiza y custodia. Ninguna pieza absorbe silenciosamente las otras». Invariante 3: Cellar conserva información legible sin ejecutar Blends o Brix. La misión de [Cellar](https://github.com/denispaiva/cellar/blob/main/README.md#misión) y la línea del [README](../../../README.md#cómo-se-organiza) dicen lo mismo. [U] Cellar conduce. Ambos invariantes, la misión y la línea deben reescribirse; la parte pasiva de Cellar conserva el invariante 3.
- **Kernel.** [H] [Arquitectura](../../architecture/overview.md#fronteras-y-contexto): «Blends Kernel» pertenece al núcleo de gobierno del sistema existente y no se reasigna. [U] Brix es el kernel técnico. Colisión de nombre, no de concepto.
- **Código.** [H] [Brix](../../../brix/README.md): los drivers de backend pertenecen al consumidor; la matriz deja la ubicación canónica del código en la instancia; VCX-D025 fija repositorios independientes. [U] Resuelto en el mismo sentido: repositorios propios.
- **MVP obligatorio.** [H] El paso 3 del recorrido pide «hipótesis de MVP» y `definitionRef` exige MVP. [U] No obligatorio. La spec de maduración ya lo lista como aplicación pendiente; no es contradicción nueva.
- **Git y diseño.** [H] El alcance conceptual de Brix no los lista. [U] Se agregan como capacidades declaradas, no implementadas. Vacío, no contradicción.
- **Precursor.** [H] [Blends](../../../blends/README.md#fuentes-de-trabajo-y-dependencias): el seguimiento operativo existente vive en el repositorio de Blends, con `.roadmap.json` y la rama `queue`. [I] Mover la conducción de proyectos a Cellar es un cambio material del gobierno del precursor; se escribe como objetivo de VCX y requiere conciliación por VCX-D011 antes de regir allí.

## Aplicación documental después de autorizar el alcance

Dimensiona el trabajo; no lo autoriza. Debe ejecutarse en un commit posterior al commit base documental, con alcance propio, sin mezclarse con los cambios ya autorizados por el [alcance del commit base](../plans/2026-10-31-root-baseline-scope.md).

| Fuente editable | Cambio previsto |
|---|---|
| [Matriz de responsabilidades](../../architecture/responsibility-matrix.md) | Partir por tramo idea y proyecto las filas de proceso, roadmap y backlog, decisiones y sesiones, FinOps y presentación; RACI con responsable del portfolio como A en ideas y PO en proyectos; reescribir invariantes 2 y 3 |
| [README](../../../README.md) y [AGENTS](../../../AGENTS.md) | Título con VibeOS como marca; reemplazar «Blends conduce el trabajo; Brix aporta capacidades e instrumentos; Cellar organiza y custodia»; principios sin cambio |
| [Cellar](https://github.com/denispaiva/cellar/blob/main/README.md), [instancias](../../../solera/README.md) y [modelo de iniciativa](https://github.com/denispaiva/cellar/blob/main/docs/initiative-model.md) | Misión con custodia y conducción; `ownerRef` cambia al graduar; referencias de conducción del proyecto; definición sin MVP obligatorio |
| [Blends](../../../blends/README.md), [recorrido](../../../blends/docs/idea-to-project.md), [ingreso](../../../blends/docs/idea-intake.md) y [FinOps](../../../blends/docs/architecture-and-finops.md) | Misión como dueño del método más tramo de idea; «PO competente» pasa a responsable del portfolio; el paso 5 entrega el proyecto a Cellar con PO asignado; «siguiente límite» apunta a la conducción en Cellar |
| [Brix](../../../brix/README.md) | Alcance conceptual suma Git y diseño; «núcleo de capacidades» en lugar de kernel |
| [Visión](../../vision.md) y [arquitectura](../../architecture/overview.md) | Fronteras actualizadas; nueva señal de independencia: un Cellar conduce un proyecto sin ejecutar Blends |
| [Interoperabilidad](../../architecture/interoperability.md) | Nuevo contrato: operaciones de conducción de proyecto, dueño Cellar; hoy no existe |
| [Matriz de tooling](../../architecture/tooling-matrix.md) | Las fases posteriores a la graduación pasan de Blends a Cellar; revisar filas y estados |
| [Spec de maduración](2026-10-31-idea-maturation-design.md) | Coherente; verificar que «autoridad humana del gate» se lea como responsable del portfolio |
| [Registro de decisiones](../../decisions/README.md) | VCX-D029 ya registrada; al aplicar, anotar fecha, autoridad y archivos cambiados |

La aplicación se considerará coherente cuando el recorrido de referencia pueda expresarse sin contradicción en todas las fuentes, se mantengan fuentes únicas y decisiones separadas, y ninguna pieza quede con dos procesos de conducción. Se comprobarán enlaces y procedencia; no se agregan pruebas que solo reproduzcan el texto.

## Pendientes

- **Conciliación con el precursor, VCX-D011.** Blends Kernel conduce proyectos hoy; este modelo no rige allí hasta conciliar.
- **Frontera entre método y conducción.** Blends define cómo se conduce; Cellar conduce. Escribirla con ejemplos para evitar dos procesos.
- **Traspaso al graduar.** Quién prepara el contexto de proyecto, cuándo lo recibe Cellar, cómo acepta el PO su responsabilidad, qué decisiones conserva el responsable del portfolio y qué ocurre si la preparación falla. El recorrido actual solo cubre la preparación reanudable; cambiar el nombre de la autoridad no lo resuelve.
- **Cambio del gate.** La [spec de maduración](2026-10-31-idea-maturation-design.md#cambio-propuesto-del-gate-y-vigencia) sigue sin aprobar y sin conciliar; VCX-D029 no la aprueba indirectamente.
- **Contrato de conducción.** Fila nueva en interoperabilidad y su dueño.
- **Delegación del responsable del portfolio.** Parámetro del perfil de gobierno, pendiente de definir.
- **Nombre «kernel».** Reservado hasta la conciliación; se usa «núcleo de capacidades».
- **Prueba de independencia nueva.** «Un Cellar conduce un proyecto sin ejecutar Blends» se demuestra al implementar, no ahora.
- **Candidato de nombre.** VibeOS como marca se incorpora al [criterio de nombres](../../naming.md) cuando se aplique el alcance; el glosario no asigna identidades.

## Contraste de la revisión recibida

Revisión trasladada por el usuario el 2026-11-01, pegada en el chat con Claude, de otro asistente que leyó el repositorio. Nota 8 de 10 orientativa, con descuentos por traspaso de autoridad impreciso y por subestimar los cambios del diseño de graduación. Confirma la distribución central y pide cinco correcciones; las cinco se incorporaron:

1. Asignar PO no sustituye `ownerRef`; las dos asignaciones coexisten y se conservan. Reescrito en «Autoridad humana» y «Transferencia de autoridad al graduar».
2. Custodiar una propuesta no es admitirla; la preparación sigue fuera del portfolio activo y puede no tener instancia elegida. Agregado en «Cellar, instancia».
3. La división pasiva/activa es una distinción de responsabilidades, no dos módulos. Reescrito en «Cellar, producto».
4. El traspaso al graduar requiere diseño propio y el cambio del gate sigue sin aprobar. Agregados como pendientes y en el recorrido de referencia.
5. Procedencia de las siete respuestas. Se dieron directamente en este chat con Claude, el 2026-10-31, y el registro nombra ese chat como fuente. El repositorio no conserva la transcripción, así que para cualquier otro lector son respuestas reportadas; la fila VCX-D029 ahora lo dice.

Dos hechos que la revisión afirma se contrastaron con el árbol de trabajo del 2026-11-01: el commit base `f47c71f` existe y hay cambios posteriores sin commitear, correcto; «VCX-D029 todavía no está registrado» es cierto para `HEAD` y falso para el árbol de trabajo, donde la fila existe sin commitear. La revisión leyó la revisión commiteada.

## Nota orientativa

8 de 10, según VCX-P2; no es aprobación ni medición objetiva. Subió desde 6 en la validación inicial porque PO, principios y custodia quedaron resueltos sin piezas ni dependencias nuevas. Descuentos: un punto porque Cellar pasa a ser una segunda pieza activa y el traspaso al graduar aún no está diseñado; un punto por el choque con el precursor que VCX-D011 todavía no concilia y por el cambio del gate sin aprobar. La revisión externa coincide en la nota y en los descuentos. Sin sobrediseño ni dependencias innecesarias identificadas.

## Verificación de esta entrega

El 2026-10-31 se escribieron únicamente este documento y la fila VCX-D029 del registro. El 2026-11-01 se incorporó la revisión externa en este documento y en esa fila, y se escribió el plan de aplicación. No se modificó ninguna otra fuente, el precursor ni el estado de Git. Los enlaces relativos de este documento se comprobaron contra el árbol del 2026-11-01. El modelo conceptual está acordado; cada cambio de la tabla anterior sigue siendo propuesta hasta su autorización.
