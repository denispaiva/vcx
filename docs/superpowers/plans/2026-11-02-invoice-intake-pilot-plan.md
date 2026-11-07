# Prueba local de extracción de comprobantes

Fecha: 2026-11-02. Estado: acordado, sin iniciar; IP-1 resuelto, siguiente paso IP-2. Decisión: VCX-D041 en el [registro](../../decisions/README.md).

## Objetivo y pregunta

Responder con evidencia si extraer comprobantes de los buzones personal y de Tintum aporta valor para el gasto real de la capacidad `finops-ledger`, antes de elegir un mecanismo de ingesta o construir una herramienta en Brix. Con 20 a 30 comprobantes la prueba mide viabilidad, no una tasa general de confiabilidad.

## Antecedentes

- El conector `gmail` sigue rechazado ([matriz](../../architecture/tooling-matrix.md), fila «Respaldar importes con comprobantes reales»): puede enviar y borrar sobre un buzón personal. Esta prueba no lo reevalúa ni lo usa.
- Gmail no ofrece un permiso OAuth acotado a una etiqueta: `gmail.readonly` lee el buzón completo. Una etiqueta solo limita lo que el programa selecciona.
- El ledger del precursor (`billing-ledger.schema.json`) admite importes en USD y una lista cerrada de proveedores, y está en solo lectura. Antes de incorporar resultados hace falta resolver su compatibilidad; no antes de la prueba.
- Hechos de OAuth verificados el 2026-11-02 en la documentación de Google ([tokens](https://developers.google.com/identity/protocols/oauth2), [verificación](https://developers.google.com/identity/protocols/oauth2/production-readiness/restricted-scope-verification)): los tokens de renovación de apps External en Testing vencen a los 7 días; los permisos de Gmail se invalidan si cambia la contraseña; existen excepciones de verificación por uso personal e interno; la evaluación de seguridad aplica cuando los datos pasan por servidores de terceros. Una app Internal de Tintum no admite la cuenta personal.

## Alcance de Tintum

Resuelto en IP-1 el 2026-11-02: el usuario eligió «Solo lo de VCX». Del buzón de Tintum entran al lote solo comprobantes de gasto atribuible a VCX. Si un comprobante cubre gasto de VCX y de Tintum, entra con su total y se marca como compartido; el porcentaje de asignación no se estima en la prueba y queda para la incorporación al ledger, que ya separa asignaciones.

## Excepciones

- 2026-11-02: el usuario pidió «en el buzón de tintum tienes que buscar todo lo que sea invoice y yo te diré que registrar en finops». El agente hizo una búsqueda de solo lectura con el conector `gmail` de la sesión (`search_threads`, vista resumida: remitente, destinatario y asunto de 50 hilos del último año; sin abrir mensajes ni adjuntos). El conector resultó estar autenticado en la cuenta personal, no en `tintum.app`, y no hubo búsquedas posteriores. No se escribió nada en el buzón. Hallazgo: las facturas de Google Workspace de `tintum.app` llegan a la cuenta personal.
- 2026-11-02: ante «todas esas aplican», el agente abrió en solo lectura los diez comprobantes elegidos y otros dos (créditos de API de Anthropic y el recibo de GitHub del 2026-08-24). También hizo una búsqueda por remitentes de proveedores del ledger desde el 2026-08-01, que trajo remitente y asunto. Ante «Falta la de Google Store» y «también faltan las de GCP», buscó y abrió además el recibo de Google Play y tres avisos de Cloud Billing. Ante el pedido de registrar Supabase, Namecheap y Cloudflare y de «regenerar una línea de tiempo desde que nació el inbox», buscó por proveedor en todo el historial. Abrió los recibos de Anthropic, GitHub, Moonshot, Namecheap y Google One. La línea de tiempo quedó fuera del repo, en el scratchpad de la sesión. El usuario sumó las facturas de Workspace y Supabase del buzón de Tintum, leídas con Codex, y aclaró que el resto del gasto llega a la cuenta personal. Por VCX-D042, la línea de tiempo pasó al ledger privado de pagos. Los adjuntos PDF no se descargaron. Cruce con los ledgers del precursor, leídos sin escribir, y destino de registro pendientes de decisión del usuario.

## Fuera de alcance

OAuth, conectores MCP, LLM externo sobre el lote de evaluación, escrituras en cualquier ledger, tipo de cambio (los candidatos conservan la moneda original y no se suman entre monedas), código en Brix y archivos de comprobantes dentro del workspace.

## Diseño

**Conjuntos separados.** Un conjunto de desarrollo, con 2 o 3 ejemplos por emisor, sirve para escribir los lectores. Un lote de evaluación distinto, de 20 a 30 `.eml`, sirve para medir; sus ejemplos nunca se usan para escribir lectores.

**Casos sembrados en el lote.** Al menos un reenvío, un comprobante recibido en ambas cuentas, uno en ARS con impuestos, un recibo solo en el cuerpo HTML y uno sin número de factura.

**Identidades.**

| Identidad | Composición | Uso |
|---|---|---|
| Ingesta | Cuenta de origen declarada, `Message-ID` cuando exista, SHA-256 del `.eml` y localizador de la parte MIME | Reintentar sin duplicar la ingesta; un reenvío es otra ingesta |
| Comprobante | Emisor + número de factura, cuando exista | Detectar el mismo comprobante en ingestas distintas |
| Posible duplicado | Emisor + fecha + importe + moneda, sin número | Solo señala; la fusión la decide una persona |

La prueba demuestra la trazabilidad de la exportación, no la identidad mediante el ID interno de Gmail.

**Candidatos.** Archivo fuera del repo con identidad de ingesta, identidad del comprobante, emisor, número, fecha, moneda original, neto, impuestos, total, marca de comprobante compartido, ruta del `.eml` y SHA-256. El `.eml` se conserva como evidencia; el hash verifica integridad, no lo reemplaza.

**Lectores.** Deterministas y locales, sin extracción, telemetría ni servicios auxiliares que envíen datos fuera del equipo.

## Criterios de aceptación

Valores esperados revisados a mano antes de correr los lectores. N cuenta todos los comprobantes esperados, incluidos los omitidos o no interpretados.

1. Total y moneda correctos en al menos `ceil(0,95 × N)` comprobantes; con N entre 20 y 39, admite un error.
2. Todos los duplicados sembrados señalados.
3. Cero fusiones incorrectas.
4. Exportación + ejecución + revisión + corrección en menos tiempo que el proceso manual actual, medido sobre el mismo lote. El tiempo de desarrollo se informa aparte.

## Privacidad

Los ejemplos de desarrollo salen del equipo hacia el proveedor del modelo de la sesión donde se escriban los lectores: Anthropic en Claude Code, OpenAI en Codex. Se comparten sanitizados, cabeceras y cuerpos incluidos. El lote de evaluación no se comparte; al chat vuelven solo métricas agregadas y los casos fallidos que el usuario decida mostrar, también sanitizados.

## Pasos

| ID | Paso | Responsable | Depende de |
|---|---|---|---|
| IP-1 | Definir qué gasto de Tintum entra. Hecho: solo lo atribuible a VCX | Usuario | Ninguno |
| IP-2 | Elegir la carpeta de la prueba fuera del workspace y listar los remitentes que realmente facturan | Usuario | IP-1 |
| IP-3 | Exportar el conjunto de desarrollo sanitizado y el lote de evaluación con sus valores esperados; medir el tiempo de exportación y el del proceso manual | Usuario | IP-2 |
| IP-4 | Escribir los lectores en la carpeta de la prueba usando solo el conjunto de desarrollo | Agente | IP-3 |
| IP-5 | Correr los lectores sobre el lote y comparar con los valores esperados | Usuario, con el script del agente | IP-4 |
| IP-6 | Con los resultados, decidir entre no construir, exportación periódica, OAuth sobre las cuentas o OAuth sobre un buzón dedicado que reciba copias; registrar la decisión | Usuario | IP-5 |

Si la prueba falla, se mantiene el proceso manual y no se construye nada en Brix. Elegir OAuth exige reevaluar la herramienta por el procedimiento de VCX-D035. El buzón dedicado requiere reglas de reenvío configuradas por el usuario en cada cuenta de origen, infiere la cuenta de origen desde las cabeceras de reenvío y lleva datos de Tintum a otro buzón: es también una decisión de gobierno de datos.
