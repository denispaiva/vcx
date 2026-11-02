# Revisión del historial de `vcx` antes de publicarlo

Fecha: 2026-11-01. Motivo: el usuario eligió «Público, revisar antes» para la visibilidad con la que nace `denispaiva/vcx`, conforme a VCX-D032, que exige revisar la dirección de correo y las rutas locales del historial. Lecturas de solo lectura sobre `main` en `6934489` y sobre el árbol de trabajo; no se creó ningún repositorio ni se reescribió historia.

Etiquetas: [H] hecho medido; [I] interpretación; [P] propuesta.

## Hallazgos

| Tema | Evidencia [H] | Lectura [I] |
|---|---|---|
| Correo en metadatos | Los 49 commits de `main` tienen autor y committer `denispaiva` con su dirección personal de correo. Los trailers solo citan `noreply@anthropic.com` | Publicar el historial tal cual publica el correo en cada commit. El perfil de GitHub de la cuenta no expone correo público, lo que sugiere que hoy se mantiene privado. Si la cuenta tiene activo el bloqueo de pushes que exponen el correo, el push sería rechazado; ese ajuste no se pudo leer con el token actual |
| Correo en documentos | Una mención, en la nota de autorización del commit base del [registro](../../decisions/README.md); entró en un solo commit | Se puede quitar del árbol hacia adelante, pero sigue en el historial |
| Rutas locales | 37 rutas absolutas en 14 archivos rastreados: 24 con `/Users/denispaiva` y 13 con `/Users/denis`; 9 commits las tocaron. Concentradas en `docs/sources.md` y planes del 2026-10-30 y 2026-10-31 | Revelan dos nombres de usuario de macOS y la organización de carpetas; riesgo bajo. Son procedencia histórica declarada |
| Inventario de controles | El [inventario](../../architecture/security-controls-inventory.md) describe la compuerta de secretos inactiva del precursor, los scopes del token de la CLI, la ausencia de respaldo de la raíz y una credencial automática no inventariada | Publicarlo expone un mapa de debilidades. Ninguna da acceso remoto por sí sola: todas requieren acceso a la máquina o a la cuenta. Riesgo medio-bajo, mientras sigan sin corregir |
| Proyectos privados | 11 archivos nombran Teyst, Melquisedec, Salmanazar o Pinot Index | Revela su existencia y la estructura del portfolio, no su código. VCX-D032 ya lo admitió al proponer `vcx` público |
| Secretos | Ninguna coincidencia en todo el historial para patrones de tokens de GitHub, Anthropic, OpenAI, AWS, Google, Slack, JWT, claves privadas ni asignaciones de `password` o `secret`. Las cadenas hexadecimales largas son SHA-256 de procedencia | Búsqueda por expresiones regulares, no un scan: `gitleaks` y `trufflehog` no están instalados |
| Importes | Ninguno en el árbol actual | Coincide con la medición de VCX-D032 |
| SHA citados | 14 SHA de commits de `vcx` aparecen en documentos rastreados; `f47c71f` en 12 archivos | Reescribir el historial cambia los 49 SHA y deja esas citas apuntando a commits inexistentes en el público |

## Alternativas

| Opción | Qué implica | Costo |
|---|---|---|
| A. Publicar el historial tal cual | Push de `main` sin cambios; las citas de SHA siguen válidas | Expone el correo en 49 commits, las rutas y el inventario de controles. Puede chocar con el bloqueo de correo de la cuenta |
| B. Reescribir antes del primer push | Reemplazar el correo por la dirección `noreply` de GitHub en los 49 commits, mientras no hay remoto; opcionalmente quitar el correo del registro en todas las versiones | Cambian los 49 SHA: hay que actualizar las citas en documentos con una tabla de correspondencia, y ninguna otra sesión puede commitear en esta raíz durante la reescritura. El criterio de no reescribir historia de VCX-D031 rige para el precursor; aquí no hay clones ni remoto, pero la reescritura sigue siendo irreversible una vez publicada |
| C. Público con historial nuevo | Un commit inicial con el árbol revisado, como B' de VCX-D032 | El historial local y el público divergen para siempre; la raíz no puede empujar a los dos. Pierde el sentido de publicar el repositorio actual |

[P] Recomendación: B, si el correo debe seguir privado, que es lo que sugiere el perfil; A, si no importa. En ambos casos: configurar desde ya la dirección `noreply` para los commits nuevos de la raíz, quitar el correo del texto del registro hacia adelante y correr un scan real antes del push. El inventario de controles puede quedar público: describe controles a corregir, no credenciales, y moverlo exigiría reescribir de todos modos. C no se recomienda.

## Límites

No se leyó la configuración de privacidad de correo de la cuenta ni se ejecutó un scanner dedicado. Los cambios sin commit del árbol de trabajo entrarán al historial que se publique y deberán revisarse con el mismo criterio antes del push.
