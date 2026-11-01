# Reporte de verificación: recuperación del commit base documental de la raíz

Fecha: 2026-11-01. Evidencia fechada de la verificación pendiente del [alcance del commit base](../plans/2026-10-31-root-baseline-scope.md), tarea 4. Cierra la ejecución autorizada el 2026-10-31 en el chat con Codex. No sustituye las fuentes editables ni el [registro de decisiones](../../decisions/README.md).

## Revisión verificada

| Dato | Valor |
|---|---|
| Commit base | `f47c71f23d41124cfa84158d8b8e6946654930c3` |
| Mensaje | `docs: preserva la base documental de VCX` |
| Autor y fecha | `denispaiva`, 2026-10-31 10:17:17 -0300 |
| Árbol | `224b77483b60f09078e53326d89c8370de3d94b6` |
| Padres | Ninguno: es el único commit raíz; `git rev-list --count f47c71f` devuelve 1 |
| Archivos | 39 rutas, todas con modo `100644`; sin gitlinks ni symlinks |
| Remoto | Ninguno configurado |

## Procedimiento

Comandos ejecutados desde `/Users/denis/VibeCoding/vcx`, con extracción en un directorio temporal nuevo creado con `mktemp -d` bajo el temporal del sistema. No se ejecutó `checkout`, `restore` ni `reset` sobre el workspace.

```sh
git archive f47c71f | tar -x -C "$T"
git ls-tree -r f47c71f
git hash-object <cada archivo extraído>
git rev-list --parents -n 1 f47c71f
git fsck --full
```

## Resultados

- **Integridad de bytes.** El hash de blob de cada uno de los 39 archivos extraídos coincide con el registrado en el árbol del commit. Cero discrepancias.
- **Lista exacta.** La extracción contiene exactamente las 39 rutas de la [lista explícita](../plans/2026-10-31-root-baseline-scope.md#lista-explícita-del-commit); ningún archivo adicional, ningún `.DS_Store`.
- **Estructura.** Un único commit raíz sin padres, en `main`, sin remoto.
- **`git fsck --full`.** Sin errores. Informa tres árboles colgantes, producto de operaciones de índice posteriores; no afectan la integridad del commit base ni de los commits siguientes.
- **Workspace.** Los documentos permanecen en su lugar; el árbol de trabajo tiene cuatro commits posteriores al base y cambios de la Fase A de VCX-D030 sin commitear, propios de esta sesión.

## Límites

- Git local no es respaldo fuera de la máquina; esta verificación demuestra recuperabilidad desde el repositorio raíz, no protección contra pérdida del disco.
- El contenido verificado es el del commit `f47c71f`, no el de `HEAD`: los documentos evolucionaron en cuatro commits posteriores y la coincidencia es contra el árbol de ese commit.
- No cubre el precursor, cuya protección depende de la transferencia verificada de referencias y estado no versionado, según el [mapa](../../architecture/repository-map.md#recuperación-y-límites).
- La autorización del 2026-10-31 queda consumida; no abarca clones, remotos, exclusiones ni migración.
