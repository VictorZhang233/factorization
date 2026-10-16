r"""Vertical layout optimiser for the App P template graph (simulated annealing on a y grid).

    python3 -I layout_opt.py appP_template_body.tex  > yopt.txt

Reads the generated node lines (\node[style] (nXX) at (x,y) {label};) and edge lines (\draw[...] (nA) -- (nB);),
estimates node boxes from the labels (\tiny\ttfamily, 0.0925 cm per character, 0.25 cm per line),
and minimises   100 * (edge passes through a non-endpoint node box)
              +   2 * (edge crossings, red edges weighted 3)
              + 0.2 * (sum of |y|)      subject to: no overlap of boxes in a column.
Prints the optimal y per node (deterministic seed).
"""
import sys, re, random, math

lines = open(sys.argv[1], encoding='utf-8').read().split('\n')
nodes, edges = {}, []
for l in lines:
    m = re.match(r'\\node\[(ffP [^\]]*)\] \((n\d\d)\) at \(([-\d.]+),([-\d.]+)\) \{(.*)\};', l)
    if m:
        st, n, x, y, lab = m.groups()
        parts = lab.split('\\\\')
        w = max(len(p) for p in parts) * 0.0925 + 0.106
        h = 0.25 * len(parts) + 0.08
        if 'conj' in st:
            w = w * 1.42 + 0.05; h = h * 1.3
        nodes[n] = dict(x=float(x), y=float(y), w=w, h=h)
        continue
    m = re.match(r'\\draw\[([^\]]*)\] \((n\d\d)\) -- \((n\d\d)\);', l)
    if m:
        edges.append((m.group(2), m.group(3), 'neck' in m.group(1)))
names = sorted(nodes)
cols = {}
for n in names:
    cols.setdefault(round(nodes[n]['x'], 2), []).append(n)

def seg_rect(p, q, r, pad=0.06):
    """does segment p-q pass through rectangle r (cx,cy,w,h)?  sample points"""
    (x1, y1), (x2, y2) = p, q
    cx, cy, w, h = r
    for k in range(1, 60):
        t = k / 60
        x, y = x1 + t * (x2 - x1), y1 + t * (y2 - y1)
        if abs(x - cx) < w / 2 + pad and abs(y - cy) < h / 2 + pad:
            return True
    return False

def cross(a, b, c, d):
    def o(p, q, r):
        return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
    if len({a, b, c, d}) < 4:
        return False
    return o(a, b, c) * o(a, b, d) < 0 and o(c, d, a) * o(c, d, b) < 0

def cost(Y):
    P = {n: (nodes[n]['x'], Y[n]) for n in names}
    c = 0.0
    for (a, b, red) in edges:
        for n in names:
            if n in (a, b):
                continue
            if seg_rect(P[a], P[b], (P[n][0], P[n][1], nodes[n]['w'], nodes[n]['h'])):
                c += 100
    for i in range(len(edges)):
        for j in range(i + 1, len(edges)):
            a, b, r1 = edges[i]; cc, d, r2 = edges[j]
            if cross(P[a], P[b], P[cc], P[d]):
                c += 2 * (3 if (r1 or r2) else 1)
    c += 0.2 * sum(abs(Y[n]) for n in names)
    # column overlaps
    for x, ns in cols.items():
        for i in range(len(ns)):
            for j in range(i + 1, len(ns)):
                a, b = ns[i], ns[j]
                if abs(Y[a] - Y[b]) < (nodes[a]['h'] + nodes[b]['h']) / 2 + 0.15:
                    c += 1000
    return c

random.seed(7)
grid = [round(-2.4 + 0.1 * k, 2) for k in range(51)]
Y = {n: nodes[n]['y'] for n in names}
best, bestc = dict(Y), cost(Y)
cur, curc = dict(Y), bestc
T = 30.0
for it in range(24000):
    n = random.choice(names)
    old = cur[n]
    cur[n] = random.choice(grid)
    c = cost(cur)
    if c < curc or random.random() < math.exp((curc - c) / T):
        curc = c
        if c < bestc:
            best, bestc = dict(cur), c
    else:
        cur[n] = old
    T = max(0.05, T * 0.9997)
print('cost', round(bestc, 2))
for n in names:
    print(n, best[n])
