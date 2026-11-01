# Procedencia de `brix-killer-questions`

Fecha: 2026-11-01. Estado: herramienta candidata, incorporada con alcance acotado; sin admisión en el inventario del precursor ni uso medido.

## Origen

| Dato | Valor |
|---|---|
| Repositorio | https://github.com/phuryn/pm-skills (autor: Pawel Huryn) |
| Revisión | `2a12295a7717569baa7be181b4cfebe3ca38a6bb` (2026-10-29, posterior a `v2.2.0`; `git describe`: `v2.2.0-4-g2a12295`) |
| Archivo | `pm-product-discovery/skills/identify-assumptions-new/SKILL.md` |
| SHA-256 del original | `962b1e0c01e45ceb930e4d806c0ffb05e36cf25dcfef5497e7828d89d6ae474b` |
| Licencia | MIT, © 2026 Pawel Huryn; texto íntegro en [LICENSE-pm-skills](LICENSE-pm-skills) (SHA-256 `a2c922f9…774ee`) |
| Obtenido | Clon de lectura el 2026-11-01; sin instalar el marketplace ni otros plugins |

## Revisión del original

Leído completo (3 227 bytes). Un solo archivo; frontmatter `name`/`description`; sin scripts, sin referencias a otras skills ni dependencias. No contiene llamadas de red: solo tres enlaces en «Further Reading» (boletín y curso de video del autor, este último comercial), omitidos en la adaptación y no necesarios. Sin dependencia de pago.

Límites del original frente al instrumento de VCX: pide 8 categorías de riesgo como estructura, «califica la confianza» de cada supuesto, sugiere una prueba pero no vincula el supuesto con una decisión, y no distingue hechos de afirmaciones del autor. Por eso se adapta en lugar de usarlo tal cual.

## Contenido original y ajustes locales

| Elemento | Origen |
|---|---|
| Idea de partir de supuestos de falla desde las perspectivas de producto, diseño e ingeniería | Original (`UPSTREAM-SKILL.md`) |
| Ocho áreas de riesgo (valor, usabilidad, viabilidad, factibilidad, ética, salida al mercado, estrategia, equipo) | Original; aquí son lentes opcionales, no categorías a llenar |
| Estructura en pasos y salida en Markdown | Original, reescrita |
| Prueba de decisividad (decisión afectada y consecuencia), ficha con evidencia, procedencia, límites y criterio observable | **Local** |
| Eliminación de «califica la confianza» | **Local**: la confianza del modelo no es evidencia |
| Reglas de no inventar cifras, tratar afirmaciones sin fuente como del autor, no aplicar semáforo ni clasificación bloqueante, no exigir MVP ni plan | **Local**, desde el [diseño de maduración](../../../../docs/superpowers/specs/2026-10-31-idea-maturation-design.md) y la [capacidad de Brix](../../../docs/idea-intake.md) |
| Idioma de las instrucciones | **Local**: español; identificadores en inglés |

`SKILL.md` es una obra derivada bajo MIT; la atribución se conserva aquí y en su encabezado.

## Ubicación y descubrimiento

Está bajo `brix/.claude/skills/` porque el [instrumento de preguntas asesinas](../../../docs/idea-intake.md) lo ofrece Brix y el directorio sigue la convención del precursor (`.claude/skills/<nombre>/`). No crea runtime ni dependencia ejecutable entre productos. Cualquier otro consumidor debe copiarlo o referenciarlo con su propia configuración.

Observado el 2026-11-01: una sesión con `brix/` como directorio de trabajo la lista y la carga; una sesión con `vcx/` como raíz no (`Unknown skill`). Son comprobaciones aisladas, no una garantía para otros entornos.

## Actualización

El original no se sincroniza solo. Para actualizar: leer la nueva revisión, comparar contra el SHA-256 anterior, repetir la revisión y registrar la nueva revisión aquí. Para retirar: marcar con fecha y motivo en la matriz de tooling antes de borrar.

## Renombre

El 2026-11-01 se renombró de `killer-questions` a `brix-killer-questions` según la convención de nombres con prefijo del producto de origen ([naming](../../../../docs/naming.md#convención)). El texto de la skill no cambió. Los reportes fechados anteriores conservan el nombre y la ruta de entonces.
