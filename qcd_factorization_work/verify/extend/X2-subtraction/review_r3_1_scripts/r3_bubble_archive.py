"""Review r3_1 -- consistency audit of the round-2 bubble-class certificate archive
logs/r2_bubble_certificates_items_big_small_eps0_1o10.json.gz (Thm 3.9).  The archive does not contain the LP matrices
(the Newton-polytope rows of the denominators), so an independent exact re-verification of optimality is NOT possible
from the archive alone; this script checks what can be checked from the archive:
  (i) counts (piece records, monomial certificates), statuses;
 (ii) exponent == -2 * max(value) over the certificates of each piece (with the frozen/comparability convention);
(iii) Splus == {i : dual_i > 0} exactly, and dim_bound == dim_bound_r1 (the S+ repair changed nothing);
 (iv) exact feasibility of each primal point for the CELL constraints 'cons' (the first rows of the LP), where the
      primal's first coordinates are the local log-variables;
  (v) minimum exponents per part and eps, compared with the claims (2 at eps = 0; 1.6 at eps0 = 1/10; 1.8 for u > 1).
"""
import sys, os, json, gzip
from fractions import Fraction as Fr
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
arc = os.path.join(os.path.dirname(HERE), 'logs', 'r2_bubble_certificates_items_big_small_eps0_1o10.json.gz')
recs = json.load(gzip.open(arc))
ncert = 0; status = Counter(); bad_exp = 0; bad_S = 0; bad_dim = 0; bad_cons = 0; nocons = 0
minexp = defaultdict(lambda: None)
for R in recs:
    rec = R['record']; status[rec.get('status')] += 1
    certs = rec.get('certs', [])
    ncert += len(certs)
    if certs:
        mx = max(Fr(c['value']) for c in certs)
        if Fr(rec['exponent']) != -2*mx:
            bad_exp += 1
    key = (R['part'], R['eps'])
    e = Fr(rec['exponent'])
    if minexp[key] is None or e < minexp[key]:
        minexp[key] = e
    cons = rec.get('cons', [])
    for c in certs:
        sup = sorted(int(i) for i, v in c['dual'].items() if Fr(v) > 0)
        if sup != sorted(c['Splus']):
            bad_S += 1
        if c.get('dim_bound') != c.get('dim_bound_r1'):
            bad_dim += 1
        x = [Fr(v) for v in c['primal']]
        if not cons:
            nocons += 1
        for (row, rhs) in cons:
            lhs = sum(Fr(a)*x[j] for j, a in enumerate(row))
            if lhs > Fr(rhs):
                bad_cons += 1
                break
print(f"piece records: {len(recs)}, monomial certificates: {ncert}, statuses: {dict(status)}")
print(f"exponent != -2*max(value): {bad_exp};  Splus != dual support: {bad_S};  dim_bound changed by S+ repair: {bad_dim}")
print(f"primal points violating the archived cell constraints: {bad_cons}  (certificates without cell constraints: {nocons})")
for k in sorted(minexp, key=lambda t: (t[0], t[1])):
    print(f"   min exponent  part={k[0]!r:28s} eps={k[1]:>5s}: {minexp[k]}  (= {float(minexp[k]):.3f})")
