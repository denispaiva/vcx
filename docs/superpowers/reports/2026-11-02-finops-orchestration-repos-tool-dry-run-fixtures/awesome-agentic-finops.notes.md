# Notas: awesome-agentic-finops (medido 2026-11-01)

- evaluatedRef: 2da98df4542f47b49e15fb24536bab9d8bab66bf (HEAD de `main`; sin releases ni tags).
- Tipo `practice`: lista curada de 3 archivos (README 223 lineas, CONTRIBUTING, LICENSE CC0). Cero codigo ejecutable, cero dependencias.
- Llamadas a la API de GitHub usadas: 18 de 40 (repo, commits/main, README raw, commits, releases, contributors, users, tree, advisories, workflows, issues, CONTRIBUTING raw, LICENSE raw, issues #7, #16, #20, #8, community/profile; una de ellas repetida con jq distinto). Sin `search/code`. Lecturas locales de solo lectura: `model-routing-policy.json` (allowPayPerToken=false) y listado de evaluaciones previas (ninguna del autor ni de Costory).

## Conteo de entradas (README, leido completo)
- 104 vinetas de lista, 101 URLs unicas, mas 9 filas de tabla comparativa (todas duplican entradas de abajo).
- Gasto de inferencia LLM/tokens: unas 5 entradas unicas lo tocan (aws-cost-explorer-mcp-server con Bedrock, Costory, Atmoz, FOCUS_Spec, finopsfoundation). El resto (~95) es nube (AWS, Azure, GCP, Kubernetes, IaC, pricing) o SaaS. Ninguna mide tokens por rama o sesion de Claude Code.
- Las 5 skills de Claude Code listadas (aws-cost-audit-skill, azure-costs-analyzer, claude-aws-cost-saver, aws-skills, gcp-ironclad) auditan facturas de nube, no el consumo de Claude. Mas cercano a la necesidad B: costory-io/costory-finops-mcp-skills (plugin Claude Code + MCP hosted comercial, gasto agregado), aws-cost-explorer-mcp-server (solo Bedrock), FOCUS_Spec (vocabulario de tokens).

## Autor, vendor y criterios
- Autor: cuenta personal `gregoire-costory` (creada 2024-04-24, 12 repos, 2 seguidores), no una organizacion. README: "Maintained by the team at Costory", vendor declarado.
- Costory figura en la propia lista 3 veces (tabla comparativa, agentes y asistentes, plugin de skills) y `costory-io/costory-finops-mcp-skills` abre la seccion de skills; 15 apariciones de la etiqueta `vendor` en total (7 vendors distintos: Costory, Vantage, CloudZero, AWS FinOps Agent, Cloudaware, Atmoz, NudgeBee). El autor reconoce en un commit (2026-08-13) que su entrada era "the least accurate".
- Licencia: CC0 1.0 (texto en LICENSE); la API reporta NOASSERTION/other. Contribuidores: 2 (15 y 1 commits).
- Criterios de admision: 3 (relevante, mantenida ~12 meses, disponible honestamente), vendor tag y estilo sin editorializar. Sin automatizacion.

## Anomalias
1. Respuesta a la comunidad: 14 items externos abiertos con 0-1 comentarios, el mas viejo del 2026-06-24; el PR #8 (awesome-ai-tokenomics, el unico adyacente a tokens) se cerro sin incorporarse y #7 (tracer de costo de llamadas LLM) sigue sin respuesta. Mientras tanto el PR propio #20 actualiza la entrada de Costory (Starter USD 300/mes).
2. Inestabilidad de hechos comerciales de la entrada del autor: prueba de Costory 14 dias (2026-10-12) y 30 dias (2026-10-15) en commits consecutivos; el titulo del PR #18 dice 30 dias pero el commit asociado decia 14.
3. Menor: licencia NOASSERTION en la API; seccion "Evals & benchmarks" vacia; commits con coautoria de Claude.

## Banderas
Todas false: el candidato es documentacion sin ejecucion; los riesgos de las herramientas enlazadas no se evaluaron aqui.
