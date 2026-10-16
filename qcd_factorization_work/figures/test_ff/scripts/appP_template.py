r"""Prototype of the App P dependency-graph generator (FIGURES_INDEX_v2 Sec. 4.9), used for the TEMPLATE
fig:appP-dependency of figure set F.  Python 3 standard library only.

    python3 -I appP_template.py outline.json out.tex

Input: outline.json written by outline_data.py (statements, \uses, tags, register, master-table rows).
Node selection: the fixed list SEL below (a Drell--Yan/TMD slice of the skeleton).  Edges: transitive
reduction of the reachability relation of the full \uses graph restricted to SEL; asm -> R_cond edges are
never removed; for the [A] process theorems PROC the edges from their master-table bottleneck assumptions
are kept and drawn thick red.  Layout: one layer per unit (book order), sub-columns by longest-path depth
inside the unit, vertical order by two barycentre sweeps (book order for ties), node separation >= 0.25 cm.
Output: plain TikZ (\node ... at (x,y) {...}; \draw ...), styles of Sec. 4.9 rules 3-5.
"""
import sys, json, re, collections

UNITS = ['front'] + ['Ch%02d' % i for i in range(1, 26)] + ['App' + c for c in 'ABCDEFGHIJKLMNOPQ']
UI = {u: i for i, u in enumerate(UNITS)}
SEL = ['asm:intro-bridge',
       'prop:method-fsi', 'prop:method-glauber-deformation', 'thm:method-template',
       'thm:dy-factorization', 'conj:dy-coloured-final',
       'asm:appN-collins', 'asm:appN-cutsum', 'thm:appN-subtraction', 'prop:appN-dy',
       'lem:appO-cut-position', 'asm:appO-lcopt', 'lem:appO-unitarity', 'def:appO-rewriting',
       'asm:appO-envelope', 'asm:appO-deformation', 'asm:appO-rewritten-cs', 'asm:appO-mixing',
       'thm:appO-main', 'cor:appO-interface']
PROC = ['thm:dy-factorization']      # [A] process theorems with master-table bottlenecks
UNITNAME = {'Ch01': '第~1~章', 'Ch08': '第~8~章', 'Ch09': '第~9~章', 'Ch12': '第~12~章', 'Ch14': '第~14~章',
            'Ch18': '第~18~章', 'AppN': '附录~N', 'AppO': '附录~O'}

d = json.load(open(sys.argv[1], encoding='utf-8'))
st = {s['label']: s for s in d['statements'] if not s['reserved']}
order = {s['label']: k for k, s in enumerate(d['statements'])}
asmtag = {k: v[1].strip('[]') if len(v) > 1 and v[1].startswith('[') else None for k, v in d['assumptions'].items()}
master = {m['label']: m for m in d['master']}

# ---------------------------------------------------------------- reachability on the full graph
users = collections.defaultdict(set)
for l, s in st.items():
    for p in s['uses']:
        if p in st:
            users[p].add(l)
reach = {}
def R(p):                       # all statements reachable from p (p is a premise of ...)
    if p in reach:
        return reach[p]
    reach[p] = set()
    out = set()
    for u in users[p]:
        out.add(u); out |= R(u)
    reach[p] = out
    return out
sys.setrecursionlimit(100000)
S = set(SEL)
rel = {(p, q) for p in SEL for q in SEL if p != q and q in R(p)}
edges = set()
for (p, q) in rel:
    if any((p, m) in rel and (m, q) in rel for m in SEL if m not in (p, q)):
        continue
    edges.add((p, q))
def kind(l):
    s = st[l]
    return s['pfx']
def is_rcond(l):
    return st[l]['tag'] == 'R' and st[l]['qual'] == 'R_cond'
for (p, q) in rel:                       # asm -> R_cond edges are never removed
    if kind(p) == 'asm' and is_rcond(q) and p in st[q]['uses']:
        edges.add((p, q))
red = set()
for t in PROC:
    bn = re.findall(r'`(asm:[A-Za-z0-9\-]+)`', master[t]['bottleneck'])
    for b in bn:
        if b in S and (b, t) in rel:
            edges.add((b, t)); red.add((b, t))

# ---------------------------------------------------------------- layers and sub-columns
units = sorted({st[l]['unit'] for l in SEL}, key=UI.get)
depth = {}
for l in sorted(SEL, key=order.get):
    u = st[l]['unit']
    preds = [p for (p, q) in edges if q == l and st[p]['unit'] == u]
    depth[l] = 1 + max([depth[p] for p in preds], default=-1)
cols = []                                   # list of (unit, depth) columns, in order
for u in units:
    for k in range(0, 1 + max(depth[l] for l in SEL if st[l]['unit'] == u)):
        if any(st[l]['unit'] == u and depth[l] == k for l in SEL):
            cols.append((u, k))
col_of = {l: cols.index((st[l]['unit'], depth[l])) for l in SEL}
members = collections.defaultdict(list)
for l in sorted(SEL, key=order.get):
    members[col_of[l]].append(l)
# vertical order: barycentre sweeps
pos = {}
for c in members:
    for i, l in enumerate(members[c]):
        pos[l] = i
def sweep(neigh):
    for c in sorted(members, key=lambda c: c if neigh == 'pred' else -c):
        def bc(l):
            nb = [p for (p, q) in edges if q == l] if neigh == 'pred' else [q for (p, q) in edges if p == l]
            nb = [x for x in nb if x in pos]
            return sum(pos[x] for x in nb) / len(nb) if nb else pos[l]
        members[c].sort(key=lambda l: (bc(l), order[l]))
        for i, l in enumerate(members[c]):
            pos[l] = i
sweep('pred'); sweep('succ')

# ---------------------------------------------------------------- coordinates
# Hand-tuned for the template (the integrator's generator computes them by barycentre sweeps):
# columns in book order of the units (Ch1 | Ch9 | Ch12 | App N | App O), sub-columns by depth inside a unit.
X = [0.0, 1.45, 2.65, 3.85, 5.3, 6.5, 7.95, 9.15, 10.6, 11.8, 13.0, 14.2]
XY = {'asm:intro-bridge': (0, 1.25),
      'prop:method-fsi': (1, -1.9), 'prop:method-glauber-deformation': (2, -0.95), 'thm:method-template': (3, 0.0),
      'thm:dy-factorization': (4, 0.0), 'conj:dy-coloured-final': (5, 1.45),
      'thm:appN-subtraction': (6, 1.65), 'asm:appN-collins': (6, 0.65), 'asm:appN-cutsum': (6, -0.65), 'prop:appN-dy': (7, 0.0),
      'asm:appO-lcopt': (8, 1.25), 'lem:appO-cut-position': (8, -1.9),
      'def:appO-rewriting': (9, -0.75), 'lem:appO-unitarity': (9, -1.9),
      'asm:appO-envelope': (10, 1.95), 'asm:appO-mixing': (10, 0.85), 'asm:appO-rewritten-cs': (10, -0.25), 'asm:appO-deformation': (10, -1.35),
      'thm:appO-main': (11, 0.85), 'cor:appO-interface': (11, -0.55)}
xy = {l: (X[c], y) for l, (c, y) in XY.items()}
col_of = {l: c for l, (c, y) in XY.items()}
cols = [('Ch01', 0), ('Ch09', 0), ('Ch09', 1), ('Ch09', 2), ('Ch12', 0), ('Ch12', 1), ('AppN', 0), ('AppN', 1),
        ('AppO', 0), ('AppO', 1), ('AppO', 2), ('AppO', 3)]
ncol = len(cols)
members = collections.defaultdict(list)
for l in SEL:
    members[col_of[l]].append(l)
XSTEP, YSTEP = 1.2, 1.0

def split_label(t, L=12):
    """split a label at hyphens into the fewest lines of length <= max(L, longest segment), balanced"""
    seg = re.findall(r'[^-]+-?', t)
    lim = max(L, max(len(x) for x in seg))
    best = None
    n = len(seg)
    import itertools
    for k in range(1, n + 1):
        for cuts in itertools.combinations(range(1, n), k - 1):
            parts, prev = [], 0
            for c in list(cuts) + [n]:
                parts.append(''.join(seg[prev:c])); prev = c
            m = max(len(x) for x in parts)
            if m <= lim and (best is None or m < best[0]):
                best = (m, parts)
        if best:
            return best[1]
    return [t]

CH = 0.0925            # width of one \tiny\ttfamily character in cm (0.525 em of 5 pt)
def width(l):
    t = l.split(':', 1)[1]
    w = max(len(x) for x in split_label(t)) * CH + 0.106
    if st[l]['pfx'] == 'conj':
        w = w * 1.42 + 0.05
    return w

def short2(l):
    return r'\\'.join(split_label(l.split(':', 1)[1]))

# automatic x positions from the column widths: gap 0.18 cm inside a unit, 0.30 cm between units
wmax = [max(width(l) for l in SEL if col_of[l] == c) for c in range(len(cols))]
X = [0.0]
for c in range(1, len(cols)):
    gap = 0.30 if cols[c][0] != cols[c - 1][0] else 0.18
    X.append(round(X[-1] + (wmax[c - 1] + wmax[c]) / 2 + gap, 3))
xy = {l: (X[c], y) for l, (c, y) in XY.items()}
print('X =', X, ' total width ~ %.2f cm' % (X[-1] + wmax[-1] / 2 + wmax[0] / 2))

def style(l):
    s = st[l]
    p = s['pfx']
    if p == 'asm':
        return 'ffP asm'
    if p == 'def':
        return 'ffP def'
    if p == 'conj':
        return 'ffP conj'
    if s['tag'] == 'V':
        return 'ffP V'
    if s['tag'] is None:                 # pure mathematics
        return 'ffP math'
    base = {'R': 'ffP R', 'A': 'ffP A', 'P': 'ffP P', 'C': 'ffP C'}[s['tag']]
    if s['tag'] == 'R' and s['qual'] == 'R_cond':
        base += ',ffP cond'
    return base
name = {l: 'n%02d' % k for k, l in enumerate(SEL)}
out = []
out.append('% ---- generated by test_ff/scripts/appP_template.py (template of the App P generator) ----')
# unit headers
for c, (u, k) in enumerate(cols):
    if k == 0:
        last = max(i for i, (uu, kk) in enumerate(cols) if uu == u)
        xm = (c + last) / 2 * XSTEP
        xm = (X[c] + X[last]) / 2
        out.append('\\node[ffP unit] at (%.3f,%.3f) {%s};' % (xm, 2.75, UNITNAME[u]))
for c in range(1, len(cols)):
    if cols[c][0] != cols[c - 1][0]:
        xs = (X[c] + X[c - 1]) / 2
        out.append('\\draw[gray!35,line width=0.4pt,dash pattern=on 1pt off 1.5pt] (%.3f,2.5) -- (%.3f,-2.45);' % (xs, xs))
EDGES_AT = len(out)
for l in SEL:
    out.append('\\node[%s] (%s) at (%.3f,%.3f) {%s};' % (style(l), name[l], xy[l][0], xy[l][1], short2(l)))
for (p, q) in sorted(edges, key=lambda e: (order[e[0]], order[e[1]])):
    st_ = 'ffP use'
    if (p, q) in red:
        st_ = 'ffP neck'
    elif kind(p) == 'asm' and is_rcond(q):
        st_ = 'ffP asmuse'
    if abs(col_of[p] - col_of[q]) > 2 and (p, q) not in red:
        st_ += ',ffP long'
    out.append('\\draw[%s] (%s) -- (%s);' % (st_, name[p], name[q]))
nodes_part = out[EDGES_AT:EDGES_AT + len(SEL)]
edges_part = out[EDGES_AT + len(SEL):]
out = out[:EDGES_AT] + nodes_part + ['\\begin{scope}[on background layer]'] + edges_part + ['\\end{scope}']
open(sys.argv[2], 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('columns:', cols)
print('nodes:', len(SEL), 'edges:', len(edges), 'red:', len(red))
ymax = max(len(v) for v in members.values())
print('max column size:', ymax, ' width ~ %.2f cm, height ~ %.2f cm' % ((ncol - 1) * XSTEP, (ymax - 1) * YSTEP))
