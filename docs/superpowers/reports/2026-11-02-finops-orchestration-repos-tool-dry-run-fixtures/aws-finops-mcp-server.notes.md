# Notas: aws-finops-mcp-server (medido 2026-11-01)

- evaluatedRef: d8316bd06943506564aeb129b162e7671c7a4b93 (HEAD de main). Release/tag única: v0.1.1 (2025-06-08).
- Verificado por API/lectura directa: metadatos del repo, releases, tags, advisories (vacío), workflows (vacío), usuario (creado 2018-02-12), 20 commits, 6 issues/PRs, árbol (15 archivos), README, pyproject.toml, requirements.txt, .python-version (3.13), main.py y helpers/util.py completos.
- Qué hace: 2 tools MCP stdio (FastMCP), ambas con readOnlyHint. get_cost (Cost Explorer, 2 llamadas por perfil) y run_finops_audit (EC2 stopped, EBS available, EIP sin asociar, Budgets). Todo boto3 read/describe; sin escrituras ni borrados en AWS ni en disco.
- Credenciales: perfiles del AWS CLI (~/.aws); all_profiles recorre todos los perfiles locales y llama sts:GetCallerIdentity. Política IAM sugerida con Resource "*". Devuelve IDs de cuenta, costos y IDs de recursos.
- Dependencias: boto3 y mcp[cli], sin versiones fijas; uv.lock presente.
- Sin SECURITY.md, sin CI, sin tests. Nada en los archivos leídos pide ejecutar comandos o revelar secretos (instalación estándar, incluye curl|sh de astral.sh para uv como opción).

## Anomalías
1. Abandonado: último push 2025-06-11 (508 días), 20 commits en 3 semanas, 3 PRs externos abiertos sin respuesta (#4, #5, #6; #6 de 2026-01-06 corrige lectura de tamaño de volumen en util.py). updated_at 2026-10-20 sólo refleja metadatos.
2. requires-python >=3.10 pero util.py usa f"{volume["Size"]} GB" (comillas anidadas, válido sólo en Python 3.12+): SyntaxError en 3.10/3.11. Además get_accessible_regions puede dejar accessible_regions sin definir si falla; get_budget_data anota un tipo de retorno distinto del real (tupla). README anuncia salidas PDF/HTML/CSV que el servidor no genera.
3. Costo: README declara USD 0.01 por invocación de get_cost (no verificado con tarifa AWS).

## Encaje
Necesidades A y B (enrutar modelos; medir tokens de inferencia por rama/sesión): nula cobertura; es una herramienta exclusiva de AWS. El resolver existente en blends cubre A y el instrumento context-window-per-branch cubre medición de contexto. observedOutcome y observedAdoption: unavailable. Sin evaluación previa del autor en el registro del precursor (grep local sin resultados).

## Flags verdaderos
newLocalDependencies, networkAccess, credentialsAccess, sensitiveDataAccess, broadScope (all_profiles multi-cuenta + IAM Resource "*", aunque de solo lectura). No remoteWrite, no destructiveActions.

## Llamadas a la API usadas: 19 (presupuesto 40). Sin search/code. Sin clonar ni ejecutar código.
