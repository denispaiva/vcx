# Arquitectura de referencia: Teyst como app nativa con la web integrada

Fecha: 2026-11-02. Estado: **propuesta del asistente**, sin ratificar; corregida el mismo día tras una revisión independiente (ver «Revisión y correcciones»). Autoridad: encargo de la sesión de assessment del scaffolding de VCX del 2026-11-02, derivado de pedidos del usuario en ese chat. Autoriza análisis y redacción. No autoriza instalar paquetes, aprovisionar cuentas o recursos, cambiar IAM o billing, ejecutar builds, publicar en tiendas, escribir en `../blends` ni commitear. Insumo previsto: el perfil de stack nativo del scaffolding de VCX, que se especifica en la sesión de origen.

Etiquetas: [U] dicho por el usuario; [H] hecho medido el 2026-11-02 en solo lectura sobre el precursor o leído en documentación oficial enlazada; [I] interpretación o inferencia; [P] propuesta.

Estructura: los siete puntos de la [capacidad de arquitectura de referencia](../../../brix/docs/reference-architecture.md#modelo-de-salida-propuesto) de Brix (secciones 1 a 7), seguidos de las decisiones pendientes, la nota orientativa y la verificación. El documento FinOps que lo consuma usará la [plantilla FinOps](https://github.com/denispaiva/cellar/blob/main/templates/finops/README.md), según la [etapa de Blends](../../../blends/docs/architecture-and-finops.md). Este diseño no lo reemplaza.

**Publicabilidad.** VCX-D032 hace público el repositorio `vcx` y deja privados los proyectos. Por eso este documento no copia importes del ledger, identificadores de facturación, números de proyecto ni cuentas personales. Cita esos datos por su fuente. Cuando exista la instancia Solera, el lugar natural de este diseño es el proyecto Teyst dentro de ella; hoy no existe ([solera](../../../solera/README.md)).

## 0. Pedido y aclaración

- [U] Respuestas del usuario en la sesión de origen: unos 10 proyectos nuevos por año; Firebase como default con «Blaze con control de gastos dentro del free tier»; «teyst deberá ser en breve una app nativa, el resto se integra».
- [U] Aclaración en esta sesión, ante la pregunta sobre qué significa «el resto se integra»: **«Web dentro de la nativa»**. Es decir, un solo código Expo: la app nativa es el canal principal y la web actual sale del mismo repositorio y sigue publicándose en Hosting como canal secundario. Los demás proyectos (Melquisedec, Pinot Index, Salmanazar) **no** se integran dentro de la app; quedan fuera de alcance salvo como dependencias ya existentes.

## 1. Problema, límites y requisitos que afectan el costo

### 1.1 Estado actual medido

| Tema | Hecho [H] | Fuente |
|---|---|---|
| Stack cliente | Expo `~57.0.16`, expo-router, React `19.2.3`, React Native `0.86.2`, react-native-web `~0.21`, `firebase` **10.14.1** fijado, sin paquetes `@react-native-firebase/*`; `expo-apple-authentication` ya está instalado | [`package.json`](../../../../blends/vc/teyst/package.json) |
| Backend | Functions con Node 24, `firebase-functions` 7, `firebase-admin` 13; política global `maxInstances: 2` vía `setGlobalOptions`; región por defecto `us-central1` | [`functions/package.json`](../../../../blends/vc/teyst/functions/package.json), `functions/src/runtimePolicyCore.ts` |
| Entrega | Solo web: `expo export -p web` publicado en Hosting con targets `dev`, `prod` y `canary`; el predeploy construye el bundle | [`firebase.json`](../../../../blends/vc/teyst/firebase.json) |
| Configuración nativa | `app.json` estático con **un solo** identificador `com.tintum.teyst.dev` para iOS y Android y esquema `teyst-dev`; `eas.json` declara los perfiles `development` y `production`, ambos con canal; `appVersionSource: remote` | [`app.json`](../../../../blends/vc/teyst/app.json), [`eas.json`](../../../../blends/vc/teyst/eas.json) |
| Builds | EAS nunca publicó un build (dato de la sesión de origen, coherente con la evaluación: «EAS no compiló nada aún») | [Plan de transición, Fase 5](../../../../blends/ideas/teyst/transition-plan-draft.md) |
| Auth | `services/auth.ts` usa `signInWithPopup`, solo web; el propio archivo anota que en nativo hace falta una credencial nativa y `signInWithCredential` | `services/auth.ts:128-147` |
| Firebase en cliente | `getAuth` y `getFirestore` sin persistencia explícita; varias suscripciones `onSnapshot` en tiempo real (lobby, ronda, podio, revelación) | `services/firebase.ts`, `services/*.ts` |
| App Check | No se encontró inicialización de App Check en `services/`, `lib/` ni `app/` del repositorio actual. La investigación previa trataba el repositorio heredado | búsqueda de `initializeAppCheck` |
| Deploy | Manual por `workflow_dispatch`, OIDC/WIF, prod con confirmación, gate por la variable `TEYST_BUDGET_GUARDRAIL_OK`; no cubre builds nativos | [`teyst-deploy.yml`](../../../../blends/.github/workflows/teyst-deploy.yml) |
| IAM | Concedido a mano y documentado, no versionado | [`infrastructure-notes.md`](../../../../blends/vc/teyst/docs/infrastructure-notes.md) |
| FinOps | Líneas Blaze de los proyectos dev, prod y legacy con presupuesto declarado **en el ledger**. Para el legacy consta que no se creó un budget en GCP. Apple Developer Program activo; registro de Play pagado; EAS en plan Free | [`billing-ledger.json`](../../../../blends/vc/teyst/finops/billing-ledger.json) |
| Admisión de EAS | `approved_with_exception`, riesgo `critical` por publicación externa irreversible. Condiciones: versión `eas-cli@22.0.0` y credenciales de submit inexistentes en CI. Vence el **2026-11-17**. La justificación cita el stack Expo 54 / RN 0.81 | [evaluación](../../../../blends/vc/tooling/evaluations/eas-build-submit.evaluation.json) |
| Deuda de dependencia | `undici` `high` en runtime, transitivo de `firebase`, se corrige en `firebase@12.18.0`; Salmanazar lista «`firebase` 12 en Teyst» como su riesgo S1 | [framework-debt](../../../../blends/vc/docs/standards/framework-debt.md), [diseño de etiquetas](../../../../blends/vc/teyst/docs/planning/etiquetas-del-evento-design.md) |
| Política de organización | Domain Restricted Sharing rechaza `allUsers` como invoker, lo que afecta callables `invoker: 'public'` | infrastructure-notes, § `allUsers` |

### 1.2 Requisitos

- [U] Canal principal nativo en iOS y Android, con la web desde el mismo código.
- [U] Firebase como default, en Blaze, con gasto contenido dentro del free tier.
- [H] VCX-D032: Teyst es privado y sus despliegues consumen cuota de Actions; el CI sin cuota rige solo para los productos públicos ([diseño de visibilidad](2026-11-01-public-visibility-design.md#ci-sin-cuota)).
- [H] La admisión de EAS prohíbe por construcción las credenciales de submit en CI.
- [H] Requisitos de tiendas vigentes: target API 36 en Play para apps nuevas y actualizaciones desde el 2026-08-31 ([Play](https://support.google.com/googleplay/android-developer/answer/11926878)); Xcode 26 y SDK 26 desde el 2026-04-28, y SDK 27 anunciado para abril de 2027 ([Apple](https://developer.apple.com/news/upcoming-requirements/)); Sign in with Apple obligatorio si se ofrece Google (guideline 4.8, ya registrado en el plan de transición). Consultado el 2026-11-02.
- [I] Escala inicial: piloto Friends & Family de 15 a 18 personas según la [nota de tiendas](../../../../blends/ideas/teyst/store-publishing-requirements.md). No hay hipótesis de usuarios después del piloto; ver sección 7.

### 1.3 Fuera de alcance

Integrar otros proyectos en la app, rediseñar el backend, Remote Config, Analytics, Crashlytics, monetización in-app y la migración de datos.

## 2. Alternativas y escenario recomendado

Cada eje se decide por separado. La recomendación del conjunto aparece en 2.10.

### 2.1 Build nativo

| Opción | Costo y cupo [H] | Ventajas | Costos y riesgos |
|---|---|---|---|
| **A1. EAS Build en la nube, plan Free** | 15 builds Android y 15 iOS por mes, prioridad baja, timeout de 45 min. El plan Free «cannot incur overage charges»: al agotarse, no hay más builds hasta el mes siguiente ([plans](https://docs.expo.dev/billing/plans/), [FAQ](https://docs.expo.dev/billing/faq/), [pricing](https://expo.dev/pricing)) | No requiere Mac con Xcode actualizado; firma gestionada; reproducible desde un checkout limpio | Las credenciales de **firma** quedan custodiadas por Expo; esperas largas en hora pico; la cuota es un tope duro, no un costo |
| **A2. Build local** (`eas build --local` o `expo prebuild` con Xcode y Gradle) | Sin cargo de nube. Sin verificar si `--local` consume cuota: la doc no lo dice ([local builds](https://docs.expo.dev/build-reference/local-builds/)) | Credenciales en la máquina del PO; no depende de la cola | Requiere Xcode 26 y el SDK de Android al día; no admite variables Secret de EAS; reproducibilidad atada a la máquina |
| **A3. Runners macOS de GitHub Actions** | En repositorio privado, macOS cuesta USD 0,062/min frente a USD 0,006/min en Linux, unas 10 veces más; el cupo Free equivale a USD 12/mes ([tarifas](https://docs.github.com/en/billing/reference/actions-runner-pricing)) | Pipeline versionado | Consume la cuota escasa de la cuenta ([política de escasez](../../../../blends/vc/docs/standards/github-scarcity.md)); contradice el espíritu de VCX-D032 |

[P] **A1 como vía normal y A2 como respaldo** cuando la cuota se agote o para development builds. **A3 descartada.** El tope sin overage de A1 cumple «dentro del free tier» por construcción. [I] El riesgo que A1 agrega es la custodia de las claves de firma en Expo. Es distinto del riesgo de submit que la admisión prohíbe en CI, y conviene registrarlo en la reevaluación (decisión D3).

### 2.2 Publicación en tiendas (submit)

[H] `eas submit` necesita una App Store Connect API Key y una clave de cuenta de servicio de Google ([submit](https://docs.expo.dev/submit/introduction/)). La documentación actual dice que, en un primer envío, el `eas submit` por defecto crea el primer release de Android en el track interno ([Android](https://docs.expo.dev/submit/android/)). La subida manual inicial es una opción, no una obligación general.

[H] **`eas submit` ejecutado localmente también envía la credencial a Expo.** En `eas-cli@22.0.0`, la versión evaluada, `ServiceAccountSource.js` lee el archivo local de la clave de Google y lo devuelve como `googleServiceAccountKeyJson`. `AndroidSubmitter.js` lo incluye en la configuración de la mutación GraphQL `createAndroidSubmissionAsync`. Del mismo modo, `IosSubmitter.js` envía `keyP8` dentro de `ascApiKey`. Leído el 2026-11-02 en el paquete publicado en npm, sin ejecutarlo. No se verificó si el backend conserva la clave después del envío.

| Opción | Dónde existen o pasan las credenciales |
|---|---|
| S1. Herramientas de las tiendas: Transporter o Xcode para iOS, subida del AAB en Play Console para Android | Solo en las consolas y en la máquina del PO; Expo nunca las recibe |
| S2. `eas submit` local del PO, con claves en archivos fuera del repositorio | Se guardan en la máquina del PO, pero **se transmiten al backend de submit de Expo** en cada envío |
| S3. `eas submit` con credenciales cargadas en EAS | Se guardan en servidores de Expo, alcanzables por cualquier automatización de EAS |

[P] **S1 mientras rija la restricción «sin credenciales de submit en EAS»**, para todos los releases y no solo el primero. S2 y S3 quedan excluidas mientras rija esa restricción: S3 almacena las credenciales en Expo y S2 se las transmite. Usar S2 exige que la reevaluación de D3 registre una excepción explícita con su riesgo. El costo de S1 es atención humana del PO en cada release. El paso de borrador a producción en cada consola sigue siendo un acto humano.

### 2.3 Variantes de app y entornos

[H] Hoy el perfil `production` de `eas.json` compilaría con `com.tintum.teyst.dev`, porque `app.json` declara un solo identificador. Es un defecto latente: el primer build de producción saldría con la identidad de desarrollo.

[P] Reemplazar `app.json` por `app.config.ts` con una variable `APP_VARIANT` (`development` | `production`) que fije, por variante, el identificador (`com.tintum.teyst.dev` / `com.tintum.teyst`), el nombre visible, el esquema (`teyst-dev` / `teyst`) y la configuración de Firebase (proyecto dev o prod). Cada perfil de `eas.json` exporta su `APP_VARIANT`. Es el patrón de variantes de la documentación de Expo [I]; la verificación de conformidad del perfil de stack puede comprobar que ningún perfil `production` resuelva un identificador con sufijo `.dev`.

### 2.4 SDK de Firebase en nativo

| Opción | Descripción | A favor | En contra |
|---|---|---|---|
| **B1. JS SDK en todas las plataformas, actualizado a ≥ 12, más RNFB solo para App Check** | `initializeAuth` con `getReactNativePersistence(AsyncStorage)` en nativo; Firestore con caché en memoria; puente App Check RNFB → `CustomProvider` | Un solo código de datos para web y nativo; cambio acotado a `services/firebase.ts`; la guía de Expo recomienda el JS SDK para apps universales y exige `firebase@12.0.0` o superior en el SDK actual ([Using Firebase](https://docs.expo.dev/guides/using-firebase/)) | **Sin persistencia en disco de Firestore en RN**: el caché persistente depende de IndexedDB, que React Native no tiene; el soporte sigue abierto como pedido ([issue 7947](https://github.com/firebase/firebase-js-sdk/issues/7947)), dato parcial. Dos instancias de Firebase conviven (JS y nativa) |
| B2. RNFB en nativo y JS SDK en web, detrás de la capa `services/` con archivos `.native.ts` / `.web.ts` | SDKs nativos para Auth, Firestore, App Check y, si llega, Messaging | Persistencia offline nativa: la doc de Firestore la declara activa por defecto en Android y Apple ([offline](https://firebase.google.com/docs/firestore/manage-data/enable-offline)) | Dos implementaciones de cada servicio, más superficie de prueba; no verificado si RNFB conserva ese default (rnfirebase.io no respondió) |
| B3. RNFB en todas las plataformas | — | — | [I] RNFB no cubre la web para la mayoría de sus módulos; rompería «web dentro de la nativa». Descartada |

[P] **B1 ahora**, con la capa `services/` como costura para pasar a B2 servicio por servicio si la sección 2.7 demuestra que el offline es necesario. [I] Teyst es una experiencia en vivo y multiusuario (lobby y rondas con `onSnapshot`); sin red no hay cata compartida, así que el valor del offline en disco es bajo hasta que se demuestre lo contrario. El salto de `firebase` 10.14.1 a ≥ 12 (última en npm: 13.1.0) es prerrequisito de compatibilidad: la guía de Expo lo exige. Hay otras dos comprobaciones relacionadas que son **independientes** y que ese requisito no demuestra:
- **Vulnerabilidad de `undici`:** se cierra solo si el árbol resuelto de la versión elegida trae una versión corregida. Se verifica con el árbol instalado y la auditoría, no por el número de `firebase`.
- **Riesgo S1 de Salmanazar:** se cierra solo cuando pasa la prueba que define su plan.

La actualización se hace como cambio propio, con versión exacta elegida, verificada primero en web y antes de tocar nativo.

### 2.5 Autenticación nativa

[H] `signInWithPopup` no funciona en nativo. [P] En nativo: Google con un SDK nativo de inicio de sesión que entregue un `idToken` a `signInWithCredential`, y Apple con `expo-apple-authentication`, ya instalado, más `OAuthProvider('apple.com')`. Para el SDK de Google se comparan dos candidatos: `@react-native-google-signin/google-signin` en su edición gratuita y `expo-auth-session`. La elección pasa por la evaluación de tooling del precursor (D6). La web conserva `signInWithPopup`, según la decisión del PO del 2026-08-28. El registro de huellas SHA en las apps Android de Firebase es requisito compartido con App Check. [H] La Restore Credentials API de Android, exigida desde abril de 2027, sigue sin camino de primera clase; la nota de tiendas fija reevaluarla en 2027-01.

### 2.6 App Check nativo

[H] Proveedores: App Attest o DeviceCheck en Apple, Play Integrity en Android. Play Integrity tiene un cupo de 10.000 llamadas por día en el tier estándar; App Check figura «No-cost, subject to quotas» ([App Check](https://firebase.google.com/docs/app-check), [precios](https://firebase.google.com/pricing)). [H] La investigación previa validó la compatibilidad de `@react-native-firebase/app-check` con Expo 54 y el patrón puente, y ordenó siete pasos en los que el enforcement va último ([investigación](../../../../blends/ideas/teyst/app-check-native-investigation.md)).

[P] Seguir esos siete pasos sobre Expo 57 (la compatibilidad se revalida: la versión verificada fue 26.2.0 y la última es 27.1.0), con el proveedor de debug para simuladores y una corrida por plataforma en dispositivo físico. [I] El puente RNFB → `CustomProvider` está documentado como patrón, pero no demostrado en Teyst. Criterio de aceptación previo al enforcement: observar, con App Check en modo monitoreo, que las solicitudes del SDK JS (callables, Firestore y Storage) llegan con token válido desde cada plataforma nativa. Las métricas de App Check de la consola deben mostrar esas solicitudes como verificadas. [P] Agregar App Check web con reCAPTCHA Enterprise (gratis hasta 10.000 evaluaciones por mes) **antes** de activar el enforcement: si se activa solo con clientes nativos atestiguados, el enforcement rompe la web. [I] App Check reduce tráfico de clientes no genuinos, pero no es un tope de gasto (ver 2.9).

### 2.7 Offline

[P] Requisito mínimo: la app abre, conserva la sesión (persistencia de Auth) y muestra un estado «sin conexión» claro; las escrituras de una cata requieren red. Es lo que B1 da sin trabajo extra. Pregunta decisiva, D5: «¿hay un caso de uso real en que la cata o su registro deban continuar sin red, por ejemplo en un winebar sin señal?». Si la respuesta es sí y se respalda con evidencia del piloto, se migra Firestore a B2 en nativo.

### 2.8 Actualizaciones OTA y push

**OTA.** [H] EAS Update Free: 1.000 MAU, 100 GiB de ancho de banda y sin overage. `eas.json` ya define canales. [P] Incluir `expo-updates` desde el primer binario, con `runtimeVersion` por política de huella (fingerprint), porque agregarlo después exige otro binario en tienda. [P] Publicar una actualización al canal `production` es un despliegue: se hace a mano, desde un checkout limpio de `main` y con la misma confirmación explícita que el deploy de prod, nunca automática desde CI. [I] OTA cambia solo JavaScript y assets; los cambios de módulo nativo siguen requiriendo un build y revisión de tienda.

**Push.** [H] FCM no tiene costo; en iOS requiere una clave APNs ([FCM iOS](https://firebase.google.com/docs/cloud-messaging/ios/get-started)). [P] **Diferir push** hasta que exista un caso de uso aceptado (VCX-P3). Cuando llegue, la opción preferida es `expo-notifications` para permisos y token del dispositivo, y FCM directo desde Functions con el Admin SDK. El Expo Push Service sería otro tercero con tokens y límites no verificados.

### 2.9 FinOps: «Blaze con control de gastos dentro del free tier»

[H] Un budget de GCP no limita el gasto: «Setting an alerts-only budget doesn't automatically cap … usage or spending», y la primera notificación puede tardar horas ([budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets), [notify](https://docs.cloud.google.com/billing/docs/how-to/notify)). [H] Cloud Functions y Cloud Storage requieren Blaze. Cupos sin costo en Blaze: Functions con 2M invocaciones/mes; Firestore con 50K lecturas, 20K escrituras y 20K borrados por día y 1 GiB almacenado; Hosting con 10 GB almacenados y 360 MB/día de transferencia ([precios](https://firebase.google.com/pricing), consultados el 2026-11-02).

| Mecanismo | Qué limita | Latencia | Permisos | Reversibilidad y efectos |
|---|---|---|---|---|
| M1. Budget de GCP con alertas (invariante 37 del precursor: USD 1 y 50/90/100 %) | Nada; solo avisa | Horas | Billing Account Administrator o Costs Manager sobre la cuenta | Reversible. [H] `TEYST_BUDGET_GUARDRAIL_OK=true` es una declaración del PO, no una medición; no consta un budget en GCP para los proyectos actuales |
| M2. Budget → Pub/Sub → función que desvincula billing ([tutorial](https://docs.cloud.google.com/billing/docs/how-to/disable-billing-with-notifications)) | Todo el proyecto, incluido el free tier | Horas, y [H] «doesn't guarantee that you won't spend more than your budget» | La SA recibe `roles/billing.admin` sobre la **cuenta de facturación**, y quien la instala también debe tenerlo | [H] «Resources might be irretrievably deleted»; reactivar «there's no guarantee of service recovery». **Irreversible en el peor caso** |
| M3. `maxInstances` por función | Concurrencia de cómputo de Functions; al tope, las solicitudes HTTP esperan 30 s y reciben 429 ([manage functions](https://firebase.google.com/docs/functions/manage-functions)) | Inmediata | Código desplegado | Reversible. [H] Ya existe: global 2 |
| M4. Cuotas por API (overrides) | Volumen de llamadas por API, no gasto; no todos los servicios las admiten; con demora de aplicación ([capping](https://docs.cloud.google.com/apis/docs/capping-api-usage)) | Minutos [I] | `roles/servicemanagement.quotaAdmin` | Reversible. No verificado si Firestore admite override de lecturas |
| M5. App Check con enforcement | Tráfico de clientes no atestiguados | Inmediata tras activarlo | Admin de Firebase | Reversible; no limita el uso de clientes legítimos |
| M6. Límites de producto (topes de Free, 3 ligas) y reglas de Firestore | Lo que cada usuario puede generar | Inmediata | Código y reglas | Reversible; es el control más fino y más barato |
| M7. Freno reversible, **experimento**: budget → Pub/Sub → función que publica reglas de Firestore y Storage *deny-all* y fija el invoker de las callables en cerrado | Lecturas y escrituras de clientes y llamadas a callables; no fija un techo de gasto | Horas, como M2 | `firebaserules.admin` y permisos de Functions **sobre el proyecto**, no sobre la cuenta | [I] Datos intactos; se revierte republicando las reglas versionadas. Sin probar y sin diseño de recuperación. Falta definir: estado si se aplica solo una parte (reglas sí e invoker no, o una sola de las bases), cómo se detecta, identidad de operación para no reaplicar ante notificaciones duplicadas (entrega at-least-once), restauración desde la revisión versionada y quién la autoriza. También hay que medir en `dev-teyst` qué consumo sigue (Hosting, invocaciones rechazadas) |

[I] **Ningún mecanismo garantiza «dentro del free tier».** Los datos de billing llegan con horas de retraso y los cupos diarios de Firestore se pueden superar antes de que llegue cualquier alerta. Lo alcanzable es un riesgo acotado: topes de diseño que hagan improbable el desvío y un freno que corte su duración.

[P] Capas, de menor a mayor costo:
1. **Ya:** verificar M1 por CLI en los dos proyectos y crearlo donde falte (acto del PO), para que el gate `TEYST_BUDGET_GUARDRAIL_OK` deje de ser una declaración. M3 en cada función nueva, en particular las públicas. M6 como requisito de diseño de cada función que lea en bucle.
2. **Con el primer build nativo:** M5 según 2.6.
3. **Antes de abrir más allá del piloto:** diseñar la recuperación de M7 (columna de la tabla), prototiparlo en `dev-teyst` y medir su latencia real con un budget de prueba. Hasta entonces, M7 no cuenta como control.
4. **M2 no se recomienda** para `prod-teyst`: cambia un sobrecosto acotado por una pérdida posible de datos y servicio, y exige un rol de cuenta de facturación que contradice el mínimo privilegio. Si el usuario lo quisiera para un proyecto descartable o de dev, es su decisión explícita (D8), con la cuenta de facturación identificada y aceptando la irreversibilidad.

Fuera de GCP, los topes ya son duros: EAS Free sin overage; Apple Developer Program a USD 99 por año y Play con pago único, ambos ya pagados según el ledger; el CI nativo fuera de Actions por 2.1.

### 2.10 Escenario recomendado

[P] Un solo repositorio Expo con `app.config.ts` y dos variantes; `firebase` ≥ 12 en todas las plataformas; autenticación nativa con Google y Apple; RNFB solo para App Check; `expo-updates` desde el primer binario; builds con EAS en la nube (local como respaldo); submit con las herramientas de las tiendas, sin credenciales de submit en CI ni en EAS; web exportada a Hosting como hoy, ahora además con App Check web y como destino de enlaces universales; push y offline en disco diferidos hasta tener evidencia. FinOps en capas M1 + M3 + M5 + M6, con M7 como experimento y M2 excluido de prod.

## 3. Componentes, responsabilidades y entornos

| Componente | Responsabilidad | Entornos | Estado |
|---|---|---|---|
| App Expo universal (iOS, Android, web) | UI y rutas; capa `services/` con variantes por plataforma solo donde haga falta (`auth`, `app-check`, `label-photo`) | variante dev → `dev-teyst`; prod → `prod-teyst` | Existe para web; nativo propuesto |
| `app.config.ts` | Identidad por variante: identificador, nombre, esquema, Firebase, plugins (`@react-native-firebase/app`, `app-check`, `expo-updates`, auth nativa) | — | Propuesto; reemplaza `app.json` |
| Firebase JS SDK ≥ 12 | Auth (persistencia AsyncStorage en nativo), Firestore, Functions, Storage | ambos | Actualización propuesta |
| RNFB `app` + `app-check` | Token de atestación nativo, puenteado a `CustomProvider` | ambos | Propuesto |
| EAS Build | Binarios firmados; perfiles `development` (dev client, interno) y `production` (tiendas) | Free | Configurado, nunca usado |
| EAS Update | Actualizaciones JS por canal `development` / `production` | Free | Propuesto |
| Hosting | Web secundaria; `/.well-known/apple-app-site-association` y `/.well-known/assetlinks.json` para enlaces universales y App Links de invitaciones a eventos | targets `dev`, `prod`, `canary` | Hosting existe; los archivos `.well-known` son propuestos |
| Functions, Firestore, Storage | Sin cambios de forma; App Check enforcement al final | ambos | Existe |
| App Store Connect, Play Console | Fichas, TestFlight, tracks interno → cerrado → producción | — | Cuentas activas; el tipo de cuenta de Play no está verificado |
| CI privado (Actions, Linux) | Verificación sin credenciales: `typecheck`, `vitest`, `expo export -p web` y [I] `expo export -p ios` y `-p android` (bundle JS, sin compilar nativo) | — | Parcial |

[P] Nada de esto se aprovisiona por este documento. El reparto manual o asistido del plan de transición (consolas y claves a cargo del PO; configuración como código a cargo del agente) se conserva.

## 4. Factores de consumo

| Componente | Unidad | Cantidad hipotética, piloto | Cupo gratuito [H] | Sensibilidad | Fuente o supuesto |
|---|---|---|---|---|---|
| EAS Build | builds por plataforma y mes | 2–6 [I] | 15 + 15, sin overage | Media: los reintentos por fallo de firma consumen cuota | Supuesto; medir desde el primer mes |
| EAS Update | MAU | ≤ 18 | 1.000 | Baja | Tamaño del piloto |
| Firestore | lecturas por día | Sin estimar: participantes × rondas × documentos por `onSnapshot` | 50.000 | **Alta**: las suscripciones en tiempo real multiplican lecturas | Falta medir una cata real; ver 7 |
| Functions | invocaciones por mes | ≪ 2M [I] | 2M | Baja con `maxInstances` | Supuesto |
| Play Integrity | llamadas por día | Una por sesión más los refrescos de token [I] | 10.000 | Baja en piloto | Supuesto |
| Hosting | MB por día | Baja: la web pasa a ser secundaria | 360 MB | Baja | Supuesto |
| Tiendas | anual o único | Ya pagado | — | Nula marginal | Ledger |
| Actions privado | USD-min | Solo Linux | Cupo Free de la cuenta, compartido | Media: el cupo es uno por cuenta | Política de escasez |

## 5. Actividades que generan costo o atención

Exploración y construcción, en orden propuesto: (1) reevaluar la admisión de EAS antes del 2026-11-17; (2) actualizar `firebase` a ≥ 12 y verificar en web; (3) `app.config.ts` con variantes; (4) development build y autenticación nativa; (5) RNFB App Check con debug provider; (6) registro de apps en Firebase y huellas SHA, App Attest y Play Integrity; (7) política de privacidad y ToS, que bloquean ambas tiendas (pendiente #2 de la nota de tiendas); (8) fichas, TestFlight y track cerrado de Play; (9) piloto F&F, que con cuenta personal de Play coincide con el requisito de 12 testers durante 14 días ([Play](https://support.google.com/googleplay/android-developer/answer/14151465)); (10) enforcement de App Check.

Atención humana del PO, sin convertirla a moneda: consolas de Apple, Google y Firebase, claves `.p8` y APNs, submit, budgets de GCP y reclutamiento de testers. Consumo de agentes: dentro del cupo de suscripción, según la [política FinOps](../../../finops-policy.md#free-tier-first-y-eficiencia-de-suscripciones).

## 6. Riesgos, simplificación, portabilidad y salida

| Riesgo | Peor caso plausible | Mitigación [P] |
|---|---|---|
| Admisión de EAS vencida o desactualizada | Primer build con una versión y un stack no evaluados (la evaluación cita Expo 54 / RN 0.81 y `eas-cli@22.0.0`); bajo VCX-P7, la aprobación no se transfiere sola a una revisión materialmente distinta | Reevaluar antes de usar (D3) |
| Build de producción con identidad de dev | Ficha de tienda creada con `com.tintum.teyst.dev`, que no se renombra | `app.config.ts` y un check de conformidad (2.3) |
| Publicación irreversible | Un binario o un update OTA defectuoso llega a usuarios | Submit con herramientas de las tiendas; OTA solo con gate; tracks internos primero |
| Credenciales de submit fuera de control | Las claves de las tiendas transitan o quedan en Expo y una automatización publica sin el PO | S1; excepción explícita en D3 para cualquier uso de `eas submit` |
| Dos instancias de Firebase (JS + RNFB) | Token de App Check no adjuntado y callables rechazadas al activar el enforcement | Criterio de aceptación de 2.6 en modo monitoreo; enforcement último; pruebas en dispositivo físico |
| Enforcement que rompe la web | La web sin App Check queda bloqueada | App Check web antes del enforcement (2.6) |
| Salto mayor de `firebase` | Regresiones en web (tiempo real, auth); dar por cerrados `undici` o S1 sin verificarlos | Cambio aislado, verificado en web y canary antes de nativo; las tres comprobaciones de 2.4 por separado |
| Churn de Expo | SDK 58 publicado el 2026-10-15 con RN 0.88 ([changelog](https://expo.dev/changelog)); 57 envejece | Primer build en 57: su tabla oficial declara target SDK de Android 36, iOS mínimo 16.4 y Xcode 26.4+ ([versiones](https://docs.expo.dev/versions/latest/)); comprobarlo en el artefacto compilado. Actualizar a 58 en un cambio propio |
| Requisitos de tiendas futuros | SDK 27 de Apple en abril de 2027; Restore Credentials en abril de 2027 | Fechas en `deadlines.json` del precursor, por pedido explícito |
| Gasto de Firestore por tiempo real | Una cata grande supera los cupos diarios antes de cualquier alerta | M6 y medición en el piloto; M7 |
| DRS de la organización | Callables públicas que no se pueden desplegar | Ya registrado como deuda; App Check no lo resuelve |
| Custodia de firma en Expo | Pérdida o compromiso de la cuenta Expo | Play App Signing deja la clave de release en Google; la clave de subida es recuperable; 2FA en Expo (D3) |

**Simplificación.** [I] La alternativa más simple que cumple el pedido es esta: no hay servidor nuevo, ni push, ni offline en disco, ni CI nativo. La única pieza que se agrega por necesidad de seguridad es RNFB App Check.

**Portabilidad y salida.** [I] EAS Build es sustituible por builds locales con `expo prebuild` (A2), así que el costo de salida es bajo. EAS Update es la dependencia más pegajosa: salir exige otro servidor de updates compatible o renunciar a OTA, que tampoco es crítico. Firebase sigue siendo el default fijado por el usuario.

## 7. Cobertura: qué falta para estimar o decidir

- Lecturas de Firestore por cata real: falta una medición (consola de uso de un evento del piloto en `dev-teyst`). Sin ese dato, la línea de Firestore no se estima.
- Usuarios después del piloto: no hay hipótesis.
- Tipo de cuenta de Play, personal u organización: abierto desde agosto.
- Existencia de budgets de GCP en los proyectos actuales: no verificado; requiere `gcloud billing budgets list` del PO.
- Target SDK de Android de Expo 57: la tabla oficial declara 36, releída el 2026-11-02. Falta comprobarlo en el artefacto compilado.
- Si `eas build --local` consume cuota de EAS: la [FAQ](https://docs.expo.dev/billing/faq/) recomienda builds locales al agotar la cuota de la nube. Eso los respalda como respaldo, pero no hay una garantía textual sobre el contador.
- Persistencia por defecto de Firestore en RNFB: activada en Android e iOS según la revisión independiente, que cita [RNFirebase](https://rnfirebase.io/firestore/usage); el asistente no pudo releerla (timeout). Aplica solo a B2: con el SDK JS de B1 no hay persistencia en disco.
- Comportamiento real y recuperación de M7: requiere diseño y un prototipo en dev.
- Requisito de 12 testers durante 14 días: aplica a cuentas personales creadas después del 2023-11-13 ([Play](https://support.google.com/googleplay/android-developer/answer/14151465)). D9 debe comprobar el tipo y la fecha de creación de la cuenta real. La exención de las cuentas de organización no figura en la página oficial.
- Retención en Expo de las claves enviadas por `eas submit`: no verificada.

## 8. Decisiones pendientes para el usuario

| ID | Decisión | Opciones | Recomendación [P] | Urgencia |
|---|---|---|---|---|
| D1 | Aceptar este escenario de referencia | Aceptar, ajustar o rechazar | Aceptar 2.10 | Media |
| D2 | Momento del primer build nativo respecto de la actualización de `firebase` | Antes o después de ≥ 12 | Después: primero la actualización, verificada en web | Media |
| D3 | Reevaluar la admisión de `eas-build-submit` | Reevaluar con la versión vigente de `eas-cli` y Expo 57, incluyendo la custodia de firma en EAS y el hecho de que `eas submit` transmite las claves a Expo; dejar vencer | **Resuelta el 2026-11-02**: reevaluada sobre `eas-cli@27.2.0` (77,3/100, confianza alta, riesgo `critical`) y `approved_with_exception` por el usuario, con alcance `eas build` y `eas update`, sin `eas submit`, vigente hasta el 2027-01-31 y revisión el 2026-12-02. Fuente: [registro](../../../brix/tooling/evaluations/eas-build-submit.evaluation.json) | Cerrada |
| D4 | Vía de submit | S1 siempre; S2 con excepción explícita registrada en D3 | S1 siempre, mientras rija «sin credenciales de submit en EAS»; revisar con la frecuencia y el esfuerzo medidos en el piloto | Media |
| D5 | ¿La cata necesita funcionar sin red? | Sí, con evidencia → B2 en nativo; no → B1 | No, hasta tener evidencia del piloto | Baja |
| D6 | SDK de Google Sign-In nativo | `@react-native-google-signin/google-signin` gratuito; `expo-auth-session` | Evaluar ambos con el pipeline de tooling | Media |
| D7 | Verificar y crear budgets de GCP en `dev-teyst` y `prod-teyst` (M1) | Sí; no | Sí, antes del primer build nativo; es acto del PO | **Alta** |
| D8 | Corte automático de billing (M2) | Nunca en prod; solo en proyectos dev o descartables; nunca | Nunca en prod; diseñar la recuperación de M7 y prototiparlo en dev | Media |
| D9 | Tipo y fecha de creación de la cuenta de Play | Personal creada después del 2023-11-13 (12 testers / 14 días); otra | Verificar ambos datos; si aplica el requisito, alinearlo con el piloto F&F | Alta antes de Android |
| D10 | Push | Diferir; implementar ya | Diferir | Baja |
| D11 | Ubicación de este diseño | Dejarlo en `vcx`; moverlo a Solera cuando exista | Mover a Solera al crearla | Baja |

## Nota orientativa

Según VCX-P2: **7 de 10** para el escenario 2.10 corregido. Es orientativa y no comparable con otras evaluaciones.

Historia de la nota:
- La primera versión se calificó 7.
- La revisión la bajó provisionalmente a 6 por una contradicción sobre credenciales y por afirmaciones sin demostrar.
- Las correcciones resolvieron esa contradicción. Durante la corrección se agregó un cuarto descuento por el trabajo manual del submit, que una segunda observación de la revisión mostró infundado: no había datos de frecuencia, esfuerzo ni riesgo operativo que lo sostuvieran, y el trabajo manual puede ser proporcional a un piloto con pocos releases y a la restricción de credenciales. Se retiró.
- El submit manual pasa a ser un dato a medir: si los releases del piloto muestran una frecuencia o un esfuerzo que lo vuelva costoso o propenso a errores, se revisa D4 con esa evidencia.

Descuentos:
- Un punto porque la meta FinOps del usuario no queda garantizada y M7 es un experimento sin diseño de recuperación.
- Un punto por la complejidad de dos SDK de Firebase conviviendo para obtener App Check, con el puente todavía sin demostrar en Teyst.
- Un punto porque la línea de costo de mayor sensibilidad (lecturas de Firestore en tiempo real) no tiene medición.

No hay descuento por sobrediseño: push, offline en disco y CI nativo quedan diferidos.

## Insumo para el perfil de stack nativo del scaffolding

[P] Controles verificables que este diseño sugiere para la verificación de conformidad, sin implementarlos aquí. Ninguno es una regla general de cualquier scaffolding: cada uno se aplica según una condición explícita del proyecto. Las decisiones de Teyst no se vuelven obligación del perfil por aparecer aquí.

Condicionados a plataforma y distribución:
- **Si la app tiene variantes de entorno y se distribuye en tiendas:** ningún perfil de build de producción resuelve el identificador de la variante de desarrollo.
- **Si se distribuye en Google Play:** el target SDK de Android cumple el mínimo de Play vigente, comprobado en el artefacto. Una app solo iOS, solo web o distribuida fuera de Play no lo necesita.

Condicionados al perfil Firebase/GCP:
- **Si el backend usa Cloud Functions:** hay `maxInstances` declarado en cada función.
- **Si hay proyectos de GCP enlazados a una cuenta de facturación:** existe un budget verificable por CLI. Es el invariante 37 del precursor, que rige ese perfil, no a cualquier stack.

Decisiones de Teyst, configurables por proyecto:
- Sin credenciales de submit en CI ni en EAS. Deriva de la admisión de EAS de Teyst; otro proyecto podría aceptar otra condición.
- `expo-updates` con una política de `runtimeVersion`. OTA es opcional por proyecto; lo verificable es que, si está, su publicación a producción tenga gate.
- Sin runners macOS en repositorios privados. Es una consecuencia de la cuota de esta cuenta y de VCX-D032, no una regla universal: en un repositorio público los runners estándar no consumen cuota.

## Qué no autoriza

No instala paquetes, no crea cuentas, apps, budgets, funciones ni claves, no cambia IAM ni billing, no ejecuta builds ni submits, no publica en tiendas, no modifica `../blends` ni sus `deadlines.json`, y no registra decisiones en el [registro](../../decisions/README.md). Cada paso de la sección 5 requiere autorización propia, con alcance, autoridad y verificación.

## Revisión y correcciones

El 2026-11-02 el usuario pegó en esta sesión la revisión de otra sesión, y después una segunda observación sobre la versión corregida. Esa revisión analizó un handoff de solo lectura de `gpt-6-luna` y releyó en persona sus puntos principales. Nota provisional de la revisión: 6/10. No registró aprobaciones ni cambió el documento. El asistente comprobó sus hallazgos antes de incorporarlos:

| Hallazgo | Comprobación del asistente | Cambio |
|---|---|---|
| `eas submit` local no mantiene las claves fuera de Expo | Confirmado en el código de `eas-cli@22.0.0` publicado en npm, la versión evaluada (2.2) | S2 corregida; S1 para todos los releases; D3 y D4 actualizadas |
| El primer release de Android no exige subida manual | Confirmado en la [doc de submit Android](https://docs.expo.dev/submit/android/) | 2.2 corregida |
| «Firebase ≥ 12 corrige `undici` y desbloquea S1» mezcla tres comprobaciones | Aceptado: la afirmación original no tenía evidencia para las dos últimas | 2.4 y riesgos |
| Target de Expo 57 = API 36 | Confirmado en la tabla oficial de versiones | Sección 7 y riesgos |
| Cuota de `--local`, persistencia de RNFB, 12 testers | Aceptados con su grado de verificación; la página de RNFB no pudo releerse | Sección 7 y D9 |
| M7 sin diseño de recuperación ni techo de gasto | Aceptado | Tabla de 2.9 y capa 3 |
| El puente App Check debe demostrar tokens en las solicitudes del SDK JS | Aceptado | Criterio de aceptación en 2.6 y riesgos |
| Los checks del scaffolding confunden requisitos de Teyst con política general | Aceptado | Insumo para el perfil, separado en dos listas |
| Segunda observación: el descuento por submit manual carece de sustento | Aceptado: no había medición de frecuencia, esfuerzo ni riesgo | Descuento retirado; nota 7/10; D4 se revisa con datos del piloto |
| Segunda observación: `maxInstances`, budgets, identidad de producción y target de Android no son reglas generales | Aceptado | Cada check del insumo queda condicionado a plataforma, distribución o perfil Firebase/GCP |

## Verificación de esta entrega

- Evidencia local: lectura de solo lectura, el 2026-11-02, de los archivos del precursor enlazados en 1.1; no se escribió en `../blends`.
- Código de `eas-cli@22.0.0`: descargado del registro de npm al scratchpad de la sesión y leído sin ejecutarlo.
- Tras las correcciones, los enlaces externos responden 200, salvo `rnfirebase.io`, que no respondió desde esta máquina (timeout); se conserva como fuente de la revisión independiente.
- Evidencia externa: documentación oficial de Expo, Firebase, Google Cloud, Google Play, Apple y GitHub, consultada el 2026-11-02 por un subagente de búsqueda y resumida por un modelo, sin citas literales salvo las entrecomilladas. El asistente principal releyó dos fuentes decisivas: el plan Free de EAS sin overage y las advertencias del corte de billing. Los datos parciales están listados en la sección 7.
- Enlaces relativos: comprobados contra el árbol local el 2026-11-02.
- Publicabilidad: no se incluyen importes del ledger, números de proyecto, cuentas de facturación ni direcciones de correo.
