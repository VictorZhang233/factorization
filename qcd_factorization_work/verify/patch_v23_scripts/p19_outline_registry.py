import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import src
import regtable
TARGET = 'FINAL_OUTLINE_v2.md'
STMT = ('def', 'asm', 'thm', 'lem', 'prop', 'cor', 'conj', 'rem', 'ex')

def tagstr(s):
    if s['pfx'] == 'asm':
        return '—' if s['tag'] is None else '[%s]' % s['tag']
    if s['tag'] == 'R':
        return '[R, %s]' % s['qual']
    if s['tag']:
        return '[%s]' % s['tag']
    return '(数学，无标签)' if s['qual'] == 'math' else '(no tag)'

def regen_units(t):
    ST = regtable.chk.parse(t)
    lines = t.split('\n')
    i08 = next(i for i, l in enumerate(lines) if l.startswith('## 08 Label registry'))
    for unit in ('AppM', 'AppN', 'AppO'):
        h = next(i for i in range(i08, len(lines)) if lines[i].strip() == '### ' + unit)
        a = h + 1
        while not lines[a].startswith('| label |'):
            a += 1
        b = a + 2
        while b < len(lines) and lines[b].startswith('|'):
            b += 1
        other = []
        for l in lines[a + 2:b]:
            m = re.match(r'^\|\s*`([a-z]+):', l)
            if m and m.group(1) not in STMT:
                other.append(l)
        new = []
        for s in ST:
            if s['unit'] == unit:
                title = s['title'].replace('|', '\\vert ')
                new.append('| `%s` | %s | %s | %s |' % (s['label'], s['pfx'], tagstr(s), title))
        lines[a + 2:b] = new + other
    return '\n'.join(lines)

def regen_register(t):
    table, total, rows = regtable.build(t)
    lines = t.split('\n')
    i08 = next(i for i, l in enumerate(lines) if l.startswith('## 08 Label registry'))
    h = next(i for i in range(i08, len(lines)) if lines[i].strip() == '### Assumptions')
    a = h + 1
    while not lines[a].startswith('| label | owner |'):
        a += 1
    b = a
    while b < len(lines) and lines[b].startswith('|'):
        b += 1
    tl = next(i for i in range(b, len(lines)) if lines[i].startswith('Total:'))
    lines[a:b] = table.split('\n')
    tl = next(i for i in range(a, len(lines)) if lines[i].startswith('Total:'))
    lines[tl] = total
    return '\n'.join(lines)

OPS = [
 ('func', regen_units),
 ('sub', 'The register of numbered assumptions (41 entries; = `ASSUMPTIONS.md` v2.2 §1).', 'The register of numbered assumptions (47 entries; = `ASSUMPTIONS.md` v2.3 §1; the six entries added by the verify patch: `asm:appM-oswi`, `asm:appN-lce`, `asm:appN-analytic-reg`, `asm:appO-adjacent-swap`, `asm:appO-real-jets`, `asm:appO-collinear-ends`).', 'The register of numbered assumptions (41 entries'),
 ('func', regen_register),
]
