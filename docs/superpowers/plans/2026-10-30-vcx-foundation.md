# Plan de fundación documental de VCX

> **Para agentes ejecutores:** usar la habilidad `superpowers:executing-plans` para ejecutar las tareas de este plan. Los pasos se registran mediante casillas. Se recomienda ejecución directa y secuencial por tratarse de documentos relacionados, sin trabajo paralelo que justifique repartir la autoría.

**Objetivo:** establecer en `VibeCoding/VCX` una estructura documental portable que explique el ecosistema, delimite sus responsabilidades y permita preparar nuevos proyectos y equipos con contextos propios.

**Arquitectura:** VCX compone una base reutilizable —Blends, Brix y Cellar— y los portfolios que la utilizan. `cellar/` documenta el producto; `cellars/` es el punto de entrada de sus instancias. Cada pieza e iniciativa tiene contexto propio y las definiciones compartidas tienen una sola fuente editable.

**Tecnologías:** Markdown, rutas relativas y archivos de instrucciones `AGENTS.md`. Esta etapa no selecciona un framework de aplicación ni incorpora dependencias o código ejecutable.

**Base de diseño:** [matriz fundacional](/Users/denispaiva/.codex/visualizations/2026/10/30/01a18a92-d2e8-7a02-bb05-bb620bc33e3d/vcx-foundational-matrix.md), documento conceptual y conversación de diseño. Son antecedentes históricos externos; las fuentes de origen también se identifican en la sección de fuentes de este plan.

**Estado:** ejecución documental autorizada por el usuario el 2026-10-30: «comienza con tu propuesta». El avance se registra en las casillas y en el [reporte](../reports/2026-10-30-vcx-foundation.md). La autorización de ejecución no ratifica automáticamente todas las decisiones de arquitectura propuestas. La migración de blends requiere un pedido posterior explícito.

**Incorporación de contexto previa a la ejecución (2026-10-30):** se añadió el [criterio de nombres](../../naming.md) y se conservó el [glosario sin curar](../../references/enology-glossary-source.md) aportado por el usuario. En ese momento las cuatro tareas seguían pendientes. El avance actual figura en el reporte; no se asignaron nombres nuevos.

## Restricciones globales

- La ubicación inicial propuesta es `/Users/denispaiva/VibeCoding/VCX`. No fija el destino de una migración del sistema existente.
- `/Users/denispaiva/blends` es referencia de solo lectura. No copiar su código, no modificar su backlog, no crear ramas ni ejecutar comandos de entrega en él.
- Inglés para nombres técnicos, archivos, carpetas, identificadores y elementos de máquina; español para documentación, interfaz y comunicación. Los nombres propios conservan su forma oficial.
- El glosario enológico es un banco de candidatos sin curar: seleccionar por afinidad con la misión o función, verificar solo los términos elegidos y consultar nombres existentes antes de aprobar un uso. No traducir ni renombrar identidades automáticamente.
- A reúne Blends, Brix y Cellar como productos reutilizables. B reúne ideas y proyectos que viven lógicamente en instancias de Cellar y conservan contexto propio.
- Una única fuente editable por dato y una única fuente canónica de código por producto. Las matrices anteriores quedan como antecedentes históricos cuando se establezca la documentación canónica de VCX.
- No presentar capacidades diseñadas como implementadas. Usar estados documentales explícitos: acordado, propuesto y pendiente.
- No elegir el nombre del primer Cellar, no crear una instancia real y no asumir que el proyecto llamado VCX en la aplicación sea un portfolio.
- No introducir una carpeta `contracts/` o `trasiego/` mientras su nombre y alcance estén pendientes. Documentar la propiedad de las interfaces dentro de arquitectura.
- No inicializar Git, elegir remotos, instalar herramientas, crear paquetes o desplegar durante esta etapa documental. El monorepo modular es el enfoque propuesto; sus decisiones físicas quedan registradas de manera explícita.

## Focos de revisión

1. Un equipo nuevo debe entender A sin necesitar el portfolio actual ni rutas locales de Denis: comprobar la lectura desde los README de productos y las plantillas en las tareas 2 y 3.
2. Un agente que entra a un componente debe encontrar su misión, alcance y contexto mínimo: comprobar las rutas de entrada de la tarea 2.
3. Una instancia de Cellar no debe confundirse con el producto Cellar ni duplicar su código: revisar la estructura y plantillas de las tareas 1 y 3.
4. Una propuesta no debe transformarse por redacción en decisión aprobada: revisar el registro de decisiones de la tarea 1 y su coherencia en la tarea 4.
5. Los enlaces internos deben sobrevivir al traslado del workspace: verificar rutas relativas y separar referencias históricas a fuentes locales en la tarea 4.

## Estructura al terminar la ejecución

```text
VCX/
├── README.md
├── AGENTS.md
├── docs/
│   ├── vision.md
│   ├── executive-pitch.md
│   ├── naming.md
│   ├── references/
│   │   └── enology-glossary-source.md
│   ├── architecture/
│   │   ├── overview.md
│   │   ├── responsibility-matrix.md
│   │   └── interoperability.md
│   ├── decisions/
│   │   └── README.md
│   ├── sources.md
│   └── superpowers/
│       └── plans/
│           └── 2026-10-30-vcx-foundation.md
├── blends/
│   ├── README.md
│   └── AGENTS.md
├── brix/
│   ├── README.md
│   └── AGENTS.md
├── cellar/
│   ├── README.md
│   ├── AGENTS.md
│   └── templates/
│       ├── cellar/
│       │   └── README.md
│       └── initiative/
│           ├── README.md
│           └── AGENTS.md
└── cellars/
    └── README.md
```

Cada carpeta tiene una función concreta. No se crean árboles vacíos de implementación. Las carpetas `blends/`, `brix/` y `cellar/` contienen inicialmente contexto documental; no son copias funcionales de los productos existentes.

## Tarea 1 — Establecer la identidad y las definiciones canónicas

**Archivos:** crear `README.md`, `AGENTS.md`, `docs/vision.md`, `docs/executive-pitch.md`, `docs/architecture/overview.md`, `docs/architecture/responsibility-matrix.md`, `docs/architecture/interoperability.md`, `docs/decisions/README.md` y `docs/sources.md`.

**Consume:** conversación, speech aceptado y matriz fundacional anterior. **Produce:** la documentación canónica de identidad, fronteras, contratos y decisiones a la que enlazan los demás contextos.

- [x] Escribir `README.md` como entrada breve: qué es VCX, grupos A/B, mapa de carpetas y estado documental inicial. Enlazar a las definiciones completas.
- [x] Escribir `docs/vision.md` con misión, visión, destinatarios, objetivos y límites de VCX. Mantener el foco en portabilidad, comienzo ágil y autonomía de las iniciativas.
- [x] Incorporar el speech aceptado a `docs/executive-pitch.md` como fuente editable del mensaje ejecutivo para una landing futura. El README enlaza a este texto en vez de mantener una copia completa.
- [x] Establecer en `overview.md` la separación entre productos, instancias y proyectos; explicar el monorepo modular propuesto y las pruebas conceptuales de independencia. Brix es un núcleo de capacidades; no reasignar el nombre histórico Blends Kernel.
- [x] Adoptar `responsibility-matrix.md` como fuente editable de responsabilidades técnicas, RACI propuesta e invariantes. Identificar la matriz anterior como antecedente fechado, sin modificarla ni mantener ambas en paralelo.
- [x] Documentar en `interoperability.md` el dueño de cada interfaz: Cellar para portfolio, Brix para capacidades, Blends para orquestación; convenciones comunes con fuente única y responsable explícito. Mantener pendiente el nombre de la capa compartida.
- [x] Registrar en `docs/decisions/README.md` cada decisión con asunto, estado, fundamento, fuente y consecuencia. Distinguir acuerdos del usuario de propuestas del autor.
- [x] Incluir como pendientes: nombre y ruta del primer Cellar, ubicación física del código de las iniciativas, distribución final de contratos y conciliación de las decisiones aprobadas del kernel. Registrar el monorepo como enfoque aceptable y recomendado, sin inventar una aprobación de todos sus detalles.
- [x] Escribir `AGENTS.md` con idioma, fuentes únicas, carga progresiva del contexto, límites entre componentes y prohibición de asumir autorización de migración. Las instrucciones locales enlazan a esta fuente y agregan solo su contexto específico.
- [x] Identificar las fuentes en `docs/sources.md`, separando antecedentes históricos de documentación normativa vigente.
- [x] Enlazar desde el README y las fuentes al criterio de nombres y al glosario ya incorporados. Mantener el glosario como antecedente sin curar y no duplicarlo en otro catálogo. Registrar cualquier nombre aprobado mediante su decisión explícita.

**Aceptación:** desde el README se puede distinguir qué es VCX, qué ofrece A, dónde vive B y qué sigue pendiente. Cada definición tiene una sola fuente normativa. No se altera la identidad de ninguna iniciativa existente.

## Tarea 2 — Preparar contextos propios para Blends, Brix y Cellar

**Archivos:** crear `blends/README.md`, `blends/AGENTS.md`, `brix/README.md`, `brix/AGENTS.md`, `cellar/README.md` y `cellar/AGENTS.md`.

**Consume:** documentos canónicos de la tarea 1. **Produce:** tres entradas autónomas de contexto, sin implementación duplicada.

- [x] Escribir el README de Blends con misión, visión, usuarios, responsabilidades, entradas, resultados esperados y límites. Presentarlo como experiencia y conducción del trabajo, incluyendo gobierno además de interfaz.
- [x] Escribir el README de Brix con misión, visión, consumidores, capacidades previstas e independencia de Blends. Distinguir esa meta del desacople parcial del Brix existente.
- [x] Escribir el README de Cellar con misión, visión, formato, configuración, custodia y portabilidad. Diferenciar el producto de las instancias y explicitar que su alcance ejecutable debe detallarse antes de implementarlo.
- [x] En cada README incluir estado actual, contexto de entrada y enlaces a las fuentes comunes; no copiar matrices o políticas completas. No crear un segundo roadmap del producto existente.
- [x] En cada `AGENTS.md` especificar qué leer primero, qué documentación adicional cargar según la tarea y qué superficies pertenecen a otros componentes.
- [x] Realizar una lectura de entrada de cada componente: comprobar que su propósito y límites se entienden sin cargar el contexto del resto del portfolio. Comprobar que sus enlaces comunes resuelven.

**Aceptación:** cada producto tiene un contexto enfocado en su misión y visión. Ninguno requiere copiar código, datos o instrucciones internas de blends para explicar su función.

## Tarea 3 — Preparar el punto de entrada y las plantillas de portfolios

**Archivos:** crear `cellars/README.md`, `cellar/templates/cellar/README.md`, `cellar/templates/initiative/README.md` y `cellar/templates/initiative/AGENTS.md`.

**Consume:** formato conceptual de Cellar y fuentes compartidas de las tareas anteriores. **Produce:** plantillas documentales reutilizables; no una instancia real ni un contrato de máquina implementado.

- [x] Documentar en `cellars/README.md` qué es una instancia, quién la custodia y cómo se relaciona con el producto `cellar/`. Explicar que este directorio todavía no contiene portfolios reales.
- [x] Crear una plantilla de Cellar con campos documentales para identidad, propietario, propósito, equipo, iniciativas, versiones adoptadas, configuración, almacenamientos y referencias de recuperación. Marcar los datos por completar con identificadores en inglés y explicar su significado en español.
- [x] Crear una plantilla de iniciativa con identidad, tipo idea/proyecto, misión, visión, destinatarios, alcance, objetivos, estado, ubicación canónica del código y referencias únicas a planificación, decisiones y evidencia. No crear archivos vacíos para cada apartado.
- [x] Crear la plantilla de instrucciones de iniciativa con entrada mínima de contexto, reglas locales y referencias a políticas adoptadas. Los enlaces se parametrizan para resolver al instanciarla; no dependen de una profundidad fija del directorio de plantillas.
- [x] Explicar el uso manual de las plantillas y los campos que deben resolverse antes de usarlas. No prometer un wizard, generador o exportador que todavía no existe.
- [x] Hacer una prueba documental con una iniciativa ficticia descrita en la revisión, sin dejar una instancia escritora adicional: verificar que puede expresar su propósito y fuentes sin nombres o rutas de proyectos actuales.

**Aceptación:** un equipo nuevo puede identificar qué información necesita para comenzar. No se crea `personal`, no se trasladan iniciativas y no se duplica el backlog de `queue`.

## Tarea 4 — Verificar y entregar la fundación documental

**Archivos:** revisar todos los creados; actualizar únicamente sus defectos y las casillas de ejecución de este plan.

**Consume:** documentos de las tareas 1–3. **Produce:** índice navegable y reporte de verificación con pendientes explícitos.

- [x] Inventariar con `rg --files --hidden -g '!.DS_Store' /Users/denispaiva/VibeCoding/VCX`; comparar contra el árbol de este plan y explicar cualquier diferencia.
- [x] Comprobar todos los enlaces locales desde la ubicación del archivo que los contiene. Las referencias históricas externas están identificadas como tales; los enlaces parametrizados de las plantillas se verifican según su instrucción de instanciación.
- [x] Revisar misión y visión de VCX y de los tres productos, la matriz, la propiedad de contratos y la separación `cellar/` / `cellars/`. Resolver contradicciones en su fuente canónica.
- [x] Comprobar que los candidatos del glosario no se presentan como nombres reservados o aprobados; que cada uso nuevo conserva su decisión y que las identidades existentes, incluida Trasiego, permanecen diferenciadas.
- [x] Buscar supuestos incrustados con `rg -n 'personal|/Users/|framework|Trasiego|contracts/' /Users/denispaiva/VibeCoding/VCX`; revisar cada coincidencia. Son admisibles referencias históricas, límites y pendientes explícitos, no dependencias operativas implícitas.
- [x] Comprobar que solo existe contenido documental: ningún código, paquete, backlog, ledger o historial del sistema actual fue copiado. Verificar mediante el registro de archivos escritos que no se modificó blends.
- [x] Entregar enlaces al README, matriz, decisiones y speech, junto con decisiones pendientes y verificaciones efectuadas. No inicializar Git ni ejecutar una entrega del repositorio blends.

**Aceptación:** la estructura puede recorrerse y comprenderse desde su raíz, conserva el desacople contextual y distingue diseño de funcionalidad disponible. La entrega no afirma que los productos estén implementados o migrados.

## Orden y cierre

Ejecutar 1 → 2 → 3 → 4. Cada tarea se acepta por coherencia y navegación documental; no se agregan pruebas automatizadas que solo reproduzcan el texto o la lista de archivos. Si se introduce código o un formato de máquina en otro pedido, requiere su propio alcance y verificaciones.

El resultado de este plan es la fundación documental. El inicio de Git, manifiestos ejecutables, herramientas de generación, selección del primer Cellar y migración de blends son trabajos posteriores explícitos.

## Fuentes históricas de este plan

- Matriz: `/Users/denispaiva/.codex/visualizations/2026/10/30/01a18a92-d2e8-7a02-bb05-bb620bc33e3d/vcx-foundational-matrix.md`.
- Propuesta anterior: `/Users/denispaiva/.codex/visualizations/2026/10/30/01a18a88-a2e2-75a0-9e02-58c50c69d340/vcx-architecture-proposal.md`.
- Documento conceptual: `/Users/denispaiva/.codex/attachments/b0ebcea4-594c-405e-91fc-0f4447246ba5/Pasted text.txt`.
- Decisiones previas: `/Users/denispaiva/blends/docs/superpowers/specs/2026-10-24-vc-carpetas-orden-design.md`.
- Confirmación de alcance y speech ejecutivo: conversación de VCX del 2026-10-30.
- Glosario sin curar aportado por el usuario: `/Users/denispaiva/Downloads/glosario_enologia_monopalabra.md`; copia histórica en `docs/references/enology-glossary-source.md` y criterio de uso en `docs/naming.md`.
