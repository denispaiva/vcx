# VCX · recursos de marca

El usuario aprobó la redacción, el encabezado y la preparación de isotipos individuales e integración para publicar en hello.tintum.app el 2026-11-11. Estas piezas derivan de la [lámina elegida](proposals/2026-11-11/wine-family-v2.png), mediante ImageGen integrado. Conservan símbolos y paletas; son recreaciones individuales, no recortes exactos de píxeles.

Los PNG conservan transparencia exterior y el fondo coloreado de cada baldosa. Usarlos acompañados del nombre del producto. No son versiones vectoriales ni monocromas. Las variantes para tamaños pequeños quedan fuera de esta entrega.

| Identidad | Archivo | Tamaño | SHA-256 |
|---|---|---|---|
| vcx | [vcx-symbol.png](vcx-symbol.png) | 1254 × 1254 | `ac3ee8e36c58cd107406b9de83375e2a73c472f7f40e707daaea4f603a90697c` |
| cellar | [cellar-symbol.png](cellar-symbol.png) | 1254 × 1254 | `ad46bf9b0aac0ea7e98182215d1a0b955bb22ca4f56a64a0eefd00b1ff07e353` |
| blends | [blends-symbol.png](blends-symbol.png) | 1254 × 1254 | `cf62503a28a5946d78ff55163b3dc785c6d90c5b28b193589513a91e408f6ebc` |
| brix | [brix-symbol.png](brix-symbol.png) | 1254 × 1254 | `875f7ac5a99197e03a3a3c11d79e68df6a04b19a9e14ebaef7f60b550ede7cce` |

Fuentes editables: [redacción pública](product-copy.md) y [justificaciones de marca](brand-rationale.md). El sitio incorpora copias propias sin depender de rutas de este workspace.

## Prompt de producción

Para cada pieza se usó la lámina v2 como referencia y el siguiente prompt, sustituyendo SUBJECT por `VCX top left grape bunch`, `Cellar top right barrel`, `Blends bottom left liquid swirl` o `Brix bottom right graduated drop`:

> Extract/reproduce ONLY the SUBJECT icon tile from this approved brand board as a single standalone square image. Preserve its original colors, symbol geometry, proportions, tactile satin 3D material and highlights faithfully. Include the colored rounded square tile, centered filling 90% of square canvas. Outside the rounded tile fully transparent. Remove all text/labels, all other tiles and cream board. No redesign, no additions. Production website brand asset.

Parámetro: `transparent_background: true`. Originales conservados en la salida de ImageGen; estas copias son los assets reutilizables del workspace.

## Publicación verificada

Publicado el 2026-11-11 en [hello.tintum.app](https://hello.tintum.app/#vcx), mediante [TintumHero PR 8](https://github.com/denispaiva/TintumHero/pull/8), commit `9b82d0076edb85ad92550e81bdd09ddc992b060b`. Versión Hosting `e8712d0ebefb7a01`, release `1794435363143000` a las `2026-11-11T22:16:03.143Z`. Versión anterior conservada para recuperación: `dc7abc298792fa33`.

Verificación: escritorio 1365 px y móvil 390 px; cuatro imágenes cargadas, sin desbordamiento horizontal móvil, justificación de Cellar expandida y enlaces/anclas locales válidos. Dominio público observado con nuevo encabezado y familia; portada y cuatro PNG del origen Hosting coinciden byte a byte con el commit. Copias de assets idénticas a esta fuente. Servidor y pestañas temporales cerrados.

La publicación usa Firebase Hosting existente, sin modificar permisos, redirecciones ni otras páginas. Las variantes vectoriales/monocromas y para favicon no se produjeron.
