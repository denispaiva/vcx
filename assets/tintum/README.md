# Tintum · recursos de marca

Fecha: 2026-11-09. Marca comercial declarada por el usuario para sus proyectos: **tintum.app**. Nombre visible en el logo: **tintum**. Firma: **powered by tintum**.

## Estado y procedencia

El usuario pidió una identidad en la línea de Teyst y luego precisó su preferencia por letras redondeadas y la textura de su falsa nariz. Tras recibir las opciones 2 y 3, respondió: «genial, cerrado eso buscaba, en assets de vcx para poder usarlo en diferentes proyectos y dame el prompt para que Claude registre todo».

Queda aceptada esa dirección visual y se conservan ambas variantes; no hubo elección explícita de una como única principal. La propuesta serif inicial no forma parte de este conjunto aceptado. La referencia exacta de la falsa nariz no se encontró: las texturas son interpretaciones de la descripción del usuario.

## Archivos

| Variante | Archivo | Contenido |
|---|---|---|
| Opción 2 · burdeos sobre crema | [tintum-burgundy-on-cream.png](tintum-burgundy-on-cream.png) | Logo redondeado con acabado gomoso satinado, ícono y firma |
| Opción 3 · crema sobre burdeos | [tintum-cream-on-burgundy.png](tintum-cream-on-burgundy.png) | Logo redondeado con textura mate porosa, ícono y firma |
| Wordmark vectorial | [tintum-wordmark.svg](tintum-wordmark.svg) | Solo la palabra `tintum`, monolínea, en `currentColor`; para la firma y cualquier tamaño |

Las dos láminas son PNG de 1536 × 1024 px, generadas con ImageGen integrado. Los [prompts originales](prompts.md) conservan la intención de generación; los valores de color allí indicados no equivalen a una paleta uniforme medida en imágenes con textura e iluminación.

El wordmark vectorial lo dibujó Claude el 2026-11-11 con [build_wordmark.py](build_wordmark.py) (trazo 19, espaciado 10) y lo aprobó el usuario con «Sí, aprobado» (VCX-D061). Es una interpretación plana de las láminas: conserva la estructura de las letras, no la textura ni el volumen. Toma el color del texto donde se usa (`currentColor`), así que sirve igual en burdeos sobre crema y en crema sobre burdeos. Se revisó a 96, 40, 24, 16, 12 y 11 px sobre crema `#F4EDE0`, burdeos `#5E1B26`, blanco y `#43121B`: se lee en todos. Las letras son trazos, no contornos. SHA-256: `f95f3470…`.

## Productos comerciales

Cada producto comercial de Tintum muestra la firma `powered by tintum` (VCX-D061). Los productos se suman a esta lista al decidirlo el usuario; la columna de procedencia registra el archivo y la revisión copiados cuando la integración exista.

| Producto | Desde | Firma integrada | Procedencia de la copia |
|---|---|---|---|
| Teyst | 2026-11-09, el más evolucionado según el usuario | Sí: en `main` desde el [PR 65 de solera-teyst](https://github.com/denispaiva/solera-teyst/pull/65); con el wordmark SVG desde el [PR 93](https://github.com/denispaiva/solera-teyst/pull/93). Publicada en `teyst.web.app` el 2026-11-11 desde `21c732b` ([corrida](https://github.com/denispaiva/solera-teyst/actions/runs/42946510773)), después del canary ([corrida](https://github.com/denispaiva/solera-teyst/actions/runs/42946146240)); [plan](../../docs/superpowers/plans/2026-11-09-teyst-tintum-signature-plan.md) | Copia del wordmark SVG de VCX en `components/icons/tintum-wordmark.tsx` (vcx `8ac42e5`; ADR 0012 de Teyst) |
| Salmanazar | 2026-11-11, elegido por el usuario entre los candidatos de Solera | Sí: en `main` desde el [PR 1 de solera-salmanazar](https://github.com/denispaiva/solera-salmanazar/pull/1), en Entrar y en la cava; con el wordmark SVG desde el [PR 2](https://github.com/denispaiva/solera-salmanazar/pull/2). Todavía sin sitio público | Copia del wordmark SVG de VCX en `apps/app/components/tintum-wordmark.ts` (vcx `8ac42e5`; ADR 0002 de Salmanazar) |

## Uso entre proyectos

Esta carpeta es la fuente de los recursos aceptados en VCX. Las salidas de `output/imagegen/tintum-2026-11-09/` son antecedentes de generación. Para usar una imagen en otro proyecto, incorporar una copia al directorio de assets de ese proyecto y registrar su procedencia y revisión; el producto debe seguir funcionando sin depender de una ruta de ejecución hacia VCX.

Las láminas reúnen logo, ícono y firma con fondo, y sirven como referencia visual. Para la firma de un producto se usa el wordmark vectorial. El ícono de la «t» y los favicons todavía no existen como piezas separadas.

La decisión está registrada como VCX-D061 en el [registro de decisiones](../../docs/decisions/README.md), fuente canónica de su autoridad, alcance y pendientes; esta guía no la reemplaza. Por declaración del usuario del mismo día, VCX y todo lo que vive debajo forman parte de Tintum, sin renombrar VCX, VibeOS ni sus productos. El ícono de la «t» y los favicons quedan como pendiente `tintum-brand-kit`; el wordmark vectorial ya lo resolvió en parte. El [prompt de continuidad](claude-registration-prompt.md) conserva el alcance con que se hizo el registro.
