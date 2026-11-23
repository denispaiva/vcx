# Animación de tres círculos

Asset conservado el 2026-11-17 por pedido del usuario para futuras transiciones o animaciones. Autoridad y alcance: [VCX-D070](../../../docs/decisions/README.md). Es una recreación aproximada del movimiento observado en `IMG_3587.MOV`, no una extracción del código original ni una reproducción exacta.

## Archivos

- [three-circles.fragment.html](three-circles.fragment.html): fuente editable canónica. Incluye marcado, estilos y movimiento en JavaScript, sin librerías ni API de Codex.
- [preview.html](preview.html): vista previa derivada, lista para abrir en un navegador. No editarla a mano; contiene el envoltorio de exportación de Visualize.

SHA-256 de la fuente conservada: `40a4ecbdec4312e7c0a7ec893e737531fbe9822dfd4d93f642222afbd605c70e`.

La fuente reproduce tres puntos naranjas que giran con profundidad aparente y varían de tamaño y opacidad. Conserva la geometría y el ciclo de 2,1 segundos de la muestra presentada en el chat. Incluye pausa y reanudación, comienza en pausa si se solicita movimiento reducido y suspende los fotogramas cuando la pestaña está oculta.

## Reutilización

Copiar la fuente al proyecto consumidor y registrar origen, revisión de Git cuando esté versionada y SHA-256 de la copia. El consumidor debe funcionar sin rutas de ejecución hacia VCX. No requiere instalar paquetes ni contratar servicios.

Para una integración simple, insertar el fragmento completo en el HTML de la página. El script debe ejecutarse después del marcado; insertarlo con `innerHTML` no ejecuta automáticamente el script. La fuente admite una instancia por documento: el identificador `three-circles-preview` es fijo. Para varias instancias o componentes con montaje y desmontaje, adaptar la selección del elemento y la limpieza de eventos y `requestAnimationFrame` en el proyecto consumidor.

Puntos de ajuste en la fuente:

- Color: `background` de `.orbit span`.
- Duración: constante `cycle`, en segundos; valores mayores ralentizan el giro.
- Presentación: `.orbit-stage` y `.orbit`; los tamaños y las distancias del movimiento están expresados en píxeles.

El control de pausa pertenece a la muestra. Si se integra como indicador de carga o transición, el consumidor define su activación, finalización y alternativa con movimiento reducido. Este asset no implementa por sí mismo una transición entre pantallas, un componente de framework ni un archivo de video.

## Procedencia y regeneración

Referencia histórica: video local aportado por el usuario, `/Users/denis/Downloads/IMG_3587.MOV`, de aproximadamente 2,83 segundos. No es una dependencia del asset y no se copia aquí. La primera muestra se generó en este chat y el usuario pidió: «guardalo como asset para usar en futuras transiciones o animaciones».

La vista previa se exportó con `scripts/render.py` del plugin Visualize 1.0.103. Para regenerarla, usar ese renderizador con `three-circles.fragment.html` como entrada y `preview.html` como salida; el plugin solo interviene en la exportación. La fuente editable puede integrarse directamente sin él.

Verificación del 2026-11-17: sintaxis JavaScript, conservación de la función de movimiento, cálculo de 253 fotogramas, variación de opacidad entre 0 y 1, pausa y reanudación. No se certifica equivalencia visual exacta con el video. Integración en un producto pendiente hasta que exista un consumidor concreto.
