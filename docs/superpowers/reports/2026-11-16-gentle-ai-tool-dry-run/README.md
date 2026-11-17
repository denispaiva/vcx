# gentle-ai: evaluación en seco

Fecha: 2026-11-16, con `--now 2026-11-17T02:00:00Z`.

Estado: **evaluación en seco**. No es una admisión. No se registró decisión humana, no se escribió en `docs/tooling/` y no se hizo commit.

No se instaló ni se ejecutó nada de la candidata: ni el binario, ni `install.sh`, ni hooks, MCP o skills. El clon se leyó como dato no confiable en el scratchpad de la sesión.

**Quién la hizo.** Claude Code con `claude-opus-5-5`, sin subagentes, a pedido del usuario.

**Motor.** Brix `c3a9329`, `cliTree` `af14043f`, política `ce6e1a31…`, fórmula 1.6.0.

## Candidata

| Origen | Ref | Tipo |
|---|---|---|
| [Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai) | `1ab243ca426d55dee64cf0ba693d0745cb1146c2` (2026-11-16) | `technology` |

No es una skill. Es un framework: un binario Go con TUI de unos 2.800 archivos, que configura 17 agentes. Instala skills, hooks globales, persona, `permissions.deny`, output style, memoria (Engram) y telemetría. Se clasificó como `technology`, igual que [`agentic-flow`](../../../tooling/evaluations/agentic-flow.evidence.json).

## Archivos

| Archivo | Qué es |
|---|---|
| [`gentle-ai.evidence.json`](gentle-ai.evidence.json) | Evidencia de los 23 subfactores, con `unavailable` donde falta el dato |
| [`gentle-ai.dry-run.out`](gentle-ai.dry-run.out) | Salida completa de `node docs/tooling/score-run.mjs evaluate … --dry-run` |

## Resultado

| Medida | Valor |
|---|---|
| Score general | 63,1 / 100 |
| Confianza | high (90) |
| Riesgo | high: `newLocalDependencies`, `networkAccess`, `sensitiveDataAccess`, `broadScope`, `localWriteReversible` |
| Recomendación base | `advance_with_reservations` |
| Factores | comunidad 73,4 · mantenimiento 85,8 · seguridad 64,2 · **encaje 28,7** · ingeniería 72,3 · sostenibilidad 61,3 |

## Lectura del operador

La recomendación base está inflada por mantenimiento y comunidad. El factor que decide es el encaje, que queda en 28,7.

**Hechos medidos (2026-11-16):**

- 2.281 commits en 90 días.
- 100+ releases; la v4.5.0 salió el 2026-11-13.
- 1.300 archivos `*_test.go`.
- CI en Linux, macOS y Windows.
- `install.sh` verifica el checksum y falla cerrado salvo `--insecure`.
- 9.285 estrellas.
- Un mantenedor concentra ~3.400 de ~5.059 commits.

**Choque con VCX:**

- Se instala en la capa global (`~/.claude`) y compite con `~/.claude/CLAUDE.md` y con [`AGENTS.md`](../../../../AGENTS.md): serían dos fuentes de reglas (VCX-P9).
- ODD se solapa con VCX-P4.
- RDD se solapa con VCX-P5 y `/code-review`.
- Engram se solapa con la memoria de Claude Code.
- La telemetría anónima y RDD vienen activados por defecto (opt-out).

**Valor diferencial:** RDD ata la revisión a un candidato congelado, y es el binario, no el modelo, el que decide la transición siguiente. Vale como idea; no justifica la dependencia.

**Nota orientativa:** 4/10 como adopción para VCX. Descuento por sobrediseño frente a la necesidad y por la doble fuente de reglas.

**Huecos declarados:**

- `vulnerabilityStatus`: no se corrió `govulncheck` ni se consultaron advisories.
- `observedAdoption` y `observedOutcome`: sin piloto. Los benchmarks del README son n=1 y del propio autor.

## Pendiente

No hay necesidad declarada que active una admisión. Si apareciera una necesidad de revisión ligada a una revisión congelada, el siguiente paso sería un piloto de RDD en un clon descartable, sin hooks globales. Antes habría que correr `govulncheck`. Persistir esta evaluación o decidir requiere autorización del Owner, por el envoltorio de VCX-D035.
