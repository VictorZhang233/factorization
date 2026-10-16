import re, os
W = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(W, '..', '..', '..'))
rn = open(os.path.join(ROOT, 'spec_v2', 'REFS_NOTES_v2.md'), encoding='utf-8').read().split('\n')
pack = open(os.path.join(ROOT, 'writing', 'packs', 'W27', 'PACK.md'), encoding='utf-8').read()
i = pack.index('### Key citation keys (Ch24)'); j = pack.index('### Verification outcomes (Ch24')
keys = sorted(set(re.findall(r'`([A-Za-z][A-Za-z0-9:\-_]+)`', pack[i:j])) | {'Braun:2019qtp','Muhlbauer:2020kut'})
out = []
for k in keys:
    rows = [l for l in rn if l.startswith('| `%s`' % k)]
    if rows:
        cells = [c.strip() for c in rows[0].split('|')]
        # columns: '', key, authors, journal, title, sections, depth, preprint, ''
        depth = cells[6] if len(cells) > 7 else '?'
        pre = cells[7] if len(cells) > 8 else ''
        out.append((k, depth, pre))
    else:
        out.append((k, '(no §4 row: v1 key or not listed)', ''))
for k, d, p in out:
    print(f'{k:32s} {d:30s} {p}')
