# Capacidad de Brix para preparar propuestas de ideas

Fecha: 2026-10-30. Estado: capacidad requerida para el diseño de VCX; todavía no implementada. El usuario fijó `brix idea` = `/idea` y `brix council` = `/council`. Las equivalencias y la ayuda de parámetros se definen en [comandos de Brix](commands.md).

## Misión de la capacidad

Convertir una explicación en texto o archivo en un documento de idea comprensible para revisión humana, enriquecido mediante preguntas asesinas y preparado para enviarse al consejo.

## Entradas

- Texto directo o archivo Markdown/PDF en el primer alcance.
- Plantilla de ideas y versión explícitas, suministradas por el consumidor.
- Configuración del instrumento de preguntas asesinas, idioma visible y límites de ejecución.
- Ámbito de lectura y destino de salida explícitos; sin asumir un Cellar o rutas de Blends.

`brix idea` y `/idea` reciben texto o archivo; sin parámetro ofrecen ayuda para completarlo. Una entrada ambigua se aclara con el humano, sin adivinar si era texto o ruta. La [ayuda de comandos](commands.md) detalla el comportamiento común; la selección de plantilla y el tratamiento de varios adjuntos se precisarán antes de implementar. Un formato adicional no se declara compatible sin su adaptador.

## Operación

1. Preservar la entrada e identificar las partes extraídas, con referencias a páginas o secciones cuando corresponda.
2. Aplicar la plantilla y distinguir cita original, interpretación propuesta y datos ausentes.
3. Invocar el instrumento de preguntas asesinas: formular preguntas decisivas, exponer supuestos y señalar qué respuestas o evidencia faltan.
4. Producir el documento `.md` con una revisión identificable, listo para la conversación humana. No producir un plan de implementación o una especificación ejecutable por haber completado una plantilla.

Las preguntas no son respuestas; la capacidad no inventa entrevistas, validación de mercado, cifras o autoridad. Los fallos de extracción y las secciones pendientes aparecen en el resultado.

## Instrumento de preguntas asesinas: herramienta candidata

Desde el 2026-11-01 existe una herramienta candidata, [`brix-killer-questions`](../.claude/skills/brix-killer-questions/PROVENANCE.md): adaptación local de una skill MIT de terceros, con procedencia fijada. Aplica el contrato de esta capacidad: lee el contexto antes de preguntar, separa hechos, afirmaciones sin fuente e inferencias, y por cada supuesto decisivo expresa pregunta refutable, decisión afectada y consecuencia, evidencia disponible y faltante con prueba proporcionada, y criterio observable. No asigna semáforo ni clasificación bloqueante (propuestas del [diseño de maduración](../../docs/superpowers/specs/2026-10-31-idea-maturation-design.md), sin aprobar) ni exige MVP.

Estado: candidata sin admisión; probada solo con un caso ficticio ([reporte](../../docs/superpowers/reports/2026-11-01-killer-questions-instrument.md)). No hay comando `brix idea` implementado ni capacidad registrada; la integración con la plantilla de ideas y el flujo queda pendiente.

## Salidas y efectos

- Archivo Markdown basado en la plantilla, con ubicación accesible al consumidor.
- Referencias a fuentes y observaciones de extracción.
- Preguntas decisivas y supuestos, con distinción entre propuestas y confirmaciones.
- Identidad y revisión del proceso de preparación; diagnóstico de resultado completo, parcial o fallido, sin inferir aprobación humana.

La capacidad escribe solo en el destino declarado. No registra la idea en un portfolio, no crea un roadmap y no invoca un consejo sin la autorización del flujo consumidor. Puede utilizarse sin instalar Blends; quien la invoque debe proporcionar plantilla, configuración y permisos necesarios.

## Relación con el consejo

El [flujo de Blends](../../blends/docs/idea-intake.md) recibe el OK humano, informa el envío y consume `brix council` o `/council` con el documento Markdown. Esa capacidad de Brix devuelve un reporte asociado a la revisión de entrada. La aceptación del reporte y el ingreso son decisiones posteriores del humano, no resultados de Brix.

El instrumento de consejo se ofrece desde Brix; Blends conserva la coordinación del proceso. Se mantendrán trazabilidad, límites y controles de repetición al diseñar su adaptación por archivo. El método existente no se modifica ni se extrae en esta etapa documental.

## Diferencia respecto del sistema actual

El `brix idea <archivo.md>` existente convierte notas en `SPEC.md` ejecutable: tiene otro propósito y no satisface por sí solo esta capacidad de ingreso. El `/council <slug>` actual requiere una idea en `ideas/`; la nueva interfaz por archivo debe admitir propuestas todavía no registradas. La [correspondencia](../../docs/architecture/current-system-mapping.md) identifica sus fuentes normativas.

La consulta previa al índice no identificó la formulación inicial `/ideas` ni `/asesinas` como capacidades independientes registradas. Es una observación histórica, no prueba de inexistencia de otros procedimientos. La equivalencia ahora decidida no demuestra que la nueva semántica de `/idea` esté implementada.
