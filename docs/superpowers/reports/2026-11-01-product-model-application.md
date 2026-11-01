# Reporte de ejecución: aplicación documental del modelo de productos (VCX-D029)

Fecha: 2026-11-01. Evidencia fechada de la ejecución del [plan de aplicación](../plans/2026-11-01-product-model-application.md), autorizada por el usuario con «Sí, ejecutá» en el chat con Claude del 2026-11-01. No sustituye las fuentes editables ni el [registro de decisiones](../../decisions/README.md).

## Resultado

Los 20 archivos del plan quedaron aplicados en el árbol de trabajo, en dos pasos del mismo día. El precursor no se leyó ni se escribió. El commit de aplicación no se hizo: requiere autorización propia.

| Paso | Archivos |
|---|---|
| Primero, sobre archivos limpios | `docs/architecture/responsibility-matrix.md`, `docs/architecture/interoperability.md`, `cellar/README.md`, `cellars/README.md`, `cellar/docs/initiative-model.md`, `blends/README.md`, `blends/docs/idea-to-project.md`, `blends/docs/idea-intake.md`, `blends/docs/architecture-and-finops.md`, `brix/README.md`, `AGENTS.md`, `docs/vision.md`, `docs/architecture/overview.md`, `docs/executive-pitch.md`, `docs/naming.md`, este reporte |
| Diferidos hasta el commit `c4d2dc1` del usuario, que registró D027 a D029, la matriz de tooling, las dos specs y el vocabulario | `README.md`, `docs/decisions/README.md`, `docs/architecture/tooling-matrix.md`, `docs/superpowers/specs/2026-10-31-idea-maturation-design.md` |

El diferimiento evitó mezclar alcances: el usuario commiteó primero los cambios ajenos, separando con `git add -p` la línea del vocabulario en `AGENTS.md` de la frase de marca de este plan. Después se aplicaron los cuatro restantes sobre archivos limpios respecto de `HEAD`.

## Tarea 1: precondiciones

- Rama `main`, un solo commit `f47c71f`, raíz del repositorio documental. Comprobado con `git log --oneline` y `git branch --show-current`.
- `git status --short` al inicio: cambios pendientes en `README.md` y `docs/decisions/README.md`; archivos sin seguimiento `docs/architecture/tooling-matrix.md`, las dos specs del 2026-10-31 y el plan. Cuatro coinciden con la lista del plan; el plan decía tres, era un error de conteo.
- Durante la ejecución apareció trabajo concurrente de otra sesión: `docs/vocabulary.md` nuevo, una línea en las convenciones de `AGENTS.md` que lo enlaza y una precisión de VCX-D028 en el registro. No se tocaron ni se revirtieron. El vocabulario es coherente con VCX-D029 y con la frontera del plan; su línea «las fuentes todavía no se actualizaron» quedó desactualizada por esta ejecución y corresponde a su propio alcance. La precisión de D028 agregó una columna «Capacidad» a la matriz de tooling antes de su commit; las filas de esta aplicación se ajustaron sobre esa versión.

## Qué cambió

- **Matriz de responsabilidades.** Sección nueva «1. Método y conducción» con la regla de reparto, la prueba de pertenencia y seis ejemplos; es la única fuente de la frontera. Filas técnicas partidas por tramo de idea y de proyecto; fila nueva de conducción. RACI: responsable del portfolio como A en ideas, gate y graduación; PO del proyecto como A en proyectos; nota de que ambas asignaciones coexisten. Invariantes 2 y 3 reescritos; el 3 conserva la lectura sin ejecutar Blends o Brix como prueba de custodia.
- **Interoperabilidad.** Fila «Operaciones de conducción de proyecto», dueño Cellar · producto, contenido pendiente. «Decisión del PO» pasa a autoridad humana competente según el tramo. El ejemplo de graduación nombra al responsable del portfolio y deja el traspaso como pendiente.
- **Cellar.** Misión, visión, alcance y resultados con custodia y conducción como responsabilidades distinguidas, sin módulos. Autoridad por tramo con ambas asignaciones. Código en repositorios propios. Instancias: custodia íntegra, conducción con PO, propuesta en preparación fuera del portfolio activo y sin instancia obligatoria. Modelo de iniciativa: `ownerRef` no se sobrescribe; `productOwnerRef` nuevo, conceptual, asignado al graduar; `definitionRef` sin MVP obligatorio; lectura por tramo.
- **Blends.** Misión como dueño del método y coordinador del tramo de idea; alcance sin conducción de proyectos; Blends Kernel sigue conduciendo en el precursor hasta VCX-D011. Recorrido: coordina el tramo de idea; responsable del portfolio decide y asigna PO; paso 3 con vía de validación propuesta; paso 5 con PO asignado y traspaso pendiente; «Siguiente límite» apunta a la conducción en Cellar. Ingreso y FinOps: responsable del portfolio como autoridad de esa etapa.
- **Brix.** Diseño y operaciones Git en el alcance conceptual, declaradas y no implementadas; núcleo de capacidades técnicas, «kernel» reservado; no aloja código de productos ni proyectos.
- **Raíz.** AGENTS: frase de marca con VibeOS, principios intactos. Visión: marca, objetivo con el reparto y señal nueva. Arquitectura: fronteras, Brix como núcleo, código en repositorios propios, prueba de independencia nueva. Speech ejecutivo: Blends define el método y acompaña ideas, Cellar conduce. Nombres: VibeOS como marca registrada, sin identidad de producto. README: título con VibeOS, línea de reparto con enlace a la matriz y entrada al modelo, el plan y este reporte.
- **Matriz de tooling.** Cellar suma conducción en las fases consideradas; las siete filas «Entrega · …» y la fila del plan del proyecto graduado pasan a «Cellar · conducción, …», con nota de dónde figuraban; estados de asignación sin cambio; el destino previsto reparte las fases entre método y conducción.
- **Spec de maduración.** Un párrafo de lectura según VCX-D029: la autoridad del gate es el responsable del portfolio y asigna el PO; no aprueba el cambio del gate.
- **Registro.** Estado de VCX-D029 «aplicación documental ejecutada el 2026-11-01»; la consecuencia cita la autorización «Sí, ejecutá», el plan, este reporte y el commit `c4d2dc1` previo. La decisión original no se reescribió.

## Recorrido de referencia por fuente

| Paso del mapa de talleres | Dónde se lee ahora | Contradicción |
|---|---|---|
| Propuesta: Brix prepara, Blends coordina, el responsable del portfolio confirma el ingreso | Ingreso, paso 6; matriz RACI; instancias | Ninguna |
| Registro y FinOps: la instancia registra, Brix propone, el responsable del portfolio autoriza | FinOps, tabla de responsabilidades; recorrido, pasos 1 y 1.1 | Ninguna |
| Exploración: Blends aplica el método, la instancia custodia | Recorrido, paso 2; matriz, fila de proceso del tramo de idea | Ninguna |
| Gate: graduar, diferir o archivar y asignar PO | Recorrido, paso 4 y encabezado; RACI, fila de graduación; modelo, `productOwnerRef` | Ninguna |
| Graduación: Blends prepara el contexto; desde ahí Cellar conduce | Recorrido, paso 5 y «Siguiente límite»; modelo, «Estados y relaciones» | Traspaso pendiente de diseño, declarado en las tres fuentes |
| Evolución: Cellar conduce bajo el método de Blends | Matriz, sección 1 y filas de conducción; Cellar README; arquitectura; speech; README de la raíz; matriz de tooling | Ninguna |

## Comprobaciones

- Frases retiradas (`Cellar organiza y custodia`, `Blends conduce el trabajo`, `hipótesis de MVP`, `decisión del PO`, `PO competente`, presupuesto «al PO» o «por el PO»): solo quedan dos menciones a «hipótesis de MVP» en la spec de maduración, donde describen el estado anterior y no se reescriben. Ninguna fila «Entrega · …» queda en la matriz de tooling.
- `\bPO\b` en las fuentes editadas: todas las ocurrencias están en contexto de proyecto, de asignación al graduar o de autoridad por tramo. Ninguna asigna PO a una idea.
- Enlaces y anclajes: comprobados con el script del plan sobre los 21 archivos modificados o nuevos; resultado «links OK».
- `git status --short` final: 19 archivos modificados, exactamente los 19 editables del plan; sin seguimiento, el plan y este reporte, además de archivos `.DS_Store`. Ningún archivo fuera de la lista.
- Precursor: ningún comando apuntó a `../blends/`.

## Límites

- Los cambios están en el árbol de trabajo, sin commit; `git diff` contra `c4d2dc1` es el diff de aplicación.
- `productOwnerRef` es un nombre conceptual propuesto, como el resto de los campos del modelo; no es esquema.
- La frontera y la fila de contrato son propuestas del asistente sobre el modelo acordado; su redacción puede revisarse sin reabrir VCX-D029.
- Nada aquí concilia el precursor ni aprueba el cambio del gate de la spec de maduración.

## Pendientes

1. Commit de aplicación, separado, con los 19 archivos modificados más el plan y este reporte, si la autorización lo nombra. Mensaje propuesto en el plan.
2. Actualizar en `docs/vocabulary.md`, alcance ajeno, la línea que dice que las fuentes no se actualizaron.
3. Diseño del traspaso al graduar; contrato de conducción; delegación del responsable del portfolio; conciliación VCX-D011; cambio del gate.
