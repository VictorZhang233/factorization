#!/usr/bin/env python3
"""
w04_landau.py -- writer W04 checks for Ch4 sec:ir-landau, sec:ir-coleman-norton and App D.
Run:  python3 -I w04_landau.py   (log: logs/w04_landau.log)

Conventions (book): metric (+,-,-,-); light front v^pm=(v0 pm v3)/sqrt2, v.w = v+w- + v-w+ - vT.wT;
D_j = q_j^2 - m_j^2, propagator 1/(-D_j - i0)^{nu_j} (VF-REG-1), D(alpha,k)=sum_j alpha_j (m_j^2-q_j^2),
U=det A, F = U * D(alpha,k_c).

L1  parametric representation: one-loop Gaussian step and Symanzik polynomials of the triangle
    (on-shell massless, off-shell Euclidean, massive legs), general two-forest formula
L2  envelope identity d(F/U)/d alpha_j = -D_j(k_c), homogeneity, Euler relation; exact for a two-loop graph
L3  constraint-preserving deformation (VF-REG-2): sum z = 1, first order -i tau eta V, real second order,
    V = sum alpha_j w_j^2 = sum alpha_j (dF_j)^2 - c^2 ; V=F=0 => Landau point
L4  alpha-space Landau sets: massless vertex, off-shell triangle (corners only), massive legs, massless box
L5  Euclidean positivity: F/U = min over Euclidean loop momenta (numerically), F >= 0 (one-loop box, two-loop)
L6  deformed simplex numerics for the massive vertex (m=1, gluon mass 0.3)
L7  Gordan alternative: exclusivity, min-norm margin; vertex points (collinear trapped, cut surface not)
L8  Cayley matrix of the massless vertex
L9  Coleman-Norton closure for the collinear pinch; soft scaling limit
L10 behaviour of F near the soft corner: off-shell (integrable) vs massive legs (log divergent)
L11 one-dimensional toy integrals: pinch, same side, endpoint (ex:ir-pinch-toy)
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import itertools, random
import numpy as np
import sympy as sp
import mpmath as mp
from scipy.optimize import minimize, linprog

RES = []
def check(name, cond):
    RES.append((name, bool(cond)))
    print(('PASS ' if cond else 'FAIL ') + name)

# ---------------------------------------------------------------- helpers (Minkowski, components (t,x,y,z))
MET = sp.diag(1, -1, -1, -1)
def mdot(a, b):
    return sum(MET[i, i]*a[i]*b[i] for i in range(4))

# =============================================================== L1 parametric representation
print('=== L1: parametric representation and Symanzik polynomials ===')
a0, a1, a2, a3 = sp.symbols('alpha0 alpha1 alpha2 alpha3', nonnegative=True)
p1sq, p2sq, qsq, m0, m1, m2 = sp.symbols('p1sq p2sq qsq m0 m1 m2', real=True)
p1p2 = sp.Symbol('p1p2', real=True)
# one loop, lines q0 = k, q1 = k - p1 (= -(p1-k)), q2 = k + p2 ; r0=0, r1=-p1, r2=p2
# U = A = sum alpha, B = sum alpha_j r_j, C = sum alpha_j (m_j^2 - r_j^2); F = U*C + B.B
A = a0 + a1 + a2
BB = a1**2*p1sq + a2**2*p2sq - 2*a1*a2*p1p2           # B.B with B = -a1 p1 + a2 p2
C = a0*m0**2 + a1*(m1**2 - p1sq) + a2*(m2**2 - p2sq)
F_gen = sp.expand(A*C + BB)
# two-forest formula: F = -(a1 a2 q^2 + a0 a1 p1^2 + a0 a2 p2^2) + U sum alpha_j m_j^2,  q = p1 + p2
F_2f = sp.expand(-(a1*a2*(p1sq + p2sq + 2*p1p2) + a0*a1*p1sq + a0*a2*p2sq) + A*(a0*m0**2 + a1*m1**2 + a2*m2**2))
check('L1 one-loop triangle: U*C + B.B equals the two-forest formula', sp.simplify(F_gen - F_2f) == 0)
Qsq, m = sp.symbols('Q2 m', positive=True)
F_onshell = sp.factor(F_2f.subs({m0: 0, m1: 0, m2: 0, p1sq: 0, p2sq: 0, p1p2: Qsq/2}))
check('L1 on-shell massless vertex: F = -Q^2 a1 a2', sp.simplify(F_onshell + Qsq*a1*a2) == 0)
F_off = sp.expand(F_2f.subs({m0: 0, m1: 0, m2: 0, p1sq: -m**2, p2sq: -m**2, p1p2: (-Qsq + 2*m**2)/2}))
check('L1 off-shell Euclidean triangle: F = m^2 a0 (a1+a2) + Q^2 a1 a2 (VF-REF-17)',
      sp.simplify(F_off - (m**2*a0*(a1 + a2) + Qsq*a1*a2)) == 0)
F_ml = sp.expand(F_2f.subs({m0: 0, m1: m, m2: m, p1sq: m**2, p2sq: m**2, p1p2: (-Qsq - 2*m**2)/2}))
check('L1 massive legs, massless gluon (q^2=-Q^2): F = Q^2 a1 a2 + m^2 (a1+a2)^2',
      sp.simplify(F_ml - (Qsq*a1*a2 + m**2*(a1 + a2)**2)) == 0)
print('   F(on-shell vertex)   =', F_onshell)
print('   F(off-shell triangle) =', sp.factor(F_off))
# Gaussian step: int d^Dk/(i pi^{D/2}) (-A k^2 - 2B.k + C - i0)^{-nu} = G(nu-D/2)/G(nu) A^{-D/2} (C+B^2/A)^{D/2-nu}
# check by the shift k = l - B/A and the master formula with Delta = C + B^2/A  (symbolic identity)
Asym, Bsq, Csym, lsq = sp.symbols('A Bsq C lsq', positive=True)
# -A k^2 - 2 B.k + C with k = l - B/A:  -A l^2 + 2 l.B - B^2/A - 2 B.l + 2 B^2/A + C = -A l^2 + B^2/A + C
lB = sp.Symbol('lB')
expr = -Asym*(lsq - 2*lB/Asym + Bsq/Asym**2) - 2*(lB - Bsq/Asym) + Csym
check('L1 shift k=l-B/A removes the linear term: -A l^2 + C + B^2/A', sp.simplify(expr - (-Asym*lsq + Csym + Bsq/Asym)) == 0)
# exponent bookkeeping: U^{-D/2} (F/U)^{LD/2-nu} = U^{nu-(L+1)D/2} F^{LD/2-nu}
L_, D_, nu_ = sp.symbols('L D nu')
check('L1 exponents: U^(-D/2)*(F/U)^(LD/2-nu) -> U^(nu-(L+1)D/2)', sp.simplify((-D_/2) - (L_*D_/2 - nu_) - (nu_ - (L_ + 1)*D_/2)) == 0)
# bubble normalisation check of VF-REG-1 (massless, Euclidean p^2<0): parametric = Gamma(eps) B(1-eps,1-eps) (-p^2)^(-eps)
eps = sp.Symbol('epsilon')
x = sp.Symbol('x', positive=True)
param = sp.gamma(eps)*sp.integrate((x*(1 - x))**(-eps), (x, 0, 1), conds='none')
known = sp.gamma(eps)*sp.gamma(1 - eps)**2/sp.gamma(2 - 2*eps)
check('L1 massless bubble: parametric form equals Gamma(eps)Gamma(1-eps)^2/Gamma(2-2eps)',
      abs(complex(sp.N((param - known).subs(eps, sp.Rational(-3, 10)), 30))) < 1e-20)

# =============================================================== L2 envelope identity (two loops, exact)
print('=== L2: envelope identity, homogeneity, Euler relation (two-loop graph, exact rationals) ===')
random.seed(7)
def rvec():
    return sp.Matrix([sp.Rational(random.randint(-9, 9), random.randint(1, 5)) for _ in range(4)])
def symanzik(lines, alphas, L):
    """lines: list of (eta (tuple len L), r (4-vector), msq). returns U, F, k_c (list of L 4-vectors), D(alpha,k) at k_c"""
    ks = [sp.Matrix(sp.symbols('k%d_0:4' % l)) for l in range(L)]
    Dform = 0
    for (eta, r, msq), al in zip(lines, alphas):
        q = sum((eta[l]*ks[l] for l in range(L)), sp.zeros(4, 1)) + r
        Dform += al*(msq - mdot(q, q))
    vars_ = [c for kk in ks for c in kk]
    sol = sp.solve([sp.diff(Dform, v) for v in vars_], vars_, dict=True)[0]
    Amat = sp.Matrix(L, L, lambda i, j: sum(al*eta[i]*eta[j] for (eta, r, msq), al in zip(lines, alphas)))
    U = sp.expand(Amat.det())
    Dc = sp.simplify(Dform.subs(sol))
    F = sp.expand(sp.simplify(U*Dc))
    kc = [kk.subs(sol) for kk in ks]
    return U, F, kc, Dc
# two-loop planar vertex-like graph: 5 lines, loop momenta k0, k1
al = sp.symbols('b0:5', positive=True)
pA, pB = rvec(), rvec()
lines2 = [((1, 0), sp.zeros(4, 1), sp.Rational(1, 3)),
          ((1, 0), -pA, 0),
          ((0, 1), pA, sp.Rational(2, 5)),
          ((1, -1), sp.zeros(4, 1), 0),
          ((0, 1), -pB, 1)]
U2, F2, kc2, Dc2 = symanzik(lines2, al, 2)
ok_env = True
for j, (eta, r, msq) in enumerate(lines2):
    q = sum((eta[l]*kc2[l] for l in range(2)), sp.zeros(4, 1)) + r
    Dj = mdot(q, q) - msq
    lhs = sp.diff(F2/U2, al[j])
    if sp.simplify(lhs + Dj) != 0:
        ok_env = False
check('L2 two-loop graph: d(F/U)/d alpha_j = -D_j(k_c) for all five lines', ok_env)
t = sp.Symbol('t', positive=True)
check('L2 homogeneity: U degree L=2, F degree L+1=3',
      sp.simplify(U2.subs({a: t*a for a in al}) - t**2*U2) == 0 and sp.simplify(F2.subs({a: t*a for a in al}) - t**3*F2) == 0)
check('L2 Euler relation: sum alpha_j dF/d alpha_j = (L+1) F', sp.simplify(sum(a*sp.diff(F2, a) for a in al) - 3*F2) == 0)
# one-loop triangle, symbolic check of the envelope identity with explicit vectors
P1, P2 = rvec(), rvec()
lines1 = [((1,), sp.zeros(4, 1), 0), ((1,), -P1, 0), ((1,), P2, 0)]
U1, F1, kc1, Dc1 = symanzik(lines1, (a0, a1, a2), 1)
check('L2 triangle: k_c = (a1 p1 - a2 p2)/U', all(sp.simplify(kc1[0][i] - (a1*P1[i] - a2*P2[i])/(a0 + a1 + a2)) == 0 for i in range(4)))

# =============================================================== L3 deformation identities
print('=== L3: constraint-preserving deformation (VF-REG-2) ===')
tau, eta_ = sp.symbols('tau eta', positive=True)
def deformation_checks(F, alphas, L, label):
    c = sum(a*sp.diff(F, a) for a in alphas)
    w = [sp.diff(F, a) - c for a in alphas]
    z = [a*(1 - sp.I*tau*eta_*wj) for a, wj in zip(alphas, w)]
    # restrict to the simplex: alpha_last = 1 - sum(others)
    sub = {alphas[-1]: 1 - sum(alphas[:-1])}
    s1 = sp.simplify(sp.expand(sum(z)).subs(sub) - 1) == 0
    Fz = F.subs(dict(zip(alphas, z)), simultaneous=True)
    ser = sp.series(Fz, eta_, 0, 4).removeO()
    c1 = sp.expand(ser.coeff(eta_, 1)).subs(sub)
    V = sum(a*sp.diff(F, a)**2 for a in alphas) - c**2
    s2 = sp.simplify(c1 + sp.I*tau*V.subs(sub)) == 0
    c2 = sp.expand(ser.coeff(eta_, 2))
    s3 = sp.simplify(sp.im(c2.subs({a: sp.Rational(random.randint(1, 9), 10) for a in alphas}))) == 0
    Vw = sum(a*wj**2 for a, wj in zip(alphas, w))
    s4 = sp.simplify((Vw - V).subs(sub)) == 0
    check('L3 %s: sum z_j = 1 on the simplex' % label, s1)
    check('L3 %s: dF(z)/d eta|_0 = -i tau V, V = sum a (dF)^2 - c^2' % label, s2)
    check('L3 %s: O(eta^2) coefficient real for real alpha, p' % label, s3)
    check('L3 %s: V = sum alpha_j w_j^2 (>= 0)' % label, s4)
mg, s_ = sp.symbols('mg s', positive=True)
F_mv = sp.expand(-(a1*a2*s_ + a0*a1*1 + a0*a2*1) + (a0 + a1 + a2)*(a0*mg**2 + a1*1 + a2*1))   # massive vertex, m=1
deformation_checks(F_mv, [a0, a1, a2], 1, 'massive vertex')
# a random homogeneous cubic (two-loop-like degree L+1=3) with four parameters
b = sp.symbols('c0:4', positive=True)
rng = random.Random(3)
cub = sum(sp.Rational(rng.randint(-5, 5), rng.randint(1, 3))*b[i]*b[j]*b[k]
          for i in range(4) for j in range(i, 4) for k in range(j, 4))
deformation_checks(sp.expand(cub), list(b), 2, 'random cubic (L=2)')
# V = F = 0 => Landau point (argument): if V=0 then dF_j = c for alpha_j>0; Euler: (L+1)F = c sum alpha = c
print('   (V=F=0 => dF_j=c on the support, (L+1)F = c => c=0 => alpha_j dF_j=0: Landau point)')

# =============================================================== L4 Landau sets
print('=== L4: alpha-space Landau sets ===')
def landau_points_scan(F, alphas, n=60, tol=1e-9, params=None):
    params = params or {}
    Fn = sp.lambdify(alphas, F.subs(params), 'numpy')
    dF = [sp.lambdify(alphas, sp.diff(F, a).subs(params), 'numpy') for a in alphas]
    pts = []
    N = len(alphas)
    grid = [c for c in itertools.product(range(n + 1), repeat=N - 1) if sum(c) <= n]
    for c in grid:
        al = [ci/n for ci in c] + [1 - sum(c)/n]
        v = [al[j]*dF[j](*al) for j in range(N)]
        if abs(Fn(*al)) < tol and max(abs(x) for x in v) < tol:
            pts.append(tuple(round(x, 6) for x in al))
    return pts
pts = landau_points_scan(-a1*a2, [a0, a1, a2])
edge_ok = all(abs(p[1]*p[2]) < 1e-12 for p in pts) and any(p[1] > 0.2 and p[2] == 0 for p in pts) and any(p[2] > 0.2 and p[1] == 0 for p in pts)
check('L4 massless vertex: Landau set = closed edges a1=0, a2=0 (no point with a1 a2 > 0)', edge_ok)
pts = landau_points_scan(F_off, [a0, a1, a2], params={m: 1, Qsq: 3})
check('L4 off-shell triangle: Landau set = the three corners only', sorted(pts) == sorted([(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0)]))
pts = landau_points_scan(F_ml, [a0, a1, a2], params={m: 1, Qsq: 3})
check('L4 massive legs + massless gluon: only the corner (1,0,0)', pts == [(1.0, 0.0, 0.0)])
y0, y1, y2, y3 = sp.symbols('y0:4', nonnegative=True)
s_b, t_b = sp.symbols('s_b t_b', positive=True)
F_box = -s_b*y0*y2 - t_b*y1*y3
pts = landau_points_scan(F_box, [y0, y1, y2, y3], n=24, params={s_b: 2, t_b: 3})
ok_box = all(abs(p[0]*p[2]) < 1e-12 and abs(p[1]*p[3]) < 1e-12 for p in pts)
supports = set(tuple(i for i in range(4) if p[i] > 0) for p in pts)
ok_box = ok_box and supports == {(0,), (1,), (2,), (3,), (0, 1), (1, 2), (2, 3), (0, 3)}
check('L4 massless box: Landau set = 4 corners + edges (01),(12),(23),(30) (VF-REG-5)', ok_box)
# exact case analysis for the off-shell triangle
eqs = [a1*(m**2*a0 + Qsq*a2), a2*(m**2*a0 + Qsq*a1), m**2*a0*(a1 + a2)]
print('   off-shell triangle: a_j dF_j =', [sp.factor(e) for e in eqs], ' (all terms >= 0 on the simplex)')

# =============================================================== L5 Euclidean positivity
print('=== L5: Euclidean kinematics: F/U = min_k D_E(alpha,k), F >= 0 ===')
def eucl_check(nlines_eta, rs, msqs, L, trials=40, seed=11):
    rng_ = np.random.default_rng(seed)
    ok, worst = True, 0.0
    for _ in range(trials):
        al = rng_.dirichlet(np.ones(len(rs)))
        Amat = np.zeros((L, L)); Bv = np.zeros((L, 4)); Cc = 0.0
        for (eta, r, ms), a in zip(zip(nlines_eta, rs, msqs), al):
            eta = np.array(eta, float)
            Amat += a*np.outer(eta, eta); Bv += a*np.outer(eta, r); Cc += a*(ms + r @ r)
        # Euclidean quadratic form D_E = k^T A k + 2 B.k + C (Euclidean dot products)
        Ainv = np.linalg.inv(Amat)
        Dmin = Cc - np.einsum('lm,li,mi->', Ainv, Bv, Bv)
        # numerical minimisation as an independent check
        def DE(kflat):
            k = kflat.reshape(L, 4); val = 0.0
            for (eta, r, ms), a in zip(zip(nlines_eta, rs, msqs), al):
                qv = np.array(eta, float) @ k + r
                val += a*(ms + qv @ qv)
            return val
        res = minimize(DE, np.zeros(4*L), method='BFGS', options={'gtol': 1e-12})
        U = np.linalg.det(Amat)
        F = U*Dmin
        ok = ok and abs(res.fun - Dmin) < 1e-7*(1 + abs(Dmin)) and F >= -1e-12
        worst = min(worst, F)
    return ok, worst
rng0 = np.random.default_rng(5)
pE = [rng0.normal(size=4) for _ in range(3)]
# one-loop massless box with Euclidean external vectors: lines k, k+p1, k+p1+p2, k-p4 (p4 = -(p1+p2+p3))
p4 = -(pE[0] + pE[1] + pE[2])
ok, worst = eucl_check([(1,), (1,), (1,), (1,)], [np.zeros(4), pE[0], pE[0] + pE[1], -p4], [0, 0, 0, 0], 1)
check('L5 one-loop massless box, Euclidean: F/U = min D_E and F >= 0 (worst %.2e)' % worst, ok)
ok, worst = eucl_check([(1, 0), (1, 0), (0, 1), (1, -1), (0, 1)], [np.zeros(4), -pE[0], pE[0], np.zeros(4), -pE[1]],
                       [0, 0, 0.4, 0, 1.0], 2)
check('L5 two-loop graph, Euclidean: F/U = min D_E and F >= 0 (worst %.2e)' % worst, ok)

# =============================================================== L6 deformed simplex numerics
print('=== L6: deformed simplex, massive vertex (m=1, gluon mass 0.3, on-shell legs) ===')
def F_num(al, sval, mgv=0.3):
    a0_, a1_, a2_ = al
    return -(a1_*a2_*sval + a0_*a1_ + a0_*a2_) + (a0_ + a1_ + a2_)*(a0_*mgv**2 + a1_ + a2_)
def grad_num(al, sval, mgv=0.3, h=1e-7):
    g = []
    for j in range(3):
        e = np.zeros(3); e[j] = h
        g.append((F_num(al + e, sval, mgv) - F_num(al - e, sval, mgv))/(2*h))
    return np.array(g)
def deformed_min(sval, etav=0.05, n=400, mgv=0.3):
    ii, jj = np.meshgrid(np.arange(n + 1), np.arange(n + 1), indexing='ij')
    mask = ii + jj <= n
    A0 = (ii/n)[mask]; A1 = (jj/n)[mask]; A2 = 1 - A0 - A1
    Fr = -(A1*A2*sval + A0*A1 + A0*A2) + (A0 + A1 + A2)*(A0*mgv**2 + A1 + A2)
    U = A0 + A1 + A2
    g0 = -(A1 + A2) + (A0*mgv**2 + A1 + A2) + U*mgv**2
    g1 = -(A2*sval + A0) + (A0*mgv**2 + A1 + A2) + U
    g2 = -(A1*sval + A0) + (A0*mgv**2 + A1 + A2) + U
    c = A0*g0 + A1*g1 + A2*g2
    Z0 = A0*(1 - 1j*etav*(g0 - c)); Z1 = A1*(1 - 1j*etav*(g1 - c)); Z2 = A2*(1 - 1j*etav*(g2 - c))
    Fz = -(Z1*Z2*sval + Z0*Z1 + Z0*Z2) + (Z0 + Z1 + Z2)*(Z0*mgv**2 + Z1 + Z2)
    return np.min(np.abs(Fr)), np.min(np.abs(Fz))
for sval in (3.0, 4.1, 4.4, 5.0, 4.0):
    mr, md = deformed_min(sval)
    print('   s=%.1f: min|F| real simplex = %.2e   min|F(z)| deformed (eta=0.05) = %.3e' % (sval, mr, md))
    if sval == 5.0:
        check('L6 above threshold (s=5): deformed contour avoids F=0', md > 1e-4 and mr < 1e-3)
    if sval == 4.0:
        check('L6 normal threshold s=4m^2: zero at the Landau point (0,1/2,1/2) cannot be avoided', md < 1e-4)
print('   Landau point check at s=4: F(0,1/2,1/2) =', F_num(np.array([0, .5, .5]), 4.0),
      ' grad =', np.round(grad_num(np.array([0, .5, .5]), 4.0), 8))

# =============================================================== L7 Gordan alternative
print('=== L7: Gordan alternative (lem:appD-gordan) ===')
def min_norm_point(D):
    # minimise |sum t_j D_j|^2 over the simplex (SLSQP)
    N = D.shape[0]
    fun = lambda tt: np.sum((tt @ D)**2)
    cons = ({'type': 'eq', 'fun': lambda tt: np.sum(tt) - 1},)
    res = minimize(fun, np.ones(N)/N, bounds=[(0, 1)]*N, constraints=cons, method='SLSQP',
                   options={'ftol': 1e-15, 'maxiter': 500})
    return res.x @ D, res.x
def landau_point_LP(D):
    # feasibility: sum a_j D_j = 0, sum a = 1, a >= 0
    N, d = D.shape
    res = linprog(np.zeros(N), A_eq=np.vstack([D.T, np.ones(N)]), b_eq=np.r_[np.zeros(d), 1], bounds=[(0, None)]*N)
    return res.status == 0, (res.x if res.status == 0 else None)
rngg = np.random.default_rng(1)
nI = nII = 0; worst = 1.0; excl = True
for trial in range(400):
    d = int(rngg.integers(2, 5)); N = int(rngg.integers(2, 8))
    D = rngg.normal(size=(N, d))
    if trial % 3 == 0:
        D = D + rngg.normal(size=d)*1.5      # some instances biased towards type I
    feas, alpha = landau_point_LP(D)
    w, tt = min_norm_point(D)
    if feas:
        nII += 1
        excl = excl and np.linalg.norm(w) < 1e-4 and np.allclose(alpha @ D, 0, atol=1e-8)
    else:
        nI += 1
        margin = np.min(D @ w) - w @ w
        worst = min(worst, margin)
        excl = excl and np.linalg.norm(w) > 1e-6 and np.all(D @ w > 0)
check('L7 Gordan: exactly one alternative in 400 random instances (type I %d, type II %d)' % (nI, nII), excl and nI > 50 and nII > 50)
check('L7 min-norm point w satisfies D_j.w >= |w|^2 (worst margin %.1e)' % worst, worst > -1e-6)
# vertex points (momentum space), p1 = (1,0,0,1)/sqrt2 * 1 along +, p2 along -
sq2 = np.sqrt(2.)
p1v = np.array([1, 0, 0, 1])/sq2; p2v = np.array([1, 0, 0, -1])/sq2
def mink(a, b_): return a[0]*b_[0] - a[1:] @ b_[1:]
def grads(kv, onshell):
    # u_j = dD_j/dk as Euclidean-component covectors: D0=k^2 -> 2 k_mu, D1=(p1-k)^2 -> -2 (p1-k)_mu, D2=(p2+k)^2 -> 2 (p2+k)_mu
    low = lambda v: np.array([v[0], -v[1], -v[2], -v[3]])
    u = {0: 2*low(kv), 1: -2*low(p1v - kv), 2: 2*low(p2v + kv)}
    return np.array([u[j] for j in onshell])
for xx in (0.3, 0.7):
    kv = xx*p1v
    feas, alpha = landau_point_LP(grads(kv, [0, 1]))
    check('L7 collinear point k=%.1f p1: Landau point alpha=(1-x,x)=%s' % (xx, np.round(alpha, 6)),
          feas and np.allclose(alpha, [1 - xx, xx], atol=1e-8))
# point on the q qbar cut surface: l1=p1-k, l2=p2+k both on shell, l1+l2 = q
l1 = np.array([0.5, 0.5*np.sin(1.0), 0, 0.5*np.cos(1.0)]); q = p1v + p2v; l2 = q - l1
kv = p1v - l1
print('   cut surface check: l1^2=%.2e l2^2=%.2e' % (mink(l1, l1), mink(l2, l2)))
feas, _ = landau_point_LP(grads(kv, [1, 2]))
vdir = np.array([1, -1, -1, -1])*(l1 - l2)      # contravariant v = l1 - l2 as a vector paired with covectors
u = grads(kv, [1, 2])
check('L7 q-qbar cut surface (Q^2>0): no Landau point, v = l1 - l2 gives u_j.v > 0', (not feas) and np.all(u @ (l1 - l2) > 0))
print('   u_j.v =', u @ (l1 - l2), ' = 2 l1.l2 =', 2*mink(l1, l2))

# =============================================================== L8 Cayley matrix
print('=== L8: Cayley matrix of the massless vertex ===')
Y = sp.Matrix([[0, 0, 0], [0, 0, -Qsq/2], [0, -Qsq/2, 0]])
ok_c = True
for S in [(0,), (1,), (2,), (0, 1), (0, 2), (1, 2)]:
    YS = Y.extract(list(S), list(S))
    ns = YS.nullspace()
    has_pos = len(ns) > 0
    if S == (1, 2):
        ok_c = ok_c and not has_pos
    else:
        ok_c = ok_c and has_pos
check('L8 Y_S has a non-negative null vector iff S in {0},{1},{2},{0,1},{0,2}; det Y_{12} = -Q^4/4',
      ok_c and sp.simplify(Y.extract([1, 2], [1, 2]).det() + Qsq**2/4) == 0)

# =============================================================== L9 Coleman-Norton
print('=== L9: Coleman-Norton closure and soft scaling limit ===')
xs, b0, b1 = sp.symbols('x beta0 beta1', positive=True)
P1s = sp.Matrix(sp.symbols('P1_0:4'))
k_ = xs*P1s
# loop X->Y2->Y1->X : line2 along (alpha2=0), line0 along (k), line1 against (p1-k)
loop = 0*P1s + b0*k_ - b1*(P1s - k_)
cond = sp.solve(sp.Eq(b0*xs, b1*(1 - xs)), b1)
check('L9 loop equation on the edge a2=0: a0 x = a1 (1-x)', sp.simplify(loop.subs(b1, cond[0])) == sp.zeros(4, 1))
# vertex positions: Y2 = X; Y1 = X + a1 (p1-k) = Y2 + a0 k
print('   Y1 - X = a1(1-x) p1 = a0 x p1: quark and gluon arrive simultaneously')
lam_, c_ = sp.symbols('lambda c', positive=True)
qv = sp.Matrix(sp.symbols('q0:4'))
alpha_soft = c_/lam_
disp = alpha_soft*lam_*qv
check('L9 soft line of momentum lambda q with alpha = c/lambda: displacement c q finite, alpha D -> 0',
      sp.simplify(disp - c_*qv) == sp.zeros(4, 1) and sp.limit(alpha_soft*(lam_**2)*mdot(qv, qv), lam_, 0) == 0)

# =============================================================== L10 soft corner behaviour
print('=== L10: F near the soft corner ===')
r, u_ = sp.symbols('r u', positive=True)
sub = {a1: r*u_, a2: r*(1 - u_), a0: 1 - r}
Foff = sp.expand(F_off.subs(sub))
Fml = sp.expand(F_ml.subs(sub))
check('L10 off-shell: F = r m^2 + O(r^2) -> int r dr / r converges',
      sp.simplify(sp.series(Foff, r, 0, 2).removeO() - r*m**2) == 0)
check('L10 massive legs: F = r^2 (m^2 + u(1-u) Q^2) -> int r dr / r^2 diverges logarithmically',
      sp.simplify(Fml - r**2*(m**2 + u_*(1 - u_)*Qsq)) == 0)

# =============================================================== L11 one-dimensional toy integrals
print('=== L11: one-dimensional pinch / endpoint toy integrals (ex:ir-pinch-toy) ===')
mp.mp.dps = 30
def I_pinch(a, b_, e):
    return mp.quad(lambda xx: 1/((xx - a + 1j*e)*(xx + b_ - 1j*e)), [-mp.inf, -abs(b_) - 1, -b_, a, abs(a) + 1, mp.inf])
def I_same(a, b_, e):
    return mp.quad(lambda xx: 1/((xx - a + 1j*e)*(xx + b_ + 1j*e)), [-mp.inf, -abs(b_) - 1, -b_, a, abs(a) + 1, mp.inf])
for (a, b_) in [(0.7, 0.2), (0.3, -0.25), (1.0, 0.5)]:
    e = 1e-3
    num = I_pinch(a, b_, e); exact = -2j*mp.pi/(a + b_ - 2j*e)
    print('   pinch a=%.2f b=%.2f: numeric %s  formula -2 pi i/(a+b-2i e) %s' % (a, b_, mp.nstr(num, 10), mp.nstr(exact, 10)))
    check('L11 pinch integral = -2 pi i/(a+b-i0) at (a,b)=(%.2f,%.2f)' % (a, b_), abs(num - exact) < 1e-8)
    ns = I_same(a, b_, e)
    check('L11 same-side poles: integral = 0 at (a,b)=(%.2f,%.2f)' % (a, b_), abs(ns) < 1e-8)
for a in (0.2, 0.05, 0.01):
    e = 1e-12
    num = mp.quad(lambda xx: 1/(xx - a + 1j*e), [0, a, 1])
    exact = mp.log((1 - a)/a) - 1j*mp.pi
    check('L11 endpoint integral int_0^1 dx/(x-a+i0) = ln((1-a)/a) - i pi at a=%.2f' % a, abs(num - exact) < 1e-6)

print()
npass = sum(1 for _, ok in RES if ok)
print('SUMMARY: %d/%d checks passed' % (npass, len(RES)))
