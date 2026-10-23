"""One-time import of the reviewed project; never fabricates build/test evidence."""
from pathlib import Path, PurePosixPath
import base64, csv, hashlib, io, json, os, re, shutil, tarfile, urllib.request
from concurrent.futures import ThreadPoolExecutor
from decimal import Decimal

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ['PUBLISH_DIR']).resolve()
PARTS = [
 '7ceceded9fb5786a7ab90cd298c134de5e3cb685a1350ff666e1c49f2cee209c',
 '34d338d0286a1a687a7fd460f85d7ed78d2a042e3d9c0092fe12d052489bc4b2',
 '164cb92a62b6ec57a8f21f4f7e5fb6ccd87b7cecf79311ea6803bc5a53aec491',
 '43b7501c5e3404a33eb346c144317d02276941ae0482ee0824f4edb39ff0b692',
 '51d3dce0065a855c6a6df4c019bc0df9199b1175f1c1af48285f99c670f3216b',
]

def digest(data):
    return hashlib.sha256(data).hexdigest()

def fetch(url, target, expected=None):
    target = Path(target)
    req = urllib.request.Request(url, headers={'User-Agent': 'Seizo-Noise-project-import'})
    with urllib.request.urlopen(req, timeout=75) as response:
        data = response.read()
    if expected and digest(data) != expected:
        raise RuntimeError(f'File integrity mismatch: {target}')
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    return data

chunks = []
errors = []
for i, expected in enumerate(PARTS):
    data = ''.join((HERE / f'part-{i:02}.b64').read_text().split()).encode('ascii')
    actual = digest(data)
    print(f'CHUNK {i}: {len(data)} characters sha256={actual}', flush=True)
    if actual != expected:
        errors.append(i)
    chunks.append(data)
if errors:
    raise RuntimeError(f'Transfer integrity failed for chunks {errors}; no publication performed')
archive = base64.b64decode(b''.join(chunks), validate=True)
assert digest(archive) == '0032a841642361731a5c5e186989e2409f63c4f686f222033bbc06c33e816586'
with tarfile.open(fileobj=io.BytesIO(archive), mode='r:xz') as tar:
    for member in tar.getmembers():
        path = PurePosixPath(member.name)
        if path.is_absolute() or '..' in path.parts or not member.isfile():
            raise RuntimeError(f'Unexpected archive entry {member.name}')
        if path.parts[0] not in {'hardware', 'docs', 'cad'}:
            raise RuntimeError(f'Unexpected destination {member.name}')
        target = OUT / str(path)
        if target.exists():
            raise RuntimeError(f'Refusing to overwrite existing project file: {path}')
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(tar.extractfile(member).read())
print('All 68 project source files extracted with matching archive checksum', flush=True)

images = [
 ('pcb-layout.png', 'https://d2ol7oe51mr4n9.cloudfront.net/user_3Exj9bDHoXP3JuENaws4UF74BKT/ccd3d291-66b6-4433-a990-394d85e70458.png', '8fd07b58eba08c19f70c2f31cfaf22b978fa4ca88a47454426f949fc62775a49'),
 ('pcb-3d.png', 'https://d2ol7oe51mr4n9.cloudfront.net/user_3Exj9bDHoXP3JuENaws4UF74BKT/9f8a716a-072b-45ce-ad91-242fde11f69f.png', '7e27222d63a69afdfe9d34fb11cb1bce1ca48406ab6488a602bfd6bb532eecc3'),
]
for filename, url, checksum in images:
    data = fetch(url, OUT / 'images' / filename, checksum)
    assert data.startswith(b'\x89PNG\r\n\x1a\n')

# Download the published reference models, not regenerated project evidence.
models = json.loads((OUT / 'docs/kicad_model_sources.json').read_text())
models.append({'path': 'Seizo_Mechanical/Pololu_D24V10F3.step', 'url': 'https://www.pololu.com/file/0J1375/pololu-1a-step-down-voltage-regulator-d24v10fx.step'})

def get_model(item):
    target = OUT / 'hardware/models' / item['path']
    data = fetch(item['url'], target)
    if b'ISO-10303-21' not in data[:300]:
        raise RuntimeError(f'Not a STEP model: {item["path"]}')
    return {'path': item['path'], 'url': item['url'], 'sha256': digest(data), 'bytes': len(data)}

with ThreadPoolExecutor(max_workers=5) as pool:
    model_results = list(pool.map(get_model, models))
(OUT / 'docs/model-download-manifest.json').write_text(json.dumps(model_results, indent=2) + '\n')

# Preserve the root BOM as requested. This snapshot is protected from the
# platform's documented overwriting of root BOM.csv during sync.
purchase = OUT / 'purchasing'
purchase.mkdir(exist_ok=True)
shutil.copyfile(OUT / 'BOM.csv', purchase / 'BOM_engineering.csv')
rows = list(csv.DictReader((OUT / 'BOM.csv').open(newline='')))
priced = [r for r in rows if r.get('Total Cost', '').strip()]
subtotal = sum((Decimal(r['Total Cost'].replace('$', '').replace(',', '')) for r in priced), Decimal('0'))
(purchase / 'BOM_status.json').write_text(json.dumps({
    'source': 'BOM.csv as read immediately before this publication',
    'priced_rows': len(priced), 'recorded_priced_subtotal_usd': str(subtotal),
    'full_project_total_known': False, 'tier_2_limit_usd_from_user_page': '65.00',
    'current_supplier_prices_rechecked': False,
    'platform_bom_updated': False,
}, indent=2) + '\n')

# Only the image/technical-file sections change. All six approved personal
# sections and the existing BOM table remain byte-for-byte unchanged.
readme = OUT / 'README.md'
old = readme.read_text()
assert old.count('## Project screenshots') == 1
assert old.count('## Hardware reference') == 1
prefix, rest = old.split('## Project screenshots', 1)
_, hardware = rest.split('## Hardware reference', 1)
section = '''## Project screenshots

![PCB layout screenshot supplied by the project owner](images/pcb-layout.png)

![3D PCB view supplied by the project owner](images/pcb-3d.png)

These are the owner's CAD screenshots, not photos of assembled hardware. The layout screenshot includes an earlier review-stage label; the editable design files below are Seizo Audio v1.0.

## Design files

| File | Link |
| --- | --- |
| KiCad schematic | [speakerpcb.kicad_sch](hardware/speakerpcb.kicad_sch) |
| PCB layout | [speakerpcb.kicad_pcb](hardware/speakerpcb.kicad_pcb) |
| Complete KiCad project | [speakerpcb.kicad_pro](hardware/speakerpcb.kicad_pro) |
| Board rules | [speakerpcb.kicad_dru](hardware/speakerpcb.kicad_dru) |
| Included footprints | [Seizo_Audio.pretty](hardware/Seizo_Audio.pretty) |
| Included symbols | [Seizo_Audio.kicad_sym](hardware/Seizo_Audio.kicad_sym) |
| Assembly instructions | [Assembly.md](docs/Assembly.md) |
| Connector pin maps | [Connections.md](docs/Connections.md) |
| Native schematic check | [ERC.rpt](validation/ERC.rpt) |
| Native board and schematic-parity check | [DRC.rpt](validation/DRC.rpt) |
| Gerbers and drills | [Seizo_Audio_Gerbers.zip](fabrication/Seizo_Audio_Gerbers.zip) |

Download the complete repository and open `hardware/speakerpcb.kicad_pro`. Keep the local symbol, footprint, and model folders with it. The native ERC and DRC reports were rerun during this publication, including copper refill and schematic-to-PCB comparison. These CAD checks do not replace assembly inspection or physical power/audio testing. Firmware has not been added just to satisfy the optional repository recommendation.

## Hardware reference'''
new = prefix + section + hardware
outdated = '- Technical BOM basis: `Seizo_Audio_Design_v1.zip`, produced earlier in the project. This update adds documentation and image links; it does not upload or modify the KiCad design files.'
replacement = '- The schematic, PCB, libraries and design records are now available under `hardware/`, `docs/` and `validation/`. Import provenance is recorded in [import_provenance.json](docs/import_provenance.json). [purchasing/BOM_engineering.csv](purchasing/BOM_engineering.csv) preserves the engineering BOM independently of platform sync; unpriced items remain unresolved.'
new = new.replace(outdated, replacement)
assert new.split('## Project screenshots', 1)[0] == prefix
# Narrative and BOM integrity evidence saved for review.
old_bom = old.split('## Bill of materials', 1)[1].split('## Sources and records', 1)[0]
new_bom = new.split('## Bill of materials', 1)[1].split('## Sources and records', 1)[0]
assert old_bom == new_bom
readme.write_text(new)
(OUT / 'docs/publication-integrity.json').write_text(json.dumps({
    'approved_narrative_sha256': digest(prefix.encode()),
    'bom_table_sha256': digest(old_bom.encode()),
    'root_bom_sha256': digest((OUT / 'BOM.csv').read_bytes()),
    'journal_sha256': digest((OUT / 'JOURNAL.md').read_bytes()),
    'images': [{'path': 'images/' + name, 'sha256': sha} for name, _, sha in images],
    'electrical_design_changed': False,
    'imported_archive_sha256': digest(archive),
}, indent=2) + '\n')
print(f'Preserved approved writing and BOM; {len(priced)} priced rows total ${subtotal}', flush=True)
