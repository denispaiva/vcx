# Instrucciones de {{initiative_name}}

**Material de plantilla, no instrucciones activas del workspace.** Al instanciar, resolver los marcadores, verificar cada referencia desde la nueva ubicación y sustituir este aviso por el alcance real. No asumir una profundidad fija de carpetas.

## Contexto mínimo

Leer `{{initiative_readme_ref}}` para misión, visión, estado y fuentes de trabajo. Consultar las reglas comunes en `{{common_instructions_ref}}` y el perfil adoptado en `{{governance_ref}}`.

Antes de activar esta plantilla en otro repositorio, comprobar que `{{common_instructions_ref}}` es accesible y corresponde a la versión o revisión adoptada. La distribución debe estar resuelta según el disparador para instancias externas de las instrucciones comunes; no dar por válida una ruta local del equipo de origen.

## Contexto según la tarea

- Para planificación, consultar `{{planning_ref}}` y `{{backlog_ref}}`.
- Para cambios de comportamiento o conexiones, consultar `{{architecture_ref}}` y las interfaces públicas de las dependencias declaradas.
- Para autoridad, revisar `{{decisions_ref}}` y el perfil adoptado.
- Para continuar una sesión, consultar `{{handoff_ref}}` y sus evidencias.

Cargar solo el contexto necesario de otras iniciativas. Mantener las fuentes canónicas y la identidad de esta iniciativa al mover o reorganizar documentos.

## Reglas y verificación locales

{{local_rules}}

{{verification_instructions}}

Las reglas locales agregan particularidades dentro del perfil adoptado. No conceden permisos sobre otros proyectos, repositorios o entornos.
