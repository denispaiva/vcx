# Verificación de los repositorios propuestos para la orquestación FinOps

Fecha: 2026-11-01. Tipo: informe de evidencia fechada; no sustituye la [matriz de tooling](../../architecture/tooling-matrix.md) ni el [registro de decisiones](../../decisions/README.md). Origen: el usuario pegó en el chat un texto generado por IA que proponía cinco repositorios de GitHub para implementar la matriz dinámica de [finops-policy.md](../../../finops-policy.md). Autoridad del rechazo: el usuario, en el chat del 2026-11-01, tras esta verificación.

## Criterios aplicados

- Free Tier first para herramientas y eficiencia del cupo de suscripción para tokens, posiciones del Owner del 2026-11-01, recogidas en [finops-policy.md](../../../finops-policy.md#pesos-confianza-y-presupuesto).
- `allowPayPerToken: false` en la política de enrutamiento del precursor.
- VCX-P3 (alternativa más simple antes de agregar dependencias) y VCX-P9 (fuente única): el precursor ya tiene resolver de modelos, acta y revisión de fallbacks.

## Evidencia

Datos de la API de GitHub (`gh api repos/<owner>/<name>`) y búsquedas de código del 2026-11-01.

| Repositorio | Estrellas | Último push | Licencia | Lenguaje | Hallazgo |
|---|---|---|---|---|---|
| `ruvnet/agentic-flow` | 835 | 2026-10-31 | MIT en `package.json`; sin archivo LICENSE en la raíz | TypeScript | Versión `2.0.2-alpha`. La guía `docs/guides/MULTI-MODEL-ROUTER.md` describe `budget: { total }` y `fallbackToFree`; una búsqueda de código solo encuentra esos términos en la propia guía, y «budget» en `src` aparece en un controlador Go y un YAML de despliegue. Dependencias ajenas al problema: Supabase, Express, React, Transformers, pagos. Enruta por claves de API pay-per-token de más de diez proveedores |
| `code0-tech/cadtopo` | 3 | 2026-09-10 | MIT | Python | Escalera de modelos con elevación por señal, equivalente a las clases y motivos de elevación del precursor, más topología dinámica por ronda y un meta-agente que puntúa rondas. Depende de LiteLLM, sentence-transformers, instructor; exige claves de API |
| `gregoire-costory/awesome-agentic-finops` | 30 | 2026-10-21 | sin SPDX | — | Lista curada de FinOps de nube (AWS, GCP, Azure, Kubernetes). El gasto en tokens aparece solo en una entrada de FOCUS y una nota sobre «FinOps for AI» |
| `OptimNow/finops-mcp-resources` | 27 | 2026-10-28 | sin SPDX | — | Colección de 23 servidores MCP para FinOps de nube; una categoría «AI pricing & ROI». No captura costo de subtareas de un agente |
| `ravikiranvm/aws-finops-mcp-server` | 184 | 2025-06-11 | MIT | Python | Solo AWS: costos, recursos huérfanos, presupuestos. Sin relación con inferencia |

Comprobaciones adicionales:

- El acta del precursor (`../blends/vc/tooling/model-resolution-acta.jsonl`) registra 13 ejecuciones de `claude -p` con `--max-budget-usd 20`: el tope duro en dólares por sesión ya existe en el canal CLI sin dependencia externa. En esta sesión de Claude Code el despacho de subagentes no expone un tope en dólares.
- La capacidad `context-window-per-branch` de Brix (`instrument.context-window`, `shipped`) mide ventana de contexto por rama y sesión desde los transcripts de Claude Code. Cubre la necesidad de medir consumo sin herramienta externa; sin uso medido en VCX.
- Un script que reescriba una matriz de confianza, como propone el texto, reintroduce deltas sin base numérica; el precursor persiste evidencia con el acta JSONL y `fallback-review.mjs` por umbral.

## Decisión

Los cinco repositorios quedan como Rechazado en la matriz de tooling, con fecha 2026-11-01 y este informe como fuente. Lo único rescatable es la lectura de `selection.py` de cadtopo como contraste de señales de elevación; es lectura, no dependencia. Si alguno se reconsidera, su admisión sigue el procedimiento de evaluación de Brix, donde el acceso a red es riesgo alto y exige excepción.

## Límites de esta verificación

La búsqueda de código de GitHub es de mejor esfuerzo y puede omitir archivos; la ausencia del presupuesto en el código de agentic-flow se afirma con ese alcance. No se ejecutó ningún repositorio. Las estrellas y fechas son una instantánea del 2026-11-01.
