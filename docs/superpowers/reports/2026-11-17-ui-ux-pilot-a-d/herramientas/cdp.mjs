// Brave sin interfaz, por el protocolo de DevTools, con un perfil propio y descartable.
// Uso:
//   node cdp.mjs ax <url>                    árbol de accesibilidad de los botones (JSON)
//   node cdp.mjs shot <url> <png> [w] [h]    captura del viewport
//   node cdp.mjs eval <url> <archivo.js>     evalúa una expresión y devuelve su valor (JSON)
import { spawn } from 'node:child_process';
import { mkdtempSync, readFileSync, writeFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';

const BRAVE = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser';
const [mode, url, a1, a2, a3] = process.argv.slice(2);
const port = 9300 + Math.floor(Math.random() * 500);
const profile = mkdtempSync(path.join(tmpdir(), 'cdp-profile-'));
const proc = spawn(BRAVE, ['--headless=new', `--remote-debugging-port=${port}`, `--user-data-dir=${profile}`,
  '--no-first-run', '--no-default-browser-check', '--disable-extensions', 'about:blank'], { stdio: 'ignore' });

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
async function target() {
  for (let i = 0; i < 50; i++) {
    try {
      const list = await (await fetch(`http://127.0.0.1:${port}/json/list`)).json();
      const page = list.find((t) => t.type === 'page');
      if (page) return page.webSocketDebuggerUrl;
    } catch {}
    await sleep(200);
  }
  throw new Error('Brave no respondió');
}

let ws; let seq = 0; const pending = new Map(); const events = [];
function send(method, params = {}) {
  const id = ++seq;
  ws.send(JSON.stringify({ id, method, params }));
  return new Promise((resolve, reject) => pending.set(id, { resolve, reject }));
}

try {
  ws = new WebSocket(await target());
  await new Promise((r) => (ws.onopen = r));
  ws.onmessage = (m) => {
    const msg = JSON.parse(m.data);
    if (msg.id && pending.has(msg.id)) {
      const p = pending.get(msg.id); pending.delete(msg.id);
      msg.error ? p.reject(new Error(msg.error.message)) : p.resolve(msg.result);
    } else events.push(msg);
  };
  const w = Number(mode === 'shot' ? a2 ?? 390 : 390); const h = Number(mode === 'shot' ? a3 ?? 844 : 844);
  await send('Emulation.setDeviceMetricsOverride', { width: w, height: h, deviceScaleFactor: 2, mobile: true });
  await send('Page.enable');
  await send('Page.navigate', { url });
  for (let i = 0; i < 50 && !events.some((e) => e.method === 'Page.loadEventFired'); i++) await sleep(100);
  await sleep(800);
  let out;
  if (mode === 'ax') {
    await send('Accessibility.enable');
    const { nodes } = await send('Accessibility.getFullAXTree');
    const byId = new Map(nodes.map((n) => [n.nodeId, n]));
    const groupOf = (n) => { let p = n; while (p) { if (p.role?.value === 'generic' && p.name?.value) return p.name.value; p = byId.get(p.parentId); } return null; };
    out = nodes.filter((n) => n.role?.value === 'button').map((n) => ({
      caso: groupOf(byId.get(n.parentId)),
      role: n.role.value,
      name: n.name?.value ?? '',
      nameFrom: (n.name?.sources ?? []).filter((s) => s.value || s.attributeValue).map((s) => ({ type: s.type, attribute: s.attribute, value: s.value?.value ?? s.attributeValue?.value, superseded: s.superseded ?? false })),
      properties: Object.fromEntries((n.properties ?? []).map((p) => [p.name, p.value.value])),
      children: (n.childIds ?? []).map((c) => byId.get(c)).map((c) => `${c?.role?.value}:${c?.name?.value ?? ''}`),
    }));
  } else if (mode === 'shot') {
    const { data } = await send('Page.captureScreenshot', { format: 'png' });
    writeFileSync(a1, Buffer.from(data, 'base64')); out = { saved: a1 };
  } else if (mode === 'eval') {
    const { result, exceptionDetails } = await send('Runtime.evaluate', { expression: readFileSync(a1, 'utf8'), returnByValue: true, awaitPromise: true });
    if (exceptionDetails) throw new Error(exceptionDetails.exception?.description ?? 'error en eval');
    out = result.value;
  }
  console.log(JSON.stringify(out, null, 1));
} finally {
  try { ws?.close(); } catch {}
  proc.kill();
  await sleep(300);
  rmSync(profile, { recursive: true, force: true });
}
