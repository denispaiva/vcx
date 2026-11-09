# Pilotos de la checklist de experiencia de uso

Fecha: 2026-11-09. Estado: **resumen público de dos pilotos**. La decisión que los cierra es VCX-D060; no es una admisión.

**Publicabilidad.** `vcx` es público y los proyectos son privados (VCX-D032). Por eso este resumen no reproduce código, rutas, commits ni textos de Teyst. Los informes de los revisores, la puntuación y el detalle completo quedan en la copia privada `solera/docs/initiatives/ux-checklist-pilot-2026-11-09/`, que está fuera del repositorio.

## Origen

El usuario pidió analizar los 35 prompts de UI/UX de un artículo de Chat Smith ([fuente](https://chatsmith.io/es/blogs/prompt/chatgpt-prompts-for-ui-ux-designers-00318)) para ver si alguno podía incorporarse a VCX como capacidad o skill. Ese análisis, contrastado con una revisión de Codex, llevó a un orden de trabajo:

1. Probar primero una checklist sola, sin herramientas, basada en los prompts 9 (recorrido), 14 (estados excepcionales), 23 (mensajes de error), 29 (interacciones) y 32 (entrega).
2. Incorporarle tres correcciones: marcar el estado de evidencia de cada hallazgo, exigir que la recuperación funcione de verdad y no inventar datos.
3. Agregar herramientas o una skill propia (`brix-ux-review`) solo ante una carencia concreta.

Instrumentos: la [checklist v0](2026-11-09-ux-checklist-pilot/checklist.md), congelada durante los pilotos, y la [checklist v1](2026-11-09-ux-checklist-pilot/checklist-v1.md).

## Método común

- **Caso:** un flujo de Teyst con defectos documentados y corregidos. Se compararon dos versiones del mismo flujo: la defectuosa y la corregida, que funciona como control.
- **Revisores ciegos:** dos subagentes `sonnet`, uno por versión, con el mismo prompt. No sabían cuál versión revisaban ni conocían los defectos, y solo podían leer los archivos entregados.
- **Medidas:**
  - detección de los defectos conocidos en la versión defectuosa;
  - defectos ya corregidos que se reportan como presentes en el control;
  - precisión de los demás hallazgos;
  - cumplimiento del formato y límites declarados;
  - consumo.

## Piloto 1: acceso a la sala de espera

Tenía tres defectos documentados:

- un mensaje técnico del SDK, en inglés;
- un texto escrito para otra acción;
- una sola denegación de acceso que producía varias señales a la vez.

| Medida | Control | Defectuosa |
|---|---|---|
| Defectos conocidos | No reportó ninguno como presente | 3 de 3 detectados |
| Hallazgos | 16 | 19 |
| Consumo | 107.598 tokens | 108.232 tokens |

**Clasificación independiente.** La hizo otra sesión, con la regla de corte fijada antes: más del 25 % de refutados cortaba la línea. Agrupó 24 hallazgos únicos, de los cuales 18 quedaron respaldados por el código, 0 refutados y 6 indeterminados. Ocho de los respaldados se comprobaron a mano en dos lecturas. «Respaldado» quiere decir que el código muestra lo que el hallazgo afirma, no que el hallazgo sea importante.

**Límite principal.** La checklist se redactó después de conocer estos defectos, y tres de sus preguntas les corresponden casi una a una. El 3 de 3 no prueba que la checklist generalice.

## Piloto 2: ingreso con código

Corrigió los límites del primero:

- un agente que no conocía la checklist eligió el caso;
- la checklist v0 se usó sin cambios;
- a las dos versiones se les quitaron los comentarios del código, que describían los defectos;
- otro agente puntuó y verificó los 29 hallazgos contra el código.

Tenía cinco defectos documentados:

- una salida bloqueada para un invitado que quería pasar a su cuenta;
- un campo editable mientras una operación seguía en curso, que podía mostrar un código y entrar a otro evento;
- un ejemplo de formato imposible;
- un error de sesión mostrado crudo y en inglés;
- un mensaje que no orientaba a quien chocaba con su propio nombre, el más débil de los cinco.

| Medida | Control | Defectuosa |
|---|---|---|
| Defectos conocidos | No reportó como presentes los cuatro corregidos; el quinto lo marcó como residual, lo cual es correcto | 3 detectados, 1 parcial, 1 sin detectar |
| Correctos / hipótesis bien marcadas / incorrectos | 7 / 4 / 1 | 10 / 5 / 2 |
| Consumo | 80.687 tokens | 80.811 tokens |

- **Lo que nadie vio:** el defecto de la operación en curso. La checklist v0 no tenía ninguna pregunta sobre concurrencia.
- **Hallazgos incorrectos:** los tres son afirmaciones falsas presentadas como observadas.
- **Consumo total del piloto,** con selección y puntuación: unos 424.000 tokens.
- **Límites:**
  - una sola corrida por versión;
  - solo tres de los cinco defectos distinguen una versión de la otra;
  - el material es código de cliente, sin backend ni componentes visuales;
  - el puntuador conocía los defectos.

## Lectura conjunta

- **Detección:** con un instrumento que no estaba hecho a medida del caso, la checklist llevó a detectar 3 de 5 defectos y 1 parcial. Los revisores declararon sus límites y casi no inventaron.
- **La carencia es de contenido:** faltaban preguntas sobre operaciones en curso. Se cubre con el ítem 12 de la v1, que todavía no está probado. No requiere una skill ni herramientas adicionales (VCX-P3).
- **Errores de los revisores:** una pasada que verifique cada afirmación «observada» contra el código habría atrapado los tres. Eso podría justificar más adelante un procedimiento con verificación, pero dos pilotos no alcanzan para mostrar que su beneficio compense el costo.

## Cierre: pendiente con disparador (VCX-D060)

No se crea `brix-ux-review` y la checklist no pasa a Brix. La regla de continuar solo con un consumidor que tenga una decisión pendiente no se cumple hoy.

- **Disparador:** una idea o un proyecto de VCX necesita revisar un flujo o un artefacto con interfaz para tomar una decisión.
- **Al activarse:**
  1. Aplicar la v1 a ese caso.
  2. Compararla con una revisión sin checklist, con criterios fijados antes de medir: detección, precisión, claridad y esfuerzo. Un empate en detección no basta para descartarla.
  3. Decidir el destino de la checklist: documento de Brix o antecedente.
- **Revisión:** 2027-02-09, con el pendiente `ux-checklist-consumer` de [`pending-triggers.json`](../../decisions/pending-triggers.json).
- **Descarte:** si a esa fecha no apareció un consumidor, la checklist se archiva como antecedente.
- **Fuera de este pendiente:** un hallazgo que podría seguir presente en Teyst. Le corresponde a quien conduce ese proyecto, desde la copia privada.
