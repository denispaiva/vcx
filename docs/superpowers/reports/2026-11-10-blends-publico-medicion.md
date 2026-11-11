# Blends público: medición previa

Fecha: 2026-11-10. Corresponde a la fase 4 del [plan de migración](../plans/2026-11-09-repos-migration-plan.md) (VCX-D032, paso 3; VCX-D063). Es una medición en solo lectura sobre el precursor en `origin/main` (`51fbd2a1`) y los repositorios vivos, autorizada por el usuario en el chat con Claude («Sí, medir Blends»). No se exportó ni se publicó nada.

Los conteos de riesgo son agregados: este repositorio es público y no repite los datos.

Etiquetas: [H] hecho medido; [I] interpretación; [P] propuesta.

## Superficie candidata (VCX-D045)

| Parte | Tamaño | Consumidores vivos fuera del precursor |
|---|---|---|
| `vc/docs/standards/` | [H] 28 archivos, unos 958 KB y 319 commits. Los dos más grandes son el `CHANGELOG.md` (242 KB) y `framework-debt.md` (160 KB) | [H] Solo citas de texto como antecedente. El `role-matrix.json` de `solera-teyst` declara un `$schema` con una ruta del precursor que ya no resuelve |
| Herramientas de `vc/tools/`: `validate-*`, `check-branch-scope`, `check-lifecycle`, `verify` y `lib/verify` | [H] 25 archivos, sin contar pruebas | [H] Ninguno. Los proyectos extraídos tienen CI propia y no las invocan |
| `roadmap/` | [H] 7 archivos | [H] Ninguno. Los tableros de `vcx` ya no lo usan |
| `vc/tooling/data-naming.json` | 1 | [H] Ninguno |
| `vcx/blends/` | [H] 5 documentos del método, ya públicos en `vcx` | — |

[I] Igual que en la [ola 2 de Brix](2026-11-10-brix-ola2-medicion.md), la parte ejecutable del núcleo no tiene consumidor: es la maquinaria de gobierno del precursor, que se archiva. Lo que sigue vivo es el método, en forma de documentación.

## Riesgo del historial de los estándares

[H] Sobre los 319 commits de `vc/docs/standards/`, en unas 10.200 líneas agregadas:

- Betterleaks no encontró secretos.
- 66 líneas tienen identificadores de infraestructura: cuentas de servicio, pools de identidad federada, números de proyecto e IDs de entorno.
- 23 líneas tienen importes en USD.
- Hay dos correos de autor reales, y uno de ellos aparece también en el contenido.
- 2 líneas tienen rutas locales.
- Hay unas 600 menciones a proyectos privados.

[I] Publicar ese historial filtrado por ruta (opción B de VCX-D032) expondría la infraestructura de los proyectos privados para siempre. Es la salida que VCX-D032 previó como B': historial nuevo, con la procedencia explícita. La reescritura de correos no alcanza, porque los datos están en el contenido de versiones viejas.

## Alcance propuesto

[P] Por VCX-D044 (curar por uso) y VCX-P3:

1. **`blends` público nace con historia nueva**, desde un export curado, con la procedencia `denispaiva/blends-precursor@51fbd2a1` declarada.
2. **Contenido: el método, no la maquinaria.** Entran los documentos de `vcx/blends/` y los estándares que describen el método, revisados uno por uno para sacar infraestructura, importes y datos de proyectos privados. El `CHANGELOG.md` y `framework-debt.md` son registros de la instancia y quedan en el archivo.
3. **Sin herramientas ejecutables por ahora:** validadores, `verify` y `roadmap/` quedan en el archivo. Se publican solo si aparece un consumidor, con su propio corte de imports.
4. **Incorporación:** el mismo mecanismo E4 sobre `vcx/blends/`, con principios, `CLAUDE.md` y enlaces.

## Decisión

El 2026-11-10, ante «¿Blends nace con historia nueva y solo con el método?», el usuario respondió «Sí, así». Eso confirma B' (historial nuevo con la procedencia declarada) y deja la maquinaria ejecutable en el archivo. Queda abierta la lista de estándares que entran y la curación de cada uno, que es el trabajo de E1 de esta fase.
