# Genera la imagen Open Graph de Tintum (1200 × 630) a partir del wordmark
# aprobado, sin copiar su geometría: lee tintum-wordmark.svg y dibuja sus trazos
# con Pillow, con el mismo método de build_icon.py (trazo redondo supermuestreado).
#
# Uso: python3 -I assets/tintum/build_og.py assets/tintum/og
# Revisión aprobada el 2026-11-11 (VCX-D061): wordmark de 560 px de ancho, centrado.
# Solo entiende los comandos que usa el wordmark (M, V, H y A circular).
import math
import re
import sys
from pathlib import Path

DEEP = '#5E1B26'
CREAM = '#F4EDE0'
OG_W, OG_H = 1200, 630
MARK_W = 560  # ancho del wordmark: entra con margen en el recorte cuadrado central de 630 px

# Aprobada el 2026-11-11 (VCX-D061): crema sobre burdeos, como el hero y la
# cabecera de tintum.app. La variante burdeos sobre crema se descartó.
VARIANTS = {
    'tintum-og': {'bg': DEEP, 'fg': CREAM},
}

SRC = Path(__file__).with_name('tintum-wordmark.svg')


def parse_wordmark():
    s = SRC.read_text()
    vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', s).group(1).split()]
    stroke = float(re.search(r'stroke-width="([^"]+)"', s).group(1))
    d = re.search(r'<path d="([^"]+)"', s).group(1)
    cx, cy, cr = (float(v) for v in re.search(
        r'<circle cx="([^"]+)" cy="([^"]+)" r="([^"]+)"', s).groups())
    return vb, stroke, d, (cx, cy, cr)


def arc_points(x0, y0, r, sweep, x1, y1, steps=48):
    """Arco circular SVG (sin large-arc) de (x0, y0) a (x1, y1)."""
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    dx, dy = x1 - x0, y1 - y0
    q = math.hypot(dx, dy)
    hgt = math.sqrt(max(r * r - (q / 2) ** 2, 0))
    # Centro a la izquierda o derecha de la cuerda según el sentido del barrido.
    sgn = 1 if sweep else -1
    ccx = mx - sgn * hgt * dy / q
    ccy = my + sgn * hgt * dx / q
    a0 = math.atan2(y0 - ccy, x0 - ccx)
    a1 = math.atan2(y1 - ccy, x1 - ccx)
    da = a1 - a0
    if sweep and da < 0:
        da += 2 * math.pi
    if not sweep and da > 0:
        da -= 2 * math.pi
    return [(ccx + r * math.cos(a0 + da * k / steps), ccy + r * math.sin(a0 + da * k / steps))
            for k in range(1, steps + 1)]


def polylines(d):
    toks = re.findall(r'[MVHA]|-?\d+(?:\.\d+)?', d)
    lines, cur, x, y, i = [], None, 0.0, 0.0, 0
    while i < len(toks):
        c = toks[i]; i += 1
        if c == 'M':
            x, y = float(toks[i]), float(toks[i + 1]); i += 2
            cur = [(x, y)]; lines.append(cur)
        elif c == 'V':
            y = float(toks[i]); i += 1; cur.append((x, y))
        elif c == 'H':
            x = float(toks[i]); i += 1; cur.append((x, y))
        elif c == 'A':
            r, _ry, _rot, large, sweep, nx, ny = (float(v) for v in toks[i:i + 7]); i += 7
            assert large == 0, 'arco grande no soportado'
            cur.extend(arc_points(x, y, r, int(sweep), nx, ny))
            x, y = nx, ny
        else:
            raise ValueError(c)
    return lines


def render(v):
    from PIL import Image, ImageDraw
    vb, stroke, d, dot = parse_wordmark()
    k = 4  # supermuestreo
    sc = MARK_W / vb[2] * k
    ox = (OG_W * k - vb[2] * sc) / 2 - vb[0] * sc
    oy = (OG_H * k - vb[3] * sc) / 2 - vb[1] * sc
    img = Image.new('RGB', (OG_W * k, OG_H * k), v['bg'])
    dr = ImageDraw.Draw(img)
    rad = stroke / 2 * sc
    for line in polylines(d):
        pts = [(ox + px * sc, oy + py * sc) for px, py in line]
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            n = max(1, int(math.hypot(x1 - x0, y1 - y0) / (rad / 4)))
            for j in range(n + 1):
                cx = x0 + (x1 - x0) * j / n
                cy = y0 + (y1 - y0) * j / n
                dr.ellipse([cx - rad, cy - rad, cx + rad, cy + rad], fill=v['fg'])
    cx, cy, cr = ox + dot[0] * sc, oy + dot[1] * sc, dot[2] * sc
    dr.ellipse([cx - cr, cy - cr, cx + cr, cy + cr], fill=v['fg'])
    return img.resize((OG_W, OG_H), Image.LANCZOS)


def main(out):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    for name, v in VARIANTS.items():
        render(v).save(out / f'{name}.png', optimize=True)


if __name__ == '__main__':
    main(sys.argv[1])
