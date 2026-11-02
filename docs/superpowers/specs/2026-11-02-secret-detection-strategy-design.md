# Estrategia verificable de detección de secretos para VCX

Fecha: 2026-11-02. Estado: **propuesta del asistente**, sin ratificar. Autoridad: el encargo del usuario del 2026-11-02 en el chat con Claude, que autoriza análisis y redacción y no autoriza instalar herramientas, modificar repositorios, activar hooks, crear remotos, ejecutar workflows, publicar contenido ni cambiar controles efectivos. Este documento no cambia ningún estado del [inventario de controles](../../architecture/security-controls-inventory.md) y no transfiere ninguna aprobación del precursor a VCX.

Etiquetas: [H] hecho medido el 2026-11-02 en solo lectura, con hora UTC cuando importa el orden; [D] hecho documentado en una fuente fechada que se enlaza; [O] hecho tomado de documentación oficial del proveedor, con enlace; [I] interpretación; [P] propuesta; [U] decisión del usuario en este chat.

Lo único ejecutado fuera de lecturas fue un script de expresiones regulares en el scratchpad de la sesión, probado sobre repositorios desechables con valores sintéticos generados al azar y corrido en solo lectura sobre la raíz `vcx`. No se instaló nada, no se escribió en `../blends` ni en `.git`, y este archivo es el único cambio en el árbol de trabajo.

## 1. Diagnóstico

### 1.1 Antecedentes revalidados

El encargo pidió tratar cinco afirmaciones como antecedentes por revalidar. La cuarta dejó de ser cierta mientras se redactaba este documento: otra sesión, con autorización del usuario registrada en el commit `22b927e`, creó `denispaiva/vcx` público y subió `main` a las 11:54 UTC. Las mediciones anteriores a esa hora se conservan con su hora para que el orden quede claro.

| Afirmación | Fuente | Fecha y hora | Resultado | Limitación |
|---|---|---|---|---|
| No hay scanner de secretos instalado en la máquina | [H] `command -v` de `gitleaks`, `trufflehog`, `betterleaks`, `detect-secrets`, `ggshield`, `cosign` y `pre-commit` | 2026-11-02 11:52 UTC | Vigente: ninguno en `PATH`. Disponibles `git` 2.50.1, `python3` 3.9.6, `bash` 3.2.57 y `ripgrep` 14.1.1 | El [scan del 2026-11-02](../reports/2026-11-02-vcx-secrets-scan.md) bajó Betterleaks 2.0.0-rc.1 a una carpeta temporal, verificó su SHA-256 y lo corrió sobre `main`; no quedó instalado. «No instalado» no significa «nunca ejecutado» |
| No hay hooks efectivos en la raíz | [H] `git config core.hooksPath` sin definir; `.git/hooks` solo con `*.sample`; sin `.githooks`, `.husky` ni `.pre-commit-config.yaml` | 2026-11-02 11:52 UTC | Vigente: SEC-03 sigue ausente | Un hook es local a cada clon y se omite con `--no-verify`; su ausencia se mide por clon, no por repositorio |
| No hay CI | [H] sin `.github/workflows` local; la API devuelve 0 workflows en `denispaiva/vcx` | 2026-11-02 11:56 UTC | Vigente | — |
| No hay remoto | [H] `git remote -v` vacío a las 11:52 UTC; a las 11:55 UTC `origin` = `https://github.com/denispaiva/vcx.git`, creado a las 11:54:23 UTC, público, `main` en `4b01168`, un solo ref remoto | 2026-11-02 11:52 y 11:55 UTC | **Ya no vigente.** El repositorio existe y es público desde las 11:54 UTC. Registrado por otra sesión en el commit `22b927e`, con «Autorizo el alcance» del usuario | Esta sesión no participó en esa publicación; lo que sabe de su autoridad es lo que dice el commit y la [topología](../../architecture/github-topology.md) |
| El precursor usa Betterleaks 2.0.0-rc.1 y gitleaks | [H] lectura de `../blends/.githooks/pre-commit`, `pre-push`, `.github/workflows/ci-node.yml`, `.betterleaks.toml`, `.betterleaksignore` y `vc/docs/standards/secrets.md`, revisión `f86a2a7` | 2026-11-02 | Confirmado: Betterleaks 2.0.0-rc.1 es compuerta en pre-commit, pre-push y CI; gitleaks 8.30.1 corre en sombra. El interruptor es `BLENDS_SECRETS_GATE` en local y la variable `SECRETS_GATE` en CI. La evaluación del precursor tiene estado `approved_with_exception` con revisión al 2026-12-30 | Los hooks de ese checkout no se ejecutan: `core.hooksPath` apunta a `/Users/denispaiva/blends/.githooks`, ruta inexistente (SEC-08). El CI sí tiene el paso (SEC-07, no comprobado por run) |
| Controles nativos de GitHub: disponibilidad y alcance | [H] `GET /repos/denispaiva/vcx`, campo `security_and_analysis`; `GET .../vulnerability-alerts`; `GET .../branches/main/protection`; `GET .../rulesets`; `GET .../actions/permissions/workflow` | 2026-11-02 11:55 UTC | `secret_scanning` **enabled**; `secret_scanning_push_protection` **enabled**; `secret_scanning_non_provider_patterns` disabled; `secret_scanning_validity_checks` disabled; `dependabot_security_updates` disabled; alertas de vulnerabilidades disabled (404). Sin protección de rama (404) y sin rulesets (`[]`). Permiso por defecto de workflows `read`; aprobación de Actions para forks: `first_time_contributors`. [O] La documentación confirma que en repositorios públicos secret scanning «runs automatically for free», que la push protection a nivel de repositorio «is disabled by default» y se activa por un administrador, y que rulesets, ramas protegidas, alertas de Dependabot y runners estándar de Actions están disponibles sin costo en repositorios públicos ([about-secret-scanning](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning), [about-rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets), [facturación de Actions](https://docs.github.com/en/billing/concepts/product-billing/github-actions)) | Estado reportado por la API en ese minuto; no se observó un push bloqueado ni una alerta. La API reporta push protection activa aunque la documentación la describe como apagada por defecto: prevalece la medición, y la diferencia queda sin explicar. No se midió el precursor de nuevo: SEC-09 sigue como está |
| Sin remoto no se puede automatizar nada | [H] el script de la §3 corrió localmente sobre `vcx` sin remoto a las 11:55 UTC; el scan de Betterleaks del mismo día también fue local | 2026-11-02 | Refutada como dependencia técnica. Lo que faltaba era autoridad para instalar y una decisión de motor: una restricción de gobierno | La automatización que sí depende del remoto es la del lado del servidor: CI, push protection y checks obligatorios |

Hechos nuevos que ningún antecedente anticipaba, medidos el 2026-11-02:

- [H] `refs/backup/main-pre-noreply` apunta al `main` anterior a la [reescritura del correo](../reports/2026-11-01-vcx-noreply-rewrite.md) y contiene la dirección personal. No se subió: el remoto tiene un solo ref. Cualquier escaneo o push «de todos los refs» debe excluirlo explícitamente.
- [H] Hay nueve refs `refs/codex/turn-diffs/checkpoints/...` con instantáneas del árbol de trabajo tomadas por una herramienta de agente, que incluyen cuatro archivos `.DS_Store` binarios. `git rev-list --all` los alcanza; un push por nombre de rama no. El escaneo de historial de la §3 los cubre y por eso cuenta 112 commits y 4 blobs binarios, frente a los 63 commits de `main`.
- [H] `main` avanzó tres veces durante este análisis (`d733649` → `4b01168` → `22b927e`): otras sesiones commitean en la misma raíz. Toda evidencia de escaneo queda atada al SHA exacto escaneado, nunca a «main».
- [H] Hay cambios sin commit (`AGENTS.md`, dos líneas) y cuatro `.DS_Store` sin seguimiento. Entrarán al historial que se suba si alguien los agrega; `vcx` no tiene `.gitignore`.

### 1.2 Discrepancias y límites

- **El encargo quedó parcialmente desactualizado al nacer.** Su fase «antes de GitHub» ya no es «antes del remoto». Se conserva porque su contenido sigue siendo necesario: SEC-03 continúa ausente, push protection solo cubre los patrones de proveedores que GitHub reconoce y actúa recién en el push, y la compuerta local sigue siendo lo único que actúa antes de que un secreto entre a un commit. La fase pasa a llamarse «compuerta local, independiente de GitHub».
- **Los patrones de la revisión del 2026-11-01 no se conservaron.** El [reporte](../reports/2026-11-01-vcx-public-history-review.md) enumera familias (tokens de GitHub, Anthropic, OpenAI, AWS, Google, Slack, JWT, claves privadas, asignaciones de `password` o `secret`) sin las expresiones ni los comandos. La reproducción exacta no es posible; la §3 documenta reglas nuevas como propuesta.
- **El scan de Betterleaks del 2026-11-02 verificó integridad, no procedencia.** Su reporte lo declara: sin `cosign` no se comprobó la firma. La cadena de confianza es «el mismo `checksums.txt` contiene el hash que la CI del precursor sí verificó con firma el 2026-10-01». Es un vínculo razonable, no una verificación propia.
- **Un cero no prueba ausencia.** Tanto el scan de Betterleaks como la búsqueda de la §3 informan qué reglas se aplicaron sobre qué revisión. Este documento no afirma que `vcx` no contenga secretos.
- **La aprobación de Betterleaks rc.1 es del PO de Blends para el precursor.** VCX-P7 impide trasladarla. El usuario autorizó rc.1 para un scan puntual («Autorizo rc.1») y después, en este chat, decidió adoptar Betterleaks para VCX (§2.2). La versión fijada y su excepción se registran en VCX con su propia revisión; la del precursor sigue siendo del PO de Blends.

## 2. Decisión técnica previa

### 2.1 Las tres alternativas del encargo

| Alternativa | Qué cubre | Dependencias y mantenimiento | Costo | Qué no cubre |
|---|---|---|---|---|
| **A. Scanner dedicado en local, ahora** | Índice preparado, árbol, historial y rango de commits antes del push; cientos de reglas mantenidas por terceros; huellas estables para excepciones | Un binario por máquina, fijado por versión y verificado antes de instalar; un archivo de configuración y uno de excepciones en el repositorio; revisión de versión cuando cambie | Cero en dinero: binarios publicados sin costo en GitHub Releases. Media hora de instalación verificada por máquina | No actúa si se omite el hook; no protege a quien clona sin instalarlo |
| **B. Búsqueda por expresiones regulares, interina** | Lo mismo en alcance, con once reglas propias y sin mantenimiento externo | Solo `git` y `python3` ya presentes; las reglas son deuda propia | Cero | Cobertura muy inferior: reconoce formatos conocidos de pocos proveedores; sin entropía, sin reglas de contexto, sin huellas compatibles con otra herramienta |
| **C. Esperar al remoto y mantener controles manuales** | Nada antes del push; en el remoto, lo que GitHub active | Ninguna local | Cero | Quedó vacía: el remoto ya existe. Mantener «controles manuales» equivale a B sin script |

[P] **Recomendación: A como objetivo inmediato, con B como puente de días, no de semanas.** A es la alternativa más simple que satisface las restricciones verificadas: sin dinero, sin servicio nuevo, sin dependencia de la raíz para los productos, y con el mismo tipo de herramienta que exige la puerta de publicación de VCX-D032 («scan completo con dos herramientas»). B cuesta menos de instalar pero más de sostener si se prolonga, porque cada regla nueva es trabajo propio y nadie la revisa fuera de VCX. C no existe ya como opción.

Lo que bloquea A hoy no es técnico: es la decisión de motor y la autoridad para instalar un binario en la máquina. B existe para que SEC-03 no siga ausente mientras esa decisión se toma, y para la segunda herramienta de SEC-14 si se prefiere no instalar dos scanners.

### 2.2 Elección de motor

Tres candidatos, todos gratuitos para este uso según la política [Free Tier first](../../../finops-policy.md#free-tier-first-y-eficiencia-de-suscripciones); las condiciones de cada uno se validaron contra su documentación oficial el 2026-11-02 y figuran en la tabla.

| Criterio | gitleaks | Betterleaks | trufflehog |
|---|---|---|---|
| Versión estable más reciente [O] | `v8.30.1`, 2026-03-21, sin prerelease ([releases](https://github.com/gitleaks/gitleaks/releases/tag/v8.30.1)) | `v1.9.0`, 2026-09-29. La línea v2 solo tiene prereleases: `v2.0.0-rc.1` (2026-09-30) a `v2.0.0-rc.6` (2026-10-30); no hay 2.x estable ([releases](https://github.com/betterleaks/betterleaks/releases)) | `v3.99.7`, 2026-10-24 |
| Licencia [O] | MIT ([LICENSE](https://github.com/gitleaks/gitleaks/blob/master/LICENSE)). La acción `gitleaks-action` tiene licencia propia desde su 2.0.0 y exige clave gratuita para organizaciones, no para cuentas personales; no se usa aquí | MIT. El README dice que la mantienen «the folks who made Gitleaks, including the original author» con apoyo de Aikido Security; no documenta por qué existe ni ningún cambio de licencia de gitleaks | AGPL-3.0 |
| Comandos para esta estrategia [O] | `gitleaks git <ruta> --staged` para el índice, `--log-opts` para rangos, `dir` para árboles; `detect` y `protect` están deprecados desde 8.19.0 pero siguen disponibles ([README](https://github.com/gitleaks/gitleaks/blob/master/README.md)) | v2 no es intercambiable con gitleaks: `dir` pasa a `filesystem`, `--report-path` a `--output`, `-v` pasa a significar validar, se retiran los reportes CSV, JUnit y SARIF y `--baseline-path` ([v2_migration](https://github.com/betterleaks/betterleaks/blob/main/docs/v2_migration.md)). `git <ruta> --staged` existe en rc.1, como usa el precursor | `trufflehog git file://<ruta>`; `--results=verified` para filtrar |
| Configuración [O] | `--config` > `GITLEAKS_CONFIG` > `.gitleaks.toml` del objetivo > defaults. `[extend] useDefault = true` extiende las reglas; `.gitleaksignore` con huellas `commit:ruta:regla:línea`, declarado experimental | v2 no carga `.betterleaks.toml` sola: `--config` o variable de entorno; campos TOML desconocidos hacen fallar la carga; `.betterleaksignore` por huella de valor con `--ignore-file` | Allowlists por detector |
| Códigos de salida [O] | «0 - no leaks present / 1 - leaks or error encountered / 126 - unknown flag»; `--exit-code` cambia el código de hallazgo | «exit code 1 for findings by default; `--exit-code` changes that» | No consultado |
| Envío de candidatos a terceros [O] | No valida contra proveedores | v2: «Scans detect secrets without credential provider requests by default»; la validación es opt-in con `-v/--validate` y también por variable de entorno | **Verifica contra la API de cada proveedor por defecto**; opt-out con `--no-verification`. Sin esa opción, cada candidato sale de la máquina |
| Verificación de artefactos [O] | Publica `gitleaks_8.30.1_checksums.txt`; **no publica firmas**: sin `.sig`, `.pem` ni `.sigstore.json`, sin `signs:` en `.goreleaser.yml`, sin instrucciones de verificación en el README. Integridad sí, procedencia solo por TLS y por el origen de la release | Publica `checksums.txt` y `checksums.txt.sigstore.json` firmados con `cosign sign-blob` desde `release.yml` con `id-token: write`; el README **no documenta** `verify-blob` ni la identidad del certificado. La identidad que usa el precursor es inferida de ese workflow y le dio «Verified OK» el 2026-10-01 | Publica `checksums.txt`, `.pem` y `.sig`, con instrucciones de `cosign verify-blob` en el README |
| Pre-commit [O] | `.pre-commit-hooks.yaml` oficial ejecuta `gitleaks git --pre-commit --redact --staged --verbose` | Hooks oficiales v2 canalizan `git diff --cached` a `betterleaks stdin --git-diff`; no hay acción oficial de GitHub, solo de terceros | Hook oficial |
| Evaluación previa en el portfolio [D] | `vc/tooling/evaluations/gitleaks.evidence.json` en el precursor, 8.30.1 como sombra | `betterleaks.evaluation.json`: `approved_with_exception` hasta 2026-12-30 por el PO de Blends; aplica al precursor | Ninguna |

[P] Recomendación del asistente, previa a la decisión: gitleaks 8.30.1 como compuerta, por ser la versión estable, MIT, sin envío de candidatos a terceros, con configuración descubierta en el repositorio y códigos de salida documentados; su deficiencia es que no publica firmas. Betterleaks tiene checksums firmados con Sigstore, validación apagada por defecto, reglas que gitleaks no tiene según el precursor y a las mismas personas detrás; lo que le falta para una adopción nueva es una versión 2 estable: la única estable es la 1.9.0, de la línea anterior, rc.1 ya fue superada por cinco candidatas, el CLI de v2 cambió respecto de gitleaks y la identidad de firma no está documentada por el proyecto. trufflehog se descarta como compuerta por su verificación externa por defecto, que contradice la regla de no enviar candidatos fuera sin autorización; puede servir como segunda herramienta de SEC-14 solo con `--no-verification`.

[U] **Decisión del usuario, 2026-11-02, en este chat: «Quiero usar betterleaks en lugar de gitleaks, ya lo veníamos usando en blends precursor y funciona OK».** El usuario es el responsable del portfolio por VCX-D034, así que la decisión tiene la autoridad que VCX-P7 exige; la recomendación anterior queda registrada como antecedente y no se repite. Versión: [P] 2.0.0-rc.1, la misma del precursor y del scan del 2026-11-02, porque es la única con procedimiento de verificación reproducido, hashes de darwin arm64 y linux x64 leídos de la release por dos vías independientes y experiencia de uso; adoptar rc.6 o esperar la 2.0.0 estable exigiría leer hashes nuevos y repetir la verificación. Esa fijación es una excepción propia de VCX, con revisión cuando Betterleaks publique su primera 2.x estable, registrada como [VCX-D037](../../decisions/README.md); no se hereda de la del PO de Blends.

La versión heredada, Betterleaks 2.0.0-rc.1, es una referencia reproducible: el precursor conserva el procedimiento de instalación verificada para darwin arm64 y linux x64, con SHA-256 fijados y la identidad de firma, y el scan del 2026-11-02 reutilizó el hash de darwin arm64. Es una release candidate con cinco candidatas posteriores y sin 2.0.0; ese es el costo de la decisión y queda como pendiente de revisión, no como objeción.

Ninguna decisión de este documento autoriza instalar. La instalación en la máquina y el workflow siguen requiriendo su propia autorización, §8.

## 3. Fase local interina: compuerta independiente de GitHub

### 3.1 Qué es y qué no es

[P] Un script de expresiones regulares, solo biblioteca estándar de Python 3.9, que analiza por separado el índice preparado, el árbol de trabajo rastreado y todos los blobs alcanzables del historial. Emite regla, ubicación y metadatos seguros; nunca el valor ni la línea. Es una **mitigación limitada**: reconoce once formatos conocidos y nada más. No equivale a un scanner dedicado y no se presenta como tal en ningún estado del inventario.

Ejecutar el script a mano no constituye una compuerta automática: es un procedimiento que una persona puede olvidar. Un hook local lo convierte en automático para ese clon, pero sigue siendo omitible con `--no-verify` y no existe en otros clones. La compuerta que no se omite está del lado del servidor, en la fase siguiente.

### 3.2 Alcance por modo

| Modo | Qué analiza | Qué queda fuera |
|---|---|---|
| `--staged` | Contenido del índice de cada ruta agregada, copiada, modificada o renombrada (`git diff --cached --diff-filter=ACMR`), leído con `git show :ruta`, no desde el disco | Archivos sin preparar; rutas borradas; cambios en `.gitignore` que afecten a futuros commits |
| `--worktree` | Archivos rastreados (`git ls-files`) leídos del disco | Archivos ignorados o sin seguimiento, por ejemplo los `.DS_Store` actuales; el contenido del índice si difiere del disco |
| `--history` | Todos los blobs alcanzables desde cualquier ref (`git rev-list --objects --all`), cada uno una sola vez, leídos con `git cat-file --batch` | Objetos no alcanzables (reflog expirado, stash eliminado); referencias no incluidas en `--all`; en `vcx` hoy, `--all` sí incluye `refs/backup` y `refs/codex`, lo cual es deseable para escanear y no para subir |
| Todos | — | Binarios: cualquier blob con un byte nulo en sus primeros 8 KiB se omite y se cuenta como `binary`; objetos mayores de 1 MiB se omiten y vuelven el análisis **parcial**; contenido comprimido o codificado dentro de texto; secretos con formatos que las once reglas no reconocen |

Nombres de archivo: las rutas se leen con `-z` y se tratan como bytes; la prueba 2 de la §3.6 usa un nombre con espacios y acentos.

### 3.3 Códigos de salida

| Código | Significado | Qué hace el procedimiento |
|---|---|---|
| 0 | Análisis completo sin hallazgos | Continuar |
| 1 | Al menos un hallazgo no exceptuado | Detener; tratar como posible exposición, §5.5 |
| 2 | Error operativo: no es un repositorio, `git` falló, objeto faltante, archivo de excepciones ilegible o malformado, modo ausente | Detener; no es un resultado limpio |
| 3 | Análisis incompleto sin hallazgos: al menos un objeto omitido por tamaño | Detener; revisar los objetos listados como `SKIPPED` por otro medio antes de continuar |

Un análisis parcial nunca devuelve 0. Un hallazgo tiene precedencia sobre la parcialidad: con hallazgos y objetos omitidos, devuelve 1 y lista ambos.

### 3.4 Reglas y excepciones

[P] Once reglas propuestas, nuevas porque las del 2026-11-01 no se conservaron: `github-token`, `github-fine-grained-pat`, `anthropic-api-key`, `openai-api-key`, `aws-access-key-id`, `google-api-key`, `slack-token`, `stripe-key`, `jwt`, `private-key-block` y `generic-assignment` (asignación entre comillas de `password`, `secret`, `api_key`, `access_token` o `auth_token` con al menos ocho caracteres). Son formatos públicos de cada proveedor; no se validan contra ningún servicio y nada sale de la máquina.

Excepciones: un archivo opcional, una por línea, con la forma `<sha256 del valor exacto> <regla> <justificación>`. Suprime solo ese valor con esa regla, en cualquier ruta; cada línea lleva su justificación y fecha de revisión. No hay exclusión por ruta, por carpeta ni por regla completa: si una regla produce ruido sistemático, se cambia la regla en el script y queda registrado en el diff. El archivo de excepciones viaja con el repositorio, así que todo cambio en él se revisa como un cambio de política de seguridad, no como un detalle; el precursor documenta la misma debilidad para `.betterleaksignore`.

### 3.5 Script

Etiqueta: **ejecutable verificado** el 2026-11-02 con las 18 comprobaciones de la §3.6 y sobre la raíz `vcx` (§3.7). Ubicación: [`scripts/secret-regex-check.py`](../../../scripts/secret-regex-check.py) en la raíz `vcx`, SHA-256 `c98969c940ab8c1484ffb5a4db3df8ccce3f32bf328c5388c1fd39e734a320ea`, agregado el 2026-11-02 con la autorización del usuario «Sí, agregar fase 1» en el chat con Claude; sin commit. Es una herramienta documental opcional del mismo tipo que `docs/exports/build_tooling_matrix_view.py`: no es una dependencia de ningún producto ni la ejecuta nada más que una persona o un hook de este clon. El hook no se activó: esa autorización no se pidió ni se dio.

```python
#!/usr/bin/env python3
"""Búsqueda interina de secretos por expresiones regulares para un repositorio Git.

Mitigación limitada: no reemplaza un scanner dedicado. Solo biblioteca estándar.
Uso:  python3 -I secret-regex-check.py --repo <ruta> (--staged | --worktree | --history) [--allow <archivo>]

Salida: una línea por hallazgo con regla, ubicación y metadatos seguros (longitud y
huella SHA-256 truncada del valor). Nunca imprime el valor ni la línea completa.
Códigos de salida: 0 limpio y completo; 1 hallazgos; 2 error operativo; 3 análisis
incompleto sin hallazgos (objetos omitidos por tamaño).
"""
import argparse
import hashlib
import re
import subprocess
import sys

MAX_BYTES = 1024 * 1024  # objetos mayores se omiten y el análisis se declara parcial
BINARY_PROBE = 8192

# Reglas propuestas (no son las del reporte del 2026-11-01, que no se conservaron).
RULES = [
    ("github-token", re.compile(rb"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{36,}\b")),
    ("github-fine-grained-pat", re.compile(rb"\bgithub_pat_[A-Za-z0-9_]{22,}\b")),
    ("anthropic-api-key", re.compile(rb"\bsk-ant-[A-Za-z0-9_-]{20,}")),
    ("openai-api-key", re.compile(rb"\bsk-(?!ant-)(?:proj-|svcacct-)?[A-Za-z0-9_-]{32,}")),
    ("aws-access-key-id", re.compile(rb"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
    ("google-api-key", re.compile(rb"\bAIza[0-9A-Za-z_-]{35}\b")),
    ("slack-token", re.compile(rb"\bxox[abprs]-[0-9A-Za-z-]{10,}\b")),
    ("stripe-key", re.compile(rb"\b[sr]k_(?:live|test)_[0-9A-Za-z]{16,}\b")),
    ("jwt", re.compile(rb"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b")),
    ("private-key-block", re.compile(rb"-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP )?PRIVATE KEY(?: BLOCK)?-----")),
    ("generic-assignment", re.compile(
        rb"(?i)\b(?:password|passwd|secret|api[_-]?key|access[_-]?token|auth[_-]?token)\s*[:=]\s*['\"][^'\"\s]{8,}['\"]")),
]


def die(msg, code=2):
    sys.stderr.write("error: %s\n" % msg)
    sys.exit(code)


def git(repo, *args, data=None):
    try:
        p = subprocess.run(["git", "-C", repo, *args], input=data, capture_output=True, check=False)
    except OSError as e:
        die("no se pudo ejecutar git: %s" % e)
    if p.returncode != 0:
        die("git %s falló: %s" % (" ".join(args[:2]), p.stderr.decode("utf-8", "replace").strip()))
    return p.stdout


def fingerprint(value):
    return hashlib.sha256(value).hexdigest()


def load_allow(path):
    allowed = {}
    if not path:
        return allowed
    try:
        with open(path, "rb") as f:
            for n, raw in enumerate(f, 1):
                line = raw.strip()
                if not line or line.startswith(b"#"):
                    continue
                parts = line.split(None, 2)
                if len(parts) < 3 or not re.fullmatch(rb"[0-9a-f]{64}", parts[0]):
                    die("%s:%d: formato esperado '<sha256> <regla> <justificación>'" % (path, n))
                allowed[(parts[0].decode(), parts[1].decode())] = parts[2].decode("utf-8", "replace")
    except OSError as e:
        die("no se pudo leer el archivo de excepciones: %s" % e)
    return allowed


def scan_blob(content, label, allowed, findings, suppressed):
    if b"\0" in content[:BINARY_PROBE]:
        return "binary"
    for rule, rx in RULES:
        for m in rx.finditer(content):
            value = m.group(0)
            fp = fingerprint(value)
            line_no = content.count(b"\n", 0, m.start()) + 1
            key = (fp, rule)
            if key in allowed:
                suppressed.append((rule, label, line_no, fp[:16]))
                continue
            findings.append((rule, label, line_no, len(value), fp[:16]))
    return "scanned"


def iter_staged(repo):
    out = git(repo, "diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z")
    for path in out.split(b"\0"):
        if path:
            yield path, git(repo, "show", b":" + path), "index:" + path.decode("utf-8", "replace")


def iter_worktree(repo):
    out = git(repo, "ls-files", "-z")
    full = git(repo, "rev-parse", "--show-toplevel").strip().decode("utf-8", "surrogateescape")
    for path in out.split(b"\0"):
        if not path:
            continue
        p = path.decode("utf-8", "surrogateescape")
        try:
            with open(full + "/" + p, "rb") as f:
                content = f.read(MAX_BYTES + 1)
        except OSError as e:
            die("no se pudo leer %r: %s" % (p, e))
        yield path, content, "worktree:" + path.decode("utf-8", "replace")


def iter_history(repo):
    # Todos los blobs alcanzables desde cualquier ref (ramas, tags, stashes, remotos).
    objs = git(repo, "rev-list", "--objects", "--all")
    blobs = {}
    for line in objs.splitlines():
        parts = line.split(b" ", 1)
        if len(parts) == 2:
            blobs.setdefault(parts[0], parts[1])
    if not blobs:
        return
    ids = list(blobs)
    out = git(repo, "cat-file", "--batch", data=b"\n".join(ids) + b"\n")
    pos = 0
    while pos < len(out):
        nl = out.index(b"\n", pos)
        header = out[pos:nl].split()
        pos = nl + 1
        if len(header) == 2 and header[1] == b"missing":
            die("objeto faltante %s" % header[0].decode())
        oid, otype, size = header[0], header[1], int(header[2])
        body = out[pos:pos + size]
        pos += size + 1
        if otype != b"blob":
            continue
        name = blobs[oid].decode("utf-8", "replace")
        yield blobs[oid], body, "blob:%s:%s" % (oid.decode()[:12], name)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repo", required=True, help="ruta explícita del repositorio")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--staged", action="store_true", help="índice preparado para commit")
    mode.add_argument("--worktree", action="store_true", help="archivos rastreados del árbol de trabajo")
    mode.add_argument("--history", action="store_true", help="todos los blobs alcanzables desde cualquier ref")
    ap.add_argument("--allow", help="archivo de excepciones: '<sha256> <regla> <justificación>' por línea")
    args = ap.parse_args()

    if git(args.repo, "rev-parse", "--is-inside-work-tree").strip() != b"true":
        die("%s no es un árbol de trabajo de Git" % args.repo)
    allowed = load_allow(args.allow)
    it = iter_staged(args.repo) if args.staged else iter_worktree(args.repo) if args.worktree else iter_history(args.repo)
    scope = "staged" if args.staged else "worktree" if args.worktree else "history"

    findings, suppressed, skipped = [], [], []
    scanned = binary = 0
    for _path, content, label in it:
        if len(content) > MAX_BYTES:
            skipped.append(label)
            continue
        if scan_blob(content, label, allowed, findings, suppressed) == "binary":
            binary += 1
        else:
            scanned += 1

    for rule, label, line_no, length, fp in sorted(findings):
        print("FINDING\t%s\t%s\tline=%d\tlen=%d\tfp=%s" % (rule, label, line_no, length, fp))
    for rule, label, line_no, fp in sorted(suppressed):
        print("ALLOWED\t%s\t%s\tline=%d\tfp=%s" % (rule, label, line_no, fp))
    for label in skipped:
        print("SKIPPED\tsize>%d\t%s" % (MAX_BYTES, label))
    print("SUMMARY\tscope=%s\tscanned=%d\tbinary=%d\tskipped=%d\tfindings=%d\tallowed=%d\trules=%d"
          % (scope, scanned, binary, len(skipped), len(findings), len(suppressed), len(RULES)))
    if findings:
        sys.exit(1)
    if skipped:
        sys.exit(3)
    sys.exit(0)


if __name__ == "__main__":
    main()
```

Decisiones de diseño que conviene conocer antes de cambiarlo: el índice se lee con `git show :ruta` y no del disco, para que `git commit -a` y `git add -p` analicen lo que de verdad se commitea; el historial se lee por blob único, así un mismo contenido en veinte commits se analiza una vez y se ubica por su `oid`, que `git log --all --find-object=<oid>` convierte en commits; `python3 -I` aísla al intérprete de módulos del directorio actual, como exige la convención del workspace para scripts que leen datos.

### 3.6 Comprobaciones con fixtures sintéticos

Etiqueta: **ejecutable verificado** el 2026-11-02, 18 de 18 comprobaciones en verde. Los valores con formato de token se generan al azar en cada corrida desde `/dev/urandom`; ninguno es una credencial. Ubicación: [`scripts/tests/secret-regex-check.fixtures.sh`](../../../scripts/tests/secret-regex-check.fixtures.sh), que localiza el script en el directorio padre; repetida desde esa ruta el 2026-11-02 a las 12:07 UTC con el mismo resultado.

```bash
#!/bin/bash
# Pruebas con fixtures sintéticos del script secret-regex-check.py.
# Los valores se generan al azar en cada corrida: no son credenciales reales.
set -u
S="$(cd "$(dirname "$0")/.." && pwd)/secret-regex-check.py"
W="$(mktemp -d "${TMPDIR:-/tmp}/srx-fixtures.XXXXXX")"
pass=0; fail=0
check() { # nombre, esperado, obtenido
  if [ "$2" = "$3" ]; then echo "PASS $1 (exit $3)"; pass=$((pass+1)); else echo "FAIL $1: esperado $2, obtenido $3"; fail=$((fail+1)); fi
}
rand() { LC_ALL=C tr -dc 'A-Za-z0-9' </dev/urandom | head -c "$1"; }
GH="ghp_$(rand 36)"; AK="AKIA$(LC_ALL=C tr -dc 'A-Z0-9' </dev/urandom | head -c 16)"
ANT="sk-ant-$(rand 40)"; SLK="xoxb-$(rand 24)"

cd "$W" && git init -q repo && cd repo && git config user.email f@x.test && git config user.name fx
echo "# documento limpio" > README.md && git add . && git commit -qm init

# 1. Repositorio limpio: 0 en los tres ámbitos.
python3 -I "$S" --repo . --worktree >/dev/null; check "limpio worktree" 0 $?
python3 -I "$S" --repo . --history  >/dev/null; check "limpio history" 0 $?
python3 -I "$S" --repo . --staged   >/dev/null; check "limpio staged (índice vacío)" 0 $?

# 2. Secreto preparado en un archivo con espacios y acentos: hallazgo, sin filtración.
printf 'token = "%s"\n' "$GH" > "config año ñ.txt"; git add "config año ñ.txt"
out=$(python3 -I "$S" --repo . --staged); rc=$?; check "staged hallazgo" 1 $rc
case "$out" in *"$GH"*) echo "FAIL filtración: el valor aparece en la salida"; fail=$((fail+1));; *) echo "PASS sin filtración staged"; pass=$((pass+1));; esac
echo "$out" | grep -q "^FINDING.github-token.index:config año ñ.txt" && { echo "PASS regla y ruta con espacios/acentos"; pass=$((pass+1)); } || { echo "FAIL formato: $out"; fail=$((fail+1)); }
# El secreto entra al historial y luego se borra: history lo sigue viendo, worktree no.
git commit -qm "agrega config"; git rm -q "config año ñ.txt"; git commit -qm "quita config"
python3 -I "$S" --repo . --worktree >/dev/null; check "worktree tras borrar" 0 $?
out=$(python3 -I "$S" --repo . --history); rc=$?; check "history conserva el hallazgo" 1 $rc
case "$out" in *"$GH"*) echo "FAIL filtración history"; fail=$((fail+1));; *) echo "PASS sin filtración history"; pass=$((pass+1));; esac

# 3. Varias reglas en el árbol de trabajo, en un archivo rastreado.
# La cabecera de clave privada se arma en tiempo de ejecución: escrita literal, este archivo
# dispararía la compuerta al commitearlo, y eximirla por huella eximiría toda cabecera igual.
{ echo "aws: $AK"; echo "anthropic: $ANT"; echo "slack: $SLK"; printf -- "-----BEGIN %s PRIVATE KEY-----\n" OPENSSH; echo "ZmFrZQ=="; printf -- "-----END %s PRIVATE KEY-----\n" OPENSSH; } > multi.txt
git add multi.txt
out=$(python3 -I "$S" --repo . --worktree); rc=$?; check "worktree multi" 1 $rc
n=$(echo "$out" | grep -c '^FINDING'); [ "$n" -eq 4 ] && { echo "PASS 4 hallazgos (aws, anthropic, slack, private-key)"; pass=$((pass+1)); } || { echo "FAIL hallazgos=$n"; echo "$out"; fail=$((fail+1)); }

# 4. Excepción por huella: suprime solo ese valor y esa regla.
fp=$(printf '%s' "$AK" | shasum -a 256 | cut -c1-64)
printf '%s aws-access-key-id ejemplo sintético de fixture, revisado 2026-11-02\n' "$fp" > allow.txt
out=$(python3 -I "$S" --repo . --worktree --allow allow.txt); rc=$?; check "allow reduce a 3" 1 $rc
echo "$out" | grep -q '^ALLOWED.aws-access-key-id' && { echo "PASS excepción registrada como ALLOWED"; pass=$((pass+1)); } || { echo "FAIL sin ALLOWED"; fail=$((fail+1)); }
printf 'no-es-sha regla x\n' > bad-allow.txt
python3 -I "$S" --repo . --worktree --allow bad-allow.txt >/dev/null 2>&1; check "allow malformado es error operativo" 2 $?
git rm -q --cached multi.txt; rm multi.txt

# 5. Archivo sobre el límite de tamaño: análisis parcial, nunca éxito.
head -c 1100000 /dev/zero | tr '\0' 'a' > big.txt; git add big.txt
python3 -I "$S" --repo . --staged >/dev/null; check "archivo grande => parcial (3)" 3 $?
git rm -q --cached big.txt; rm big.txt

# 6. Binario: omitido por diseño, resultado limpio.
printf 'PK\0\0%s' "$GH" > bin.dat; git add bin.dat
python3 -I "$S" --repo . --staged >/dev/null; check "binario omitido (declarado fuera de alcance)" 0 $?
git rm -q --cached bin.dat; rm bin.dat

# 7. Errores operativos: ruta que no es repositorio, flags inválidos.
python3 -I "$S" --repo "$W" --worktree >/dev/null 2>&1; check "no repo => 2" 2 $?
python3 -I "$S" --repo . >/dev/null 2>&1; rc=$?; [ $rc -ne 0 ] && { echo "PASS sin modo => error ($rc)"; pass=$((pass+1)); } || { echo "FAIL sin modo => 0"; fail=$((fail+1)); }

echo "RESULTADO: $pass pasaron, $fail fallaron"
rm -rf "$W"
[ $fail -eq 0 ]
```

[H] Al preparar el commit de estos archivos el 2026-11-02, el propio script bloqueó el índice con código 1: la cabecera literal de clave privada del fixture 3, en la prueba y en su copia embebida aquí, coincide con la regla `private-key-block`. No se resolvió con una excepción, porque la huella de esa cabecera es la misma en cualquier archivo y la excepción habría eximido toda clave OpenSSH; se resolvió armando la cabecera en tiempo de ejecución. Es la primera evidencia de que la compuerta actúa sobre lo que se commitea, y de que una excepción por valor puede abrir más de lo que parece.

La prueba 6 documenta un límite, no una virtud: un secreto dentro de un archivo binario pasa. El scanner dedicado de la §2 tampoco descomprime archivos; para binarios la defensa es no versionarlos sin revisión.

### 3.7 Resultado sobre la raíz `vcx`

[H] Corrido en solo lectura el 2026-11-02 a las 11:55 UTC, con `HEAD` en `4b01168`:

| Modo | Objetos analizados | Binarios omitidos | Omitidos por tamaño | Hallazgos | Código |
|---|---|---|---|---|---|
| `--worktree` | 117 | 0 | 0 | 0 | 0 |
| `--history` (112 commits alcanzables, incluidos `refs/backup` y `refs/codex`) | 288 | 4 (`.DS_Store` de los checkpoints) | 0 | 0 | 0 |
| `--staged` | 0 (índice vacío en esa sesión) | 0 | 0 | 0 | 0 |

[I] Con once reglas, ninguna coincidencia en el árbol rastreado ni en ningún blob alcanzable. Es consistente con el scan de Betterleaks del mismo día sobre `main`, que usa muchas más reglas pero solo cubre `main`. Ninguno de los dos afirma ausencia de secretos.

### 3.8 Procedimiento manual

Etiqueta: los dos comandos de escaneo son **ejecutables verificados** desde el repositorio el 2026-11-02 a las 12:07 UTC, con `HEAD` en `09bcced`: `--worktree` 117 objetos y `--history` 292 objetos, 4 binarios, 0 hallazgos, código 0 en ambos. El hook sigue **propuesto sin ejecutar**.

Antes de un commit en la raíz `vcx`, con el script en `scripts/`:

```bash
python3 -I scripts/secret-regex-check.py --repo . --staged
```

Antes del primer push de una rama, o de cualquier push de refs nuevos:

```bash
python3 -I scripts/secret-regex-check.py --repo . --history
```

Con código 1, 2 o 3 no se commitea ni se pushea; §5.5 define el tratamiento de un hallazgo. El historial se escanea completo y no solo el rango a subir, porque el costo es de medio segundo en `vcx` y porque `--all` alcanza los refs que un push por nombre no incluye: eso es lo que detecta un `refs/backup` con correo o un checkpoint con un archivo que nunca debió existir. El push mismo se hace siempre con refspec explícito, como hizo la publicación del 2026-11-02 (`main:main`), nunca con `--all` ni `--mirror`.

Hook opcional por clon, **propuesto sin ejecutar**; activa la comprobación del índice en este clon y solo en él:

```bash
git config core.hooksPath .githooks
```

con `.githooks/pre-commit`:

```bash
#!/bin/sh
# Compuerta interina de secretos de la raíz vcx. Falla cerrado: sin python3 no hay commit.
# Se omite con `git commit --no-verify`; esa omisión es visible en revisión, no invisible.
unset GIT_DIR GIT_WORK_TREE GIT_PREFIX
command -v python3 >/dev/null 2>&1 || { echo "✖ python3 no disponible: no se puede comprobar el índice" >&2; exit 1; }
exec python3 -I "$(git rev-parse --show-toplevel)/scripts/secret-regex-check.py" --repo "$(git rev-parse --show-toplevel)" --staged
```

Se deja `GIT_INDEX_FILE` sin desarmar a propósito: en `git commit -a` Git apunta esa variable al índice temporal que se va a commitear y `git show :ruta` debe leer ese índice. El precursor registró este hallazgo el 2026-09-12. La ruta de hooks se fija relativa, no absoluta, para no repetir el caso de SEC-08.

## 4. Fase de transición: repositorio remoto y CI

Configuración independiente por repositorio: cada repositorio de VCX lleva su propio workflow, su configuración y sus excepciones. No hay servicio central, no hay workflow reutilizable de la raíz y nada busca al precursor. Los bloques siguientes están escritos para `denispaiva/vcx` con Betterleaks 2.0.0-rc.1, el motor decidido por el usuario y la única versión con procedimiento de verificación reproducido y hashes leídos de la release por dos vías independientes; cambiar de versión cambia los hashes y la identidad del tag, no la estructura.

### 4.1 Instalación local reproducible, darwin arm64

Etiqueta: **ejecutable verificado** en esta máquina el 2026-11-02 a las 12:14 UTC, con autorización del usuario «Sí, instalar y activar»: `cosign` 3.1.4 instalado con Homebrew; `cosign verify-blob` devolvió «Verified OK» con la identidad indicada; los dos `shasum -c` dieron `OK`; `betterleaks version` imprime `2.0.0-rc.1`; binario en `~/.local/bin`, que no está en el `PATH` de los shells de esta máquina, por lo que el hook lo antepone. Es el procedimiento que el precursor documenta en `vc/docs/standards/secrets.md`, reproducido sin cambios de fondo. Procedencia: `checksums.txt` está firmado con Sigstore desde el workflow de release del proyecto; la identidad del certificado no está documentada por Betterleaks y se infiere de ese workflow, pero el precursor obtuvo «Verified OK» con ella el 2026-10-01. Integridad: el SHA-256 del tarball se comprueba contra el valor fijado aquí y contra la línea firmada; el valor de darwin arm64 coincide con el que el [scan del 2026-11-02](../reports/2026-11-02-vcx-secrets-scan.md) leyó de la release. Requiere `cosign`, hoy no instalado (`brew install cosign`); sin `cosign` el procedimiento no se degrada a «solo checksum»: se detiene. VCX no firma nada propio, porque no distribuye artefactos.

```bash
(
  set -euo pipefail   # cualquier verificación que falle aborta antes de instalar
  v=2.0.0-rc.1
  release=https://github.com/betterleaks/betterleaks/releases/download/v$v
  tarball=betterleaks_${v}_darwin_arm64.tar.gz
  command -v cosign >/dev/null || { echo "cosign no está instalado: no se verifica la procedencia, no se instala" >&2; exit 1; }
  cd "$(mktemp -d)"
  curl -sSL --fail -O "$release/$tarball" -O "$release/checksums.txt" -O "$release/checksums.txt.sigstore.json"
  # 1. Procedencia: checksums.txt firmado por el workflow de release del proyecto, en ese tag.
  cosign verify-blob checksums.txt --bundle checksums.txt.sigstore.json \
    --certificate-identity "https://github.com/betterleaks/betterleaks/.github/workflows/release.yml@refs/tags/v$v" \
    --certificate-oidc-issuer https://token.actions.githubusercontent.com
  # 2. Integridad: contra el hash fijado al adoptar y contra la línea firmada.
  echo "666b96714a4d4e01d4007030bdbfbea9579a356585c0d45b1dfead0faf47a380  $tarball" | shasum -a 256 -c -
  grep " $tarball\$" checksums.txt | shasum -a 256 -c -
  # 3. Recién aquí se extrae; la versión se comprueba antes de dejar el binario en PATH.
  tar -xzf "$tarball" betterleaks
  [ "$(./betterleaks version | head -n 1)" = "$v" ]
  mkdir -p ~/.local/bin
  install -m 0755 betterleaks ~/.local/bin/betterleaks
  echo "instalado betterleaks $v"
)
```

Homebrew ofrece Betterleaks 1.9.0, de la línea v1, que no entiende `--config`, `--ignore-file`, `--validate` ni `--analyze`; no sirve para esta compuerta. Por eso se instala la release fijada y el hook exige la versión exacta.

Configuración del repositorio, [`.betterleaks.toml`](../../../.betterleaks.toml) en la raíz de `vcx`, creada el 2026-11-02. v2 no la descubre sola: el hook y el workflow la pasan con `--config`, y su ausencia es un error, no un pase con defaults. A diferencia del precursor no se desactiva `generic-password`: el scan del 2026-11-02 con las reglas por defecto dio cero hallazgos en `vcx`, así que no hay falsos positivos que justificar todavía.

```toml
# Compuerta de secretos de la raíz vcx: Betterleaks 2.0.0-rc.1. Extiende las reglas por defecto.
# Las excepciones por valor van en .betterleaksignore con su huella y justificación; no se agregan
# allowlists por ruta ni se desactivan reglas sin registrar el motivo en este archivo.
title = "vcx — Betterleaks"

[extend]
useDefault = true
```

Hook [`.githooks/pre-commit`](../../../.githooks/pre-commit) con el motor, activo en este clon desde el 2026-11-02 con `git config core.hooksPath .githooks`, ruta relativa; reemplaza al interino de la §3.8, que queda como segunda herramienta para SEC-14. Probado en un repositorio desechable con el mismo hook y configuración: commit limpio pasa; commit con un token sintético de GitHub bloqueado por la rama 3, salida redactada sin el valor; `git commit -a` con el valor en un archivo rastreado bloqueado; sin `.betterleaks.toml` bloqueado por la comprobación previa. En `vcx`, el hook sobre el índice con la configuración y el hook preparados dio «no leaks found», `config_hash` `2b8e4814…`, el mismo del scan del 2026-11-02. Falla cerrado: sin binario, con otra versión o sin configuración no hay commit. `--validate=false --analyze=false` explícitos, porque en v2 la validación también se enciende por variable de entorno y enviaría los candidatos a las API de sus proveedores. Con `--exit-code 3`, los hallazgos salen con 3 y cualquier error con 1; el flag está documentado («`--exit-code` changes that»), y la distinción se comprueba en la primera ejecución.

```bash
#!/bin/sh
# Compuerta de secretos de la raíz vcx: Betterleaks 2.0.0-rc.1 sobre el índice. Falla cerrado.
# Se deja GIT_INDEX_FILE: en `git commit -a` apunta al índice temporal que se commitea.
# Diseño y procedimiento: docs/superpowers/specs/2026-11-02-secret-detection-strategy-design.md §4.1.
unset GIT_DIR GIT_WORK_TREE GIT_PREFIX
PATH="$HOME/.local/bin:$PATH"   # la release verificada se instala ahí; los hooks no cargan el perfil del shell
ROOT="$(git rev-parse --show-toplevel)"
V=2.0.0-rc.1
command -v betterleaks >/dev/null 2>&1 || { echo "✖ betterleaks no está instalado; ver docs/superpowers/specs/2026-11-02-secret-detection-strategy-design.md §4.1" >&2; exit 1; }
[ "$(betterleaks version 2>/dev/null | head -n 1)" = "$V" ] || { echo "✖ betterleaks no es la versión $V fijada por la compuerta" >&2; exit 1; }
[ -f "$ROOT/.betterleaks.toml" ] || { echo "✖ falta .betterleaks.toml en la raíz: v2 no lo descubre solo" >&2; exit 1; }
IGNORE=""
[ -f "$ROOT/.betterleaksignore" ] && IGNORE="--ignore-file $ROOT/.betterleaksignore"
# shellcheck disable=SC2086
betterleaks git "$ROOT" --staged --config "$ROOT/.betterleaks.toml" $IGNORE \
  --redact --no-banner --validate=false --analyze=false --exit-code 3
rc=$?
case $rc in
  0) exit 0 ;;
  3) echo "✖ Commit bloqueado: posible secreto en el índice. Quitarlo, rotarlo si ya se usó; falso positivo: huella en .betterleaksignore con justificación." >&2; exit 1 ;;
  *) echo "✖ Commit bloqueado: betterleaks terminó con error $rc, no con un resultado limpio." >&2; exit 1 ;;
esac
```

### 4.2 Workflow de CI

Etiqueta: **propuesto sin ejecutar**. Archivo creado el 2026-11-02 en [`.github/workflows/secrets.yml`](../../../.github/workflows/secrets.yml), idéntico a este bloque y con YAML válido; no corre hasta que un push lo lleve a `denispaiva/vcx`, y su primer run es la evidencia que SEC-23 exige. Decisiones: dispara en `push` a cualquier rama y en `pull_request`, nunca en `pull_request_target`, porque la documentación advierte que ese evento puede dar a código no confiable acceso a permisos de escritura o secretos; `permissions: contents: read` e `id-token` sin conceder, porque verificar una firma ajena no requiere identidad propia; sin secretos, porque el escaneo no los necesita; acciones fijadas por SHA completo de commit, verificado hoy contra el tag `v4.1.2` de `cosign-installer` y `v7.0.1` de `actions/checkout`; `fetch-depth: 0` para que el historial completo esté disponible. El escaneo cubre todo el historial alcanzable del checkout en cada ejecución: en `vcx` cuesta menos de un segundo. Las contribuciones desde forks corren con el token de solo lectura y sin secretos; GitHub exige aprobación manual para contribuyentes nuevos según la configuración medida.

```yaml
name: secrets

on:
  push:
  pull_request:

permissions:
  contents: read

jobs:
  scan:
    name: secrets
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - name: Checkout con historial completo
        uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1
        with:
          fetch-depth: 0
          persist-credentials: false

      - name: Instalar cosign
        uses: sigstore/cosign-installer@6f9f17788090df1f26f669e9d70d6ae9567deba6 # v4.1.2

      - name: Descargar y verificar Betterleaks 2.0.0-rc.1 antes de extraer
        run: |
          set -euo pipefail
          v=2.0.0-rc.1
          release=https://github.com/betterleaks/betterleaks/releases/download/v$v
          tarball=betterleaks_${v}_linux_x64.tar.gz
          curl -sSL --fail -o "$tarball" "$release/$tarball"
          curl -sSL --fail -o checksums.txt "$release/checksums.txt"
          curl -sSL --fail -o checksums.txt.sigstore.json "$release/checksums.txt.sigstore.json"
          # Procedencia: checksums.txt firmado por el workflow de release del proyecto en el tag exacto.
          # La identidad no está documentada por Betterleaks; es la que el precursor verificó el 2026-10-01.
          cosign verify-blob checksums.txt --bundle checksums.txt.sigstore.json \
            --certificate-identity "https://github.com/betterleaks/betterleaks/.github/workflows/release.yml@refs/tags/v$v" \
            --certificate-oidc-issuer https://token.actions.githubusercontent.com
          # Integridad: hash fijado al adoptar, igual al que el precursor fijó el 2026-10-01, y línea firmada.
          echo "ccbbf68d0a403af44ed5d118c495d20c06bbf39d09129d2ae733d69aa9242404  $tarball" | sha256sum -c -
          grep " $tarball\$" checksums.txt | sha256sum -c -
          mkdir -p "$RUNNER_TEMP/bin"
          tar -xzf "$tarball" -C "$RUNNER_TEMP/bin" betterleaks
          [ "$("$RUNNER_TEMP/bin/betterleaks" version | head -n 1)" = "$v" ]
          echo "$RUNNER_TEMP/bin" >> "$GITHUB_PATH"

      - name: Comprobar configuración
        run: |
          set -euo pipefail
          [ -f .betterleaks.toml ] || { echo "::error::falta .betterleaks.toml: la compuerta no escanea con defaults"; exit 1; }

      - name: Escaneo de secretos sobre el historial del checkout
        run: |
          set +e
          args="--config .betterleaks.toml --redact --no-banner --validate=false --analyze=false --exit-code 3"
          [ -f .betterleaksignore ] && args="$args --ignore-file .betterleaksignore"
          # shellcheck disable=SC2086
          betterleaks git . $args
          rc=$?
          set -e
          case $rc in
            0) echo "sin hallazgos; revisión $GITHUB_SHA" ;;
            3) echo "::error::hallazgo de secretos en la revisión $GITHUB_SHA; ver el log redactado"; exit 1 ;;
            *) echo "::error::betterleaks terminó con error $rc: fallo operativo o de configuración, no un resultado limpio"; exit 1 ;;
          esac
```

Qué distingue el workflow y cómo responde cada caso:

| Caso | Dónde se detecta | Resultado |
|---|---|---|
| Hallazgo | Paso de escaneo, código 3 | Job rojo con `::error::`; nunca se reintenta con otro motor |
| Error de instalación o integridad | Paso de descarga: `curl --fail`, `cosign verify-blob`, `sha256sum -c`, comprobación de versión | Job rojo antes de extraer o ejecutar nada |
| Error de configuración | Paso de comprobación: falta `.betterleaks.toml`; campo TOML desconocido o flag inválido hacen fallar la carga con código distinto de 0 y de 3 | Job rojo con mensaje explícito; no se escanea con defaults |
| Fallo operativo del scanner | Código 1 u otro en el paso de escaneo | Job rojo; el estado inconcluso impide integrar cuando el check sea obligatorio |

El log redactado del run es la evidencia; no se sube ningún reporte como artefacto. Una investigación que necesite el reporte completo lo regenera en local con `--output`.

### 4.3 Selección de motor y recuperación

[D] El contrato del precursor, confirmado en su fuente: en local, `BLENDS_SECRETS_GATE=betterleaks|gitleaks` elige la compuerta, cualquier otro valor falla cerrado y la otra herramienta corre en sombra solo si está instalada; en CI, la variable de repositorio `SECRETS_GATE` con valor `gitleaks` invierte los papeles mediante `continue-on-error` en cada paso, y cualquier otro valor deja a Betterleaks como compuerta. Un hallazgo de la sombra nunca aprueba ni bloquea; un hallazgo de la compuerta siempre bloquea. El cambio es manual y trazable: una variable que alguien fija con `gh variable set`. No es un fallback automático.

[P] Para VCX, la alternativa más simple: **un solo motor, sin sombra y sin interruptor.** El cambio de motor o de versión es un PR que modifica el workflow y el hook, con los hashes y la identidad nuevos en el diff y la decisión registrada; eso es más trazable que una variable de repositorio, que no deja rastro en el historial. Un fallback automático no se propone: exigiría demostrar equivalencia de cobertura entre dos motores, preservar los errores del primero y probar las dos ramas en cada cambio, y el caso que debería resolver, «el motor falla», ya tiene respuesta correcta, bloquear. Si en el futuro VCX quiere una segunda opinión, la forma del precursor, sombra que solo avisa, es la adecuada: se agrega como paso separado con `continue-on-error: true` y sin capacidad de aprobar. gitleaks 8.30.1, estable y ya evaluado como sombra en el precursor, es el candidato natural para ese papel.

### 4.4 Check obligatorio

Etiqueta: **plantilla incompleta**. Solo cuando exista autoridad para restringir `main`; hoy el único autor es el responsable del portfolio y no hay protección alguna. Rulesets están disponibles sin costo en repositorios públicos. El contexto del check es el nombre del job, `secrets`. La plantilla deja sin fijar si `main` admite push directo, que es una decisión de gobierno:

```json
{
  "name": "main-secrets-gate",
  "target": "branch",
  "enforcement": "active",
  "conditions": { "ref_name": { "include": ["refs/heads/main"], "exclude": [] } },
  "rules": [
    { "type": "deletion" },
    { "type": "non_fast_forward" },
    { "type": "required_status_checks",
      "parameters": { "strict_required_status_checks_policy": true,
                      "required_status_checks": [ { "context": "secrets" } ] } }
  ]
}
```

Se aplicaría con `gh api -X POST repos/denispaiva/vcx/rulesets --input <archivo>` y se comprobaría con `GET .../rulesets`. Un ruleset que exige un check solo bloquea el merge de PR y los pushes que no lo cumplan; no retroactúa sobre lo ya integrado.

### 4.5 Cobertura

| Evento | Cubierto por | Observación |
|---|---|---|
| Commit en local | Hook de la §4.1, o interino de la §3.8 | Omisible con `--no-verify`; por clon |
| Push | Push protection de GitHub para patrones de proveedores soportados; workflow en `push` para el resto | Push protection actúa antes de que el contenido llegue; el workflow, después |
| Pull request | Workflow en `pull_request` sobre el historial del merge | Sin secretos, token de solo lectura |
| Historial previo a publicación | Scan de Betterleaks del 2026-11-02 sobre `4b01168`; búsqueda de la §3.7 sobre todos los refs | Cada futura publicación de un producto repite el scan sobre el SHA exportado, con dos herramientas, según VCX-D032 |
| Refs locales no publicados | Solo la §3 con `--all` | Ningún control del servidor los ve, porque no se suben |

## 5. Fase de controles, evidencia y gobierno

### 5.1 Correspondencia con el inventario

Cada resultado se relaciona con el control y el repositorio correctos. No se reutiliza ningún ID para otro alcance y ningún estado cambia por redactar este documento.

| Control | Repositorio | Qué aporta este diseño | Estado hoy | Estado al que podría pasar y con qué evidencia |
|---|---|---|---|---|
| SEC-03, compuerta de secretos previa al commit en la raíz | `vcx` local | §3: script, procedimiento y hook opcional; §2: scanner dedicado como objetivo | Ausente | `Diseñado` por este documento, si se acepta; `Implementado` cuando el script y el hook existan en el clon; `Verificado` cuando una prueba con un valor sintético bloquee un commit en ese clon, con fecha y SHA del script |
| SEC-07, compuerta de secretos en CI | Precursor `denispaiva/blends` | Nada. Se leyó como referencia; no se modifica desde VCX | Implementado, no comprobado | Sin cambio |
| SEC-08, compuerta local del precursor | Precursor, checkout `../blends` | Nada. Su causa, `core.hooksPath` absoluto, informa el diseño del hook de la §3.8 | Inactivo | Sin cambio; la corrección es del PO de Blends |
| SEC-09, secret scanning, push protection y Dependabot | Precursor `denispaiva/blends` | Nada. La medición de hoy fue sobre `denispaiva/vcx`, no sobre el precursor | No comprobado | Sin cambio |
| **SEC-22** [P], funciones nativas de GitHub en `denispaiva/vcx` | `denispaiva/vcx` | Medición del 2026-11-02 11:55 UTC, §1.1 | Fila nueva propuesta: `Implementado` para secret scanning y push protection, cada una por separado; `Ausente` para patrones no de proveedor, chequeos de validez, alertas de vulnerabilidades y actualizaciones de seguridad de Dependabot | `Verificado` solo por función y con evidencia individual: un push de prueba bloqueado para push protection, una alerta observada para secret scanning. La cobertura parcial se conserva como tal |
| **SEC-23** [P], compuerta de secretos en CI de `denispaiva/vcx` | `denispaiva/vcx` | §4: workflow propuesto | Fila nueva propuesta: `Diseñado` | `Implementado` al existir el workflow en `main`; `Verificado` con un run identificado, sobre un SHA, con su resultado y su código de salida |
| **SEC-24** [P], check obligatorio de secretos en `main` de `denispaiva/vcx` | `denispaiva/vcx` | §4.4: ruleset propuesto | Fila nueva propuesta: `Ausente`; hoy no hay protección de rama ni rulesets | `Implementado` cuando la API devuelva el ruleset; `Verificado` cuando un PR con un run rojo no pueda integrarse |

CI no reemplaza push protection: la primera corre después de que el contenido llegó al remoto y bloquea la integración; la segunda actúa en el push y solo para los patrones que GitHub reconoce. Son controles distintos con filas distintas.

Fragmentos propuestos para el inventario, condicionados a que el responsable del portfolio acepte este diseño. El encabezado de cada fila usa los estados que el inventario define.

```markdown
| SEC-22 | Secret scanning y push protection nativos en `denispaiva/vcx` | Implementado por función: secret scanning y push protection enabled; patrones no de proveedor, chequeos de validez, alertas de vulnerabilidades y Dependabot security updates disabled | [H] `GET /repos/denispaiva/vcx` `security_and_analysis` y `GET .../vulnerability-alerts` (404), 2026-11-02 11:55 UTC. Conclusión: reportado como activo; ningún bloqueo ni alerta observados | 27001 A.8.8, A.8.12; SOC 2 CC7.1 | Pasar a Verificado por función con un push de prueba bloqueado y una alerta observada; decidir si se activan patrones no de proveedor y alertas de Dependabot |
| SEC-23 | Compuerta de secretos en CI de `denispaiva/vcx` | Diseñado | [D] [estrategia de detección de secretos](../superpowers/specs/2026-11-02-secret-detection-strategy-design.md), §4 | 27001 A.8.12, A.8.28; SOC 2 CC6.7, CC8.1 | Autorizar el workflow; primer run sobre un SHA identificado |
| SEC-24 | Check obligatorio de secretos en `main` de `denispaiva/vcx` | Ausente | [H] sin protección de rama (404) ni rulesets (`[]`), 2026-11-02 11:55 UTC | 27001 A.8.32; SOC 2 CC8.1 | Crear el ruleset cuando exista autoridad; depende de SEC-23 |
```

Y para SEC-03, un reemplazo de la columna «Pendiente» cuando el diseño se acepte: «Diseño en la [estrategia de detección de secretos](../superpowers/specs/2026-11-02-secret-detection-strategy-design.md); decidir motor e instalación; mientras tanto, script interino de la §3».

### 5.2 Evidencia mínima por escaneo

| Dato | Ejemplo con el resultado de la §3.7 |
|---|---|
| Repositorio y revisión analizada | `vcx` local, `HEAD` `4b01168`; en historial, los 112 commits alcanzables por `--all` |
| Fecha y ámbito | 2026-11-02 11:55 UTC; `--worktree`, `--history`, `--staged` |
| Scanner, versión y digest de configuración | `secret-regex-check.py`, SHA-256 `c98969c9…a320ea`; sin archivo de excepciones |
| Resultado y código de salida | 0 hallazgos; código 0 en los tres modos; 4 binarios omitidos en historial, 0 por tamaño |
| Identificador del run | No aplica en local; en CI, el ID del run y su URL |
| Excepciones vigentes y límites de cobertura | Ninguna excepción; límites de la §3.2 |

### 5.3 Ubicación y retención

[P] Los resúmenes seguros, como la tabla anterior, viven en `docs/superpowers/reports/` de la raíz `vcx`, que ya aloja el [scan del 2026-11-02](../reports/2026-11-02-vcx-secrets-scan.md); un reporte por escaneo que respalde una transición, fechado y con SHA. No se versionan salidas crudas: ni líneas de contexto, ni valores, ni `.betterleaksignore` con huellas de secretos reales. Las salidas completas con huellas, si hacen falta para una investigación, se conservan fuera del repositorio, en una carpeta local del responsable del portfolio con acceso restringido, el tiempo que dure la investigación, y se citan por fecha y hash desde el reporte. En CI, el log del run es la evidencia y queda bajo la retención de GitHub para repositorios públicos; el workflow usa `--redact` para que ese log tampoco contenga valores.

`brix/tooling/` no aloja evidencia operativa de la raíz: según VCX-D035 guarda evaluaciones de herramientas con su procedencia, que es otro dato. Si Brix o Cellar adoptan la misma compuerta, cada repositorio guarda su propia evidencia en su propio contexto.

### 5.4 Responsables propuestos

| Rol | Quién | Qué decide o hace |
|---|---|---|
| A, autoridad | Responsable del portfolio, `denispaiva` por VCX-D034 | Motor, instalación en la máquina, workflow en `main`, ruleset, activación de funciones de GitHub, excepciones |
| R, mantenimiento | Quien prepare cada transición del [mapa](../../architecture/repository-map.md#secuencia-acordada-para-preservar-y-versionar) | Correr el escaneo, escribir el reporte, actualizar las filas del inventario que la puerta exija |
| Precursor | PO de Blends | SEC-07, SEC-08 y SEC-09 siguen bajo su gobierno; nada de este documento los toca |

### 5.5 Respuesta ante hallazgos

Aplica a cualquier modo, local o CI, con el script interino o con el scanner dedicado.

1. **Detener** el commit, el push o la publicación en curso. Si el hallazgo apareció en CI, el contenido ya está en el remoto: tratarlo como expuesto a todo el que tenga acceso al repositorio, que en `denispaiva/vcx` es cualquiera.
2. **Evaluar la exposición**: qué credencial es, a qué da acceso, desde cuándo está en el historial (`git log --all --find-object=<oid>`) y en qué remotos existe ese commit.
3. **Revocar o rotar** en el proveedor cuando sea una credencial real. Es el único paso que cierra la exposición; borrar el texto no invalida la credencial. Un falso positivo se documenta con su huella y justificación en el archivo de excepciones, nunca desactivando la regla ni el hook.
4. **Reescribir el historial solo con decisión explícita**, no por inferencia. En `vcx` ya pasó una vez con alcance autorizado y una tabla de correspondencia de SHA; cualquier repetición exige la misma autoridad y, una vez publicado, se asume que el valor es público aunque se reescriba.
5. **Volver a comprobar**: repetir el escaneo sobre el SHA resultante y registrar el reporte de la §5.2 con la resolución del hallazgo.

## 6. Plan en tres fases

| Fase | Entregables | Responsable propuesto | Dependencias | Criterio observable de salida |
|---|---|---|---|---|
| **1. Compuerta local interina** | Script en `scripts/`, pruebas en `scripts/tests/`, procedimiento de la §3.8, hook opcional | R: quien prepare el siguiente push; A: responsable del portfolio | Archivos agregados el 2026-11-02, sin commit; falta decidir el hook | Las 18 comprobaciones en verde desde el repositorio, cumplido el 2026-11-02; `--history` en 0 sobre el SHA a subir, cumplido sobre `09bcced`; reporte en `docs/superpowers/reports/`, pendiente |
| **2. Motor dedicado, local y CI** | Decisión de motor tomada el 2026-11-02 (Betterleaks); versión y excepción registradas en el registro de decisiones; `cosign` y Betterleaks instalados con verificación; `.github/workflows/secrets.yml`; `.betterleaks.toml`; ruleset cuando haya autoridad | A: responsable del portfolio | Instalación y hook hechos el 2026-11-02 en este clon; faltan el registro de la decisión, el commit de la configuración y el hook, y la autoridad para crear el workflow | Un commit con un valor sintético bloqueado en local; un run de CI identificado, rojo con el fixture y verde sin él; ruleset que exige el check, comprobado por API |
| **3. Controles y evidencia** | Filas SEC-22 a SEC-24 en el inventario; SEC-03 actualizado; reportes por escaneo; retiro o reubicación del script interino como segunda herramienta de SEC-14 | R: quien prepare la transición; A: responsable del portfolio | Fases 1 y 2 | Cada fila con estado, evidencia fechada y SHA; ninguna fila en Verificado sin la prueba que su definición exige |

Orden: la fase 1 puede ejecutarse hoy con una autorización de dos archivos. La fase 2 está desbloqueada del lado de GitHub desde las 11:54 UTC y bloqueada del lado local por la decisión de motor. La fase 3 cierra cada una con evidencia, no con redacción.

## 7. Matriz de verificación

| Caso | Fase | Cómo se prueba | Resultado esperado | Estado |
|---|---|---|---|---|
| Repositorio limpio | 1 | Fixture 1 | 0 en los tres modos | Verificado 2026-11-02 |
| Secreto en el índice, ruta con espacios y acentos | 1 | Fixture 2 | 1; salida sin el valor; regla y ruta correctas | Verificado |
| Secreto borrado del árbol pero presente en historial | 1 | Fixture 2 | `--worktree` 0, `--history` 1 | Verificado |
| Cuatro proveedores en un archivo | 1 | Fixture 3 | 1 con cuatro `FINDING` | Verificado |
| Excepción por huella y regla | 1 | Fixture 4 | 1 con tres `FINDING` y un `ALLOWED` | Verificado |
| Archivo de excepciones malformado | 1 | Fixture 4 | 2 | Verificado |
| Objeto sobre 1 MiB | 1 | Fixture 5 | 3, nunca 0 | Verificado |
| Binario con secreto | 1 | Fixture 6 | 0, límite declarado | Verificado |
| Ruta que no es repositorio; sin modo | 1 | Fixture 7 | 2 | Verificado |
| Hook bloquea `git commit -a` con secreto no preparado | 2 | Commit en un clon desechable con el hook de Betterleaks activo | Commit rechazado con código 1 | Verificado 2026-11-02 con el hook de la §4.1; no probado con el interino |
| Scanner dedicado bloquea un valor sintético en local | 2 | Token sintético de GitHub preparado en un clon desechable, hook activo | Betterleaks sale con 3, el hook con 1, salida redactada | Verificado 2026-11-02 |
| CI rojo con fixture en un PR; verde sin él | 2 | Dos PR de prueba desde una rama del propio repositorio | Run rojo y run verde identificados | Propuesto sin ejecutar |
| Verificación de integridad falla | 2 | Alterar un byte del tarball descargado en un run de prueba | El paso de verificación falla antes de extraer; el job no pasa al escaneo | Propuesto sin ejecutar |
| Error de configuración | 2 | Quitar el archivo de configuración del motor | El job o el hook fallan con mensaje explícito; no se escanea con defaults | Verificado 2026-11-02 en local; en CI, propuesto sin ejecutar |
| Fallo operativo del scanner | 2 | Binario incorrecto para la plataforma | El job falla; nunca pasa a verde por ausencia de hallazgos | Propuesto sin ejecutar |
| Push protection bloquea un push | 3 | Push de un valor sintético con formato de proveedor soportado a una rama de prueba | Push rechazado por GitHub con referencia al patrón | Propuesto sin ejecutar; requiere autoridad por ser un push a un repositorio público |
| Check obligatorio impide integrar | 3 | PR con run rojo | Botón de merge bloqueado; API lo confirma | Propuesto sin ejecutar |

## 8. Pendientes que requieren autoridad o evidencia adicional

1. **Decisión de motor registrada** como [VCX-D037](../../decisions/README.md) el 2026-11-02: Betterleaks, 2.0.0-rc.1 con excepción propia de VCX y revisión al publicarse la primera 2.x estable o antes del 2026-12-30.
2. **Commit de `scripts/secret-regex-check.py`, su prueba y este documento**, y autorización para activar el hook de la §3.8 en este clon. Los archivos ya están en el árbol de trabajo desde el 2026-11-02.
3. **Instalación hecha el 2026-11-02** de `cosign` 3.1.4 y Betterleaks 2.0.0-rc.1 en esta máquina, con firma y hashes verificados; `.betterleaks.toml` y `.githooks/pre-commit` entraron al historial en `b3c0bb5`, un commit de otra sesión sobre el tablero del portfolio que arrastró los archivos preparados en el índice compartido; la procedencia correcta es esta estrategia, y el mensaje de ese commit no la menciona. Se registra como deuda de trazabilidad, sin reescribir historia. Falta repetir la instalación en cualquier otro clon o máquina.
4. **Autorización para el workflow en `main` de `denispaiva/vcx`** y, con él, la primera ejecución de Actions en un repositorio de VCX. Sin costo en runners estándar para repositorios públicos según VCX-D032, condición que conviene volver a leer en la documentación de GitHub al activarlo.
5. **Ruleset con check obligatorio**: autoridad y decisión de si `main` admite push directo mientras el único autor es el responsable del portfolio.
6. **Funciones de GitHub apagadas**: decidir si se activan patrones no de proveedor, alertas de vulnerabilidades y actualizaciones de seguridad de Dependabot en `denispaiva/vcx`. Hoy sin dependencias ejecutables, su valor es bajo; se registra para que la cobertura parcial de SEC-22 no se lea como completa.
7. **`.gitignore` para la raíz**, al menos para `.DS_Store`: no es un control de secretos, pero evita que instantáneas de herramientas y archivos del sistema entren al historial.
8. **`refs/backup/main-pre-noreply` y `refs/codex/*`**: decidir si se conservan, por cuánto tiempo y bajo qué regla de no publicación. Mientras existan, todo push se hace por refspec explícito.
9. **Evidencia de verificación del precursor** (SEC-07) sigue pendiente de un run identificado; no es tarea de VCX, se anota para no confundir «implementado» con «verificado».
10. **Revalidación de este documento** si cambia la visibilidad del repositorio, el motor, la versión o las condiciones de uso de GitHub Actions o de las funciones de seguridad.

## Fuentes

- [Inventario de controles](../../architecture/security-controls-inventory.md), [topología](../../architecture/github-topology.md), [mapa](../../architecture/repository-map.md), [diseño de visibilidad](2026-11-01-public-visibility-design.md), [registro de decisiones](../../decisions/README.md), [política FinOps](../../../finops-policy.md).
- [Revisión del historial](../reports/2026-11-01-vcx-public-history-review.md), [reescritura del correo](../reports/2026-11-01-vcx-noreply-rewrite.md), [scan de Betterleaks](../reports/2026-11-02-vcx-secrets-scan.md).
- Precursor, solo lectura, revisión `f86a2a7`: `.githooks/pre-commit`, `.githooks/pre-push`, `.github/workflows/ci-node.yml`, `.betterleaks.toml`, `.betterleaksignore`, `vc/docs/standards/secrets.md`, `vc/tooling/evaluations/betterleaks.evaluation.json`.
- Documentación oficial consultada el 2026-11-02, enlazada en las §2.2 y §4.
