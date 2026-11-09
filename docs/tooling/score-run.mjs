#!/usr/bin/env node
// Envoltorio de VCX-D035 sobre `brix tool score` del precursor. Hace cumplir las
// precondiciones 2 y 3 del procedimiento y agrega una línea por comando persistido
// a score-runs.jsonl. Diseño: docs/superpowers/specs/2026-11-01-tooling-evaluation-in-vcx-design.md
//
// Uso, desde la raíz de VCX:
//   node docs/tooling/score-run.mjs evaluate --input <evidencia> --now <ISO> --operator "<texto>"
//       [--offline] [--dry-run] [--replace-decision]
//   node docs/tooling/score-run.mjs decide --id <id> --status <estado> --by "<nombre>"
//       [--rationale <texto>] [--review-at <fecha>] [--accepted-risk]
//       --now <ISO> --operator "<texto>" [--dry-run] [--replace-decision]
//
// --policy, --output-dir y --narrative-doc los fija el envoltorio. --replace-decision
// es obligatorio si el registro ya tiene una decisión humana. El motor no tiene
// --dry-run en decide: en seco, decide solo corre los controles.
//
// Salidas: 0 éxito; 1 precondición o argumentos; 3 el precursor cambió durante la
// corrida (no se agrega línea; revertir a mano lo que el motor escribió en docs/tooling).
// Otro código distinto de 0 es el del motor.
//
// Límites: no bloquea corridas concurrentes ni verifica el estado de VCX fuera de
// docs/tooling (paso 8 manual de D035). Si el motor escribe y falla agregar la línea,
// la corrida siguiente lo detecta por el hash del registro.

import { spawnSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { appendFileSync, existsSync, readFileSync, realpathSync } from 'node:fs';
import path from 'node:path';

const ROOT = path.resolve(import.meta.dirname, '../..');
const PRECURSOR = path.resolve(ROOT, '../blends');
const CLI = '../blends/vc/brix/packages/cli/bin/brix.js';
const POLICY = '../blends/vc/tooling/scoring-policy.json';
const OUTPUT_DIR = 'docs/tooling';
const RUNS_FILE = path.join(ROOT, OUTPUT_DIR, 'score-runs.jsonl');
const GUARDED_PATHS = ['vc/brix/packages/cli', 'vc/tooling/scoring-policy.json'];
const RESERVED_FLAGS = ['policy', 'output-dir', 'narrative-doc'];
const OWN_FLAGS = ['now', 'operator', 'replace-decision', 'dry-run'];
const RATIONALE_PLACEHOLDER = '<ver humanDecision.rationale>';

function fail(message, code = 1) {
  console.error(`score-run: ${message}`);
  process.exit(code);
}

// Misma semántica que parseFlags del motor: `--name valor` si el siguiente token no
// empieza con `--`; si no, booleano. Conserva el orden para reconstruir el comando.
function parseArgs(argv) {
  const pairs = [];
  for (let i = 0; i < argv.length; i++) {
    const token = argv[i];
    if (!token.startsWith('--')) fail(`argumento inesperado "${token}"`);
    const next = argv[i + 1];
    if (next != null && !next.startsWith('--')) {
      pairs.push([token.slice(2), next]);
      i++;
    } else {
      pairs.push([token.slice(2), true]);
    }
  }
  return pairs;
}

function sha256(buffer) {
  return createHash('sha256').update(buffer).digest('hex');
}

function git(...args) {
  const result = spawnSync('git', ['--no-optional-locks', '-C', PRECURSOR, ...args], {
    encoding: 'utf8',
  });
  if (result.status !== 0) {
    fail(`git ${args.join(' ')} falló: ${(result.stderr || result.error?.message || '').trim()}`);
  }
  return result.stdout.trim();
}

function precursorFingerprint() {
  return {
    dirty: git('status', '--porcelain', '--ignored', '--', ...GUARDED_PATHS),
    precursorHead: git('rev-parse', 'HEAD'),
    cliTree: git('rev-parse', 'HEAD:vc/brix/packages/cli'),
    policySha256: sha256(readFileSync(path.join(PRECURSOR, 'vc/tooling/scoring-policy.json'))),
  };
}

function readRecord(candidateId) {
  const file = path.join(ROOT, OUTPUT_DIR, 'evaluations', `${candidateId}.evaluation.json`);
  if (!existsSync(file)) return null;
  const raw = readFileSync(file);
  try {
    return { sha: sha256(raw), record: JSON.parse(raw) };
  } catch (error) {
    fail(`${path.relative(ROOT, file)} no es JSON válido (${error.message}); revisarlo con git`);
  }
}

function lastRunFor(candidateId) {
  if (!existsSync(RUNS_FILE)) return null;
  const runs = readFileSync(RUNS_FILE, 'utf8')
    .split('\n')
    .map((line, index) => [line, index + 1])
    .filter(([line]) => line.trim() !== '')
    .map(([line, number]) => {
      try {
        return JSON.parse(line);
      } catch (error) {
        fail(`score-runs.jsonl, línea ${number}, no es JSON válido (${error.message})`);
      }
    })
    .filter((run) => run.candidate === candidateId);
  return runs.at(-1) ?? null;
}

function quote(value) {
  return /^[\w./:<>@=+-]+$/.test(value) ? value : JSON.stringify(value);
}

// Mismo formato que las líneas existentes (separadores `, ` y `: `).
function formatLine(line) {
  const fields = Object.entries(line).map(([key, value]) => `${JSON.stringify(key)}: ${JSON.stringify(value)}`);
  return `{${fields.join(', ')}}`;
}

const [subcommand, ...rest] = process.argv.slice(2);
if (subcommand !== 'evaluate' && subcommand !== 'decide') {
  fail('falta el subcomando: evaluate o decide (ver el uso en la cabecera de docs/tooling/score-run.mjs)');
}

const pairs = parseArgs(rest);
const flags = Object.fromEntries(pairs);

// 1. Desde la raíz: evidenceInputRef y las rutas relativas dependen del cwd.
if (realpathSync(process.cwd()) !== realpathSync(ROOT)) {
  fail(`correr desde la raíz de VCX (${ROOT}), no desde ${process.cwd()}`);
}

// 2. Flags y configuración que el envoltorio fija.
for (const name of RESERVED_FLAGS) {
  if (name in flags) fail(`--${name} lo fija el envoltorio; quitarlo`);
}
for (const name of ['brix.config.json', '.brixrc.json']) {
  if (existsSync(path.join(ROOT, name))) {
    fail(`${name} en la raíz cambiaría rutas del motor (por ejemplo narrativeDocPath); quitarlo antes de correr`);
  }
}
if (typeof flags.now !== 'string' || Number.isNaN(Date.parse(flags.now))) {
  fail('falta --now <ISO> válido; se reutiliza entre la corrida en seco y la persistida');
}
if (typeof flags.operator !== 'string' || flags.operator.trim() === '') {
  fail('falta --operator "<quién corre y con qué autorización>"');
}

let candidateId;
if (subcommand === 'evaluate') {
  if (typeof flags.input !== 'string') fail('evaluate: falta --input <evidencia>');
  try {
    candidateId = JSON.parse(readFileSync(flags.input, 'utf8')).candidate?.id;
  } catch (error) {
    fail(`evaluate: no se pudo leer --input: ${error.message}`);
  }
} else {
  candidateId = flags.id;
}
if (typeof candidateId !== 'string' || !/^[a-z0-9][a-z0-9._-]*$/i.test(candidateId)) {
  fail(`id de candidato inválido o ausente: ${JSON.stringify(candidateId)}`);
}

// 3. Precondición 2: motor y política sin cambios locales ni ignorados.
const before = precursorFingerprint();
if (before.dirty !== '') {
  fail(`el motor o la política del precursor tienen cambios locales o ignorados; no es reproducible:\n${before.dirty}`);
}

// 4. Procedencia del registro vigente: su hash debe ser el de su última línea.
const previous = readRecord(candidateId);
const lastRun = lastRunFor(candidateId);
if (previous && lastRun?.evaluationSha256 !== previous.sha) {
  fail(
    `el registro de "${candidateId}" (sha256 ${previous.sha}) no coincide con su última línea en score-runs.jsonl ` +
      `(${lastRun?.evaluationSha256 ?? 'sin líneas'}): corrida fuera del envoltorio o escritura parcial; resolver antes de seguir`,
  );
}
if (!previous && lastRun) {
  fail(`score-runs.jsonl tiene líneas de "${candidateId}" pero falta su registro en ${OUTPUT_DIR}/evaluations/`);
}
if (!previous && subcommand === 'decide') {
  fail(`decide: no hay evaluación de "${candidateId}" en ${OUTPUT_DIR}/evaluations/`);
}

// 5. Precondición 3: no reemplazar una decisión humana sin saberlo.
const previousStatus = previous?.record.status ?? null;
const decision = previous?.record.humanDecision;
if (decision) {
  const expiresAt = previous.record.expiresAt;
  const expired = expiresAt != null && Date.parse(expiresAt) <= Date.parse(flags.now);
  console.error(
    `score-run: "${candidateId}" tiene una decisión ${decision.status} de ${decision.decidedBy} ` +
      `(${decision.decidedAt}), ${expiresAt ? `${expired ? 'vencida' : 'vigente'} hasta ${expiresAt}` : 'sin vencimiento registrado'}` +
      `${decision.reviewAt ? `, revisión ${decision.reviewAt}` : ''}.`,
  );
  if (!flags['replace-decision']) {
    fail(`${subcommand} la reemplazaría; confirmarlo con el usuario y repetir con --replace-decision`);
  }
}

const engineArgs = [];
const recordedArgs = [];
for (const [name, value] of pairs) {
  if (OWN_FLAGS.includes(name)) continue;
  engineArgs.push(`--${name}`);
  recordedArgs.push(`--${name}`);
  if (value !== true) {
    engineArgs.push(value);
    recordedArgs.push(name === 'rationale' ? RATIONALE_PLACEHOLDER : quote(value));
  }
}
const fixedArgs = ['--policy', POLICY, '--output-dir', OUTPUT_DIR, '--now', flags.now];
engineArgs.push(...fixedArgs);
recordedArgs.push(...fixedArgs.map(quote));

const line = {
  candidate: candidateId,
  command: ['node', CLI, 'tool', 'score', subcommand, ...recordedArgs].join(' '),
  now: flags.now,
  precursorHead: before.precursorHead,
  cliTree: before.cliTree,
  policySha256: before.policySha256,
  formulaVersion: null,
  evaluationSha256: null,
  previousStatus,
  operator: flags.operator,
};

if (flags['dry-run']) {
  if (subcommand === 'evaluate') {
    const result = spawnSync(process.execPath, [CLI, 'tool', 'score', 'evaluate', ...engineArgs, '--dry-run'], {
      cwd: ROOT,
      stdio: 'inherit',
    });
    if (result.status !== 0) fail(`el motor terminó con código ${result.status}`, result.status ?? 1);
  } else {
    console.log('(decide no tiene --dry-run en el motor: solo se corrieron los controles)');
  }
  console.log(`\nscore-run en seco: no se escribió nada. Línea que se agregaría (sin formulaVersion ni evaluationSha256):\n${formatLine(line)}`);
  process.exit(0);
}

// 6. Corrida persistida.
const result = spawnSync(process.execPath, [CLI, 'tool', 'score', subcommand, ...engineArgs], {
  cwd: ROOT,
  stdio: 'inherit',
});
const after = precursorFingerprint();
const current = readRecord(candidateId);

if (result.status !== 0) {
  if (current?.sha !== previous?.sha) {
    console.error('score-run: el motor falló pero el registro cambió; revisar docs/tooling con git antes de reintentar');
  }
  fail(`el motor terminó con código ${result.status}; no se agregó línea`, result.status ?? 1);
}

// 7. Precondición 2, después: si el precursor cambió, la corrida no es reproducible.
const changed = ['precursorHead', 'cliTree', 'policySha256'].filter((key) => before[key] !== after[key]);
if (after.dirty !== '' || changed.length > 0) {
  fail(
    `corrida inválida: el precursor cambió durante la corrida (${[...changed, after.dirty && 'cambios locales'].filter(Boolean).join(', ')}). ` +
      'No se agregó línea; revertir a mano lo que el motor escribió en docs/tooling',
    3,
  );
}
if (!current) fail(`el motor terminó bien pero no hay registro de "${candidateId}"`);

line.formulaVersion = current.record.formulaVersion ?? null;
line.evaluationSha256 = current.sha;
appendFileSync(RUNS_FILE, `${formatLine(line)}\n`, 'utf8');
console.log(`\nscore-run: línea agregada a ${OUTPUT_DIR}/score-runs.jsonl:\n${formatLine(line)}`);
