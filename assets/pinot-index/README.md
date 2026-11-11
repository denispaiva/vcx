# Pinot Index · asset aprobado

Nombre visible: **Pinot Index**. Marca gráfica: **P(index)**, con P de Pinot y notación de función matemática. Aprobación del usuario: 2026-11-11, registrada en [VCX-D066](../../docs/decisions/README.md). Esta es la revisión visual aprobada; no describe una fórmula ejecutable.

## Archivo canónico

- [pinot-index.png](pinot-index.png): PNG de 1254 × 1254 px, con canal alfa, burdeos y crema, letras redondeadas y relieve suave. SHA-256: `5dc9ad3c64c738d5a88d631889d98eda1b76e5dde8f7ef6a6716b70e0ae01e9c`.
- Generado con ImageGen integrado. [Prompt y antecedente](proposals/p-index.md); los otros archivos de `proposals/` son exploraciones, no variantes adoptadas.

## Integración en el sitio

Consumidor autorizado: sección «Productos» de la portada de `hello.tintum.app`, fuente `hello/public/index.html` de [TintumHero](https://github.com/denispaiva/TintumHero). El sitio incorpora una copia byte a byte en `hello/public/assets/pinot-index.png`, con hash y revisión documentados en su README, sin dependencia de ejecución hacia VCX.

La tarjeta identifica Pinot Index como motor de scoring y enlaza la página explicativa existente `/teyst/pinot-index/`. No implica disponibilidad de una aplicación o API independiente. Lleva la firma `powered by tintum` con el recurso ya existente en el sitio.

Estado de entrega: publicada el 2026-11-11 en [hello.tintum.app](https://hello.tintum.app/#h-pinot-index), con autorización explícita del usuario. Fuente desplegada: [PR 5 de TintumHero](https://github.com/denispaiva/TintumHero/pull/5), commit `a344443ffee212d3feab02e06d478e7e703c96cd`. Firebase Hosting: versión `0beddba3d0055c56`, release `1794428835326000`, 20:27:15 UTC (17:27:15 de Córdoba). Se preservaron la configuración y los archivos anteriores; solo cambió la portada y se agregó el PNG. Versión anterior para recuperación: `a914485acaecce16`. Se comprobó la carga del asset, ausencia de desbordamiento horizontal a 320 y 1280 px y navegación del enlace explicativo. Capturas de revisión: [escritorio](evidence/desktop.png) y [móvil](evidence/mobile.png). El PNG aprobado se conserva sin redibujar ni transformar. Legibilidad como favicon, SVG y optimización de peso quedan fuera de esta entrega; no usar esta pieza como favicon por inferencia.

Verificación pública: la tarjeta, el asset de 1254 px y su enlace se comprobaron en el navegador sobre `hello.tintum.app`. Los hashes de portada y PNG en el origen de Hosting coinciden con la revisión local. La terminal recibió HTTP 403 de Cloudflare en el dominio personalizado; la navegación normal funcionó. Despliegue mediante la [API oficial de Firebase Hosting](https://firebase.google.com/docs/hosting/api-deploy) con la sesión existente de Google Cloud, porque Firebase CLI tenía la autenticación vencida. No se crearon credenciales ni se cambiaron permisos.
