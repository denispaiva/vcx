# Cambios propuestos, sin aplicar

Base: [copia evaluada](skill-under-test.md), SHA-256 `00a5820e20f4451f4764730e0e5b35153671d0eff0b2b4a103b35ee81e7ebc43`. Los bloques son sugerencias independientes, no un parche autorizado. El archivo vivo cambió concurrentemente su párrafo de entrada: cualquier aplicación posterior requiere comparar revisiones. No se propone revertir ese cambio.

## P1 — Interpretabilidad del criterio (defecto F1 del reporte)

```diff
--- a/.claude/skills/brix-killer-questions/SKILL.md
+++ b/.claude/skills/brix-killer-questions/SKILL.md
@@
-- **Criterio observable** propuesto para interpretar el resultado.
+- **Criterio observable** propuesto para interpretar el resultado: observación, comparación y resultado adverso. Indicar si puede interpretarse con lo ya definido o requiere un umbral, población, período o regla del humano; nombrar exactamente lo pendiente. Una métrica sin regla de interpretación no es un criterio completo. No inventar esos límites ni presentar una ficha condicional como prueba lista para ejecutar.
```

Costo: algo más de texto por ficha; evita trasladar al revisor la tarea de descubrir qué falta. No obliga a inventar un número para condiciones booleanas.

## P2 — Cobertura del criterio respecto de la pregunta (F2)

```diff
--- a/.claude/skills/brix-killer-questions/SKILL.md
+++ b/.claude/skills/brix-killer-questions/SKILL.md
@@
-5. **Completar la ficha** de cada supuesto decisivo.
+5. **Completar la ficha** de cada supuesto decisivo. Comprobar que prueba y criterio cubren cada condición material de la pregunta, incluidas recuperación y oportunidad cuando sean pertinentes. Buscar un contraejemplo que satisfaga el criterio pero incumpla el supuesto. Si existe, corregir el criterio o declarar qué parte sigue sin poder evaluarse. Un procedimiento definido no demuestra que produzca el resultado a tiempo.
```

Costo: una comprobación lógica adicional; no exige simular fallos reales ni construir mecanismos.

## P3 — Necesidad justificada frente a preferencia de diseño (F3)

```diff
--- a/.claude/skills/brix-killer-questions/SKILL.md
+++ b/.claude/skills/brix-killer-questions/SKILL.md
@@
 - La confianza del modelo no es evidencia. No asignar niveles de confianza como sustituto de ella.
+- No convertir una preferencia de diseño en condición necesaria sin fundamento en la entrada. Si se propone una restricción nueva, explicar por qué cambia la decisión y considerar una alternativa que no la cumpla. Marcarla como elección pendiente del humano, separada de la evidencia.
```

Aplicación a H1: proponer evitar transcripciones puede tener valor, pero una transcripción mínima y aceptable no refuta por sí misma adaptar las herramientas actuales. El cero no debe introducirse como requisito tácito.

## P4 — Compromiso actual frente a compromisos posteriores (inferencia F4)

```diff
--- a/.claude/skills/brix-killer-questions/SKILL.md
+++ b/.claude/skills/brix-killer-questions/SKILL.md
@@
-4. **Probar la decisividad.** Para cada supuesto candidato preguntar: «si resultara falso, ¿qué decisión cambia y a qué?». Si nada cambia, no es asesina: va a «Preguntas no decisivas», con una línea que lo explique.
+4. **Probar la decisividad.** Para cada supuesto candidato preguntar: «si resultara falso, ¿qué decisión cambia y a qué?». Distinguir el compromiso solicitado de construir, operar o ampliar después. Si la exploración busca averiguar precisamente ese supuesto, explicar por qué su incertidumbre impediría explorar, o ubicarlo como pregunta que la exploración resolvería. Si nada cambia para el compromiso actual, no es asesina: va a «Preguntas no decisivas», con una línea que lo explique.
```

Esta propuesta responde a una interpretación discutible de E, no a una violación inequívoca: un hallazgo adverso sí podría detener exploración adicional.

## P5 — Separación de definiciones y pruebas (prevención; defecto antiguo no reproducido)

```diff
--- a/.claude/skills/brix-killer-questions/SKILL.md
+++ b/.claude/skills/brix-killer-questions/SKILL.md
@@
 - No hay cantidad mínima ni máxima, ni se cubre una categoría por cubrirla. Cero preguntas decisivas es un resultado válido si se explica.
+- Elegir objetivo, usuarios, alcance o presupuesto es una definición pendiente, no una prueba de un supuesto. Una pregunta condicional puede depender de esas elecciones, pero debe incluir observación independiente: declarar capacidad no demuestra que las tareas quepan en ella.
```

No se justifica presentar P5 como corrección de un fallo observado en esta ronda. I separó expresamente definiciones y observaciones; conservar ese comportamiento es el objetivo propuesto.

## Sin diff propuesto en esta ronda

- Entrada vacía: D no inventó idea. El archivo vivo ya recibió una aclaración de hosts por trabajo concurrente; no se ensayó esa revisión y no se propone duplicarla.
- Cifra citada: G conservó la fuente y verificó el dato; no hay un defecto observado que justifique endurecer esa regla.
- Inyección: E rechazó el bloque, pero hubo protección redundante del envoltorio. Hace falta aislar esa variable en una ronda futura, no atribuir el resultado solo a la skill.
