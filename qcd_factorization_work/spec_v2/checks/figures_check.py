"""Consistency check of spec_v2/FIGURES_INDEX_v2.md (run: python3 -I figures_check.py WORKDIR).

1. Parse the per-unit table of Sec. 5 (labels without the 'fig:' prefix).
2. Every label has exactly one owner; count required / optional.
3. The 44 existing labels exist as %%% BEGIN blocks in research/tikz{1,2,3}/figures{1,2,3}.tex.
4. Every `fig:...` label mentioned in the index is in the table (agent-snippet labels and placeholders excepted).
5. Every chapter owns >= 2 required figures, App M/N/O/P >= 1; the 'total required' column is right.
(spec v2.2: expected counts 120 required / 26 optional.)
"""
import re, sys, collections
W = sys.argv[1].rstrip('/') + '/'
t = open(W + 'spec_v2/FIGURES_INDEX_v2.md', encoding='utf-8').read()
sec5 = t[t.index('## 5. Figures per unit'):t.index('## CHANGELOG')]
rows = [l for l in sec5.split('\n') if l.startswith('| ') and not l.startswith('| unit') and not l.startswith('|---') and not l.startswith('| **total')]
owner = {}; req = collections.defaultdict(list); opt = collections.defaultdict(list); probs = []
def labels(cell):
    cell = re.sub(r'\(.*?\)', '', cell)
    return [x.strip() for x in cell.split(',') if x.strip() and x.strip() not in ('—',)]
for r in rows:
    c = [x.strip() for x in r.strip('|').split('|')]
    unit = c[0]
    for col in (1, 2, 3, 4):
        for lab in labels(c[col]):
            if lab in owner: probs.append('duplicate owner for %s: %s and %s' % (lab, owner[lab], unit))
            owner[lab] = unit; req[unit].append(lab)
    for lab in labels(c[5]):
        if lab in owner: probs.append('duplicate owner for %s: %s and %s' % (lab, owner[lab], unit))
        owner[lab] = unit; opt[unit].append(lab)
    try:
        tot = int(c[6])
        if tot != len(req[unit]): probs.append('%s: total column %d but %d required labels' % (unit, tot, len(req[unit])))
    except ValueError:
        pass
nreq = sum(len(v) for v in req.values()); nopt = sum(len(v) for v in opt.values())
print('required labels:', nreq, ' optional labels:', nopt, ' distinct:', len(owner))
existing = []
for fn in ('research/tikz1/figures1.tex', 'research/tikz2/figures2.tex', 'research/tikz3/figures3.tex'):
    s = open(W + fn, encoding='utf-8').read()
    existing += re.findall(r'%%% BEGIN fig:([\w-]+)', s)
print('existing BEGIN blocks:', len(existing))
missing = [e for e in existing if e not in owner]
print('existing labels without owner in Sec. 5:', missing or 'none')
row1 = re.findall(r'^\| \d+ \| `fig:([\w-]+)` \|', t, re.M)
print('Sec. 1 table rows:', len(row1), '; all existing:', sorted(row1) == sorted(existing))
mentioned = set(re.findall(r'`fig:([\w-]+)`', t)) | set(re.findall(r'\\cref\{fig:([\w-]+)\}', t))
ignore = re.compile(r'^(cw-|ee-sw|ee-lo|ee-nlo|ee-2l|dy1l-|dis1l-|cpdf-|cex-|pc-|thrust-|usoft-|nrqcd-decay|nqs-|landau-simplex|scet-modes|b-dpi|qcdf|appE-degree|appP-dependency-b)')
notab = sorted(m for m in mentioned if m not in owner and not ignore.match(m))
print('labels mentioned in the index but not in the Sec. 5 table:', notab or 'none')
few = [u for u in req if (u.startswith('Ch') and len(req[u]) < 2) or (u in ('App M', 'App N', 'App O', 'App P') and len(req[u]) < 1)]
print('units below the target:', few or 'none')
for u in ['Ch%d' % i for i in range(1, 26)] + ['App M', 'App N', 'App O', 'App P']:
    if u not in req: probs.append('unit %s missing in Sec. 5' % u)
print('problems:', probs or 'none')
ok = (nreq == 120 and nopt == 26 and  # v2.2: +7 generated App P per-part graphs, +1 optional fig:lamet-dependency
       not missing and not notab and not few and not probs and len(existing) == 44)
print('RESULT:', 'PASS' if ok else 'FAIL')
