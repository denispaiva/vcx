# Adopción de VCX en un proyecto nuevo

Fecha: 2026-11-16. Estado: **propuesta**, no ratificada. El usuario pidió el checklist en un chat con Claude, ante «¿Escribo el checklist de adopción para un proyecto nuevo?», con la respuesta «Sí, escribirlo». Este documento reconstruye lo que ya funciona en los proyectos de Solera (Teyst, Melquisedec, Salmanazar, Pinot Index y Tintum): no agrega reglas, solo enlaza las decisiones que las fijan. No autoriza crear repositorios, desplegar ni gastar; cada uno de esos actos conserva su autorización propia, según VCX-P7.

No existe un instalador, generador ni `brix init`. Todo se hace a mano. Recién conviene automatizarlo después de aplicar este checklist a un segundo proyecto y medir qué pasos se repiten sin cambios (VCX-P3).

## Qué viaja y qué no

| Pieza | Mecanismo | Fuente única |
|---|---|---|
| Principios VCX-P1 a P9 | Copia derivada en el `AGENTS.md` del proyecto, con versión y origen | [AGENTS.md de la raíz](../../AGENTS.md#principios-transversales-de-vcx) |
| CLI de Brix | Tarball en `vendor/` con `procedencia.md`, o instalación global desde un clon | [denispaiva/brix](https://github.com/denispaiva/brix#instalación) |
| Skills de Brix | Copia por proyecto con `PROVENANCE.md` y SHA del original (VCX-D033, punto 5) | `brix/.agents/skills/` |
| Plantillas de Cellar | Copia de la plantilla necesaria, con los marcadores `{{...}}` resueltos | [Cellar](https://github.com/denispaiva/cellar#plantillas-documentales) |
| Admisiones de tooling | **No viajan.** Se consultan en su registro | [docs/tooling/evaluations/](../tooling/evaluations/) y la [matriz](tooling-matrix.md) |
| Configuración local (`.claude/`, MCP del proyecto, `.env`, secretos de CI) | **No viaja.** Se declara de nuevo en cada repositorio | Cada proyecto |

## Caso A · proyecto nuevo dentro de Solera

Todos los pasos se ejecutan en el repositorio del proyecto. La raíz `vcx` no se toca, salvo para registrar decisiones.

### 1. Identidad y ubicación

- [ ] Elegir el identificador técnico según el [criterio de nombres](../naming.md). El repositorio se llama `denispaiva/solera-<proyecto>` y el checkout queda en `vcx/solera/<proyecto>/` (VCX-D057).
- [ ] Comprobar que el nombre esté libre en GitHub, en solo lectura.
- [ ] Crear el repositorio **privado** (VCX-D032: las instancias y los proyectos nunca se vuelven públicos). *Requiere autorización.*
- [ ] Si va a tener CI con acceso a la nube, atar WIF a `repository_id`, no al nombre, para que un renombre no corte el deploy (VCX-D057).

**Verificación:** `git -C vcx/solera/<proyecto> remote get-url origin` devuelve `solera-<proyecto>`, y `vcx/solera/.gitignore` ignora la carpeta.

### 2. Instrucciones y principios

- [ ] Escribir un `AGENTS.md` con la misión, la visión y el estado del proyecto, más una sección «Principios transversales de VCX» que diga: *Copia derivada de `vcx/AGENTS.md`, versión documental `<versión>`, `<fecha>`. No es una fuente independiente: se actualiza desde el origen, de forma explícita.* Debajo, el texto de VCX-P1 a P9 sin cambios.
- [ ] Escribir un `CLAUDE.md` que contenga solo `@AGENTS.md`.

**Verificación:** abrir una sesión nueva **desde la carpeta del proyecto** y pedir que cite VCX-P5. Hay que comprobar la carga en el IDE que se use; la carpeta padre no garantiza que se herede (ver [interoperabilidad](interoperability.md#preparación-de-productos-independientes)). En Codex: `codex debug prompt-input`.

### 3. Guardia de secretos

- [ ] Copiar `.betterleaks.toml` y `.githooks/pre-commit` de otro proyecto de Solera y ajustar el `title`.
- [ ] Ejecutar `git config core.hooksPath .githooks`. Requiere Betterleaks 2.0.0-rc.1.
- [ ] Agregar `.env` al `.gitignore` y versionar solo `.env.example`.

**Verificación:** un commit de prueba con un secreto falso tiene que ser rechazado. Descartar el commit después.

### 4. Brix

- [ ] Para ejecución o CI: `npm pack` desde un tag de `denispaiva/brix`, renombrar el archivo y guardarlo en `vendor/` con un `procedencia.md` que registre el tag, el commit, el sha256 y cómo se regenera.
- [ ] Para uso interactivo: alcanza con `npm install --global ./packages/cli` desde el clon de Brix.
- [ ] Declarar un `brix.config.json` solo si el layout difiere de los valores por defecto.
- [ ] Importar solo lo que el paquete exporte. Hoy no declara `exports`, y los proyectos que importan rutas internas acumulan deuda declarada.

**Verificación:** `node_modules/.bin/brix --help` (o `brix --help`) responde sin red y sin `vcx/` como carpeta padre.

### 5. Skills

- [ ] Copiar solo las skills que el proyecto vaya a usar a `.agents/skills/<skill>/` y crear el symlink de directorio `.claude/skills → ../.agents/skills`, como en Brix.
- [ ] Llevar el `PROVENANCE.md` de cada skill y agregarle el SHA de Brix del que se copió.
- [ ] Antes de copiar, revisar que la admisión siga vigente (paso 6). Por ejemplo, `brix-llm-council` tiene `approved_with_exception`, con autorización por corrida.

**Verificación:** la skill aparece listada en una sesión nueva abierta desde el proyecto.

### 6. Tooling: consultar, no volver a registrar

- [ ] Cruzar las herramientas que vaya a usar el proyecto con [docs/tooling/evaluations/](../tooling/evaluations/): estado, `expiresAt` y motivo.
- [ ] **Reevaluar solo** si la admisión venció, si el proyecto no existía cuando se evaluó la herramienta o si el motivo del rechazo dependía del contexto, por ejemplo de un stack distinto. La reevaluación se hace con el envoltorio de VCX-D035 y queda en el mismo registro, no en el proyecto.
- [ ] Aplicar la [política Free Tier first](../../finops-policy.md#free-tier-first-y-eficiencia-de-suscripciones) antes de sumar MCP o servicios pagos.

**Verificación:** cada herramienta que use el proyecto tiene una decisión vigente o una excepción registrada con su autoridad.

### 7. Registro en la instancia y método

- [ ] Si el proyecto nace de una idea, seguir el [ingreso](https://github.com/denispaiva/blends/blob/main/docs/idea-intake.md): primero la plantilla de idea, después el consejo y la confirmación humana. Recién entonces se registra como iniciativa.
- [ ] Crear `.roadmap.json` copiando la estructura de un proyecto existente. Hoy su esquema lo consume `brix finops`, y su definición canónica sigue en el kernel del precursor.
- [ ] Agregar la fila al cuadro «Proyectos» del README de Solera.

**Verificación:** el proyecto figura en el README de Solera y su `.roadmap.json` pasa la validación del paso 8.

### 8. FinOps

- [ ] Crear `finops/billing-ledger.json` con los providers del proyecto. Lo que ya está en el ledger compartido no se cuenta dos veces.
- [ ] Declarar los límites de consumo antes de comprometer recursos (VCX-P8). Los pagos reales van al ledger privado, fuera de los repos (VCX-D042).

**Verificación:** `brix finops validate finops/billing-ledger.json`, y desde Solera `brix finops validate --portfolio .`.

### 9. CI

- [ ] `brix ci --watch <globs> --entrypoint <ruta>` genera `.github/workflows/ci.yml`. Agregar tests, lint y la validación del ledger.
- [ ] Los runners de un repositorio privado consumen cuota de Actions (VCX-D032). Hay que medir el costo antes de agregar jobs pesados.
- [ ] Si hay deploys: grupo de concurrencia por target y guardas de ref, CI verde y duplicados, como en Teyst.

**Verificación:** el primer push dispara el workflow y pasa.

### 10. Ensayo aislado

- [ ] Clonar el repositorio en una carpeta temporal fuera de `vcx/`, instalar con `npm ci` (o equivalente) y correr tests y `brix --help`.
- [ ] Anotar cualquier ruta que apunte a `../`, a `vcx/` o al precursor. Cada una es una dependencia implícita, y se corrige o se declara como deuda.

**Verificación:** el proyecto funciona sin carpeta padre. Recién entonces se puede afirmar que es portable.

## Caso B · otro equipo u otro portfolio

Una instancia de Cellar por workspace (VCX-D036): otro equipo arma su propio `vcx/`, con su instancia propia. Antes de aplicar el caso A:

- [ ] Resolver y registrar cómo recibe los principios: fuente, revisión, quién aprueba las actualizaciones y qué pasa si la fuente no está disponible. Es el [disparador de VCX-D023](interoperability.md#distribución-de-principios-a-instancias-externas). El mecanismo sigue sin elegirse (VCX-D008); la copia derivada del paso 2 alcanza si se registra como decisión.
- [ ] Crear el repositorio de la instancia desde la [plantilla de Cellar](https://github.com/denispaiva/cellar/blob/main/templates/cellar/README.md), con su identidad, custodia y recuperación.
- [ ] Decidir si va a usar el registro de tooling de este workspace (solo lectura, por URL pública) o uno propio. Las admisiones de este portfolio no autorizan herramientas a otro equipo (VCX-P7).
- [ ] Cumplir en Blends, Brix y Cellar el [ensayo aislado de productos](interoperability.md#preparación-de-productos-independientes), que todavía no se hizo.

## Deuda conocida

| Deuda | Efecto | Disparador para resolverla |
|---|---|---|
| Las copias derivadas no avisan cuando el original cambia | Principios y skills desactualizados sin que nadie lo note | Tercer consumidor de la misma copia, o el primer cambio de versión de los principios |
| Brix no declara `exports` | Los proyectos importan rutas internas | Ya en curso en `denispaiva/brix` |
| El esquema de `.roadmap.json` vive en el precursor | El proyecto nuevo copia la estructura sin una fuente publicada | Migración del kernel a Blends |
| La matriz de tooling es transitoria (VCX-D028) y no indica qué aplica a cada tipo de proyecto | Hay que leerla entera | Campo `phases` en el inventario, al preparar los repositorios independientes |
| No hay ensayo aislado de los productos | La portabilidad no está demostrada | Antes del primer equipo externo |
