# Notas: finops-mcp-resources (medido 2026-11-02)

- evaluatedRef: `7a364fc58d74f3c5dcd67a9c8c51fd4c795c34b8` (HEAD de `main`, 2026-10-28). Tipo `practice`: colección de documentación, no software.
- Llamadas a la API de GitHub usadas: 17 de 40 (repo, commit HEAD, árbol, releases, tags, commits, advisories, workflows, users, issues, y 7 lecturas de archivos: README, LICENSE, SECURITY, CONTRIBUTING, servers/INDEX, registry.yaml, CHANGELOG). Sin `search/code`. Nada clonado ni ejecutado.

## Qué verifiqué
- 27 estrellas, 8 forks, 1 issue abierto (#9, 2026-04-11). Sin releases ni tags. 0 workflows. 0 advisories.
- Commits: 3 en 30 días, 14 en 90, 21 en 180 (de los últimos 100). Autores: OptimNow 49, Jean Latiere 47, 3 externos.
- Contenido de `servers/`: INDEX.md, 6 documentos (aws, azure, gcp, jira, slack, tagging) y `configs/registry.yaml` + `schema.json`. El registro tiene 23 entradas, coincide con el recuento declarado.
- Clasificación por texto del registro: 2 de precios/ROI de LLM como foco (`ai-pricing-hub-mcp`, `ai-roi-calculator-mcp`), 3 con gasto de IA como parte de una oferta mayor (`nable-finops-mcp`, `costory-finops-mcp`, `cloud-finops-mcp`), 18 de nube/flujos (AWS 7, Azure 4, GCP 4, tagging/JIRA/Slack 3).
- Criterio de admisión: no existe uno formal. CONTRIBUTING pide probar lo que se documenta; los proveedores se autopostulan por PR (Costory #15, nable #12 y #20).
- No se siguieron enlaces externos. Los datos de los servidores listados son lo que dice el registro, sin verificar.

## Anomalías
1. `OptimNow` es una cuenta User, no una Organization (el brief la daba por organización). Cuenta creada 2025-07-15, repo 2025-09-01.
2. LICENSE truncado: 284 B con la cabecera de Apache 2.0 y sin el texto completo; la API da `NOASSERTION`. El README declara Apache-2.0.
3. Conflicto editorial: 3 de los 5 servidores relacionados con IA son del propio mantenedor, en una sección propia. Costory (de pago, 300 USD/mes) entró por PR de su propio proveedor.
4. Badge "links checked" sin enlace ni workflow que lo respalde; 0 verificación automática. README con "Recent Updates (July 2026)" atrasado y "registry now at 18 entries" frente a 23 reales.
5. Binarios sin inspeccionar: `AWS-Amplify-Frontend.zip` (477 KB), CloudFormation de 206 KB y un mp4 de 1.9 MB.
6. No hay evaluación previa de OptimNow en `/Users/denis/VibeCoding/blends/vc/tooling/evaluations/`.

## Encaje
- A (elegir clase/modelo): ningún servidor enruta. `ai-pricing-hub-mcp` da precios de 250+ modelos, pero la política del resolver fija `allowPayPerToken: false` y `costOrder` [free, subscription-included, pay-per-token]; el precio por token no entra en la decisión. Es endpoint alojado por un tercero (Alpic).
- B (tokens por rama/sesión): ninguno lee transcripts locales; `nable` mide gasto vía APIs de proveedores, que no refleja consumo de suscripciones.
- Veredicto de evidencia: cobertura marginal para este consumidor. Útil como lista de candidatos a evaluar por separado, no como herramienta.

## riskFlags
Sólo `scopedLocalReadOnly` (leer documentación). Adoptar cualquier servidor listado activaría `networkAccess` y, en la mayoría, `credentialsAccess`; eso corresponde a evaluar cada servidor, no la colección.

## Pendiente de verificación
- Contenido de los tutoriales (instrucciones de instalación/ejecución) no leído en profundidad. No se evaluó ningún servidor listado.
