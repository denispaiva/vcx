# mattpocock-grilling: evaluación en seco

Fecha: 2026-11-21, con `--now 2026-11-21T15:00:00Z`.

Estado: **rechazada.** Primero se hizo la evaluación en seco. Después, el 2026-11-22T02:08Z (21/11 en UTC−3), se corrió la formal ([`mattpocock-grilling.formal.evaluate.out`](mattpocock-grilling.formal.evaluate.out)), con el mismo puntaje, y se registró la decisión del Owner en [`docs/tooling/evaluations/mattpocock-grilling.evaluation.json`](../../../tooling/evaluations/mattpocock-grilling.evaluation.json). No se instaló la skill.

**Quién la hizo.** Claude Code con `claude-opus-5-5`, a pedido del usuario («Sí, evaluarla»), después de descartar `grill-with-docs` completa. El autor de la evidencia es el mismo que la puntuó. No hubo revisión independiente.

**Motor.** Brix `591c25f`, `cliTree` `af14043f`, política `ce6e1a31…`. La comunidad se tomó con token y quedó disponible.

## Candidata

| Origen | Ref | Tipo |
|---|---|---|
| [mattpocock/skills](https://github.com/mattpocock/skills), `skills/productivity/grilling/` | `d1478fcb140db0b93c0c8df17bcfd311844749d0` (release `v1.3.2`, 2026-10-29) | `skill` |

Es un `SKILL.md` de 2.077 bytes y un `agents/openai.yaml` de metadatos para Codex. El último cambio de la skill, `7739eae`, entró en ese release.

Se evalúa sola. `grill-with-docs` la combina con `domain-modeling`, que escribe `GLOSSARY.md` y `docs/adr/` en rutas fijas. En Teyst eso choca con `docs/decisions/` (ADR 0001 a 0015) y con el vocabulario de `AGENTS.md`, y por eso quedó fuera.

## Archivos

| Archivo | Qué es |
|---|---|
| [`mattpocock-grilling.evidence.json`](mattpocock-grilling.evidence.json) | Evidencia de los 23 subfactores; `observedOutcome` queda `unavailable` |
| [`mattpocock-grilling.dry-run.out`](mattpocock-grilling.dry-run.out) | Salida completa de `node docs/tooling/score-run.mjs evaluate … --dry-run` |

## Resultado

| Medida | Valor |
|---|---|
| Score general | 67,9 / 100 |
| Confianza | high (95) |
| Riesgo | low: `scopedLocalReadOnly` |
| Recomendación base | `advance_with_reservations` |
| Factores | comunidad 73,9 · mantenimiento 69,0 · seguridad 77,0 · encaje 54,9 · ingeniería 50,8 · sostenibilidad 87,8 |

## Lectura del operador

**Lo que suma:** es solo texto, sin dependencias, sin escritura de archivos y sin red. Tiene release con notas por PR y se retira borrando un archivo. Su aporte sobre VCX-P2 es un método concreto:

- preguntar en una ronda todas las decisiones cuyos prerrequisitos ya están resueltos;
- dar una recomendación por pregunta, redactada para que «sí» la acepte;
- no preguntar hechos que se pueden averiguar;
- no actuar hasta que el usuario confirme.

**Lo que resta:**

- La cola de issues casi no se atiende: 96 abiertos y 14 cerrados en 30 días.
- No hay pruebas del comportamiento de la skill.
- Un solo autor firma 91 de 105 commits.
- No hay uso medido en VCX.

**Reservas para un uso en Teyst:**

1. Fijarla a `d1478fc` y revisar el diff de la carpeta antes de cada actualización.
2. Pedirle en cada uso que responda en español y que resuelva el vocabulario contra `AGENTS.md` y `docs/decisions/`.
3. Usarla solo a pedido, en decisiones materiales; en un cambio chico y reversible manda VCX-P4.
4. Mientras no esté `active`, no reemplaza a VCX-P2: es una forma de cumplirla.

**Nota orientativa:** 7/10. Le resto por el encaje parcial (en inglés y en parte cubierta ya por política) y por la falta de verificación del comportamiento.

## Decisión

El Owner la rechazó en el chat con «Rechazarla», ante la recomendación de diferirla. Después de esta evaluación se encontraron dos cosas que le restan encaje, más allá del puntaje:

- **El ingreso de Blends ya tiene rondas.** `brix/docs/idea-intake.md` las define: preguntas asesinas más respuestas, con un mínimo de 2, un tope de 3 y un control de madurez. Lo que falta es el instrumento `brix-killer-questions`, que no tiene admisión.
- **Dos reglas de la skill no sirven para un ingreso.** Lo objetó la [revisión independiente de Codex](../2026-11-21-superpowers-brainstorming-codex-review/README.md): redactar cada pregunta para que «sí» acepte la recomendación favorece la aquiescencia, y despachar un subagente por cada hecho es caro.

Se reevalúa solo si un piloto del ingreso muestra que faltan rondas mejor ordenadas. El motivo completo está en `humanDecision.rationale`.
