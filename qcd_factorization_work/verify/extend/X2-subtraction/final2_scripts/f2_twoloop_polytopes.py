"""X2 final2 / f2_twoloop_polytopes.py -- Fix 4(a) of the final review: discharge of (RA2) (and of (RA1) for the nine
single-approximator terms) of the two-loop planar off-shell vertex via the Euler-Mellin theorems of Berkesch-Forsgard-
Passare (Michigan Math. J. 63 (2014) 101; arXiv:1103.6273), Thm 2.2 (convergence) and Thm 2.4 (meromorphic continuation,
polar locus on the facet hyperplanes of the Newton polytope).

For every one of the 49 non-trivial zeroing patterns T_p Gamma of X2 Thm E.1/E.3 (file twoloop_patterns.json, key 'r'),
with the six lines g1=k1, g2=k2, a1=p1-k2, a2=p1-k1-k2, b1=p2+k2, b2=p2+k1+k2 (X2 coordinates, line factor -V^2, the
coordinate zeroing of X2 applied):
  (1) the Schwinger/Lee-Pomeransky polynomials are computed EXACTLY from sum_l x_l D_l = -k^T M k + 2 B.k + C
      (Minkowski dot products, light-cone components):  U = det M,  F = U (C + B^T M^{-1} B);
  (2) positivity: every coefficient of U and F (as polynomials in x, P, P', m2) is positive;
  (3) the Newton polytope Delta_G of G = U + F (support in the six Schwinger parameters) -- its dimension;
      singles: full dimension 6 is required by BFP Thm 2.4; composites: dimension < 6 (scaleless => the
      Euler-Mellin integral converges nowhere, consistent with X2 Thm E.3(i));
  (4) singles: ALL facets of Delta_G, by exact brute-force enumeration over 6-point subsets of the support (complete:
      every facet contains 6 affinely independent support points), with primitive inward normals mu and
      nu = min_{Delta_G} <mu,.>;
  (5) singles: the (RA2) criterion -- every facet with nu = 0 has <mu, 1> >= 1 -- so that no polar hyperplane
      <mu, 1+delta> - nu (2-eps) = -n (n in N_0) of BFP Thm 2.4 contains a neighbourhood of a point (eps, 0) with
      eps outside a discrete set; the discrete set Z_R = {eps : <mu,1> - nu(2-eps) in -N_0 for some facet with nu != 0}
      near eps = 0 is listed;
  (6) singles: the pure-DR convergence set {eps real : <mu_k, 1> > nu_k (2 - eps) for all k} (BFP Thm 2.2 with
      s = 1, t = 2 - eps), i.e. whether the single converges absolutely in pure DR on an open eps-interval.
Run: python3 -I f2_twoloop_polytopes.py  (log: ../final2_logs/f2_twoloop_polytopes.log)"""
import sys, os, json, itertools
from fractions import Fraction as Fr
from math import gcd
from functools import reduce
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
PAT = json.load(open(os.path.join(os.path.dirname(HERE), 'scripts', 'twoloop_patterns.json')))

P, Pp, m2 = sp.symbols('P Pp m2', positive=True)
k1p, k1m, k1x, k1y, k2p, k2m, k2x, k2y = sp.symbols('k1p k1m k1x k1y k2p k2m k2x k2y', real=True)
COMP = [k1p, k1m, k1x, k1y, k2p, k2m, k2x, k2y]
LINES = ['g1', 'g2', 'a1', 'a2', 'b1', 'b2']
X = sp.symbols('x_g1 x_g2 x_a1 x_a2 x_b1 x_b2', positive=True)

def vec(p, m, x, y): return (sp.sympify(p), sp.sympify(m), sp.sympify(x), sp.sympify(y))
def add(*terms):
    out = [0, 0, 0, 0]
    for s, v in terms:
        for i in range(4): out[i] += s*v[i]
    return tuple(out)
def dot(v, w): return sp.expand(v[0]*w[1] + v[1]*w[0] - v[2]*w[2] - v[3]*w[3])
K1 = vec(k1p, k1m, k1x, k1y); K2 = vec(k2p, k2m, k2x, k2y)
def p1(mm): return vec(P, -mm/(2*P), 0, 0)
def p2(mm): return vec(mm/(2*Pp), -Pp, 0, 0)

def line_factor(name, zset):
    """X2's zeroed line factor -V^2: zero the listed light-cone components of k1, k2; 'M' sets m2 -> 0 in this line."""
    mm = 0 if 'M' in zset else m2
    sub = {}
    if 'k1+' in zset: sub[k1p] = 0
    if 'k1-' in zset: sub[k1m] = 0
    if 'k1T' in zset: sub[k1x] = 0; sub[k1y] = 0
    if 'k2+' in zset: sub[k2p] = 0
    if 'k2-' in zset: sub[k2m] = 0
    if 'k2T' in zset: sub[k2x] = 0; sub[k2y] = 0
    k1 = tuple(c.subs(sub) for c in K1); k2 = tuple(c.subs(sub) for c in K2)
    V = {'g1': k1, 'g2': k2, 'a1': add((1, p1(mm)), (-1, k2)), 'a2': add((1, p1(mm)), (-1, k1), (-1, k2)),
         'b1': add((1, p2(mm)), (1, k2)), 'b2': add((1, p2(mm)), (1, k1), (1, k2))}[name]
    # NB: p_i^2 = -m2 enters through -V^2 of the unzeroed momentum; X2's zeroing acts on the line momentum
    return sp.expand(-dot(V, V))

def UF(factors):
    S = sp.expand(sum(x*f for x, f in zip(X, factors)))
    H = sp.Matrix(8, 8, lambda i, j: sp.diff(S, COMP[i], COMP[j])/2)
    J = sp.Matrix([sp.diff(S, c).subs({cc: 0 for cc in COMP}) for c in COMP])
    C = S.subs({cc: 0 for cc in COMP})
    # M_ij from -k^T M k:  the coefficient of k_i^+ k_j^- in S is -M_ij  (i, j = 1, 2)
    idx = {1: (0, 1), 2: (4, 5)}
    M = sp.Matrix(2, 2, lambda i, j: -sp.diff(S, COMP[idx[i + 1][0]], COMP[idx[j + 1][1]]))
    U = sp.expand(M.det())
    if U == 0:
        return None, None, None
    Hinv = H.inv()
    Delta = sp.together(C - (J.T*Hinv*J)[0, 0]/4)
    F = sp.factor(sp.expand(sp.cancel(U*Delta)))
    F = sp.expand(F)
    return U, F, M

def positive_coeffs(poly_expr):
    if poly_expr == 0: return True
    pol = sp.Poly(poly_expr, *X, P, Pp, m2)
    return all(c > 0 for c in pol.coeffs())

def support(G):
    return sorted({m for m in sp.Poly(G, *X).monoms()})

def rank_fr(rows):
    M = [[Fr(x) for x in r] for r in rows]; rk = 0; nc = len(M[0]) if M else 0
    for col in range(nc):
        piv = next((i for i in range(rk, len(M)) if M[i][col] != 0), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]
        for i in range(len(M)):
            if i != rk and M[i][col] != 0:
                f = M[i][col]/M[rk][col]; M[i] = [a - f*b for a, b in zip(M[i], M[rk])]
        rk += 1
    return rk

def affine_dim(pts):
    if len(pts) <= 1: return 0
    base = pts[0]
    return rank_fr([[a - b for a, b in zip(p, base)] for p in pts[1:]])

def nullvec(rows, n):
    """exact non-zero solution of rows . y = 0 (rows: list of length-n lists), assuming corank 1"""
    M = [[Fr(x) for x in r] for r in rows]; piv_cols = []; rk = 0
    for col in range(n):
        piv = next((i for i in range(rk, len(M)) if M[i][col] != 0), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]
        pv = M[rk][col]; M[rk] = [a/pv for a in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][col] != 0:
                f = M[i][col]; M[i] = [a - f*b for a, b in zip(M[i], M[rk])]
        piv_cols.append(col); rk += 1
    free = [c for c in range(n) if c not in piv_cols]
    if len(free) != 1: return None
    fc = free[0]; y = [Fr(0)]*n; y[fc] = Fr(1)
    for r, pc in enumerate(piv_cols): y[pc] = -M[r][fc]
    return y

def facets(pts):
    """all facets of conv(pts) in R^N (N = 6), exact: (mu primitive inward integer normal, nu)"""
    N = len(pts[0]); found = {}
    for sub in itertools.combinations(range(len(pts)), N):
        Q = [pts[i] for i in sub]
        if affine_dim(Q) != N - 1: continue
        # hyperplane <mu, x> = nu through Q:  [x, -1] . (mu, nu) = 0
        y = nullvec([list(q) + [-1] for q in Q], N + 1)
        if y is None: continue
        mu, nu = y[:N], y[N]
        vals = [sum(m_*p_ for m_, p_ in zip(mu, p)) - nu for p in pts]
        if all(v >= 0 for v in vals): pass
        elif all(v <= 0 for v in vals): mu = [-m_ for m_ in mu]; nu = -nu
        else: continue
        den = reduce(lambda a, b: a*b//gcd(a, b), [x.denominator for x in mu + [nu]], 1)
        mi = [int(x*den) for x in mu]; ni = int(nu*den)
        g = reduce(gcd, [abs(x) for x in mi if x != 0])
        mi = tuple(x//g for x in mi); ni = ni//g
        found[mi] = ni
    return found

def main():
    Z = PAT['Z']; singles = {R: [Z[R][ln] for ln in LINES] for R in Z}
    pats = [(pz, c) for pz, c in PAT['r'] if any(len(z) for z in pz)]
    print(f"non-trivial patterns in the remainder decomposition: {len(pats)}")
    def key(pz): return tuple(tuple(sorted(z)) for z in pz)
    single_keys = {key(v): R for R, v in singles.items()}
    out = {}; ok_all = True
    print("\n=== composites (40): U, F positivity and dim Newt(U+F) (< 6 expected: scaleless) ===")
    ncomp = 0; comp_dims = {}
    for pz, c in pats:
        if key(pz) in single_keys: continue
        ncomp += 1
        U, F, M = UF([line_factor(ln, z) for ln, z in zip(LINES, pz)])
        if U is None:
            comp_dims.setdefault('singular M', 0); comp_dims['singular M'] += 1; continue
        G = sp.expand(U + F); sup = support(G); dm = affine_dim(sup)
        pos = positive_coeffs(U) and positive_coeffs(F)
        comp_dims[(dm, pos)] = comp_dims.get((dm, pos), 0) + 1
        if dm >= 6: ok_all = False; print("   composite with full-dimensional polytope:", pz)
    print(f"   {ncomp} composites; (dim, positive) counts: {comp_dims}")
    print("\n=== singles (9) ===")
    for R in ['HH', 'HC1', 'HC2', 'C1C1', 'C2C2', 'HS', 'C1S', 'C2S', 'SS']:
        pz = singles[R]
        factors = [line_factor(ln, z) for ln, z in zip(LINES, pz)]
        U, F, M = UF(factors)
        pos = positive_coeffs(U) and positive_coeffs(F)
        G = sp.expand(U + F); sup = support(G); dm = affine_dim(sup)
        print(f"\n-- {R}: line factors:")
        for ln, f in zip(LINES, factors): print(f"     {ln}: {f}")
        print(f"   U = {U}")
        print(f"   F = {sp.factor(F)}")
        print(f"   positive coefficients: {pos};  support size {len(sup)};  dim Newt(G) = {dm}")
        if not pos or dm != 6:
            ok_all = False; continue
        fac = facets(sup)
        bad = [(mu, nu) for mu, nu in fac.items() if nu == 0 and sum(mu) < 1]
        # pure-DR convergence interval: <mu,1> > nu (2 - eps) for all facets
        lo, hi = -sp.oo, sp.oo
        for mu, nu in fac.items():
            s1 = sum(mu)
            # s1 - 2 nu + nu eps > 0
            if nu > 0: lo = max(lo, sp.Rational(2*nu - s1, nu))
            elif nu < 0: hi = min(hi, sp.Rational(2*nu - s1, nu))
            elif s1 <= 0: lo, hi = sp.oo, -sp.oo
        conv = (lo < hi)
        # poles at delta = 0 near eps = 0 (|eps| <= 1): s1 - 2 nu + nu eps = -n
        poles = set()
        for mu, nu in fac.items():
            if nu == 0: continue
            s1 = sum(mu)
            for n in range(0, 40):
                e = sp.Rational(-n - s1 + 2*nu, nu)
                if abs(e) <= 1: poles.add(e)
        print(f"   facets: {len(fac)};  facets with nu = 0: {sorted((mu, sum(mu)) for mu, nu in fac.items() if nu == 0)}")
        print(f"   (RA2) criterion (every nu = 0 facet has <mu,1> >= 1): {'PASS' if not bad else 'FAIL ' + str(bad)}")
        print(f"   pure-DR absolute convergence set (BFP Thm 2.2, delta = 0): "
              f"{'eps in (' + str(lo) + ', ' + str(hi) + ')' if conv else 'EMPTY'}")
        print(f"   possible poles of I_R(eps, 0) with |eps| <= 1 (from facets with nu != 0): {sorted(poles)}")
        out[R] = dict(U=str(U), F=str(F), support=sup, facets={str(k): v for k, v in fac.items()},
                      ra2=not bad, conv=[str(lo), str(hi)] if conv else None, poles=[str(p) for p in sorted(poles)])
        ok_all &= (not bad)
    json.dump(out, open(os.path.join(os.path.dirname(HERE), 'final2_logs', 'f2_twoloop_polytopes.json'), 'w'), indent=1, default=str)
    print("\nALL SINGLES SATISFY THE (RA2) CRITERION; ALL COMPOSITES DEGENERATE" if ok_all else "\nSOME CHECK FAILED")

if __name__ == "__main__":
    main()
