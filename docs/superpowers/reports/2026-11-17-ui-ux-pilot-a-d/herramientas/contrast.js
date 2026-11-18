// Contraste WCAG 2.2 de cada texto visible contra el primer fondo opaco de sus ancestros.
// Compone fondos semitransparentes; si antes del fondo opaco aparece un background-image, el texto es «no medible».
(() => {
  const parse = (c) => {
    const m = c.match(/rgba?\(([^)]+)\)/);
    if (!m) return null;
    const p = m[1].split(/[ ,/]+/).filter(Boolean).map(Number);
    return { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 };
  };
  const over = (top, bottom) => {
    const a = top.a + bottom.a * (1 - top.a);
    if (a === 0) return { r: 0, g: 0, b: 0, a: 0 };
    const mix = (k) => (top[k] * top.a + bottom[k] * bottom.a * (1 - top.a)) / a;
    return { r: mix('r'), g: mix('g'), b: mix('b'), a };
  };
  const lum = ({ r, g, b }) => {
    const f = (v) => { v /= 255; return v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; };
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b);
  };
  const ratio = (x, y) => { const [a, b] = [lum(x), lum(y)].sort((p, q) => q - p); return (a + 0.05) / (b + 0.05); };
  const hex = (c) => '#' + [c.r, c.g, c.b].map((v) => Math.round(v).toString(16).padStart(2, '0')).join('');

  function background(el) {
    const layers = [];
    for (let e = el; e; e = e.parentElement) {
      const cs = getComputedStyle(e);
      if (cs.backgroundImage && cs.backgroundImage !== 'none') return { unmeasurable: cs.backgroundImage.slice(0, 60) };
      const c = parse(cs.backgroundColor);
      if (c && c.a > 0) { layers.push(c); if (c.a >= 1) break; }
    }
    let bg = { r: 255, g: 255, b: 255, a: 1 }; // lienzo blanco por defecto
    for (const layer of layers.reverse()) bg = over(layer, bg);
    return { bg };
  }

  const rows = [];
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const seen = new Set();
  for (let n = walker.nextNode(); n; n = walker.nextNode()) {
    const text = n.textContent.trim();
    const el = n.parentElement;
    if (!text || !el || seen.has(el)) continue;
    seen.add(el);
    const cs = getComputedStyle(el);
    const rect = el.getBoundingClientRect();
    if (cs.visibility === 'hidden' || cs.display === 'none' || Number(cs.opacity) === 0 || rect.width === 0 || rect.height === 0) continue;
    if (el.closest('[aria-hidden="true"]') && el.closest('svg')) continue;
    const size = parseFloat(cs.fontSize);
    const weight = Number(cs.fontWeight) || 400;
    const large = size >= 24 || (size >= 18.66 && weight >= 700);
    const required = large ? 3 : 4.5;
    const b = background(el);
    const fgRaw = parse(cs.color);
    if (b.unmeasurable) { rows.push({ text: text.slice(0, 40), size, weight, result: 'no medible', reason: b.unmeasurable }); continue; }
    const fg = over(fgRaw, b.bg);
    const r = ratio(fg, b.bg);
    rows.push({ text: text.slice(0, 40), size, weight, fg: hex(fg), bg: hex(b.bg), ratio: Math.round(r * 100) / 100, required, result: r >= required ? 'pasa' : 'falla' });
  }
  const count = (k) => rows.filter((r) => r.result === k).length;
  return { textos: rows.length, pasa: count('pasa'), falla: count('falla'), noMedible: count('no medible'), fallas: rows.filter((r) => r.result === 'falla'), noMedibles: rows.filter((r) => r.result === 'no medible'), rows };
})()
