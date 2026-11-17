# Piloto B: resultado

Fecha: 2026-11-16. Estado: **ejecutado; resumen público.** Lo pidió el PO en el chat de Claude Code («ejecuta el piloto B»), según el [diseño](pilot-design.md). El protocolo, los hallazgos, la llave y la puntuación quedan en la copia privada `solera/docs/initiatives/web-rules-pilot-2026-11-16/`. Este resumen no reproduce código ni textos del proyecto (VCX-D032).

## Qué se hizo

- **Caso:** un artboard HTML de diseño de Teyst, sorteado entre 19.
- **Revisión:** dos subagentes `sonnet` lo revisaron solo leyendo. Uno usó `design:accessibility-review` (`anthropics/knowledge-work-plugins@c71b6f3`, aprobada el 2026-11-16). El otro, las reglas de `vercel-labs/web-interface-guidelines` fijadas en `434b7f9` y sin red.
- **Puntuación:** otro subagente, con las listas bajo etiquetas neutras, clasificó cada hallazgo contra el código y lo emparejó con el de la otra lista.

## Resultado

| | Accesibilidad | Reglas fijadas |
|---|---|---|
| Hallazgos | 12 | 16 |
| Incorrectos | 0 | 0 |
| Correctos únicos de severidad media o mayor | — | 1 |
| Choques con el español | — | 0 |

- **Regla:** las reglas pasaban a documento de Brix con al menos 3 hallazgos correctos únicos de severidad media o mayor y como mucho 25 % de incorrectos. Aportaron 1, así que **se archivan como antecedente**.
- **Superposición:** los cinco problemas de severidad alta los encontraron los dos brazos.
- **Lo propio de las reglas:** la falta de estilos de foco y varios detalles de severidad baja (imágenes, rendimiento, tipografía y vocabulario).

## Límites

- **Un solo caso,** y es un mock de diseño, no código en producción.
- **Un solo puntuador,** y la ceguera fue parcial: una lista cita criterios WCAG. El operador comprobó a mano tres afirmaciones.
- **Costo:** 269.542 tokens. El PO amplió el tope de 200.000 a 300.000 después del primer brazo, antes de ver los resultados del segundo.
