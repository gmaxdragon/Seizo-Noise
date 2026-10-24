#!/usr/bin/env python3
from pathlib import Path
import hashlib,json
r=Path(__file__).resolve().parent
hashes=json.loads((r/'RELEASE_HOLD_MANIFEST.json').read_text())['checksums_sha256']
for name,expected in hashes.items():
    p=r/name
    if not p.is_file(): continue # additional optional artifacts are in complete zip
    actual=hashlib.sha256(p.read_bytes()).hexdigest()
    if actual!=expected: raise SystemExit(f'FAIL: {name} sha256 mismatch')
for name in ('Seizo_Noise_v2.kicad_pcb','Seizo_Noise_v2.kicad_pro','Seizo_Noise_v2.kicad_sch','fp-lib-table','sym-lib-table','Seizo_V2_Symbols.kicad_sym'):
    if not (r/name).is_file(): raise SystemExit(f'FAIL: {name} missing')
print('PASS: packaged source file checksums. Does NOT validate KiCad ERC/DRC or hardware.')
