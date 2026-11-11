# Genera el ícono de Tintum (la «t» del wordmark en un cuadrado redondeado) en
# SVG y sus favicons en PNG e ICO. La misma geometría alimenta las dos salidas:
# el SVG con trazos y el PNG dibujando ese trazo con Pillow, que es la única
# dependencia (para los PNG e ICO).
#
# Uso: python3 -I assets/tintum/build_icon.py assets/tintum/icon
# Revisión aprobada el 2026-11-11 (VCX-D061): trazo 21, radio de la curva 17.
import math
import sys
from pathlib import Path

BURGUNDY = '#7B2335'
DEEP = '#5E1B26'
CREAM = '#F4EDE0'

# Lienzo 100 × 100, radio de esquina 22.
SIZE = 100
CORNER = 22

# La «t» del ícono: la misma forma que la del wordmark (fuste, curva hacia la
# derecha, cola corta y travesaño), con proporciones propias para un trazo más
# grueso, como la «t» de las láminas, que aguante a 16 px. Unidades del ícono,
# con el fuste en x=0 antes de centrar.
W = 21          # trazo
TOP = -30       # arranque del fuste
BAR_Y = -11     # altura del travesaño
BAR_L, BAR_R = -15, 15
BASE = 30       # línea central de la base
R = 17          # radio de la curva inferior
TAIL = 19       # fin de la cola a la derecha del fuste
LEFT, RIGHT = BAR_L, max(BAR_R, TAIL)
CX = 50 - (LEFT + RIGHT) / 2
CY = 50 - (TOP + BASE) / 2


def p(x, y):
    return (CX + x, CY + y)


def t_segments():
    """La «t» como polilíneas densas, para dibujarla con trazo redondo."""
    stem = [p(0, TOP), p(0, BASE - R)]
    arc = []
    for k in range(0, 33):
        a = math.pi - (math.pi / 2) * k / 32  # de 180° a 90°: abajo a la derecha
        arc.append(p(R + R * math.cos(a), BASE - R + R * math.sin(a)))
    tail = [p(R, BASE), p(TAIL, BASE)] if TAIL > R else []
    bar = [p(BAR_L, BAR_Y), p(BAR_R, BAR_Y)]
    return [stem + arc + tail, bar]


def t_path_d():
    f = lambda v: ('%g' % round(v, 2))
    x0, y0 = p(0, TOP)
    _, y1 = p(0, BASE - R)
    xe, ye = p(R, BASE)
    xt, _ = p(TAIL, BASE)
    bx0, by = p(BAR_L, BAR_Y)
    bx1, _ = p(BAR_R, BAR_Y)
    tail = f' H{f(xt)}' if TAIL > R else ''
    return (f'M{f(x0)},{f(y0)} V{f(y1)} A{R} {R} 0 0 0 {f(xe)},{f(ye)}{tail} '
            f'M{f(bx0)},{f(by)} H{f(bx1)}')


VARIANTS = {
    # Opción 2: cuadrado burdeos, «t» crema. Base de los favicons.
    'tintum-icon': {'bg': BURGUNDY, 'fg': CREAM, 'accent': False},
    # Opción 3: cuadrado crema, «t» burdeos y el acento redondo arriba a la derecha.
    'tintum-icon-cream': {'bg': CREAM, 'fg': DEEP, 'accent': True},
}
ACCENT = (79, 21, 6)  # cx, cy, r


def svg(v):
    accent = (f'\n  <circle cx="{ACCENT[0]}" cy="{ACCENT[1]}" r="{ACCENT[2]}" fill="{v["fg"]}"/>'
              if v['accent'] else '')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SIZE} {SIZE}" role="img" aria-label="tintum">\n'
            f'  <title>tintum</title>\n'
            f'  <rect width="{SIZE}" height="{SIZE}" rx="{CORNER}" fill="{v["bg"]}"/>\n'
            f'  <path d="{t_path_d()}" fill="none" stroke="{v["fg"]}" stroke-width="{"%g" % round(W, 2)}" '
            f'stroke-linecap="round" stroke-linejoin="round"/>{accent}\n'
            f'</svg>\n')


def png(v, px):
    from PIL import Image, ImageDraw
    k = 8  # supermuestreo
    big = px * k
    sc = big / SIZE
    img = Image.new('RGBA', (big, big), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, big - 1, big - 1], radius=CORNER * sc, fill=v['bg'])
    r = W / 2 * sc
    for seg in t_segments():
        pts = [(x * sc, y * sc) for x, y in seg]
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            n = max(1, int(math.hypot(x1 - x0, y1 - y0) / (r / 4)))
            for i in range(n + 1):
                x = x0 + (x1 - x0) * i / n
                y = y0 + (y1 - y0) * i / n
                d.ellipse([x - r, y - r, x + r, y + r], fill=v['fg'])
    if v['accent']:
        cx, cy, ar = (c * sc for c in ACCENT)
        d.ellipse([cx - ar, cy - ar, cx + ar, cy + ar], fill=v['fg'])
    return img.resize((px, px), Image.LANCZOS)


def main(out):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    for name, v in VARIANTS.items():
        (out / f'{name}.svg').write_text(svg(v))
    base = VARIANTS['tintum-icon']
    for px, name in [(16, 'favicon-16.png'), (32, 'favicon-32.png'), (48, 'favicon-48.png'),
                     (180, 'apple-touch-icon.png'), (192, 'icon-192.png'), (512, 'icon-512.png')]:
        png(base, px).save(out / name, optimize=True)
    png(base, 256).save(out / 'favicon.ico', sizes=[(16, 16), (32, 32), (48, 48)])


if __name__ == '__main__':
    main(sys.argv[1])
