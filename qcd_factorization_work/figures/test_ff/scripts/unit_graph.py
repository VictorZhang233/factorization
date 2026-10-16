r"""Unit-level dependency graph from the \uses data of FINAL_OUTLINE_v2 (via outline.json).

    python3 -I unit_graph.py outline.json

Prints: number of statement edges per unit pair, strongly connected components of the unit graph,
the transitive reduction of its condensation, and the critical-path check.
"""
import sys, json, collections

UNITS = ['front'] + ['Ch%02d' % i for i in range(1, 26)] + ['App' + c for c in 'ABCDEFGHIJKLMNOPQ']
d = json.load(open(sys.argv[1], encoding='utf-8'))
st = [s for s in d['statements'] if not s['reserved']]
unit = {s['label']: s['unit'] for s in st}
E = collections.Counter()
for s in st:
    for u in s['uses']:
        if u in unit and unit[u] != s['unit']:
            E[(unit[u], s['unit'])] += 1          # premise unit -> user unit
nodes = [u for u in UNITS if any(u in e for e in E)]
print('units with edges:', len(nodes))
adj = collections.defaultdict(set)
for (a, b) in E:
    adj[a].add(b)
# Tarjan
sys.setrecursionlimit(10000)
idx, low, on, stack, comps, c = {}, {}, set(), [], [], [0]
def sc(v):
    idx[v] = low[v] = c[0]; c[0] += 1; stack.append(v); on.add(v)
    for w in adj[v]:
        if w not in idx:
            sc(w); low[v] = min(low[v], low[w])
        elif w in on:
            low[v] = min(low[v], idx[w])
    if low[v] == idx[v]:
        comp = []
        while True:
            w = stack.pop(); on.discard(w); comp.append(w)
            if w == v:
                break
        comps.append(comp)
for v in nodes:
    if v not in idx:
        sc(v)
big = [sorted(cc, key=UNITS.index) for cc in comps if len(cc) > 1]
print('non-trivial SCCs:', big)
for cc in big:
    for a in cc:
        for b in cc:
            if (a, b) in E:
                print('   ', a, '->', b, E[(a, b)])
# list edges into / out of selected units
for u in ['AppM', 'AppN', 'AppO']:
    print(u, 'used by:', sorted([b for (a, b) in E if a == u], key=UNITS.index))
    print(u, 'uses   :', sorted([a for (a, b) in E if b == u], key=UNITS.index))
print('total unit edges:', len(E))
