# Propuesta ficticia: caché de respuestas en el CLI de ejemplo

Estado: borrador para prueba de la skill. Documento sintético; no describe ningún producto real de VCX.

## Problema

El CLI de ejemplo consulta un servicio remoto en cada ejecución. Las consultas repetidas con los mismos parámetros tardan entre 2 y 4 segundos y consumen cuota del servicio.

## Propuesta

Guardar las respuestas en un archivo local durante 24 horas, indexadas por los parámetros de la consulta. Una opción `--no-cache` fuerza la consulta remota.

## Restricciones declaradas

- No agregar dependencias nuevas.
- El archivo de caché vive en el directorio del usuario, no en el repositorio.
- Las respuestas con errores no se guardan.

## Supuestos

- Los parámetros identifican por completo la respuesta.
- 24 horas es un plazo aceptable para todos los usuarios.
