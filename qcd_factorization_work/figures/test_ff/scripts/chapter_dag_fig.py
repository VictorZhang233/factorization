r"""Generate fig:summary-chapter-dag (FIGURES_INDEX_v2 Sec. 4.8, optional) from the \uses data of FINAL_OUTLINE_v2.

    python3 -I chapter_dag_fig.py outline.json out_block.tex [seed]

Data (all generated from outline.json, never typed by hand):
  * chapter -> chapter edges: transitive reduction of the "effective" chapter graph (an edge U -> V iff some statement
    of V uses, directly or through appendix statements only, a statement of U) -- as scripts/chapter_dag.py;
  * appendix -> chapter edges for the proof appendices M, N, O (direct \uses), with their multiplicities;
  * the users of the tool appendices A--L (direct \uses), printed as a list under the graph;
  * the critical path of WRITER_SPEC_v2 Sec. 12.1 (App N -> App O -> Ch12/Ch14/Ch18 -> Ch22--Ch24), drawn in red
    with the direct unit edges that realise it (each is checked to exist in the data).
Layout: chapters in layers = longest path in the reduced chapter DAG (top to bottom); Ch17 and Ch19 may sit lower
(their only premises are far above); App M, N, O in a column on the right.  x positions inside the layers and the rows of
the flexible nodes are chosen by simulated annealing (crossings, edges through boxes, length).
"""
import sys, json, collections, itertools, random, math

UNITS = ['front'] + ['Ch%02d' % i for i in range(1, 26)] + ['App' + c for c in 'ABCDEFGHIJKLMNOPQ']
UI = {u: i for i, u in enumerate(UNITS)}
SHORT = {'Ch01': '引言', 'Ch02': 'QCD 基础', 'Ch03': '工具', 'Ch04': '红外结构', 'Ch05': 'Sudakov',
         'Ch06': '$e^+e^-$', 'Ch07': 'DIS/OPE', 'Ch08': 'PDF/FF', 'Ch09': '一般方法', 'Ch10': 'DIS 全阶',
         'Ch11': '共线过程', 'Ch12': 'DY 过程', 'Ch13': '阈值', 'Ch14': 'TMD', 'Ch15': 'SCET', 'Ch16': '喷注',
         'Ch17': '小 $x$', 'Ch18': '破坏', 'Ch19': '遍举', 'Ch20': '重夸克', 'Ch21': '幂次修正', 'Ch22': 'LaMET',
         'Ch23': 'Y.~Liu', 'Ch24': '其他前沿', 'AppM': 'OPE 证明', 'AppN': 'Collins 减除', 'AppO': 'Glauber 相消'}
PART = {**{'Ch%02d' % i: 'I' for i in range(1, 6)}, **{'Ch%02d' % i: 'II' for i in range(6, 9)},
        **{'Ch%02d' % i: 'III' for i in range(9, 14)}, **{'Ch%02d' % i: 'IV' for i in range(14, 19)},
        'Ch19': 'V', 'Ch20': 'V', 'Ch21': 'VI', 'Ch22': 'VII', 'Ch23': 'VII', 'Ch24': 'VII',
        'AppM': 'App', 'AppN': 'App', 'AppO': 'App'}
DY = 0.66                       # row spacing (cm)
BW, BH = 1.92, 0.42             # chapter box size (cm)
AW = 2.25                       # appendix box width
XMIN, XMAX, XAPP = 2.3, 9.3, 11.2
CRIT = [('AppN', 'AppO'), ('AppO', 'Ch12'), ('AppO', 'Ch14'), ('AppO', 'Ch18'), ('Ch12', 'Ch14'),
        ('Ch14', 'Ch22'), ('Ch14', 'Ch23'), ('Ch14', 'Ch24'), ('Ch18', 'Ch24')]

d = json.load(open(sys.argv[1], encoding='utf-8'))
st = [s for s in d['statements'] if not s['reserved']]
unit = {s['label']: s['unit'] for s in st}
uses = {s['label']: [u for u in s['uses'] if u in unit] for s in st}
isapp = lambda u: u.startswith('App')
E = collections.Counter()
for s in st:
    for p in uses[s['label']]:
        if unit[p] != s['unit']:
            E[(unit[p], s['unit'])] += 1
memo = {}
def chap_premises(lab):
    if lab in memo:
        return memo[lab]
    memo[lab] = set()
    out = set()
    for p in uses[lab]:
        out |= chap_premises(p) if isapp(unit[p]) else {p}
    memo[lab] = out
    return out
EC = collections.Counter()
for s in st:
    if isapp(s['unit']) or s['unit'] == 'front':
        continue
    for p in chap_premises(s['label']):
        if unit[p] != s['unit']:
            EC[(unit[p], s['unit'])] += 1
adj = collections.defaultdict(set)
for (a, b) in EC:
    adj[a].add(b)
chs = sorted({x for e in EC for x in e}, key=UI.get)
reach = {}
for v in reversed(chs):
    r = set()
    for w in adj[v]:
        r.add(w)
        r |= reach.get(w, set())
    reach[v] = r
RED = sorted((a, b) for (a, b) in EC if not any(b in reach[c] for c in adj[a] if c != b))
for e in CRIT:
    assert E.get(e, 0) > 0, ('critical edge not in the data', e)
APPE = sorted((a, b) for (a, b) in E if a in ('AppM', 'AppN', 'AppO') and (b.startswith('Ch') or b in ('AppN', 'AppO', 'AppM')))
APPE = [e for e in APPE if e != ('AppO', 'AppN')]          # drawn together with N -> O as a two-way edge
two_way_NO = E.get(('AppO', 'AppN'), 0) > 0
nodes = [u for u in UNITS if u.startswith('Ch') and u != 'Ch25'] + ['AppM', 'AppN', 'AppO']
edges = sorted(set(RED) | set(APPE) | set(CRIT))
crit = set(CRIT)

# ------------------------------------------------------------------ layout (layers = longest path; x hand-tuned, checked below)
pred = collections.defaultdict(list)
for a, b in RED:
    pred[b].append(a)
lay = {}
def Lr(n):
    if n not in lay:
        lay[n] = 1 + max([Lr(p) for p in pred[n]], default=-1)
    return lay[n]
for n in [u for u in UNITS if u.startswith('Ch') and u not in ('Ch25',)]:
    Lr(n)
POS = {'Ch01': 4.2, 'Ch02': 6.6, 'Ch17': 7.9, 'Ch13': 4.2, 'Ch14': 6.7, 'Ch19': 1.15, 'Ch21': 4.4, 'Ch15': 6.8,
       'Ch22': 2.65, 'Ch20': 6.45, 'Ch16': 8.85, 'Ch23': 2.65, 'Ch18': 8.85, 'Ch24': 5.8}
ROW = {'Ch19': 12}                                   # Ch19 lowered from its layer 8 (its only premise is Ch09)
CH = [u for u in UNITS if u.startswith('Ch') and u != 'Ch25']
X = {n: POS.get(n, 5.4) for n in CH}
Y = {n: -DY * ROW.get(n, lay[n]) for n in CH}
for n in CH:
    assert ROW.get(n, lay[n]) >= lay[n]
    for (a, b) in RED:
        if a == n:
            assert ROW.get(b, lay[b]) > ROW.get(n, lay[n]), (n, b)
BW = 2.2
ORTHO = {('Ch09', 'Ch19'): 'west', ('Ch17', 'Ch24'): 'east'}     # long edges routed around the spine
XBUS = {('Ch09', 'Ch19'): 1.15, ('Ch17', 'Ch24'): 10.15}
# geometric check of the straight edges
def seg_hits(p, q, c, w, h, pad=0.04):
    (x1, y1), (x2, y2) = p, q
    lo, hi = 0.0, 1.0
    dx, dy = x2 - x1, y2 - y1
    for pp, qq in ((-dx, x1 - (c[0] - w / 2 - pad)), (dx, (c[0] + w / 2 + pad) - x1),
                   (-dy, y1 - (c[1] - h / 2 - pad)), (dy, (c[1] + h / 2 + pad) - y1)):
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
def cross(a, b, c, e):
    def o(p, q, r):
        return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
    return o(a, b, c) * o(a, b, e) < 0 and o(c, e, a) * o(c, e, b) < 0
straight = [e for e in RED if e not in ORTHO]
P = {n: (X[n], Y[n]) for n in CH}
for (a, b) in straight:
    for n in CH:
        if n not in (a, b) and seg_hits(P[a], P[b], P[n], BW, BH):
            sys.stderr.write('EDGE THROUGH BOX: %s->%s hits %s\n' % (a, b, n))
ncross = sum(1 for e, f in itertools.combinations(straight, 2) if len(set(e) | set(f)) == 4 and cross(P[e[0]], P[e[1]], P[f[0]], P[f[1]]))
sys.stderr.write('straight edges %d, crossings %d\n' % (len(straight), ncross))
for i in range(len(CH)):
    for j in range(i + 1, len(CH)):
        a, b = CH[i], CH[j]
        if abs(Y[a] - Y[b]) < 1e-6 and abs(X[a] - X[b]) < BW + 0.15:
            sys.stderr.write('OVERLAP %s %s\n' % (a, b))

# ------------------------------------------------------------------ TikZ
crit_nodes = ['Ch12', 'Ch14', 'Ch18', 'Ch22', 'Ch23', 'Ch24']
badge = {}
for app, letter in (('AppM', 'M'), ('AppN', 'N'), ('AppO', 'O')):
    for (a, b), v in sorted(E.items()):
        if a == app and b in CH:
            badge.setdefault(b, []).append(letter)
out = []
out.append('% ---- generated by test_ff/scripts/chapter_dag_fig.py from the \\uses data of FINAL_OUTLINE_v2 ----')
for n in CH:
    k = int(n[2:])
    style = 'ff ch' + (',ff crit' if n in crit_nodes else '')
    out.append('\\node[%s] (%s) at (%.2f,%.3f) {};' % (style, n, X[n], Y[n]))
    out.append('\\node[ff chlab] at ($(%s.west)+(0.07,0)$) {\\textbf{%d}\\,%s};' % (n, k, SHORT[n]))
    for i, letter in enumerate(reversed(badge.get(n, []))):
        out.append('\\node[ff badge %s] at ($(%s.east)+(%.2f,0)$) {%s};' % (letter, n, -0.15 - 0.25 * i, letter))
out.append('\\begin{scope}[on background layer]')
for (a, b) in RED:
    if (a, b) in ORTHO:
        side = ORTHO[(a, b)]
        xb = XBUS[(a, b)]
        if side == 'west':
            out.append('\\draw[ff dep,rounded corners=3pt] (%s.west) -- (%.2f,%.3f) -- (%s.north);' % (a, xb, Y[a], b))
        else:
            out.append('\\draw[ff dep,rounded corners=3pt] (%s.east) -- (%.2f,%.3f) -- (%.2f,%.3f) -- (%s.east);' % (a, xb, Y[a], xb, Y[b], b))
    else:
        out.append('\\draw[ff dep] (%s) -- (%s);' % (a, b))
out.append('\\end{scope}')
# right column: proof appendices, tool appendices, critical path
def users(app):
    return sorted([(b, v) for (a, b), v in E.items() if a == app], key=lambda t: UI[t[0]])
def chlist(app, with_counts, chapters_only=False):
    items = []
    for b, v in users(app):
        if chapters_only and not b.startswith('Ch'):
            continue
        lab = str(int(b[2:])) if b.startswith('Ch') else b[3:]
        items.append('%s（%d）' % (lab, v) if with_counts else lab)
    return '、'.join(items)
proof = []
for app, name in (('AppM', 'OPE 证明'), ('AppN', 'Collins 减除'), ('AppO', 'Glauber 相消')):
    proof.append('\\textbf{%s}\\,%s：%s' % (app[3:], name, chlist(app, True, True)))
appapp = []
for app in ('AppM', 'AppN', 'AppO'):
    for b, v in users(app):
        if not b.startswith('Ch'):
            appapp.append('%s$\\to$%s（%d）' % (app[3:], b[3:], v))
tools = []
for c in 'ABCDEFIJKL':
    tools.append('%s：%s' % (c, chlist('App' + c, False)))
none = [c for c in 'GHQ' if not users('App' + c)]
right = {'proof': proof, 'tools': tools, 'none': none,
         'NO': E.get(('AppN', 'AppO'), 0), 'ON': E.get(('AppO', 'AppN'), 0)}
blk = open(sys.argv[2] + '.in', encoding='utf-8').read() if False else None
tpl = open(__file__.rsplit('/', 1)[0] + '/12_fig_summary-chapter-dag.tex.in', encoding='utf-8').read()
tpl = tpl.replace('%%GENERATED%%', '\n'.join('  ' + l for l in out))
tpl = tpl.replace('%%PROOF%%', '\\\\\n      '.join(proof))
tpl = tpl.replace('%%TOOLS%%', '；'.join(tools[:5]) + '；\\\\\n      ' + '；'.join(tools[5:]) + '；' + '、'.join(none) + ' 无依赖关系')
tpl = tpl.replace('%%APPAPP%%', '、'.join(appapp))
tpl = tpl.replace('%%NRED%%', str(len(RED)))
open(sys.argv[2], 'w', encoding='utf-8').write(tpl)
sys.stderr.write('reduction edges %d; badges %s\n' % (len(RED), badge))
