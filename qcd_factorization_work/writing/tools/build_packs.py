#!/usr/bin/env python3
"""Build one context pack per writer (writing/packs/Wnn/PACK.md + figblocks.tex).
Everything is extracted verbatim from the binding spec files; the pack is a convenience
index, the spec files remain binding."""
import os, re, sys, json
W = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
S = os.path.join(W, 'spec_v2')
OUT = os.path.join(W, 'writing', 'packs')
outline = open(os.path.join(S, 'FINAL_OUTLINE_v2.md')).read().split('\n')
vf = open(os.path.join(S, 'VERIFIED_FORMULAS_v2.md')).read().split('\n')
asmf = open(os.path.join(S, 'ASSUMPTIONS.md')).read().split('\n')
figidx = open(os.path.join(S, 'FIGURES_INDEX_v2.md')).read().split('\n')
figstat = open(os.path.join(W, 'figures', 'FIGURES_STATUS.md')).read().split('\n')
refsn = open(os.path.join(S, 'REFS_NOTES_v2.md')).read().split('\n')

WRITERS = {
 'W01': ['front', 'Ch01'], 'W02': ['Ch02', 'AppJ'], 'W03': ['Ch03', 'AppA', 'AppI'],
 'W04': ['Ch04', 'AppD', 'AppE'], 'W05': ['Ch05', 'AppB'], 'W06': ['Ch06', 'AppC'],
 'W07': ['Ch07'], 'W08': ['AppM'], 'W09': ['Ch08', 'AppK', 'AppL'], 'W10': ['Ch09', 'AppF'],
 'W11': ['AppN'], 'W12': ['Ch10'], 'W13': ['Ch11'], 'W14': ['Ch12'], 'W15': ['AppO'],
 'W16': ['Ch13'], 'W17': ['Ch14'], 'W18': ['Ch15'], 'W19': ['Ch16'], 'W20': ['Ch17'],
 'W21': ['Ch18'], 'W22': ['Ch19'], 'W23': ['Ch20'], 'W24': ['Ch21'], 'W25': ['Ch22'],
 'W26': ['Ch23'], 'W27': ['Ch24'], 'W28': ['Ch25', 'AppP'], 'W29': ['AppG', 'AppH'], 'W30': ['AppQ'],
}

# ---- outline sections (## headings)
heads = [i for i, l in enumerate(outline) if l.startswith('## ')]
def section(i):
    k = heads.index(i); j = heads[k + 1] if k + 1 < len(heads) else len(outline)
    return outline[i:j]
def find_head(pred):
    for i in heads:
        if pred(outline[i]): return i
    raise KeyError
def unit_head(u):
    if u == 'front': return find_head(lambda l: l.startswith('## Front matter'))
    if u.startswith('Ch'):
        n = int(u[2:]); return find_head(lambda l: re.match(r'## Chapter %d —' % n, l))
    if u.startswith('App'):
        x = u[3:]; return find_head(lambda l: l.startswith('## Appendix %s —' % x))
G0 = find_head(lambda l: l.startswith('## 0. Global decisions'))
GVII = find_head(lambda l: l.startswith('## Part VII'))
FVII = [find_head(lambda l, p=p: l.startswith(p)) for p in ('## F1.', '## F4.', '## F5.', '## F6.')]
GMQ = find_head(lambda l: l.startswith('## Global rules for the appendices M'))
REG = find_head(lambda l: l.startswith('## 08 Label registry'))
MST = find_head(lambda l: l.startswith('## 09 Master-table'))

# ---- registry
reg_lines = section(REG)
owner, regrow, unit_rows = {}, {}, {}
cur = None
for l in reg_lines:
    m = re.match(r'### (\S+)', l)
    if m: cur = m.group(1); unit_rows[cur] = []; continue
    m = re.match(r'\| `([^`]+)` \|', l)
    if m and cur:
        owner.setdefault(m.group(1), cur); regrow.setdefault(m.group(1), l); unit_rows[cur].append(l)
def unit_reg_block(u):
    out, on = [], False
    for l in reg_lines:
        if l.startswith('### '):
            on = (l.strip() == '### ' + u)
        if on: out.append(l)
    return out

LAB = re.compile(r'\b(?:def|thm|lem|prop|cor|conj|rem|ex|asm|sec|fig|tab|eq|ch|app):[A-Za-z0-9][A-Za-z0-9\-]*')
VFID = re.compile(r'\bVF-[A-Z]+-\d+[a-z]?\b')
KEY = re.compile(r'\\cite[tp]?\*?(?:\[[^\]]*\])?\{([^}]+)\}|`([A-Z][A-Za-z\-]+:?\d{4}[a-z]{0,3})`|\b([A-Z][A-Za-z\-]+:\d{4}[a-z]{2,3})\b')

# ---- VF entries
vf_entry = {}
cur = None
for l in vf:
    m = re.match(r'### (VF-[A-Z]+-\d+[a-z]?)\b', l)
    if m: cur = m.group(1); vf_entry[cur] = [l]; continue
    if l.startswith('## ') or l.startswith('# '): cur = None; continue
    if cur: vf_entry[cur].append(l)
# ---- assumptions
asm_entry = {}
cur = None
for l in asmf:
    m = re.match(r'#### `(asm:[^`]+)`', l)
    if m: cur = m.group(1); asm_entry[cur] = [l]; continue
    if l.startswith('### ') or l.startswith('## '): cur = None; continue
    if cur: asm_entry[cur].append(l)
# ---- figure status rows
fig_status = {}
for l in figstat:
    m = re.match(r'\| `(fig:[^`]+)` \|', l)
    if m: fig_status[m.group(1)] = l
def fig_block(label):
    row = fig_status.get(label, '')
    m = re.search(r'`([^`]+\.tex)`:(\d+)', row)
    if not m: return None, None
    path = os.path.join(W, m.group(1))
    if not os.path.exists(path): return m.group(1), None
    txt = open(path).read().split('\n')
    beg = None
    for i, l in enumerate(txt):
        if re.match(r'%%% BEGIN ' + re.escape(label) + r'\s*$', l.strip()) or l.strip() == '%%% BEGIN ' + label:
            beg = i; break
    if beg is None: return m.group(1), None
    for j in range(beg, len(txt)):
        if txt[j].strip() == '%%% END ' + label:
            return m.group(1), '\n'.join(txt[beg:j + 1])
    return m.group(1), None
def figidx_paras(label):
    out = []
    for i, l in enumerate(figidx):
        if label in l and not l.startswith('|---'):
            out.append(l)
    return out

def mst_rows(labels):
    out = []
    for l in section(MST):
        if l.startswith('| ') and any('`%s`' % x in l for x in labels): out.append(l)
    return out

stats = {}
ONLY = set(sys.argv[1:])
for wid, units in WRITERS.items():
    if ONLY and wid not in ONLY: continue
    d = os.path.join(OUT, wid); os.makedirs(d, exist_ok=True)
    P = []
    P.append(f'# Context pack {wid} — units: {", ".join(units)}\n')
    P.append('Generated by writing/tools/build_packs.py from spec v2.3.1. **Convenience extract only; the spec files in spec_v2/ remain binding** (order of authority: lead-author decisions (writing/LEAD_DECISIONS.md) > WRITER_SPEC_v2 > FINAL_OUTLINE_v2 > VERIFIED_FORMULAS_v2 > ...). If something seems missing here, grep the full files.\n')
    body_lines = []
    P.append('\n\n# PART 1 — Your unit section(s) of FINAL_OUTLINE_v2 (verbatim)\n')
    for u in units:
        sec = section(unit_head(u)); body_lines += sec
        P.append('\n'.join(sec))
    if any(u in ('Ch22', 'Ch23', 'Ch24') for u in units):
        P.append('\n\n# PART 1b — Part VII global decisions and annexes F1/F4/F5/F6 (verbatim)\n')
        for h in [GVII] + FVII:
            sec = section(h); body_lines += sec; P.append('\n'.join(sec))
    if any(u in ('AppM', 'AppN', 'AppO', 'AppP', 'AppQ') for u in units):
        P.append('\n\n# PART 1c — Global rules for the appendices M–Q (verbatim)\n')
        sec = section(GMQ); body_lines += sec; P.append('\n'.join(sec))
    body = '\n'.join(body_lines)
    P.append('\n\n# PART 2 — Registry blocks of your unit(s) (§08; labels you OWN)\n')
    own = set()
    for u in units:
        blk = unit_reg_block(u); P.append('\n'.join(blk))
        for l in blk:
            m = re.match(r'\| `([^`]+)` \|', l)
            if m: own.add(m.group(1))
    labels = sorted(set(LAB.findall(body)))
    ext = [x for x in labels if x not in own]
    P.append('\n\n# PART 3 — External labels mentioned in your section(s) (owner unit + registry row)\n')
    P.append('| label | owner | registry row |\n|---|---|---|')
    unknown = []
    for x in ext:
        if x in owner: P.append(f'| `{x}` | {owner[x]} | {regrow[x]} |')
        else: unknown.append(x)
    if unknown:
        P.append('\nLabels mentioned but not in the registry (equation labels, withdrawn slot names, reserved/optional labels or text references — never define them unless your section says so; check §10 of the outline):\n' + ', '.join('`%s`' % x for x in unknown))
    P.append('\n\n# PART 4 — Assumption register entries used (ASSUMPTIONS.md §3, verbatim)\n')
    asms = sorted({x for x in labels if x.startswith('asm:')})
    for a in asms:
        if a in asm_entry: P.append('\n'.join(asm_entry[a]))
        else: P.append(f'#### `{a}` — (no full entry found in ASSUMPTIONS.md; see FINAL_OUTLINE_v2 owner entry)')
    P.append('\n\n# PART 5 — VERIFIED_FORMULAS_v2 entries referenced (verbatim)\n')
    vfs = sorted(set(VFID.findall(body)), key=lambda s: (s.split('-')[1], int(re.sub(r'\D', '', s.split('-')[2]) or 0), s))
    missing_vf = []
    for v in vfs:
        if v in vf_entry: P.append('\n'.join(vf_entry[v]))
        else: missing_vf.append(v)
    if missing_vf: P.append('\nVF IDs mentioned but without a `### VF-…` heading (grep VERIFIED_FORMULAS_v2.md; some are sub-items): ' + ', '.join(missing_vf))
    P.append('\n\n# PART 6 — Figures you OWN (status row, index description lines, source block location)\n')
    figs = sorted(x for x in own if x.startswith('fig:'))
    FB = []
    for f in figs:
        P.append(f'\n## `{f}`\n- status: {fig_status.get(f, "(no status row)")}')
        for l in figidx_paras(f)[:12]: P.append('- index: ' + l[:3000])
        src, blk = fig_block(f)
        if blk: FB.append(blk); P.append(f'- block extracted verbatim into `writing/packs/{wid}/figblocks.tex` (source `{src}`)')
        else: P.append(f'- block NOT extracted (source {src}); follow FIGURES_INDEX_v2 §0 (generated or optional/not drawn → placeholder protocol or omit optional)')
    open(os.path.join(d, 'figblocks.tex'), 'w').write('\n\n'.join(FB) + '\n')
    P.append('\n\n# PART 7 — Master-table rows (§09) that name your labels\n')
    P.append('\n'.join(mst_rows(own)))
    P.append('\n\n# PART 8 — REFS_NOTES_v2 lines mentioning bib keys that occur in your section(s)\n')
    keys = set()
    for m in KEY.finditer(body):
        for g in m.groups():
            if g:
                for k in g.split(','): keys.add(k.strip())
    rl = []
    for l in refsn:
        if any(k and k in l for k in keys): rl.append(l)
    P.append('\n'.join(rl[:600]))
    txt = '\n'.join(P)
    open(os.path.join(d, 'PACK.md'), 'w').write(txt)
    stats[wid] = dict(units=units, kb=round(len(txt.encode()) / 1024, 1), own=len(own), ext=len(ext), vf=len(vfs), asm=len(asms), figs=len(figs), figblocks=len(FB))
if not ONLY: json.dump(stats, open(os.path.join(OUT, 'PACKS_STATS.json'), 'w'), indent=1)
for k, v in stats.items(): print(k, v)
