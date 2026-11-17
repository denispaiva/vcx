# Chequeo de integridad del workspace

Fecha: 2026-11-16. Estado: **diseño propuesto**, sin implementar ni ratificar. El usuario preguntó en un chat con Claude «No deberíamos tener algún comando health de vcx que recorra la integridad de las piezas?» y, ante «¿Implemento la primera versión de scripts/health.py con estos cuatro chequeos?», respondió «Primero el diseño». No autoriza implementar, activar hooks en otros repositorios ni cambiar `AGENTS.md` de proyectos.

Etiquetas: [H] hecho medido; [I] interpretación; [P] propuesta.

## Problema

Las piezas de VCX viajan como copias con procedencia (ver el [checklist de adopción](../../architecture/project-adoption.md#qué-viaja-y-qué-no)). Nada comprueba que esas copias sigan siendo fieles al original ni que cada checkout tenga las protecciones que se le exigen. Hoy existen chequeos parciales que no cubren eso: `scripts/pending_triggers.py` (fechas y vencimientos, VCX-D058), Betterleaks por repositorio y `brix finops validate`.

Medición del 2026-11-16, en solo lectura sobre los checkouts locales:

| Pieza | Resultado |
|---|---|
| [H] Texto de VCX-P1 a P9 en 9 `AGENTS.md` (raíz de Solera, 5 proyectos, Blends, Brix, Cellar) | Idéntico al de la raíz en los 9 |
| [H] Declaración de origen de esas copias | Dos formatos: Teyst declara la versión documental `1.1.0`; Melquisedec declara el SHA `585264d` de `vcx`. Un script no puede leer el origen de forma uniforme |
| [H] `vendor/*.tgz` | Solo Teyst, 3 tarballs. El sha256 de `brix-cli-v0.1.0.tgz` coincide con su `procedencia.md` |
| [H] Copias de skills de Brix en consumidores | **Ninguna.** Ningún repositorio fuera de `brix/` tiene `.agents/skills/` |
| [H] Remotos | Los 10 checkouts siguen la regla: productos con su nombre, Solera `solera`, proyectos `solera-<p>` (VCX-D057) |
| [H] `core.hooksPath` | Activo en la raíz, Solera, Teyst y Tintum. **Vacío** en Melquisedec, Pinot Index, Salmanazar, Blends, Brix y Cellar, y ninguno de esos seis escanea secretos en su CI |

[I] El último hallazgo es el más grave y no depende de que exista el health: seis repositorios no tienen compuerta de secretos local ni en CI. Se trata en [Pendientes](#pendientes), por separado.

## Objetivo

Un comando de solo lectura que, desde la raíz, informe en un solo reporte si cada pieza distribuida coincide con su origen y si cada checkout cumple la topología y las protecciones declaradas. Avisa; no corrige, no bloquea commits ni decide.

**Criterio de aceptación observable:** sobre el workspace actual, el comando reporta exactamente los hallazgos de la tabla anterior, ni más ni menos. Sobre un fixture con un desvío sembrado en cada chequeo, reporta ese desvío con su código.

## Alternativas

| Opción | Costo | Por qué no, o cuándo sí |
|---|---|---|
| A · Checklist manual | Cero código | Ya existe en el checklist de adopción; nadie lo vuelve a correr. Sirve con un solo proyecto, no con diez checkouts |
| **B · `scripts/health.py` en la raíz** | Un archivo, sin dependencias | **Elegida.** Opcional, como `pending_triggers.py`: ningún producto lo necesita para funcionar, así que no convierte la raíz en dependencia ejecutable |
| C · `brix health` | Comando en el CLI | Brix «no presupone un Cellar» ni la topología de este workspace (README de Brix). Meterle reglas de VCX-D057 lo acopla a una instancia |
| D · Un job de CI por repositorio | Un workflow en cada repo | El CI de un repo no ve a los otros, que es justo lo que hay que comparar. Además consume cuota en los privados |

## Diseño

### Inventario: de dónde sale la lista de repositorios

Sin descubrimiento implícito (VCX-P3). La lista sale de las dos declaraciones que ya son operativas y llevan su decisión en un comentario:

- `vcx/.gitignore`: `/blends/`, `/brix/`, `/cellar/`, `/solera/`.
- `vcx/solera/.gitignore`: las líneas `/<proyecto>/` del bloque de checkouts. Se ignoran los patrones con comodín, como `/*-wt-*/`.

Si una entrada no tiene checkout local, es un aviso: `TOPO-ABSENT`. Si una carpeta tiene `.git` y no está declarada, es un error: `TOPO-UNDECLARED`.

Los patrones con comodín no suman repositorios al inventario, pero sí cuentan como declarados para `TOPO-UNDECLARED`: un worktree como `solera/teyst-wt-activa`, cubierto por `/*-wt-*/`, no es un error. Para compararlos se usa `fnmatch` sobre el nombre de primer nivel. Las negaciones (`!`) no cuentan como declaración. Corrección del 2026-11-16, después de la revisión de la primera implementación.

### Chequeos de la primera versión

| Código | Chequeo | Severidad | Fuente de la regla |
|---|---|---|---|
| `PRIN-TEXT` | El bloque de VCX-P1 a P9 de cada `AGENTS.md` es idéntico al de la raíz en el `HEAD` local | error | VCX-P9; [AGENTS.md](../../../AGENTS.md#principios-transversales-de-vcx) |
| `PRIN-ORIGIN` | La copia declara el SHA de `vcx` del que deriva, y ese SHA existe en la historia local | aviso si declara solo la versión; error si el SHA no existe | [Interoperabilidad](../../architecture/interoperability.md#distribución-de-principios-a-instancias-externas) |
| `VEND-HASH` | Cada `vendor/*.tgz` tiene una entrada en `vendor/procedencia.md` y su sha256 coincide | error | VCX-D046 |
| `TOPO-REMOTE` | `origin` es `denispaiva/<p>` para productos y Solera, y `denispaiva/solera-<p>` para proyectos | error | VCX-D057 |
| `TOPO-HOOKS` | `core.hooksPath` está definido y la ruta existe | aviso si falta; error si apunta a una ruta inexistente (el caso de SEC-08) | [Inventario de controles](../../architecture/security-controls-inventory.md), SEC-03 y SEC-08 |

Además, el comando **llama** a `scripts/pending_triggers.py --window 14` e incorpora su salida bajo el código `PEND`. No reimplementa esa lógica.

Quedan fuera de la primera versión, con su disparador:

- **Skills** (`SKIL-PROV`): hoy no hay ningún consumidor que verificar. Se agrega con la primera copia de una skill fuera de `brix/`.
- **Ledgers FinOps:** requiere el CLI de Brix instalado y ya tiene su comando, `brix finops validate --portfolio`. Se agrega si un desvío de ledger llega a un commit sin detectarse.
- **Enlaces, matriz de tooling y tests de cada proyecto:** cada uno ya se ve o tiene su CI.

### Extracción del bloque de principios

El bloque va desde la línea que empieza con `1. **VCX-P1` hasta la línea anterior al primer encabezado `## ` o a la línea que empieza con `Adopción y procedencia`. Se normalizan los finales de línea y se compara con SHA-256. El texto introductorio (versión y procedencia) no entra al hash; para eso está `PRIN-ORIGIN`.

### Interfaz

```bash
python3 -I scripts/health.py [--root <ruta>] [--json] [--only <códigos>]
```

- **Salida de texto:** una línea por hallazgo con código, severidad, repositorio, ruta y un dato concreto (por ejemplo, el hash esperado y el obtenido). Al final, un resumen con cantidades por severidad.
- **`--json`:** la misma información, para tests y para un uso futuro desde otra vista.
- **Códigos de salida:**
  - `0`: sin errores, aunque haya avisos;
  - `1`: al menos un error;
  - `2`: datos inválidos o ilegibles (un `.gitignore` o una `procedencia.md` que no se pueden parsear). Así un dato roto no pasa como «todo bien», igual que en `pending_triggers.py`.

### Límites

- **Solo lectura.** Nunca escribe, nunca usa la red, nunca ejecuta hooks ni código de los proyectos. Usa solo la biblioteca estándar de Python y `git` en modo lectura (`config --get`, `remote get-url`, `cat-file -e`).
- **Uso solo local.** El CI de la raíz no tiene los checkouts de los productos, que están ignorados; ahí solo corren los tests con fixtures. La salida menciona proyectos privados, así que no se commitea ni se publica: el repositorio raíz es público (VCX-D032).
- **Revisa coherencia, no funcionamiento.** Que todo esté en verde no prueba que un proyecto funcione fuera de `vcx/` (paso 10 del checklist) ni que los hooks bloqueen de verdad: eso exige el commit de prueba de SEC-03.
- **Fallas del entorno:** si falta `git` o un checkout no es un repositorio válido, el hallazgo se reporta con el código `ENV` y el resto de los chequeos sigue corriendo.

### Pruebas

`scripts/tests/health.fixtures.sh`, con el mismo estilo que `pending-triggers.fixtures.sh`: arma en un directorio temporal un workspace con repos `git init`, un `AGENTS.md` raíz y copias. Un caso limpio sale con código 0; hay un caso por cada código sembrado; más un `.gitignore` ilegible (código 2) y un checkout ausente (aviso, código 0). Se suma al workflow existente o a uno nuevo de la raíz, sin red.

## Riesgos

- **Falsa sensación de seguridad.** Un verde se puede leer como «el workspace está sano». La salida dice explícitamente qué no cubre.
- **Formatos que cambian.** Si cambia el encabezado de los principios o el formato de `procedencia.md`, el chequeo da error 2 en vez de un falso verde. Conviene que sea así.
- **Mantenimiento.** Cinco chequeos sin dependencias, con un costo esperado bajo. Si nadie lo corre en un mes, se retira (VCX-P9), anotándolo en `pending-triggers.json`.

## Pendientes

1. **Compuerta de secretos en seis repositorios.** Hallazgo de seguridad independiente del health: activar `core.hooksPath` con `.githooks/pre-commit`, o agregar el escaneo en CI, en Melquisedec, Pinot Index, Salmanazar, Blends, Brix y Cellar. Cada repositorio requiere su propia autorización y debe quedar reflejado en el inventario de controles.
2. **Unificar la declaración de origen** de las copias de los principios al formato con SHA de Melquisedec. Mientras tanto, `PRIN-ORIGIN` da aviso, no error, cuando hay solo versión.
3. **Registrar la decisión** si el diseño se aprueba: número VCX-D siguiente en el registro.
