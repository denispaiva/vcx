# Inventario de controles de seguridad y privacidad

Fecha: 2026-11-01. Estado: propuesta. Fuente editable del estado de los controles de seguridad y privacidad que afectan a VCX, a sus productos y al precursor del que provienen. Autorizado como redacción documental el 2026-11-01 en el chat con Claude («Sí, redactar»), tras una evaluación cruzada con otra sesión que convergió en empezar por este inventario antes que por un programa de conformidad. Este documento no activa controles, no asigna autoridad, no modifica el precursor ni autoriza publicación, migración o gasto.

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

La columna de correspondencia normativa indica a qué requisito se parece cada control. No demuestra satisfacción: eso solo lo prueba la columna de evidencia. Los números de ISO/IEC 27001:2022 Anexo A y las series de los Trust Services Criteria de SOC 2 son una asignación orientativa hecha de memoria por el asistente, pendiente de cotejo con el texto de las normas. ISO/IEC 27701 se indica solo donde hay datos personales.

## Inventario

### Raíz VCX

| ID | Control | Estado | Evidencia | Correspondencia | Pendiente |
|---|---|---|---|---|---|
| SEC-01 | Copia del repositorio raíz fuera de esta máquina | Ausente | [H] `git remote -v` vacío; la [organización en GitHub](github-topology.md#hoy) registra que nada de VCX está en GitHub | 27001 A.8.13; SOC 2 A1.2 | Crear el remoto privado `vcx`, decisión abierta en la topología; hasta entonces la única copia es local |
| SEC-02 | Recuperación del commit base documental | Verificado una vez | [D] [reporte del 2026-11-01](../superpowers/reports/2026-11-01-root-baseline-verification.md): extracción y comparación de hashes de `f47c71f` | 27001 A.8.13, A.5.33; SOC 2 A1.3 | Repetir tras SEC-01 sobre la copia remota |
| SEC-03 | Compuerta de secretos previa al commit en la raíz | Ausente | [H] `core.hooksPath` sin definir y sin hooks en `.git/hooks`; no hay `.gitignore` | 27001 A.8.12; SOC 2 CC6.7 | Decidir mecanismo antes del primer push; VCX-D032 prevé scan del historial al publicar, no una compuerta continua |
| SEC-04 | Datos personales y rutas locales en documentos versionados | Hallazgo abierto | [D] el [diseño de visibilidad](../superpowers/specs/2026-11-01-public-visibility-design.md) midió una dirección de correo en el registro de decisiones y 31 rutas absolutas en documentos históricos | 27001 A.5.34, A.8.12; 27701; SOC 2 P4 | Tratamiento previsto en VCX-D032 antes de publicar; la dirección es del usuario, quien decide si se conserva |
| SEC-05 | Contenido no confiable tratado como datos y autoridad explícita en agentes | Regla adoptada, sin control ejecutable | [D] VCX-P5 y VCX-P7 en [AGENTS.md](../../AGENTS.md#principios-transversales-de-vcx); el mismo texto declara que no existen controles ejecutables que los apliquen | 27001 A.5.1, A.5.36; SOC 2 CC1.1 | Ninguno en esta etapa; la revisión de reglas sigue VCX-P9 |

### Precursor `../blends` y repositorio `denispaiva/blends`

Solo lectura según VCX-D024. Nada de esta sección se corrige desde VCX: cada corrección requiere alcance propio en el checkout que corresponda, según VCX-D031.

| ID | Control | Estado | Evidencia | Correspondencia | Pendiente |
|---|---|---|---|---|---|
| SEC-06 | Protección de `main` | Verificado | [H] API de GitHub: `enforce_admins` activo; checks obligatorios `base / verify`, `governance`, `lint` y `teyst`; sin revisores obligatorios ni historial lineal | 27001 A.8.32, A.8.4; SOC 2 CC8.1 | El check `teyst` acopla la protección al proyecto, riesgo ya registrado en la [topología](github-topology.md); sin revisores obligatorios, el único control humano es el autor del PR |
| SEC-07 | Compuerta de secretos en CI | Implementado | [H] `ci-node.yml`, job `verify`: Betterleaks 2.0.0-rc.1 descargado con firma cosign y suma SHA-256 comprobadas; es parte del check obligatorio `base / verify` de SEC-06 | 27001 A.8.12, A.8.28; SOC 2 CC6.7, CC8.1 | No se observó una ejecución en esta medición; leer un run reciente para pasar a verificado |
| SEC-08 | Compuerta de secretos local previa a commit y push | Inactivo | [H] `.githooks/pre-commit` y `pre-push` existen, pero `core.hooksPath` apunta a `/Users/denispaiva/blends/.githooks`, ruta que no existe; Git no ejecuta ningún hook en ese checkout. Registrado en la [propuesta VCX-D030](../decisions/README.md) | 27001 A.8.12; SOC 2 CC6.7 | Corregir con alcance propio; SEC-07 sigue cubriendo el push al remoto, no el commit local |
| SEC-09 | Secret scanning, push protection y actualizaciones de Dependabot en GitHub | No reportados | [H] la API no devuelve estado de esas funciones para el repositorio privado | 27001 A.8.8, A.8.12; SOC 2 CC7.1 | VCX-D032 cuenta con que los repositorios públicos nuevos las tengan disponibles; verificar y activar al crear cada uno |
| SEC-10 | Gestión de secretos: identidad efímera y excepción `GH_SCARCITY_PAT` con rotación por vencimiento | Adoptado en el precursor | [D] `vc/docs/standards/secrets.md`, consultado en solo lectura; tabla de mecanismos por caso y excepción documentada con baja prevista | 27001 A.5.17, A.8.24; SOC 2 CC6.1 | No rige en VCX hasta conciliar por VCX-D011; el estándar no se copia |
| SEC-11 | Seguridad de aplicación del portfolio | Decidido, no vigente | [D] `vc/docs/standards/security.md` lo declara en su encabezado, con migración diferida a un PR del precursor; ya identificado en [fuentes](../sources.md#antecedentes-de-los-principios-transversales) | 27001 A.8.25 a A.8.29; SOC 2 CC8.1 | Es asunto del PO de Blends en el precursor; VCX solo lo registra |
| SEC-12 | Alcance del token de la CLI de GitHub | Hecho, sin evaluar | [H] scopes `gist`, `read:org`, `repo` y `workflow`; `repo` alcanza todos los repositorios privados de la cuenta, incluidos los proyectos; no incluye lectura de plan ni consumo, como anotó VCX-D032 | 27001 A.5.15, A.8.2; SOC 2 CC6.1, CC6.3 | [P] Evaluar un token de alcance fino por tarea; decisión del usuario, sin cambio en esta etapa |
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

## Prioridades propuestas

[P] Orden por riesgo, no por cantidad. Ninguna corrección se ejecuta desde este documento.

1. **SEC-08.** Un control que se cree activo y no actúa es el peor caso de VCX-P5. Corrección en el checkout vigente del precursor, con alcance propio del PO de Blends.
2. **SEC-01 y SEC-02.** La única copia de VCX es local. Crear el remoto privado es una decisión ya abierta en la topología.
3. **SEC-12, SEC-13 y SEC-20.** Credenciales amplias o no inventariadas. Inventariar primero; reducir alcance después, con decisión del usuario.
4. **SEC-17, SEC-09 y SEC-14.** Son condiciones previas a cualquier repositorio público; ordenan la secuencia de VCX-D032, no la adelantan.
5. **SEC-18 y SEC-19.** Pasan a bloqueantes con la primera instancia real o el primer comando de Brix; antes no requieren trabajo.

## Responsables

[P] La RACI exige una autoridad humana competente sobre cada ámbito para cambiar controles compartidos. Hoy no está designada. Se propone registrar como decisión: el responsable del portfolio como A de los controles de la raíz y de los productos; el PO de Blends como A de los del precursor. Hasta ese registro, ninguna fila tiene responsable asignado y este documento no lo supone.

## Presupuesto

[P] Límite de gasto nuevo para todo lo listado: cero. Cada control propuesto usa funciones ya disponibles sin costo en los repositorios públicos previstos o herramientas locales ya presentes. Un escaneo pago, una plataforma de cumplimiento o una auditoría requieren autoridad y límite declarados antes de comprometerlos, según VCX-P8.

## Relación con los marcos

[P] ISO/IEC 27001 e ISO/IEC 27701 aplican a una organización que gestione seguridad o trate datos personales, operen o no un servicio; SOC 2 informa sobre los controles de una organización de servicios y lo emite un auditor independiente. Hoy VCX no opera servicios para terceros y los únicos datos personales medidos son los de SEC-04 y los accesibles por SEC-20. Abrir un trabajo formal de certificación o de SOC 2 requiere propósito, alcance, autoridad y presupuesto definidos; este inventario es su insumo, no su inicio.

## Mantenimiento

Cada fila conserva la fecha de su última medición en la evidencia. Un hecho [H] se vuelve a medir cuando cambia su condición o antes de cada transición del [mapa](repository-map.md#secuencia-acordada-para-preservar-y-versionar); un hecho [D] se actualiza enlazando la fuente nueva. Las filas no se eliminan: un control retirado cambia su estado y conserva la traza. La correspondencia normativa se revisa cuando se decida certificar; hasta entonces es orientativa.
