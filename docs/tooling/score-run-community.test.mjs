// Pruebas del freno de comunidad de score-run.mjs. Correr desde la raíz de VCX:
//   node --test docs/tooling/score-run-community.test.mjs
import assert from 'node:assert/strict';
import test from 'node:test';
import { postflightCommunity, preflightCommunity } from './score-run-community.mjs';

const base = { offline: false, allowMissing: false };

test('el chequeo previo deja seguir con datos, conflicto o fuente que no es de GitHub', () => {
  for (const collectorState of ['available', 'conflicting', 'not_applicable']) {
    assert.deepEqual(preflightCommunity({ ...base, collectorState }), { ok: true }, collectorState);
  }
});

test('el chequeo previo corta con cupo agotado, colector caído o repositorio inexistente', () => {
  for (const collectorState of ['rate_limited', 'unavailable', 'not_found']) {
    const gate = preflightCommunity({ ...base, collectorState });
    assert.equal(gate.ok, false, collectorState);
    assert.match(gate.message, new RegExp(collectorState));
    assert.match(gate.message, /--offline/);
    assert.match(gate.message, /--allow-missing-community/);
  }
});

test('el chequeo previo respeta --offline y --allow-missing-community', () => {
  assert.equal(preflightCommunity({ ...base, collectorState: 'rate_limited', offline: true }).ok, true);
  assert.equal(preflightCommunity({ ...base, collectorState: 'rate_limited', allowMissing: true }).ok, true);
});

test('el chequeo posterior corta si el colector respondía y el registro quedó sin comunidad', () => {
  const post = postflightCommunity({
    ...base,
    collectorState: 'available',
    record: { factorScores: { community: null, maintenance: 46.4 } },
  });
  assert.equal(post.ok, false);
});

test('el chequeo posterior acepta un registro con comunidad, aunque valga 0', () => {
  for (const community of [74.7, 0]) {
    const record = { factorScores: { community } };
    assert.equal(postflightCommunity({ ...base, collectorState: 'available', record }).ok, true, String(community));
  }
});

test('el chequeo posterior no exige comunidad cuando no se esperaba', () => {
  const record = { factorScores: { community: null } };
  for (const collectorState of ['not_applicable', 'conflicting', null]) {
    assert.equal(postflightCommunity({ ...base, collectorState, record }).ok, true, String(collectorState));
  }
  assert.equal(postflightCommunity({ ...base, collectorState: 'available', offline: true, record }).ok, true);
  assert.equal(postflightCommunity({ ...base, collectorState: 'available', allowMissing: true, record }).ok, true);
});
