# Brix E1 y E2: export local y prueba aislada

Fecha: 2026-11-09. Etapa E1 del [diseño de la extracción de Brix](../specs/2026-11-07-brix-extraction-design.md) (VCX-D056), dentro del [plan de migración](../plans/2026-11-09-repos-migration-plan.md) (VCX-D059). El usuario la autorizó en el chat con Claude («Sí, Brix E1»). El export es local y descartable: no se publicó nada y no se escribió en el precursor.

Etiquetas: [H] hecho medido; [I] interpretación; [P] propuesta.

## Procedimiento

1. Clon del remoto `denispaiva/blends`, `main` en `4742bb99` (la misma base que la medición de D056), en el scratchpad de la sesión.
2. `git subtree split --prefix=vc/brix`: 151 commits.
3. `git filter-branch --prune-empty`, en una sola pasada:
   - autor y committer pasan a `denispaiva <15215397+denispaiva@users.noreply.github.com>`;
   - se quitan `data/`, `finops/` y `.roadmap.json` de **todo** el historial, no solo del árbol final.
4. Purga del reflog y `gc --prune=now`.

[I] Elegí `filter-branch`, que viene con Git, en lugar de instalar `git-filter-repo` (VCX-P3). Para un subárbol de este tamaño alcanza, y D056 dejaba esa elección para E1.

Resultado: 138 commits, punta `6960cb00`, 82 archivos.

## Compuerta de E1

| Criterio | Resultado |
|---|---|
| Correo reescrito | [H] Los 138 commits tienen autor y committer `noreply`. En el contenido y los mensajes solo aparecen `noreply@anthropic.com` (líneas `Co-Authored-By`), el correo `noreply` del autor y `git@github.com` |
| Datos de instancia fuera de todo el historial | [H] 0 apariciones de `data/`, `finops/` o `.roadmap.json` en `git log --name-only` |
| Scan de secretos sobre todo el historial exportado | [H] Betterleaks 2.0.0-rc.1, con la configuración de `vcx`: ~507 KB, sin hallazgos |
| Revisión de referencias registrada | Este documento |

## Revisión de referencias

| Hallazgo | Dónde | Lectura | Propuesta |
|---|---|---|---|
| Ruta local `/Users/denispaiva/blends` | Fixture de `scripts/tests/context-window.test.mjs` | [I] Es el usuario de GitHub y una ruta ya inexistente | [P] Conservar |
| «USD 13,82» de consumo de Actions | `docs/decisions/0001-graduation.md:61`, contexto del Gate | [H] Es el único importe que parece un gasto real; el resto son precios públicos de listas o fixtures | Conservar: lo decidió el usuario el 2026-11-09 («Conservarlo») |
| `dev-teyst`, `prod-teyst` | `docs/decisions/0007-seeding-motor.md` | [I] Son IDs de proyecto Firebase, ya visibles en la configuración web de Teyst | [P] Conservar |
| Menciones a proyectos | Líneas agregadas: 54 a Teyst, 14 a Pinot, 8 a Melquisedec | [I] `vcx` público ya los nombra | [P] Conservar |
| Plan y research de la Fase 0, matriz de roles | 2 planes, 4 investigaciones y `docs/governance/role-matrix.json` | [H] No hay importes, correos ni rutas sensibles. Son la historia de desarrollo de Brix, con tareas y decisiones del PO | [P] Exportar: el filtrado no ganaría privacidad y quitarlos rompería 0001 y 0002 |

## Pendientes para E2

- [H] 34 enlaces relativos de 11 archivos salen del producto o apuntan a rutas inexistentes (`../../../../ideas/`, `vc/docs/standards/`, `vc/tooling/`), sobre todo en `docs/decisions/` y en el `$schema` de la matriz de roles.
- [H] Los 9 `scripts/` siguen dentro, sin decisión según la clase provisoria de D056. Escriben en `data/`, que ya no está.
- D056 ya listaba el resto: el import inverso en `tests/finops/cli-wiring.test.mjs`, `files` de `packages/cli/package.json` sin `finops` ni `seeding`, y la CI que no corre las pruebas.

## E2: prueba aislada

El usuario la autorizó en el chat con Claude («Sí, Brix E2»). Sobre el export se agregó un commit, `c77bbd5`, de modo que el historial queda en 139 commits. Sigue siendo local.

| Cambio | Motivo |
|---|---|
| `discoverLedgers` y `runPortfolioValidation` reciben `portfolioDir` y `excludeDirs` | El layout `vc/` y la exclusión de `vc/framework` eran del precursor. Sin `portfolioDir`, fallan con un error que lo nombra. No hay llamadas a estas funciones dentro de Brix; el envoltorio del precursor usa su propia copia congelada |
| Valores por defecto de `ci` y de las referencias de `scoring`, para el repositorio propio | Eran `vc/**` y `vc/brix/packages/...`. El precursor declara los suyos en su `brix.config.json` |
| `files` del CLI: se agregan `finops` y `seeding` y se quita `scripts`, que no existía en el paquete | Pendiente de D056 |
| Se retira `tests/finops/cli-wiring.test.mjs` | Era el único import saliente. Probaba `vc/tools/validate-billing-ledger.mjs`, que pertenece a la ola 2 o a Solera. El motor sigue cubierto por `validate-ledger.test.mjs` |
| Los 34 enlaces que salían del producto pasan a texto con su procedencia: `(precursor privado, <ruta> en 4742bb99)` | Así se conserva el antecedente sin que el enlace sea requisito de uso |
| `role-matrix.json` pierde el `$schema` que apuntaba al precursor | Era una referencia rota |
| CI nueva: pruebas, arranque del CLI y contenido del paquete; acciones fijadas por SHA; permisos de solo lectura | La anterior solo arrancaba el CLI |

Compuerta, medida en un clon limpio cuya carpeta padre no es un repositorio y sin `GH_TOKEN` ni `GITHUB_TOKEN`:

| Criterio | Resultado |
|---|---|
| Todas las pruebas pasan | [H] 160 de 160: las 159 de la línea base, menos la retirada, más dos nuevas sobre `portfolioDir` |
| `npm pack` incluye `finops` y `seeding` | [H] 29 archivos: `bin`, `src`, `scoring`, `finops`, `seeding`, `LICENSE`, `README.md` y `package.json` |
| Sin rutas `vc/` funcionales en el paquete | [H] Solo quedan 4 menciones, todas en comentarios históricos de `scoring/engine.mjs` |
| Sin imports ni enlaces que salgan del producto | [H] 0 y 0 |

Lo que esta compuerta no cubre:

- Node 24: la prueba local corrió con Node 26.13. La primera evidencia sobre Node 24 será la CI en E3.
- La carga de instrucciones: el export no tiene `AGENTS.md` ni `CLAUDE.md` propios. Los de `vcx/brix/` se fusionan en E4, y ahí se repite la prueba de carga que se hizo con Cellar.
- Instalación y backends reales, como ya advertía D056.

Decisión pendiente: los 9 `scripts/` (instrumentos F1 y C5 de la Fase 0) miden el portfolio y escriben en `data/`, que ya no está en el export. `kpi-history.mjs` agrupa claves por el prefijo `vc/`. No forman parte del paquete y sus pruebas pasan. D056 deja la poda para después del corte.

## Recuperación

Borrar el export, que está en el scratchpad de la sesión. Ni el precursor ni GitHub cambiaron.
