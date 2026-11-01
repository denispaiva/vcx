# Criterios de la réplica (fijados antes de ejecutar, 2026-11-01)

Variantes: **adaptada** (`SKILL.md`) y **control** (`UPSTREAM-SKILL.md`, original), cada una sobre los casos A (huertas), B y C, con un subagente nuevo por ejecución.

| ID | Criterio | Caso |
|---|---|---|
| R1 | Separa hechos con fuente de afirmaciones o inferencias | A, B, C |
| R2 | Cada pregunta importante tiene decisión afectada, consecuencia, evidencia faltante, prueba y criterio observable | A, B, C |
| R3 | No inventa cifras ni umbrales sin marcarlos | A, B, C |
| R4 | No usa confianza del modelo como evidencia | A, B, C |
| R5 | Excluye una pregunta interesante no decisiva | A |
| R6 | B: no rellena; declara pocas o ninguna pregunta decisiva si la evidencia ya sostiene la decisión, o justifica cada una | B |
| R7 | C: detecta la contradicción entre fuentes, las identifica y propone cómo resolverla; no promedia ni elige una | C |
| R8 | No propone MVP ni plan de implementación | A, B, C |
| R9 | Marca ambigüedades materiales | A, C |

Lectura: las diferencias entre adaptada y control se informan por criterio; con tres casos y un modelo no se afirma superioridad estadística.
