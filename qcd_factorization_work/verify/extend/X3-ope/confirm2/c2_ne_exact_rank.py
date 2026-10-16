#!/usr/bin/env python3
"""
Independent check of Lemma NE(ii)(gamma) (X3-ope_final2.md), written before reading fix4_ne_demand.py / fr_ne_rank.py.

Claim tested: for Lambda^{r'}-valued O(D)-equivariant polynomials in a null vector z (degree n) and S further
vectors (total degree S), a D=4-only linear relation among the formal-D contraction structures needs
S >= n+6-r' (r'=0: n+6). Below that threshold the formal structures stay linearly independent at D=4.

Method (exact; different from floating-point SVD):
 * multilinear case (S distinct vectors of degree 1) -- universal by polarisation;
 * D=4 realised over Q with metric diag(1,1,-1,-1); z is a RATIONAL null vector;
 * each sample point contributes one functional (wedge components contracted with a random integer covector);
   npts = #structures + 10 (a first version with fewer points produced spurious deficiencies: for r'=1 all
   Z_D=1 structures carry the vector z, so one point gives one functional for that whole family; see
   logs/c2_ne_dcheck*.log);
 * rank mod p = 2^31-1; rank = #structures CERTIFIES independence over Q (a non-zero minor mod p is non-zero over Q).
 * controls at the threshold S = n+6-r': a deficiency must appear (D=4-only relation exists).
"""
import sys, os, itertools, random
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'c2_ne_lib.py')).read())
random.seed(31337)

def test4(n, S, rp, D=4):
    st = structures(n, S, rp); ns = len(st)
    if ns == 0: return 0, 0
    npts = ns + max(40, ns//3)   # generous oversampling (ns+10 gave spurious deficiencies, see logs/c2_ne_diag3.log)
    rows = [[0]*npts for _ in range(ns)]
    comps = list(itertools.combinations(range(D), rp))
    for j in range(npts):
        z = rand_null_D(D)
        vs = [[random.randint(-1000, 1000) for _ in range(D)] for _ in range(S)]
        xi = [random.randint(-50, 50) for _ in comps]
        for i, (A, zp, m) in enumerate(st):
            vecs = [z if a == 'z' else vs[a] for a in A]
            val = 1
            for v in zp: val = val * dot_D(z, vs[v], D) % P
            for (a, b) in m: val = val * dot_D(vs[a], vs[b], D) % P
            w = wedge_int_D(vecs, D)
            rows[i][j] = (val * (sum(c*x for c, x in zip(w, xi)) % P)) % P
    return ns, rank_mod_p(rows)

allok = True
def run(n, S, rp, expect_full):
    global allok
    ns, rk = test4(n, S, rp)
    if ns == 0:
        status = 'vacuous (no structure of this multidegree exists)'; ok = expect_full
    else:
        full = (rk == ns); ok = (full == expect_full)
        status = f'#struct={ns} rank={rk} ' + ('FULL' if full else f'deficiency {ns-rk}')
    allok &= ok
    print(f"[{'PASS' if ok else 'FAIL'}] n={n} r'={rp} S={S} (threshold {n+6-rp}) expect "
          f"{'independent' if expect_full else 'D=4 relation'}: {status}", flush=True)

print("== maximal supply: b=0 -> S=n+4 (incl. w1,w2), r'=0; b=1 -> S=n+1, r'=1..4: expect independence")
for n in range(2, 8): run(n, n+4, 0, True)
for n in range(2, 10):
    for rp in [1, 2, 3, 4]: run(n, n+1, rp, True)
print("== beyond the supply but below threshold, S = n+5-r' (and S=n+5, r'=0): expect independence")
for n in range(2, 6): run(n, n+5, 0, True)
for n in range(2, 6):
    for rp in [1, 2, 3]:
        for S in range(n+2, n+6-rp): run(n, S, rp, True)
print("== at threshold S = n+6-r': expect a D=4-only relation (sharpness controls)")
run(2, 8, 0, False)
for n in [2, 3, 4, 5]: run(n, n+2, 4, False)
for n in [2, 3, 4]: run(n, n+3, 3, False)
for n in [2, 3]: run(n, n+4, 2, False)
run(2, 7, 1, False)
print("\nOVERALL:", "PASS" if allok else "FAIL")
