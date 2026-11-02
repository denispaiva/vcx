# Inventario de controles de seguridad y privacidad

Fecha: 2026-11-01. Estado: propuesta. Fuente editable del estado de los controles de seguridad y privacidad que afectan a VCX, a sus productos y al precursor del que provienen. Autorizado como redacción documental el 2026-11-01 en el chat con Claude («Sí, redactar»), tras una evaluación cruzada con otra sesión que convergió en empezar por este inventario antes que por un programa de conformidad. Revisado el mismo día tras una crítica cruzada con otra sesión: se separó ausencia de evidencia de fallo, se corrigió la cobertura atribuida a CI, se agregaron puertas por transición, mediciones con su conclusión admisible, recuperación por corrección y roles de mantenimiento y autoridad por separado. Este documento no activa controles, no asigna autoridad, no modifica el precursor ni autoriza publicación, migración o gasto.

Etiquetas: [H] hecho medido el 2026-11-01 desde esta carpeta, en solo lectura; [D] hecho documentado en una fuente fechada que se enlaza; [P] propuesta.

## Para qué sirve

Separar lo que existe de lo que está decidido, propuesto o solo escrito, antes de hablar de ISO/IEC 27001, ISO/IEC 27701 o SOC 2. Cada fila enlaza su fuente y conserva allí la definición; aquí solo se registra el estado. Los [principios](../../AGENTS.md#principios-transversales-de-vcx) y los [invariantes](responsibility-matrix.md#5-invariantes-de-diseño) no se copian.

Estados usados, en el sentido de las [convenciones](../../AGENTS.md#convenciones) de distinguir implementado, diseñado, acordado y propuesto:

| Estado | Significado |
|---|---|
| Verificado | Existe y se comprobó funcionando en la fecha indicada |
| Implementado | Existe en código o configuración; su funcionamiento no se observó en esta medición |
| Inactivo | Existe, pero una condición medida impide que actúe |
| Decidido, no vigente | Hay decisión registrada; no rige todavía, por su propia declaración |
| Diseñado | Está en un documento de arquitectura o modelo; sin implementación |
| Propuesto | Figura en una propuesta sin ratificar |
| Ausente | No existe y se identifica como necesario |
| No comprobado | Puede existir; no se obtuvo evidencia en esta revisión. No equivale a inactivo ni a fallo |

Cada medición termina en una de tres conclusiones: comprobado en esta revisión, falló, o no comprobado. La ausencia de evidencia bloquea una transición que la exija; no convierte una incertidumbre en un hecho. Una evidencia antigua tampoco demuestra que el control dejó de funcionar: solo obliga a medir de nuevo.
La columna de correspondencia normativa indica a qué requisito se parece cada control. No demuestra satisfacción: eso solo lo prueba la columna de evidencia. Los números de ISO/IEC 27001:2022 Anexo A y las series de los Trust Services Criteria de SOC 2 son una asignación orientativa hecha de memoria por el asistente, pendiente de cotejo con el texto de las normas. ISO/IEC 27701 se indica solo donde hay datos personales.

## Inventario

### Raíz VCX

| ID | Control | Estado | Evidencia | Correspondencia | Pendiente |
|---|---|---|---|---|---|
| SEC-01 | Respaldo independiente del repositorio raíz | Ausente al medir; desde el 2026-11-02, Implementado sin recuperación comprobada | [H] `git remote -v` vacío; Time Machine sin destinos configurados; la carpeta no está bajo iCloud Drive; Spotlight no encuentra otra copia de este documento en la carpeta de usuario. La [organización en GitHub](github-topology.md#hoy) registra que nada de VCX está en GitHub. Conclusión: falló; un respaldo manual en disco externo u otro servicio no se puede descartar por estos medios. Actualización del 2026-11-02: `origin` es `denispaiva/vcx`, público por VCX-D032 y no privado como decía la acción, con `main` en `4b01168`; `git ls-remote` coincide con el local. La recuperación desde el remoto no se comprobó | 27001 A.8.13; SOC 2 A1.2 | Crear el remoto privado `vcx`, decisión abierta en la topología, y comprobar la recuperación desde él según SEC-02; un remoto por sí solo no es un respaldo recuperable |
| SEC-02 | Recuperación del commit base documental | Verificado una vez | [D] [reporte del 2026-11-01](../superpowers/reports/2026-11-01-root-baseline-verification.md): extracción y comparación de hashes de `f47c71f` | 27001 A.8.13, A.5.33; SOC 2 A1.3 | Repetir sobre la copia remota cuando exista; la prueba debe cubrir la recuperación completa del repositorio desde el remoto, no solo el commit base |
| SEC-03 | Compuerta de secretos previa al commit en la raíz | Verificado en este clon el 2026-11-02 | [H] 2026-11-02 12:14 UTC: `core.hooksPath` = `.githooks`, relativo; `.githooks/pre-commit` ejecuta Betterleaks 2.0.0-rc.1, instalado con firma Sigstore y SHA-256 verificados; en un clon desechable con el mismo hook, un token sintético preparado bloqueó el commit con salida redactada y un commit limpio pasó. Medición anterior del 2026-11-01: `core.hooksPath` sin definir y sin hooks. Sigue sin `.gitignore` | 27001 A.8.12; SOC 2 CC6.7 | Vale por clon: cada clon nuevo repite la instalación y el `core.hooksPath`; omisible con `--no-verify`. Diseño y evidencia en la [estrategia de detección de secretos](../superpowers/specs/2026-11-02-secret-detection-strategy-design.md) |
| SEC-04 | Datos personales y rutas locales en documentos versionados | Hallazgo abierto | [D] el [diseño de visibilidad](../superpowers/specs/2026-11-01-public-visibility-design.md) midió una dirección de correo en el registro de decisiones y 31 rutas absolutas en documentos históricos | 27001 A.5.34, A.8.12; 27701; SOC 2 P4 | Tratamiento previsto en VCX-D032 antes de publicar; la dirección es del usuario, quien decide si se conserva |
| SEC-05 | Contenido no confiable tratado como datos y autoridad explícita en agentes | Regla adoptada, sin control ejecutable | [D] VCX-P5 y VCX-P7 en [AGENTS.md](../../AGENTS.md#principios-transversales-de-vcx); el mismo texto declara que no existen controles ejecutables que los apliquen | 27001 A.5.1, A.5.36; SOC 2 CC1.1 | Ninguno en esta etapa; la revisión de reglas sigue VCX-P9 |
| SEC-22 | Secret scanning y push protection nativos en `denispaiva/vcx` | Implementado por función | [H] 2026-11-02 11:55 UTC, `GET /repos/denispaiva/vcx` `security_and_analysis`: `secret_scanning` enabled, `secret_scanning_push_protection` enabled, `secret_scanning_non_provider_patterns` disabled, `secret_scanning_validity_checks` disabled, `dependabot_security_updates` disabled; `GET .../vulnerability-alerts` 404, alertas apagadas. Conclusión: reportado como activo para dos funciones; ningún bloqueo ni alerta observados | 27001 A.8.8, A.8.12; SOC 2 CC7.1 | Pasar a Verificado por función con un push de prueba bloqueado y una alerta observada; decidir si se activan patrones no de proveedor y alertas de Dependabot. Cobertura parcial: no se lee como completa |
| SEC-23 | Compuerta de secretos en CI de `denispaiva/vcx` | Verificado para `9273fd0`, caso favorable | [H] run 41444746822 del 2026-11-02 12:26 UTC, workflow `secrets.yml`: Betterleaks 2.0.0-rc.1 con firma Sigstore y SHA-256 verificados antes de extraer, historial del checkout escaneado, «no leaks found», job verde. Diseño en la [estrategia de detección de secretos](../superpowers/specs/2026-11-02-secret-detection-strategy-design.md) | 27001 A.8.12, A.8.28; SOC 2 CC6.7, CC8.1 | Probar el caso de hallazgo en CI con un PR de prueba; cada SHA tiene su propio run; sin SEC-24, un run rojo no impide integrar |
| SEC-24 | Check obligatorio de secretos en `main` de `denispaiva/vcx` | Ausente | [H] 2026-11-02 11:55 UTC: `GET .../branches/main/protection` 404 y `GET .../rulesets` vacío | 27001 A.8.32; SOC 2 CC8.1 | Crear el ruleset cuando exista autoridad; plantilla en la estrategia §4.4; depende de SEC-23 |

### Precursor `../blends` y repositorio `denispaiva/blends`

Solo lectura según VCX-D024. Nada de esta sección se corrige desde VCX: cada corrección requiere alcance propio en el checkout que corresponda, según VCX-D031.

| ID | Control | Estado | Evidencia | Correspondencia | Pendiente |
|---|---|---|---|---|---|
| SEC-06 | Protección de `main` | Verificado | [H] API de GitHub: `enforce_admins` activo; checks obligatorios `base / verify`, `governance`, `lint` y `teyst`; sin revisores obligatorios ni historial lineal | 27001 A.8.32, A.8.4; SOC 2 CC8.1 | El check `teyst` acopla la protección al proyecto, riesgo ya registrado en la [topología](github-topology.md); sin revisores obligatorios, el único control humano es el autor del PR |
| SEC-07 | Compuerta de secretos en CI | Implementado, no comprobado | [H] `ci-node.yml`, job `verify`: Betterleaks 2.0.0-rc.1 descargado con firma cosign y suma SHA-256 comprobadas; es parte del check obligatorio `base / verify` de SEC-06 | 27001 A.8.12, A.8.28; SOC 2 CC6.7, CC8.1 | Actúa al integrar en `main`, cuando el contenido ya llegó al remoto: bloquea la integración, no la primera exposición en una rama. Para pasar a verificado: identificar un run, la revisión analizada, el alcance del escaneo, diff o historial completo, y su resultado |
| SEC-08 | Compuerta de secretos local previa a commit y push | Inactivo | [H] `.githooks/pre-commit` y `pre-push` existen, pero `core.hooksPath` apunta a `/Users/denispaiva/blends/.githooks`, ruta que no existe; Git no ejecuta ningún hook en ese checkout. Registrado en la [propuesta VCX-D030](../decisions/README.md) | 27001 A.8.12; SOC 2 CC6.7 | Corregir con alcance propio del PO de Blends en ese checkout. Cobertura compensatoria parcial: SEC-07 detiene la integración, pero el contenido ya está en el remoto privado cuando corre; SEC-09 no está disponible. Recuperación: restaurar el valor anterior de `core.hooksPath` si el nuevo impide commitear |
| SEC-09 | Secret scanning, push protection y actualizaciones de Dependabot en GitHub | No comprobado | [H] la API no devuelve estado de esas funciones para el repositorio privado. Eso indica que no se reportan, no que estén desactivadas. Conclusión: no comprobado | 27001 A.8.8, A.8.12; SOC 2 CC7.1 | VCX-D032 cuenta con que los repositorios públicos nuevos las tengan disponibles; verificar y activar al crear cada uno |
| SEC-10 | Gestión de secretos: identidad efímera y excepción `GH_SCARCITY_PAT` con rotación por vencimiento | Adoptado en el precursor | [D] `vc/docs/standards/secrets.md`, consultado en solo lectura; tabla de mecanismos por caso y excepción documentada con baja prevista | 27001 A.5.17, A.8.24; SOC 2 CC6.1 | No rige en VCX hasta conciliar por VCX-D011; el estándar no se copia |
| SEC-11 | Seguridad de aplicación del portfolio | Decidido, no vigente | [D] `vc/docs/standards/security.md` lo declara en su encabezado, con migración diferida a un PR del precursor; ya identificado en [fuentes](../sources.md#antecedentes-de-los-principios-transversales) | 27001 A.8.25 a A.8.29; SOC 2 CC8.1 | Es asunto del PO de Blends en el precursor; VCX solo lo registra |
| SEC-12 | Alcance del token de la CLI de GitHub | Hecho, sin evaluar | [H] scopes `gist`, `read:org`, `repo` y `workflow`; `repo` alcanza todos los repositorios privados de la cuenta, incluidos los proyectos; no incluye lectura de plan ni consumo, como anotó VCX-D032. El token se guarda en el keyring del sistema, cobertura compensatoria frente a lectura del disco | 27001 A.5.15, A.8.2; SOC 2 CC6.1, CC6.3 | [P] Evaluar un token de alcance fino por tarea; decisión del usuario. Recuperación: emitir el token nuevo y comprobarlo antes de revocar el actual, para no perder acceso |
| SEC-13 | Escritor automático fuera de `blends` | Credencial no inventariada | [D] la [topología](github-topology.md#hoy) registra commits automáticos de baseline diario en `syrah`; la credencial que los firma no está identificada en VCX | 27001 A.5.16, A.8.2; SOC 2 CC6.2 | Identificar credencial, dueño y baja en el inventario de automatizaciones del paso 4 del [mapa](repository-map.md#secuencia-acordada-para-preservar-y-versionar) |

### Productos Blends, Brix y Cellar en `vcx/`

| ID | Control | Estado | Evidencia | Correspondencia | Pendiente |
|---|---|---|---|---|---|
| SEC-14 | Superficie publicable declarada y scan del historial exportado antes de publicar | Propuesto | [D] VCX-D032, con la opción de historial filtrado elegida el 2026-11-01 y el resto sin ratificar, según el [registro](../decisions/README.md) | 27001 A.5.14, A.8.12; SOC 2 CC6.7 | Ratificación y autorización de ejecución; el scan debe correr sobre todo el historial exportado con dos herramientas, como fija el diseño |
| SEC-15 | Procedencia y licencia de skills de terceros incorporadas a Brix | Implementado, sin versionar | [H] `brix/.claude/skills/brix-killer-questions/` conserva `PROVENANCE.md`, `UPSTREAM-SKILL.md` y la licencia del origen; `brix-llm-council/` conserva `PROVENANCE.md`; el directorio está sin seguimiento en Git | 27001 A.5.19 a A.5.21, A.8.30; SOC 2 CC9.2 | Versionar con su alcance; fijar la regla de procedencia obligatoria para cada skill o MCP admitido en el catálogo |
| SEC-16 | Revisión de seguridad de cambios sensibles | Asignado, sin uso medido | [D] fila de la [matriz de tooling](tooling-matrix.md) para conducción en Cellar, skill `security-review` con alcance de tarea | 27001 A.8.29; SOC 2 CC8.1 | Definir qué cambio cuenta como sensible; medir uso |
| SEC-17 | Canal de reporte de vulnerabilidades por producto | Ausente | [H] no existe `SECURITY.md` en la raíz ni en los productos | 27001 A.5.24 a A.5.26, A.8.8; SOC 2 CC7.3 | Necesario antes de que un producto sea público; un archivo por repositorio, proporcional: contacto y plazo de respuesta |
| SEC-18 | Aislamiento efectivo entre propietarios e instancias; secretos fuera del respaldo | Diseñado | [D] invariantes 9 y 10 de la [matriz](responsibility-matrix.md#5-invariantes-de-diseño); el [modelo de iniciativas](../../cellar/docs/initiative-model.md) exige validar el aislamiento antes de escrituras reales y excluye secretos y locks del respaldo | 27001 A.5.15, A.8.3, A.8.13; SOC 2 CC6.1, A1.2 | Sin implementación; la primera instancia real lo convierte en bloqueante |
| SEC-19 | Permisos declarados en la interfaz y verificados en la ejecución de capacidades | Diseñado | [D] [interoperabilidad](interoperability.md): la interfaz declara permisos y la implementación debe verificarlos; una recomendación de Brix no equivale a autoridad | 27001 A.5.15, A.8.3; SOC 2 CC6.1 | Sin código; el primer comando de Brix debe traerlo |

### Agentes y herramientas de trabajo

| ID | Control | Estado | Evidencia | Correspondencia | Pendiente |
|---|---|---|---|---|---|
| SEC-20 | Inventario de conectores y permisos de las sesiones de agentes sobre este workspace | Ausente | [H] la sesión que redactó este documento tenía habilitados conectores de correo, calendario y almacenamiento de archivos del usuario, además de la CLI de GitHub de SEC-12; ningún documento de VCX registra qué conectores admite cada producto o tarea | 27001 A.5.15, A.8.1, A.5.34; 27701; SOC 2 CC6.1, P1 | [P] Registrar en la matriz de tooling, por fila, qué accesos requiere cada herramienta; desactivar los que una tarea no necesita |
| SEC-21 | Autorización donde ocurre el efecto, límites de gasto y excepciones registradas | Regla adoptada, con ejemplos | [D] VCX-P7 y VCX-P8; VCX-D027 es un ejemplo de excepción acotada con alcance, rama y acciones enumeradas | 27001 A.5.36; SOC 2 CC1.1, CC3.1 | Sin control ejecutable; el presupuesto de este inventario se declara abajo |

## Puertas por transición

[P] Cada transición del [mapa](repository-map.md#secuencia-acordada-para-preservar-y-versionar) o de VCX-D032 reúne pruebas sobre una revisión identificada por hash, una autoridad decide con ellas y queda registrada la resolución de cada fallo o excepción. Si cambia el contenido evaluado, se revisa qué evidencia sigue siendo válida: la evidencia queda atada a la revisión sobre la que se tomó. Esta tabla enlaza las filas SEC sin duplicarlas y no altera el orden del mapa, que sigue siendo su fuente.

| Transición | Controles aplicables | Evidencia requerida para continuar | Decide |
|---|---|---|---|
| Crear el remoto privado `vcx`, decisión abierta en la [topología](github-topology.md) | SEC-01, SEC-02, SEC-03, SEC-04 | Visibilidad privada comprobada por API; recuperación clonando desde el remoto y comparando el hash de `HEAD`; mecanismo de compuerta de secretos decidido antes del primer push; tratamiento de la dirección de correo decidido por el usuario | Responsable del portfolio, cuando esté registrado; mientras tanto, autorización puntual del usuario con alcance explícito |
| Clon de autoría y corte de escritores del precursor, pasos del mapa y VCX-D030 | SEC-08, SEC-10, SEC-13 | Inventario de automatizaciones y credenciales con dueño y baja; hooks activos en el checkout que recibe escritores, comprobados con una ejecución que bloquee un secreto de prueba | PO de Blends, bajo el gobierno vigente del precursor |
| Primer clon independiente de cada producto, VCX-D025 | SEC-06, SEC-07, SEC-15, SEC-19 | Protección de `main` y check de secretos configurados en el repositorio nuevo, comprobados por API y por un run; procedencia de skills versionada; permisos declarados en cada capacidad | Responsable del producto según el gobierno adoptado |
| Publicar un producto, VCX-D032 | SEC-04, SEC-09, SEC-14, SEC-17 | Hash exacto del historial exportado; scan completo con dos herramientas y tratamiento registrado de cada hallazgo; `SECURITY.md` presente; secret scanning y push protection comprobados por API en el repositorio público nuevo | Autoridad que ratifique VCX-D032; PO de Blends sobre importes y superficie publicable |
| Primera instancia real de Cellar, disparador de VCX-D023 | SEC-18, SEC-20 | Prueba de acceso cruzado entre propietarios que falla; conectores admitidos por tarea registrados en la matriz de tooling | Responsable de custodia del Cellar y responsable del portfolio |

## Prioridades propuestas

[P] Orden por riesgo demostrado, cobertura compensatoria y exposición, no por cantidad. Cambió respecto de la primera versión del mismo día: la medición de respaldos movió SEC-01 al primer lugar. Ninguna corrección se ejecuta desde este documento; cada una lleva una recuperación breve.

1. **SEC-01 y SEC-02.** No se halló ningún respaldo por los medios medidos y no hay cobertura compensatoria. Crear el remoto privado es una decisión ya abierta en la topología. Recuperación: ninguna necesaria; crear un remoto no modifica el repositorio local.
2. **SEC-12, SEC-13 y SEC-20.** Credenciales amplias o no inventariadas. El keyring compensa la lectura del disco, pero no el alcance del token sobre los proyectos. Inventariar primero; reducir después, con decisión del usuario. Recuperación: emitir y comprobar la credencial nueva antes de revocar la anterior.
3. **SEC-08.** Control que se cree activo y no actúa, con cobertura parcial de SEC-07 en la integración. La ventana de exposición es la rama en el remoto privado. Corrección en el checkout vigente, con alcance propio del PO de Blends. Recuperación: restaurar la ruta anterior de hooks.
4. **SEC-17, SEC-09 y SEC-14.** Condiciones previas a cualquier repositorio público; ordenan la secuencia de VCX-D032, no la adelantan. Recuperación: un repositorio público nuevo puede volverse privado, pero lo expuesto no se retira; por eso la puerta exige el scan antes.
5. **SEC-18 y SEC-19.** Pasan a bloqueantes con la primera instancia real o el primer comando de Brix; antes no requieren trabajo.

## Responsables

[P] Dos roles distintos, conforme a la [RACI](responsibility-matrix.md#4-matriz-raci-humana-propuesta): quien mantiene el inventario y reúne pruebas (R) y quien autoriza cambios o acepta riesgos (A).

- **Autoridad.** Para las filas del precursor existe hoy: el PO de Blends, bajo su gobierno vigente, que no autoriza corregir el precursor desde VCX. Para las filas de la raíz y de los productos no hay designación general registrada. Esa falta no invalida una autorización puntual del usuario con alcance explícito, como las que registran VCX-D026 y VCX-D027; solo obliga a pedirla en cada caso. Esa propuesta está registrada como [VCX-D034](../decisions/README.md), pendiente de ratificación.
- **Mantenimiento.** Quien prepara una transición actualiza las filas que esa puerta exige, como parte de su evidencia, y registra fecha y conclusión. No hace falta un mantenedor permanente hasta que exista una revisión periódica programada.

## Presupuesto

[P] Límite de gasto nuevo para todo lo listado: cero. Cada control propuesto usa funciones ya disponibles sin costo en los repositorios públicos previstos o herramientas locales ya presentes. Un escaneo pago, una plataforma de cumplimiento o una auditoría requieren autoridad y límite declarados antes de comprometerlos, según VCX-P8.

## Relación con los marcos

[P] ISO/IEC 27001 e ISO/IEC 27701 aplican a una organización que gestione seguridad o trate datos personales, operen o no un servicio; SOC 2 informa sobre los controles de una organización de servicios y lo emite un auditor independiente. Hoy VCX no opera servicios para terceros y los únicos datos personales medidos son los de SEC-04 y los accesibles por SEC-20. Abrir un trabajo formal de certificación o de SOC 2 requiere propósito, alcance, autoridad y presupuesto definidos; este inventario es su insumo, no su inicio.

## Mantenimiento

Cada fila conserva la fecha de su última medición en la evidencia. Un hecho [H] se vuelve a medir cuando cambia su condición o antes de cada transición del [mapa](repository-map.md#secuencia-acordada-para-preservar-y-versionar); un hecho [D] se actualiza enlazando la fuente nueva. Las filas no se eliminan: un control retirado cambia su estado y conserva la traza. La correspondencia normativa se revisa cuando se decida certificar; hasta entonces es orientativa.

Un script de re-medición queda pospuesto hasta que las comprobaciones manuales sean repetibles y cada comando tenga definido qué mide y qué conclusión admite; automatizar una inferencia débil solo la repite más rápido. La tabla siguiente fija ese significado para las mediciones [H] de esta revisión, todas de solo lectura.

| Fila | Comando o lectura | Qué mide | Conclusión que admite |
|---|---|---|---|
| SEC-01 | `git remote -v`; `tmutil destinationinfo`; ruta real de la carpeta; búsqueda de Spotlight en la carpeta de usuario | Remoto configurado, destinos de Time Machine, pertenencia a iCloud Drive, otras copias indexadas | Ausencia de esos cuatro respaldos; no descarta otros medios |
| SEC-03 | `git config core.hooksPath`, contenido del directorio de hooks y commit de prueba con un valor sintético en un clon desechable | Hooks configurados en la raíz y si bloquean | Ausencia de compuerta local; o compuerta activa en ese clon, no en otros |
| SEC-06 | API de GitHub, protección de `main` | Configuración en vigor en ese momento | Qué exige la protección; no que los checks pasen o fallen |
| SEC-07 | Lectura del workflow `ci-node.yml` | Qué haría el job `verify` | Existencia del control; no su ejecución ni resultado |
| SEC-08 | `git config core.hooksPath` y existencia de esa ruta | Si Git puede encontrar los hooks | Hooks no ejecutados en ese checkout; no juzga su contenido |
| SEC-09 | API de GitHub, campo de seguridad del repositorio | Estado reportado de esas funciones | Reportado o no reportado; nunca activado o desactivado |
| SEC-12 | `gh auth status` | Scopes y almacenamiento del token activo | Alcance declarado; no su uso efectivo |
| SEC-15 | Listado de `brix/.claude/skills/` y estado en Git | Archivos de procedencia y seguimiento | Presencia de procedencia; no su exactitud |
| SEC-17 | Búsqueda de `SECURITY.md` en el árbol | Existencia del archivo | Ausencia del canal declarado; no de un canal informal |
