"""Prepara la revisión ciega del caso A.

Copia cada screen.html sin comentarios a blind/<id>/screen.html con un id al azar y guarda
la correspondencia fuera de blind/. Uso: python3 -I blind.py <carpeta A>
"""
import json
import re
import secrets
import sys
from pathlib import Path

base = Path(sys.argv[1])
runs = ["S1", "S2", "S3", "N1", "N2", "N3"]
ids = [f"D{n}" for n in range(1, 7)]
rng = secrets.SystemRandom()
rng.shuffle(ids)
mapping = dict(zip(ids, runs))
blind = base / "blind"
blind.mkdir(exist_ok=False)
for bid, run in mapping.items():
    html = (base / "runs" / run / "screen.html").read_text()
    html = re.sub(r"<!--.*?-->", "", html, flags=re.S)
    html = re.sub(r"/\*.*?\*/", "", html, flags=re.S)
    (blind / bid).mkdir()
    (blind / bid / "screen.html").write_text(html)
(base / "blind-mapping.json").write_text(json.dumps(dict(sorted(mapping.items())), indent=1) + "\n")
print(sorted(mapping))
