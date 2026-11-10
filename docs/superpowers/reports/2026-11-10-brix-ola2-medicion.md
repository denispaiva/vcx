# Ola 2 de Brix: medición

Fecha: 2026-11-10. Es la ola 2 de la [extracción de Brix](../specs/2026-11-07-brix-extraction-design.md) (VCX-D056), dentro de la fase 3 bis del [plan de migración](../plans/2026-11-09-repos-migration-plan.md) (VCX-D063). Medición en solo lectura sobre el precursor en `51fbd2a1` y los repositorios vivos; no se escribió en ninguno. La autorizó el usuario en el chat con Claude («Sí, ola 2»).

Etiquetas: [H] hecho medido; [I] interpretación; [P] propuesta.

## Qué se midió

- [H] `vc/tools/` tiene 68 módulos `.mjs` en su raíz y en `lib/`. VCX-D045 clasificó 36 archivos, por nombre y cabecera, como capacidades de Brix: `blend-run`, resolución de modelos, registro y uso de tooling, recursos, escasez y utilidades.
- [H] En el registro `vc/tooling/brix-capabilities.json`, las 14 capacidades con dueño `brix` ya viven en `denispaiva/brix`. Las excepciones son los cuatro instrumentos de `scripts/`, que quedaron en la instancia por decisión del 2026-11-09.
- [H] Se buscaron referencias a `vc/tools/` fuera de Markdown en los repositorios vivos: `vcx`, `brix`, `cellar`, `solera`, `solera-teyst`, `solera-melquisedec`, `solera-salmanazar` y `solera-pinot-index`. Todas son comentarios, procedencia, evidencia histórica o texto de una vista. **Ningún repositorio vivo importa ni ejecuta código de `vc/tools/`.**
- [H] El último registro de uso medido del tooling del precursor es del 2026-10-01, y el último tren, del 2026-10-29.

## Conclusión

[I] La ola 2 no tiene consumidor. Según VCX-D044 (curar por uso) y VCX-P3 (sin futuro sin fundamento), nada de `vc/tools/` pasa a Brix: queda en el precursor archivado, con su historia, y se rescata solo si aparece un consumidor real.

## Lo que sí depende del precursor

Lo que se rompe al archivarlo no es código de `vc/tools/`, sino cinco herramientas que leen el checkout del precursor:

| Herramienta | Qué lee del precursor | Propuesta |
|---|---|---|
| `vcx/docs/tooling/score-run.mjs` | `vc/tooling/scoring-policy.json` y la huella del checkout | [H] La política es idéntica, campo por campo, a `default-scoring-policy.json` de Brix. [P] Usar esa, versionada con el CLI, y quitar la huella del precursor |
| `vcx/docs/exports/build_tooling_matrix_view.py` | `vc/tooling/evaluations/`, como segunda fuente de la vista | [P] Dejar de leerla. Las evaluaciones del precursor quedan en el archivo; la matriz pública muestra las de `vcx` |
| `vcx/docs/exports/build_portfolio_board_view.py` y `build_spend_view.py` | Roadmaps y FinOps del portfolio | [P] Apuntar a `solera` (FinOps) y a los `solera-<proyecto>` (roadmaps), o retirarlas si no se usan |
| `solera/docs/exports/product-map/build.py` | Roadmaps de los proyectos y `brix-capabilities.json` | [H] Hoy ya lee de la ruta equivocada: apunta a la raíz de `solera`, que no tiene `vc/`. [P] Igual que las dos anteriores |

[H] `vc/tooling/` tiene además 324 archivos de evaluaciones, 26 de uso y 8 de ciclo de vida. VCX-D045 los mandaba a Solera. [P] No se mueven mientras nadie los use: quedan en el archivo.

## Qué no decide

No toca el precursor ni GitHub. El retiro de las cinco dependencias y la decisión sobre las vistas van con autorización propia.
