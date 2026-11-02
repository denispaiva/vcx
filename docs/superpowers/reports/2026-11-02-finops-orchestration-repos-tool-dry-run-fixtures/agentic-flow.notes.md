# agentic-flow: notas de evaluación

Medido el 2026-11-02 a las 00:5x UTC (2026-11-01 21:5x en hora local, -03). `evaluatedRef` es el HEAD de main: `2c86073bf55a105282bbdd4476fc18f5b7e6f97d`, el merge del PR #248. No se usó tag porque la última release (v2.1.3) no corresponde al paquete actual (3.1.0).

## Qué se verificó

- Metadatos del repo y del autor, releases (25), tags (51), commits de 90 días (54), issues abiertos y cerrados, advisories (1), workflows (10), corridas de CI en main y el árbol completo (3.928 blobs, sin truncar).
- Leídos directamente en el SHA: `package.json` (raíz) y `agentic-flow/package.json`, `agentic-flow/docs/guides/MULTI-MODEL-ROUTER.md`, `agentic-flow/src/router/{router,types,cost-optimal-router}.ts`, `agentic-flow/scripts/postinstall.js`, `SECURITY.md`, `.github/workflows/test.yml`, ambos README, el benchmark de cost-optimal, `src/cli/claude-code-wrapper.ts` y `src/cli-proxy.ts`.
- Documentado frente a implementado: `RouterOptimizedAgent`, `budget.total`, `perDocument` y `fallbackToFree` solo aparecen en las dos copias de la guía (search/code: 2 resultados cada uno). `router.ts` no los contiene, y `selectByCost` es un stub con `TODO: Implement actual cost calculation` y un orden fijo. `costOptimization.maxCostPerRequest` y `budgetAlerts` se declaran en `types.ts`, pero `router.ts` nunca los lee. La CLI no tiene modo `router`, aunque la guía documenta `router init/test`.
- Claves: el proveedor por defecto es `anthropic` y exige `ANTHROPIC_API_KEY`; OpenRouter y Gemini también usan claves de API. Las únicas rutas sin pago por token son locales (Ollama u ONNX). No hay una ruta para usar suscripciones Claude Max o ChatGPT: el wrapper reemplaza `ANTHROPIC_BASE_URL` y `ANTHROPIC_API_KEY` de Claude Code por un proxy propio.
- Versión: la raíz declara `2.0.2-alpha` y `agentic-flow/` declara `3.1.0` (no alpha). El README raíz dice v2.0.0-alpha. Existe el tag `v3.0.0-alpha.2` sin release.
- Dependencias del paquete publicable: 26 de runtime (11 vinculadas al enrutamiento y 15 ajenas: memoria vectorial, MCP, P2P y Supabase) y 7 opcionales.
- Antecedente: `ruflo.evaluation.json` (diferida, riesgo crítico, RCE CVE-2026-59726). El archivo `ruflo.evidence.json` que pide el brief no existe en el precursor; se usó la narrativa de `vc/docs/tooling/evaluations.md#ruflo`.

## Anomalías

1. La guía del router documenta un control de presupuesto que no existe en el código, y el README presenta como "Measured" un benchmark que el propio script declara sintético (PRNG con semilla).
2. `SECURITY.md` es la plantilla de GitHub sin editar (versiones 5.1.x y 4.0.x inexistentes, sin canal de reporte), y el reporte privado está pendiente (#235). A esto se suma un CVE alto (8.8, CWE-78) parcheado en junio de 2026.
3. El versionado retrocede: tags v2.3.x en 2025, versiones 2.1.x y 2.0.14 en 2026, dos package.json con el mismo nombre y versiones distintas, y 2.1.4, 2.1.5, 3.0.0 y 3.1.0 publicadas en PR sin tag.
4. El README declara MIT y enlaza un `LICENSE` inexistente en la raíz (la API devuelve `license=null`); `agentic-flow/package.json` incluye `LICENSE` en `files`, pero el archivo tampoco existe allí.
5. Hay artefactos versionados (11 `.tgz` y `.db-shm`) y un `.env.test` en la raíz, que no se leyó. El postinstall reescribe archivos de `agentdb`, y el wrapper imprime los primeros 10 caracteres de `ANTHROPIC_API_KEY`.
6. La API lista `test-agentdb-attention.yml` como activo, pero en el árbol figura como `.disabled`. Benchmarks y Docker fallan de forma sostenida en main.
7. El mapeo de releases es ambiguo: la release más reciente por fecha (v2.1.3, 2026-09-16) aparece primera en la lista, delante de v2.3.6 (2025-11).

## Encaje

Necesidad A: no aporta frente al resolver propio ni frente a `claude -p --max-budget-usd`. Su único diferencial (cost-optimal aprendido) exige un dataset etiquetado y proveedores pagados por token, lo que choca con `allowPayPerToken: false`. Necesidad B: no la cubre.

## Flags y presupuesto

- Flags verdaderos: localWriteReversible, newLocalDependencies, networkAccess, credentialsAccess, sensitiveDataAccess (envía prompts a proveedores externos) y broadScope (213 herramientas MCP, swarms, reparación autónoma). destructiveActions quedó en falso para el uso como enrutador; la reparación autónoma (Darwin) no se evaluó.
- Llamadas a la API: 29 de 40 (2 de `search/code`). No se clonó ni ejecutó nada del candidato. Ningún contenido leído pidió ejecutar comandos.
