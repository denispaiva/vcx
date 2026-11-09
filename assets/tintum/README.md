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

Ambas imágenes son PNG de 1536 × 1024 px, generadas con ImageGen integrado. Los [prompts originales](prompts.md) conservan la intención de generación; los valores de color allí indicados no equivalen a una paleta uniforme medida en imágenes con textura e iluminación.

## Productos comerciales

Cada producto comercial de Tintum muestra la firma `powered by tintum` (VCX-D061). Los productos se suman a esta lista al decidirlo el usuario; la columna de procedencia registra el archivo y la revisión copiados cuando la integración exista.

| Producto | Desde | Firma integrada | Procedencia de la copia |
|---|---|---|---|
| Teyst | 2026-11-09, el más evolucionado según el usuario | Sí, en `main` desde el 2026-11-09 ([PR 65 de solera-teyst](https://github.com/denispaiva/solera-teyst/pull/65), merge `9622813`); publicada el 2026-11-09 desde `f62c2ea` en `dev-teyst.web.app` ([corrida](https://github.com/denispaiva/solera-teyst/actions/runs/42664075013)) y en el canary `prod-teyst.web.app` ([corrida](https://github.com/denispaiva/solera-teyst/actions/runs/42664813248)); `teyst.web.app` sigue sin la firma; [plan](../../docs/superpowers/plans/2026-11-09-teyst-tintum-signature-plan.md) | Sin copia: firma en texto (ADR 0012 de Teyst) |

## Uso entre proyectos

Esta carpeta es la fuente de los recursos aceptados en VCX. Las salidas de `output/imagegen/tintum-2026-11-09/` son antecedentes de generación. Para usar una imagen en otro proyecto, incorporar una copia al directorio de assets de ese proyecto y registrar su procedencia y revisión; el producto debe seguir funcionando sin depender de una ruta de ejecución hacia VCX.

Los archivos actuales son láminas de identidad con fondo: cada uno reúne logo, ícono y firma. Pueden usarse como referencia visual o como lámina completa. No son todavía un paquete de piezas individuales transparentes, SVG ni favicons; su separación y la verificación a tamaños pequeños quedan pendientes para la integración que las necesite. No se ha modificado ni publicado ningún proyecto consumidor.

La decisión está registrada como VCX-D061 en el [registro de decisiones](../../docs/decisions/README.md), fuente canónica de su autoridad, alcance y pendientes; esta guía no la reemplaza. Por declaración del usuario del mismo día, VCX y todo lo que vive debajo forman parte de Tintum, sin renombrar VCX, VibeOS ni sus productos. La separación en piezas transparentes, SVG y favicons y la validación a tamaño pequeño quedan como pendiente `tintum-brand-kit`. El [prompt de continuidad](claude-registration-prompt.md) conserva el alcance con que se hizo el registro.
