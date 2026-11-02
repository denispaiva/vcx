# `brix-llm-council`: pedidos para la revisión del 2026-12-02

Fecha: 2026-11-01. Estado: propuesta; nada ejecutado ni autorizado. Continúa la [evaluación de la etapa 3](../reports/2026-11-01-council-stage3-evaluation.md), que admitió la skill con excepción a VCX-D035 y fijó revisión el 2026-12-02.

## Dónde viven estos pedidos

VCX no tiene backlog propio. El que describe el [vocabulario](../../vocabulary.md) vive en la rama `queue` del precursor, que es de solo lectura. Por eso los pedidos quedan aquí con IDs locales `CR-n`, sin IDs `BL-…` que podrían chocar con los del precursor. Cuando Brix tenga roadmap, se cargan allí con la trazabilidad `CR-n → <ID nuevo>` y este documento queda como antecedente. Hasta entonces, este es su único lugar editable.

## Objetivo y regla

Llegar a la revisión con evidencia que responda a las reservas escritas en la excepción. No se trata de sumar los 2 puntos que faltan para llegar a 60. Cada pedido nombra el defecto que ataca. Si la reevaluación sigue por debajo de 60, la decisión vuelve a ser tuya, con las mismas reglas de lectura.

## Pedidos

| ID | Pedido | Defecto o reserva que ataca | Depende de | Costo |
|---|---|---|---|---|
| CR-1 | Corrida de verificación del consejo sobre un documento real, con criterios fijados antes de correr | La corrección `ce392b1` sin reverificar; `automatedVerification` 20 | Tu autorización de documento, pregunta, destino y tope | 11 invocaciones; en la etapa 2, de 102 a 159 mil tokens de salida por corrida completa; dinero `not_measured` |
| CR-2 | Verificador del reporte: script que valida un reporte de consejo contra el contrato de salida de SKILL.md | Sin verificación automatizada; carga manual del orquestador (`operatingOverhead` 45) | Aprobar su diseño (VCX-P3) | Esfuerzo de una sesión; sin consumo de modelo |
| CR-3 | Versión declarada de la skill y política de tags | `versioningDiscipline` 20 | Decidir si VCX usa tags antes del primer push (VCX-D032, historial reescrito a noreply) | Bajo |
| CR-4 | Decidir cómo medir la adopción | `observedAdoption` sin dato | Ninguna para decidir; para implementar, la opción elegida | Bajo para decidir |
| CR-5 | Reevaluar con el envoltorio y decidir | Vencimiento de la revisión | CR-1 a CR-3 hechos o declarados fuera; tu autorización de corrida persistida | Sin consumo de modelo |

Quedan fuera, como dependencias declaradas: CI y escaneo de secretos (`securityHygiene` 35) dependen de que exista el repositorio en GitHub; un segundo host o familia de modelo depende del runner `command`, reservado para otra versión. Si VCX se publica antes de CR-5, VCX-D033 decisión 3 obliga a declarar su `sourceUrl`, y `community` y `maintenance` puntuarán un repositorio nuevo: eso probablemente baja el total y se acepta.

### CR-1 · Corrida de verificación

Criterios a fijar en su plan antes de correr, además de C1 a C7, C9 y C10 de la [etapa 2](2026-11-01-council-stage2-run-plan.md). V3 reemplaza a C8; C11 a C16 corresponden a fixtures y fallos inducidos:

- V1: cada consigna pide no usar el contexto del host y declarar si estaba presente, y el reporte registra esa declaración por asiento.
- V2: ninguna respuesta de asesor empieza nombrando su asiento; si alguna lo hace, el recorte aparece junto al mapeo.
- V3: el reporte tiene el conteo de palabras por asiento frente a su límite, contado con herramienta; un exceso no causa recorte ni reintento.
- V4: los revisores reciben la pregunta 4 reformulada y no reciben el documento; la síntesis declara que es el único asiento que verifica hechos.

V1 a V4 se verifican con herramienta sobre las transcripciones y el reporte, como en la etapa 2. La corrida cuenta también como un uso real para `observedOutcome` solo si el documento y la pregunta son de trabajo vigente y no un fixture.

### CR-2 · Verificador del reporte

Propuesta mínima: un archivo Python de biblioteca estándar, ejecutado con `python3 -I`, dentro de la carpeta de la skill para que viaje con ella. Comprueba:

- las claves del frontmatter y la primera línea;
- las secciones obligatorias, el mapeo ausente en un reporte `partial` y la tabla de conteo de palabras;
- el `run_hash`, recalculado con la receta de SKILL.md a partir de las entradas declaradas.

No reproduce el texto de SKILL.md: valida la salida de una corrida.

Alternativa más simple: una lista de control manual en SKILL.md, que no mueve `automatedVerification` y mantiene la carga del orquestador. Contra la propuesta: agrega código a una skill que hoy es solo Markdown y cambia `dependencySimplicity` (requiere Python 3).

Prueba posterior: debe aceptar los dos reportes completos y el parcial de la etapa 2 tal como están. Los de la etapa 2 se generaron con la revisión anterior de la skill, así que se registra qué controles nuevos no cumplen en vez de corregirlos. Debe rechazar copias alteradas de esos reportes: falta una sección, mapeo en un parcial, `run_hash` distinto.

### CR-3 · Versionado

Opciones para decidir:

1. Clave `version` en PROVENANCE.md y un tag anotado `brix-llm-council/v0.1.0` en VCX.
2. Solo la clave, sin tags hasta extraer Brix a su repositorio.

La 1 es la única que el motor puede leer como disciplina de versiones. Publica un tag en cuanto VCX se suba a GitHub. Prueba posterior: `git describe --match 'brix-llm-council/*'` resuelve la revisión evaluada.

### CR-4 · Medición de adopción

Opciones:

1. Contar los reportes de consejo en VCX con `git ls-files` sobre el patrón de nombre de la salida, solo para este consumidor.
2. Que la skill agregue una línea por corrida a un registro de uso.
3. Dejar `observedAdoption` sin dato y declararlo.

La 2 agrega una escritura a la skill y cambia su perfil de riesgo; la 1 no descubre rutas fuera de VCX. Prueba posterior: el número coincide con el conteo manual de reportes `complete` y excluye los fixtures sintéticos.

### CR-5 · Reevaluación

1. Nueva evidencia en el scratchpad con `evaluatedRef` en el último commit de la carpeta.
2. Correr `node brix/tooling/score-run.mjs evaluate` con `--dry-run`, informar el resultado y pedir decisión.
3. Solo con autorización, la corrida persistida con `--replace-decision`. Esa corrida archiva la `approved_with_exception` vigente y deja el registro en `decision_pending` hasta tu `decide`, así que se hace en una misma sesión, sin pausa entre los dos comandos.
4. Commit en VCX y regeneración de la vista.

Prueba posterior:

- `score-runs.jsonl` gana dos líneas y cada archivo nuevo en `history/` tiene la suya.
- El precursor queda igual.
- La vista muestra la nueva decisión y su fecha de revisión.

## Orden y calendario propuestos

CR-3 y CR-4 son decisiones baratas y pueden tomarse en cualquier momento. CR-2 va antes que CR-1, para que la corrida de verificación ya se valide con el script. CR-1 requiere autorización de consumo. CR-5 entre el 2026-11-25 y el 2026-12-02. Si para el 2026-11-25 no hay autorización de CR-1, CR-5 se hace igual con la evidencia disponible, o la revisión se pospone con una nueva fecha registrada como decisión tuya. No se deja vencer sin registro.

## Qué no autoriza este plan

Nada de lo anterior. Cada pedido necesita su propia aprobación: el diseño de CR-2, la decisión de CR-3 y CR-4, el consumo de CR-1 y la corrida persistida de CR-5.
