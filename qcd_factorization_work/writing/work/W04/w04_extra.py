#!/usr/bin/env python3
"""
w04_extra.py -- additional writer-W04 checks (items not covered by w04_landau.py / w04_power.py).
Run:  python3 -I w04_extra.py   (log: logs/w04_extra.log)

X1  exact deformation identity D(k + i eta chi v) = D(k) - eta^2 chi^2 v'^2 + 2 i eta chi q.v'  (thm:ir-landau-momentum)
X2  off-shell triangle: k_c at the three corners (zero-momentum lines), F linear near the quark corners
    (integrable), F linear near the soft corner; F > 0 on the closed simplex minus the corners (ex:ir-euclid-triangle)
X3  massless self-energy: U, F; F = -p^2 a1 a2 (no alpha-space pinch away from p^2=0), momentum-space collinear
    Landau point alpha = (1-x, x) for k = x p at p^2 = 0 (Collins 2020 App. D1 caveat, lem:ir-envelope)
X4  transverse Dirac identity sum_i gamma^i gamma^j gamma^i = (D-4) gamma^j  => J_T.H_T = 0 in D = 4 (ex:ir-k-dominance)
X5  Glauber region of the one-loop vertex: in k^- only the pole of D1 lies at |k^-| ~ lambda^2; the poles of D0 and D2
    are at |k^-| ~ lambda^0 (prop:ir-glauber-trapping (a)); same for k^+ with D2
X6  Euclidean soft-subset IR degree d = A + A_q/2 (Euler relations; VF-EE-13), random graphs
X7  mode geometry: the five on-shell modes satisfy c = (a+b)/2; Glauber (2,2,1) lies below (fig:ir-mode-exponents)
X8  gauge-field decomposition A = (k/k^+) A^+ + G-part, G-part has no + component and transverse part
    (k^+ A^j - k^j A^+)/k^+ (prop:ir-super-leading); abelian field strength G^{+j}(k) = -i(k^+A^j - k^j A^+)
X9  normal coordinates of the collinear vertex region: shell integrals int_{lam<|kT|<2lam} d^2kT/kT^2 = pi ln 4
X10 one-dimensional pinch integral, symbolic residue: int dx/((x-a+i e)(x+b-i e)) = -2 pi i/(a+b-2 i e)
X11 Weinberg/YFS exponent for a two-charge process at high energy: A -> (2 alpha/pi)(ln(-q^2/m^2) - 1)
X12 Glauber exchange between spectators: lambda^(6-2-4)=lambda^0, soft exchange lambda^(4-2-1-1)=lambda^0,
    ultrasoft lambda^(8-4-2-2)=lambda^0 (power counting of one exchanged gluon between A and B lines)
X13 eikonal error: ultrasoft O(lam^2) only for p_T = 0 lines; O(lam) for generic jet lines (VF-REG-7 made precise)
X14 Dirac identity behind K dominance at O(lam^2): ubar(p1) gamma^+ gamma_T gamma_T v(p2) = 0
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import random
import numpy as np
import sympy as sp
import mpmath as mp
from scipy.optimize import linprog

RES = []
def check(name, cond):
    RES.append((name, bool(cond)))
    print(('PASS ' if cond else 'FAIL ') + name)

# --------------------------------------------------------------- X1
print('=== X1: exact deformation identity ===')
q = sp.Matrix(sp.symbols('q0:4', real=True)); v = sp.Matrix(sp.symbols('v0:4', real=True))
eta, chi, m = sp.symbols('eta chi m', real=True)
G = sp.diag(1, -1, -1, -1)
dot = lambda a, b: (a.T*G*b)[0]
lhs = sp.expand(dot(q + sp.I*eta*chi*v, q + sp.I*eta*chi*v) - m**2)
rhs = sp.expand(dot(q, q) - m**2 - eta**2*chi**2*dot(v, v) + 2*sp.I*eta*chi*dot(q, v))
check('X1 D(q + i eta chi v) = D(q) - eta^2 chi^2 v^2 + 2 i eta chi q.v (exact, no higher orders)', sp.simplify(lhs - rhs) == 0)
# Im D = eta chi u.v with u = dD/dq (covector 2 q_mu): 2 q.v = u.v
check('X1 Im part = eta chi (dD/dq).v with dD/dq_mu = 2 q_mu', sp.simplify(sp.im(rhs) - eta*chi*2*dot(q, v)) == 0)

# --------------------------------------------------------------- X2
print('=== X2: off-shell (Euclidean) triangle, corners ===')
a0, a1, a2, s, t, r, u = sp.symbols('alpha0 alpha1 alpha2 s t r u', nonnegative=True)
Q2, m2 = sp.symbols('Q2 m2', positive=True)
F = m2*a0*(a1 + a2) + Q2*a1*a2
# corner alpha1 = 1: alpha0 = s, alpha2 = t small
F1 = sp.expand(F.subs({a1: 1 - s - t, a0: s, a2: t}))
lin1 = sp.series(sp.series(F1, s, 0, 2).removeO(), t, 0, 2).removeO()
check('X2 near corner alpha1=1: F = m^2 s + Q^2 t + O(2) (linear => int rho drho/rho converges)',
      sp.simplify(sp.expand(lin1).coeff(s, 1).subs(t, 0) - m2) == 0 and sp.simplify(sp.expand(lin1).coeff(t, 1).subs(s, 0) - Q2) == 0)
F0 = sp.expand(F.subs({a0: 1 - r, a1: r*u, a2: r*(1 - u)}))
check('X2 near corner alpha0=1: F = m^2 r + O(r^2)', sp.simplify(sp.series(F0, r, 0, 2).removeO() - m2*r) == 0)
# positivity of F on the simplex except at corners (sample)
rng = np.random.default_rng(0); ok = True
for _ in range(20000):
    al = rng.dirichlet([1, 1, 1])
    val = 1.0*al[0]*(al[1] + al[2]) + 3.0*al[1]*al[2]
    if min(1 - al[0], 1 - al[1], 1 - al[2]) > 1e-6:
        ok = ok and val > 0
check('X2 F > 0 on the closed simplex away from the corners (20000 samples, m^2=1, Q^2=3)', ok)
# k_c at the corners: lines q0 = k, q1 = k - p1, q2 = k + p2 ; k_c = (a1 p1 - a2 p2)/U
P1 = sp.Matrix(sp.symbols('P1_0:4')); P2 = sp.Matrix(sp.symbols('P2_0:4'))
kc = lambda A0, A1, A2: (A1*P1 - A2*P2)/(A0 + A1 + A2)
ok = (kc(1, 0, 0) == sp.zeros(4, 1)) and (kc(0, 1, 0) - P1 == sp.zeros(4, 1)) and (kc(0, 0, 1) + P2 == sp.zeros(4, 1))
check('X2 corners: alpha0=1 -> k=0 (gluon line 0 soft); alpha1=1 -> k=p1 (line 1 zero momentum); alpha2=1 -> k=-p2', ok)

# --------------------------------------------------------------- X3
print('=== X3: massless self-energy (Collins 2020 App. D1 caveat) ===')
p2s = sp.Symbol('p2', real=True)
# lines k (alpha1) and p - k (alpha2): U = a1 + a2, F = -p^2 a1 a2 (2-forest formula)
F_se = -p2s*a1*a2
eqs = [a1*sp.diff(F_se, a1), a2*sp.diff(F_se, a2)]
check('X3 F = -p^2 a1 a2: for p^2 != 0 the alpha-space Landau points are only the corners (a1 a2 = 0)',
      all(sp.factor(e) == -p2s*a1*a2 for e in eqs))
check('X3 at p^2 = 0, F vanishes identically on the whole simplex (no isolated pinch: totally degenerate)',
      F_se.subs(p2s, 0) == 0)
# momentum space at p^2 = 0: k = x p, u_0 = 2k, u_1 = -2(p-k); LP finds alpha = (1-x, x)
pv = np.array([1., 0, 0, 1.])/np.sqrt(2)
low = lambda w: np.array([w[0], -w[1], -w[2], -w[3]])
for x in (0.25, 0.6):
    kv = x*pv
    U = np.array([2*low(kv), -2*low(pv - kv)])
    res = linprog(np.zeros(2), A_eq=np.vstack([U.T, np.ones(2)]), b_eq=np.r_[np.zeros(4), 1], bounds=[(0, None)]*2)
    check('X3 p^2=0, k=%.2f p: momentum-space Landau point alpha=(1-x,x)=%s (trapped)' % (x, np.round(res.x, 6)),
          res.status == 0 and np.allclose(res.x, [1 - x, x], atol=1e-8))

# --------------------------------------------------------------- X4
print('=== X4: transverse Dirac identity ===')
I2 = np.eye(2); Z2 = np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]]); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]])
g0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
gs = [np.block([[Z2, sm], [-sm, Z2]]).astype(complex) for sm in (sx, sy, sz)]
ok = True
for j in (1, 2):
    tot = sum(gs[i - 1] @ gs[j - 1] @ gs[i - 1] for i in (1, 2))
    ok = ok and np.allclose(tot, 0)
check('X4 D=4: sum_{i=1,2} gamma^i gamma^j gamma^i = 0 for j = 1, 2', ok)
Dd = sp.Symbol('D')
# general D: sum_i gamma^i gamma^j gamma^i = -gamma^j sum_i (gamma^i)^2 + 2 g^{jj} gamma^j ; (gamma^i)^2 = -1, D-2 transverse dims
coef = -(-(Dd - 2)) + 2*(-1)
check('X4 general D: coefficient (D-2) - 2 = D - 4 = -2 eps (O(eps) in CDR)', sp.simplify(coef - (Dd - 4)) == 0)

# --------------------------------------------------------------- X5
print('=== X5: Glauber region of the one-loop vertex: pole positions in k^- ===')
# D0 = 2k+k- - kT^2, D1 = -2(p1+ - k+)k- - kT^2, D2 = 2k+(p2- + k-) - kT^2 ; Glauber k+ ~ lam^2, kT ~ lam
def poles_kminus(lam, p1p=1.0, p2m=1.0, cp=0.7, cT=0.9):
    kp = cp*lam**2; kT2 = (cT*lam)**2
    pD0 = kT2/(2*kp)                 # D0 = 0
    pD1 = -kT2/(2*(p1p - kp))        # D1 = 0
    pD2 = -p2m + kT2/(2*kp)          # D2 = 0
    return abs(pD0), abs(pD1), abs(pD2)
lams = [1e-2, 1e-3, 1e-4]
P = np.array([poles_kminus(l) for l in lams])
sl = [np.polyfit(np.log(lams), np.log(P[:, i]), 1)[0] for i in range(3)]
print('   |k^-| of the poles of D0, D1, D2 ~ lam^%.3f, lam^%.3f, lam^%.3f' % tuple(sl))
check('X5 only the D1 pole is in the Glauber window |k^-| ~ lam^2; D0, D2 poles at |k^-| ~ lam^0',
      abs(sl[0]) < 1e-3 and abs(sl[1] - 2) < 1e-3 and abs(sl[2]) < 1e-3)

# --------------------------------------------------------------- X6
print('=== X6: Euclidean IR degree of a soft subset ===')
rng2 = random.Random(11); ok = True; n = 0
for _ in range(4000):
    nggg, nccg, nqqg, V4 = rng2.randint(0, 3), rng2.randint(0, 2), rng2.randint(0, 3), rng2.randint(0, 2)
    A_q, A_c = rng2.randint(0, 3), rng2.randint(0, 2)
    A_g = rng2.randint(0, 4)
    V3 = nggg + nccg + nqqg
    twoNq = 2*nqqg + A_q
    twoNc = 2*nccg + A_c
    twoNg = 3*nggg + nccg + nqqg + 4*V4 + A_g
    if twoNq % 2 or twoNc % 2 or twoNg % 2:
        continue
    Nq, Nc, Ng = twoNq//2, twoNc//2, twoNg//2
    A = A_q + A_c + A_g
    NS = Ng + Nq + Nc
    LS = NS - V3 - V4
    d = 4*LS - 2*Ng - Nq - 2*Nc + nggg + nccg
    ok = ok and (sp.Rational(d) == A + sp.Rational(A_q, 2)); n += 1
check('X6 d = 4L_S - 2N_g - N_q - 2N_c + n_ggg + n_ccg = A + A_q/2 for %d random soft subsets' % n, ok and n > 500)

# --------------------------------------------------------------- X7
print('=== X7: mode geometry (exponents (a,b,c)) ===')
modes = {'hard': (0, 0, 0), 'A-coll': (0, 2, 1), 'B-coll': (2, 0, 1), 'soft': (1, 1, 1), 'usoft': (2, 2, 2)}
ok = all(sp.Rational(a + b, 2) == c for (a, b, c) in modes.values())
check('X7 hard, A-coll, B-coll, soft, ultrasoft lie on c = (a+b)/2 (k_T^2 ~ k^+ k^-)', ok)
check('X7 Glauber (2,2,1): c < (a+b)/2 (k_T^2 >> |k^+ k^-|): below the on-shell plane', 1 < sp.Rational(4, 2))
check('X7 soft (1,1,1) is the centre of the parallelogram hard/A/B/ultrasoft',
      all(sp.Rational(sum(x[i] for x in (modes['hard'], modes['A-coll'], modes['B-coll'], modes['usoft'])), 4) == modes['soft'][i] for i in range(3)))

# --------------------------------------------------------------- X8
print('=== X8: K + G decomposition of a collinear gluon field ===')
kp, km, k1, k2 = sp.symbols('kp km k1 k2', real=True)
Ap, Am, A1, A2 = sp.symbols('Ap Am A1 A2')
# light-front components (plus, minus, 1, 2); K part = k^mu A^+ / k^+
K = [kp*Ap/kp, km*Ap/kp, k1*Ap/kp, k2*Ap/kp]
Gp = [Ap - K[0], Am - K[1], A1 - K[2], A2 - K[3]]
check('X8 G part has vanishing + component', sp.simplify(Gp[0]) == 0)
check('X8 transverse G part = (k^+ A^j - k^j A^+)/k^+', sp.simplify(Gp[2] - (kp*A1 - k1*Ap)/kp) == 0 and sp.simplify(Gp[3] - (kp*A2 - k2*Ap)/kp) == 0)
# abelian field strength in momentum space, A(x) = A e^{-ikx}: G^{+j} = d^+ A^j - d^j A^+ -> -i(k^+ A^j - k^j A^+)
# (d^mu e^{-ikx} = -i k^mu e^{-ikx})
check('X8 G^{+j} = -i (k^+ A^j - k^j A^+): proportional to the transverse G part times k^+',
      sp.simplify(-sp.I*(kp*A1 - k1*Ap) - (-sp.I*kp)*Gp[2]) == 0)

# --------------------------------------------------------------- X9
print('=== X9: logarithmic shells of the collinear vertex region ===')
kk = sp.Symbol('kk', positive=True); lam_ = sp.Symbol('lam', positive=True)
shell = sp.integrate(2*sp.pi*kk/kk**2, (kk, lam_, 2*lam_))
check('X9 int_{lam<|kT|<2lam} d^2kT/kT^2 = 2 pi ln 2 = pi ln 4 (independent of lam)', sp.simplify(shell - sp.pi*sp.log(4)) == 0)

# --------------------------------------------------------------- X10
print('=== X10: one-dimensional pinch integral (residue) ===')
x_, a_, b_ = sp.symbols('x a b', real=True); e_ = sp.Symbol('e', positive=True)
f = 1/((x_ - a_ + sp.I*e_)*(x_ + b_ - sp.I*e_))
res = sp.residue(f, x_, -b_ + sp.I*e_)
check('X10 closing above: 2 pi i Res_{x=-b+ie} = -2 pi i/(a+b-2ie)', sp.simplify(2*sp.pi*sp.I*res + 2*sp.pi*sp.I/(a_ + b_ - 2*sp.I*e_)) == 0)

# --------------------------------------------------------------- X11
print('=== X11: soft-photon exponent at high energy ===')
mp.mp.dps = 30
def A_closed(pdpp, mm=1.0):
    beta = mp.sqrt(1 - mm**4/pdpp**2)
    return (2/mp.pi)*((1/(2*beta))*mp.log((1 + beta)/(1 - beta)) - 1)
ok = True
for pdpp in (1e3, 1e5, 1e7):
    q2 = 2 - 2*pdpp     # q^2 = 2 m^2 - 2 p.p'
    approx = (2/mp.pi)*(mp.log(-q2/1.0) - 1)
    ok = ok and abs(A_closed(mp.mpf(pdpp)) - approx) < 10/pdpp*mp.log(pdpp)
check('X11 A -> (2 alpha/pi)[ln(-q^2/m^2) - 1] for -q^2 >> m^2 (corrections O(m^2/q^2 ln))', ok)

# --------------------------------------------------------------- X12
print('=== X12: one-gluon exchange between an A line and a B line: soft, ultrasoft, Glauber ===')
cnt = {'soft (1,1,1)': (1+1+2*1) - 2*1 - 1 - 1, 'ultrasoft (2,2,2)': (2+2+2*2) - 2*2 - 2 - 2, 'Glauber (2,2,1)': (2+2+2*1) - 2*1 - 2 - 2}
print('   ', cnt)
check('X12 all three exchanges scale as lambda^0 (measure - gluon - two eikonal/spectator propagators)', all(v == 0 for v in cnt.values()))

# --------------------------------------------------------------- X13
print('=== X13: eikonal error for a generic jet line (p_T ~ lam) vs a line along the axis ===')
def lcdot(a, b): return a[0]*b[1] + a[1]*b[0] - a[2]*b[2] - a[3]*b[3]
def eik_err_exp(scal, pT_scaled):
    a, b, c = scal; errs = []; lams = [1e-3, 1e-4, 1e-5, 1e-6]
    for lam in lams:
        lam = mp.mpf(lam)
        if pT_scaled:
            pA = (mp.mpf(1), mp.mpf('0.37')*lam**2, mp.mpf('0.6')*lam, mp.mpf('-0.25')*lam)   # generic A-collinear line, p^2 ~ lam^2
        else:
            pA = (mp.mpf(1), mp.mpf(0), mp.mpf(0), mp.mpf(0))
        k = (mp.mpf('0.7')*lam**a, mp.mpf('-0.45')*lam**b, mp.mpf('0.6')*lam**c, mp.mpf('-0.3')*lam**c)
        pk = tuple(pA[i] + k[i] for i in range(4))
        exact = lcdot(pk, pk); eik = lcdot(pA, pA) + 2*pA[0]*k[1]          # keep p^2 and 2 p^+ k^-
        errs.append(abs((exact - eik)/exact))
    return np.polyfit([float(mp.log(l)) for l in lams], [float(mp.log(e)) for e in errs], 1)[0]
mp.mp.dps = 40
e_us_axis = eik_err_exp((2, 2, 2), False); e_us_gen = eik_err_exp((2, 2, 2), True)
e_s_gen = eik_err_exp((1, 1, 1), True); e_g_gen = eik_err_exp((2, 2, 1), True)
print('   relative eikonal error exponents: ultrasoft (p_T=0) %.3f, ultrasoft (p_T~lam) %.3f, soft (p_T~lam) %.3f, Glauber (p_T~lam) %.3f'
      % (e_us_axis, e_us_gen, e_s_gen, e_g_gen))
check('X13 ultrasoft: O(lam^2) for p_T = 0, but O(lam) for a jet line with p_T ~ lam (term 2 p_T.k_T)',
      abs(e_us_axis - 2) < 1e-2 and abs(e_us_gen - 1) < 1e-2)
check('X13 soft O(lam), Glauber O(1) also for generic jet lines', abs(e_s_gen - 1) < 1e-2 and abs(e_g_gen) < 1e-2)

# --------------------------------------------------------------- X14
print('=== X14: the O(lam) piece of (J^+/k^+) k_T.H_T vanishes: ubar(p1) gamma^+ gamma_T^mu gamma^i v(p2) = 0 ===')
gp = (g0 + gs[2])/np.sqrt(2); gm = (g0 - gs[2])/np.sqrt(2)
def slash_lc(pp, pm, t1, t2):          # gamma.p = p^+ gamma^- + p^- gamma^+ - p_T.gamma_T
    return pp*gm + pm*gp - t1*gs[0] - t2*gs[1]
def null_vecs(M):
    u_, s_, vh = np.linalg.svd(M); return vh[2:].conj().T
U1 = null_vecs(slash_lc(1.0, 0, 0, 0)); V2 = null_vecs(slash_lc(0, 1.0, 0, 0))
ok = True
for i in range(2):
    ub = U1[:, i].conj() @ g0
    for j in range(2):
        v = V2[:, j]
        for mu in (0, 1):
            for ii in (0, 1):
                val = ub @ gp @ gs[mu] @ gs[ii] @ v
                ok = ok and abs(val) < 1e-12
check('X14 ubar(p1) gamma^+ gamma^mu_T gamma^i_T v(p2) = 0 (gamma^+ v(p2) = 0 for p2 || n_B)', ok)

print()
npass = sum(1 for _, ok in RES if ok)
print('SUMMARY: %d/%d checks passed' % (npass, len(RES)))
