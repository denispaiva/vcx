# Corridas en seco de `/tool` sobre los repositorios propuestos para la orquestación FinOps

Fecha: 2026-11-02. Tipo: informe de evidencia fechada; no sustituye la [matriz de tooling](../../architecture/tooling-matrix.md), el [registro de decisiones](../../decisions/README.md) ni el registro de evaluaciones de `brix/tooling/`. Origen: el usuario pidió en el chat del 2026-11-02 «Dispara subagentes en opus u otros modelos para analizar con /tool» sobre los cinco repositorios ya verificados en el [informe anterior](2026-11-01-finops-orchestration-repos-check.md). Marco: procedimiento de VCX-D035 en el [diseño](../specs/2026-11-01-tooling-evaluation-in-vcx-design.md).

## Alcance y por qué no se persistió

Se ejecutaron los pasos 1 a 5 del procedimiento: identificar, precondiciones, evidencia y corrida en seco con `--dry-run`, que no escribe nada. No se persistió ninguna evaluación ni decisión por dos motivos:

1. VCX-D035, decisión 3 aprobada por el usuario: la primera evaluación se corre a mano y cualquier segundo candidato exige antes un envoltorio delgado que haga cumplir las precondiciones y escriba `score-runs.jsonl`. Ese envoltorio no existe.
2. La primera evaluación ya se persistió: otra sesión registró `brix-llm-council` en `brix/tooling/` el 2026-11-02 a las 00:50 UTC. Desde ese momento estos cinco serían el segundo candidato en adelante.

Persistir y decidir requieren, por tanto, el envoltorio y una autorización aparte. La decisión humana vigente sobre los cinco sigue siendo el rechazo del 2026-11-01, registrado en la matriz.

## Método

- Evidencia: un subagente por candidato produjo el archivo de evidencia con los 23 subfactores y los 12 `riskFlags`, a partir de la API de GitHub autenticada y lecturas directas de archivos, sin clonar ni ejecutar código. Brief común y plantilla en los fixtures. Modelos: `claude-opus-5-5` para `cadtopo` y `agentic-flow` (perfil `audit`, clase `frontier`); `claude-sonnet-5-5` para las dos listas y el servidor MCP (perfiles `inventory` y `bounded-search`). `opus` no está en el catálogo contratado del precursor; se usó por decisión del usuario en este chat. Máximo tres subagentes simultáneos, según [finops-policy.md](../../../finops-policy.md).
- Contrato del motor: todo subfactor con `method: "rubric"` exige `evidenceRefs`, incluso `unavailable`. Un archivo (`awesome-agentic-finops`) llegó sin referencias en `observedOutcome` y `observedAdoption`; se agregó a cada uno una referencia a la fuente consultada y vacía, sin tocar puntajes ni fundamentos. Los otros cuatro ya cumplían. El script `normalize.py` del scratchpad registró el cambio.
- Motor: `node ../blends/vc/brix/packages/cli/bin/brix.js tool score evaluate --input <evidencia> --policy ../blends/vc/tooling/scoring-policy.json --output-dir brix/tooling --now 2026-11-02T01:00:00.000Z --dry-run`, desde la raíz de VCX, con `GITHUB_TOKEN` de `gh auth token` para el colector de comunidad.
- Precondición 2 de VCX-D035, medida antes y después: `git --no-optional-locks -C ../blends status --porcelain --ignored -- vc/brix/packages/cli vc/tooling/scoring-policy.json` vacío; `precursorHead` `f86a2a7df72e55bbb97451c1a35ef3c03b961fc3`; `cliTree` `889332c5d1065a3a39e25889587f503caad40195`; `policySha256` `ce6e1a319f1f296cdf491fe38dfa32ee08306f9ba6dedcadac21f9cd5ad49161`, `formulaVersion` 1.6.0. Sin cambios entre ambas mediciones.
- Control de escritura: `brix/tooling/evaluations/` contiene solo `brix-llm-council` antes y después; el motor imprimió «dry-run: no se escribió nada» en las cinco corridas.

## Resultados

| Candidato | Tipo | Puntaje | Confianza | Riesgo | Recomendación base | `evaluatedRef` | Evaluador |
|---|---|---|---|---|---|---|---|
| `cadtopo` | technology | **36.3** | high (93) | high | do_not_advance | `1ba0af0ee116` | `claude-opus-5-5` |
| `agentic-flow` | technology | **38.4** | high (94) | high | do_not_advance | `2c86073bf55a` | `claude-opus-5-5` |
| `awesome-agentic-finops` | practice | **46.3** | high (95) | low | do_not_advance | `2da98df4542f` | `claude-sonnet-5-5` |
| `finops-mcp-resources` | practice | **45.0** | high (93) | low | do_not_advance | `7a364fc58d74` | `claude-sonnet-5-5` |
| `aws-finops-mcp-server` | mcp | **33.6** | high (94) | high | do_not_advance | `d8316bd06943` | `claude-sonnet-5-5` |

Lectura según las reglas fijadas en VCX-D035: `do_not_advance` no admite; las decisiones posibles son `rejected` o `deferred`. Los cinco quedan por debajo del umbral de 60 de `advance_with_reservations`, con confianza `high` en todos los casos. Tres tienen riesgo `high` por acceso a red y credenciales; las dos listas tienen riesgo `low` porque no ejecutan nada, pero adoptar cualquier servidor que listan activaría esos flags.

## Hallazgos por candidato

### `cadtopo`

- El enlace al paper DyTopo del README apunta a la raíz de arXiv, no a un paper: la base académica no se puede verificar.
- Toda llamada pasa por LiteLLM con claves por peldaño; sin claves pago por token solo queda un modelo local que el repo no documenta. `tracing.py` escribe prompts completos en `runs/` sin declararlo. Un autor, 7 commits en 3 días y ninguno en 52; `pyproject` 0.1.0 frente a un único tag 0.0.1.

### `agentic-flow`

- El control de presupuesto que documenta `MULTI-MODEL-ROUTER.md` (`budget.total`, `fallbackToFree`, `router init`) no existe en `src`: `selectByCost` es un stub con TODO. El README presenta como medido un benchmark que su propio script declara sintético.
- `SECURITY.md` es la plantilla de GitHub sin editar; un CVE alto (8.8, CWE-78) parcheado en 2.0.14; dos `package.json` con el mismo nombre (2.0.2-alpha y 3.1.0), tags que retroceden y un LICENSE enlazado que no existe en la raíz. El proveedor por defecto exige `ANTHROPIC_API_KEY` de pago por token.

### `awesome-agentic-finops`

- De 101 URL únicas, unas 5 tocan gasto de LLM y unas 95 son nube o SaaS. Ninguna mide tokens por rama o sesión en Claude Code; las más cercanas son un MCP comercial alojado, un servidor solo para Bedrock y la especificación FOCUS.
- La mantiene Costory, que figura tres veces como vendor en su propia lista y abre la tabla. Cuenta personal con 15 de 16 commits; 14 ítems externos abiertos sin respuesta desde 2026-06-24 y el único PR adyacente a tokens se cerró sin incorporar.

### `finops-mcp-resources`

- De 23 servidores, 2 tratan precios o ROI de LLM como foco, 3 parcialmente y 18 son de nube o flujos. Ninguno enruta modelos ni lee transcripts locales; los de precios por token chocan con `allowPayPerToken: false`.
- Cuenta de usuario, no organización; LICENSE truncado a 284 bytes; sin releases, sin CI y un badge de enlaces verificados sin respaldo. Sin criterio formal de admisión; 3 de los 5 servidores de IA son del propio mantenedor.

### `aws-finops-mcp-server`

- Abandonado: último push el 2025-06-11, 20 commits en 3 semanas, una release y 3 PR externos sin respuesta. Exclusivo de AWS: no enruta modelos ni mide tokens.
- Declara `requires-python >=3.10` pero usa sintaxis válida solo desde 3.12. El README anuncia salidas PDF, HTML y CSV que el servidor no genera. `all_profiles` recorre todos los perfiles AWS locales con `Resource: *` de solo lectura.

## Detalle por factor

### `cadtopo`

Factores: community 8.8, maintenance 42.4, security 59.0, fit 23.0, engineering 46.0, sustainability 48.5.

Flags verdaderos: localWriteReversible, newLocalDependencies, networkAccess, credentialsAccess. Subfactores sin evidencia: maintenance.responseHealth, fit.observedOutcome, fit.observedAdoption.

Notas del evaluador: `cadtopo.notes.md` en el scratchpad de la sesión (no se versionan; el archivo de evidencia es la fuente).

### `agentic-flow`

Factores: community 48.0, maintenance 61.5, security 42.8, fit 16.7, engineering 28.0, sustainability 34.8.

Flags verdaderos: localWriteReversible, newLocalDependencies, networkAccess, credentialsAccess, sensitiveDataAccess, broadScope. Subfactores sin evidencia: fit.observedOutcome, fit.observedAdoption.

Notas del evaluador: `agentic-flow.notes.md` en el scratchpad de la sesión (no se versionan; el archivo de evidencia es la fuente).

### `awesome-agentic-finops`

Factores: community 24.2, maintenance 54.1, security 63.3, fit 29.3, engineering 37.5, sustainability 92.2.

Flags verdaderos: ninguno. Subfactores sin evidencia: fit.observedOutcome, fit.observedAdoption.

Notas del evaluador: `awesome-agentic-finops.notes.md` en el scratchpad de la sesión (no se versionan; el archivo de evidencia es la fuente).

### `finops-mcp-resources`

Factores: community 26.7, maintenance 61.8, security 59.5, fit 23.3, engineering 39.8, sustainability 78.5.

Flags verdaderos: scopedLocalReadOnly. Subfactores sin evidencia: fit.observedOutcome, fit.observedAdoption.

Notas del evaluador: `finops-mcp-resources.notes.md` en el scratchpad de la sesión (no se versionan; el archivo de evidencia es la fuente).

### `aws-finops-mcp-server`

Factores: community 33.2, maintenance 12.3, security 56.0, fit 10.2, engineering 34.4, sustainability 67.0.

Flags verdaderos: newLocalDependencies, networkAccess, credentialsAccess, sensitiveDataAccess, broadScope. Subfactores sin evidencia: fit.observedOutcome, fit.observedAdoption.

Notas del evaluador: `aws-finops-mcp-server.notes.md` en el scratchpad de la sesión (no se versionan; el archivo de evidencia es la fuente).


## Costo

- Consumo de subagentes informado por el harness: 580.294 tokens en total (102.540, 120.728, 98.542, 138.887 y 119.597), 105 usos de herramienta, entre 107 y 381 segundos por subagente. Es consumo de cupo de suscripción, no un cobro; el costo en dinero no está disponible, según la regla de la política.
- Llamadas a la API de GitHub: unas 170 entre subagentes, motor y comprobaciones; el límite quedó en 4.831 de 5.000 al cierre.

## Límites

- La evidencia la produjeron modelos, con fundamentos escritos pero sin revisión humana subfactor por subfactor. Los puntajes `rubric` llevan ese sesgo declarado.
- Una corrida por candidato, sin iteración sobre `fit`: el consumidor no aportó un caso de uso nuevo que la moviera.
- Los `evaluatedRef` son instantáneas del 2026-11-01 y 2026-11-02; una persistencia futura debe repetir la medición si el HEAD cambió.
- `community` lo calculó el colector del motor contra la API en el momento de la corrida; no se guardó snapshot fuera de las salidas de los fixtures.

## Archivos

Carpeta [`2026-11-02-finops-orchestration-repos-tool-dry-run-fixtures/`](2026-11-02-finops-orchestration-repos-tool-dry-run-fixtures/): cinco `*.evidence.json` (entrada canónica de una persistencia futura), cinco `*.notes.md` de los evaluadores, cinco `*.out` con la salida del motor, el brief común y la plantilla.

## Pendientes

- Si se quiere registro canónico: construir el envoltorio de VCX-D035, obtener autorización, repetir `evaluate` sin `--dry-run` y `decide --status rejected --by "Denis Paiva"` por candidato, con su línea en `score-runs.jsonl`.
- Nada de esto cambia la decisión vigente de la matriz; las corridas la confirman con puntaje.
