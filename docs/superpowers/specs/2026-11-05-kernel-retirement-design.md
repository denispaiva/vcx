# Retiro de «Blends Kernel» como entidad objetivo

Fecha: 2026-11-05. Estado: VCX-D045, ratificada por el usuario como decisión documental el 2026-11-05. No autoriza ejecución ni cambia el precursor. Etiquetas: [H] hecho medido; [I] interpretación; [P] propuesta.

## Problema

[H] `vc/framework/` solo contiene su `.roadmap.json`. El nombre «Blends Kernel» agrupa método, capacidades y datos que VCX-D029 reparte entre dueños distintos. [I] Sostenerlo obligaría a mantener una entidad sin dueño propio dentro del modelo de productos.

## Reparto medido

[H] Medición de solo lectura sobre `vc/tools/` en `main` `f86a2a7d`, sin carpetas de pruebas: 87 archivos y 29.550 líneas. La clasificación usa nombre, cabecera y registro de capacidades; no se leyó cada archivo completo.

| Destino | Archivos | Líneas | Contenido |
|---|---:|---:|---|
| Blends | 26 | 10.430 | `validate-*`, `check-branch-scope`, `check-lifecycle`, `verify` y `lib/verify` |
| Solera | 24 | 11.280 | Tren, cola, `recycle`, `deliver`, sesiones, backlog y roadmap, `reconcile-backends`, `check-renewals` |
| Brix | 36 | 7.796 | `blend-run`, resolución de modelos, registro y uso de tooling, recursos, escasez y utilidades compartidas |
| Sin clasificar | 1 | 44 | `README.md` |

[P] Fuera de `vc/tools/`: `roadmap/` y los estándares van a Blends; `vc/finops/` e `vc/tooling/evaluations/` van a Solera. De los seis JSON de configuración, `data-naming` va a Blends, `brix-capabilities` a Brix (DH-19) y `branch-scopes`, `codenames`, `cepas` y `environment-ids` a Solera.

### Tren y cola quedan en la instancia

La primera propuesta los llevaba a Brix. La medición lo desaconseja: el tren importa directamente `validate-versions`, `check-branch-scope` y `lib/verify/environment`, de modo que Brix dependería de Blends. Además, publicaría código de un mecanismo con hallazgos de seguridad abiertos.

[P] Quedan en Solera, como ya indica el [destino de decisiones](../../architecture/repository-map.md#destino-de-las-decisiones-durante-la-transición) para `queue` y trenes. Pasarían a Brix solo si aparece un segundo consumidor (VCX-P3). El costo es deuda declarada: código ejecutable dentro de una instancia. Backlog y roadmap se quedan con ellos porque dependen de la cola y el contrato de conducción de Cellar todavía no existe.

### Imports por resolver

[P] Dirección permitida: Solera puede importar de Blends y Brix, y Blends de Brix. Brix no importa de ninguno, porque no presupone un Cellar ni Blends.

[H] Con este reparto quedan cuatro imports fuera de esa regla, a cortar antes de extraer Brix:

| Origen | Destino |
|---|---|
| `lib/versions.mjs` | `validate-versions.mjs` |
| `produce-resource-actuals.mjs` | `validate-tooling.mjs` |
| `lib/register-tooling.mjs` | `lib/roadmap-writer.mjs` |
| `lib/usage-records.mjs` | `lib/queue.mjs` |

## Puntos abiertos

### `validate-governance`

[H] Son 2.524 líneas sin imports propios, con las reglas escritas en el código, que reciben la matriz de roles y el plan por argumento. No hay un motor que separar. [P] Va entero a Blends, porque la [frontera](../../architecture/responsibility-matrix.md#1-método-y-conducción) dice que Blends publica el método y lo verifica. Esto reemplaza la idea inicial de separar regla y motor, que sumaba trabajo sin un consumidor que lo pida.

El mismo criterio aplica a los demás validadores: Blends conserva código ejecutable y no queda solo en documentos.

### Export de VCX-D032

[I] La opción B y la regla de salida B' no cambian. El paso 3 ya pide declarar la superficie publicable por rutas: cambia la lista, no el procedimiento.

[H] Una lista provisoria de Blends (validadores, `verify`, estándares, plantillas, `roadmap/` y `AGENTS.md`) toca 671 commits, frente a los 1088 de las rutas del kernel. La lista definitiva suma workflows y debe medirse otra vez. [I] Publicar menos reduce la superficie a revisar; los 131 archivos con importes también deben recontarse.

[P] Ajustes acordados:

- El texto «rutas del kernel» pasa a «superficie publicable de Blends» en VCX-D032, VCX-D030 y sus documentos.
- `train-notice` deja de pasar al público con el kernel y sigue a Solera. Los minutos de esa CI siguen consumiendo cuota privada.
- El paso 4, Brix, amplía su export con los archivos del reparto.

### Movimiento a `vc/kernel/`

[H] El PO aprobó el movimiento y el usuario eligió el 2026-11-01 ejecutarlo en el destino, nunca en el precursor (DH-10). [I] Con VCX-D045 ese destino deja de existir. [P] Revocar expresamente la opción B de la spec del 2026-10-05 y la Fase 2 de configuración, y conservar la separación semántica de D-1 mediante el reparto de arriba. D-2 pierde objeto. D-3, sobre inventario de backends, sigue vigente. Las identidades `framework` no cambian.

[P] Esto concilia solo esos puntos. VCX-D011 sigue pendiente para el resto de destinos y controles. La spec del precursor no se edita: la revocación vive en este registro y se refleja en la `queue` cuando el PO lo ordene.

### Pedidos abiertos

[H] Son 58 en la `queue` al 2026-11-01. [P] Por destino: 36 Solera, 13 Blends, 6 Brix, 1 a dividir y 2 por cerrar, los dos movimientos al kernel. Es una clasificación por título y resumen, sin validar por el PO. Su detalle vive en un triage privado en `cellars/`, porque trae información del portfolio y de seguridad.

[I] Los tres pedidos P0 no dependen de este retiro y no deberían esperar a la migración.

## Riesgos

- **Deuda en la instancia.** Solera conserva 11.280 líneas de código, y otra instancia no tendría tren. Es aceptable mientras haya un solo portfolio.
- **Clasificación superficial.** Puede haber archivos mal ubicados. Cada extracción debe repetir la medición de imports.
- **Dos nombres por un tiempo.** «Blends Kernel» sigue como nombre del sistema vigente en el precursor hasta cada extracción.

## Qué no decide

No modifica el precursor, su backlog ni sus identificadores. No crea repositorios ni autoriza exports. No cierra VCX-D011 ni fija fechas.
