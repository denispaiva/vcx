# Brix E1: export local del historial

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

## Recuperación

Borrar el export, que está en el scratchpad de la sesión. Ni el precursor ni GitHub cambiaron.
