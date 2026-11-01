# Plan de aplicación documental del modelo de productos (VCX-D029)

> **Para agentes ejecutores:** aplicar `superpowers:executing-plans` de forma directa y secuencial cuando este alcance esté autorizado. Las casillas registran ejecución, no aprobación.

**Objetivo:** llevar a las fuentes editables de VCX el modelo acordado en VCX-D029, método en Blends, conducción y custodia en Cellar, capacidades en Brix y VibeOS como marca, sin crear segundas fuentes, sin escribir en el precursor y dejando evidencia de verificación.

**Base:** [spec del modelo de productos](../specs/2026-10-31-product-model-design.md), fila VCX-D029 del [registro de decisiones](../../decisions/README.md) y principios VCX-P1 a VCX-P9 de [AGENTS](../../../AGENTS.md#principios-transversales-de-vcx).

**Tecnologías:** Markdown y rutas relativas. Sin código, comandos, instancias, dependencias ni pruebas que reproduzcan el texto.

**Fecha:** 2026-11-01. **Estado:** plan propuesto a pedido del usuario («Sí, planificá», 2026-11-01, chat con Claude). Ajustado el mismo día con la revisión externa incorporada en la spec. Autorizado con «Sí, ejecutá» el 2026-11-01 y ejecutado ese día en dos pasos: 16 archivos primero y, tras el commit `c4d2dc1` de los cambios ajenos pendientes, los 4 restantes; evidencia en el [reporte](../reports/2026-11-01-product-model-application.md). Alcance separado del commit base documental, que ya existe como `f47c71f` en `main`.

## Qué resuelve y qué deja fuera

Resuelve las filas de la tabla «Aplicación documental» de la spec y dos archivos que esa tabla no listó y el inventario del 2026-11-01 encontró: el [speech ejecutivo](../../executive-pitch.md), que repite «Blends conduce el trabajo», y el [criterio de nombres](../../naming.md), que no menciona VibeOS. Incorpora el ajuste «MVP recomendado, no obligatorio» en los dos pasajes donde hoy es exigencia, porque la spec de maduración lo deja como aplicación pendiente y el modelo de productos lo reafirma; ejecutarlo aquí cierra esa fila para ambas specs y evita aplicarlo dos veces.

Escribe la frontera entre método y conducción, que la spec deja pendiente, porque sin ella la aplicación dejaría dos procesos de conducción. El texto se propone más abajo y se aprueba junto con este plan; se escribe una sola vez, en la matriz de responsabilidades, y el resto de las fuentes la enlaza.

Deja fuera, con registro explícito:

- La conciliación con el precursor, VCX-D011. Las fuentes de VCX se escriben como objetivo; Blends Kernel sigue conduciendo proyectos allí hasta conciliar.
- El contenido del contrato de conducción. Solo se agrega su fila y dueño en interoperabilidad; entradas, resultados y permisos quedan para su diseño.
- La delegación del responsable del portfolio, parámetro del perfil de gobierno pendiente de definir.
- El diseño del traspaso al graduar: quién prepara el contexto, cuándo lo recibe Cellar, cómo acepta el PO su responsabilidad, qué decisiones conserva el responsable del portfolio y qué ocurre si la preparación falla. Las fuentes solo nombran el destino y marcan ese diseño como pendiente.
- El cambio de criterio del gate de la spec de maduración, que sigue siendo propuesta sin aprobar; VCX-D029 no lo aprueba indirectamente.
- Los documentos fechados: specs anteriores, reportes, correspondencia del sistema actual y el OPML. Son evidencia de su fecha y no se reescriben.
- El commit de aplicación. Se propone al final; ejecutarlo requiere que la autorización lo incluya expresamente.

## Frontera propuesta entre método y conducción [P]

Regla de reparto, a escribir en la matriz de responsabilidades:

- **Método, dueño Blends.** Toda regla que aplique a cualquier proyecto de cualquier Cellar: etapas, compuertas, criterios de evidencia, qué registra una decisión, roles y plantillas de proceso. Blends la publica versionada y la verifica; no ejecuta el proyecto.
- **Conducción, dueño Cellar.** Toda acción o decisión sobre un proyecto concreto después de graduar: planificar, priorizar, entregar, evolucionar y registrar, con el PO del proyecto como autoridad humana. Cellar conduce aplicando el método adoptado; no redefine las reglas.
- **Tramo de idea, coordina Blends.** Desde la propuesta hasta la graduación, Blends coordina actividades e hitos y la instancia de Cellar custodia. El responsable del portfolio decide.
- **Capacidad, dueño Brix.** Todo cálculo, instrumento o integración reutilizable, invocado desde cualquiera de los dos tramos con permisos explícitos.

Prueba de pertenencia: si la frase vale para todos los proyectos, es método; si nombra a un proyecto, es conducción; si describe cómo se calcula o integra algo, es capacidad.

| Ejemplo, con el mapa de talleres de cerámica | Pertenece a |
|---|---|
| «Cada decisión registra autoridad, revisión, alcance y qué no autoriza» | Método, Blends |
| «El directorio prioriza horarios antes que fotos en la primera entrega» | Conducción, Cellar, decide el PO |
| «Estimar el costo mensual del hosting del directorio» | Capacidad, Brix, invocada por Cellar bajo la plantilla FinOps |
| «Confirmar qué preguntas asesinas bloquean el gate» | Tramo de idea, coordina Blends, decide el responsable del portfolio |
| «Un Cellar debe poder leerse sin ejecutar Blends ni Brix» | Custodia, responsabilidad de Cellar, invariante conservado |
| «La propuesta del directorio está en preparación y todavía no eligió instancia» | Custodia previa al ingreso, fuera del portfolio activo hasta la confirmación de VCX-D017 |

## Precondiciones

- Árbol de trabajo sin cambios ajenos a este alcance en los archivos de la lista. Al 2026-11-01 hay cambios sin commitear de otros alcances: una línea de `README.md`, tres filas de `docs/decisions/README.md`, `docs/architecture/tooling-matrix.md`, la spec de maduración y la spec del modelo. Tres de esos archivos también se editan aquí. Deben quedar commiteados por sus alcances antes de ejecutar; este plan no decide cómo se agrupan esos commits.
- Commit base presente y verificado: `git log` muestra `f47c71f` como raíz de `main`.
- El precursor `../blends/` no se lee ni se escribe. Ninguna tarea lo necesita.
- Solo se tocan los archivos de la lista. Un archivo nuevo o una contradicción no prevista detiene la ejecución y se registra, no se resuelve por inferencia.

## Archivos y cambio previsto

| Archivo | Cambio | Regla de la spec |
|---|---|---|
| `docs/architecture/responsibility-matrix.md` | Frontera método/conducción; filas de proceso, roadmap, decisiones, FinOps, presentación y código partidas por tramo idea/proyecto; RACI con responsable del portfolio como A en ideas y PO del proyecto como A en proyectos; invariantes 2 y 3 reescritos | Contraste «PO» y «Cellar pasivo» |
| `docs/architecture/interoperability.md` | Fila nueva «Operaciones de conducción de proyecto», dueño Cellar · producto, estado propuesto; «decisión del PO» pasa a «decisión de la autoridad humana competente» | Contrato de conducción |
| `cellar/README.md` | Misión, visión y alcance con custodia y conducción como responsabilidades distinguidas, sin módulos ni servicios; «no ejecuta el gobierno de Blends» pasa a «conduce bajo el método de Blends, sin redefinirlo» | Cellar producto |
| `cellars/README.md` | La instancia custodia íntegra en todas las etapas y conduce sus proyectos; registra la ubicación del código sin alojarlo; la preparación previa al ingreso queda fuera del portfolio activo y puede no tener instancia elegida | Cellar instancia |
| `cellar/docs/initiative-model.md` | `ownerRef` no se sobrescribe; la graduación agrega la referencia al PO del proyecto con su decisión y conserva ambas asignaciones; `definitionRef` sin MVP obligatorio; lectura y actualización por tramo | Transferencia de autoridad; MVP |
| `blends/README.md` | Misión como dueño del método y coordinador del tramo de idea; alcance sin entrega ni presentación de proyectos; párrafo final de reparto reescrito | Blends |
| `blends/docs/idea-to-project.md` | «Blends conduce» pasa a «coordina el tramo de idea»; «PO competente» y «presupuesto al PO» pasan a responsable del portfolio; paso 3 sin hipótesis de MVP obligatoria; paso 5 nombra a Cellar como destino con PO asignado en la misma decisión y marca el traspaso como diseño pendiente; «Siguiente límite» apunta a la conducción en Cellar | Recorrido de referencia |
| `blends/docs/idea-intake.md` | Paso 6: «humano competente» pasa a responsable del portfolio; el resto sin cambio | Autoridad humana |
| `blends/docs/architecture-and-finops.md` | Fila de autoridad: responsable del portfolio en esta etapa | Autoridad humana |
| `brix/README.md` | Alcance conceptual suma Git y diseño como capacidades declaradas, no implementadas; una frase que lo identifica como núcleo de capacidades técnicas y reserva «kernel» | Brix; Kernel |
| `README.md` | Título «VCX · VibeOS, Vibe Coding for X projects»; línea de reparto reescrita; entrada a la spec del modelo en «Por dónde empezar» | VibeOS; Cellar pasivo |
| `AGENTS.md` | Solo la frase de marca en «Entrada y alcance», si hace falta nombrar VibeOS; principios sin cambio | VibeOS |
| `docs/vision.md` | Nota de marca; señal nueva: un Cellar conduce un proyecto sin ejecutar Blends, con el método adoptado disponible como recurso versionado | Visión |
| `docs/architecture/overview.md` | «Fronteras y contexto» con el reparto nuevo; prueba de independencia nueva en la lista | Arquitectura |
| `docs/executive-pitch.md` | Párrafos de Blends y Cellar coherentes con el reparto; VibeOS junto a VCX | Inventario 2026-11-01 |
| `docs/naming.md` | VibeOS como nombre de marca del conjunto, registrado en VCX-D029; no es identidad de producto | Pendiente «candidato de nombre» |
| `docs/architecture/tooling-matrix.md` | «Fases consideradas»: Cellar suma conducción; las filas «Entrega · …» y «Plan del proyecto graduado» pasan a «Cellar · conducción, …»; «Blends · preparación» conserva el contexto de proyecto | Matriz de tooling |
| `docs/superpowers/specs/2026-10-31-idea-maturation-design.md` | Una línea en «Acuerdos y alcance»: la autoridad humana del gate es el responsable del portfolio según VCX-D029; sin otros cambios | Spec de maduración |
| `docs/decisions/README.md` | Estado de VCX-D029: «aplicado el AAAA-MM-DD», autoridad y enlace al reporte; la decisión original no se reescribe | Registro |
| `docs/superpowers/reports/2026-11-01-product-model-application.md` | Nuevo: evidencia fechada de ejecución, verificaciones, hallazgos y pendientes | Verificación |

## Restricciones

- Una fuente por regla: la frontera vive en la matriz; las demás fuentes la enlazan, no la copian.
- Distinguir acordado de propuesto: el modelo es acordado [U]; la frontera, la fila de contrato y los cambios de texto son propuestas hasta su autorización. Los pasajes nuevos conservan su etiqueta de estado.
- No ampliar: no se diseñan el contrato de conducción, la delegación, el almacenamiento ni comandos. No se cambia el criterio del gate.
- No reescribir historia: specs y reportes fechados conservan su texto, incluido «PO ficticio» en el primer recorrido.
- Español para prosa; identificadores, estados y nombres de archivo en inglés. Rutas relativas.
- El precursor y sus reglas quedan intactos. Nada de lo escrito aquí concilia VCX-D011.
- Un cambio de alcance detectado al ejecutar se registra en el reporte y se eleva; no se decide por inferencia.

## Focos de verificación

1. Dos procesos de conducción: ninguna fuente deja a Blends conduciendo, planificando o entregando proyectos después de graduar, ni a Cellar definiendo reglas de método.
2. PO en el tramo equivocado: ninguna fuente asigna PO a ideas ni responsable del portfolio a proyectos, salvo documentos fechados identificados.
3. Custodia debilitada: ningún pasaje nuevo hace depender la lectura o recuperación de un Cellar de ejecutar Blends o Brix.
4. Reescritura de historia: `git diff` no toca specs anteriores, reportes, correspondencia ni OPML.
5. Precursor: ningún comando apunta a `../blends/`; ninguna regla vigente se declara reemplazada.
6. Mezcla de alcances: el diff de aplicación contiene solo los archivos de la lista.
7. Autoridad sustituida: ninguna fuente borra o reemplaza la asignación del responsable del portfolio al asignar el PO; ninguna convierte en admitida una propuesta en preparación.

## Tarea 1 — Comprobar precondiciones

- [x] Leer VCX-D029, la spec del modelo y este plan; confirmar que la autorización cita este alcance.
- [x] Comprobar `git status --short`: sin cambios ajenos en los archivos de la lista; registrar qué quedó pendiente de otros alcances si lo hay y detenerse si coincide con un archivo a editar.
- [x] Comprobar `git log --oneline -1` sobre `f47c71f` y la rama `main`.

## Tarea 2 — Matriz de responsabilidades, fuente del reparto

**Archivo:** `docs/architecture/responsibility-matrix.md`.

- [x] Agregar la sección «Método y conducción» con la regla y la tabla de ejemplos de este plan, etiquetada como propuesta derivada de VCX-D029.
- [x] Partir por tramo las filas de proceso, roadmap y backlog, decisiones y sesiones, FinOps, presentación y código: en idea, Blends coordina y la instancia custodia; en proyecto, Cellar conduce y custodia y Blends mantiene el método.
- [x] RACI: «PO de la iniciativa» pasa a «responsable del portfolio» en filas de idea y a «PO del proyecto» en filas de proyecto; agregar la fila «Graduar y asignar PO» con responsable del portfolio como A.
- [x] Invariante 2: «Blends define el método y coordina el tramo de idea; Brix ejecuta capacidades; Cellar custodia en todas las etapas y conduce los proyectos. Ninguna pieza absorbe silenciosamente las otras». Invariante 3: conservar la lectura sin ejecutar Blends o Brix y precisar que aplica a la parte pasiva de Cellar.
- [x] Nota de estado: reparto derivado de VCX-D029; no rige en el precursor hasta VCX-D011.

## Tarea 3 — Interoperabilidad

**Archivo:** `docs/architecture/interoperability.md`.

- [x] Agregar la fila «Operaciones de conducción de proyecto», dueño Cellar · producto, consumidores PO, equipos e integraciones, frontera «aplica el método de Blends sin redefinirlo»; estado propuesto, contenido pendiente.
- [x] Reemplazar «decisión del PO» por «decisión de la autoridad humana competente, responsable del portfolio o PO según el tramo».

## Tarea 4 — Cellar: producto, instancias y modelo

**Archivos:** `cellar/README.md`, `cellars/README.md`, `cellar/docs/initiative-model.md`.

- [x] Misión de Cellar con custodia y conducción; visión con «conducir sus proyectos bajo el método adoptado»; alcance con las dos responsabilidades distinguidas, sin prescribir módulos, y la frase de gobierno reescrita.
- [x] `cellars/README.md`: custodia íntegra en todas las etapas, conducción de proyectos, registro de la ubicación del código y preparación previa al ingreso fuera del portfolio activo, con instancia de destino opcional.
- [x] `ownerRef`: responsable del portfolio mientras es idea; al graduar no se sobrescribe y se agrega la referencia al PO del proyecto con su decisión, conservando ambas asignaciones; si falta el PO, la preparación queda pendiente. Enlazar el tratamiento de interrupciones del recorrido y marcar como pendiente qué decisiones pasan a cada autoridad.
- [x] `definitionRef`: «propuesta de valor, vía de validación propuesta y alternativas»; MVP recomendado, no obligatorio, con enlace a la spec de maduración.
- [x] «Lectura, actualización y custodia»: Blends aplica el proceso en el tramo de idea; Cellar conduce en el tramo de proyecto; ambos por la interfaz, sin canal alternativo.

## Tarea 5 — Blends: README, recorrido, ingreso y FinOps

**Archivos:** `blends/README.md`, `blends/docs/idea-to-project.md`, `blends/docs/idea-intake.md`, `blends/docs/architecture-and-finops.md`.

- [x] Misión: dueño del método, coordina el tramo de idea; alcance sin entrega ni presentación de proyectos; párrafo de reparto reescrito con enlace a la matriz.
- [x] Recorrido: encabezado «coordina el tramo de idea»; autoridad antes de graduar es el responsable del portfolio; paso 3 con vía de validación propuesta; paso 5 nombra a Cellar como destino con PO asignado y deja el traspaso como diseño pendiente; «Siguiente límite» nombra la conducción en Cellar.
- [x] Ingreso: paso 6 con responsable del portfolio como quien confirma; conservar VCX-D017.
- [x] FinOps: fila de autoridad con responsable del portfolio en esta etapa.

## Tarea 6 — Brix

**Archivo:** `brix/README.md`.

- [x] Alcance conceptual suma diseño y Git como capacidades declaradas; mantener «la disponibilidad real debe verificarse».
- [x] Frase: Brix es el núcleo de capacidades técnicas de VCX; «kernel» queda reservado al núcleo de gobierno del precursor, con enlace a la arquitectura.

## Tarea 7 — Raíz, narrativa y nombres

**Archivos:** `README.md`, `AGENTS.md`, `docs/vision.md`, `docs/architecture/overview.md`, `docs/executive-pitch.md`, `docs/naming.md`, `docs/architecture/tooling-matrix.md`, `docs/superpowers/specs/2026-10-31-idea-maturation-design.md`, `docs/decisions/README.md`.

- [x] README: título con VibeOS; línea de reparto: «Blends define el método y coordina las ideas; Brix aporta capacidades; Cellar custodia y conduce los proyectos»; entrada a la spec del modelo.
- [x] AGENTS: solo si hace falta, la frase de marca; comprobar que los principios no cambian con `git diff`.
- [x] Visión y arquitectura: reparto nuevo en «Fronteras y contexto»; señal y prueba de independencia nuevas con su condición.
- [x] Speech ejecutivo: párrafos de Blends y Cellar coherentes; VibeOS junto a VCX.
- [x] Nombres: VibeOS como marca registrada en VCX-D029, sin asignar identidad de producto.
- [x] Matriz de tooling: fases y filas de entrega bajo «Cellar · conducción»; sin cambiar estados de asignación.
- [x] Spec de maduración: una línea de lectura según VCX-D029; sin tocar la propuesta de gate.
- [x] Registro: estado de VCX-D029 con fecha, autoridad y enlace al reporte.

## Tarea 8 — Verificar y reportar

**Archivo nuevo:** `docs/superpowers/reports/2026-11-01-product-model-application.md`.

- [x] Recorrer el mapa de talleres de cerámica por cada fuente editada y anotar en el reporte dónde se lee cada paso; una contradicción detiene el cierre.
- [x] Ejecutar las comprobaciones de texto y enlaces de la sección siguiente; pegar resultados en el reporte.
- [x] Comparar `git status --short` con la lista de archivos; registrar cualquier diferencia.
- [x] Escribir hallazgos, límites y pendientes: VCX-D011, contrato de conducción, delegación, gate.

## Comprobaciones

Texto, desde la raíz. Cada coincidencia se revisa a mano; se admiten solo en documentos fechados identificados en el reporte.

```sh
grep -rn --include='*.md' -E "Cellar organiza y custodia|Blends conduce el trabajo|hipótesis de MVP|decisión del PO" .
```

```sh
grep -rn --include='*.md' -E "\bPO\b" blends cellar cellars docs/architecture README.md
```

Enlaces y anclajes de los archivos de la lista:

```sh
python3 - <<'EOF'
import re, os
files = [l.strip() for l in open('docs/superpowers/plans/2026-11-01-product-model-application.md', encoding='utf-8') if l.startswith('| `') ]
files = [re.match(r'\| `([^`]+)`', l).group(1) for l in files]
def anchors(p):
    out = set()
    for line in open(p, encoding='utf-8'):
        m = re.match(r'#+\s+(.*)', line)
        if m:
            t = re.sub(r'[^\w\s-]', '', m.group(1).strip().lower())
            out.add(re.sub(r'\s+', '-', t))
    return out
bad = 0
for f in files:
    if not os.path.exists(f):
        print('NEW OR MISSING', f); continue
    for m in re.finditer(r'\]\(([^)\s]+)\)', open(f, encoding='utf-8').read()):
        u = m.group(1)
        if u.startswith(('http', 'mailto')): continue
        path, _, anc = u.partition('#')
        tgt = os.path.normpath(os.path.join(os.path.dirname(f), path)) if path else f
        if not os.path.exists(tgt): print('MISSING', f, u); bad += 1; continue
        if anc and tgt.endswith('.md') and anc not in anchors(tgt): print('ANCHOR', f, u); bad += 1
print('links OK' if not bad else f'{bad} problems')
EOF
```

Alcance del diff:

```sh
git status --short
```

## Recuperación ante fallos

Si una tarea se interrumpe, conservar los archivos editados y registrar en el reporte qué casillas se completaron. No usar `git checkout`, `restore` ni `reset` para volver atrás: revisar el diff y decidir con el usuario. Una contradicción nueva se anota con fuente y resolución requerida; no se oculta con otra definición.

## Cierre y autorización solicitada

Resultado aceptable: los veinte archivos de la lista expresan el recorrido de referencia sin contradicción, la frontera está escrita una sola vez, las comprobaciones pasan, el diff contiene solo esos archivos y el reporte deja evidencia y pendientes. No demuestra independencia ejecutable ni concilia el precursor.

Se solicita autorizar la edición de los archivos listados y la creación del reporte en `/Users/denis/VibeCoding/vcx`, con las precondiciones cumplidas. El commit de aplicación se propone como uno solo, posterior y separado, con mensaje `docs: aplica el modelo de productos de VCX-D029`; ejecutarlo requiere que la autorización lo nombre.
