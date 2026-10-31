# {{cellar_name}}

Plantilla documental; reemplazar este párrafo al instanciar. Resolver cada marcador con valores propios, indicar explícitamente lo que no aplica y comprobar referencias desde el destino. Los campos son una guía documental, no un esquema de máquina implementado. Las rutas pueden ser referencias relativas o ubicaciones externas declaradas según el almacenamiento elegido.

| Campo | Valor por completar | Significado |
|---|---|---|
| `cellarId` | `{{cellar_id}}` | Identidad estable de esta instancia |
| `owner` | `{{owner}}` | Propietario del portfolio |
| `custodian` | `{{custodian}}` | Responsable de custodia y recuperación |
| `purpose` | {{purpose}} | Propósito y límites del portfolio |
| `team` | {{team}} | Participantes y referencias a su autoridad |
| `initiativeIndexRef` | `{{initiative_index_ref}}` | Fuente única que identifica y localiza las iniciativas |
| `adoptedVersionsRef` | `{{adopted_versions_ref}}` | Versiones de productos y formatos efectivamente adoptadas |
| `policyProfileRef` | `{{policy_profile_ref}}` | Fuente y versión del perfil de gobierno adoptado |
| `configurationRef` | `{{configuration_ref}}` | Parámetros particulares autorizados |
| `portfolioDecisionsRef` | `{{portfolio_decisions_ref}}` | Decisiones transversales del portfolio |
| `storageRefs` | `{{storage_refs}}` | Fuentes de estado, incluidas ramas u otros servicios |
| `recoveryRef` | `{{recovery_ref}}` | Respaldo, restauración, integridad y evidencia de recuperación |
| `accessPolicyRef` | `{{access_policy_ref}}` | Autoridad y permisos de esta instancia |

## Iniciativas y memoria

Cada idea o proyecto tiene misión, visión, alcance y una fuente propia de estado. El índice referencia esas fuentes, sin copiarlas. Las decisiones y evidencias transversales pertenecen al portfolio; las específicas se conservan con su iniciativa.

Para incorporar una iniciativa, usar la plantilla correspondiente del producto Cellar adoptado. Registrar su ubicación canónica y sus dependencias; no asumir que copiar su código es necesario para gobernarla.

## Comprobación de preparación

Antes de declarar esta instancia lista: resolver los campos, verificar los destinos de referencia y designar la autoridad de acceso. Registrar el almacenamiento canónico de cada dato y cómo se recupera. No incluir credenciales ni representar locks de procesos como evidencia durable.

Si un producto o formato aún no tiene una versión adoptable, registrar ese estado en lugar de inventar una versión o afirmar que existe una integración funcional.
