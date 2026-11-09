# Checklist de revisión de experiencia de uso (piloto, v0)

Origen: prompts 9, 14, 23, 29 y 32 del artículo de Chat Smith, con tres correcciones acordadas en VCX (estado de evidencia, recuperación real, nada inventado).

## Antes de empezar

- Anotar la tarea del usuario que se revisa, quién la hace y en qué contexto.
- Listar los materiales recibidos. Revisar solo esos; no buscar otros.
- Declarar qué no puede evaluarse con esos materiales (por ejemplo, foco, lectores de pantalla o tiempos reales cuando solo hay código).

## Recorrido (prompt 9)

1. Describir el camino ideal paso a paso, desde la entrada hasta completar la tarea.
2. Marcar cada punto de decisión y cada punto donde el sistema puede fallar.
3. Señalar pasos que se podrían eliminar.

## Estados excepcionales (prompt 14)

Para cada pantalla del recorrido, recorrer: vacío, cargando, error, sin conexión, primer uso, sin sesión, sin permiso.

4. ¿Qué ve la persona en cada estado? ¿Qué puede hacer?
5. ¿Una sola causa produce una sola señal, o varias señales que compiten o se contradicen?
6. ¿Algún estado muestra información falsa o engañosa (por ejemplo, datos vacíos cuando en realidad no hay acceso)?

## Mensajes de error (prompt 23)

7. ¿Cada mensaje dice qué pasó, por qué importa y qué hacer, en el idioma y el tono de la interfaz?
8. ¿Algún mensaje puede mostrar texto técnico crudo (de un SDK, del servidor o un código HTTP)? Seguir la ruta del error hasta su origen.
9. ¿El mensaje corresponde a lo que la persona intentaba hacer en esa pantalla, o fue escrito para otro contexto?

## Recuperación

10. Cada acción que el mensaje propone (reintentar, iniciar sesión, volver) ¿existe en la pantalla y funciona?
11. ¿Repetir la acción puede duplicar efectos?

## Interacciones y entrega (prompts 29 y 32)

12. Los controles ¿tienen estados de deshabilitado, en curso, error y éxito? ¿Etiquetas accesibles?
13. ¿Quedan preguntas abiertas que el equipo de desarrollo tendría que resolver?

## Formato de cada hallazgo

| Campo | Contenido |
|---|---|
| Ubicación | archivo:línea o pantalla y estado |
| Estado de evidencia | `observado` (se ve en el material), `hipótesis` (inferido, no comprobado) o `no verificable` con este material |
| Evidencia | cita breve del material |
| Consecuencia | qué le pasa a la persona |
| Severidad | alta, media o baja |
| Corrección | cambio concreto |
| Cómo comprobarla | prueba u observación que demuestre la corrección |

Cerrar con lo que no se pudo evaluar y qué evidencia lo resolvería. No inventar usuarios, citas, frecuencias ni métricas.
