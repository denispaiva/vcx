// Freno del envoltorio score-run.mjs para el factor community.
//
// Cuando el colector de GitHub responde rate_limited o unavailable y no hay snapshot
// vigente que reutilizar, el motor deja factorScores.community en null sin escribir
// ninguna nota. Así se persistieron el 2026-11-17 cinco evaluaciones con puntajes y
// una recomendación distintos, sin aviso: el cupo anónimo de la API (60 por hora) se
// había agotado. Este módulo decide, sin I/O, si una corrida puede seguir.

// Estados del colector con los que la corrida sigue: hay datos, el conflicto queda
// explícito en el registro, o la fuente no es de GitHub y no se espera comunidad.
const PROCEED_STATES = new Set(['available', 'conflicting', 'not_applicable']);

/**
 * Antes de correr el motor. `collectorState` es el `state` que devolvió
 * collectGithubCommunityEvidence para la sourceUrl del candidato.
 * Devuelve { ok: true } o { ok: false, message }.
 */
export function preflightCommunity({ collectorState, offline, allowMissing }) {
  if (offline || allowMissing) return { ok: true };
  if (PROCEED_STATES.has(collectorState)) return { ok: true };
  return {
    ok: false,
    message:
      `el colector de comunidad respondió "${collectorState}": la evaluación saldría con community en null. ` +
      'Reintentar más tarde (con GITHUB_TOKEN o `gh auth login`), usar --offline para que el motor ' +
      'reutilice el snapshot vigente, o --allow-missing-community para seguir sin comunidad a sabiendas',
  };
}

/**
 * Después de la corrida persistida: el colector respondió "available" en el chequeo
 * previo, pero el registro igual quedó sin comunidad (por ejemplo, el cupo se agotó
 * entre el chequeo y el motor). Devuelve { ok: true } o { ok: false, message }.
 */
export function postflightCommunity({ collectorState, offline, allowMissing, record }) {
  if (offline || allowMissing || collectorState !== 'available') return { ok: true };
  if (record?.factorScores?.community != null) return { ok: true };
  return {
    ok: false,
    message:
      'el registro quedó con community en null aunque el colector respondía antes de correr ' +
      '(cupo agotado o red caída durante la corrida)',
  };
}
