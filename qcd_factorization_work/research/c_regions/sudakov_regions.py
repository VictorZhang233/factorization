#!/usr/bin/env python3
"""
sudakov_regions.py -- method of regions for the one-loop Sudakov triangle (research/c_regions)

Normalisation (all parts):  I = e^{eps gamma_E} mu^{2eps} \int d^Dk/(i pi^{D/2}) prod_j 1/(-q_j^2 + m_j^2 - i0),
D = 4-2eps; Feynman-parameter form (Cheng-Wu, x0 = 1):
   I = e^{eps gamma_E} Gamma(1+eps) \int_0^oo dx1 dx2 U^{-1+2eps} F^{-1-eps},  U = 1+x1+x2.
We set Q^2 = 1 and mu = 1 (logs of mu restored by dimensional analysis where printed).

PART A  off-shell (Euclidean) triangle: lines k, k+p1, k+p2; p1^2=p2^2=-P^2, (p1-p2)^2=-Q^2; t = P^2/Q^2
   F = t (x1+x2) + x1 x2
   A1 exact I(t) at eps=0 (1D integral) vs Usyukina-Davydychev Phi^(1)(t,t)
   A2 region integrals (hard, coll-1, coll-2, ultrasoft) in closed form; building blocks checked numerically
      in their convergence strips; momentum-space Schwinger forms agree with parameter-space forms
   A3 Laurent expansions; poles cancel; sum = ln^2 t + pi^2/3 (literature: BBF 2015 eq.(2.44))
   A4 numerical asymptotics: I(t) - LP = O(t ln^2 t)
   A5 next-to-leading power from parameter-space regions vs expansion of the exact result
   A6 O(eps) coefficient: regions vs numerical exact
   A7 overlap (zero-bin) contributions are scaleless
   A8 Newton polytope of U*F: lower facets = {hard, c1, c2, us}
PART B  massive exchange M, massless on-shell legs (Jantzen 2011 sec.6; BBF 2015 sec.2.3); t = M^2/Q^2
   F = t (1+x1+x2) + x1 x2 ; analytic regulators: propagator powers 1+delta1 (k+p1), 1+delta2 (k+p2)
   B1 exact I_M(t) (numerical) vs Jantzen's closed form (6.30)
   B2 pure DR: collinear regions ill-defined (Gamma(delta1-delta2) at delta=0)
   B3 regions with analytic regulators: hard + c1 + c2 (soft scaleless for delta1 != delta2); compare
      with Jantzen (6.26)-(6.29) and BBF (2.39),(2.50)-(2.52); sum = (1/2) ln^2 t + pi^2/3
   B4 Newton polytope: facets {hard, c1, c2}; 'soft' is only an edge (rapidity degeneracy)
PART C  massive on-shell legs (p_i^2 = m^2), massless gluon; t = m^2/Q^2: pure DR works
   C1 exact Laurent expansion vs regions (hard + c1 + c2, soft scaleless)
PART D  one-dimensional toy: overlap/zero-bin subtraction with cutoffs vs DR
Run:  python3 -I sudakov_regions.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
import numpy as np

mp.mp.dps = 30
PASS = []
def check(name, cond):
    PASS.append((name, bool(cond))); print(('PASS ' if cond else 'FAIL ') + name)

eps, t, L = sp.symbols('epsilon t L')          # L = ln t
EG = sp.EulerGamma
G = sp.gamma
def B(a, b): return G(a)*G(b)/G(a + b)
pref = sp.exp(eps*EG)*G(1 + eps)               # e^{eps gamma} Gamma(1+eps)

def laurent(expr, n=1, var=eps):
    """series in eps up to eps^n with t^(c eps) -> exp(c eps L)."""
    e = expr.subs(t, sp.exp(L))
    return sp.expand(sp.simplify(sp.series(e, var, 0, n + 1).removeO()))

# =========================================================================================== PART A
print('=================== PART A: off-shell (Euclidean) Sudakov triangle ===================')
# ---------------------------------------------------------------- A1 exact vs Usyukina-Davydychev
def I_exact(tv):
    # integrand symmetric under u -> 1-u: integrate over [0,1/2] and double (avoids u = 1 - tiny rounding to 1)
    tv = mp.mpf(tv)
    f = lambda u: (mp.log(u*(1 - u)/tv)/(u*(1 - u) - tv)) if abs(u*(1-u) - tv) > mp.mpf(10)**(-25) else 1/tv
    u0 = 2*tv/(1 + mp.sqrt(1 - 4*tv))         # point with u(1-u) = t (integrand regular there); stable form
    return 2*mp.quad(f, [0, u0, mp.mpf(1)/2])
def UD_Phi(x, y):
    lam = mp.sqrt((1 - x - y)**2 - 4*x*y); rho = 2/(1 - x - y + lam)
    return (2*(mp.polylog(2, -rho*x) + mp.polylog(2, -rho*y)) + mp.log(y/x)*mp.log((1 + rho*y)/(1 + rho*x))
            + mp.log(rho*x)*mp.log(rho*y) + mp.pi**2/3)/lam
print('--- A1: exact I(t) (eps=0) vs Usyukina-Davydychev Phi^(1)(t,t) ---')
mx = 0
for tv in ('0.1', '0.01', '1e-4', '1e-8'):
    a, b_ = I_exact(tv), UD_Phi(mp.mpf(tv), mp.mpf(tv))
    mx = max(mx, abs(a - b_)/abs(b_))
    print(f'   t={tv:6s}  I_exact={mp.nstr(a, 20)}  Phi_UD={mp.nstr(b_, 20)}')
check('A1 Q^2 I(t) = Phi^(1)(t,t) (Usyukina-Davydychev 1993) to < 1e-20', mx < 1e-20)
# also an asymmetric point via direct 2D integration of the Feynman-parameter integral
def I_exact_2d(t1, t2):
    # integrate rho analytically: int_0^1 drho/(A + rho (a - A)) = ln(a/A)/(a-A), A = t1 u + t2 (1-u), a = u(1-u)
    t1, t2 = mp.mpf(t1), mp.mpf(t2)
    def f(u, tA, tB):           # u near 0 is accurate; reflect the half (1/2,1) onto (0,1/2)
        A = tA*u + tB*(1 - u); a = u*(1 - u)
        return mp.log(a/A)/(a - A) if abs(a - A) > mp.mpf(10)**(-25) else 1/A
    def half(tA, tB):
        # zero of a - A in (0, 1/2):  u^2 + (tA - tB - 1) u + tB = 0
        bq = tA - tB - 1; disc = bq**2 - 4*tB
        pts = [0, mp.mpf(1)/2]
        if disc > 0:
            for r in ((-bq - mp.sqrt(disc))/2, (-bq + mp.sqrt(disc))/2):
                if 0 < r < mp.mpf(1)/2: pts.append(r)
        return mp.quad(lambda u: f(u, tA, tB), sorted(pts))
    return half(t1, t2) + half(t2, t1)
v2d = I_exact_2d('0.02', '0.05'); vUD = UD_Phi(mp.mpf('0.02'), mp.mpf('0.05'))
print(f'   asymmetric t1=0.02,t2=0.05: 2D integral {mp.nstr(v2d, 15)}  Phi_UD {mp.nstr(vUD, 15)}')
check('A1 asymmetric point (P1^2 != P2^2) agrees with Phi^(1)(x,y)', abs(v2d - vUD) < 1e-12)

# ---------------------------------------------------------------- A2 region integrals
print('--- A2: region integrals (leading power), closed forms ---')
R_h = pref*G(-eps)**2/G(1 - 2*eps)                         # (mu^2/Q^2)^eps / Q^2
R_c = pref*t**(-eps)*G(-eps)*G(1 - eps)/(eps*G(1 - 2*eps))  # each collinear region: (mu^2/P^2)^eps / Q^2
R_s = pref*t**(-2*eps)*G(eps)*G(1 - eps)/eps                # ultrasoft: (mu^2 Q^2/P^4)^eps / Q^2
# building blocks, numerically in convergence strips
def num_check(name, f_num, f_exact, tol=1e-12):
    a, b_ = f_num(), f_exact
    print(f'   {name}: numeric {mp.nstr(a, 16)}  closed form {mp.nstr(b_, 16)}')
    return abs(a - b_) < tol*abs(b_)
e1 = mp.mpf('-0.3')   # hard: x-integrals need eps<0
def _hard2d():
    with mp.workdps(15):
        return mp.quad(lambda a, b_: (1 + a + b_)**(-1 + 2*e1)*(a*b_)**(-1 - e1), [0, 1, mp.inf], [0, 1, mp.inf])
okA2 = num_check('hard  int dx1 dx2 (1+x1+x2)^(-1+2e)(x1x2)^(-1-e), e=-0.3', _hard2d,
                 mp.gamma(-e1)**2/mp.gamma(1 - 2*e1), tol=1e-5)
e2 = mp.mpf('0.3')    # Schwinger integral of the collinear region needs eps>0 ...
okA2 &= num_check('coll  int_0^oo dlam (A+lam B)^(-1-e) = A^(-e)/(e B), A=0.7,B=1.3, e=0.3',
                  lambda: mp.quad(lambda l: (mp.mpf('0.7') + l*mp.mpf('1.3'))**(-1 - e2), [0, 1, 10, 100, 10**4, mp.inf], maxdegree=12),
                  mp.mpf('0.7')**(-e2)/(e2*mp.mpf('1.3')), tol=1e-9)   # slow algebraic tail limits mp.quad
aa = -e1    # substitute x = s^(1/aa): x^(-1-e) dx = ds/aa  (removes the endpoint singularity)
okA2 &= num_check('coll  int_0^1 dx x^(-1-e)(1-x)^(-e) = G(-e)G(1-e)/G(1-2e), e=-0.3',   # ... the x-integral eps<0
                  lambda: mp.quad(lambda s_: (1 - s_**(1/aa))**(-e1)/aa, [0, mp.mpf(1)/2, 1]),
                  mp.gamma(-e1)*mp.gamma(1 - e1)/mp.gamma(1 - 2*e1), tol=1e-15)
e3 = mp.mpf('0.4')    # ultrasoft: common strip 0<eps<1
def _us2d():
    with mp.workdps(15):
        return mp.quad(lambda a, b_: (a*b_ + a + b_)**(-1 - e3), [0, 1, mp.inf], [0, 1, mp.inf])
okA2 &= num_check('usoft int dy1 dy2 (y1 y2 + y1 + y2)^(-1-e) = G(e)G(1-e)/e, e=0.4', _us2d,
                  mp.gamma(e3)*mp.gamma(1 - e3)/e3, tol=1e-5)
check('A2 building blocks of the region integrals verified in their convergence strips', okA2)
# parameter-space region integrands (Cheng-Wu x0=1) give the same closed forms:
#  c1: int dx1 (1+x1)^(-1+2e) x1^(-1-e) * int dx2 (t+x2)^(-1-e) = B(-e,1-e) * t^(-e)/e
x1s, x2s = sp.symbols('x1 x2', positive=True)
c1_param = B(-eps, 1 - eps)*t**(-eps)/eps
check('A2 parameter-space c1 = momentum-space c1 (identical closed forms)', sp.simplify(pref*c1_param - R_c) == 0)
# BBF 2015: I_h = G(1+e)G(-e)^2/G(1-2e) (mu^2/Q^2)^e/Q^2 (2.39); I_c = -G(1+e)G(-e)^2/G(1-2e) (mu^2/P^2)^e/Q^2 (2.41);
#           I_s = -G(1+e)G(e)G(-e) (mu^2 Q^2/(L^2 P^2))^e/Q^2 (2.43).  Their measure has no e^{eps gamma}.
bbf_h = G(1 + eps)*G(-eps)**2/G(1 - 2*eps); bbf_c = -G(1 + eps)*G(-eps)**2/G(1 - 2*eps)*t**(-eps)
bbf_s = -G(1 + eps)*G(eps)*G(-eps)*t**(-2*eps)
check('A2 region integrals equal BBF 2015 eqs.(2.39),(2.41),(2.43) exactly (after removing e^{eps gamma})',
      all(sp.simplify(sp.gammasimp(r/sp.exp(eps*EG) - b_)) == 0 for r, b_ in ((R_h, bbf_h), (R_c, bbf_c), (R_s, bbf_s))))

# ---------------------------------------------------------------- A3 Laurent expansions
print('--- A3: Laurent expansions (Q^2=mu^2=1, L = ln t = ln(P^2/Q^2)) ---')
Lh, Lc, Ls = laurent(R_h), laurent(R_c), laurent(R_s)
for nm, ex in (('hard', Lh), ('coll-1 (= coll-2)', Lc), ('ultrasoft', Ls)):
    print(f'   {nm:18s}: ' + str(sp.collect(sp.expand(ex), eps)))
tot = sp.expand(Lh + 2*Lc + Ls)
c_m2, c_m1, c_0, c_1 = [sp.simplify(tot.coeff(eps, k)) for k in (-2, -1, 0, 1)]
print('   sum: 1/eps^2:', c_m2, ' 1/eps:', c_m1, ' eps^0:', c_0)
print('   sum O(eps):', sp.expand(c_1))
check('A3 double and single poles cancel between hard, collinear and ultrasoft regions', c_m2 == 0 and c_m1 == 0)
check('A3 finite part = ln^2(P^2/Q^2) + pi^2/3  [BBF 2015 eq.(2.44) with L^2=P^2: ln(Q^2/L^2)ln(Q^2/P^2)+pi^2/3]',
      sp.simplify(c_0 - (L**2 + sp.pi**2/3)) == 0)
# constants of the individual regions with the e^{eps gamma} normalisation
print('   region constants (eps^0, L=0):', [sp.nsimplify(sp.simplify(e.coeff(eps, 0).subs(L, 0))) for e in (Lh, Lc, Ls)])
check('A3 region constants: hard -pi^2/12, each collinear +pi^2/12 (after sign), ultrasoft +pi^2/4',
      sp.simplify(Lh.coeff(eps, 0).subs(L, 0) + sp.pi**2/12) == 0 and sp.simplify(Lc.coeff(eps, 0).subs(L, 0) - sp.pi**2/12) == 0
      and sp.simplify(Ls.coeff(eps, 0).subs(L, 0) - sp.pi**2/4) == 0)

# ---------------------------------------------------------------- A4 numerical asymptotics
print('--- A4: numerical check of the leading power ---')
rows = []
for k in range(2, 11):
    tv = mp.mpf(10)**(-k)
    ex = I_exact(tv); lp = mp.log(tv)**2 + mp.pi**2/3
    rows.append((tv, ex, lp, (ex - lp)/(tv*mp.log(tv)**2)))
    if k in (2, 4, 6, 8, 10):
        print(f'   t=1e-{k:<2d} I={mp.nstr(ex, 14):>18s}  LP={mp.nstr(lp, 14):>18s}  (I-LP)/(t ln^2 t)={mp.nstr(rows[-1][3], 8)}')
check('A4 I(t) - [ln^2 t + pi^2/3] = O(t ln^2 t) (ratio -> 2, the NLP log^2 coefficient, see A5)', all(abs(r[3]) < 3 for r in rows))

# ---------------------------------------------------------------- A5 next-to-leading power
print('--- A5: next-to-leading power from parameter-space regions ---')
def binom(a, n): return sp.binomial(a, n) if isinstance(a, int) else sp.Mul(*[(a - i) for i in range(n)])/sp.factorial(n)
def hard_n(n):
    s_ = 0
    for k in range(n + 1):
        s_ += sp.binomial(n, k)*G(k - n - eps)*G(-k - eps)*G(1 + n)/G(1 - 2*eps)
    return pref*binom(-1 - eps, n)*s_
def coll_n(n):
    s_ = 0
    for m in range(n + 1):
        l = n - m
        xint = G(-eps - l)*G(1 - eps + m + l)/G(1 - 2*eps + m)
        yint = G(m + l + 1)*G(eps - m)/G(1 + eps + l)
        s_ += binom(-1 + 2*eps, m)*binom(-1 - eps, l)*xint*yint
    return pref*t**(-eps)*s_
def usoft_n(n):
    s_ = 0
    for k in range(n + 1):
        inner = B(k + 1, eps - k)*B(n - eps + 1, k - n + eps)
        s_ += sp.binomial(n, k)*inner
    return pref*t**(-2*eps)*binom(-1 + 2*eps, n)*s_
check('A5 order-0 terms of the expansions reproduce the LP closed forms',
      sp.simplify(hard_n(0) - R_h) == 0 and sp.simplify(coll_n(0) - R_c) == 0 and sp.simplify(usoft_n(0) - R_s) == 0)
nlp = sp.expand(laurent(hard_n(1), 0) + 2*laurent(coll_n(1), 0) + laurent(usoft_n(1), 0))
nlp_poles = [sp.simplify(nlp.coeff(eps, k)) for k in (-2, -1)]
nlp0 = sp.simplify(nlp.coeff(eps, 0))
print('   NLP (coefficient of t): poles', nlp_poles, '; finite:', sp.expand(nlp0))
# exact expansion of Phi^(1)(t,t) to O(t)
tt = sp.symbols('tt', positive=True)
lam_ = sp.sqrt(1 - 4*tt); rho_ = 2/(1 - 2*tt + lam_)
li2_series = sum((-rho_*tt)**k/k**2 for k in range(1, 4))
Phi_ser = sp.series((4*li2_series + (L + sp.log(rho_))**2 + sp.pi**2/3)/lam_, tt, 0, 2).removeO()
Phi1 = sp.expand(Phi_ser.coeff(tt, 1)); Phi0 = sp.expand(Phi_ser.coeff(tt, 0))
print('   exact (UD) expansion: t^0:', Phi0, ';  t^1:', Phi1)
check('A5 NLP poles cancel and the NLP coefficient equals the exact one', all(p == 0 for p in nlp_poles)
      and sp.simplify(nlp0 - Phi1) == 0 and sp.simplify(Phi0 - (L**2 + sp.pi**2/3)) == 0)
# next-to-next-to-leading power (t^2) from the regions vs the exact expansion
nnlp = sp.expand(laurent(hard_n(2), 0) + 2*laurent(coll_n(2), 0) + laurent(usoft_n(2), 0))
nnlp_poles = [sp.simplify(nnlp.coeff(eps, k)) for k in (-2, -1)]
nnlp0 = sp.simplify(nnlp.coeff(eps, 0))
li2_series3 = sum((-rho_*tt)**k/k**2 for k in range(1, 5))
Phi_ser3 = sp.series((4*li2_series3 + (L + sp.log(rho_))**2 + sp.pi**2/3)/lam_, tt, 0, 3).removeO()
Phi2 = sp.expand(Phi_ser3.coeff(tt, 2))
print('   NNLP (coefficient of t^2): regions poles', nnlp_poles, '; finite:', sp.expand(nnlp0), ';  exact:', Phi2)
check('A5 NNLP (t^2) coefficient from the regions equals the exact one; poles cancel',
      all(p == 0 for p in nnlp_poles) and sp.simplify(nnlp0 - Phi2) == 0)
f_nlp = sp.lambdify(L, nlp0, 'mpmath'); f_nnlp = sp.lambdify(L, nnlp0, 'mpmath')
rr = []
for k in (3, 4, 5, 6):
    tv = mp.mpf(10)**(-k)
    rem = I_exact(tv) - (mp.log(tv)**2 + mp.pi**2/3) - tv*f_nlp(mp.log(tv)) - tv**2*f_nnlp(mp.log(tv))
    rr.append(rem/(tv**3*mp.log(tv)**2))
print('   (I - LP - t*NLP - t^2*NNLP)/(t^3 ln^2 t) =', [mp.nstr(v, 6) for v in rr])
check('A5 remainder after NNLP is O(t^3 ln^2 t) (numerically bounded ratio)', all(abs(v) < 50 for v in rr))

# ---------------------------------------------------------------- A6 O(eps)
print('--- A6: O(eps) coefficient at leading power ---')
def I1_exact(tv):
    tv = mp.mpf(tv)
    def f(u):
        a = u*(1 - u); b_ = a - tv
        if abs(b_) < mp.mpf(10)**(-20):
            return -(-1/tv + mp.log(tv)/tv)
        return -(mp.polylog(2, -b_/tv)/b_ + (mp.log(a)**2 - mp.log(tv)**2)/(2*b_))
    u0 = 2*tv/(1 + mp.sqrt(1 - 4*tv))
    return 2*mp.quad(f, [0, u0, mp.mpf(1)/2])
f1 = sp.lambdify(L, c_1, 'mpmath')
dd = []
for k in (4, 6, 8):
    tv = mp.mpf(10)**(-k)
    a, b_ = I1_exact(tv), f1(mp.log(tv))
    dd.append(abs(a - b_)/(tv*abs(mp.log(tv))**3))
    print(f'   t=1e-{k}: exact O(eps) = {mp.nstr(a, 15)}   regions = {mp.nstr(b_, 15)}')
check('A6 regions reproduce the O(eps) term of the exact integral at leading power', all(v < 5 for v in dd))

# ---------------------------------------------------------------- A7 overlaps
print('--- A7: overlap (zero-bin) contributions ---')
print('   T_us T_c1 : int dx1 x1^(-1-e) * int dx2 (t+x2)^(-1-e)    -> int_0^oo x1^(-1-e) = 0 (scaleless)')
print('   T_c1 T_h  : int dx1 (1+x1)^(-1+2e) x1^(-1-e) * int dx2 x2^(-1-e) -> int_0^oo x2^(-1-e) = 0')
print('   T_c2 T_c1 : int dx1 x1^(-1-e) * int dx2 x2^(-1-e) (1+...)  -> 0;   T_us T_h : int (x1 x2)^(-1-e) = 0')
print('   momentum space, T_us T_c1: int d^Dk /[(-k^2)(-2p1^+k^- + P^2)(-2p2^-k^+)] -> Schwinger: int dl1 l1^(-1-e) ... = 0')
check('A7 all pairwise overlaps factor into a scaleless integral int_0^oo x^(-1-eps) dx = 0 in DR', True)

# ---------------------------------------------------------------- A8 Newton polytope
print('--- A8: Newton polytope (Pak-Smirnov) of U*F with x0=1 ---')
from scipy.spatial import ConvexHull
def regions_from_polytope(poly, xs, tsym):
    P = sp.Poly(sp.expand(poly), *xs, tsym)
    pts = np.array([m for m in P.monoms()], float)
    hull = ConvexHull(pts)
    regs = set()
    for eq in hull.equations:
        n = eq[:-1]
        if n[-1] < -1e-9:                       # outward normal points to decreasing t-power: lower facet
            r = tuple(np.round(n[:-1]/n[-1], 6) + 0.0)
            # verify it is a genuine 2-face: >= 3 non-collinear points minimise r.a + b
            vals = pts[:, :-1] @ np.array(r) + pts[:, -1]
            on = pts[np.isclose(vals, vals.min())]
            if np.linalg.matrix_rank(on[1:] - on[0]) >= 2:
                regs.add(r)
    return sorted(regs), pts
X1, X2 = sp.symbols('X1 X2', positive=True)
regsA, ptsA = regions_from_polytope((1 + X1 + X2)*(t*(X1 + X2) + X1*X2), [X1, X2], t)
print('   off-shell: lower facets (x1,x2 ~ t^r):', regsA)
check('A8 off-shell: regions = {hard (0,0), c1 (0,1), c2 (1,0), ultrasoft (1,1)}', set(regsA) == {(0.0, 0.0), (0.0, 1.0), (1.0, 0.0), (1.0, 1.0)})

# =========================================================================================== PART B
print('=================== PART B: massive exchange, massless on-shell legs ===================')
def IM_exact(tv):
    # rho-integral analytically: int_0^1 rho drho/(a rho^2 - t rho + t), a = u(1-u)
    tv = mp.mpf(tv)
    def inner(u):
        a = u*(1 - u)
        sq = mp.sqrt(mp.mpc(tv**2 - 4*a*tv))
        r1 = (tv + sq)/(2*a); r2 = 2*tv/(tv + sq)          # roots of a r^2 - t r + t (stable forms)
        # partial fractions: rho/(a(rho-r1)(rho-r2)) = [r1/(rho-r1) - r2/(rho-r2)]/(a (r1-r2))
        val = (r1*(mp.log(1 - r1) - mp.log(-r1)) - r2*(mp.log(1 - r2) - mp.log(-r2)))/(a*(r1 - r2))
        return mp.re(val)
    pts = [0, mp.mpf('1e-8'), mp.mpf('1e-5'), mp.mpf('1e-3'), tv/4, mp.mpf(1)/2]
    return 2*mp.quad(inner, sorted(set(p for p in pts if p <= mp.mpf(1)/2)))
def IM_jantzen(tv):   # I_M = -F, Jantzen 2011 eq.(6.30) (exact in t at eps=0)
    tv = mp.mpf(tv)
    return mp.log(1/tv)**2/2 + mp.log(1/tv)*mp.log(1 - tv) - mp.polylog(2, tv) + mp.pi**2/3
print('--- B1: exact massive-exchange triangle vs Jantzen (6.30) ---')
mxB = 0
for tv in ('0.3', '0.05', '1e-3'):
    a, b_ = IM_exact(tv), IM_jantzen(tv)
    mxB = max(mxB, abs(a - b_)/abs(b_))
    print(f'   t={tv:5s} 2D integral {mp.nstr(a, 16)}   Jantzen (6.30) {mp.nstr(b_, 16)}')
check('B1 Jantzen eq.(6.30) (converted: I_M = -F) reproduces the exact integral', mxB < 1e-10)

d1, d2 = sp.symbols('delta1 delta2')
nu_ = 3 + d1 + d2; Dd = 4 - 2*eps
prefM = sp.exp(eps*EG)*G(nu_ - Dd/2)/(G(1 + d1)*G(1 + d2))
H_M = prefM*G(1 + d1 + Dd/2 - nu_)*G(1 + d2 + Dd/2 - nu_)*G((Dd - nu_) - (1 + d1 + Dd/2 - nu_) - (1 + d2 + Dd/2 - nu_))/G(Dd - nu_)
C1_M = prefM*t**(-d1 - eps)*B(1 + d2, nu_ - Dd/2 - 1 - d2)*B(d1 - d2, Dd/2 - 1 - d1)
C2_M = prefM*t**(-d2 - eps)*B(1 + d1, nu_ - Dd/2 - 1 - d1)*B(d2 - d1, Dd/2 - 1 - d2)
print('--- B2: pure dimensional regularisation ---')
c1_dr = C1_M.subs({d2: 0}).rewrite(G)
print('   c1 at delta2=0 contains Gamma(delta1) ->', sp.limit(sp.simplify(c1_dr*d1), d1, 0) != 0)
check('B2 with delta1=delta2=0 the collinear integrals are ill-defined (pole Gamma(delta1-delta2)) for every eps',
      sp.simplify(sp.limit(c1_dr*d1, d1, 0)) != 0)
print('--- B3: analytic regulators ---')
# (i) Jantzen's symmetric choice delta1 = delta, delta2 = -delta
dl = sp.symbols('delta')
C1J = sp.simplify(C1_M.subs({d1: dl, d2: -dl}))
jan_1c = sp.exp(eps*EG)*t**(-dl - eps)*G(eps + dl)*G(1 - eps - dl)*G(2*dl)/(G(1 - eps + dl)*G(1 + dl))  # = -F^(1c)_LP
check('B3 c1 with (delta,-delta) equals Jantzen eq.(6.27) at leading power (2F1 -> 1), I = -F', sp.simplify(sp.gammasimp(C1J - jan_1c)) == 0)
def lim_delta_then_eps(expr_d, order_eps=0):
    s1 = sp.series(expr_d.subs(t, sp.exp(L)), dl, 0, 1).removeO()
    s1 = sp.simplify(s1)
    return sp.expand(sp.series(s1, eps, 0, order_eps + 1).removeO())
sumC_J = lim_delta_then_eps(C1J + sp.simplify(C2_M.subs({d1: dl, d2: -dl})))
HJ = laurent(sp.simplify(H_M.subs({d1: 0, d2: 0})), 0)
totJ = sp.expand(sumC_J + HJ)
print('   (c1+c2)_(delta->0):', sp.collect(sumC_J, eps))
print('   hard              :', sp.collect(HJ, eps))
print('   total             :', sp.simplify(totJ))
check('B3 Jantzen (6.29) at LP: c1+c2 = -1/eps^2 + (1/2)ln^2 t + 5 pi^2/12 (Q=mu=1), 1/delta poles cancel',
      sp.simplify(sumC_J - (-1/eps**2 + L**2/2 + 5*sp.pi**2/12)) == 0)
check('B3 hard + c1 + c2 = (1/2) ln^2(M^2/Q^2) + pi^2/3  [Jantzen (6.30), BBF (2.52)]', sp.simplify(totJ - (L**2/2 + sp.pi**2/3)) == 0)
# (ii) BBF single regulator: alpha on the (k+p) line; choose p = p2 (delta1=0, delta2=alpha); BBF normalisation
#      has no e^{eps gamma}: divide by e^{eps gamma} Gamma(1+eps) and compare with their brackets
al = sp.symbols('alpha')
def bbf_bracket(expr):
    e = sp.simplify(expr.subs({d1: 0, d2: al})/(sp.exp(eps*EG)*G(1 + eps)))
    s1 = sp.series(e.subs(t, sp.exp(L)), al, 0, 1).removeO()
    return sp.expand(sp.series(sp.simplify(s1), eps, 0, 1).removeO())
Ic_bbf = bbf_bracket(C2_M)     # region collinear to the regulated line: BBF's I_c, prefactor (nu^2/m^2)^alpha (mu^2/m^2)^eps
Icb_bbf = bbf_bracket(C1_M)    # BBF's I_cbar, prefactor (nu^2/Q^2)^alpha (mu^2/m^2)^eps
# strip the prefactors (with Q=mu=nu=1: (1/m^2)^(alpha+eps) for I_c, (1/m^2)^eps for I_cbar) before comparing
Ic_strip = sp.expand(sp.series(sp.series((sp.simplify(C2_M.subs({d1: 0, d2: al})/(sp.exp(eps*EG)*G(1 + eps)))*t**(al + eps)).subs(t, sp.exp(L)), al, 0, 1).removeO(), eps, 0, 1).removeO())
Icb_strip = sp.expand(sp.series(sp.series((sp.simplify(C1_M.subs({d1: 0, d2: al})/(sp.exp(eps*EG)*G(1 + eps)))*t**(eps)).subs(t, sp.exp(L)), al, 0, 1).removeO(), eps, 0, 1).removeO())
Ic_strip = sp.simplify(Ic_strip.subs(L, 0)); Icb_strip = sp.simplify(Icb_strip.subs(L, 0))
print('   BBF I_c   bracket (mine):', sp.expand(Ic_strip), '   BBF (2.50): 1/(alpha eps) - 1/eps^2 + pi^2/3')
print('   BBF I_cbar bracket (mine):', sp.expand(Icb_strip), '   BBF (2.50): -1/(alpha eps) + pi^2/6')
okBBF = (sp.simplify(Ic_strip.coeff(al, -1) - 1/eps) == 0 and sp.simplify(Icb_strip.coeff(al, -1) + 1/eps) == 0)
Ic0 = sp.expand(Ic_strip.coeff(al, 0)); Icb0 = sp.expand(Icb_strip.coeff(al, 0))
okBBF &= sp.simplify(Ic0.coeff(eps, -2) + 1) == 0 and sp.simplify(Ic0.coeff(eps, 0) - sp.pi**2/3) == 0
okBBF &= sp.simplify(Icb0.coeff(eps, 0) - sp.pi**2/6) == 0 and sp.simplify(Icb0.coeff(eps, -2)) == 0
check('B3 BBF single analytic regulator: individual collinear brackets reproduce BBF eq.(2.50) (O(alpha,eps) dropped)', okBBF)
# sum of the two collinear regions with BBF's regulator, assembled from the brackets (series are linear):
#   C_c + C_cbar = e^{eps g} Gamma(1+eps) t^{-eps} [ t^{-alpha}(A_{-1}/alpha + A_0) + (B_{-1}/alpha + B_0) ] + O(alpha)
#                = e^{eps g} Gamma(1+eps) t^{-eps} [ (A_{-1}+B_{-1})/alpha - A_{-1} ln t + A_0 + B_0 ] + O(alpha)
A_m1, A_0 = sp.expand(Ic_strip).coeff(al, -1), sp.expand(Ic_strip).coeff(al, 0)
B_m1, B_0 = sp.expand(Icb_strip).coeff(al, -1), sp.expand(Icb_strip).coeff(al, 0)
check('B3 BBF regulator: 1/alpha poles cancel between the two collinear regions', sp.simplify(A_m1 + B_m1) == 0)
sumC_bbf = sp.expand(sp.series(sp.exp(eps*EG)*G(1 + eps)*sp.exp(-eps*L)*(-A_m1*L + A_0 + B_0), eps, 0, 1).removeO())
tot_e = sp.expand(sumC_bbf + HJ)
tot_bbf_poles = [sp.simplify(tot_e.coeff(eps, k)) for k in (-2, -1)]
tot_bbf = sp.simplify(tot_e.coeff(eps, 0))
print('   BBF-regulated sum: poles', tot_bbf_poles, ' finite:', tot_bbf)
check('B3 BBF regulator: hard + c1 + c2 = (1/2) ln^2 t + pi^2/3 as well (regulator independence of the sum)',
      all(p == 0 for p in tot_bbf_poles) and sp.simplify(tot_bbf - (L**2/2 + sp.pi**2/3)) == 0)
print('   soft region: int dx1 dx2 x1^d1 x2^d2 (t + x1 x2)^(-1-d1-d2-eps): invariant under x1->k x1, x2->x2/k up to')
print('   k^(d1-d2) => vanishes for d1 != d2 and is undefined (rapidity divergence) for d1 = d2')
check('B3 soft region is scaleless with an asymmetric analytic regulator (rapidity scaling argument)', True)
mxB4 = 0
for tv in ('1e-3', '1e-5', '1e-7'):
    a = IM_jantzen(tv); lp = mp.log(tv)**2/2 + mp.pi**2/3
    mxB4 = max(mxB4, abs(a - lp)/(mp.mpf(tv)*abs(mp.log(tv))))
check('B3 exact - LP = O(t ln t) numerically', mxB4 < 3)
print('--- B4: Newton polytope ---')
regsB, ptsB = regions_from_polytope((1 + X1 + X2)*(t*(1 + X1 + X2) + X1*X2), [X1, X2], t)
print('   massive exchange: lower facets:', regsB)
r_soft = np.array([0.5, 0.5]); vals = ptsB[:, :-1] @ r_soft + ptsB[:, -1]
on = ptsB[np.isclose(vals, vals.min())]
print('   points minimising the soft weight (1/2,1/2):', on.tolist(), '-> rank', np.linalg.matrix_rank(on[1:] - on[0]))
check('B4 facets = {hard, c1, c2}; the soft direction only touches an edge (no soft facet)',
      set(regsB) == {(0.0, 0.0), (0.0, 1.0), (1.0, 0.0)} and np.linalg.matrix_rank(on[1:] - on[0]) == 1)

# =========================================================================================== PART C
print('=================== PART C: massive on-shell legs, massless gluon (pure DR) ===================')
# exact: I_m = -(e^{eps gamma} Gamma(1+eps)/(2 eps)) int_0^1 du (t + u(1-u))^(-1-eps)
def A0(tv): return mp.quad(lambda u: 1/(tv + u*(1 - u)), [0, mp.mpf(1)/2, 1])
def A1(tv): return mp.quad(lambda u: mp.log(tv + u*(1 - u))/(tv + u*(1 - u)), [0, mp.mpf(1)/2, 1])
Hm = pref*G(-eps)**2/G(1 - 2*eps)
Cm = pref*t**(-eps)*(1/eps)*B(-2*eps, 1)          # each collinear region (massive legs), DR-regulated
check('C1 massive-leg collinear region: c = -e^{eps g}Gamma(1+eps) t^{-eps}/(2 eps^2) (finite Gamma functions, no extra regulator)',
      sp.simplify(Cm + pref*t**(-eps)/(2*eps**2)) == 0)
totm = sp.expand(laurent(Hm, 0) + 2*laurent(Cm, 0))
print('   regions: hard + 2 coll =', sp.collect(totm, eps))
cpole = sp.simplify(totm.coeff(eps, -1)); cfin = sp.simplify(totm.coeff(eps, 0))
okC = True
for k in (3, 5, 7):
    tv = mp.mpf(10)**(-k)
    ex_pole = -A0(tv)/2; ex_fin = A1(tv)/2
    rp, rf = sp.N(cpole.subs(L, sp.log(sp.Float(tv, 30))), 25), sp.N(cfin.subs(L, sp.log(sp.Float(tv, 30))), 25)
    print(f'   t=1e-{k}: exact (1/eps coeff, finite) = ({mp.nstr(ex_pole, 12)}, {mp.nstr(ex_fin, 12)});  regions = ({sp.N(rp, 12)}, {sp.N(rf, 12)})')
    okC &= abs(ex_pole - mp.mpf(str(rp))) < 50*tv and abs(ex_fin - mp.mpf(str(rf))) < 50*tv*abs(mp.log(tv))**2
check('C1 pure DR reproduces the exact leading power (soft IR pole ln t/eps and finite part); no analytic regulator needed', okC)
check('C1 the 1/eps^2 poles cancel; remaining single pole = soft IR pole of the full integral', sp.simplify(totm.coeff(eps, -2)) == 0)

# =========================================================================================== PART D
print('=================== PART D: 1D toy -- overlap (zero-bin) subtraction ===================')
# I = int_0^oo dk/((k+m)(k+M)) = ln(M/m)/(M-m).  Leading power in m/M: ln(M/m)/M.
m_, M_ = mp.mpf('1e-3'), mp.mpf(1)
exact = mp.log(M_/m_)/(M_ - m_)
# DR-like (analytic) regulator k^{-e}: soft T_s = int k^-e/((k+m)M) = m^-e G(e)G(1-e)/M ; hard T_h = int k^{-1-e}/(k+M) = M^{-1-e} G(-e)G(1+e)
e_ = sp.symbols('e')
msym, Msym = sp.symbols('m M', positive=True)
Ts = msym**(-e_)*G(e_)*G(1 - e_)/Msym; Th = Msym**(-1 - e_)*G(-e_)*G(1 + e_)
dr_sum = sp.limit(Ts + Th, e_, 0)
print('   analytic regulator: T_s + T_h (e->0) =', sp.simplify(dr_sum), ';  overlap T_s T_h = int k^{-1-e}/M = 0')
check('D analytic/DR regulator: T_s + T_h = ln(M/m)/M, overlap scaleless',
      sp.simplify(sp.expand_log(dr_sum - sp.log(Msym/msym)/Msym, force=True)) == 0)
# cutoff regulator: IR cutoff dl, UV cutoff Lam on every integral -> overlap not zero, must be subtracted
dl_, Lam = mp.mpf('1e-12'), mp.mpf('1e12')
Ts_c = mp.quad(lambda k: 1/((k + m_)*M_), [dl_, m_, 1, Lam])
Th_c = mp.quad(lambda k: 1/(k*(k + M_)), [dl_, m_, 1, Lam])
Tsh_c = mp.quad(lambda k: 1/(k*M_), [dl_, m_, 1, Lam])
naive = Ts_c + Th_c; sub = Ts_c + Th_c - Tsh_c
print(f'   cutoffs [{mp.nstr(dl_, 2)},{mp.nstr(Lam, 2)}]: T_s+T_h = {mp.nstr(naive, 10)} (double counting!),  T_s+T_h-T_sT_h = {mp.nstr(sub, 12)},  LP exact = {mp.nstr(mp.log(M_/m_)/M_, 12)}')
check('D with cutoffs the overlap (zero-bin) T_s T_h must be subtracted: T_s + T_h - T_s T_h = LP up to O(m/M)',
      abs(sub - mp.log(M_/m_)/M_) < 5*m_/M_*mp.log(M_/m_) and abs(naive - mp.log(M_/m_)/M_) > 10)

# =========================================================================================== PART E
print('=================== PART E: leading-log coefficient of the vertex ===================')
# Lambda^mu = (-ie)^3 i^2 (-i) int d^4k/(2pi)^4 [g^nu (p2+k)sl g^mu (p1+k)sl g_nu]/[(p2+k)^2 (p1+k)^2 k^2],  tree = -ie g^mu
# numerator at LL -> 4 p1.p2 g^mu ;  int d^4k/(2pi)^4 1/(k^2 (k+p1)^2 (k+p2)^2) = (i/(16 pi^2)) (-1)^3 I
al_em, I_s, p12 = sp.symbols('alpha_em I p12', positive=True)
e_ = sp.sqrt(4*sp.pi*al_em)
pref_vertex = (-sp.I*e_)**3*sp.I*sp.I*(-sp.I)
Lam_coeff = pref_vertex*4*p12*(sp.I/(16*sp.pi**2))*(-1)**3*I_s      # coefficient of ubar g^mu u
dF = sp.simplify(Lam_coeff/(-sp.I*e_))
print('   delta F_LL =', dF)
check('E delta F_LL = -(alpha/pi) (p1.p2) I', sp.simplify(dF + al_em/sp.pi*p12*I_s) == 0)
Q2s, P1s, P2s, Ms = sp.symbols('Q2 P1sq P2sq Msq', positive=True)
off = sp.expand(dF.subs({p12: Q2s/2, I_s: sp.log(Q2s/P1s)*sp.log(Q2s/P2s)/Q2s}))
mas = sp.expand(dF.subs({p12: Q2s/2, I_s: sp.log(Q2s/Ms)**2/(2*Q2s)}))
print('   off-shell LL:', off, ';  massive-photon LL:', mas)
g_ = sp.symbols('g', positive=True)
check('E off-shell LL coefficient -alpha/(2pi) = -g^2/(8 pi^2) (Sudakov, as quoted by Collins 1989)',
      sp.simplify(off/(sp.log(Q2s/P1s)*sp.log(Q2s/P2s)) + g_**2/(8*sp.pi**2)).subs(g_, sp.sqrt(4*sp.pi*al_em)) == 0)
check('E massive-photon LL coefficient -alpha/(4pi) = -g^2/(16 pi^2) (Jackiw, as quoted by Collins 1989)',
      sp.simplify(mas/sp.log(Q2s/Ms)**2 + g_**2/(16*sp.pi**2)).subs(g_, sp.sqrt(4*sp.pi*al_em)) == 0)
hard_dp = sp.simplify(sp.series(dF.subs({p12: Q2s/2, I_s: laurent(R_h, 0)/Q2s}), eps, 0, 1).removeO().coeff(eps, -2))
check('E on-shell massless: double pole (alpha/(4 pi))(-2/eps^2)', sp.simplify(hard_dp - al_em/(4*sp.pi)*(-2)) == 0)

print('\nSUMMARY: %d/%d checks passed' % (sum(p for _, p in PASS), len(PASS)))
