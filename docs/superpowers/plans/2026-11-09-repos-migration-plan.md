# Migración de Brix, Blends y Cellar a `vcx/` con correspondencia en GitHub

Fecha: 2026-11-09. Estado: plan aceptado por el usuario en VCX-D059. Ordena decisiones vigentes (VCX-D025, D030, D032, D036, D053, D056, D057); no las reemplaza. Cada fase con efecto externo requiere autorización propia, con repositorio, ruta y alcance.

Etiquetas: [H] hecho medido; [I] interpretación; [P] propuesta.

## Situación medida

| Pieza | Local | GitHub | Coincide |
|---|---|---|---|
| Raíz | `vcx/` | `vcx` público | Sí |
| Brix | `vcx/brix/`, versionado por `vcx`, y `blends/vc/brix/` con el código | `brix` privado, espejo detenido desde septiembre | No |
| Blends | `vcx/blends/`, versionado por `vcx`, y `~/VibeCoding/blends`, el precursor | `blends` privado, el precursor | No; el nombre está ocupado |
| Cellar | `vcx/cellar/`, versionado por `vcx` (situación inicial) | No existía; `denispaiva/cellar` público desde el 2026-11-09 | Sí, al cerrar E4 |
| Teyst | `vcx/solera/teyst/` | `solera-teyst` | Sí; su descripción todavía dice que el deploy sigue en `blends` |

Hallazgos del 2026-11-09:

- [H] `vcx/solera/docs/` (10 archivos, 264 KB) está ignorado por `vcx` y no pertenece a ningún repositorio. Respaldo local en `~/vcx-respaldos/solera-docs-2026-11-09.tar.gz`, SHA-256 `9cd1fbbc…c9ae0`, con `solera/README.md`. Es un respaldo en la misma máquina, no fuera de ella.
- [H] Colocar el precursor en `vcx/solera/` choca con ese `docs/` y con `solera/README.md`, que hoy versiona `vcx`.
- [H] 83 archivos versionados del precursor citan `denispaiva/blends`, no 24 como dice el paso 2 de VCX-D032. La cifra crece con el historial documental y hay que reclasificarla: los planes y reportes fechados son históricos y no se reescriben.
- [H] `core.hooksPath` del precursor sigue apuntando a `/Users/denispaiva/blends/.githooks`, una ruta que no existe.
- [H] `main` del precursor exige el check `teyst`, aunque Teyst ya se extrajo.
- [H] `git-filter-repo` no está instalado. Para un subárbol sin reescritura de autor alcanza `git subtree split`, que viene con Git.
- [H] Siete commits de merge de `vcx` público tienen autor `denispaiva@gmail.com`, con committer `noreply@github.com`: son merges hechos desde la web. El historial público ya expone ese correo.

## Orden

### Fase 0 · Coherencia barata

1. Respaldar `vcx/solera/docs/`: hecho localmente el 2026-11-09. Falta un respaldo fuera de la máquina, que llega con el repositorio `solera` en la fase 3.
2. Corregir la descripción de `solera-teyst` y poner una a `blends`. Es un cambio en GitHub: requiere autorización.
3. Herramienta de export: `git subtree split` para Cellar y Brix ola 1, mientras no haga falta reescribir autores.

### Fase 1 · Cellar, piloto

El más simple: no tiene nada en el precursor, su contenido ya es público dentro de `vcx` y VCX-D032 permite adelantarlo. Ensaya el mecanismo de incorporación que Brix y Blends repiten.

| Etapa | Qué hace | Estado |
|---|---|---|
| E1 Export local | `git subtree split --prefix=cellar` desde `main` de `vcx` | Hecho el 2026-11-09 desde `b6a28d2`: 4 commits, autor y committer `noreply`, Betterleaks 2.0.0-rc.1 sin hallazgos sobre el historial exportado |
| E2 Prueba aislada | Ningún enlace relativo sale del producto | Hecho: 20 enlaces salientes pasaron a URL absolutas de `vcx` (PR 8); export repetido desde `638a1fd`, 5 commits, sin hallazgos |
| E3 Publicación | Repositorio público `cellar`, push de `main`, protección | Hecho el 2026-11-09 con autorización del usuario: `denispaiva/cellar` público, `main` en `ca00822`, protegido (solo por PR, también para administradores; sin force-push ni borrado) |
| E4 Incorporación | En `vcx`: sacar `cellar/` del índice sin borrarlo, ignorar `/cellar/` y colocar el clon | Autorizado el 2026-11-09. Principios adoptados y `CLAUDE.md` en `cellar` (PR 1), con prueba de carga en clon aislado; 32 enlaces de `vcx` hacia `cellar/` pasan a URL de `denispaiva/cellar` |

[I] Los enlaces a `blends/docs/` apuntan a `vcx` mientras Blends viva ahí. Cuando Blends se extraiga en la fase 4, se actualizan en `cellar`.

[H] Resuelto en E4: `cellar/AGENTS.md` remitía a las instrucciones comunes de la raíz. En un clon aislado los agentes no las cargan solas; hay que incorporar una copia derivada de los principios, como hace Teyst.

### Fase 2 · Brix

Sigue las etapas E1 a E5 de VCX-D056 sin cambios: aparta el espejo, crea `brix` público con el historial filtrado de `vc/brix/` y lo fusiona con `vcx/brix/`. Desde E3, `vc/brix/` queda congelada en el SHA de corte.

Estado al 2026-11-09: E1, E2 y E3 hechos. `denispaiva/brix` es público con `v0.1.0`; `scripts/` quedó en Solera por decisión del usuario; corte en `4742bb99`. Detalle en el [reporte](../reports/2026-11-09-brix-e1-export.md). E4 hecho el mismo día: el producto se fusionó en `denispaiva/brix`, las evaluaciones pasaron a `docs/tooling/` y `vcx/brix/` es un clon ignorado por la raíz. E5 en PR (Teyst consume el tarball de `v0.1.0`; `score-run.mjs` usa `brix/`). Pendiente aparte: la ola 2 (`vc/tools`).

### Fase 3 · Preparación del precursor (hecha)

Medición previa del 2026-11-09, en solo lectura. Su detalle incluye datos de infraestructura y se custodia fuera de este repositorio público. Encontró dos bloqueantes:

- La regla de no escribir en el precursor. VCX-D062 la levantó solo para esta fase.
- Dos identidades de deploy en la nube autorizaban por el nombre del repositorio. Se migraron al ID el mismo día, con autorización del usuario, y se verificaron con deploys a los entornos de desarrollo, con y sin la autorización por nombre.

Entró en los PR 310 a 313 de `denispaiva/blends`:

- Baja de 18 evaluaciones de tooling vencidas, que bloqueaban la gobernanza.
- `vc/teyst/` congelada, en lugar de retirarla: el tooling la usa como proyecto de referencia.
- Las herramientas del tren derivan el nombre del repositorio.
- Los documentos de la instancia, que vinieron de `vcx/solera/docs/`.

El retiro completo del job y el check `teyst` queda como deuda.

### Fase 3 bis · Extraer, archivar y `solera` limpio (VCX-D063)

El renombre del precursor a `solera` se descartó: la instancia heredaría todo lo que no le corresponde. En su lugar, cada paso con su propia autorización:

1. **`solera` nuevo**, privado y vacío, con lo que es de la instancia: los documentos de la instancia, FinOps, ideas e iniciativas. Checkout en `vcx/solera/`, con `/teyst/` y los demás `solera-*` ignorados. `vcx` deja de versionar `solera/README.md` e ignora `/solera/` entero. Hecho el 2026-11-09: `denispaiva/solera`, privado, colocado en `vcx/solera/`.
2. **Proyectos vivos a `solera-<proyecto>`**, como Teyst: Melquisedec y Salmanazar con sus deploys, cuyas identidades en la nube pasan al ID del repositorio nuevo, y Pinot Index, reutilizando su espejo si conviene. Hecho el 2026-11-09 para Melquisedec y Salmanazar: repositorios privados propios con historia, CI y deploy. Sus identidades en la nube autorizan solo al repositorio nuevo, lo que se verificó con deploys a desarrollo, y los workflows del precursor quedaron deshabilitados. Pinot Index, el mismo día: se reutilizó su espejo privado, que entró por fast-forward, renombrado a `solera-pinot-index`.
3. **Ola 2 de Brix:** las capacidades de `vc/tools` que sigan en uso pasan a `brix`. Las demás quedan en el archivo. Medida el 2026-11-10 ([reporte](../reports/2026-11-10-brix-ola2-medicion.md)): ningún repositorio vivo usa `vc/tools/`, así que nada pasa a Brix. Antes de archivar hay que desacoplar cinco herramientas que leen el checkout del precursor.
4. **Fase 4**, abajo: el núcleo de Blends al `blends` público.
5. **Archivo:** el precursor se renombra a `blends-precursor` y se archiva, privado y con toda su historia, ramas y tags. Esto libera el nombre `blends`, así que va antes de crear el `blends` público.

### Fase 4 · Blends público

Paso 3 de VCX-D032. Export del núcleo desde el precursor (archivado o no) con historial filtrado, repositorio público nuevo e incorporación con el mismo mecanismo E4 sobre `vcx/blends/`.

Medición previa del 2026-11-10 ([reporte](../reports/2026-11-10-blends-publico-medicion.md)): el historial de los estándares contiene infraestructura e importes, así que se propone historia nueva (B') y publicar el método sin la maquinaria ejecutable, que no tiene consumidores.

## Resultado esperado

Cada carpeta de primer nivel de `vcx/` es un repositorio con el mismo nombre en GitHub: `vcx`, `blends`, `brix` y `cellar` públicos; `solera` y `solera-*` privados.

## Riesgos

- Dos fuentes editables de Brix y Blends mientras el precursor no esté archivado. El `git diff` de corte detecta la divergencia, no la impide.
- Lo publicado es irreversible: el scan cubre el historial exportado, no solo el árbol final.
- Las referencias `uses:` de Actions no siguen un renombre: antes de archivar el precursor, ningún workflow vivo puede depender de él.
- El cupo de Actions es uno por cuenta. Los repositorios públicos con runners estándar no lo consumen.

Nota orientativa según VCX-P2: 7 de 10. Descuentos: la ola 2 de Brix sigue sin diseñar, y las 83 referencias no están clasificadas entre vivas e históricas.
