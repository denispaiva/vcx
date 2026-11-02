# cadtopo: notas de evaluación (2026-11-01)

evaluatedRef: `1ba0af0ee116eff0d00e53cca42fe1726d29dd1f` (HEAD de `main`, 2026-09-10). Se eligió HEAD y no el tag `0.0.1` porque el tag es prerelease y quedó 2 commits atrás.

## Qué se verificó
- Repo: creado 2026-08-18, último push 2026-09-10 (52 días), 7 commits de un único autor en 3 días, 1 release prerelease `0.0.1`, 0 advisories, 0 issues de terceros, MIT, 3 estrellas, 0 forks.
- Organización `code0-tech`: verificada, creada 2023-11-12, 29 repos públicos activos, sitio codezero.build. cadtopo no es parte del producto central (plataforma no-code). Sin SECURITY.md en el repo ni en `code0-tech/.github`.
- Archivos leídos: README.md, pyproject.toml, workflows build/publish, backbone.py, selection.py, llm.py, embedding.py, telemetry.py, tools.py, extracto de tracing.py, examples/humaneval/.env.example, los 10 archivos de tests y uv.lock.
- Tests: 133 funciones `test_` en 10 archivos; CI `build.yml` corre pytest en cada push (5 corridas de build, todas success, incluida HEAD). Solo Python 3.12/ubuntu.
- Dependencias: 6 directas de runtime; uv.lock con 108 entradas, incluidas torch 2.13.0, transformers 5.14.1, litellm 1.95.0 y 15 paquetes nvidia. El modelo de embeddings `sentence-transformers/multi-qa-mpnet-base-dot-v1` se descarga de HuggingFace al primer uso.
- Llamadas a modelos: todas por `litellm.completion` (directo o vía Instructor) con `api_key`/`api_base` por backbone; `api_key=None` cae en la resolución por entorno de LiteLLM. Un modelo local es posible en teoría vía `api_base` (p. ej. Ollama), pero el repo no lo documenta ni lo prueba; los ejemplos usan OpenRouter con `sk-...`. Los modelos de suscripción (Claude Max, ChatGPT) no son alcanzables por LiteLLM sin claves pago por token.
- Antecedentes: no hay evaluación previa de code0-tech o cadtopo en `blends/vc/tooling/evaluations/`.

## Anomalías
1. El enlace al paper DyTopo del README apunta a `https://arxiv.org/` (raíz), no a un paper concreto: la base académica declarada no es verificable.
2. Versionado incoherente: `pyproject.toml` dice 0.1.0, el único tag es 0.0.1 (prerelease) y el workflow sobrescribe la versión con el tag; los 2 commits posteriores cambian comportamiento (escala 0-100, jueces cruzados) sin release.
3. La sección de licencia del README habla de "subprojects" inexistentes; LICENSE es MIT. Cabecera con branding de la organización ajeno al proyecto.
4. El quickstart del README muestra `api_key="sk-..."` literal en código; `tracing.py` escribe prompts y respuestas completas en `runs/`; nada de esto está declarado como permiso o dato.
5. Sin contenido que intente instruir a agentes ni pedir ejecución de comandos fuera de la instalación normal.

## Encaje
- Necesidad A: aporta ideas (eje log-costo, urgencia por rondas restantes, escalado y desescalado por señal, par de jueces de modelo distinto con escalado por desacuerdo), pero no perfiles de tarea, pisos por riesgo, motivos de elevación ni acta, que el resolver existente ya tiene. La señal que usa (confianza autodeclarada por el agente) no la expone el despacho de Claude Code.
- Necesidad B: solo cuenta tokens de sus propias llamadas en proceso; no lee transcripts ni distingue rama o sesión.
- Costo: Python + torch, claves de proveedor (contra `allowPayPerToken: false`) y reestructurar el trabajo en rondas con manager.

## Flags verdaderos
networkAccess, credentialsAccess (high), localWriteReversible, newLocalDependencies (medium). `sensitiveDataAccess` quedó en false: la herramienta no lee datos sensibles por sí misma, pero envía a proveedores y escribe en `runs/` todo lo que se le pase.

## Presupuesto de API
36 llamadas a `gh api` de 40 (0 a `search/code`). Lecturas locales del precursor: policy y tamaño del resolver, listado de evaluaciones.
