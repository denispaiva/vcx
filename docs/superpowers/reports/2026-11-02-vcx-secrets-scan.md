# Scan de secretos del historial de `vcx`

Fecha: 2026-11-02. Autoridad: el usuario respondió «Autorizo rc.1» a la propuesta de bajar Betterleaks v2.0.0-rc.1 y escanear el historial de `main` en solo lectura, tras preguntar «¿por qué no betterleaks?» ante la propuesta inicial de gitleaks. Antecedentes: la [revisión del historial](2026-11-01-vcx-public-history-review.md) y la [reescritura del correo](2026-11-01-vcx-noreply-rewrite.md), previas a publicar `denispaiva/vcx` según VCX-D032.

## Herramienta

[H] Betterleaks v2.0.0-rc.1 es la compuerta de secretos que el PO de Blends aprobó en el precursor el 2026-10-01, con estado `approved_with_exception`, vigencia hasta el 2026-12-30 y gitleaks 8.30.1 en sombra. Se usó la misma versión para no extender esa aprobación a otra revisión, según VCX-P7. Homebrew ofrece la 1.9.0, de la línea v1, y la release más reciente es la v2.0.0-rc.6; ninguna se usó.

- Origen: release oficial `betterleaks/betterleaks`, archivo `betterleaks_2.0.0-rc.1_darwin_arm64.tar.gz` de 8 730 265 bytes, en una carpeta temporal aislada; no se instaló nada en el sistema.
- Integridad: SHA-256 `666b96714a4d4e01d4007030bdbfbea9579a356585c0d45b1dfead0faf47a380`, igual a la línea de `checksums.txt` de la release. Ese mismo `checksums.txt` contiene el SHA-256 del tarball de linux que la CI del precursor fijó y verificó con firma Sigstore el 2026-10-01.
- Límite: la firma Sigstore no se verificó aquí porque `cosign` no está instalado. La integridad queda comprobada; la procedencia, solo por el vínculo anterior.

## Ejecución

`betterleaks git <vcx> --log-opts=main --redact --validate=false --analyze=false`, las mismas opciones de validación que usa la CI del precursor, con la configuración por defecto: `vcx` no tiene `.betterleaks.toml`.

| Dato | Valor |
|---|---|
| Revisión | `main` en `d733649`, 62 commits |
| Estado del scan | `complete`, 1 850 653 bytes en 234 ms |
| Hash de configuración | `2b8e48142a4a505d626346caef5a5e2bc46af95893529cfcd80928efbc98ec70` |
| Hallazgos | 0 |

Control positivo: en un repositorio descartable con un token falso con formato de GitHub, la misma invocación terminó con código 1 y un hallazgo `github-pat`, redactado. El repositorio de control se borró.

## Lectura y pendientes

[I] El historial de `main` hasta `d733649` no contiene secretos detectables con las reglas por defecto de esta versión. Un cero no prueba ausencia: cubre lo que las reglas reconocen. No cubre los cambios sin commit ni los commits posteriores a `d733649`, que otras sesiones siguen agregando.

[P] Antes del push, repetir la misma invocación sobre la revisión exacta que se suba y adjuntar el resultado; si aparece un hallazgo real, el push se detiene.
