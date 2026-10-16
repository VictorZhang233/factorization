r"""Chapter-level DAG from the statement-level \uses graph of FINAL_OUTLINE_v2 (via outline.json).

    python3 -I chapter_dag.py outline.json

Edge  U -> V  (U, V chapters or appendices) iff some statement of V uses, directly, a statement of U.
Chapter -> chapter "effective" edges also count paths that pass only through appendix statements
(the appendices deliver proofs; WRITER_SPEC_v2 4.5 item 5 forbids hidden forward dependencies, so these
edges go forward).  Prints the transitive reduction of the chapter graph and the appendix attachments.
"""
import sys, json, collections, itertools

UNITS = ['front'] + ['Ch%02d' % i for i in range(1, 26)] + ['App' + c for c in 'ABCDEFGHIJKLMNOPQ']
UI = {u: i for i, u in enumerate(UNITS)}
d = json.load(open(sys.argv[1], encoding='utf-8'))
st = [s for s in d['statements'] if not s['reserved']]
unit = {s['label']: s['unit'] for s in st}
uses = {s['label']: [u for u in s['uses'] if u in unit] for s in st}
isapp = lambda u: u.startswith('App')

# direct unit edges with multiplicities
E = collections.Counter()
for s in st:
    for p in uses[s['label']]:
        if unit[p] != s['unit']:
            E[(unit[p], s['unit'])] += 1

# effective chapter->chapter edges: for each chapter statement S, the chapter statements reachable backwards
# through chains of appendix statements only
memo = {}
def chap_premises(lab):
    """chapter statements reachable from lab's premises through appendix statements only"""
    if lab in memo:
        return memo[lab]
    memo[lab] = set()
    out = set()
    for p in uses[lab]:
        if isapp(unit[p]):
            out |= chap_premises(p)
        else:
            out.add(p)
    memo[lab] = out
    return out
EC = collections.Counter()
for s in st:
    if isapp(s['unit']) or s['unit'] == 'front':
        continue
    for p in chap_premises(s['label']):
        if unit[p] != s['unit']:
            EC[(unit[p], s['unit'])] += 1
bad = [(a, b) for (a, b) in EC if UI[a] > UI[b]]
print('effective chapter edges:', len(EC), ' backward:', bad)
chs = sorted({x for e in EC for x in e}, key=UI.get)
adj = collections.defaultdict(set)
for (a, b) in EC:
    adj[a].add(b)
# reachability and transitive reduction
reach = {}
for v in reversed(chs):
    r = set()
    for w in adj[v]:
        r.add(w); r |= reach.get(w, set())
    reach[v] = r
red = set()
for (a, b) in EC:
    if not any(b in reach[c] for c in adj[a] if c != b):
        red.add((a, b))
print('transitive reduction (%d edges):' % len(red))
for a in chs:
    outs = sorted([b for (x, b) in red if x == a], key=UI.get)
    if outs:
        print('  %s -> %s' % (a, ', '.join(outs)))
print('chapters without edges:', [u for u in UNITS[1:26] if u not in chs])
# appendix attachments: for each appendix, chapters that use it directly and chapters it uses directly
for a in [u for u in UNITS if isapp(u)]:
    ub = sorted([b for (x, b) in E if x == a], key=UI.get)
    us = sorted([x for (x, b) in E if b == a], key=UI.get)
    if ub or us:
        print('%s  used by: %s | uses: %s' % (a, ', '.join('%s(%d)' % (b, E[(a, b)]) for b in ub), ', '.join('%s(%d)' % (x, E[(x, a)]) for x in us)))
# Part VII dependencies
for v in ['Ch22', 'Ch23', 'Ch24', 'Ch25']:
    print(v, 'premise units (direct):', sorted({x for (x, b) in E if b == v}, key=UI.get))
json.dump(dict(direct={'%s>%s' % k: n for k, n in E.items()}, effective={'%s>%s' % k: n for k, n in EC.items()},
               reduction=sorted('%s>%s' % e for e in red)), open('scripts/chapter_dag.json', 'w'), indent=1)
