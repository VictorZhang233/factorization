r"""Prototype of the App P dependency-graph generator (FIGURES_INDEX_v2 Sec. 4.9), used for the TEMPLATE
fig:appP-dependency of figure set F (agent figF).  Python 3 standard library + xelatex (for exact box sizes).

    python3 -I appP_template2.py outline.json out_block.tex [seed]

Input : outline.json written by outline_data.py (statements, \uses, tags, register, master-table rows);
        05_fig_appP-dependency.tex.in (styles, legend, caption) in the directory of this script.
Output: the complete figure block (%%% BEGIN ... %%% END) with plain TikZ node/edge lines.

Algorithm (what the integrator's generator is expected to do; Sec. 4.9 rules 1-5):
 1. node selection  SEL (here: a fixed Drell--Yan / measurement slice of the skeleton);
 2. edges           transitive reduction of the reachability relation of the FULL \uses graph restricted to SEL
                    (an edge p -> q: q depends on p, possibly through statements that are not drawn);
                    bottleneck edges b -> t for every [A] process theorem t in PROC and every assumption b in SEL
                    listed in t's master-table column 瓶颈 (drawn even when implied), thick red;
 3. layers          one layer per unit in book order (front, Ch1..Ch25, App A..Q); inside a unit, sub-columns by
                    the longest path over intra-unit edges;
 4. box sizes       measured: every node is typeset once with its style (measure_appP.tex in the test directory);
 5. x positions     from the column widths, gaps GAP_IN (inside a unit) and GAP_UNIT (between units);
 6. y positions     barycentre sweeps for the initial order, then simulated annealing on a 0.05 cm grid minimising
                        W_HIT * (edge passes through a box that is not its endpoint)
                      + W_X   * (edge crossings; crossings involving a red edge weighted 4)
                      + W_LEN * (total |dy| of the edges)
                    subject to a vertical clearance >= SEP between the boxes of one column (rule 2: >= 0.25 cm);
 7. TikZ            styles of rule 3 (type, tag, R_cond dashed), rule 4 (edge classes); edges spanning more than two
                    columns (except red ones) with opacity 0.5.
"""
import sys, os, json, re, collections, random, math, itertools, subprocess

UNITS = ['front'] + ['Ch%02d' % i for i in range(1, 26)] + ['App' + c for c in 'ABCDEFGHIJKLMNOPQ']
UI = {u: i for i, u in enumerate(UNITS)}
SEL = ['asm:intro-bridge',
       'thm:dy-factorization', 'conj:dy-coloured-final',
       'prop:break-measurement', 'thm:break-tmd',
       'asm:appN-collins', 'asm:appN-cutsum', 'thm:appN-subtraction', 'prop:appN-dy',
       'asm:appO-lcopt', 'def:appO-family',
       'asm:appO-mixing', 'asm:appO-deformation', 'asm:appO-rewritten-cs', 'prop:appO-target',
       'thm:appO-main', 'cor:appO-interface']
PROC = ['thm:dy-factorization']          # [A] process theorems whose bottleneck assumptions are drawn in red
UNITNAME = {'Ch01': '第~1~章', 'Ch09': '第~9~章', 'Ch12': '第~12~章', 'Ch14': '第~14~章', 'Ch18': '第~18~章',
            'AppN': '附录~N', 'AppO': '附录~O'}
HERE = os.path.dirname(os.path.abspath(__file__))
TESTDIR = os.path.dirname(HERE)
TEMPLATE = os.path.join(HERE, '05_fig_appP-dependency.tex.in')
GAP_IN, GAP_UNIT = 0.14, 0.24
SEP = 0.25
YMIN, YMAX = -2.4, 2.4
W_HIT, W_X, W_LEN = 80.0, 4.0, 0.12

d = json.load(open(sys.argv[1], encoding='utf-8'))
st = {s['label']: s for s in d['statements'] if not s['reserved']}
order = {s['label']: k for k, s in enumerate(d['statements'])}
master = {m['label']: m for m in d['master']}
for l in SEL:
    assert l in st, l

# ------------------------------------------------------------------ edges
users = collections.defaultdict(set)
for l, s in st.items():
    for p in s['uses']:
        if p in st:
            users[p].add(l)
sys.setrecursionlimit(100000)
reach = {}
def R(p):
    if p in reach:
        return reach[p]
    reach[p] = set()
    out = set()
    for u in users[p]:
        out.add(u)
        out |= R(u)
    reach[p] = out
    return out
rel = {(p, q) for p in SEL for q in SEL if p != q and q in R(p)}
edges = {(p, q) for (p, q) in rel if not any((p, m) in rel and (m, q) in rel for m in SEL if m not in (p, q))}
red = set()
for t in PROC:
    for b in re.findall(r'`(asm:[A-Za-z0-9\-]+)`', master[t]['bottleneck']):
        if b in SEL:
            assert (b, t) in rel, (b, t)
            red.add((b, t))
edges |= red

def is_rcond(l):
    return st[l]['tag'] == 'R' and st[l]['qual'] == 'R_cond'
def eclass(e):
    p, q = e
    if e in red:
        return 'neck'
    if st[p]['pfx'] == 'asm' and is_rcond(q):
        return 'asmuse'
    return 'use'
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
    if s['tag'] is None:
        return 'ffP math'
    b = {'R': 'ffP R', 'A': 'ffP A', 'P': 'ffP P', 'C': 'ffP C'}[s['tag']]
    return b + (',ffP cond' if is_rcond(l) else '')

# ------------------------------------------------------------------ labels and measured box sizes
def split_label(t, L=10, L2=12):
    """split at hyphens: one line if <= L characters, else two lines of <= L2 characters, else the fewest lines of
    <= max(L, longest segment) characters (balanced)"""
    seg = re.findall(r'[^-]+-?', t)
    n = len(seg)
    for k in range(1, n + 1):
        lim = L2 if k == 2 else max(L, max(len(x) for x in seg))
        best = None
        for cuts in itertools.combinations(range(1, n), k - 1):
            parts, prev = [], 0
            for c in list(cuts) + [n]:
                parts.append(''.join(seg[prev:c]))
                prev = c
            m = max(len(x) for x in parts)
            if m <= lim and (best is None or m < best[0]):
                best = (m, parts)
        if best:
            return best[1]
    return [t]
lab = {l: split_label(l.split(':', 1)[1], L2=(10 if st[l]['pfx'] == 'conj' else 12)) for l in SEL}
name = {l: 'n%02d' % k for k, l in enumerate(SEL)}
tpl = open(TEMPLATE, encoding='utf-8').read()
styles = tpl[tpl.index('\\begin{tikzpicture}[fd,') + len('\\begin{tikzpicture}['):tpl.index('%%GENERATED%%')].rstrip().rstrip(']')
meas = ['\\input{preamble_fact.tex}', '\\begin{document}', '\\begin{tikzpicture}[' + styles + ']']
for l in SEL:
    meas.append('\\node[%s] (%s) at (0,0) {%s};' % (style(l), name[l], '\\\\'.join(lab[l])))
    # width from the west/east anchors, height from south/north (compass corner anchors lie on an ellipse's border)
    meas.append('\\pgfpointdiff{\\pgfpointanchor{%s}{west}}{\\pgfpointanchor{%s}{east}}\\pgfgetlastxy{\\ffw}{\\ffdummy}'
                '\\pgfpointdiff{\\pgfpointanchor{%s}{south}}{\\pgfpointanchor{%s}{north}}\\pgfgetlastxy{\\ffdummy}{\\ffh}'
                '\\typeout{FFSIZE:%s:\\ffw:\\ffh}' % (name[l], name[l], name[l], name[l], name[l]))
meas += ['\\end{tikzpicture}', '\\end{document}']
open(os.path.join(TESTDIR, 'measure_appP.tex'), 'w', encoding='utf-8').write('\n'.join(meas) + '\n')
subprocess.run(['xelatex', '-interaction=nonstopmode', '-halt-on-error', 'measure_appP.tex'], cwd=TESTDIR,
               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
W, H = {}, {}
inv = {v: k for k, v in name.items()}
for m in re.finditer(r'FFSIZE:(n\d\d):([\d.]+)pt:([\d.]+)pt', open(os.path.join(TESTDIR, 'measure_appP.log'), encoding='utf-8', errors='replace').read()):
    W[inv[m.group(1)]] = float(m.group(2)) / 72.27 * 2.54
    H[inv[m.group(1)]] = float(m.group(3)) / 72.27 * 2.54
for l in SEL:
    if st[l]['tag'] == 'V' and st[l]['pfx'] != 'conj':
        W[l] += 0.04; H[l] += 0.04                 # outer double line
assert len(W) == len(SEL)

# ------------------------------------------------------------------ layers and sub-columns
units = sorted({st[l]['unit'] for l in SEL}, key=UI.get)
depth = {l: 0 for l in SEL}
changed = True
while changed:                                      # longest path over intra-unit edges (fix-point)
    changed = False
    for (p, q) in edges:
        if st[p]['unit'] == st[q]['unit'] and depth[q] < depth[p] + 1:
            depth[q] = depth[p] + 1
            changed = True
cols = []
for u in units:
    for k in sorted({depth[l] for l in SEL if st[l]['unit'] == u}):
        cols.append((u, k))
col = {l: cols.index((st[l]['unit'], depth[l])) for l in SEL}
members = collections.defaultdict(list)
for l in sorted(SEL, key=order.get):
    members[col[l]].append(l)
wcol = [max(W[l] for l in members[c]) for c in range(len(cols))]
X = [0.0]
for c in range(1, len(cols)):
    gap = GAP_UNIT if cols[c][0] != cols[c - 1][0] else GAP_IN
    X.append(X[-1] + wcol[c - 1] / 2 + gap + wcol[c] / 2)
x = {l: X[col[l]] for l in SEL}

# ------------------------------------------------------------------ initial y: barycentre sweeps
pos = {}
for c in members:
    for i, l in enumerate(members[c]):
        pos[l] = i - (len(members[c]) - 1) / 2
def sweep(forward):
    for c in (range(len(cols)) if forward else reversed(range(len(cols)))):
        def bc(l):
            nb = [p for (p, q) in edges if q == l] if forward else [q for (p, q) in edges if p == l]
            return sum(pos[n] for n in nb) / len(nb) if nb else pos[l]
        members[c].sort(key=lambda l: (bc(l), order[l]))
        for i, l in enumerate(members[c]):
            pos[l] = i - (len(members[c]) - 1) / 2
sweep(True)
sweep(False)
y = {l: round(pos[l] * 0.9 / 0.05) * 0.05 for l in SEL}

# ------------------------------------------------------------------ annealing
E = sorted(edges)
def seg_hits_box(p, q, b, pad=0.06):
    (x1, y1), (x2, y2) = p, q
    cx, cy, w, h = b
    lo, hi = 0.0, 1.0                                    # Liang--Barsky clipping against the padded box
    dx, dy = x2 - x1, y2 - y1
    for pp, qq in ((-dx, x1 - (cx - w / 2 - pad)), (dx, (cx + w / 2 + pad) - x1),
                   (-dy, y1 - (cy - h / 2 - pad)), (dy, (cy + h / 2 + pad) - y1)):
        if pp == 0:
            if qq < 0:
                return False
        else:
            t = qq / pp
            if pp < 0:
                lo = max(lo, t)
            else:
                hi = min(hi, t)
            if lo > hi:
                return False
    return True
def crosses(a, b, c, e):
    def o(p, q, r):
        return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
    return o(a, b, c) * o(a, b, e) < 0 and o(c, e, a) * o(c, e, b) < 0
def cost(Y, detail=False):
    P = {l: (x[l], Y[l]) for l in SEL}
    hit = cr = 0.0
    for (p, q) in E:
        for n in SEL:
            if n not in (p, q) and seg_hits_box(P[p], P[q], (P[n][0], P[n][1], W[n], H[n])):
                hit += 1
    for i in range(len(E)):
        for j in range(i + 1, len(E)):
            (a, b), (c, e) = E[i], E[j]
            if len({a, b, c, e}) == 4 and crosses(P[a], P[b], P[c], P[e]):
                cr += 4 if (E[i] in red or E[j] in red) else 1
    ln = sum(abs(Y[p] - Y[q]) for (p, q) in E)
    ov = 0
    for c, ns in members.items():
        for a, b in itertools.combinations(ns, 2):
            if abs(Y[a] - Y[b]) < (H[a] + H[b]) / 2 + SEP:
                ov += 1
    tot = W_HIT * hit + W_X * cr + W_LEN * ln + 1e4 * ov
    return (tot, hit, cr, ln, ov) if detail else tot
best_all = None
for seed in ([int(sys.argv[3])] if len(sys.argv) > 3 else [3, 7, 11, 19]):
    random.seed(seed)
    grid = [round(YMIN + 0.05 * k, 2) for k in range(int(round((YMAX - YMIN) / 0.05)) + 1)]
    cur = dict(y)
    cc = cost(cur)
    best, bc_ = dict(cur), cc
    T = 40.0
    for it in range(30000):
        n = random.choice(SEL)
        old = cur[n]
        cur[n] = random.choice(grid) if random.random() < 0.3 else \
            min(YMAX, max(YMIN, round(old + random.choice([-0.3, -0.15, -0.05, 0.05, 0.15, 0.3]), 2)))
        c = cost(cur)
        if c <= cc or random.random() < math.exp((cc - c) / T):
            cc = c
            if c < bc_:
                best, bc_ = dict(cur), c
        else:
            cur[n] = old
        T = max(0.02, T * 0.9997)
    sys.stderr.write('seed %d: cost %.2f\n' % (seed, bc_))
    if best_all is None or bc_ < best_all[1]:
        best_all = (best, bc_)
y = best_all[0]
y = {l: round(v - (max(y.values()) + min(y.values())) / 2, 3) for l, v in y.items()}
tot, hit, cr, ln, ov = cost(y, True)
sys.stderr.write('final cost %.2f  hits %d  crossings %.0f  length %.2f  overlaps %d\n' % (tot, hit, cr, ln, ov))

# ------------------------------------------------------------------ TikZ
top = max(y[l] + H[l] / 2 for l in SEL)
bot = min(y[l] - H[l] / 2 for l in SEL)
out = ['% ---- generated by test_ff/scripts/appP_template2.py (template of the App P generator) ----']
for u in units:
    cs = [c for c, (uu, k) in enumerate(cols) if uu == u]
    out.append('\\node[ffP unit] at (%.3f,%.3f) {%s};' % ((X[cs[0]] + X[cs[-1]]) / 2, top + 0.45, UNITNAME[u]))
for c in range(1, len(cols)):
    if cols[c][0] != cols[c - 1][0]:
        xs = (X[c] - wcol[c] / 2 + X[c - 1] + wcol[c - 1] / 2) / 2
        out.append('\\draw[ffP sep] (%.3f,%.3f) -- (%.3f,%.3f);' % (xs, top + 0.28, xs, bot - 0.08))
for l in SEL:
    out.append('\\node[%s] (%s) at (%.3f,%.3f) {%s};' % (style(l), name[l], x[l], y[l], '\\\\'.join(lab[l])))
out.append('\\begin{scope}[on background layer]')
for (p, q) in sorted(E, key=lambda e: (eclass(e) == 'neck', order[e[0]], order[e[1]])):
    s = 'ffP ' + eclass((p, q))
    if abs(col[p] - col[q]) > 2 and (p, q) not in red:
        s += ',ffP long'
    out.append('\\draw[%s] (%s) -- (%s);' % (s, name[p], name[q]))
out.append('\\end{scope}')
body = '\n'.join('  ' + l for l in out)
blk = tpl.replace('%%GENERATED%%', body).replace('%%LEGENDY%%', '%.3f' % (bot - 0.55))
blk = blk.replace('%%LEGENDX%%', '%.3f' % (-wcol[0] / 2)).replace('%%NNODES%%', str(len(SEL)))
open(sys.argv[2], 'w', encoding='utf-8').write(blk)
sys.stderr.write('columns %s\nwidth %.2f cm, height %.2f cm, nodes %d, edges %d (red %d)\n'
                 % (cols, X[-1] + wcol[-1] / 2 + wcol[0] / 2, top - bot, len(SEL), len(E), len(red)))
