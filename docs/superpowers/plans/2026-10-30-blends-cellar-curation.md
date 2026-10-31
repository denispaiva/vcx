# Plan de curación de Cellar y Blends

> **Para agentes ejecutores:** usar `superpowers:executing-plans` para ejecutar secuencialmente las tareas aprobadas. Las casillas registran avance, no aprobación del usuario.

**Objetivo:** dejar Cellar y Blends con contextos de proyecto claros, verificables y suficientes para continuar su desarrollo como productos de primer nivel de VCX.

**Arquitectura:** conservar `cellar/` y `blends/` como pares directamente bajo VCX. Curar primero Cellar y después Blends, contrastándolos con el recorrido conjunto existente. Sus README serán las entradas canónicas; las definiciones compartidas seguirán enlazadas desde sus fuentes actuales.

**Tecnologías:** Markdown y referencias relativas; sin código, instalaciones ni cambios de almacenamiento operativo.

**Base de diseño:** [arquitectura](../../architecture/overview.md), [primer recorrido conjunto](../specs/2026-10-30-cellar-blends-first-journey-design.md), contextos de [Cellar](../../../cellar/README.md) y [Blends](../../../blends/README.md).

**Estado al 2026-10-30:** plan aprobado por el usuario mediante «vamos» después de su presentación, incluyendo la secuencia y modalidad directa recomendadas. Ejecución documental completada según las casillas y el [reporte](../reports/2026-10-30-blends-cellar-curation.md). La autorización no incluye implementación, instancia real ni migración.

## Alcance y criterio de curación

Un proyecto queda documentalmente curado cuando su entrada permite comprender propósito, destinatarios, alcance, estado respaldado, fuentes canónicas, dependencias, autoridad, decisiones abiertas y siguiente entregable. Debe poder leerse sin cargar todo el portfolio y sin confundir capacidades diseñadas con disponibles.

Se enriquecen los contextos existentes: no se vuelve a ingresar estos productos como ideas ni se inventan actas de graduación. La pertenencia lógica de su seguimiento a una futura instancia de Cellar permanece pendiente.

## Restricciones

- Conservar nombres e identidades; Brix mantiene su posición actual y solo se consulta por dependencias declaradas.
- Mantener una fuente editable por dato; no crear roadmaps, backlogs, presupuestos o políticas paralelos.
- El sistema existente de Blends es referencia de solo lectura. No mover, copiar o extraer implementación; no modificar `queue`, ramas, controles, recursos cloud o despliegues.
- No crear una instancia real de Cellar, inicializar Git ni elegir ubicación física del código por inferencia.
- Documentar en español y conservar identificadores, archivos y estados técnicos en inglés.
- Usar rutas relativas entre documentos de VCX. Las ubicaciones externas se identifican como referencias de origen, no como requisitos operativos.
- No interpretar esta curación como aprobación de las interfaces, matriz o modelo que siguen propuestos.
- No agregar dependencias ni pruebas que solo reproduzcan el texto. Verificar navegación, coherencia y procedencia.

## Archivos y responsabilidad

| Archivo | Cambio previsto y responsabilidad |
|---|---|
| `cellar/README.md` | Curar la entrada del proyecto y enlazar su estado, fuentes y siguiente entregable |
| `cellar/AGENTS.md` | Ajustar la lectura de entrada únicamente si la curación modifica referencias |
| `blends/README.md` | Curar la entrada del proyecto, distinguiendo objetivo y antecedentes implementados |
| `blends/AGENTS.md` | Ajustar la lectura de entrada únicamente si corresponde |
| `docs/decisions/README.md` | Registrar el acuerdo de jerarquía y prioridad, y decisiones surgidas con su autoridad |
| `README.md` | Enlazar el recorrido de curación y mostrar la prioridad sin cambiar la composición de VCX |
| `docs/sources.md` | Incorporar referencias nuevas solo si aportan una fuente no registrada |
| `docs/superpowers/reports/2026-10-30-blends-cellar-curation.md` | Crear evidencia fechada de ejecución, verificaciones y pendientes |

Los documentos de dominio y las plantillas se leen para contrastar la entrada; su rediseño no forma parte de este corte. Una contradicción se registra con fuente y resolución requerida, sin ocultarla mediante otra definición en el README. Tampoco se duplica la matriz de responsabilidades.

## Focos de revisión

1. Cellar producto frente a instancia: el lector distingue formato y mecanismos de datos concretos de portfolio.
2. Blends objetivo frente a sistema existente: cada afirmación de disponibilidad tiene fuente y fecha; la curación no declara independencia demostrada.
3. Jerarquía frente a autoridad: estar directamente bajo VCX no concede permisos ni crea una instancia propietaria del seguimiento.
4. Contexto frente a estado operativo: los README localizan fuentes de trabajo; no copian estados completos del backlog ni compromisos financieros.
5. Acuerdos frente a propuestas: los pendientes siguen visibles y ningún requisito documentado aparece como capacidad ejecutable.

## Tarea 1 — Fijar acuerdos y fuentes de entrada

**Archivos:** modificar `docs/decisions/README.md`; leer las fuentes de diseño enlazadas y las instrucciones comunes y locales.

**Consume:** confirmación del usuario sobre jerarquía y validación posterior de este plan. **Produce:** alcance trazable para ambas curaciones.

- [x] Registrar, con el siguiente ID libre, fecha y cita de esta conversación, el acuerdo de Blends y Cellar como pares de primer nivel y su prioridad de curación.
- [x] Registrar el orden Cellar → Blends como aprobado solo si la validación lo incluye; conservar separados los pendientes de instancia, código y kernel.
- [x] Identificar las fuentes necesarias de cada producto usando `docs/sources.md`; usar `docs/architecture/current-system-mapping.md` como evidencia histórica, no como inventario actualizado.

**Aceptación:** el registro expresa qué decidió el usuario y qué sigue pendiente, sin ratificar otras propuestas o autorizar migración.

## Tarea 2 — Curar el proyecto Cellar

**Archivos:** modificar `cellar/README.md`; ajustar `cellar/AGENTS.md` solo si cambia la navegación.

**Consume:** alcance de tarea 1, modelo de iniciativa, plantillas existentes e interfaces propuestas. **Produce:** entrada autónoma de Cellar que Blends pueda referenciar.

- [x] Revisar misión, visión, destinatarios y límites existentes; conservarlos salvo correcciones de coherencia sustentadas.
- [x] Explicitar el estado: definición y plantillas disponibles; modelo propuesto; mecanismos ejecutables e instancia real pendientes.
- [x] Añadir referencias de trabajo a modelo, plantillas, contratos y decisiones, sin copiar sus definiciones.
- [x] Mostrar dependencias con Blends y Brix y distinguir custodia del portfolio de gobierno e instrumentos.
- [x] Formular como propuesta el siguiente entregable: alinear las plantillas con el modelo mínimo mediante un caso sintético. Indicar aceptación esperada: identidad, procedencia, decisiones y fuentes representables sin instancia real ni dobles registros. Su ejecución queda fuera de esta curación.
- [x] Comprobar leyendo la entrada que se distingue producto/instancia, que no se inventan propietarios, versiones o backend y que todos sus enlaces locales resuelven.

**Aceptación:** un lector identifica qué ofrece hoy Cellar, qué falta diseñar o implementar y dónde se mantiene cada definición.

## Tarea 3 — Curar el proyecto Blends

**Archivos:** modificar `blends/README.md`; ajustar `blends/AGENTS.md` solo si cambia la navegación.

**Consume:** entrada curada de Cellar, documentos de proceso y correspondencia histórica con Blends existente. **Produce:** entrada autónoma de Blends compatible con las fronteras de Cellar.

- [x] Revisar misión, visión, destinatarios y alcance sin reducir Blends a una interfaz visual.
- [x] Separar el diseño disponible en VCX de la implementación del sistema existente. Cuando haga falta confirmar una afirmación, leer solo su fuente concreta y registrar fecha y límites de esa comprobación.
- [x] Enlazar las fuentes de ingreso, exploración, FinOps y graduación; localizar el seguimiento existente sin copiar sus ítems o porcentajes.
- [x] Explicitar dependencias: Cellar custodia información; Brix provee instrumentos; la autoridad humana conserva decisiones de su ámbito.
- [x] Formular como propuesta el siguiente entregable: precisar una operación documental de ingreso y registro sobre el modelo de Cellar, con entradas, salidas, revisiones, permisos y recuperación definidos. Su aceptación deberá cubrir las dos decisiones humanas del ingreso y la ausencia de duplicados, sin implementar comandos en este corte.
- [x] Comprobar que la entrada distingue Blends Kernel, producto objetivo y seguimiento actual; que no atribuye a Brix el gobierno y que los enlaces resuelven.

**Aceptación:** el lector comprende propósito, situación, dependencias y siguiente paso sin asumir migración, gasto o automatizaciones disponibles.

## Tarea 4 — Comprobar el conjunto y entregar

**Archivos:** modificar `README.md`, actualizar `docs/sources.md` si corresponde y crear el reporte señalado en la tabla de archivos.

**Consume:** entradas curadas y registro actualizado. **Produce:** navegación coherente y evidencia de cierre.

- [x] Enlazar desde la raíz los contextos curados y este plan, conservando Brix en la base reutilizable y `cellars/` como entrada de futuras instancias.
- [x] Recorrer el ejemplo sintético del diseño conjunto como lectura de coherencia: localizar información en Cellar, proceso en Blends e instrumentos en Brix. No ejecutar consejo, comandos o registros reales.
- [x] Comprobar enlaces relativos y anclas de todos los documentos modificados desde su ubicación; verificar que los marcadores solo correspondan a material de plantilla.
- [x] Revisar los cinco focos y registrar contradicciones, evidencia y pendientes concretos; no declarar cerradas decisiones que requieren al usuario.
- [x] Verificar que las escrituras se limitaron a los archivos documentales autorizados en VCX y que no se modificó el sistema de origen.
- [x] Completar casillas y reporte con archivos cambiados, verificaciones realmente realizadas, límites y próximos entregables propuestos por producto.

**Aceptación final:** ambos proyectos tienen entradas suficientes para continuar; los enlaces resuelven; las responsabilidades coinciden con sus fuentes; no se duplicó estado operativo ni se implementó o migró ningún producto.

## Orden y validación

Ejecutar 1 → 2 → 3 → 4, de forma directa y secuencial por compartir fuentes y decisiones. Esta es la modalidad recomendada; no exige repartir autoría entre agentes.

El usuario validó este plan y se entregan los contextos curados y sus pendientes. Cualquier implementación, instancia o migración posterior tendrá un alcance explícito propio.
