# Genera el wordmark vectorial de Tintum (tintum-wordmark.svg): letras
# monolínea con terminaciones redondas, dibujadas sobre la estructura de las
# láminas aceptadas. Sin dependencias.
#
# Uso: python3 -I assets/tintum/build_wordmark.py <trazo> <espaciado> <salida>
# Revisión aprobada el 2026-11-11 (VCX-D061): trazo 19, espaciado 10.
import sys
w=float(sys.argv[1]); gap=float(sys.argv[2]); out=sys.argv[3]
h=w/2; X=40; B=100
top=X+h; base=B-h
R=17   # n/u arch centerline radius
r=15   # m arch radius
tr=13  # t tail radius
def fmt(v): return ('%g' % round(v,2))
paths=[]; x=h  # current left outer edge = 0
def t(L):
    x=L+h+11  # stem centerline; crossbar extends 11 left
    paths.extend([f"M{fmt(x)},{fmt(22+h)} V{fmt(base-tr)} A{tr} {tr} 0 0 0 {fmt(x+tr)},{fmt(base)} H{fmt(x+tr+3)}",
                  f"M{fmt(x-11)},{fmt(top)} H{fmt(x+14)}"])
    return x+tr+3+h
def i(L):
    x=L+h; paths.append(f"M{fmt(x)},{fmt(top)} V{fmt(base)}"); dots.append(x); return x+h
def n(L):
    x=L+h; paths.extend([f"M{fmt(x)},{fmt(top)} V{fmt(base)}", f"M{fmt(x)},{fmt(top+R)} A{R} {R} 0 0 1 {fmt(x+2*R)},{fmt(top+R)} V{fmt(base)}"]); return x+2*R+h
def u(L):
    x=L+h; paths.extend([f"M{fmt(x)},{fmt(top)} V{fmt(base-R)} A{R} {R} 0 0 0 {fmt(x+2*R)},{fmt(base-R)}", f"M{fmt(x+2*R)},{fmt(top)} V{fmt(base)}"]); return x+2*R+h
def m(L):
    x=L+h; paths.extend([f"M{fmt(x)},{fmt(top)} V{fmt(base)}", f"M{fmt(x)},{fmt(top+r)} A{r} {r} 0 0 1 {fmt(x+2*r)},{fmt(top+r)} V{fmt(base)}", f"M{fmt(x+2*r)},{fmt(top+r)} A{r} {r} 0 0 1 {fmt(x+4*r)},{fmt(top+r)} V{fmt(base)}"]); return x+4*r+h
dots=[]
L=0
for f,g in ((t,gap),(i,gap),(n,gap-2),(t,gap),(u,gap),(m,0)):
    L=f(L)+g
W=L
dr=h+1.2
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 {fmt(24-dr-2)} {fmt(W)} {fmt(B-(24-dr-2))}" role="img" aria-label="tintum">
  <title>tintum</title>
  <g fill="none" stroke="currentColor" stroke-width="{fmt(w)}" stroke-linecap="round" stroke-linejoin="round">
    <path d="{' '.join(paths)}"/>
  </g>
  <circle cx="{fmt(dots[0])}" cy="24" r="{fmt(dr)}" fill="currentColor"/>
</svg>
'''
open(out,'w').write(svg)
print(svg.split('\n')[0])
