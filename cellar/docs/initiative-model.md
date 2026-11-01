# Modelo mínimo de una iniciativa en Cellar

Fecha: 2026-10-30. Estado: propuesta de diseño del primer recorrido Cellar–Blends. Los nombres de campos son conceptuales; no constituyen un esquema implementado ni cambian el formato de los proyectos existentes.

## Propósito y fuente

Conservar el contexto desde la preparación de una propuesta hasta su ingreso como idea y eventual preparación como proyecto, con procedencia explícita, identidad estable desde el registro y una fuente canónica por dato. Este documento define la información; [el recorrido de Blends](../../blends/docs/idea-to-project.md) define el proceso del tramo de idea y la [matriz](../../docs/architecture/responsibility-matrix.md#1-método-y-conducción) el reparto entre método y conducción.

## Antes de ser una idea registrada

El [ingreso previo](../../blends/docs/idea-intake.md) prepara una propuesta con `/idea`, preguntas asesinas, un documento Markdown revisado por el humano y un reporte del consejo. Solo la confirmación humana posterior al reporte habilita su registro como idea. Es un requisito expresado por el usuario, no un cambio aplicado al sistema existente.

El ámbito de preparación conserva `submissionId`, fuentes, revisiones del documento, OK de envío, reporte y decisión de ingreso. No es una entrada activa del portfolio y no tiene todavía estado `registered`, `archived` o `deferred` del ciclo de iniciativas. Puede estar asociado a un destino propuesto, sin exigir que ya exista una instancia configurada para preparar el documento. Custodiar esa preparación no la admite.

Al admitir la propuesta se asigna o confirma `initiativeId` en el Cellar elegido y se conserva su relación con `submissionId`. A partir del registro, esa identidad de iniciativa permanece en todo el ciclo. El documento preparado se transfiere o reclasifica como fuente activa con su historia, sin mantener otro borrador editable paralelo. El formato del ámbito de entrada y su retención siguen siendo decisiones de implementación pendientes.

## Qué corresponde a cada nivel

| Nivel | Información propia | Qué referencia |
|---|---|---|
| Cellar | Identidad del portfolio, propietario, participantes, configuración y versiones adoptadas, prioridades y decisiones transversales | Iniciativas, perfiles de gobierno, almacenamientos y recuperación |
| Iniciativa | Identidad, propósito, situación, exploración, decisiones y evidencia específicas | Su planificación, autoridad, código cuando exista y dependencias declaradas |
| Producto reutilizable | Método en Blends, instrumentos en Brix, formato de portfolio y conducción de proyectos en Cellar | Interfaces públicas y versiones compatibles |

El índice del Cellar guarda identidades y ubicaciones; no replica el estado completo de cada iniciativa. El aislamiento entre instancias debe validarse antes de escrituras reales.

## Información mínima y aparición progresiva

| Campo conceptual | Semántica y momento requerido | Fuente propuesta |
|---|---|---|
| `cellarId` | Portfolio propietario; requerido desde el registro | Identidad del Cellar referenciada por la iniciativa |
| `initiativeId` | Identidad estable en ese portfolio; requerido desde el registro | Registro de iniciativa |
| `displayName` | Nombre visible; cambiarlo no cambia la identidad | Registro de iniciativa |
| `kind` | `idea` o `project`; cambia solo al completar la graduación | Registro de iniciativa |
| `ownerRef` | Autoridad responsable del propósito y decisiones: el responsable del portfolio mientras es idea; no se sobrescribe al graduar | Asignación explícita, referenciada desde la iniciativa |
| `productOwnerRef` | PO del proyecto, asignado en la decisión de graduar; requerido para publicar `kind=project`. Coexiste con `ownerRef` y ambas asignaciones se conservan como historia; qué decisiones corresponden a cada autoridad se precisa con el traspaso, pendiente | Decisión de graduación referenciada desde la iniciativa |
| `captureRef` | Palabras originales, problema y primera validación; requerido al registrar | Captura preservada; los refinamientos posteriores no la reescriben |
| `submissionRef` | Procedencia del proceso de preparación, requerido al ingresar por `/idea` | Registro de preparación con fuentes y revisiones |
| `ideaDocumentRef` | Documento Markdown revisado y enviado al consejo | Contexto de idea según la plantilla adoptada; una fuente activa |
| `councilReportRef` | Reporte del consejo y revisión del documento que analizó; requerido al registrar | Reporte de asesoría preservado con sus límites, no evidencia externa por sí mismo |
| `admissionDecisionRef` | Confirmación humana de ingreso posterior a revisar el reporte | Decisión de ingreso vinculada a documento y reporte concretos |
| `referenceArchitectureRef` | Modelo propuesto por Brix después del ingreso, con revisión y escenarios | Documento de arquitectura de referencia; hipótesis, no implementación aprobada |
| `finopsRef` | Estimación derivada del modelo, con escenarios y cobertura | Documento FinOps de la iniciativa; enlaza el gasto real en vez de duplicar transacciones |
| `budgetDecisionRef` | Presupuesto y alcance autorizados para la fase solicitada | Decisión humana sobre revisión, escenario, período y límites concretos |
| `mission` y `vision` | Pueden estar pendientes o propuestas en una idea; deben quedar explícitas para el contexto de proyecto | Contexto propio de la iniciativa |
| `lifecycleState` | Etapa del ciclo de idea; independiente del estado de trabajo | Registro de ciclo de vida de la iniciativa |
| `workStatusRef` | Referencia al estado de trabajo cuando existe planificación | Planificación canónica, no otro estado copiado al índice |
| `explorationRef` | Preguntas decisivas, presupuesto autorizado y resultados; requerido al iniciar exploración | Registro de exploración |
| `definitionRef` | Propuesta de valor, vía de validación propuesta y alternativas; MVP recomendado, no obligatorio; requerido para solicitar el gate ordinario | Definición acotada de la idea |
| `decisionRefs` | Decisiones con autoridad y evidencia, incluida graduación | Registros de decisión de la iniciativa |
| `evidenceRefs` | Fuentes y resultados que sustentan afirmaciones | Evidencia de la iniciativa o referencia a su ubicación declarada |
| `governanceRef` | Perfil y autoridad efectivos; parámetros adoptados sin copiar la política general | Perfil versionado y asignaciones particulares |
| `codeRef` | Ubicación canónica del código; puede no existir incluso después de graduar | Declaración de localización, no copia del producto |
| `planningRef`, `backlogRef`, `handoffRef` | Referencias al seguimiento y continuidad conforme se necesiten | Fuentes particulares declaradas; sin archivos vacíos por anticipación |
| `revisionRef` | Revisión del contexto sobre la que se pide o aplica una decisión | Almacenamiento declarado; su representación depende del adaptador |

Los IDs se interpretan junto con `cellarId`, evitando confundir iniciativas homónimas de distintos portfolios. Cambios de propietario entre Cellars quedan fuera de este recorrido. El tipo, la ruta o el nombre visible no se usan como identidad.

## Estados y relaciones

El proceso conserva los estados de ciclo documentados en el sistema existente: `registered`, `exploring`, `gate-ready`, `graduated`, `deferred` y `archived`. Son valores de máquina; la interfaz los presenta en español. La conservación de este vocabulario no exige copiar la representación técnica actual.

El estado de preparación previo al ingreso es otra dimensión y no amplía silenciosamente esa lista. El OK para consultar al consejo, la aceptación como idea y la graduación a proyecto son decisiones diferentes.

Después del registro se construye FinOps desde una arquitectura de referencia propuesta por Brix. La iniciativa sigue `registered` durante esa preparación; tener una estimación o un modelo no equivale a `exploring` sin presupuesto de exploración autorizado ni a `graduated`.

`lifecycleState` no reemplaza el estado de un roadmap: un proyecto puede conservar el antecedente `graduated` y tener trabajo `planned` o `active` según su seguimiento. Una idea lista para gate no se convierte por ello en proyecto.

La propuesta usa una sola identidad de iniciativa durante el recorrido. Al graduar, el contexto de proyecto referencia su captura, su decisión y la asignación del PO; la exploración se conserva como historia y no como una segunda iniciativa activa. Desde entonces Cellar conduce el proyecto bajo el método de Blends; el traspaso concreto está pendiente de diseño. Este es un criterio del diseño pendiente de aprobación, no una migración de IDs existentes.

## Decisión y evidencia

Una decisión registra identidad, fecha, autoridad, alcance, revisión evaluada, veredicto, fundamento, evidencia, riesgos pendientes y qué no autoriza. Una excepción identifica además la condición que se exceptúa y la autoridad competente que la admite. El mero texto «aprobado» escrito por un ejecutor no prueba una autorización.

Cada evidencia registra identidad, origen, fecha, autor o productor, ubicación, afirmación sustentada y límites. Las fuentes durables se preservan o se identifican mediante revisión o integridad verificable; un enlace mutable sin procedencia no demuestra qué se revisó. Un resultado de Brix conserva la naturaleza que tenga: cálculo, evaluación o asesoría, nunca aprobación humana. El reporte del consejo es asesoría, no evidencia externa ni autorización.

## Lectura, actualización y custodia

Cellar expone lectura por identidad y revisión, actualización autorizada y referencias verificables. Debe comprobar pertenencia al ámbito, permisos, integridad referencial y conflictos de revisión. Blends aplica el proceso y sus compuertas del tramo de idea a través de esa interfaz, y Cellar conduce el tramo de proyecto por la misma interfaz; el acceso directo a almacenamiento no debe convertirse en un canal alternativo que eluda la autoridad adoptada.

La preparación de proyecto debe poder completarse o recuperarse sin publicar dos seguimientos activos: [el recorrido](../../blends/docs/idea-to-project.md) fija el resultado y el tratamiento de interrupciones. Este corte no selecciona backend, protocolo, librería o formato persistente.

El respaldo de un Cellar real deberá incluir sus almacenamientos declarados, incluso otras ramas o servicios. Este modelo no descarga bases operativas ni conserva secretos o locks de procesos como memoria del portfolio.
