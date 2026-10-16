"""
fix4_ne_demand.py  (X3 final2, Fix 4: Lemma NE(ii)(beta)-(gamma))

Part 1 (combinatorics of the demand/supply count of Lemma NE(ii)(gamma)).
  A D=4-only relation is a combination of terms (5-antisymmetrizer) x (polynomial).  Types:
    G    : 5x5 Gram minor det(v_i.u_j): 10 vector slots (5 upper, 5 lower); the Dirac structure gamma^[r'] of the
           vertex (if any) lies entirely outside the minor;
    M_r  : mixed antisymmetrizer, r Dirac indices (1 <= r <= r') + (5-r) vectors in the upper set, 5 vectors in the
           lower set; the other r'-r Dirac indices lie outside;
    G5   : gamma^[5] contracted with 5 vectors (needs r' >= 5).
  z (null, degree n) occupies at most one slot of each antisymmetrized set (Z_up, Z_low <= 1) and at most one
  Dirac index outside the antisymmetrizer (Z_D <= 1, only if such an index exists); every other z must be
  contracted with a non-z vector (z.z = 0).  Every outside Dirac index needs a distinct vector.
  Non-z demand  = (vector slots - Z_up - Z_low) + (outside Dirac indices - Z_D) + (n - Z_up - Z_low - Z_D).
  Supply        = (n + 2 - 3b) momentum/polarisation factors + 2 auxiliary vectors (w1, w2; B^- only).
  Claim checked: min demand = n+6 (b=0), n+6-r' >= n+2 (b=1, r' <= 4), > supply in every case; and
  the minimum is attained (so the count is sharp): n+6-r'.
Part 2 (numerical rank controls, using the final reviewer's evaluator
  verify/extend/X3-ope/review_final_scripts/fr_ne_rank.py, imported unchanged):
  (C5) Dirac rank 4, z^n and n+2 non-z vectors of degree 1   -> D=4-only relation exists (deficiency >= 1);
  (C6) Dirac rank 4, z^n and n+1 non-z vectors               -> no D=4-only relation (deficiency 0);
  (C7) Dirac ranks 0..4 together, z^n and n+1 non-z vectors  -> deficiency 0 (supply of b = 1 vertices);
  (C8) Dirac rank 3, z^n and n+3 non-z vectors -> deficiency >= 1; n+2 -> 0  (threshold n+6-r' for r' = 3).
Run: python3 -I fix4_ne_demand.py
"""
import sys, os, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.join(HERE, '..', 'review_final_scripts'))
ok_all = True

# ---------------- Part 1
def demands(n, b, rp):
    """all (type, demand) for a vertex with b bilinears and Dirac rank rp (rp = 0 if b = 0)"""
    out = []
    # Gram minor
    for Zu, Zl, ZD in itertools.product((0, 1), (0, 1), (0, 1)):
        if ZD and rp == 0: continue
        if Zu + Zl + ZD > n: continue
        dem = (10 - Zu - Zl) + (rp - ZD) + (n - Zu - Zl - ZD)
        out.append(("G", dem))
    # mixed M_r
    for r in range(1, min(rp, 5) + 1):
        if r == 5: continue
        for Zu, Zl, ZD in itertools.product((0, 1), (0, 1), (0, 1)):
            if ZD and rp - r == 0: continue
            if Zu + Zl + ZD > n: continue
            dem = (10 - r - Zu - Zl) + (rp - r - ZD) + (n - Zu - Zl - ZD)
            out.append(("M%d" % r, dem))
    # pure gamma^[5]
    if rp >= 5:
        for Z, ZD in itertools.product((0, 1), (0, 1)):
            if ZD and (rp - 5 == 0 or Z): continue
            dem = (5 - Z) + (rp - 5 - ZD) + (n - Z - ZD)
            out.append(("G5", dem))
    return out

print("Part 1: minimal non-z demand versus maximal supply")
part1 = True
for n in range(2, 31):
    for b, rps in ((0, (0,)), (1, (0, 1, 2, 3, 4))):
        for minus in (False, True):
            supply = (n + 2 - 3 * b) + (2 if minus else 0)
            for rp in rps:
                ds = demands(n, b, rp)
                mind = min(d for _, d in ds)
                expected = n + 6 if b == 0 else n + 6 - rp
                part1 &= (mind == expected) and (mind > supply)
            if n in (2, 3, 4, 12, 30):
                mins = {rp: min(d for _, d in demands(n, b, rp)) for rp in rps}
                print("   n=%2d b=%d %s supply=%2d  min demand by Dirac rank r': %s" % (n, b, "B^-" if minus else "B^+", supply, mins))
print("   min demand = n+6 (b=0), n+6-r' (b=1, r'<=4); demand > supply in all cases (n = 2..30): %s" % part1)
# chirality is not needed: even r' (0, 2, 4) also fail to meet the supply n+1
print("   b=1, r'=4 (even rank, chirality not assumed): demand n+2 > supply n+1 -> (gamma) holds without chirality")
ok_all &= part1

# ---------------- Part 2
import numpy as np
import fr_ne_rank as F

def rank_test(n, nvec, ranks, minus=False):
    deg = {'z': n}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'][:nvec]
    for l in labels: deg[l] = 1
    if minus:
        deg['w1'] = 1; deg['w2'] = 1
    monos = F.monomials(deg, ranks)
    if not monos: return 0, 0, 0
    ns = F.nsamples(monos, True)
    r4, _ = F.rank(F.evaluate(monos, deg, 4, ns, True))
    r10, _ = F.rank(F.evaluate(monos, deg, 10, ns, True))
    return len(monos), r4, r10

print("Part 2: numerical rank controls (D=4 versus D=10 proxy; fr_ne_rank evaluator)")
part2 = True
for n in (2, 3):
    nm, r4, r10 = rank_test(n, n + 2, (4,))
    c5 = (r10 == nm) and (nm - r4 >= 1)
    print("   (C5) n=%d rank-4 Dirac, %d non-z vectors (= n+2): #mono=%d rank4=%d rank10=%d deficiency=%d (>=1 expected) %s"
          % (n, n + 2, nm, r4, r10, nm - r4, c5))
    nm, r4, r10 = rank_test(n, n + 1, (4,))
    c6 = (nm == 0) or ((r10 == nm) and (nm - r4 == 0))
    print("   (C6) n=%d rank-4 Dirac, %d non-z vectors (= n+1): #mono=%d rank4=%d rank10=%d deficiency=%d (0 expected) %s"
          % (n, n + 1, nm, r4, r10, nm - r4, c6))
    nm, r4, r10 = rank_test(n, n + 1, (0, 1, 2, 3, 4))
    c7 = (r10 == nm) and (nm - r4 == 0)
    print("   (C7) n=%d ranks 0..4, %d non-z vectors (= n+1): #mono=%d rank4=%d rank10=%d deficiency=%d (0 expected) %s"
          % (n, n + 1, nm, r4, r10, nm - r4, c7))
    nm, r4, r10 = rank_test(n, n + 3, (3,))
    c8a = (r10 == nm) and (nm - r4 >= 1)
    nm2, r42, r102 = rank_test(n, n + 2, (3,))
    c8b = (r102 == nm2) and (nm2 - r42 == 0)
    print("   (C8) n=%d rank-3 Dirac: n+3 vectors deficiency=%d (>=1 expected) %s ; n+2 vectors deficiency=%d (0 expected) %s"
          % (n, nm - r4, c8a, nm2 - r42, c8b))
    part2 &= c5 and c6 and c7 and c8a and c8b
# B^- variant: supply n+1 consists of (n-1) momentum/polarisation factors + w1, w2
for n in (2, 3):
    nm, r4, r10 = rank_test(n, n - 1, (0, 1, 2, 3, 4), minus=True)
    c9 = (r10 == nm) and (nm - r4 == 0)
    print("   (C9) n=%d B^- : ranks 0..4, %d vectors + w1,w2 (supply n+1): #mono=%d rank4=%d rank10=%d deficiency=%d (0 expected) %s"
          % (n, n - 1, nm, r4, r10, nm - r4, c9))
    part2 &= c9
ok_all &= part2
print("RESULT:", "PASS" if ok_all else "FAIL")
