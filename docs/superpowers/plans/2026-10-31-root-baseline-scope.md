# Alcance de ejecución: commit base documental de la raíz

> **Para agentes ejecutores:** aplicar `superpowers:executing-plans` de forma directa y secuencial cuando este alcance esté autorizado. Las casillas registran ejecución, no aprobación.

**Objetivo:** preservar el estado documental de VCX mediante un único commit local en el repositorio raíz y comprobar que sus archivos pueden recuperarse sin pérdida.

**Arquitectura:** repositorio documental en la raíz, con excepción transitoria para los documentos de producto conforme a VCX-D026. Sin repositorios de producto, gitlinks, remotos o exclusiones de productos en esta etapa.

**Tecnologías:** Git local, Markdown, OPML y comprobaciones temporales de inventario, hashes y recuperación. Sin dependencias nuevas o pruebas que reproduzcan el texto.

**Base:** [VCX-D026](../../decisions/README.md) y pasos 1–2 de la [secuencia acordada](../../architecture/repository-map.md#secuencia-acordada-para-preservar-y-versionar).

**Fecha:** 2026-10-31. **Estado al corte documental:** alcance autorizado el 2026-10-31 en este chat con Codex mediante «si», en respuesta a la pregunta explícita de ejecutar únicamente este alcance. Git ya está inicializado en la raíz; el commit y su recuperación están pendientes de comprobar en este corte. El OK previo solo había autorizado preparar el alcance y la ratificación documental de VCX-D026 no había autorizado ejecutarlo. La entrega final identificará la revisión y resultados, sin modificar después este corte para incorporar su propio SHA.

## Superficie permitida

- Directorio de trabajo único: `/Users/denis/VibeCoding/vcx`.
- Crear exclusivamente el repositorio Git de esa raíz, con rama inicial `main`, índice y primer commit local.
- Registrar los 39 archivos de la lista siguiente, incluidos temporalmente 5 de Blends, 5 de Brix y 8 de Cellar. Los otros 21 son documentación de raíz, incluido `cellars/README.md` y este alcance.
- Registrar la autorización real y el estado de inicialización en `docs/decisions/README.md`, `README.md`, `docs/architecture/overview.md`, `docs/architecture/repository-map.md` y este alcance, únicamente en los pasajes de estado afectados. Conservar la historia de autorizaciones. No cambiar principios, contratos, contenido de productos ni clasificación de decisiones.
- Usar un directorio temporal creado mediante `mktemp -d` bajo el temporal del sistema para la extracción de verificación y evidencia transitoria. No usar el precursor ni conservar otra fuente editable o respaldo documental permanente.

La presencia de los documentos de producto en la historia raíz es intencional. Su congelamiento de transferencia, retirada del índice y exclusión corresponden a fases posteriores; este commit no realiza esos pasos.

## Lista explícita del commit

Rutas relativas a VCX. No usar `git add .`, `git add -A` ni agregar carpetas recursivamente. Si aparece un archivo nuevo, un symlink, un repositorio anidado o una discrepancia con esta lista, detenerse y revisar el alcance antes de incorporarlo.

```text
AGENTS.md
README.md
blends/AGENTS.md
blends/README.md
blends/docs/architecture-and-finops.md
blends/docs/idea-intake.md
blends/docs/idea-to-project.md
brix/AGENTS.md
brix/README.md
brix/docs/commands.md
brix/docs/idea-intake.md
brix/docs/reference-architecture.md
cellar/AGENTS.md
cellar/README.md
cellar/docs/initiative-model.md
cellar/templates/cellar/README.md
cellar/templates/finops/README.md
cellar/templates/idea/README.md
cellar/templates/initiative/AGENTS.md
cellar/templates/initiative/README.md
cellars/README.md
docs/architecture/current-system-mapping.md
docs/architecture/interoperability.md
docs/architecture/overview.md
docs/architecture/repository-map.md
docs/architecture/responsibility-matrix.md
docs/decisions/README.md
docs/executive-pitch.md
docs/exports/vcx-ecosystem.opml
docs/naming.md
docs/references/enology-glossary-source.md
docs/sources.md
docs/superpowers/plans/2026-10-30-blends-cellar-curation.md
docs/superpowers/plans/2026-10-30-vcx-foundation.md
docs/superpowers/plans/2026-10-31-root-baseline-scope.md
docs/superpowers/reports/2026-10-30-blends-cellar-curation.md
docs/superpowers/reports/2026-10-30-vcx-foundation.md
docs/superpowers/specs/2026-10-30-cellar-blends-first-journey-design.md
docs/vision.md
```

## Exclusiones y límites

No registrar `.DS_Store`, secretos, datos operativos, credenciales, archivos de entorno, logs, temporales ni contenidos del precursor. No crear todavía `.gitignore`: la lista explícita limita el índice, mientras los metadatos existentes permanecen sin seguimiento. No borrarlos para obtener un estado limpio.

No inicializar `blends/`, `brix/` o `cellar/`; no crear clones, ramas de incorporación, submódulos, remotos, tags o instancias; no ejecutar fetch, push, trenes, `queue`, hooks del precursor o despliegues; no mover o retirar archivos del índice. La carpeta `/Users/denis/VibeCoding/blends` no recibe ninguna escritura ni necesita inspección para este commit.

No configurar identidad de Git, credenciales, firma o permisos por inferencia. Usar la identidad existente solo después de comprobarla; si falta o requiere una decisión, detenerse y pedir ese dato concreto. No deshabilitar controles para obtener el commit. Si el sandbox exige aprobación de escritura sobre `.git`, solicitarla para el comando concreto: aprobar el alcance no elude los permisos efectivos del entorno.

## Focos de verificación

1. Operar por error en otro repositorio: comprobar ruta física, ausencia de Git previo o heredado y variables de entorno que redirijan Git.
2. Incorporación accidental: lista exacta de rutas y modos regulares; ningún gitlink, symlink o archivo ajeno.
3. Commit que no protege los bytes esperados: cotejar contenido del índice y extracción posterior con hashes calculados sobre el estado final autorizado.
4. Cambios concurrentes durante la preparación: detectar diferencias y detenerse sin sobrescribir o resetear trabajo.
5. Confundir protección con autorización adicional: entregar la revisión base y detenerse antes de clones, exclusiones o migraciones; Git local no protege contra pérdida del disco.

## Tarea única — Crear y comprobar la línea base

### 1. Comprobar precondiciones y registrar autorización

- [x] Leer nuevamente la autorización explícita de este alcance, registrar cita literal y procedencia real en el registro, sin ampliar su objeto.
- [x] Revalidar el inventario completo del workspace: 39 documentos permitidos; todo lo demás queda fuera. Identificar cambios concurrentes y comparar con la lista, no adoptar automáticamente lo nuevo.
- [x] Comprobar que la ruta física de trabajo es la indicada; no existen `.git` en la raíz, sus padres o productos ni un índice previo. Si existe Git, no reinicializarlo: revisar ese estado y el alcance.
- [x] Comprobar que las variables `GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE`, redirecciones de objetos y configuración no desvían la operación. Revisar configuración efectiva de identidad, firma, filtros, templates y hooks aplicables sin exponer secretos. No ejecutar un hook desconocido o una integración externa por accidente.
- [x] Confirmar que Git está disponible y que se pueden usar sus comandos sin instalar herramientas. La operación inicial se realiza sobre una raíz sin historia; no requiere crear un worktree desde un repositorio inexistente.

### 2. Inicializar y preparar el contenido exacto

Comando de inicialización autorizado y ejecutado en esta etapa:

```sh
git init --initial-branch=main /Users/denis/VibeCoding/vcx
```

- [x] Ejecutar la inicialización solo tras las precondiciones y comprobar que `--show-toplevel` devuelve la raíz exacta y que la rama es `main`.
- [x] Comprobar hooks/templates y configuración resultantes antes del commit. No copiar ni activar el gobierno del precursor en el repositorio documental raíz.
- [x] Actualizar únicamente los pasajes de estado de los documentos permitidos: Git inicializado y preservación aún pendiente de comprobar, con autorización de ejecución separada de la ratificación documental anterior. No afirmar éxito antes de verificarlo.
- [ ] Cerrar la edición, calcular hashes SHA-256 de los 39 archivos finales y mantener ese inventario en evidencia temporal. No incluir el inventario como archivo adicional en el commit ni calcular una autorreferencia imposible del hash del commit dentro de su propio contenido.
- [ ] Preparar las 39 rutas explícitas mediante `git add --`, usando la lista de este alcance, y comprobar que ninguna fue omitida por exclusiones globales. No forzar una exclusión silenciosamente.

Comandos de inspección propuestos, desde la raíz:

```sh
git rev-parse --show-toplevel
git branch --show-current
git diff --cached --name-status
git ls-files --stage
git diff --cached --check
git diff --cached --stat
```

- [ ] Revisar el diff completo preparado y los posibles datos sensibles antes del primer commit. Los nombres o explicaciones sobre secretos no prueban que exista una credencial; no desactivar un control para silenciar un hallazgo real.
- [ ] Comparar el índice con la lista exacta: 39 archivos regulares, sin modos de gitlink o symlink. Cotejar sus bytes con los hashes de trabajo, detectando transformaciones de filtros o finales de línea. Si no coinciden, revisar sin hacer el commit.
- [ ] Volver a comprobar los archivos de trabajo inmediatamente antes del commit. Cualquier diferencia respecto del corte final exige conciliar el cambio, no descartarlo.

### 3. Registrar un único commit local

Mensaje propuesto, en español con prefijo estructurado:

```sh
git commit -m "docs: preserva la base documental de VCX"
```

- [ ] Crear el commit sin omitir hooks o firmas exigidos. Si falla, conservar archivos y diagnóstico; no repetir indiscriminadamente ni modificar identidad, hooks o configuración por cuenta propia.
- [ ] Comprobar que hay exactamente un commit raíz sin padres, en `main`, con las 39 rutas exactas y sin remoto configurado. Inspeccionar el resultado del commit: los hooks no deben haber cambiado archivos o agregado contenido fuera de alcance.

### 4. Probar integridad y recuperación

Comandos de inspección propuestos:

```sh
git rev-parse HEAD
git rev-list --count HEAD
git rev-list --parents -n 1 HEAD
git ls-tree -r --full-tree HEAD
git remote -v
git status --short --untracked-files=all
git fsck --full
```

- [ ] Extraer `git archive HEAD` en un directorio temporal nuevo y vacío; no ejecutar `checkout`, `restore` o `reset` sobre el workspace para probar recuperación.
- [ ] Comparar rutas, modos y bytes recuperados con los 39 archivos del corte final: igualdad total de SHA-256. Comprobar además que la extracción no contiene metadatos o archivos fuera de la lista.
- [ ] Comprobar que el workspace conserva sus documentos y que no hay diferencias rastreadas o preparadas. `.DS_Store` puede continuar sin seguimiento; un archivo inesperado o un cambio documental se informa y no se borra.
- [ ] Entregar SHA del commit, número de archivos, resultados de recuperación y límites. Registrar esta evidencia en el cierre de la ejecución, sin reescribir el commit para insertar su propio SHA ni crear automáticamente un segundo commit de reporte. Los pasajes que indiquen preservación pendiente reflejan el momento del commit; la aceptación posterior queda identificada por la revisión en la entrega.

## Recuperación ante fallos

Si falla antes del commit, conservar los archivos y el repositorio parcial; no borrar `.git`, limpiar carpetas o resetear. Registrar qué pasos se realizaron y revisar antes de reanudar. Si hay un fallo después del commit, usar extracción o lectura de la revisión conocida para diagnosticar y recuperar a una ubicación temporal, sin sobrescribir trabajo posterior.

No usar `git clean`, `reset --hard`, `rm` o reescritura de historia para volver al estado anterior. La necesidad de eliminar el repositorio recién creado o corregir un commit con contenido fuera de alcance exige un alcance explícito propio; el destino no se publica en esta etapa.

## Cierre y autorización solicitada

El resultado aceptable es un único commit local recuperable, 39 documentos exactos, cero dependencias de objetos externos, ningún gitlink y ninguna modificación del precursor o inicialización de productos. No demuestra todavía portabilidad de los productos ni respaldo fuera de la máquina.

La autorización que se solicita es ejecutar únicamente esta tarea en `/Users/denis/VibeCoding/vcx`, incluidos la creación de `.git`, preparación del índice, un commit base y sus verificaciones temporales. Clones, remotos, exclusiones, movimientos y la migración siguen fuera de alcance. La preparación de este documento no consume esa autorización.
