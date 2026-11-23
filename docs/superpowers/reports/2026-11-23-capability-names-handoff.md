# Traspaso de Codex a Claude · 23 de noviembre de 2026

Para retomar desde otro worktree, `git worktree list` identifica el checkout principal. Estos cambios están en sus archivos de trabajo. El [README](../../../README.md) enlaza este traspaso.

**Actualización del 23 de noviembre:** el PO eligió **Poda** para el optimizador de CI. Las menciones a Dosaje que siguen corresponden al primer traspaso. La elección vigente consta en VCX-D074.

## Qué modificó Codex

- La [matriz](../../architecture/tooling-matrix.md) identifica a Vendimia con la clave `backlog-and-sprint-planning` y el rol Sprint Planner, a Barenboim con `model-resolution` y el rol AI Model Optimizer, y a Dosaje como nombre del optimizador de CI. Para Dosaje el PO aprobó la denominación. Su operación debe verificarse en el consumidor.
- El [registro](../../decisions/README.md) conserva la elección de Vendimia como ampliación de D071, la denominación de Barenboim en D073 y la elección de Dosaje en D074 del checkout local. Los nombres conservan el reparto de responsabilidades. Sigue pendiente la titularidad definitiva de Barenboim.
- Codex recuperó la [regla de Barenboim](../../../finops-policy.md#regla-de-sesión-de-barenboim) de la revisión de Claude `2db0c75` y añadió la autorización del PO para ejecutar un handoff en Codex. [AGENTS.md](../../../AGENTS.md) enlaza la regla y [CLAUDE.md](../../../CLAUDE.md) carga las instrucciones comunes.

## Evidencia del primer despacho en Codex

Codex despachó la redacción de este traspaso a `gpt-6-luna` con razonamiento `low`. El primer borrador leyó las diferencias de los commits de regeneración y omitió las decisiones presentes en sus árboles. El principal contrastó los registros con `git show <sha>:docs/decisions/README.md`, pidió la corrección al mismo agente y editó el resultado final. Hubo retrabajo. El consumo comparativo de cupo quedó sin medir.

## Ramas que debe cotejar quien integre

| Asunto | Evidencia local |
|---|---|
| D072 en dos ramas | `docs/model-optimizer-v1@070d16f` registra el piloto de modelos. `docs/orquestador-disponibilidad-po@3181b6e` registra la disponibilidad diaria del PO. Son decisiones diferentes. |
| D073 en dos ramas | `docs/barenboim-orquestador-modelos@5220501` nombra la capacidad. `docs/model-optimizer-v1@9aa07d0` incorpora además el piloto y su regla. Los respectivos commits de vista son `1d5840d` y `2db0c75`. |

Al retomar, consultá el remoto y los PR vigentes, reconciliá D072 conservando cada decisión con su procedencia y cotejá que D074 siga disponible. Al preparar el commit, separá estos cambios de las ediciones previas del README y del registro de decisiones. Después del commit de la matriz, ejecutá `python3 -I docs/exports/build_tooling_matrix_view.py` y verificá los tres nombres en la vista. Al cierre de esta sesión, el checkout raíz llevaba cambios locales y el acceso a GitHub fallaba por resolución de nombre.
