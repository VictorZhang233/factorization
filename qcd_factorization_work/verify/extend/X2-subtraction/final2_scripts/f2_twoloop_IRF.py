"""X2 final2 / f2_twoloop_IRF.py -- (IRF) for the planar and the crossed two-loop vertex graphs of (M1) (X2 §2, Cor A.5,
Thm E.3), with an explicit eps_0.

Feynman (projective) representation at delta = 0 (all powers 1), d/2 = 2 - eps, L = 2 loops, six lines:
     I = Gamma(2 + 2 eps) * J,   J = int_{simplex} U^{3 eps} F^{-2-2 eps}.
U, F are computed EXACTLY from the momentum routing (same code as f2_twoloop_polytopes.py); after P' = Qt2/(2P) every
coefficient is a polynomial in (Qt2, m2) with positive coefficients (boost invariance), so on R_+^6 each polynomial is
comparable within constant factors to its largest monomial and, in homogeneous log coordinates, the modulus of the
integrand is comparable to exp(psi_eps(r)),  psi_eps(r) = <1, r> + 3 eps h_U(r) - (2 + 2 eps) h_F(r),
h_V(r) = max_{v in supp V} <v, r>.  J converges absolutely iff psi_eps(r) < 0 for all r not in R(1,...,1).
Certificate at eps = 0: p = (1/2)(1,...,1) = sum_v lambda_v v with all lambda_v >= lambda_min > 0 (v in supp F), exact
rationals; then <1,r> - 2 h_F(r) <= -2 lambda_min osc_F(r).  Radius: on representatives with sum r_i = 0,
|3 h_U - 2 h_F| <= 12 max_i |r_i| <= 12 (max r - min r) <= 12 D osc_F(r), where D is the diameter of the graph on the six
coordinates with an edge {i, j} whenever e_i - e_j is a difference of two points of supp F (exact BFS).  Hence J converges
absolutely for |eps| < lambda_min/(6 D): (IRF) with eps_0 = lambda_min/(6 D) (any smaller positive number)."""
import sys, os, itertools
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np
from scipy.optimize import linprog
import functools
print = functools.partial(print, flush=True)
import f2_twoloop_polytopes as TP

Qt2 = sp.Symbol('Qt2', positive=True)
def full_graph_UF(kind):
    k1, k2 = TP.K1, TP.K2; p1, p2 = TP.p1(TP.m2), TP.p2(TP.m2)
    if kind == 'planar':      # g1 = k1 (inner rung), g2 = k2 (outer rung), a1 = p1-k2, a2 = p1-k1-k2, b1 = p2+k2, b2 = p2+k1+k2
        V = [k1, k2, TP.add((1, p1), (-1, k2)), TP.add((1, p1), (-1, k1), (-1, k2)), TP.add((1, p2), (1, k2)),
             TP.add((1, p2), (1, k1), (1, k2))]
    else:                     # crossed: p1 line emits k1 then k2; p2 line absorbs k2 then k1
        V = [k1, k2, TP.add((1, p1), (-1, k1)), TP.add((1, p1), (-1, k1), (-1, k2)), TP.add((1, p2), (1, k2)),
             TP.add((1, p2), (1, k1), (1, k2))]
    fs = [sp.expand(-TP.dot(v, v)) for v in V]
    U, F, M = TP.UF(fs)
    U = sp.expand(U/4); F = sp.expand(sp.factor(F)/4)
    F = sp.expand(sp.simplify(F.subs(TP.Pp, Qt2/(2*TP.P))))
    return U, F

def positive_poly(E):
    """every coefficient (as a polynomial in the six Schwinger parameters) is a polynomial in Qt2, m2 with positive
       coefficients and no dependence on P"""
    for c in sp.Poly(E, *TP.X).coeffs():
        c = sp.factor(sp.together(sp.expand(c)))
        if c.has(TP.P) or c.has(TP.Pp): return False
        n_, d_ = sp.fraction(c)
        pd = sp.Poly(d_, Qt2, TP.m2)
        if len(pd.coeffs()) != 1 or pd.coeffs()[0] <= 0: return False          # denominator: positive monomial
        if not all(x > 0 for x in sp.Poly(sp.expand(n_), Qt2, TP.m2).coeffs()): return False
    return True

def relint_certificate(S, p):
    """exact strictly positive rational convex combination sum lam_s s = p over the support S (affinely spanning the
       hyperplane sum x = 3); returns (lam dict, lam_min) or (None, None)"""
    S = [tuple(int(c) for c in s) for s in S]; n_ = len(S); dim = len(S[0])
    A_eq = np.array([[s[i] for s in S] for i in range(dim)] + [[1]*n_], float)
    b_eq = np.array([float(x) for x in p] + [1.0])
    c = np.zeros(n_ + 1); c[-1] = -1
    A_ub = np.hstack([-np.eye(n_), np.ones((n_, 1))]); b_ub = np.zeros(n_)
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=np.hstack([A_eq, np.zeros((dim + 1, 1))]), b_eq=b_eq,
                  bounds=[(0, None)]*n_ + [(None, 1)], method='highs')
    if not res.success or res.x[-1] <= 1e-9: return None, None
    lam = res.x[:n_]
    # exactify: fix all but an affine basis at rational approximations below the LP value, solve for the basis exactly
    order = sorted(range(n_), key=lambda i: -lam[i])
    basis = []
    for i in order:
        if TP.affine_dim([S[j] for j in basis + [i]]) == len(basis): basis.append(i)
        if len(basis) == dim: break
    # the support lies in the hyperplane sum x = 3: an affine basis has dim (= 6) points spanning a 5-dim affine space
    others = [i for i in range(n_) if i not in basis]
    L = {i: Fr(float(lam[i])).limit_denominator(10**4) for i in others}
    rhs = [Fr(x) for x in p] + [Fr(1)]
    for i in others:
        for k in range(dim): rhs[k] -= L[i]*S[i][k]
        rhs[dim] -= L[i]
    Mx = sp.Matrix([[S[b][k] for b in basis] for k in range(dim)] + [[1]*len(basis)])
    rv = sp.Matrix([sp.Rational(x.numerator, x.denominator) for x in rhs])
    sol, params = Mx.gauss_jordan_solve(rv)
    if params.shape[0] != 0: sol = sol.subs({t: 0 for t in params})
    lamx = dict(L); lamx.update({basis[j]: Fr(int(sp.fraction(sol[j])[0]), int(sp.fraction(sol[j])[1])) for j in range(len(basis))})
    # exact verification
    ok = (all(val > 0 for val in lamx.values()) and sum(lamx.values()) == 1 and
          all(sum(lamx[i]*S[i][k] for i in range(n_)) == Fr(p[k]) for k in range(dim)))
    if not ok: return None, None
    return lamx, min(lamx.values())

ALL_OK = True
for kind in ['planar', 'crossed']:
    U, F = full_graph_UF(kind)
    pos = positive_poly(U) and positive_poly(F)
    SU = TP.support(U); SF = TP.support(F)
    print(f"{kind} two-loop vertex:")
    print(f"   U = {sp.factor(U)}")
    print(f"   F = {sp.factor(F)}")
    print(f"   positive coefficients in (Qt2, m2), P-independent: {pos};  |supp U| = {len(SU)}, |supp F| = {len(SF)},"
          f" affine dim supp F = {TP.affine_dim(SF)}")
    lam, lmin = relint_certificate(SF, [Fr(1, 2)]*6)
    print(f"   p = (1/2)(1,...,1) in relint Newt(F): {lam is not None}  (exact certificate; lambda_min = {lmin})")
    if lam is None:
        ALL_OK = False; continue
    edges = set()
    for f_, g_ in itertools.permutations(SF, 2):
        dlt = [a - b for a, b in zip(f_, g_)]
        if sorted(dlt) == [-1, 0, 0, 0, 0, 1]:
            edges.add((dlt.index(1), dlt.index(-1)))
    adj = {i: set() for i in range(6)}
    for i, j in edges: adj[i].add(j); adj[j].add(i)
    def bfs(s0):
        dist = {s0: 0}; fr = [s0]
        while fr:
            nf = []
            for x in fr:
                for y in adj[x]:
                    if y not in dist: dist[y] = dist[x] + 1; nf.append(y)
            fr = nf
        return dist
    dists = [bfs(i) for i in range(6)]
    connected = all(len(dd) == 6 for dd in dists)
    if not connected:
        print("   coordinate graph not connected: no explicit radius"); ALL_OK = False; continue
    Dm = max(max(dd.values()) for dd in dists)
    rad = lmin/(6*Dm)
    print(f"   coordinate-difference graph connected, diameter D = {Dm};  J converges absolutely for |eps| < "
          f"lambda_min/(6D) = {rad} = {float(rad):.3g}  (delta = 0):  (IRF) holds with eps_0 = {rad}")
    # sanity: the tropical function at random rays for eps = rad/2 (floating point)
    rng = np.random.default_rng(1)
    SUa = np.array(SU, float); SFa = np.array(SF, float)
    worst = -np.inf
    for _ in range(20000):
        r = rng.normal(size=6); r -= r.mean()
        e = float(rad)/2
        psi = r.sum() + 3*e*np.max(SUa @ r) - (2 + 2*e)*np.max(SFa @ r)
        worst = max(worst, psi/np.max(np.abs(r)))
    print(f"   check: max over 20000 random rays of psi_eps(r)/max|r_i| at eps = eps_0/2: {worst:.4f} (< 0)")
    ALL_OK &= worst < 0 and pos
print("\nALL CHECKS PASS" if ALL_OK else "\nSOME CHECK FAILED")
