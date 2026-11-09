# Extracción de Brix desde el precursor

Fecha: 2026-11-07. Estado: VCX-D056 en el [registro de decisiones](../../decisions/README.md), ratificada por el usuario como decisión documental el 2026-11-07. El usuario preguntó en el chat con Claude «Conviene planificar la migración de brix hacia vcx desde el antiguo repo?», aprobó planificarla y respondió «Ratificar D056». La ratificación no autoriza ninguna etapa: no crea repositorios, no publica, no mueve código y no escribe en el precursor. Etiquetas: [H] hecho medido; [I] interpretación; [P] propuesta.

## Problema

[H] El CLI de Brix vive en `vc/brix/` del precursor, de solo lectura para este trabajo. `vcx/brix/` tiene documentos, skills y evaluaciones, sin el CLI y sin `.git` propio: lo rastrea la raíz. Resultado: Brix no tiene dónde editarse.

[H] El bloqueo ya tiene costo. `brix spec` (VCX-D055) requiere cambiar el CLI; Teyst consume un tarball empaquetado desde el precursor, y `brix/tooling/score-run.mjs` invoca el CLI por la ruta `../blends/vc/brix/`.

[I] Límite de la urgencia: si `/idea` (VCX-D054) se resuelve primero como skill y el CLI no se toca en semanas, ejecutar puede esperar. Esta spec sirve igual: deja medido el costo y sus compuertas.

## Medición

Base: `denispaiva/blends` remoto, `main` en `4742bb99`, en un clon temporal fuera de los repositorios, el 2026-11-07. El `main` local del precursor sigue en `f86a2a7d`, 58 commits atrás: **toda medición y extracción debe partir del remoto.** `../blends` no cambió: mismo HEAD y mismo estado antes y después.

| Medida | Resultado | Cómo |
|---|---|---|
| Tamaño | [H] 82 archivos, 149 commits, 86 rutas históricas | `git ls-files`, `git log -- vc/brix` |
| Deriva local → remoto | [H] 2 líneas en `vc/brix/`, en 2 archivos del ledger | API `compare` de GitHub |
| Prueba aislada | [H] 158 de 159 pruebas pasan; falla solo `tests/finops/cli-wiring.test.mjs`, que no carga | `git archive` de `vc/brix`, `node --test`, Node 26.13, sin VCX ni precursor como padres, con `GH_TOKEN` y `GITHUB_TOKEN` sin definir |
| Mismas pruebas en el monorepo | [H] 160 de 160 | `node --test` en el clon |
| Imports salientes de Brix | [H] 1: esa misma prueba hacia `vc/tools/validate-versions.mjs` | Grafo de imports relativos |
| Imports entrantes | [H] 34 aristas desde 22 archivos: 14 son tests y 8 no lo son | Grafo de imports relativos, multilínea |
| Secretos | [H] Sin hallazgos en ~614 KB | Betterleaks 2.0.0-rc.1 con `.betterleaks.toml`, `git` y `--log-opts="4742bb99 -- vc/brix"` |
| Referencias en el historial | [H] 173 líneas agregadas nombran proyectos, 108 de ellas en `data/`; 5 con posibles importes; 3 con direcciones de correo | Expresiones regulares sobre `git log -p`; conteo, no revisión |
| Autoría | [H] Los 149 commits llevan un correo real | `git log --format=%ae` |

[I] La prueba aislada confirma que el desacople del 2026-09-13 del precursor, `docs/lifecycle/decoupling-brix.md`, se sostuvo. Brix es mucho más independiente de lo que sugiere la deuda DH-18.

Límites: las pruebas corrieron sin instalar dependencias y sin ejercitar backends reales; el scan cubre solo `vc/brix`, no los archivos de `vc/tools`; el grafo no ve invocaciones por `spawn` ni rutas armadas en tiempo de ejecución.

### Correcciones a lo documentado

| Fuente | Dice | Medido hoy |
|---|---|---|
| DH-18 | 39 imports hacia Brix | 34 aristas; la cifra anterior usaba otra base y otro método, y no se recalculó aquí |
| VCX-D032, paso 4 | Brix después del renombre y de Blends | Ninguno de los dos ocurrió, y Brix no los necesita |
| VCX-D045 | Cortar cuatro imports antes de extraer Brix | Los cuatro están en `vc/tools`: se cortan al mover esos archivos, no para extraer `vc/brix` |
| `packages/cli/package.json` | `files` declara `bin`, `src`, `scripts` y `scoring` | Deja fuera `finops` y `seeding`; Teyst lo sorteó con `git archive`, según su commit `8d0d02a` |
| CI anidada `ci.yml` | Se presenta como CI de Brix | Solo ejecuta el CLI sin argumentos y no corre las pruebas |

## Propuestas ratificadas

### 1. Brix antes de Blends

[P] Enmendar el orden del paso 4 de VCX-D032: extraer Brix antes del renombre del precursor y del `blends` público, como VCX-D043 hizo con Teyst.

[I] La regla de VCX-D045 es que Blends y Solera importan de Brix y Brix no importa de nadie, así que el orden natural va de la dependencia hacia el consumidor. Costo: Brix debe sostenerse solo antes de que exista su consumidor público, y el nombre `brix` hay que liberarlo apartando el espejo.

### 2. Dos olas

[P] Separar lo que VCX-D045 une. Reduce riesgo y deja `brix spec` destrabado con la primera:

- **Ola 1, el CLI:** `vc/brix/` menos lo excluido. Un solo import por cortar.
- **Ola 2, capacidades de `vc/tools`:** los 36 archivos de VCX-D045 y `brix-capabilities`, con sus cuatro imports y consumidores en Solera y Blends. Se planifica aparte, con su propia medición. Puede no ejecutarse si la curación de VCX-D044 reduce la lista.

[H] La lista de la ola 2 es provisoria: mi clasificación por nombre difiere en algunos archivos de los conteos de VCX-D045, que también clasificó por nombre y cabecera.

Costo: durante un tiempo, capacidades de Brix viven en dos lugares con dueños distintos. [I] Es deuda declarada y acotada, porque hoy ya están separadas.

### 3. Superficie de la ola 1

| Ruta | Tratamiento | Motivo |
|---|---|---|
| `packages/`, `tests/`, `LICENSE`, `package.json`, `brix.config.json`, `.gitignore`, `.github/` | Exportar | Código y pruebas del producto |
| `docs/decisions/` | Exportar con revisión | Son capacidades de Brix; traen menciones del portfolio |
| `docs/plans/`, `docs/research/`, `docs/governance/` | Revisar uno por uno | Mezclan método y datos de la instancia |
| `README.md` | Exportar y fusionar con `vcx/brix/README.md` | Dos descripciones del mismo producto |
| `scripts/` | Decidir con la clase de abajo | Miden el portfolio y escriben en `data/` |
| `data/`, `finops/`, `.roadmap.json` | Excluir; quedan en Solera | Datos de instancia (VCX-D032) |

Clase inicial de VCX-D044. Es provisoria: cruza análisis estático y consumidores, pero falta uso medido, y sin evidencia de uso no equivale a muerto.

| Elemento | Consumidor comprobado | Clase provisoria |
|---|---|---|
| `tool score` | Envoltorio de VCX-D035, herramientas de tooling | Conservar |
| `seed` | Teyst | Conservar |
| Motor `finops` | `roadmap/build.mjs`, `validate-billing-ledger`, Teyst | Conservar |
| `idea` | Documentación y validadores; pasa a `brix spec` por VCX-D055 | Conservar |
| `ci` | Solo registro de capacidades, bitácora y tests | Sin decidir |
| `graduate` | Solo registro, protocolo de gate y tests; opera `git subtree` sobre un monorepo | Sin decidir; candidato a retirar después del corte |
| `scripts/` y sus pruebas | Sin medir | Sin decidir |

La poda ocurre después del corte, en el repositorio destino, en commits por grupo.

### 4. Historial

[P] Repositorio nuevo con historial filtrado por rutas, según VCX-D032, y correo de autor reescrito a `noreply`, como se hizo en `vcx`. Si el scan del export falla o la revisión encuentra algo no publicable, historial nuevo con procedencia explícita de `4742bb99`. Esto cierra la alternativa que el [mapa](../../architecture/repository-map.md) dejaba abierta para Brix.

[I] Las menciones a proyectos no bloquean por sí solas, porque `vcx` público ya los nombra. Los posibles importes y las direcciones sí exigen revisión. Filtrar por rutas no limpia versiones anteriores de los archivos que se conservan: la revisión debe cubrir el historial, no solo el árbol final. `git-filter-repo` no está instalado; elegir herramienta es parte de E1.

### 5. Espejo

[P] Apartar `denispaiva/brix` con otro nombre y archivarlo, sin reutilizarlo. [H] Está detenido desde septiembre y 102 commits atrás. [I] Reutilizarlo daría dos historias del mismo subárbol y mantiene privado un nombre que debe nacer público. Esto cierra el punto 2 de la [topología](../../architecture/github-topology.md#decisiones-que-esto-deja-al-usuario) solo para Brix.

### 6. Evaluaciones reales

[H] `brix/AGENTS.md` dice que las evaluaciones reales no van en el producto, pero `brix/tooling/` tiene ocho y su registro. VCX-D045 envía a Solera las de `vc/tooling/evaluations/`, del precursor. [H] Las de `vcx` alimentan `docs/exports/build_tooling_matrix_view.py` y la [matriz de tooling](../../architecture/tooling-matrix.md), públicas.

[P] Moverlas en E4 a la raíz, en `docs/tooling/`, junto con `score-run.mjs`. VCX-D035 ya fija el registro en VCX, y enviarlas a Solera, privada, rompería la matriz pública. El motor queda en Brix y el envoltorio del procedimiento, con sus datos. Queda opcional: la raíz no se vuelve dependencia de ningún producto.

## Etapas

Cada etapa requiere autorización propia, con repositorio, ruta y alcance. La aprobación de una no se extiende a la siguiente.

| Etapa | Qué hace | Efecto | Compuerta de salida | Recuperación |
|---|---|---|---|---|
| **E1** Export local | Filtra el historial en el scratchpad y aplica la superficie | Local y descartable | Scan limpio sobre todo el historial exportado; revisión de referencias registrada; correo reescrito | Borrar el export |
| **E2** Prueba aislada | Corta el import inverso, corrige `files` y hace que la CI corra las pruebas | Local y descartable | Clon limpio sin VCX ni precursor: todas las pruebas pasan; `npm pack` incluye `finops` y `seeding`; sin rutas `vc/` funcionales; se comprueba la carga de instrucciones | Corregir y repetir |
| **E3** Publicación | Fija el corte, aparta el espejo y crea `brix` público | **Externo y difícil de revertir** | Scan repetido antes del push; protección de `main`; CI verde en runners estándar; tag de versión | Antes del push, nada que deshacer. Después, lo publicado debe tratarse como visible, aunque se borre |
| **E4** Incorporación | Clon en ubicación temporal; fusiona documentos y skills, traslada decisiones, adopta principios; después retira `brix/` del índice raíz sin borrar, activa `/brix/` y coloca el clon | Raíz y repositorio nuevo | Hashes de la fuente registrados; la raíz ignora `brix/` sin gitlink; skills visibles en Claude Code y Codex; enlaces resueltos en clon aislado | Restaurar desde el commit base y la versión apartada, sin borrar ninguna |
| **E5** Consumidores | Teyst pasa a un tarball del tag público; `score-run.mjs` deja de apuntar a `../blends` | Teyst y raíz | Suite de Teyst y corrida en seco de `score-run` verdes | Volver al tarball anterior, que sigue en la historia |
| **Ola 2** | Se planifica aparte | Instancia, Blends y Brix | Medición propia | Propia |

Aclaraciones:

- **Decisiones (E4):** VCX-D019 y los registros `0001` a `0008` pasan al repositorio del producto, según la [clasificación](../../architecture/repository-map.md#clasificación-de-decisiones). Hay dos registros con número `0007`: conservarlos y resolverlo sin renumerar en silencio.
- **Distribución (E5):** no hace falta publicar en npm. Un tarball de un tag público alcanza para un solo consumidor externo (VCX-P3).
- **Precursor:** sigue usando su copia. Reemplazar sus imports es parte del corte de Solera, no de esta extracción.

## Congelamiento y peor escenario

[I] Peor escenario plausible: dos fuentes editables, porque el tren del precursor todavía puede tocar `vc/brix/` después del corte.

[P] Desde E3, la fuente canónica de Brix es el repositorio público y `vc/brix/` queda congelada en el SHA de corte. Cualquier corrección entra por `brix` y, si el precursor la necesita, se concilia a mano bajo su gobierno.

Una regla documental no es un control. Se agrega una comprobación observable antes de cada versión de Brix:

```bash
git diff <sha-de-corte>..origin/main --stat -- vc/brix
```

Una salida no vacía detiene la versión hasta conciliar, sin imponer ninguna de las dos copias. Límite declarado: detecta la divergencia, no la impide.

[H] Por título, los 6 pedidos de `queue` clasificados para Brix recaen en `vc/tools` o son decisiones, no en `packages/cli`; el detalle sigue en el triage privado. Pesan en la ola 2 y no fueron validados por el PO.

## Riesgos y contraejemplos

- **La prueba aislada es optimista.** No cubre instalación desde el paquete ni backends reales. E2 agrega `npm pack` y E5 prueba un consumidor real.
- **Referencias privadas en versiones antiguas.** Un árbol final limpio no prueba un historial limpio. E1 revisa el historial; si no se puede sostener, aplica la salida de historial nuevo.
- **Publicación irreversible.** Borrar un repositorio público no retira lo ya visto. Por eso E1 y E2 son locales y E3 repite el scan.
- **`score-run` depende del precursor.** Su control de exit `3` compara el precursor durante la corrida. Debe rediseñarse en E5 para fijar la versión del motor, no solo cambiar la ruta.
- **Mantenimiento doble.** Si la ola 2 se posterga mucho, la deuda se vuelve estable. Hay que revisarla al ratificar la secuencia de Solera.
- **Alternativa más simple descartada por ahora.** Dejar el CLI donde está y crecer solo con skills cuesta cero hoy, pero deja `brix spec`, Teyst y `score-run` atados a un repositorio de solo lectura. Es válida solo si no se toca el CLI.

## Costo

[I] Sin gasto adicional previsto: runners estándar en repositorio público, Betterleaks ya instalado y tarball sin registro de paquetes. El costo real es atención humana en las revisiones de E1 y E3, y tokens de la ejecución. No se estimó en horas.

## Qué no decide

- No autoriza ninguna etapa, ni crear, renombrar o archivar repositorios.
- No retira capacidades ni aplica la poda.
- No planifica la ola 2, el corte de Solera ni el `blends` público.
- No cambia `.gitignore`, la cola ni el precursor.

## Verificación de esta entrega

El clon temporal quedó fuera de los repositorios y `../blends` no cambió. Las cifras citan método, SHA y fecha. La tabla de correcciones señala dónde difiere de lo ya registrado, sin editar esas fuentes salvo los punteros acordados.

Nota orientativa según VCX-P2: 7 de 10 como plan. Descuentos: uno porque la clase de VCX-D044 no tiene uso medido; uno porque la prueba aislada no cubre instalación ni backends; uno porque la ola 2 queda sin diseñar. No es una aprobación.
