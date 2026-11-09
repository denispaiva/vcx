# Migración de Brix, Blends y Cellar a `vcx/` con correspondencia en GitHub

Fecha: 2026-11-09. Estado: plan aceptado por el usuario en VCX-D059. Ordena decisiones vigentes (VCX-D025, D030, D032, D036, D053, D056, D057); no las reemplaza. Cada fase con efecto externo requiere autorización propia, con repositorio, ruta y alcance.

Etiquetas: [H] hecho medido; [I] interpretación; [P] propuesta.

## Situación medida

| Pieza | Local | GitHub | Coincide |
|---|---|---|---|
| Raíz | `vcx/` | `vcx` público | Sí |
| Brix | `vcx/brix/`, versionado por `vcx`, y `blends/vc/brix/` con el código | `brix` privado, espejo detenido desde septiembre | No |
| Blends | `vcx/blends/`, versionado por `vcx`, y `~/VibeCoding/blends`, el precursor | `blends` privado, el precursor | No; el nombre está ocupado |
| Cellar | `vcx/cellar/`, versionado por `vcx` | No existe | No |
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
| E2 Prueba aislada | Ningún enlace relativo sale del producto | Los 20 enlaces salientes pasan a URL absolutas de `vcx` en esta misma entrega; hay que volver a exportar después del merge |
| E3 Publicación | Repositorio público `cellar`, push de `main`, protección | Requiere autorización |
| E4 Incorporación | En `vcx`: sacar `cellar/` del índice sin borrarlo, ignorar `/cellar/` y colocar el clon | Requiere autorización |

[I] Los enlaces a `blends/docs/` apuntan a `vcx` mientras Blends viva ahí. Cuando Blends se extraiga en la fase 4, se actualizan en `cellar`.

[P] Pendiente de E4: `cellar/AGENTS.md` remite a las instrucciones comunes de la raíz. En un clon aislado los agentes no las cargan solas; hay que incorporar una copia derivada de los principios, como hace Teyst.

### Fase 2 · Brix

Sigue las etapas E1 a E5 de VCX-D056 sin cambios: aparta el espejo, crea `brix` público con el historial filtrado de `vc/brix/` y lo fusiona con `vcx/brix/`. Desde E3, `vc/brix/` queda congelada en el SHA de corte.

### Fase 3 · Precursor → `solera`

1. Llevar `vcx/solera/docs/` y `README.md` al repositorio de la instancia, y que `vcx` ignore `/solera/` entero (VCX-D059).
2. Colocar el clon del precursor en `vcx/solera/`, con `/teyst/` en su `.gitignore`, y corregir `core.hooksPath`.
3. Retirar `vc/teyst/` dejando un puntero y sacar el check `teyst` de la protección en la misma entrega.
4. Actualizar las referencias vivas a `denispaiva/blends`, los remotos, los worktrees y las tareas programadas; después, renombrar en GitHub.
5. Verificar `queue`, trenes y workflows con el nombre nuevo.

Necesita los trenes detenidos durante el renombre.

### Fase 4 · Blends público

Paso 3 de VCX-D032. El repositorio nuevo termina la redirección del nombre viejo: todo lo de la fase 3 tiene que estar actualizado antes. Incorporación con el mismo mecanismo E4 sobre `vcx/blends/`.

## Resultado esperado

Cada carpeta de primer nivel de `vcx/` es un repositorio con el mismo nombre en GitHub: `vcx`, `blends`, `brix` y `cellar` públicos; `solera` y `solera-*` privados.

## Riesgos

- Dos fuentes editables de Brix y Blends mientras el tren del precursor siga activo. El `git diff` de corte detecta la divergencia, no la impide.
- Lo publicado es irreversible: el scan cubre el historial exportado, no solo el árbol final.
- Las referencias `uses:` de Actions no siguen el renombre: Blends público va después.
- El cupo de Actions es uno por cuenta. Los repositorios públicos con runners estándar no lo consumen.

Nota orientativa según VCX-P2: 7 de 10. Descuentos: la ola 2 de Brix sigue sin diseñar, y las 83 referencias no están clasificadas entre vivas e históricas.
