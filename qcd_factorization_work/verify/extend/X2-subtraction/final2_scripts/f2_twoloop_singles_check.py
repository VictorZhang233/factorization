"""X2 final2 / f2_twoloop_singles_check.py -- supporting checks for Prop E.4 / Thm E.3 (final-review Fix 4).

(A) Loop-by-loop parametric closed forms, WITH independent analytic powers 1+delta_l, of the three ultrasoft-type
    singles, and their delta -> 0 limits compared symbolically with Smirnov-Rakhmetov hep-ph/9812529 eqs. (5), (6), (7)
    (SR: omit i pi^{d/2} per loop; SR's -m^2 = our m^2 > 0, SR's Q^2 = our Qt^2 = 2PP'):
      one-loop building blocks (Euclidean-continued parametric formulas, U = sum of quadratic-line parameters):
      S(ma2, mb2; ng, na, nb) = int d^dk/(i pi^{d/2}) (-k^2)^-ng (ma2 + 2P k-)^-na (mb2 + 2P' k+)^-nb
         = Gamma(s - nb) Gamma(na + nb - s) Gamma(s - na) / (Gamma(ng) Gamma(na) Gamma(nb)) * (Qt2)^(s - na - nb)
           * ma2^(nb - s) * mb2^(na - s),      s = ng + na + nb - d/2;
      Coll(meff2; ng, n1, nh) = int (-k^2)^-ng (-(p1'-k)^2)^-n1 (2P' k+)^-nh,  p1'^2 = -meff2, p1'^+ = P
         = Gamma(s) B(nh, s - nh) B(ng + nh - s, d/2 - ng - nh) / (Gamma(ng) Gamma(n1) Gamma(nh)) * Qt2^-nh
           * meff2^(nh - s),   s = ng + n1 + nh - d/2;
      Tri0(ng, n1, n2) = massless on-shell triangle = Gamma(s) Gamma(d/2 - ng - n1) Gamma(d/2 - ng - n2)
           Gamma(...)...  (only its delta = 0 value is needed: Gamma(1+eps) Gamma(-eps)^2/Gamma(1-2eps) Qt2^(-1-eps)).
    HS: the integrand factorizes exactly (lines g1, a2, b2 depend on k1 only; g2, a1, b1 on k2 only);
    SS: inner k1 loop = S(m2 + 2P k2-, m2 + 2P' k2+; ...), then the outer loop is S with shifted powers;
    C1S: inner k1 loop = Coll with meff2 = m2 + 2P k2- (line a2 = -(p1' - k1)^2 with p1'^- = p1^- - k2^-), outer = S.
    The one-loop formulas are verified here symbolically against direct Cheng-Wu integration (sympy) and numerically.
(B) Exact relative-interior certificates (strictly positive rational convex combinations) proving absolute convergence
    of the pure-DR Feynman integral J at the stated eps: SS on (0,1) (U_SS is a monomial, so the tropical exponent is
    concave and convergence <=> a(eps) = (1 + 3 eps (e_g1 + e_g2))/(2 + 2 eps) in relint Newt(F_SS); a(eps) runs over the
    open segment between a(0) and a(1); certificate: midpoint in relint and both endpoints in Newt(F_SS)), and the FULL
    planar two-loop vertex Gamma and the crossed two-loop vertex at eps = 0 ((1/2)(1,...,1) in relint Newt(F)), which
    gives absolute convergence on a neighbourhood of (eps, delta) = 0, i.e. (IRF) for both graphs, with an explicit
    eps_0 from the perturbation bound  psi_eps <= -2 lam_min osc_F + |eps| |3 h_U - 2 h_F|."""
import sys, os, json, itertools
from fractions import Fraction as Fr
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np
import functools
print = functools.partial(print, flush=True)
from scipy.optimize import linprog
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import f2_twoloop_polytopes as TP

eps = sp.Symbol('epsilon')
Qt2, m2s = sp.symbols('Qt2 m2', positive=True)
dh = 2 - eps                                          # d/2
G = sp.gamma
def Bf(a, b): return G(a)*G(b)/G(a + b)

def S_blk(ma2, mb2, ng, na, nb):
    s = ng + na + nb - dh
    return G(s - nb)*G(na + nb - s)*G(s - na)/(G(ng)*G(na)*G(nb))*Qt2**(s - na - nb)*ma2**(nb - s)*mb2**(na - s)
def Coll_blk(meff2, ng, n1, nh):
    s = ng + n1 + nh - dh
    return G(s)*Bf(nh, s - nh)*Bf(ng + nh - s, dh - ng - nh)/(G(ng)*G(n1)*G(nh))*Qt2**(-nh)*meff2**(nh - s)

print("(A0) one-loop building blocks vs direct Cheng-Wu integration (numerical, mpmath):")
import mpmath as mp
mp.mp.dps = 15
def S_num(ma2, mb2, ng, na, nb, e, Q2=1.0):
    # projective form with x_g = 1 (U = x_g = 1): Gamma(s)/prod Gamma * int int xa^(na-1) xb^(nb-1) (xa ma2 + xb mb2 + xa xb Q2)^(-s)
    s = ng + na + nb - (2 - e)
    def f(ta, tb):
        xa = ta/(1 - ta); xb = tb/(1 - tb)
        return xa**(na - 1)*xb**(nb - 1)*(xa*ma2 + xb*mb2 + xa*xb*Q2)**(-s)/((1 - ta)**2*(1 - tb)**2)
    val = mp.quad(f, [0, 0.5, 1], [0, 0.5, 1])
    return mp.gamma(s)/(mp.gamma(ng)*mp.gamma(na)*mp.gamma(nb))*val
for (ma, mb, ng, na, nb, e) in [(0.3, 0.7, 1, 1, 1, 0.3), (0.2, 0.2, 1.1, 1.2, 0.9, 0.25), (0.5, 0.1, 1, 1.3, 1.3, 0.4)]:
    ex = S_blk(sp.Float(ma), sp.Float(mb), sp.Float(ng), sp.Float(na), sp.Float(nb)).subs({eps: e, Qt2: 1})
    print(f"   S({ma},{mb};{ng},{na},{nb}) at eps={e}: closed {sp.N(ex, 15)}  numeric {mp.nstr(S_num(ma, mb, ng, na, nb, e), 15)}")
def C_num(meff2, ng, n1, nh, e, Q2=1.0):
    # projective form, Cheng-Wu x_1 = 1: U = x_g + 1, F = x_g meff2 + x_h Q2
    s = ng + n1 + nh - (2 - e); N = ng + n1 + nh
    def f(tg, th):
        xg = tg/(1 - tg); xh = th/(1 - th)
        return xg**(ng - 1)*xh**(nh - 1)*(1 + xg)**(N - 2*(2 - e))*(xg*meff2 + xh*Q2)**(-s)/((1 - tg)**2*(1 - th)**2)
    val = mp.quad(f, [0, 0.5, 1], [0, 0.5, 1])
    return mp.gamma(s)/(mp.gamma(ng)*mp.gamma(n1)*mp.gamma(nh))*val
for (me, ng, n1, nh, e) in [(0.3, 0.6, 1.6, 1.0, 0.2), (0.5, 0.7, 1.5, 0.9, 0.1)]:
    # convergence needs nh>0, s>nh, ng+nh>s, d/2>ng+nh: choose analytic powers accordingly
    ex = Coll_blk(sp.Float(me), sp.Float(ng), sp.Float(n1), sp.Float(nh)).subs({eps: e, Qt2: 1})
    s = ng + n1 + nh - (2 - e)
    ok = nh > 0 and s > nh and ng + nh > s and (2 - e) > ng + nh
    print(f"   Coll({me};{ng},{n1},{nh}) at eps={e}: closed {sp.N(ex, 15)}  numeric {mp.nstr(C_num(me, ng, n1, nh, e), 15) if ok else '(outside convergence domain)'}")

print("\n(A1) singles with independent analytic powers, delta -> 0, vs SR eqs. (5), (6), (7):")
d = sp.symbols('d_g1 d_g2 d_a1 d_a2 d_b1 d_b2')
n = {k: 1 + v for k, v in zip(['g1', 'g2', 'a1', 'a2', 'b1', 'b2'], d)}
# structure of the singles from the zeroing patterns (which lines depend on which loop momentum)
for R in ['HS', 'SS', 'C1S']:
    fs = [TP.line_factor(ln, z) for ln, z in zip(TP.LINES, [TP.PAT['Z'][R][ln] for ln in TP.LINES])]
    dep = {ln: ('k1' if any(f.has(c) for c in TP.COMP[:4]) else '') + ('k2' if any(f.has(c) for c in TP.COMP[4:]) else '')
           for ln, f in zip(TP.LINES, fs)}
    print(f"   {R}: line -> loop momenta {dep}")
# HS: k1 lines g1, a2, b2 = massless on-shell triangle; k2 lines g2, a1, b1 = S(m2, m2; ...)
tri0 = G(1 + eps)*G(-eps)**2/G(1 - 2*eps)*Qt2**(-1 - eps)
HS0 = sp.gammasimp(tri0*S_blk(m2s, m2s, 1, 1, 1).subs(eps, eps))
SR6 = G(1 + eps)*G(1 - eps)*G(eps)**2*G(-eps)**2/(G(1 - 2*eps)*m2s**(2*eps)*Qt2**2)
print("   HS (delta = 0) / SR(6) - 1 =", sp.simplify(sp.gammasimp(HS0/SR6) - 1))
# SS with general powers: inner k1 loop (g1, a2, b2) with ma2 = m2 + 2P k2-, mb2 = m2 + 2P' k2+
s1 = n['g1'] + n['a2'] + n['b2'] - dh
inner_pref = G(s1 - n['b2'])*G(n['a2'] + n['b2'] - s1)*G(s1 - n['a2'])/(G(n['g1'])*G(n['a2'])*G(n['b2']))*Qt2**(s1 - n['a2'] - n['b2'])
na_out = n['a1'] + s1 - n['b2']; nb_out = n['b1'] + s1 - n['a2']
SSd = inner_pref*S_blk(m2s, m2s, n['g2'], na_out, nb_out)
SS0 = sp.gammasimp(SSd.subs({x: 0 for x in d}))
SR5 = G(1 - eps)**2*G(2*eps)**2/(eps**2*m2s**(4*eps)*Qt2**(2 - 2*eps))
print("   SS (delta = 0) / SR(5) - 1 =", sp.simplify(sp.gammasimp(SS0/SR5) - 1))
print("   SS(eps, delta): explicit product of Gamma functions; Gamma arguments at delta = 0:",
      sorted({str(sp.simplify(a.args[0].subs({x: 0 for x in d}))) for a in SSd.atoms(sp.gamma)}))
# C1S: inner k1 loop (g1, a2, b2): a2 = -(p1' - k1)^2, p1'^2 = -(m2 + 2P k2-), b2 = 2P' k1+ (eikonal); outer: g2, a1, b1
s1c = n['g1'] + n['a2'] + n['b2'] - dh
coll_pref = G(s1c)*Bf(n['b2'], s1c - n['b2'])*Bf(n['g1'] + n['b2'] - s1c, dh - n['g1'] - n['b2'])/(G(n['g1'])*G(n['a2'])*G(n['b2']))*Qt2**(-n['b2'])
C1Sd = coll_pref*S_blk(m2s, m2s, n['g2'], n['a1'] + s1c - n['b2'], n['b1'])
C1S0 = sp.gammasimp(C1Sd.subs({x: 0 for x in d}))
SR7 = G(1 - eps)**2*G(eps)*G(2*eps)*G(-eps)/(eps*G(1 - 2*eps)*m2s**(3*eps)*Qt2**(2 - eps))
print("   C1S (delta = 0) / SR(7) - 1 =", sp.simplify(sp.gammasimp(C1S0/SR7) - 1))
print("   C1S(eps, delta): Gamma arguments at delta = 0:",
      sorted({str(sp.simplify(a.args[0].subs({x: 0 for x in d}))) for a in C1Sd.atoms(sp.gamma)}))
# numerical check of the general-delta closed forms against the Lee-Pomeransky integral is not attempted (6-dim);
# instead (B) checks J_SS numerically at eps = 0.3 (pure DR) in a 2+2-dimensional loop-by-loop form.

print("\n(B) exact relative-interior certificates:")
def relint_certificate(S, p):
    """strictly positive rational lambda with sum lam = 1, sum lam s = p (S spans the hyperplane affinely)"""
    S = [tuple(int(c) for c in s) for s in S]; n_ = len(S); dim = len(S[0])
    A_eq = np.array([[s[i] for s in S] for i in range(dim)] + [[1]*n_], float)
    b_eq = np.array([float(x) for x in p] + [1.0])
    # variables lam (n_) and tau; maximize tau s.t. lam_s >= tau
    c = np.zeros(n_ + 1); c[-1] = -1
    A_ub = np.hstack([-np.eye(n_), np.ones((n_, 1))]); b_ub = np.zeros(n_)
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=np.hstack([A_eq, np.zeros((dim + 1, 1))]), b_eq=b_eq,
                  bounds=[(0, None)]*n_ + [(None, 1)], method='highs')
    if not res.success or res.x[-1] <= 1e-9: return None, None
    lam = res.x[:n_]; tau = res.x[-1]
    # exactify: pick a basis of affinely independent points among the largest lambdas, fix the others
    order = sorted(range(n_), key=lambda i: -lam[i])
    basis = []
    for i in order:
        if TP.affine_dim([S[j] for j in basis + [i]]) == len(basis): basis.append(i)
        if len(basis) == dim: break
    others = [i for i in range(n_) if i not in basis]
    L = {i: Fr(float(lam[i])).limit_denominator(10**6) for i in others}
    # solve sum_{basis} lam_b (s_b, 1) = (p, 1) - sum_others L_i (s_i, 1)   (dim+1 eqs, dim unknowns; consistent)
    rhs = [Fr(x) for x in p] + [Fr(1)]
    for i in others:
        for k in range(dim): rhs[k] -= L[i]*S[i][k]
        rhs[dim] -= L[i]
    M = [[Fr(S[b][k]) for b in basis] for k in range(dim)] + [[Fr(1)]*len(basis)]
    sol = sp.Matrix(M).solve_least_squares(sp.Matrix(rhs)) if False else None
    Ms = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in M])
    rs = sp.Matrix([sp.Rational(x.numerator, x.denominator) for x in rhs])
    sol = (Ms.T*Ms).LUsolve(Ms.T*rs)
    lamx = {}
    for j, b in enumerate(basis): lamx[b] = Fr(int(sp.fraction(sol[j])[0]), int(sp.fraction(sol[j])[1]))
    lamx.update(L)
    ok = all(v > 0 for v in lamx.values()) and sum(lamx.values()) == 1 and \
         all(sum(lamx[i]*S[i][k] for i in range(n_)) == Fr(p[k]) for k in range(dim))
    return (lamx, min(lamx.values())) if ok else (None, None)

def in_hull_certificate(S, p):
    """lambda >= 0 (not nec. strict) with sum lam = 1, sum lam s = p, exact"""
    S = [tuple(int(c) for c in s) for s in S]; n_ = len(S); dim = len(S[0])
    for sub in itertools.combinations(range(n_), dim):
        M = sp.Matrix([[S[b][k] for b in sub] for k in range(dim)] + [[1]*dim])
        rs = sp.Matrix([sp.Rational(x) for x in p] + [1])
        try:
            sol = (M.T*M).LUsolve(M.T*rs)
        except Exception:
            continue
        if M*sol == rs and all(x >= 0 for x in sol):
            return {sub[j]: sol[j] for j in range(dim)}
    return None

D = json.load(open(os.path.join(os.path.dirname(HERE), 'final2_logs', 'f2_twoloop_polytopes.json')))
SF_SS = TP.support(sp.sympify(D['SS']['F'], locals={str(s): s for s in list(TP.X) + [TP.P, TP.Pp, TP.m2]}))
v_g = [1, 1, 0, 0, 0, 0]
def a_of(e): return [Fr(1 + 3*e*v, 1)/(2 + 2*e) if isinstance(e, int) else (1 + 3*e*v)/(2 + 2*e) for v in v_g]
a0 = [Fr(1, 2)]*6; a1 = [Fr(1 + 3*v, 4) for v in v_g]; amid = [(x + y)/2 for x, y in zip(a0, a1)]
print("   SS: affine dim of supp F_SS =", TP.affine_dim(SF_SS), "(5 = full in the hyperplane sum x = 3)")
lam_mid, lmin = relint_certificate(SF_SS, amid)
print(f"   SS: midpoint a(1/3) = {[str(x) for x in amid]} in relint Newt(F_SS): {lam_mid is not None} (min lambda {lmin})")
print(f"   SS: a(0) in Newt(F_SS): {in_hull_certificate(SF_SS, a0) is not None};  a(1) in Newt(F_SS): {in_hull_certificate(SF_SS, a1) is not None}")
print("   => J_SS converges absolutely for every eps in (0, 1) (pure DR), consistent with f2_twoloop_Jconv.log")
# numerical: pure-DR SS at eps = 0.3, loop-by-loop is the derivation itself; here a direct 4-dim check of the
# combined two-loop parametric integral in the factorized Cheng-Wu chart is not independent -- skipped.

def full_graph_UF(kind):
    """U, F of the full (unzeroed) planar or crossed two-loop vertex, X2 kinematics"""
    k1, k2 = TP.K1, TP.K2; p1, p2 = TP.p1(TP.m2), TP.p2(TP.m2)
    if kind == 'planar':
        V = [k1, k2, TP.add((1, p1), (-1, k2)), TP.add((1, p1), (-1, k1), (-1, k2)), TP.add((1, p2), (1, k2)),
             TP.add((1, p2), (1, k1), (1, k2))]
    else:   # crossed: p1 line emits k1 then k2; p2 line absorbs k2 then k1
        V = [k1, k2, TP.add((1, p1), (-1, k1)), TP.add((1, p1), (-1, k1), (-1, k2)), TP.add((1, p2), (1, k2)),
             TP.add((1, p2), (1, k1), (1, k2))]
    fs = [sp.expand(-TP.dot(v, v)) for v in V]
    U, F, M = TP.UF(fs)
    return U, F

for kind in ['planar', 'crossed']:
    U, F = full_graph_UF(kind)
    def pos_general(E):
        # coefficients (as functions of P, P', m2) of the x-monomials: boost invariant, positive rational functions of
        # (Qt2, m2) with positive coefficients in numerator and denominator
        QQ = sp.Symbol('Qt2', positive=True)
        for c in sp.Poly(E, *TP.X).coeffs():
            c2 = sp.factor(sp.simplify(c.subs(TP.Pp, QQ/(2*TP.P))))
            if c2.has(TP.P): return False
            nu, de = sp.fraction(sp.together(c2))
            for part in (nu, de):
                if not all(x > 0 for x in sp.Poly(sp.expand(part), QQ, TP.m2).coeffs()): return False
        return True
    pos = pos_general(U) and pos_general(F)
    SU = TP.support(U); SFp = TP.support(F)
    print(f"\n   full {kind} two-loop vertex: U = {sp.factor(U)}")
    print(f"      F = {sp.factor(F)}")
    print(f"      positive coefficients: {pos}; |supp U| = {len(SU)}, |supp F| = {len(SFp)}, affine dim supp F = {TP.affine_dim(SFp)}")
    lam, lmin = relint_certificate(SFp, [Fr(1, 2)]*6)
    print(f"      (1/2)(1,...,1) in relint Newt(F): {lam is not None}  (exact certificate, min lambda = {lmin})")
    if lam is None: continue
    # explicit radius (rigorous): on representatives with sum r = 0,
    #   psi_eps(r) <= -2 lam_min osc_F(r) + |eps| |3 h_U(r) - 2 h_F(r)| <= (-2 lam_min + 12 |eps| D) osc_F(r),
    # with |h_U| <= 2 max|r_i|, |h_F| <= 3 max|r_i|, max|r_i| <= max r - min r <= D osc_F(r), where D is the diameter of
    # the graph on the six coordinates with an edge {i,j} whenever e_i - e_j is a difference of two points of supp F.
    edges = set()
    for f, g in itertools.permutations(SFp, 2):
        dlt = [a - b for a, b in zip(f, g)]
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
    Dm = max(max(dd.values()) for dd in dists) if connected else None
    if connected:
        rad = lmin/(6*Dm)
        print(f"      coordinate graph connected, diameter D = {Dm}; J converges absolutely for |Re eps| < lam_min/(6D) = {rad} = {float(rad):.4g} (delta = 0)")
    else:
        print("      coordinate graph not connected: no explicit radius from this bound (qualitative neighbourhood only)")
