# Correspondencia del primer recorrido con el sistema existente

Fecha: 2026-10-30. Análisis acotado de solo lectura. Esta tabla clasifica responsabilidades para diseñar VCX; no instruye movimientos de archivos ni sustituye las fuentes actuales.

## Base contrastada

Repositorio de referencia: `/Users/denispaiva/blends`. `HEAD` y `main` permanecen en `f86a2a7df72e55bbb97451c1a35ef3c03b961fc3`, sin diferencias versionadas respecto de la base analizada. La referencia local de `queue` consultada es `358ab19d8c2ebb887acbc1e85ff39af4d279110b`; es una foto local, sin fetch ni afirmación sobre el estado remoto.

Se observaron archivos no rastreados en `img/` y dos archivos de migración de Teyst. No se abrieron ni modificaron. No se ejecutaron scripts del sistema, hooks, sincronización de la cola, entrega o acciones de nube.

## Clasificación de responsabilidades

Las ubicaciones siguientes son relativas al repositorio de referencia, no rutas de destino.

| Fuente actual | Qué se preserva | Responsabilidad objetivo propuesta | Tratamiento en este corte |
|---|---|---|---|
| `ideas/README.md` | Captura mínima y primera validación del wizard actual | Blends: experiencia y proceso; Brix: nueva preparación requerida | La entrada actual crea la idea directamente; el objetivo nuevo exige revisión y consejo previos al registro. No se cambia el wizard existente |
| `vc/brix/README.md` e índice `vc/docs/tooling/brix-capabilities.md` | `brix idea <archivo.md>` está registrado como generador de `SPEC.md` ejecutable | Brix: distinguir capacidades por propósito | El usuario decide reutilizar `brix idea` como `/idea` de ingreso en VCX; el generador pasará a `brix spec` (VCX-D055); hace falta resolver compatibilidad antes de cambiarlo |
| `.claude/commands/council.md` e índice de capacidades | `/council <slug>` pertenece a Blends y requiere idea registrada; cinco asesores, revisión cruzada y síntesis sin recomendación | Objetivo: instrumento portable en Brix, orquestación de proceso en Blends | `brix council` = `/council` deberá recibir Markdown previo al ingreso; no se extrae ni modifica el comando existente en esta etapa |
| `vc/docs/standards/idea-lifecycle.md` | Preguntas decisivas, presupuesto, definición, gate humano y graduación de gobierno | Blends: proceso; Cellar: parámetros y registros concretos | Conservar reglas y vocabulario, sin cambiar su aplicación actual |
| `ideas/<id>/README.md` y documentos de exploración | Captura, preguntas, contexto e historia | Instancia de Cellar: iniciativa | Referenciar como aprendizaje; no duplicar datos operativos |
| `ideas/<id>/.roadmap.json` y `vc/<id>/.roadmap.json` | Identidad y seguimiento; separación entre tag de ciclo y `status` de trabajo | Instancia de Cellar: fuente declarada de seguimiento | El modelo nuevo distingue ambas dimensiones, sin reescribir esquemas o tags actuales |
| `vc/<id>/docs/decisions/0001-graduation.md` | Autoridad, fecha, evidencia, riesgos, excepciones y alcance de aprobación | Instancia de Cellar: decisión; Blends: verificación del gate | Se contrastó el acta de Salmanazar como precedente de excepción explícita |
| `vc/tools/lib/backlog-store.mjs` y `queue:backlog/` | Backlog, IDs y coordinación mediante el lock de la cola | Datos de portfolio en almacenamiento declarado; Blends coordina el acceso | No crear un backlog en VCX; leer la ref con Git, sin invocar funciones que sincronizan |
| `queue:queue/` y herramientas del tren | Integración y estado compartidos por repositorio | Blends: entrega; controles con ámbito del repositorio | No confundir cada Cellar con una cola o tren independiente |
| `vc/tools/` | Código de gobierno, validación y operación | Principalmente Blends; revisar capacidad por capacidad | No mover todos los scripts a Brix ni copiar su implementación |
| `vc/brix/` | Motores e instrumentos reutilizables con independencia parcial | Brix | Reconocer su frontera; no extraerlo ni asumir desacople completado |
| `vc/docs/templates/architecture.md` | Plantilla general de arquitectura con contexto, capas, contratos, riesgos y pruebas | Brix: capacidad objetivo de proponer una referencia; Cellar: documento de la iniciativa | Una plantilla no demuestra un generador implementado. La referencia temprana para FinOps no exige cerrar diseño final de construcción |
| `vc/docs/templates/finops-review.md` | Separación entre presupuesto, forecast, actuals, fuentes, allocation y decisión | Blends: revisión; Cellar: documento concreto | Preservar conceptos sin copiar importes, planes o proveedores del portfolio original como defaults de un equipo nuevo |
| `vc/brix/docs/decisions/0004-finops-motor.md` y `vc/brix/packages/cli/finops/` | Motor registrado de validación y agregación, esquema y multi-ledger | Brix: cálculo y validación | No equivale a generar arquitectura o presupuestos. La nueva plantilla documental no declara compatibilidad automática con el esquema vigente |
| `vc/tooling/evaluations/`, `usage/` y registros de adopción | Evidencia e historial del consumidor | Instancia de Cellar propietaria | Mantener la inmutabilidad y sus referencias históricas |
| `vc/tooling/branch-scopes.json` y `control-plane.json` | Alcances y autoridad del repositorio | Configuración de ese ámbito, interpretada por Blends | Un perfil de Cellar no puede anularlos |
| `vc/tooling/environment-ids.json` | Inventario canónico de backends y su dueño | Datos concretos del portfolio; Blends verifica; instrumentos reutilizables según contrato | Conservar la fuente actual y su relación con iniciativas graduadas |
| `roadmap/` y vistas generadas | Presentación del portfolio | Blends: implementación; salida derivada del estado declarado | No usar el dashboard como fuente de decisiones o estado alternativo |

## Decisiones aprobadas que siguen vigentes

| Decisión o control de origen | Conciliación propuesta en VCX | Qué no se decide aquí |
|---|---|---|
| Renombre visible a Blends Kernel; conservación de `framework`, `frameworkVersion`, `framework#…` y `blends-framework` | Preservar identidades y entender el kernel como gobierno de Blends | No renombrar IDs ni asignar ese kernel a Brix |
| Movimiento aprobado `vc/framework/` → `vc/kernel/` bajo disparadores | Revocado por VCX-D045, junto con su Fase 2 de configuración | No editar la spec del precursor; la `queue` se actualiza cuando lo ordene el PO |
| D-1: documentar y separar configuración del kernel de `tooling/` | Conservar la separación semántica entre código, política, configuración y datos | El destino de cada archivo sale del reparto de VCX-D045 |
| D-2: fases 1 y 2 en trenes separados, con una semana entre ambas | Pierde objeto con la revocación de VCX-D045 | No trasladar ese calendario al diseño documental de VCX |
| D-3: inventario de backends antes de crear el entorno de Salmanazar | Preservar dueño graduado, inventario y conciliación | No provisionar, renombrar o auditar recursos de nube desde esta tarea |

La comprobación actual encuentra inventario `schemaVersion=1.1.0`, listas y estados de backends, `vc/tools/reconcile-backends.mjs` y el runbook `vc/docs/tooling/backend-inventory.md` en `main`. A la vez, la entrada `BL-20261024-fase-s-inventario-de-backends-conciliado` sigue `open` en la foto local de `queue`. La presencia de implementación y el estado administrativo no se confunden: esta entrega no declara la Fase S pendiente de construir ni la cierra por inferencia.

Las decisiones D-1 y D-2 se corroboraron también en sus entradas de `queue:backlog/`: figuran `withdrawn` con notas `DECISION` del PO. En este sistema ese estado del ítem no significa que las decisiones fueron rechazadas. Las notas y las fuentes de aprobación conservan su significado.

## Diferencias que requieren diseño explícito

El usuario añadió al objetivo una entrada `/ideas <texto o archivo>` sobre Brix, aplicación de una plantilla de ideas, preguntas asesinas, revisión humana del Markdown, consejo por archivo y reporte antes de decidir el ingreso. Confirmó que la idea se registra **después** de revisar el reporte y confirmar su ingreso. Este requisito de VCX difiere de la captura directa actual y de la ubicación del consejo en la exploración del sistema existente; no se aplica retroactivamente a sus ideas.

El índice consultado no registra `/ideas` ni un comando independiente `/asesinas`; esto no prueba que no haya otros procedimientos. La nueva capacidad se documenta como requerida, no como disponible. El consejo actual es asesoría y no evidencia; su reporte tampoco gradúa una idea. La configuración y empaquetado de un instrumento de asesinas portable deben definirse antes de implementarlo.

El usuario precisó luego los nombres objetivo: `brix idea` = `/idea` y `brix council` = `/council`, con ayuda para completar el parámetro. La mención plural anterior se conserva como antecedente. La nueva semántica de `brix idea` y la extracción del instrumento de consejo a Brix requieren compatibilidad explícita; no se presupone que el CLI activo ya implemente el diseño.

El usuario añadió FinOps después del ingreso, construido desde un modelo de arquitectura de referencia de Brix. En el índice consultado no se identificó una capacidad registrada con esa interfaz; sí el motor FinOps. Se trata la arquitectura de referencia como requisito de capacidad y los documentos existentes como antecedentes, no como prueba de automatización disponible.

El sistema actual puede representar una etapa en el documento de idea y mediante un tag en el roadmap; el modelo de VCX propone una fuente canónica de ciclo y presentaciones derivadas. No se elige ahora cuál dato heredado prevalecería ante divergencias: una migración futura debe resolverlas con evidencia y autoridad.

El estándar actual fija el primer código greenfield dentro de `vc/<nombre>/`. La localización física en VCX sigue abierta: en esta fase solo se prepara contexto documental. Antes de implementar código nuevo o migrarlo habrá que conciliar esa regla de destino, sin cambiarla silenciosamente.

## Fuentes de la comprobación

- Instrucciones `AGENTS.md` y `vc/AGENTS.md` del repositorio de referencia.
- `vc/docs/standards/idea-lifecycle.md`, `ideas/README.md` y `vc/salmanazar/docs/decisions/0001-graduation.md`.
- `vc/docs/tooling/brix-capabilities.md`, `vc/tooling/brix-capabilities.json`, `vc/brix/README.md` y `.claude/commands/council.md`, consultados para distinguir interfaces y comportamiento existentes de las capacidades objetivo.
- `vc/docs/templates/architecture.md`, `vc/docs/templates/finops-review.md`, `vc/brix/docs/decisions/0004-finops-motor.md` y el esquema vigente del ledger, consultados sin copiar datos reales o asumir vigencia de precios de sus ejemplos.
- `vc/tools/lib/backlog-store.mjs`; entradas D-1, D-2 y Fase S mediante `git show queue:backlog/<id>.json`, sin checkout o sincronización.
- Diseños aprobados `docs/superpowers/specs/2026-10-05-kernel-renombre-to-be-design.md` y `2026-10-24-vc-carpetas-orden-design.md`.
- Rutas e inventario comprobados en `main`. Los estados de refs son evidencia fechada, no un monitor del sistema activo.
