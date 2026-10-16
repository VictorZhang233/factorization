# Reviewer r3_2: partial independent audit of the bubble-class certificate archive (data only; no script code imported).
import gzip, json, sys
from fractions import Fraction as Fr
from collections import Counter
path = sys.argv[1]
d = json.load(gzip.open(path))
ncert = 0; bad_dual = 0; changed = 0; bad_val = 0; bad_cons = 0; maxL = 0; exp_mismatch = 0; splus_mismatch = 0
eps_of = Counter(); worst = {}
for rec in d:
    r = rec['record']
    n = len(r['local']); w = [Fr(x) for x in r['weights']]
    cons = [([Fr(a) for a in g], Fr(h)) for g, h in r['cons']]
    vals = []
    for c in r['certs']:
        ncert += 1
        y = {int(k): Fr(v) for k, v in c['dual'].items()}
        if any(v <= 0 for v in y.values()): bad_dual += 1
        if sorted(y.keys()) != sorted(c['Splus']): splus_mismatch += 1
        if c['dim_bound'] != c['dim_bound_r1']: changed += 1
        maxL = max(maxL, c['dim_bound'])
        x = [Fr(v) for v in c['primal']]
        a = c['monomial']
        K = len(x) - n
        cvec = [Fr(a[i]) + w[i] for i in range(n)] + [Fr(-1)]*K
        val = sum(ci*xi for ci, xi in zip(cvec, x)) - Fr(a[n])
        if val != Fr(c['value']): bad_val += 1
        X = x[:n]
        if any(sum(gi*xi for gi, xi in zip(g, X)) > h for g, h in cons): bad_cons += 1
        vals.append(Fr(c['value']))
    if vals:
        e = -2*max(vals)
        if Fr(r['exponent']) != e: exp_mismatch += 1
        key = (rec['part'], rec['eps'])
        worst[key] = min(worst.get(key, Fr(100)), Fr(r['exponent']))
print(f"records {len(d)}, certificates {ncert}")
print(f"dual entries <= 0: {bad_dual};  Splus != support(dual): {splus_mismatch};  dim bound changed by S+: {changed};  max dim bound: {maxL}")
print(f"c.x + const != claimed value: {bad_val};  primal X violates stored cell constraints: {bad_cons}")
print(f"record exponent != -2*max(cert value): {exp_mismatch}")
for k, v in sorted(worst.items()):
    print("   min exponent", k, v)
