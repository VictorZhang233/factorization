import json, gzip, random, collections, sys
from fractions import Fraction as Fr
LOGS = sys.argv[1]
random.seed(7)
b = json.load(gzip.open(LOGS + '/r3_bubble_certificates_sc.json.gz'))
t = json.load(gzip.open(LOGS + '/r3_triangle_certificates_sc.json.gz'))

def inside(cons, X):
    return all(sum(Fr(g[i])*X[i] for i in range(len(X))) <= Fr(h) for g, h in cons)

# ---- bubble: collect distinct cells per (part, region, eps) ----
cells = collections.defaultdict(set)
for e in b:
    rec = e['record']
    if not rec or rec.get('status') != 'ok': continue
    lp = rec['lpdata']
    key = (e['part'], rec['region'], e['eps'], tuple(lp['local']))
    cells[key].add(json.dumps(lp['cons']))
for k in sorted(cells): print(k, len(cells[k]), 'cells')

def sample_check(key, gen, N=20000):
    cl = [json.loads(c) for c in cells[key]]
    miss = []
    for _ in range(N):
        X = gen()
        if not any(inside(c, X) for c in cl):
            miss.append(X)
    return miss

R = lambda lo, hi: Fr(random.randint(0, 10**6), 10**6)*(hi - lo) + lo
for eps in ['0', '1/10']:
    # region I: local (u,kap): X_u in (-inf, 0], X_k in R  (actual cell u <= 1/2 sits inside X_u <= 0)
    keyI = ('remainder 0<u<1', 'I', eps, ('u', 'kap'))
    keyII = ('remainder 0<u<1', 'II', eps, ('v', 'kap'))
    keyC = ('remainder 0<u<1 corner', 'II', eps, ('v', 'kap'))
    keyB = ('remainder u>1', 'BIG', eps, ('u', 'kap'))
    mI = sample_check(keyI, lambda: [R(-30, 0), R(-40, 40)]) if keyI in cells else ['no cells']
    # region II: X_v in (-inf,0], X_k in R, minus the corner {X_v <= -3, X_k <= -4} (corner records)
    def genII():
        while True:
            X = [R(-30, 0), R(-40, 40)]
            if not (X[0] <= -3 and X[1] <= -4): return X
    mII = sample_check(keyII, genII) if keyII in cells else ['no cells']
    mC = sample_check(keyC, lambda: [R(-30, -3), R(-40, -4)]) if keyC in cells else ['no cells']
    mB = sample_check(keyB, lambda: [R(0, 30), R(-40, 40)]) if keyB in cells else ['no cells']
    print(f"eps={eps}: uncovered samples  I: {len(mI)}  II\\corner: {len(mII)}  corner: {len(mC)}  u>1: {len(mB)}")
    for name, m in [('I', mI), ('II', mII), ('corner', mC), ('u>1', mB)]:
        if m and m != ['no cells']:
            print('   e.g.', name, [float(x) for x in m[0]])

# ---- triangle remainder cells: r I (X_u<=0), r II (X_v<=0), r u>1 (X_u>=0), sliver A/B ----
tri = collections.defaultdict(list)
for r in t:
    tri[(r['label'], r['eps'])].append(r['lpdata']['cons'])
for (lab, eps), cl in sorted(tri.items()):
    if lab.startswith('r ') or lab.startswith('sliver'):
        print('triangle', lab, eps, cl)
