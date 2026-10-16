#!/usr/bin/env python3
"""
landau_oneloop.py  --  Landau equations for one-loop graphs (research/c_regions)

Checks (all exact sympy unless stated):
  L1  envelope identity  d(F/U)/dx_j = -D_j(k_c)   (links alpha-space and momentum-space Landau eqs)
  L2  deformation identity  Im F(z) = -eta * sum_j x_j w_j^2 + O(eta^3),  z_j = x_j (1 - i eta w_j),
      w_j = dF/dx_j - sum_k x_k dF/dx_k   (on sum x = 1); O(eta^2) term real
  L3  alpha-space Landau sets on the closed simplex:
        massless on-shell vertex  -> two closed edges {x1=0}, {x2=0} (collinear-2, collinear-1), meeting
                                     at the soft corner (1,0,0)
        off-shell (Euclidean) vertex -> only the three corners (zero-momentum massless lines)
        massive-exchange vertex, massless on-shell legs -> corners (0,1,0),(0,0,1) only
        massive on-shell legs, massless gluon -> corner (1,0,0) only
        massless box -> the 4 edges (0,1),(1,2),(2,3),(3,0) + vertices
        massless bubble -> corners for p^2 != 0; whole simplex for p^2 = 0
  L4  momentum-space Landau eqs for the vertex (Cayley matrix + explicit k_c), Coleman-Norton picture
  L5  Gordan alternative at sample points (linear programming, numerical)
  L6  numerical illustration of the alpha-deformation: massive vertex above threshold (no Landau point)
      vs at the normal threshold s=4m^2 (Landau point): min |F(z)| on the deformed simplex
  L7  power counting at the soft corner: F linear (off-shell, integrable) vs F quadratic (massive legs,
      log divergent) -- why Landau solutions are necessary but not sufficient
Run:  python3 -I landau_oneloop.py
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np

PASS = []
def check(name, cond):
    PASS.append((name, bool(cond)))
    print(('PASS ' if cond else 'FAIL ') + name)

# ---------------------------------------------------------------- generic one-loop Symanzik polynomials
def symanzik_oneloop(x, sinv, msq):
    """x: list of Feynman parameters; sinv[(i,j)] = (r_i - r_j)^2 ; msq[j] = m_j^2.
    Lines q_j = k + r_j, propagators 1/(q_j^2 - m_j^2 + i0).  U = sum x,
    F = sum_{i<j} x_i x_j ( -(r_i-r_j)^2 ) + U sum_j x_j m_j^2   (Minkowski; integrand ~ (F - i0)^(-...))"""
    n = len(x)
    U = sum(x)
    F = sum(x[i]*x[j]*(-sinv[(i, j)]) for i in range(n) for j in range(i+1, n)) + U*sum(x[j]*msq[j] for j in range(n))
    return sp.expand(U), sp.expand(F)

def mdot(a, b):  # Minkowski product, metric (+,-,-,-), components (t,x,y,z)
    return a[0]*b[0] - a[1]*b[1] - a[2]*b[2] - a[3]*b[3]

# ---------------------------------------------------------------- L1 envelope identity (random rational kinematics)
print('=== L1: envelope identity d(F/U)/dx_j = -D_j(k_c) ===')
x = sp.symbols('x0:4', positive=True)
rng = np.random.default_rng(7)
for n in (3, 4):
    xs = x[:n]
    r = [sp.Matrix([0, 0, 0, 0])] + [sp.Matrix([sp.Rational(int(v), 7) for v in rng.integers(-9, 10, 4)]) for _ in range(n-1)]
    m2 = [sp.Rational(int(v), 5) for v in rng.integers(0, 6, n)]
    sinv = {(i, j): mdot(r[i]-r[j], r[i]-r[j]) for i in range(n) for j in range(n)}
    U, F = symanzik_oneloop(list(xs), sinv, m2)
    kc = -sum((xs[j]*r[j] for j in range(n)), sp.zeros(4, 1))/U     # stationary point of sum x_j (q_j^2 - m_j^2)
    ok = True
    for j in range(n):
        qj = kc + r[j]
        Dj = mdot(qj, qj) - m2[j]
        ok &= sp.simplify(sp.diff(F/U, xs[j]) + Dj) == 0
    # stationary value: sum_j x_j (m_j^2 - q_j^2)|_{kc} = F/U
    val = sum(xs[j]*(m2[j] - mdot(kc + r[j], kc + r[j])) for j in range(n))
    ok &= sp.simplify(val - F/U) == 0
    check(f'L1 envelope identity and F/U = stationary value, n={n} lines', ok)

# ---------------------------------------------------------------- L2 deformation identity (general massive triangle)
print('=== L2: deformation identity ===')
s12, s13, s23, m0, m1, m2_ = sp.symbols('s01 s02 s12 m0sq m1sq m2sq', real=True)
eta = sp.symbols('eta', positive=True)
x0, x1, x2 = sp.symbols('x0 x1 x2', positive=True)
U3, F3 = symanzik_oneloop([x0, x1, x2], {(0, 1): s12, (0, 2): s13, (1, 2): s23}, [m0, m1, m2_])
X = [x0, x1, x2]
dF = [sp.diff(F3, v) for v in X]
c = sum(X[j]*dF[j] for j in range(3))
w = [dF[j] - c for j in range(3)]
Z = {X[j]: X[j]*(1 - sp.I*eta*w[j]) for j in range(3)}
Fz = sp.expand(F3.subs(Z, simultaneous=True))
on_simplex = {x0: 1 - x1 - x2}
c1 = sp.expand(sp.diff(Fz, eta).subs(eta, 0).subs(on_simplex))
c2 = sp.expand((sp.diff(Fz, eta, 2)/2).subs(eta, 0).subs(on_simplex))
V = sp.expand(sum(X[j]*w[j]**2 for j in range(3)).subs(on_simplex))
check('L2 dF(z)/deta|0 = -i * sum x_j w_j^2 on the simplex', sp.simplify(c1 + sp.I*V) == 0)
check('L2 O(eta^2) coefficient is real for real kinematics', sp.simplify(sp.im(c2)) == 0 or sp.expand(c2 - sp.conjugate(c2)) == 0)
check('L2 deformation preserves sum z_j = 1', sp.simplify(sum(Z[v] for v in X).subs(on_simplex) - 1) == 0)
check('L2 V = sum x_j (dF_j)^2 - c^2 (variance form)',
      sp.simplify(V - sp.expand((sum(X[j]*dF[j]**2 for j in range(3)) - c**2).subs(on_simplex))) == 0)

# ---------------------------------------------------------------- L3 alpha-space Landau sets on the closed simplex
print('=== L3: alpha-space Landau solution sets (closed simplex) ===')
def landau_alpha_sets(F, xs, extra_assump=()):
    """Return list of (support S, solution description).  On the face with support S (x_j>0 iff j in S),
    the conditions x_j dF/dx_j = 0 for all j reduce to dF/dx_j = 0 for j in S (F=0 then follows by Euler)."""
    n = len(xs)
    out = []
    for size in range(1, n+1):
        for S in itertools.combinations(range(n), size):
            face = {xs[j]: 0 for j in range(n) if j not in S}
            eqs = [sp.expand(sp.diff(F, xs[j]).subs(face)) for j in S]
            eqs = [e for e in eqs if e != 0]
            Svars = [xs[j] for j in S]
            if not eqs:
                out.append((S, 'whole face'))
                continue
            # add normalisation and require strict positivity of the support
            sols = sp.solve(eqs + [sum(Svars) - 1], Svars, dict=True)
            good = []
            for so in sols:
                vals = [so.get(v, v) for v in Svars]
                # accept if every value is positive (numbers) or free (parametric family with positive range)
                if all((not vv.free_symbols and vv > 0) or vv.free_symbols for vv in vals):
                    good.append(so)
            if good:
                out.append((S, good))
    return out

s, t_, Q2, P2, M2, msq = sp.symbols('s t Q2 P2 M2 msq', positive=True)
# (a) massless on-shell vertex: lines 0=gluon k, 1=quark p1-k (r1=-p1), 2=antiquark p2+k (r2=p2)
U, Fv = symanzik_oneloop([x0, x1, x2], {(0, 1): 0, (0, 2): 0, (1, 2): s}, [0, 0, 0])
print('  massless on-shell vertex: F =', Fv)
sets = landau_alpha_sets(Fv, [x0, x1, x2])
for S, d in sets: print('   support', S, ':', d)
supp = [S for S, d in sets]
check('L3a massless vertex: Landau set = edges {0,1},{0,2} (+ their endpoints); edge {1,2} and interior excluded',
      set(supp) == {(0,), (1,), (2,), (0, 1), (0, 2)})
# (b) off-shell Euclidean vertex (task convention): p1^2=p2^2=-P2, (p1-p2)^2=-Q2
U, Fo = symanzik_oneloop([x0, x1, x2], {(0, 1): -P2, (0, 2): -P2, (1, 2): -Q2}, [0, 0, 0])
print('  off-shell vertex: F =', Fo)
sets = landau_alpha_sets(Fo, [x0, x1, x2]); supp = [S for S, d in sets]
for S, d in sets: print('   support', S, ':', d)
check('L3b off-shell vertex: only the three corners (each = one massless line at zero momentum)', set(supp) == {(0,), (1,), (2,)})
# (c) massive exchange M, massless on-shell legs, Euclidean Q2
U, Fm = symanzik_oneloop([x0, x1, x2], {(0, 1): 0, (0, 2): 0, (1, 2): -Q2}, [M2, 0, 0])
print('  massive-exchange vertex: F =', sp.factor(Fm))
sets = landau_alpha_sets(Fm, [x0, x1, x2]); supp = [S for S, d in sets]
for S, d in sets: print('   support', S, ':', d)
check('L3c massive exchange: only corners (0,1,0),(0,0,1) (zero-momentum quark lines)', set(supp) == {(1,), (2,)})
# (d) massive on-shell legs (p_i^2 = m^2), massless gluon, Euclidean Q2
U, Fq = symanzik_oneloop([x0, x1, x2], {(0, 1): msq, (0, 2): msq, (1, 2): -Q2}, [0, msq, msq])
print('  massive-leg vertex: F =', sp.factor(Fq))
sets = landau_alpha_sets(Fq, [x0, x1, x2]); supp = [S for S, d in sets]
for S, d in sets: print('   support', S, ':', d)
check('L3d massive legs, massless gluon: only corner (1,0,0)', supp == [(0,)])
# (e) massless box, lines q_j = k + r_j, r0=0, r1=p1, r2=p1+p2, r3=-p4 ; s=(p1+p2)^2, t=(p2+p3)^2
y = sp.symbols('y0:4', positive=True)
U, Fb = symanzik_oneloop(list(y), {(0, 1): 0, (0, 2): s, (0, 3): 0, (1, 2): 0, (1, 3): t_, (2, 3): 0}, [0, 0, 0, 0])
print('  massless box: F =', Fb)
sets = landau_alpha_sets(Fb, list(y)); supp = set(S for S, d in sets)
for S, d in sets: print('   support', S, ':', d)
check('L3e massless box: Landau set = 4 vertices + edges (0,1),(1,2),(2,3),(0,3); (0,2),(1,3) excluded',
      supp == {(0,), (1,), (2,), (3,), (0, 1), (1, 2), (2, 3), (0, 3)})
# (f) massless bubble
U, Fs = symanzik_oneloop([x0, x1], {(0, 1): s}, [0, 0])
sets = landau_alpha_sets(Fs, [x0, x1]); supp = set(S for S, d in sets)
check('L3f massless bubble (p^2=s!=0): only the two corners (trivial zero-momentum lines)', supp == {(0,), (1,)})
check('L3f massless bubble at p^2=0: F vanishes identically (every point is a solution)', Fs.subs(s, 0) == 0)

# ---------------------------------------------------------------- L4 momentum space, vertex
print('=== L4: momentum-space Landau equations for the vertex ===')
# Cayley matrix Y_ij = (m_i^2+m_j^2-(r_i-r_j)^2)/2 = q_i.q_j on shell; loop eq. sum a_j q_j = 0 => Y a = 0
Y = sp.Matrix([[0, 0, 0], [0, 0, -s/2], [0, -s/2, 0]])
print('  Cayley matrix Y =', Y.tolist())
for S in [(0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)]:
    YS = Y.extract(list(S), list(S))
    ns = YS.nullspace()
    print('   S =', S, ' null space of Y_S:', [list(v) for v in ns])
check('L4 det Y_{12} = -s^2/4 (normal threshold only at s=0)', sp.simplify(Y.extract([1, 2], [1, 2]).det() + s**2/4) == 0)
# explicit k_c = x1 p1 - x2 p2 (lines l0=k, l1=p1-k, l2=p2+k): check on the faces
p1p, p2m, xx = sp.symbols('p1p p2m xx', positive=True)
def lc(plus, minus, t1=0, t2=0):  # light-cone -> Cartesian (t,x,y,z), v^pm=(v0 pm v3)/sqrt2
    return sp.Matrix([(plus+minus)/sp.sqrt(2), t1, t2, (plus-minus)/sp.sqrt(2)])
P1v = lc(p1p, 0); P2v = lc(0, p2m)
kc = lambda a1, a2: a1*P1v - a2*P2v
k = kc(xx, 0)  # face x2 = 0, x1 = xx
D0 = mdot(k, k); D1 = mdot(P1v-k, P1v-k); D2 = mdot(P2v+k, P2v+k)
check('L4 face x2=0: k_c = x1 p1 puts lines 0 and 1 on shell (collinear-1), line 2 off shell',
      sp.simplify(D0) == 0 and sp.simplify(D1) == 0 and sp.simplify(D2 - xx*2*p1p*p2m) == 0)
# loop equation with orientation (antiquark X->Y2: p2+k ; gluon Y2->Y1: k ; quark Y1->X: k-p1)
a0, a1, a2 = (1 - xx), xx, 0
loop = a2*(P2v + k) + a0*k + a1*(k - P1v)
check('L4 loop equation a2(p2+k)+a0 k+a1(k-p1)=0 holds with (a0,a1,a2)=(1-x,x,0), k=x p1', sp.simplify(loop) == sp.zeros(4, 1))
# Coleman-Norton: Y1-X = a1 (p1-k), Y1-Y2 = a0 k, Y2-X = a2 (p2+k): consistent
cn = a1*(P1v - k) - (a0*k + a2*(P2v + k))
check('L4 Coleman-Norton: vertex positions consistent (Y2=X, quark and gluon both reach Y1 along p1)',
      sp.simplify(cn) == sp.zeros(4, 1))

# ---------------------------------------------------------------- L5 Gordan alternative (numerical LP)
print('=== L5: Gordan alternative at sample points (scipy linprog) ===')
from scipy.optimize import linprog
G = np.diag([1., -1., -1., -1.])
def gordan(grads):
    """grads: list of covectors u_i (R^4).  Return ('trap', alpha) if exists alpha>=0, sum=1, sum alpha_i u_i=0;
    else ('deform', v) with u_i.v >= 1 for all i."""
    m = len(grads); A = np.array(grads).T  # 4 x m
    res = linprog(np.zeros(m), A_eq=np.vstack([A, np.ones((1, m))]), b_eq=np.r_[np.zeros(4), 1.], bounds=[(0, None)]*m)
    if res.status == 0:
        return 'trap', res.x
    res2 = linprog(np.zeros(4), A_ub=-np.array(grads), b_ub=-np.ones(m), bounds=[(None, None)]*4)
    return ('deform', res2.x) if res2.status == 0 else ('??', None)
p1n = np.array([1., 0, 0, 1.]); p2n = np.array([1., 0, 0, -1.])  # light-like, Q^2 = 2 p1.p2 = 4
def grads_at(kv):
    """Covectors dD_j/dk (lower index -> use G) for on-shell lines at real k."""
    lines = {0: (kv, 1.), 1: (p1n - kv, -1.), 2: (p2n + kv, 1.)}  # (momentum, d(momentum)/dk)
    out, on = [], []
    for j, (q, sgn) in lines.items():
        if abs(q @ G @ q) < 1e-12:
            on.append(j); out.append(2*sgn*(G @ q))
    return on, out
for label, kv in [('collinear-1 point k=0.3 p1', 0.3*p1n), ('collinear-2 point k=-0.6 p2', -0.6*p2n),
                  ('soft point k=0', np.zeros(4)), ('generic point on k^2=0', np.array([1., 0.6, 0.8, 0.])),
                  ('both quark lines on shell (qqbar cut surface)', p1n - np.array([1., 0., 1., 0.]))]:
    on, gr = grads_at(kv)
    res = gordan(gr) if gr else ('no line on shell', None)
    print(f'   {label:45s} on-shell lines {on}: {res[0]}', '' if res[1] is None else np.round(res[1], 4))
on, gr = grads_at(0.3*p1n); check('L5 collinear point is trapped (alpha exists)', gordan(gr)[0] == 'trap')
on, gr = grads_at(np.array([1., 0.6, 0.8, 0.])); check('L5 generic on-shell point is not trapped (deformation exists)', gordan(gr)[0] == 'deform')

# ---------------------------------------------------------------- L6 numerical alpha-deformation illustration
print('=== L6: deformed simplex, massive vertex (m=1, gluon mass 0.3, on-shell legs p_i^2=m^2) ===')
def Fmass(z0, z1, z2, s_, m=1.0, lg=0.3):
    return -s_*z1*z2 + z0**2*lg**2 + z0*(z1+z2)*lg**2 + (z1+z2)**2*m**2
def dFmass(z0, z1, z2, s_, m=1.0, lg=0.3):
    return np.array([2*z0*lg**2 + (z1+z2)*lg**2, -s_*z2 + z0*lg**2 + 2*(z1+z2)*m**2, -s_*z1 + z0*lg**2 + 2*(z1+z2)*m**2])
def min_absF_deformed(s_, eta_=0.05, N=400):
    best = np.inf
    for a in np.linspace(0, 1, N):
        for b in np.linspace(0, 1-a, max(2, int(N*(1-a)))):
            xv = np.array([1-a-b, a, b]); g = dFmass(*xv, s_); cc = xv @ g; wv = g - cc
            z = xv*(1 - 1j*eta_*wv)
            best = min(best, abs(Fmass(*z, s_)))
    return best
for s_ in (3.0, 5.0, 4.4, 4.1, 4.0):
    mn_real = min(abs(Fmass(1-a-b, a, b, s_)) for a in np.linspace(0, 1, 201) for b in np.linspace(0, 1-a, max(2, int(201*(1-a)))))
    print(f'   s={s_:4.1f}: min|F| real simplex = {mn_real:.2e}   min|F(z)| deformed (eta=0.05) = {min_absF_deformed(s_):.3e}')
check('L6 above threshold (s=5m^2): deformed contour avoids F=0', min_absF_deformed(5.0) > 1e-3)
check('L6 at normal threshold (s=4m^2): F(z) vanishes on the deformed contour too (Landau point x=(0,1/2,1/2))',
      abs(Fmass(0, .5, .5, 4.0)) < 1e-14 and np.allclose(dFmass(0, .5, .5, 4.0)[1:], 0))

# ---------------------------------------------------------------- L7 power counting at the soft corner
print('=== L7: behaviour of F near the soft corner x=(1,0,0) ===')
r_, u_ = sp.symbols('r u', positive=True)
Fo_c = sp.series(Fo.subs({x0: 1 - r_, x1: r_*u_, x2: r_*(1-u_)}), r_, 0, 3).removeO()
Fq_c = sp.series(Fq.subs({x0: 1 - r_, x1: r_*u_, x2: r_*(1-u_)}), r_, 0, 3).removeO()
print('   off-shell vertex   F ~', sp.factor(sp.expand(Fo_c)))
print('   massive-leg vertex F ~', sp.factor(sp.expand(Fq_c)))
check('L7 off-shell: F = r P2 + O(r^2) -> int r dr / r converges (no divergence despite Landau point)',
      sp.simplify(sp.expand(Fo_c).coeff(r_, 1) - P2) == 0)
check('L7 massive legs: F = r^2 (msq + u(1-u) Q2) -> int r dr / r^2 diverges logarithmically (soft divergence)',
      sp.simplify(sp.expand(Fq_c) - r_**2*(msq + u_*(1-u_)*Q2)) == 0)

print('\nSUMMARY: %d/%d checks passed' % (sum(p for _, p in PASS), len(PASS)))
