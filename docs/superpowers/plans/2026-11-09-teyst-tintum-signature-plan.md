# Plan · firma «powered by tintum» en Teyst

Fecha: 2026-11-09. Estado: **ejecutado hasta el PR** el 2026-11-09, autorizado con «Sí, ejecutá»: opción A en el login y en las páginas legales, [PR 65](https://github.com/denispaiva/solera-teyst/pull/65), ADR 0012 de Teyst. Mergeado el 2026-11-09 en `main` (`9622813`, CI verde); sin deploy a Hosting. Decisión que lo origina: VCX-D061 en el [registro](../../decisions/README.md); lista de productos comerciales en [recursos de Tintum](../../../assets/tintum/README.md#productos-comerciales). Pedido: el usuario respondió «Sí, planificala» a «¿Planifico la integración de la firma en Teyst?».

Teyst es el primer producto comercial que muestra la firma. Este plan cubre solo esa integración. No incluye deploys, piezas nuevas de marca ni otros productos.

## Hechos relevados

Leídos en solo lectura el 2026-11-09 en `vcx/solera/teyst/` (repositorio `denispaiva/solera-teyst`, canónico por VCX-D049).

- **Tintum ya aparece en Teyst, pero no se ve.** [`app/privacy.tsx`](https://github.com/denispaiva/solera-teyst/blob/main/app/privacy.tsx) y [`app/terms.tsx`](https://github.com/denispaiva/solera-teyst/blob/main/app/terms.tsx) dicen que Denis Paiva opera Teyst «bajo el nombre comercial Tintum». El contacto es `denis@tintum.app` y los identificadores nativos son `com.tintum.teyst.dev` / `com.tintum.teyst`. En ninguna pantalla aparece `powered by tintum`.
- **El login tiene un pie de texto legal.** `LoginLegalNotice`, en [`components/login-fullbleed-chrome.tsx`](https://github.com/denispaiva/solera-teyst/blob/main/components/login-fullbleed-chrome.tsx), muestra «Al continuar confirmás… Términos y Política de Privacidad» a 11 px, en `InstrumentSans_400Regular`, color `textoTerciarioNoche` sobre `#43121B` (contraste medido en el código: 7,15). Lo usan el login por defecto y la bienvenida.
- **Las páginas legales comparten un marco.** [`components/legal-page.tsx`](https://github.com/denispaiva/solera-teyst/blob/main/components/legal-page.tsx) arma `/privacy` y `/terms`, con fondo claro por tema.
- **La paleta coincide.** El token `crema` de Teyst es `#F4EDE0`, el mismo crema de los prompts de Tintum. El fondo del login, `burdeosSombra` `#43121B`, es más oscuro que el burdeos de la lámina crema sobre burdeos (`#5E1B26` en el prompt).
- **No hay fuente redondeada cargada.** Teyst carga Instrument Sans y Marcellus. El lettering redondeado de `tintum` existe solo dentro de las láminas PNG, con textura y fondo.
- **La marca de Teyst es ADR 0009.** [`docs/decisions/0009-official-brand-mark.md`](https://github.com/denispaiva/solera-teyst/blob/main/docs/decisions/0009-official-brand-mark.md) fija el isotipo y dice que agregar marca a una pantalla «sería un cambio de diseño, que necesita su propia decisión». La firma de Tintum es ese tipo de cambio.
- **El checkout está ocupado.** El checkout tiene 48 archivos modificados en `feat/tarjeta-borrador-iconos`, y otras sesiones trabajan en esa carpeta: dos estaban corriendo al relevarla. Su `AGENTS.md` exige que todo deploy salga de `main` con CI verde y con autorización por acción, objeto y entorno.

## Decisión de diseño: firma en texto ahora, logotipo después

| Opción | Qué se ve | Costo | Riesgo |
|---|---|---|---|
| **A · Texto** (recomendada) | `powered by tintum` en Instrument Sans, con el mismo estilo del pie legal | Un componente chico, sin assets ni dependencias | No reproduce el lettering redondeado de la marca |
| B · Recorte raster de la lámina | El lockup texturado, recortado | Recorte y fondo a mano | A 11–14 px la textura 3D se vuelve una mancha; el fondo no coincide con `#43121B` |
| C · Logotipo vectorial | `tintum` redondeado en SVG | Depende de `tintum-brand-kit` (VCX-D061), que hoy no existe | Bloquea la firma hasta tener el kit |

Se recomienda **A**: indica la firma hoy, es legible, accesible y sin copia de assets. La procedencia queda como «firma en texto, sin copia». Cuando exista el kit, C reemplaza solo la palabra `tintum` dentro del mismo componente. Ese cambio activa el pendiente `tintum-brand-kit`, sin rehacer la integración.

## Ubicación propuesta

1. **Login, debajo del aviso legal.** Es la primera pantalla de quien llega y ya tiene un pie de texto chico. La firma va en una línea propia, centrada, con el mismo cuerpo y color terciario. Es estática y no depende de la sesión, así que no introduce parpadeo.
2. **Pie de `/privacy` y `/terms`.** Va en `LegalPage`, debajo del contenido. Esas páginas ya nombran a Tintum como nombre comercial.

Fuera de este plan: la home, el menú de cuenta, el splash, los íconos nativos, las fichas de tienda y la OG image. Cada uno cambia el diseño de una superficie con más tráfico y se decide aparte.

**Enlace.** `tintum` enlaza a `https://tintum.app`, con apertura externa como los enlaces legales, solo si al implementar se comprueba que el dominio sirve una página. Si no la sirve, la firma va sin enlace. El área táctil sigue el patrón `TERMS_LINK_HIT_PADDING` (mínimo de 24 CSS px en web y 44 pt en iOS).

## Pasos

| # | Paso | Dónde | Verificación |
|---|---|---|---|
| 1 | Crear una rama `feat/powered-by-tintum` desde `origin/main` actualizado, en un worktree propio. No tocar el checkout compartido ni la rama `feat/tarjeta-borrador-iconos` | `solera-teyst` | `git status` limpio en el worktree; base = `origin/main` |
| 2 | Registrar la decisión en Teyst: una ADR 0012 (en `origin/main` la última es 0011) o un agregado a ADR 0009 que cite VCX-D061, la opción A y las dos ubicaciones | `docs/decisions/` de Teyst | La ADR enlaza VCX-D061 por URL pública, sin rutas a `vcx/` |
| 3 | Crear el componente `PoweredBy` con el texto, un `accessibilityLabel` y el enlace condicional | `components/powered-by.tsx` | `npm run typecheck`, `npm run lint` |
| 4 | Montarlo en `LoginLegalNotice` y en `LegalPage` | los dos componentes | Revisión visual en el dev server a 320, 390 y 1280 px; contraste ≥ 4,5 en ambos fondos; área táctil medida |
| 5 | Pruebas existentes | — | `npm run test:unit` y `npm run test:rules` sin regresiones |
| 6 | Actualizar en VCX la fila de Teyst en la [lista de productos](../../../assets/tintum/README.md#productos-comerciales): firma integrada, PR y modo «texto, sin copia» | `vcx` | Enlaces resuelven |
| 7 | PR en `solera-teyst` con capturas, para que el PO lo revise y mergee | GitHub | CI verde |

**Deploy:** no está incluido. La firma llega a `teyst.web.app` recién con un deploy de Hosting desde `main`, que necesita su propia autorización según el `AGENTS.md` de Teyst.

## Criterios de aceptación

- `powered by tintum` se ve en el login (por defecto y en la bienvenida) y en `/privacy` y `/terms`, a 320 px sin cortes ni desborde.
- Si hay enlace, abre `https://tintum.app` fuera de la app, con área táctil dentro de las pautas.
- Contraste medido ≥ 4,5:1 en los dos fondos.
- Sin cambios en la lógica de sesión, en Functions, en reglas ni en identificadores nativos.
- typecheck, lint, pruebas unitarias y de reglas en verde.

## Riesgos y recuperación

- **Ruido en un pie ya denso.** El login suma una línea a un pie de 11 px. Si en la revisión visual compite con el aviso legal, se deja solo en las páginas legales: es la variante mínima.
- **Choque con trabajo en curso.** Otras sesiones tocan los mismos componentes del login. El worktree propio aísla el trabajo, y antes del PR se rebasa sobre `origin/main`.
- **Reversión.** Es un componente y dos montajes: se revierte con un `git revert` del merge, sin datos ni migraciones.

## Decisiones que quedan para el PO

1. Opción A (texto ahora) frente a esperar el logotipo vectorial.
2. Ubicación: login + legales, o solo legales.
3. Enlace a `tintum.app`, si el dominio sirve página.
