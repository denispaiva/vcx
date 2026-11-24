# Caso A: revisión ciega

**Revisor:** subagente `opus` nuevo, que no sabía que había dos ramas ni qué herramienta se probaba. Recibió el brief y, por cada entrada, `screen.png` (390 × 844 a 2×) y `screen.html` sin comentarios.

**Consumo:** 120.273 tokens, 52,6 s, 10 llamadas a herramientas.

La correspondencia entre identificadores y corridas se guardó en [`blind-mapping.json`](blind-mapping.json) antes de la revisión, y se abrió después.

## Puntajes

Puntajes del revisor, de 1 a 5, y su orden, sin empates. Las columnas «Corrida» y «Rama» se agregaron al abrir el ciego.

| Entrada | Corrida | Rama | Jerarquía | Claridad | Calidad visual | Ajuste al brief | Accesibilidad aparente | Total | Posición |
|---|---|---|---|---|---|---|---|---|---|
| D5 | S3 | con skill | 4 | 4 | 5 | 5 | 4 | 22 | 1 |
| D6 | S2 | con skill | 4 | 5 | 3 | 5 | 4 | 21 | 2 |
| D4 | N2 | sin skill | 4 | 4 | 4 | 5 | 4 | 21 | 3 |
| D3 | N3 | sin skill | 4 | 4 | 4 | 5 | 3 | 20 | 4 |
| D2 | N1 | sin skill | 4 | 4 | 4 | 5 | 3 | 20 | 5 |
| D1 | S1 | con skill | 3 | 3 | 2 | 5 | 3 | 16 | 6 |

El revisor desempató los totales iguales (D6 con D4, D3 con D2) por defectos de construcción y semántica.

## Motivos del revisor, resumidos

- **D5 (S3), 1.º** Es la única con carácter propio: fondo de pegboard, slab serif, contornos con sombra desplazada y herramientas ilustradas. Tiene la mejor semántica:
  - `input type=search`;
  - categorías con `aria-pressed`;
  - `aria-current` en la pestaña activa;
  - estilos `focus-visible`;
  - disponibilidad indicada también por la forma del punto.

  Pierde puntos porque el botón flotante tapa datos de la cuarta tarjeta.
- **D6 (S2), 2.º** Es la más clara y sin defectos: un banner para prestar herramientas y una semántica sólida. Su aspecto es correcto pero genérico.
- **D4 (N2), 3.º** Es más distintiva que D6. Pierde puntos porque el botón flotante tapa una insignia y porque «See all» es un `<a>` sin `href`.
- **D3 (N3), 4.º** Pulida y cálida. Usa `div` y `<a>` sin `href` para las pestañas, las categorías y la acción principal, y sus íconos no están ocultos para lectores de pantalla.
- **D2 (N1), 5.º** Es casi igual a D3 pero más apagada, y la menos semántica salvo D1.
- **D1 (S1), 6.º** Es un buen concepto con la construcción rota:
  - las categorías, los nombres y el botón principal salen con el estilo por defecto de los enlaces, azul y subrayado;
  - el atajo `font` del botón es inválido;
  - el banner rompe el flujo de buscar y después explorar.

## Parecidos que señaló el revisor

- **D2 y D3, las dos sin skill, son casi duplicados:** tienen la misma estructura, las mismas pestañas y valores de CSS casi iguales.
- **D1 y D6, las dos con skill,** comparten el concepto de un banner verde para prestar herramientas.
- **D4 y D5, una de cada rama,** comparten las pestañas y los puntos redondos y cuadrados.
- **Las seis convergen en una paleta:** crema, verde pino y naranja quemado.
