"""Release consistency checks, not validation of the reviewed experiments."""
import argparse
from decimal import Decimal as D
import hashlib
import json
from pathlib import Path
import re
import sys

from pypdf import PdfReader
from budget_example import calculate

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def normalized(text):
    return re.sub(r'\s+', '', text)


def pdf_text(path):
    reader = PdfReader(path)
    require(not reader.is_encrypted, 'PDF must be readable')
    texts = [p.extract_text() for p in reader.pages]
    require(all(len(t) > 100 for t in texts), 'Blank or incomplete page')
    require(all('Not peer reviewed' in t for t in texts), 'Missing status footer')
    require(all('\u25a0' not in t and '\ufffd' not in t for t in texts), 'Missing-glyph marker')
    return texts


def verify(rebuild=None):
    refs = json.loads((ROOT / 'references.json').read_text(encoding='utf-8-sig'))
    source = (ROOT / 'manuscript.md').read_text(encoding='utf-8-sig')
    readable = (ROOT / 'paper.md').read_text(encoding='utf-8-sig')
    ids = re.findall(r'\[@([A-Z0-9]+)\]', source)
    unique = list(dict.fromkeys(ids))
    require(len(refs) == len(unique) == 49, 'Expected 49 declared sources')
    require(set(unique) == {r['id'] for r in refs}, 'Reference mismatch')
    require(all(r['url'].startswith('https://') and r['reading_scope'] and r['evidence_type'] for r in refs), 'Incomplete evidence metadata')
    require('[@' not in readable, 'Unresolved citations')
    require('10. Research vision proposed by AnimaFoundry' in source, 'Missing attributed vision')
    require(source.index('10. Research vision') < source.index('## Declarations'), 'Vision order')
    require('not a systematic review' in source and 'No listed experiment is claimed to have been performed' in source, 'Missing scope limits')

    saved = json.loads((ROOT / 'budget_example.json').read_text(encoding='utf-8'))
    require(saved == calculate(), 'Saved calculation differs from implementation')
    # Fixed external arithmetic expectations lock the examples reported in the text.
    expected = [('0.1', '0.10368', '10.368'), ('1', '1.0368', '103.68'), ('10', '10.368', '1036.8')]
    for row, (rate, raw, retained) in zip(saved['traffic'], expected):
        require(D(row['rate_hz']) == D(rate), 'Sampling-rate mismatch')
        require(D(row['raw_TB_per_day_decimal']) == D(raw), 'Raw traffic mismatch')
        require(D(row['ten_percent_payload_GB_per_day']) == D(retained), 'Retained traffic mismatch')
    for key, value in {'hypothetical_training_hours': '96', 'one_hz_retained_joint_samples': '8640000000', 'update_bytes_without_metadata': '500000', 'receive_energy_joules_without_overheads': '.4', 'harvest_seconds_for_receive_only': '40000', 'fleet_unicast_payload_TB_decimal': '.5'}.items():
        require(D(saved[key]) == D(value), 'Budget mismatch: ' + key)
    for text in ['1.0368 TB', '8.64 billion', '345,600 seconds', '96 hours', '0.5 MB', '0.4 J', '40,000 seconds']:
        require(text in source, 'Manuscript/example mismatch: ' + text)

    texts = pdf_text(ROOT / 'paper.pdf')
    body_pages = [re.sub(r'AnimaFoundry \| Review preprint v1\.0\.0 \| Not peer reviewed\s*\d+\s*', '', t) for t in texts]
    whole = normalized('\n'.join(body_pages))
    for heading in re.findall(r'^#{1,3} (.+)$', source, re.M):
        require(normalized(heading) in whole, 'Missing heading in PDF: ' + heading)
    for r in refs:
        require(normalized(r['title']) in whole, 'Missing PDF reference: ' + r['id'])
    # Every prose paragraph (including captions) must survive rendering.
    for block in source.split('\n\n'):
        if not block.strip() or block.lstrip().startswith(('#', '|', '```', '![')):
            continue
        cleaned = re.sub(r'\[@([A-Z0-9]+)\]', lambda m: f'[{unique.index(m.group(1))+1}]', block).replace('**', '')
        require(normalized(cleaned) in whole, 'Missing rendered prose: ' + cleaned[:70])

    manifest = json.loads((ROOT / 'RELEASE_MANIFEST.json').read_text(encoding='utf-8'))
    names = [r['path'] for r in manifest['files']]
    require(len(names) == len(set(names)), 'Duplicate manifest path')
    for row in manifest['files']:
        path = Path(row['path'])
        require(not path.is_absolute() and '..' not in path.parts, 'Unsafe release path')
        data = (ROOT / path).read_bytes()
        require(len(data) == row['bytes'], 'Size mismatch: ' + row['path'])
        require(hashlib.sha256(data).hexdigest() == row['sha256'], 'Hash mismatch: ' + row['path'])
    require(all(x in names for x in ['paper.pdf','paper.md','manuscript.md','references.json','METHODS.md','LICENSE-TEXT','LICENSE-CODE']), 'Incomplete release allowlist')

    if rebuild:
        for path in ['paper.md', 'figures/architecture.svg']:
            require((ROOT / path).read_bytes() == (rebuild / path).read_bytes(), 'Rebuild differs: ' + path)
        rebuilt = pdf_text(rebuild / 'paper.pdf')
        require(texts == rebuilt, 'Rebuilt PDF text or page boundaries differ')
    return {'status': 'PASS', 'sources': len(refs), 'pages': len(texts), 'manifest_files': len(names), 'rebuild_checked': bool(rebuild), 'scope': 'document and arithmetic consistency; no empirical replication'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--rebuild', type=Path)
    try:
        print(json.dumps(verify(parser.parse_args().rebuild), indent=2))
    except (ValueError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
