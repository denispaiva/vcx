# Piloto A: resultado

Fecha: 2026-11-16. Estado: **ejecutado; resumen público.** Lo autorizó el PO en el chat de Claude Code («Sí, piloto A»), según el [diseño](pilot-design.md). El protocolo congelado, las salidas y la llave del sorteo quedan en la copia privada `solera/docs/initiatives/ui-design-pilot-2026-11-16/`. Este resumen no reproduce código, rutas ni textos del proyecto (VCX-D032).

## Qué se hizo

- **Caso:** una pantalla de producto de Teyst pendiente de diseño, la única del flujo sin artboard.
- **Brazos:** seis corridas con subagentes `sonnet`, tres por brazo. El control recibió brief, tokens, ejemplo de formato y checklist v1. El otro brazo recibió lo mismo más el texto de `frontend-design` fijado en `anthropics/skills@e4bb5d9`, sin instalar nada.
- **Medidas:** adherencia a tokens con un script, piso de calidad en el navegador a 320, 420 y 1280 px (el chequeo se validó antes con un contraejemplo) y preferencia del PO en tres pares ciegos.

## Resultado

| Condición de la regla | Control | Con skill | ¿Cumple? |
|---|---|---|---|
| Preferencia del PO, al menos 2 de 3 | 0 | 3 | Sí |
| Mediana de valores fuera de tokens, no peor | 47 | 31 | Sí |
| Piso de calidad, 6 ítems | 6/6 en las tres corridas | 6/6 en las tres corridas | Sí |
| Costo mediano por corrida, hasta 1,5 veces | 132.036 tokens | 135.704 tokens (1,03) | Sí |

**`frontend-design` pasa a evaluación formal:** se prepara una evaluación persistida con `observedOutcome` respaldado, para decisión del PO. No se instala nada por este resultado.

## Límites

- **Tope excedido:** la generación costó 809.734 tokens, el doble de los 400.000 del diseño. La estimación previa fue de 40 a 60 mil por corrida, y las seis se lanzaron en paralelo sin medir antes una. Por regla, se omitió la puntuación por modelo.
- **Muestra chica:** tres pares. Sin diferencia real, 3 de 3 saldría una vez de cada ocho.
- **El piso no discrimina:** todo pasó en los dos brazos. Lo que separó a los brazos fue la preferencia del PO y, en menor medida, el espaciado.
- **Sin puntuador independiente:** las medidas objetivas son scripts fijos, corridos por el operador, que conocía la llave.
- **Alcance:** un artboard HTML no prueba la implementación en React Native.
