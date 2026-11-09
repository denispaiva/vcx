# Brix E1, E2 y E3: export, prueba aislada y publicación

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
| Ruta local `/Users/denispaiva/blends` | Fixture de `scripts/tests/context-window.test.mjs` | [I] Es el usuario de GitHub y una ruta ya inexistente | Salió con `scripts/` (E2) |
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

### Decisión sobre `scripts/`

El 2026-11-09, ante «¿Qué hago con los 9 scripts/ de Brix?», el usuario respondió «Dejarlos a Solera». Los instrumentos F1 y C5 de la Fase 0 miden el portfolio y escriben en `data/`, así que son medición de la instancia y no capacidad del producto.

- Se quitó `scripts/` de **todo** el historial, igual que `data/` y `finops/`. Con eso desaparece también la ruta local del fixture. La fuente sigue en el precursor.
- El README explica dónde quedaron, la estructura refleja el árbol real y el origen describe el repositorio como fuente canónica. La CI corre solo `tests/`.
- Resultado: 140 commits, punta `f89b1e6`.

Compuerta repetida en un clon limpio, sin tokens:

| Criterio | Resultado |
|---|---|
| Pruebas | [H] 101 de 101; las 59 que faltan respecto de las 160 eran de los instrumentos |
| CLI | [H] Arranca con salida 0 |
| `npm pack` | [H] 29 archivos, con `finops` y `seeding` |
| Datos de instancia en el historial | [H] 0 rutas de `scripts/`, `data/`, `finops/` o `.roadmap.json` |
| Correos | [H] Solo `noreply` del autor, `noreply@anthropic.com` y `git@github.com` |
| Rutas locales en el historial | [H] 0 |
| Secretos | [H] Betterleaks sin hallazgos |

## E3: publicación

El usuario la autorizó en el chat con Claude («Sí, Brix E3»). Es la etapa externa y difícil de revertir.

| Paso | Resultado |
|---|---|
| Apartar el espejo | [H] `denispaiva/brix` pasó a llamarse `denispaiva/brix-espejo-2026-09`, sigue privado, quedó archivado y su descripción apunta a la fuente nueva. No se borró nada |
| Scan antes del push | [H] Betterleaks sobre todo el historial: sin hallazgos |
| Repositorio público | [H] `denispaiva/brix`, con `main` en `f89b1e6` (140 commits) |
| Protección de `main` | [H] Solo por PR, check obligatorio `test`, también para administradores, sin force-push ni borrado |
| Bloqueo de `graduation-export` | [H] Ruleset activo, sin excepciones: impide crear o actualizar esa rama. `brix.config.json` del precursor todavía la apunta a `denispaiva/brix`, así que un `brix graduate` publicaría el subárbol |
| CI | [H] La primera corrida falló: Node 24 no acepta un directorio en `--test`, y la compuerta de E2 había corrido con Node 26. Se corrigió con un glob en el PR 1 de `brix`, que mergeó el usuario. En `main` `31b1c6d` pasan 101 de 101 pruebas, el CLI arranca y el paquete está completo |
| Tag | [H] `v0.1.0`, anotado, sobre `31b1c6d` |

### Corte

Desde el 2026-11-09, la fuente canónica de Brix es `denispaiva/brix`. `vc/brix/` del precursor queda congelada en `4742bb99`. El control que fija D056 es correr `git diff --stat 4742bb99..origin/main -- vc/brix` en el precursor antes de cada versión de Brix. Línea base: `origin/main` en `4742bb99`, salida vacía.

Siguen E4 (incorporación en `vcx`) y E5 (Teyst pasa al tarball del tag público), cada una con su propia autorización.

## Recuperación

Antes de E3: borrar el export. Desde E3, lo publicado se trata como visible aunque se borre. El espejo apartado se puede desarchivar y renombrar.
