"""
W10 / Ch9 -- independent re-derivation of everything used in ex:method-naive-induction and
ex:method-sudakov-subtraction (one-loop off-shell scalar triangle), in the conventions of the book:

  light-front v^pm = (v^0 pm v^3)/sqrt2, v.w = v^+w^- + v^-w^+ - vT.wT ; components written (plus, minus, T)
  p1 = (P, -m2/(2P), 0_T), p2 = (m2/(2P'), -P', 0_T), both incoming, p_i^2 = -m2
  Qt2 = 2 P P'  (tilde Q^2),  Q2 = -(p1+p2)^2 = (Qt2+m2)^2/Qt2
  D_g = -k^2, D_1 = -(p1-k)^2, D_2 = -(p2+k)^2 (each with -i0), Gamma = 1/(D_g D_1 D_2)
  e1 = m2+2P k^-, h1 = 2P k^-, t1 = 2P k^- - k^2 ; e2 = m2+2P'k^+, h2 = 2P'k^+, t2 = 2P'k^+ - k^2
  measure mu^{2eps} int d^dk/(i pi^{d/2}),  d = 4 - 2 eps

Checks:
 (A) decompositions D_1 = e1 - (m2/P)k^+ + D_g, D_2 = e2 - (m2/P')k^- + D_g; Q2 formula
 (B) approximators as per-line semilattice maps; chain recursion == closed forms; (Com), (Abs)
 (C) VF-REF-18: C_{C2}Gamma and (1-T_{C1})T_S Gamma; the U_H and U_{C1} grouped forms
 (D) k^- residues of T_{C2}Gamma (pinch) vs C_{C2}Gamma (no pinch)
 (E) homogeneity exponents of T_{C1}Gamma at the rapidity end and in the UV
 (F) fibered densities by my own residue code; kappa and x integrals numerically at eps=0.3 vs closed forms (VF-REF-3)
 (G) eps expansion of the sum of the four values; pole cancellation; finite part
 (H) exact remainder from Usyukina-Davydychev Phi^(1); expansion; value at m2=0.02, P=0.8, P'=1.3
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

npass = 0; nfail = 0
def check(name, ok, info=''):
    global npass, nfail
    if ok: npass += 1
    else: nfail += 1
    print(('[PASS] ' if ok else '[FAIL] ') + name + ((' : ' + str(info)) if info != '' else ''))

kp, km = sp.symbols('kp km', real=True)
kT2 = sp.symbols('kT2', positive=True)
P, Pp, m2 = sp.symbols('P Pp m2', positive=True)

def dot(a, b):  # (plus, minus, T2) with T part given as a scalar product value if needed
    return a[0]*b[1] + a[1]*b[0]
def sq(a, aT2):
    return 2*a[0]*a[1] - aT2

k = (kp, km)
p1 = (P, -m2/(2*P)); p2 = (m2/(2*Pp), -Pp)
Dg = -sq(k, kT2)
D1 = -sq((p1[0]-kp, p1[1]-km), kT2)
D2 = -sq((p2[0]+kp, p2[1]+km), kT2)
e1 = m2 + 2*P*km; h1 = 2*P*km; t1 = 2*P*km + Dg
e2 = m2 + 2*Pp*kp; h2 = 2*Pp*kp; t2 = 2*Pp*kp + Dg
Qt2 = 2*P*Pp

# ---------------------------------------------------------------- (A)
check('(A) p1^2 = p2^2 = -m2', sp.simplify(sq(p1, 0)+m2) == 0 and sp.simplify(sq(p2, 0)+m2) == 0)
check('(A) D1 = e1 - (m2/P) k^+ + D_g', sp.simplify(D1 - (e1 - m2/P*kp + Dg)) == 0)
check('(A) D2 = e2 - (m2/P\') k^- + D_g', sp.simplify(D2 - (e2 - m2/Pp*km + Dg)) == 0)
Q2 = -sq((p1[0]+p2[0], p1[1]+p2[1]), 0)
check('(A) Q^2 = (Qt2+m2)^2/Qt2', sp.simplify(Q2 - (Qt2+m2)**2/Qt2) == 0)
check('(A) h_i - t_i = k^2 = -D_g', sp.simplify(h1 - t1 - (-Dg)) == 0 and sp.simplify(h2 - t2 - (-Dg)) == 0)

# ---------------------------------------------------------------- (B) approximators as maps on line states
# line state in {D, e, t, h}; composition table: x o x = x, e o t = t o e = h, h o x = h, D o a = a
def comp(s, a):
    if a == 'D': return s
    if s == 'D': return a
    if s == a: return s
    return 'h'
act = {'S': ('e', 'e'), 'C1': ('D', 'h'), 'C2': ('h', 'D'), 'H': ('t', 't')}   # (line 1, line 2)
den = {1: {'D': D1, 'e': e1, 't': t1, 'h': h1}, 2: {'D': D2, 'e': e2, 't': t2, 'h': h2}}
# an "integrand" = dict {(s1,s2): coeff}; value = sum coeff/(Dg den1[s1] den2[s2])
def T(R, F):
    out = {}
    for (s1, s2), c in F.items():
        key = (comp(s1, act[R][0]), comp(s2, act[R][1]))
        out[key] = out.get(key, 0) + c
    return {kk: v for kk, v in out.items() if v != 0}
def add(F, G, s=1):
    out = dict(F)
    for kk, v in G.items():
        out[kk] = out.get(kk, 0) + s*v
    return {kk: v for kk, v in out.items() if v != 0}
def val(F):
    return sum(c/(Dg*den[1][s1]*den[2][s2]) for (s1, s2), c in F.items())
Gam = {('D', 'D'): 1}
order = ['S', 'C1', 'C2', 'H']
below = {'S': [], 'C1': ['S'], 'C2': ['S'], 'H': ['S', 'C1', 'C2']}
C = {}
for R in order:
    X = dict(Gam)
    for Rp in below[R]:
        X = add(X, C[Rp], -1)
    C[R] = T(R, X)
CS, CC1, CC2, CH = [sp.together(val(C[R])) for R in order]
check('(B) C_S Gamma = 1/(D_g e1 e2)', sp.simplify(CS - 1/(Dg*e1*e2)) == 0)
check('(B) C_C1 Gamma = (1/(D_g h2))(1/D1 - 1/e1)', sp.simplify(CC1 - (1/(Dg*h2))*(1/D1 - 1/e1)) == 0)
check('(B) C_C2 Gamma = (1/(D_g h1))(1/D2 - 1/e2)', sp.simplify(CC2 - (1/(Dg*h1))*(1/D2 - 1/e2)) == 0)
check('(B) C_H Gamma = (1/D_g)(1/t1-1/h1)(1/t2-1/h2) = D_g/(t1 h1 t2 h2)',
      sp.simplify(CH - (1/Dg)*(1/t1-1/h1)*(1/t2-1/h2)) == 0 and sp.simplify(CH - Dg/(t1*h1*t2*h2)) == 0)
# commutation and absorption
def same(F, G): return sp.simplify(val(F) - val(G)) == 0
F0 = {('D', 'D'): 1, ('e', 'D'): 2, ('t', 'h'): -3}
ok_com = all(same(T(a, T(b, F0)), T(b, T(a, F0))) for a in order for b in order)
ok_abs = same(T('C1', T('C2', F0)), T('C1', T('S', T('C2', F0))))
ok_idem = all(same(T(a, T(a, F0)), T(a, F0)) for a in order)
check('(B) (Com) T_R T_R\' = T_R\' T_R on a test integrand', ok_com)
check('(B) (Abs) T_C1 T_C2 = T_C1 T_S T_C2', ok_abs)
check('(B) idempotence T_R^2 = T_R', ok_idem)
# product formula
def one_minus(R, F): return add(F, T(R, F), -1)
rprod = one_minus('H', one_minus('C2', one_minus('C1', one_minus('S', Gam))))
r = sp.together(1/(Dg*D1*D2) - CS - CC1 - CC2 - CH)
check('(B) r = prod_R (1-T_R) Gamma (product formula)', sp.simplify(val(rprod) - r) == 0)
Dl1 = 1/D1 - 1/h1; Dl2 = 1/D2 - 1/h2; Dp1 = 1/e1 - 1/h1; Dp2 = 1/e2 - 1/h2; dl1 = 1/t1 - 1/h1; dl2 = 1/t2 - 1/h2
check('(B) r = (1/D_g)[Dl1 Dl2 - Dp1 Dp2 - dl1 dl2]', sp.simplify(r - (Dl1*Dl2 - Dp1*Dp2 - dl1*dl2)/Dg) == 0)
check('(B) U_H form r = (1/D_g)[(Dl1-dl1)Dl2 + dl1(Dl2-dl2) - Dp1 Dp2]',
      sp.simplify(r - ((Dl1-dl1)*Dl2 + dl1*(Dl2-dl2) - Dp1*Dp2)/Dg) == 0)
check('(B) Dl_i - dl_i = (t_i - D_i)/(D_i t_i), Dp_i = -m2/(e_i h_i)',
      sp.simplify(Dl1-dl1 - (t1-D1)/(D1*t1)) == 0 and sp.simplify(Dp1 + m2/(e1*h1)) == 0 and sp.simplify(Dp2 + m2/(e2*h2)) == 0)
XC1 = one_minus('C1', one_minus('S', Gam))
check('(B) U_C1 object (1-T_C1)(1-T_S)Gamma = (1/D_g)[(1/D1) Dl2 - (1/e1) Dp2]',
      sp.simplify(val(XC1) - ((1/D1)*Dl2 - (1/e1)*Dp2)/Dg) == 0)
check('(B) t_i - D_i : t1 - D1 = m2/P k^+ - m2 ; t2-D2 = m2/P\' k^- - m2',
      sp.simplify(t1 - D1 - (m2/P*kp - m2)) == 0 and sp.simplify(t2 - D2 - (m2/Pp*km - m2)) == 0)

# ---------------------------------------------------------------- (C) VF-REF-18
TC2G = T('C2', Gam); TSG = T('S', Gam)
CC2_alt = m2/(2*P*Pp)/(Dg*D2*e2) - 1/(h1*D2*e2)
check('(C) C_C2 Gamma = T_C2(Gamma - T_S Gamma) = m2/(2PP\') 1/(D_g D2 e2) - 1/(h1 D2 e2)', sp.simplify(CC2 - CC2_alt) == 0)
check('(C) e2 - D2 = (m2/P\')k^- - D_g', sp.simplify(e2 - D2 - (m2/Pp*km - Dg)) == 0)
lhsb = val(add(TSG, T('C1', TSG), -1))
check('(C) (1-T_C1) T_S Gamma = (1/(D_g e1))(1/e2 - 1/h2)', sp.simplify(lhsb - (1/(Dg*e1))*(1/e2-1/h2)) == 0)
check('(C) relative size (1/e2-1/h2)/(1/e2) = -m2/(2P\'k^+)', sp.simplify((1/e2-1/h2)*e2 + m2/(2*Pp*kp)) == 0)

# ---------------------------------------------------------------- (D) residues: pinch of T_C2 Gamma in C1
# denominators are written as (beta*km + a - i0 w); pole in upper half plane iff w/beta > 0
def poles_of(expr_dens):
    out = []
    for d, w in expr_dens:
        beta = sp.diff(d, km); a = sp.simplify(d - beta*km)
        out.append((d, beta, a, w))
    return out
def kminus_integral(dens, numer=1, kpval=None, closing='auto'):
    """int dkm numer/prod dens, each dens = (expr linear in km, w>0 meaning -i0*w); returns 2 pi i * sum of residues
    on the side that contains the poles in the upper half plane (closing up) -- valid if degree <= -2"""
    # find upper-half-plane poles: Im(pole) = +i0 w/beta -> UHP iff beta>0 (since d - i0 w = 0 -> km = (i0 w - a)/beta)
    res = 0
    for i, (d, w) in enumerate(dens):
        beta = sp.diff(d, km)
        bval = beta.subs(kp, kpval) if kpval is not None else beta
        if bval == 0: continue
        if sp.sign(bval) > 0:   # pole in UHP
            pole = sp.solve(sp.Eq(d, 0), km)[0]
            rest = numer
            for j, (dj, wj) in enumerate(dens):
                if j != i: rest = rest/dj
            res += (rest/beta).subs(km, pole)
    return sp.simplify(2*sp.pi*sp.I*res)
kpv = sp.Rational(3, 10)
subsd = {P: sp.Rational(4, 5), Pp: sp.Rational(13, 10), m2: sp.Rational(1, 10)}
I_TC2 = kminus_integral([(Dg.subs(subsd), 1), (h1.subs(subsd), 1), (D2.subs(subsd), 1)], 1, kpv).subs(kp, kpv)
expected = 2*sp.pi*sp.I/(2*subsd[P]*kT2*(subsd[m2] + 2*subsd[Pp]*kpv + kT2))
check('(D) int dk^- T_C2 Gamma = 2 pi i/(2P kT^2 (e2 + kT^2)) ~ 1/kT^2 (collinear pinch, kp=0.3)', sp.simplify(I_TC2 - expected) == 0, I_TC2)
I_CC2a = kminus_integral([(Dg.subs(subsd), 1), (D2.subs(subsd), 1)], (m2/(2*P*Pp)/e2).subs(subsd), kpv).subs(kp, kpv)
I_CC2b = kminus_integral([(h1.subs(subsd), 1), (D2.subs(subsd), 1)], (-1/e2).subs(subsd), kpv).subs(kp, kpv)
check('(D) first term of C_C2 Gamma: both poles in LHP -> 0', sp.simplify(I_CC2a) == 0)
check('(D) second term: finite at kT->0: -2 pi i/(2P (e2+kT^2) e2)', sp.simplify(I_CC2b - (-2*sp.pi*sp.I/(2*subsd[P]*(subsd[m2]+2*subsd[Pp]*kpv + kT2)*(subsd[m2]+2*subsd[Pp]*kpv)))) == 0, I_CC2b)

# ---------------------------------------------------------------- (E) homogeneity exponents of T_C1 Gamma = 1/(D_g D1 h2)
a = sp.symbols('a', positive=True)
cp, cm, cT = sp.symbols('cp cm cT', positive=True)
eps = sp.symbols('epsilon')
TC1G = 1/(Dg*D1*h2)
# rapidity end: k = (a^2 cp, cm, a cT), a->0
expr = TC1G.subs({kp: a**2*cp, km: cm, kT2: a**2*cT**2})
lead = sp.limit(sp.log(sp.Abs(expr.subs({cp: 1, cm: sp.Rational(1, 3), cT: 1, P: 1, Pp: 1, m2: sp.Rational(1, 10)})))/sp.log(a), a, 0)
check('(E) rapidity end k=(a^2,1,a): integrand ~ a^-4', lead == -4, lead)
# measure dk^+ dk^- d^{d-2}k_T ~ a^2 * 1 * a^{d-2} = a^{4-2eps}: integral ~ int da a^{-1-2eps}: needs eps<0
# UV: k = (cp, a cm, sqrt(a) cT), a -> infinity
expr2 = TC1G.subs({kp: cp, km: a*cm, kT2: a*cT**2})
lead2 = sp.limit(sp.log(sp.Abs(expr2.subs({cp: 1, cm: 1, cT: 1, P: 1, Pp: 1, m2: sp.Rational(1, 10)})))/sp.log(a), a, sp.oo)
check('(E) UV direction k=(1,a,sqrt a): integrand ~ a^-2', lead2 == -2, lead2)
print('    => measure a^{4-2eps} at the rapidity end: int da a^{-1-2eps} converges at 0 only for eps<0;')
print('       measure a^{2-eps} in the UV: int da a^{-1-eps} converges at infinity only for eps>0.')

# ---------------------------------------------------------------- (F) fibered densities (own residue code) and values
mp.mp.dps = 30
def density(terms, Pv, Ppv, m2v):
    """terms: list of (coefficient, list of denominators) ; returns function rho(x, kappa) = (1/(pi i)) int dkm F"""
    xs, ks = sp.symbols('xs ks', real=True)
    fns = []
    for coeff, dens in terms:
        dd = [d.subs({P: Pv, Pp: Ppv, m2: m2v, kT2: ks}) for d in dens]
        cc = sp.sympify(coeff).subs({P: Pv, Pp: Ppv, m2: m2v, kT2: ks})
        # residues for kp = xs symbolic, sign of beta depends on xs: handle three intervals by evaluating sign numerically later
        fns.append((cc, dd))
    def rho(x, kap):
        tot = mp.mpf(0)
        for cc, dd in fns:
            ddx = [d.subs(kp, x) for d in dd]
            res = 0
            for i, d in enumerate(ddx):
                beta = sp.diff(d, km)
                if beta == 0: continue
                if float(beta) > 0:
                    pole = sp.solve(sp.Eq(d, 0), km)[0]
                    rest = cc.subs(kp, x)
                    for j, dj in enumerate(ddx):
                        if j != i: rest = rest/dj
                    res += (rest/beta).subs(km, pole)
            # (1/(pi i)) * 2 pi i * res = 2 res
            tot += mp.mpf(sp.N(sp.sympify(2*res).subs(sp.Symbol('ks', real=True), kap), 25))
        return tot
    return rho
# faster: closed-form densities derived symbolically per interval, then lambdify
def density_closed(terms, x_interval_point):
    """rho_F = (1/(pi i)) int dk^- F, computed by residues on the side with fewer poles."""
    xs = sp.Symbol('x', real=True); ks = sp.Symbol('kappa', positive=True)
    numv = {P: sp.Rational(4, 5), Pp: sp.Rational(13, 10), m2: sp.Rational(1, 10), kp: x_interval_point}
    tot = 0
    for coeff, dens in terms:
        dd = [d.subs({kT2: ks}) for d in dens]
        up, lo = [], []
        for i, d in enumerate(dd):
            beta = sp.diff(d, km)
            if beta == 0: continue
            (up if beta.subs(numv) > 0 else lo).append(i)
        side = up if len(up) <= len(lo) else lo
        sgn = 1 if side is up else -1
        res = 0
        for i in side:
            d = dd[i]; beta = sp.diff(d, km)
            pole = sp.solve(sp.Eq(d, 0), km)[0]
            rest = sp.sympify(coeff).subs({kT2: ks})
            for j, dj in enumerate(dd):
                if j != i: rest = rest/dj
            res += (rest/beta).subs(km, pole)
        tot += 2*sgn*res
    return sp.simplify(sp.sympify(tot).subs(kp, xs))
Pv, Ppv, m2v, epsv = sp.Rational(4, 5), sp.Rational(13, 10), sp.Rational(1, 10), mp.mpf('0.3')
x, kap = sp.Symbol('x', real=True), sp.Symbol('kappa', positive=True)
terms = {
    'S': [(1, [Dg, e1, e2])],
    'C1': [(1/h2, [Dg, D1]), (-1/h2, [Dg, e1])],
    'C2': [(1, [Dg, h1, D2]), (-1/e2, [Dg, h1])],
    'H': [(1/(h1*h2), [Dg, t1, t2]), (-1/h2, [Dg, h1, t2]), (-1/h1, [Dg, t1, h2]), (1/(h1*h2), [Dg])],
}
# careful: the C_H decomposition: (1/D_g)(1/t1-1/h1)(1/t2-1/h2) = 1/(Dg t1 t2) - 1/(Dg t1 h2) - 1/(Dg h1 t2) + 1/(Dg h1 h2)
terms['H'] = [(1, [Dg, t1, t2]), (-1/h2, [Dg, t1]), (-1/h1, [Dg, t2]), (1/(h1*h2), [Dg])]
# the last term 1/(Dg h1 h2) has degree -1 in km only through Dg: treat C_H as one combined integrand instead
CHcomb = sp.together(CH)
num_CH, den_CH = sp.fraction(CHcomb)
print('    C_H combined: numerator', sp.factor(num_CH), '; denominator', sp.factor(den_CH))
# C_H = Dg/(t1 h1 t2 h2): residues of Dg/(t1 h1 t2) (h2 is km independent): degree -2 in km
terms['H'] = [(Dg/h2, [t1, h1, t2])]
import numpy as np
from scipy import integrate as sint
def value_from_density(name, x_ranges):
    tot = 0.0
    for (xa, xb, xmid) in x_ranges:
        dens_expr = density_closed(terms[name], xmid).subs({P: Pv, Pp: Ppv, m2: m2v})
        if dens_expr == 0:
            continue
        f = sp.lambdify((x, kap), dens_expr, 'numpy')
        ev = float(epsv)
        def g(xx):
            # kappa integral with the weight kappa^{-eps}: split [0,1] (algebraic weight) and [1, inf)
            a = sint.quad(lambda kk: f(xx, kk), 0, 1, weight='alg', wvar=(-ev, 0), limit=200, epsabs=0, epsrel=1e-11)[0]
            b = sint.quad(lambda kk: kk**(-ev)*f(xx, kk), 1, np.inf, limit=200, epsabs=0, epsrel=1e-11)[0]
            return a + b
        xa_, xb_ = float(xa), (np.inf if xb == mp.inf else float(xb))
        if xb_ == np.inf:
            tot += sint.quad(g, xa_, 2*float(Pv), limit=200, epsabs=0, epsrel=1e-10)[0] + \
                   sint.quad(g, 2*float(Pv), np.inf, limit=200, epsabs=0, epsrel=1e-10)[0]
        else:
            tot += sint.quad(g, xa_, xb_, limit=200, epsabs=0, epsrel=1e-10)[0]
    return tot/float(mp.gamma(1-epsv))
Pf, Ppf, m2f = mp.mpf('0.8'), mp.mpf('1.3'), mp.mpf('0.1')
sl = -m2f/(2*Ppf)
ranges_pos = [(mp.mpf(0), Pf, mp.mpf('0.4')), (Pf, mp.inf, mp.mpf('2'))]
ranges_all = [(sl, mp.mpf(0), sl/2)] + ranges_pos
Qt2f = 2*Pf*Ppf
A_ = mp.gamma(1+epsv)*mp.gamma(1-epsv)**2/(epsv**2*mp.gamma(1-2*epsv))
B_ = mp.gamma(1+epsv)**2*mp.gamma(1-epsv)/epsv**2
closed = {'H': (1/Qt2f)*(1/Qt2f)**epsv*A_, 'C1': -(1/Qt2f)*(1/m2f)**epsv*A_, 'C2': -(1/Qt2f)*(1/m2f)**epsv*A_,
          'S': (1/Qt2f)*(Qt2f/m2f**2)**epsv*B_}
print('    closed forms at eps=0.3, P=0.8, P\'=1.3, m2=0.1, mu=1:', {kk: mp.nstr(v, 12) for kk, v in closed.items()})
for name in ['S', 'C1', 'C2', 'H']:
    v = value_from_density(name, ranges_all)
    check('(F) fibered value of C_%s Gamma = closed form (VF-REF-3)' % name, abs(v/float(closed[name])-1) < 1e-7,
          '%.12g vs %s' % (v, mp.nstr(closed[name], 12)))

# ---------------------------------------------------------------- (G) eps expansion of the sum
e = sp.symbols('epsilon')
Lq, Lm = sp.symbols('Lq Lm')   # Lq = ln(mu^2/Qt2), Lm = ln(mu^2/m2)
Asym = sp.gamma(1+e)*sp.gamma(1-e)**2/(e**2*sp.gamma(1-2*e))
Bsym = sp.gamma(1+e)**2*sp.gamma(1-e)/e**2
S_sum = sp.exp(e*Lq)*Asym - 2*sp.exp(e*Lm)*Asym + sp.exp(e*(2*Lm-Lq))*Bsym
ser = sp.series(S_sum, e, 0, 1).removeO()
ser = sp.expand(sp.simplify(ser))
c2 = sp.simplify(ser.coeff(e, -2)); c1 = sp.simplify(ser.coeff(e, -1)); c0 = sp.simplify(ser.coeff(e, 0))
check('(G) 1/eps^2 coefficient: 1 - 2 + 1 = 0', c2 == 0, c2)
check('(G) 1/eps coefficient vanishes for all mu', sp.simplify(c1) == 0, c1)
Lt = sp.symbols('Ltilde')  # ln(Qt2/m2) = Lm - Lq
c0s = sp.simplify(c0.subs(Lm, Lq + Lt))
check('(G) finite part = ln^2(Qt2/m2) + pi^2/3 (mu independent)', sp.simplify(c0s - (Lt**2 + sp.pi**2/3)) == 0, c0s)
# individual poles: H: 1/eps^2 + Lq/eps ; C_i: -(1/eps^2 + Lm/eps) ; S: 1/eps^2 + (2Lm-Lq)/eps
gE = sp.EulerGamma
for nm, ex, exp2, exp1 in [('H', sp.exp(e*Lq)*Asym, 1, Lq - gE), ('C', -sp.exp(e*Lm)*Asym, -1, -(Lm - gE)), ('S', sp.exp(e*(2*Lm-Lq))*Bsym, 1, 2*Lm-Lq-gE)]:
    s_ = sp.expand(sp.series(ex, e, 0, 1).removeO())
    check('(G) poles of %s: %s/eps^2 + (%s)/eps' % (nm, exp2, exp1), sp.simplify(s_.coeff(e, -2) - exp2) == 0 and sp.simplify(s_.coeff(e, -1) - exp1) == 0)
    print('      finite part of', nm, ':', sp.simplify(s_.coeff(e, 0)))

# ---------------------------------------------------------------- (H) exact remainder
mp.mp.dps = 50
def Phi1(t):
    rho = 2/(1-2*t+mp.sqrt(1-4*t))
    return (4*mp.polylog(2, -rho*t) + mp.log(rho*t)**2 + mp.pi**2/3)/mp.sqrt(1-4*t)
def remainder(m2v, Pv, Ppv):
    Qt2v = 2*Pv*Ppv; Q2v = (Qt2v+m2v)**2/Qt2v; t = m2v/Q2v
    I = Phi1(t)/Q2v
    S0 = (mp.log(Qt2v/m2v)**2 + mp.pi**2/3)/Qt2v
    return I - S0, Q2v, t
rv, Q2v, tv = remainder(mp.mpf('0.02'), mp.mpf('0.8'), mp.mpf('1.3'))
check('(H) int r at m2=0.02, P=0.8, P\'=1.3 = -0.0173434339581 (VF-REF-3)', abs(rv - mp.mpf('-0.0173434339581')) < 1e-12, mp.nstr(rv, 15))
# expansion check: int r = -4 m2/Q^4 + m^4/Q^6 (L^2 - 15 + pi^2/3) + O(m^6 L^2/Q^8)
for m2t in ['1e-3', '1e-4', '1e-5', '1e-6']:
    m2v = mp.mpf(m2t)
    rv, Q2v, tv = remainder(m2v, 1/mp.sqrt(2), 1/mp.sqrt(2))
    L = mp.log(Q2v/m2v)
    approx = -4*m2v/Q2v**2 + m2v**2/Q2v**3*(L**2 - 15 + mp.pi**2/3)
    resid = (rv - approx)/(m2v**3*L**2/Q2v**4)
    print('    m2=%s: int r = %s ; [int r - (NLP+NNLP)]/(m^6 L^2/Q^8) = %s' % (m2t, mp.nstr(rv, 12), mp.nstr(resid, 6)))
check('(H) NLP coefficient -4 (no logarithm at NLP): Q^4 int r/m2 -> -4',
      abs(remainder(mp.mpf('1e-12'), 1/mp.sqrt(2), 1/mp.sqrt(2))[0]*1/mp.mpf('1e-12') + 4) < 1e-9)
# rho t = m2/Qt2 exactly
tt = sp.symbols('t', positive=True)
for m2t in [sp.Rational(1, 10), sp.Rational(3, 100)]:
    Qt2s = 1; Q2s = (Qt2s+m2t)**2/Qt2s; ts = m2t/Q2s
    rhos = 2/(1-2*ts+sp.sqrt(1-4*ts))
    check('(H) rho t = m2/Qt2 exactly (m2=%s, Qt2=1)' % m2t, sp.simplify(rhos*ts - m2t) == 0)
# NLP expansion of I in Q units: Q^2 I = L^2 + pi^2/3 + t(2L^2 - 4L - 4 + 2pi^2/3) + t^2(6L^2-14L-11+2pi^2)
for tt_ in ['1e-4', '1e-6']:
    t_ = mp.mpf(tt_); L = mp.log(1/t_)
    lhs = Phi1(t_)
    rhs = L**2 + mp.pi**2/3 + t_*(2*L**2 - 4*L - 4 + 2*mp.pi**2/3) + t_**2*(6*L**2 - 14*L - 11 + 2*mp.pi**2)
    print('    t=%s: (Q^2 I - expansion)/(t^3 L^2) = %s' % (tt_, mp.nstr((lhs-rhs)/(t_**3*L**2), 6)))
check('(H) Q^2 I expansion through t^2 (VF-REF-2)', abs((Phi1(mp.mpf('1e-6')) - (mp.log(1e6)**2 + mp.pi**2/3 + mp.mpf('1e-6')*(2*mp.log(1e6)**2 - 4*mp.log(1e6) - 4 + 2*mp.pi**2/3) + mp.mpf('1e-12')*(6*mp.log(1e6)**2 - 14*mp.log(1e6) - 11 + 2*mp.pi**2)))) < 1e-13)

print('\n=== w10_triangle: %d PASS, %d FAIL ===' % (npass, nfail))
