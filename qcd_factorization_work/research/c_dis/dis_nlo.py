"""
dis_nlo.py -- O(alpha_s) DIS partonic structure functions in dimensional regularisation and the
MS-bar coefficient functions C_2^q, C_2^g, C_L^q, C_L^g.

Normalisation (binding conventions of the project; W^{mu nu} = (1/4pi) int e^{iqz} <[J,J]>):
   F_2(x,Q^2)/x = sum_q e_q^2 { q + qbar + (as/2pi) [ C_2^q (x) (q+qbar) + 2 C_2^g (x) g ] }
   F_L(x,Q^2)/x = sum_q e_q^2 (as/2pi) [ C_L^q (x) (q+qbar) + 2 C_L^g (x) g ]
with (f (x) g)(x) = int_x^1 dxi/xi f(x/xi) g(xi), PDFs and alpha_s in MS-bar at mu_F = mu_R = mu.
Partonic: F_a/x = sum_j (Fhat_a^j/z) (x) f_j  with Fhat computed from on-shell massless partons.

Dimensional regularisation: D = 4 - 2 eps,  bare coupling g0^2 = 4 pi as mu^(2 eps) e^(eps gE)/(4pi)^eps.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
import mpmath as mp
import dirac_d as dd
import real_me
from distributions import Dist, expand_singular, expand_regular, z, eps, clean

y = real_me.y
gE = sp.EulerGamma
CF, TF, CA = sp.symbols('C_F T_F C_A', positive=True)
Lmu = sp.Symbol('L_mu')          # ln(mu^2/Q^2)
z2 = sp.zeta(2)

# ------------------------------------------------------------------ helpers
def y_integrate(expr):
    """int_0^1 dy (y(1-y))^(-eps) expr(y), expr rational in y, exactly (analytic continuation)."""
    expr = sp.apart(sp.together(expr), y)
    res = 0
    for t in sp.Add.make_args(sp.expand(expr)):
        c, ydep = sp.factor(t).as_independent(y, as_Add=False)
        a = b = 0
        for base, ex in ydep.as_powers_dict().items():
            if base == y:
                a += ex
            elif sp.simplify(base - (y - 1)) == 0:
                b += ex
                c *= (-1) ** ex
            elif sp.simplify(base - (1 - y)) == 0:
                b += ex
            elif base == 1:
                pass
            else:
                raise ValueError('unexpected y-dependence: %s' % ydep)
        res += c * sp.gamma(a + 1 - eps) * sp.gamma(b + 1 - eps) / sp.gamma(a + b + 2 - 2 * eps)
    return res


def coeff_dict(series_dict):
    return {n: d.simplify() for n, d in series_dict.items()}


def report(name, ok):
    print(f'  [{"PASS" if ok else "FAIL"}] {name}')
    return ok


ALL_OK = True

# ------------------------------------------------------------------ 1. virtual form factor
def virtual_form_factor():
    """
    One-loop quark form factor F = 1 + F1 for gamma*(q) q(p) -> q(p'), q^2 = -Q^2 < 0, massless,
    Feynman gauge, computed from the trace projector  F1 = Tr[p' Lambda^mu p gamma_mu]/Tr[p' g^mu p g_mu].
    Lambda^mu = -i g0^2 C_F int d^Dl/(2pi)^D g^a (p'-l) g^mu (p-l) g_a / [l^2 (p-l)^2 (p'-l)^2].
    Returns F1 / [ (as/4pi) C_F (mu^2/Q^2)^eps ]  exactly in eps.
    """
    x1, x2, Ds, Q2 = sp.symbols('x1 x2 D_s Q2', positive=True)
    pp_ = Q2 / 2                                   # p.p' = Q^2/2
    # loop momentum l = L + x1 p + x2 p'  (Feynman parameters x1 for (p-l)^2, x2 for (p'-l)^2)
    dd.set_dots({('p', 'p'): 0, ('pp', 'pp'): 0, ('p', 'pp'): pp_})
    I, V = dd.I, dd.V
    num = dd.tr([V(pp=1), I('a'), V(pp=1 - x2, p=-x1, L=-1), I('m'),
                 V(p=1 - x1, pp=-x2, L=-1), I('a'), V(p=1), I('m')])
    den = dd.tr([V(pp=1), I('m'), V(p=1), I('m')])
    # symmetric integration: odd powers of L vanish; (L.u)(L.v) -> L^2 (u.v)/D
    Lp, Lpp, LL = sp.Symbol('L_p'), sp.Symbol('L_pp'), sp.Symbol('L_L')
    poly = sp.Poly(sp.expand(num), Lp, Lpp, LL)
    A = 0   # coefficient of L^2
    B = 0   # L-independent part
    dotv = {(Lp, Lp): 0, (Lpp, Lpp): 0, (Lp, Lpp): pp_}
    for (a1, a2, a3), c in poly.terms():
        deg = a1 + a2 + 2 * a3
        if deg == 0:
            B += c
        elif deg == 2:
            if a3 == 1:
                A += c
            elif a1 == 2:
                A += c * dotv[(Lp, Lp)] / dd.D
            elif a2 == 2:
                A += c * dotv[(Lpp, Lpp)] / dd.D
            else:
                A += c * dotv[(Lp, Lpp)] / dd.D
        elif deg % 2 == 1:
            continue
        else:
            raise ValueError('unexpected power of loop momentum')
    A = sp.expand(A.subs(dd.D, 4 - 2 * eps))
    B = sp.expand(B.subs(dd.D, 4 - 2 * eps))
    den = den.subs(dd.D, 4 - 2 * eps)
    # loop integrals (Peskin-Schroeder A.44-A.45), Delta = x1 x2 Q^2:
    #  int l^2/(l^2-Delta)^3 = + i/(4pi)^{D/2} (D/4) Gamma(eps) Delta^{-eps}
    #  int 1  /(l^2-Delta)^3 = - i/(4pi)^{D/2} (1/2) Gamma(1+eps) Delta^{-1-eps}
    # prefactor -i g0^2 C_F,  g0^2/(4pi)^{D/2} = (as/4pi) mu^{2eps} e^{eps gE};  Feynman measure 2 int_simplex
    # => F1/[(as/4pi) C_F mu^{2eps} e^{eps gE}] = 2 int [ A (D/4) G(eps) Delta^-eps - B (1/2) G(1+eps) Delta^{-1-eps} ]/den
    Dval = 4 - 2 * eps

    def simplex(expr, power):
        """int over x1,x2>=0, x1+x2<=1 of expr(x1,x2) * (x1 x2)^power  (Dirichlet integral)"""
        P = sp.Poly(sp.expand(expr), x1, x2)
        out = 0
        for (i1, i2), c in P.terms():
            a, b = i1 + power + 1, i2 + power + 1
            out += c * sp.gamma(a) * sp.gamma(b) / sp.gamma(a + b + 1)
        return out

    termA = simplex(A, -eps) * (Dval / 4) * sp.gamma(eps) * Q2 ** (-eps)
    termB = -simplex(B, -1 - eps) * sp.Rational(1, 2) * sp.gamma(1 + eps) * Q2 ** (-1 - eps)
    F1 = 2 * (termA + termB) / den
    # strip (mu^2/Q^2)^eps: the result must be proportional to Q2^(-eps)
    F1 = sp.simplify(F1 * Q2 ** eps) * sp.exp(eps * gE)
    return sp.simplify(F1)


print('=' * 78)
print('1. One-loop quark form factor (spacelike, massless, DR, Feynman gauge)')
Vff = virtual_form_factor()
K = sp.exp(eps * gE) * sp.gamma(1 + eps) * sp.gamma(1 - eps) ** 2 / sp.gamma(1 - 2 * eps)
Vexpected = K * (1 / eps - 2 / (eps ** 2 * (1 - 2 * eps)))
ALL_OK &= report('F1 = (as/4pi) CF (mu^2/Q^2)^eps e^{eps gE} G(1+e)G(1-e)^2/G(1-2e) [1/e - 2/(e^2(1-2e))]',
                 sp.simplify(sp.gammasimp(Vff / Vexpected) - 1) == 0 or
                 abs(sp.N((Vff - Vexpected).subs(eps, sp.Rational(-3, 10)), 30)) < 1e-25)
Vser = sp.expand(clean(sp.series(Vff, eps, 0, 2).removeO()))
print('   F1/[(as/4pi)CF(mu^2/Q^2)^eps] =', sp.simplify(Vser))
ALL_OK &= report('Laurent: -2/eps^2 - 3/eps - 8 + zeta2 + O(eps)',
                 sp.simplify(sp.expand(Vser).coeff(eps, -2) + 2) == 0 and
                 sp.simplify(sp.expand(Vser).coeff(eps, -1) + 3) == 0 and
                 sp.simplify(sp.expand(Vser).coeff(eps, 0) - (-8 + z2)) == 0)

# ------------------------------------------------------------------ 2. real emission, exact in eps
print('=' * 78)
print('2. Real emission, D-dim phase space, exact y-integration')
Tq_g, Tq_pp = real_me.quark_channel()
Tg_g, Tg_pp = real_me.gluon_channel()
pref_ps = sp.exp(eps * gE) / sp.gamma(1 - eps)       # from (4pi/s)^eps/Gamma(1-eps) with MS-bar g0^2
# quark channel: Fhat_a/(z e_q^2) = (as/2pi) C_F (mu^2/Q^2)^eps R_a^q ;  (mu^2/s)^eps = (mu^2/Q^2)^eps (z/(1-z))^eps
proj2_q = (Tq_g + (3 - 2 * eps) * 4 * z ** 2 * Tq_pp) / (1 - eps)
projL_q = 8 * z ** 2 * Tq_pp
Y2q = y_integrate(proj2_q)
YLq = y_integrate(projL_q)
# R = (1/8) (z/(1-z))^eps pref_ps * Y ;  write R = (1-z)^(-1-eps) G
G2q = sp.simplify(sp.Rational(1, 8) * z ** eps * pref_ps * (1 - z) * Y2q)
RLq = sp.simplify(sp.Rational(1, 8) * (z / (1 - z)) ** eps * pref_ps * YLq)
print('   G_2^q(z,eps) = (1-z)^(1+eps) R_2^q =', sp.simplify(G2q / (z ** eps * pref_ps)), ' x z^eps e^{eps gE}/Gamma(1-eps)')
print('   R_L^q(z,eps) =', sp.simplify(RLq / ((z / (1 - z)) ** eps * pref_ps)), ' x (z/(1-z))^eps e^{eps gE}/Gamma(1-eps)')
# gluon channel: extra 1/(D-2) = 1/(2(1-eps)) polarisation average -> overall 1/(8(1-eps))
proj2_g = (Tg_g + (3 - 2 * eps) * 4 * z ** 2 * Tg_pp) / (1 - eps)
projL_g = 8 * z ** 2 * Tg_pp
Y2g = y_integrate(proj2_g)
YLg = y_integrate(projL_g)
R2g = sp.simplify(sp.Rational(1, 8) / (1 - eps) * (z / (1 - z)) ** eps * pref_ps * Y2g)
RLg = sp.simplify(sp.Rational(1, 8) / (1 - eps) * (z / (1 - z)) ** eps * pref_ps * YLg)
print('   R_2^g(z,eps) =', sp.simplify(R2g / ((z / (1 - z)) ** eps * pref_ps)), ' x (z/(1-z))^eps e^{eps gE}/Gamma(1-eps)')
print('   R_L^g(z,eps) =', sp.simplify(RLg / ((z / (1 - z)) ** eps * pref_ps)), ' x (z/(1-z))^eps e^{eps gE}/Gamma(1-eps)')

# ------------------------------------------------------------------ 3. Laurent expansion as distributions
print('=' * 78)
print('3. Laurent expansion in eps (distributions in z), mu = Q')
real2q = expand_singular(G2q, order_max=0)
realLq = expand_regular(RLq, order_max=0)
real2g = expand_regular(R2g, order_max=0)
realLg = expand_regular(RLg, order_max=0)
virt = sp.expand(clean(sp.series(Vff, eps, 0, 1).removeO()))
# total quark F2 (coefficient of (as/2pi) C_F): R + V delta;  note 2 Re F1 = (as/2pi) CF (...) V
tot2q = {n: (real2q[n] + Dist(delta=virt.coeff(eps, n))).simplify() for n in range(-3, 1)}
for n in (-2, -1, 0):
    print(f'   F2^q, eps^{n}:  ', tot2q[n].latex())

# splitting functions (DGLAP normalisation  d f/d ln mu^2 = (as/2pi) P (x) f)
Pqq_over_CF = Dist(delta=sp.Rational(3, 2), plus={0: 2}, reg=-(1 + z))        # [(1+z^2)/(1-z)]_+
Pqg_over_TF = Dist(reg=z ** 2 + (1 - z) ** 2)

ALL_OK &= report('no 1/eps^2 pole in F2^q (soft-collinear cancellation real+virtual)', tot2q[-2].is_zero())
ALL_OK &= report('1/eps pole of F2^q = -(1/eps) P_qq(z)  [collinear, incl. (3/2) delta from virtual]',
                 (tot2q[-1] + Pqq_over_CF).is_zero())
ALL_OK &= report('F_L^q finite (no poles)', all(realLq[n].is_zero() for n in (-3, -2, -1)))
ALL_OK &= report('1/eps pole of F2^g = -(1/eps) 2 P_qg(z)  [q and qbar collinear to the gluon]',
                 (real2g[-1].scale(TF) + Pqg_over_TF.scale(2 * TF)).is_zero() and real2g[-2].is_zero())
ALL_OK &= report('F_L^g finite (no poles)', all(realLg[n].is_zero() for n in (-3, -2, -1)))

# ------------------------------------------------------------------ 4. MS-bar coefficient functions
print('=' * 78)
print('4. MS-bar coefficient functions (mu_F = mu_R = Q)')
# partonic PDFs in MS-bar, DR:  f_{i/j}(z) = delta_ij delta(1-z) - (as/2pi)(1/eps) P_ij(z) + O(as^2)
C2q = (tot2q[0]).scale(CF).simplify()
CLq = realLq[0].scale(CF).simplify()
C2g = real2g[0].scale(TF / 2).simplify()       # per quark (or antiquark): Fhat_2^g = e_q^2 (as/2pi) 2 C_2^g
CLg = realLg[0].scale(TF / 2).simplify()
print('   C_2^q =', C2q.latex())
print('   C_L^q =', CLq.latex())
print('   C_2^g =', C2g.latex())
print('   C_L^g =', CLg.latex())

# literature (BBDM 1978 / Furmanski-Petronzio 1982 / ESW (4.80)ff), canonical form
lit_C2q = Dist(delta=-(sp.Rational(9, 2) + sp.pi ** 2 / 3), plus={1: 2, 0: -sp.Rational(3, 2)},
               reg=-(1 + z) * sp.log(1 - z) - (1 + z ** 2) / (1 - z) * sp.log(z) + 3 + 2 * z).scale(CF)
lit_C2g = Dist(reg=(z ** 2 + (1 - z) ** 2) * sp.log((1 - z) / z) - 8 * z ** 2 + 8 * z - 1).scale(TF)
lit_CLq = Dist(reg=2 * z).scale(CF)
lit_CLg = Dist(reg=4 * z * (1 - z)).scale(TF)
ALL_OK &= report('C_2^q = C_F[2(ln(1-z)/(1-z))_+ - 3/2 (1/(1-z))_+ - (1+z)ln(1-z) - (1+z^2)/(1-z) ln z + 3 + 2z - (9/2+pi^2/3) delta(1-z)]',
                 (C2q - lit_C2q).is_zero())
ALL_OK &= report('C_2^g = T_F[(z^2+(1-z)^2) ln((1-z)/z) - 8z^2 + 8z - 1]', (C2g - lit_C2g).is_zero())
ALL_OK &= report('C_L^q = 2 C_F z', (CLq - lit_CLq).is_zero())
ALL_OK &= report('C_L^g = 4 T_F z(1-z)', (CLg - lit_CLg).is_zero())

# ------------------------------------------------------------------ 5. mu dependence from the D-dim result
print('=' * 78)
print('5. General mu: (mu^2/Q^2)^eps factor -> log terms')
# Fhat/(z e_q^2) = delta + (as/2pi) (mu^2/Q^2)^eps [ -(1/eps) P + C + O(eps) ]  =>  finite part after MS-bar
# subtraction  C(z) + ln(Q^2/mu^2) P(z).
def with_mu(series):
    out = {}
    fac = sp.series(sp.exp(eps * Lmu), eps, 0, 4).removeO()
    for n in range(-3, 1):
        acc = Dist()
        for m in range(-3, 1):
            c = sp.expand(fac).coeff(eps, n - m)
            if c != 0:
                acc = acc + series[m].scale(c)
        out[n] = acc.simplify()
    return out
tot2q_mu = with_mu(tot2q)
C2q_mu = tot2q_mu[0].scale(CF).simplify()
ALL_OK &= report('C_2^q(z, mu) = C_2^q(z) + ln(Q^2/mu^2) P_qq(z)',
                 (C2q_mu - C2q - Pqq_over_CF.scale(-Lmu * CF)).is_zero())
real2g_mu = with_mu(real2g)
C2g_mu = real2g_mu[0].scale(TF / 2).simplify()
ALL_OK &= report('C_2^g(z, mu) = C_2^g(z) + ln(Q^2/mu^2) P_qg(z)',
                 (C2g_mu - C2g - Pqg_over_TF.scale(-Lmu * TF)).is_zero())

print('=' * 78)
print('OVERALL:', 'ALL CHECKS PASS' if ALL_OK else 'SOME CHECKS FAILED')

# export for other scripts
RESULTS = dict(Vff=Vff, G2q=G2q, RLq=RLq, R2g=R2g, RLg=RLg, C2q=C2q, CLq=CLq, C2g=C2g, CLg=CLg,
               Pqq=Pqq_over_CF.scale(CF), Pqg=Pqg_over_TF.scale(TF))
