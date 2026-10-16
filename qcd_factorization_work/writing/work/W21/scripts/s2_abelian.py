r"""
s2_abelian.py  (writer W21, Ch18 `break`): independent re-derivation of the abelian eikonal algebra behind
thm:break-tmd and ex:break-c07, in the conventions of the book.

  A1  eikonal factors of the extra gluon (momentum l flowing from the spectator of H1 into the line) in
      Catani-Seymour (all-outgoing) charges: outgoing line  g e_j/(l^+ - i0), incoming line g e_j/(l^+ + i0);
      CQ/C07 charges e_a = g1, e_b = g2, e_c = -g1, e_d = -g2  ->  E(l) of C07 eq. (2);
      E = -i pi (2 g2 + g1) delta - g1 PV  (VF-GLA-7); comparison with the future (SIDIS-type) and past
      (DY-type) Wilson lines of charge g1.
  A2  two gluons on opposite sides of the cut: E(l1) E(l2)^*; anomaly 4 pi^2 g2 (g2 + g1) delta delta;
      same side: E(l1) E(l2) (generalized exponentiation), the anomaly with the opposite sign.
  A3  F(k) closed form vs Feynman-parameter form; G(k) two-parameter form vs b-space (Hankel) form.
  A4  b-space forms F~ = (2pi)^2 K0(mg b) K0(mq b), G~ = (2pi)^3 K0(mg b)^2 K0(mq b) (numerical Hankel transforms).
  A5  Parseval: int d^2k F^2 = int d^2k G/(k^2+mq^2) = (2pi)^3 int b K0g^2 K0q^2 db  -> int (I1+I2) = 0.
  A6  Cauchy-Schwarz: F(0)^2 < G(0)/mq^2 (measure d mu = d^2b/(2pi)^2 2pi K0(mq b), int d mu = 1/mq^2).
  A7  numbers: (I1+I2)/N at k = 0, 0.3, 0.8, 1.5, 3, 6 for (mg, mq) = (0.5, 1); sign change.
  A8  mass dimensions: corrected I ~ M^{-2} with [N] = M^2 (scalar trilinear couplings of dimension M);
      the printed extra factor prod_j (k^2+mq^2) changes the dimension by M^4.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
from scipy import integrate, special

RES = []
def check(name, ok, detail=''):
    RES.append((name, bool(ok)))
    print(('PASS' if ok else 'FAIL') + '  ' + name + (('   [' + detail + ']') if detail else ''))

# ------------------------------------------------------------------------------------------- A1
print('=== A1 one-gluon eikonal sum ===')
# Represent a distribution in one variable x = l^+ as  c_P * PV(1/x) + c_D * delta(x).
#   1/(x + i0) = PV - i pi delta ;  1/(x - i0) = PV + i pi delta ;  1/(-x + i0) = -PV - i pi delta.
g1, g2, g = sp.symbols('g1 g2 g', real=True)
PI = sp.pi; I = sp.I
def inv_plus(c=1):   # c/(x + i0)
    return (c, -I * PI * c)
def inv_minus(c=1):  # c/(x - i0)
    return (c, I * PI * c)
def add(*ds):
    return (sp.simplify(sum(d[0] for d in ds)), sp.simplify(sum(d[1] for d in ds)))
# CS charges (incoming partons counted as outgoing antiparticles): a = phi1 in (+g1), b = phi2 in (+g2),
# c = phi1 out (-g1), d = phi2 out (-g2); colour (charge) conservation:
ea, eb, ec, ed = g1, g2, -g1, -g2
check('A1 charge conservation e_a+e_b+e_c+e_d = 0', sp.simplify(ea + eb + ec + ed) == 0)
# eikonal factors: outgoing j: e_j/(l^+ - i0) ; incoming j: e_j/(l^+ + i0)  (overall factor g dropped)
E = add(inv_plus(eb), inv_minus(ed), inv_minus(ec))
# C07 eq.(2): g2/(l+i0) + g2/(-l+i0) + g1/(-l+i0)
E_C07 = add(inv_plus(g2), (-g2, -I * PI * g2), (-g1, -I * PI * g1))
check('A1 E(l) from the CS-charge rule equals C07 eq. (2)', sp.simplify(E[0] - E_C07[0]) == 0 and sp.simplify(E[1] - E_C07[1]) == 0,
      'PV coeff %s, delta coeff %s' % (E[0], E[1]))
check('A1 E = -g1 PV - i pi (2 g2 + g1) delta  (VF-GLA-7)', sp.simplify(E[0] + g1) == 0 and sp.simplify(E[1] + I * PI * (2 * g2 + g1)) == 0)
# standard Wilson lines of charge g1 for hadron 1 (only the own line c attached): future pointing (SIDIS)
Ef = inv_minus(ec)            # = g1/(-l+i0) = -g1 PV - i pi g1 delta
Ep = (-g1, I * PI * g1)       # past pointing (DY):  g1/(-l - i0) = -g1 PV + i pi g1 delta
check('A1 T-even (PV) part of E equals the standard future/past line value', sp.simplify(E[0] - Ef[0]) == 0 and sp.simplify(E[0] - Ep[0]) == 0)
ratio_f = sp.simplify(E[1] / Ef[1]); ratio_p = sp.simplify(E[1] / Ep[1])
check('A1 T-odd part: E/future = (g1+2 g2)/g1, E/past = -(g1+2 g2)/g1; equal to +-1 only for g2=0 or g2=-g1',
      sp.simplify(ratio_f - (g1 + 2 * g2) / g1) == 0 and sp.simplify(ratio_p + (g1 + 2 * g2) / g1) == 0
      and set(sp.solve(sp.Eq(ratio_f ** 2, 1), g2)) == {0, -g1}, '%s ; %s' % (ratio_f, ratio_p))

# ------------------------------------------------------------------------------------------- A2
print('=== A2 two gluons (Collins 2007) ===')
# product of distributions in independent variables l1, l2: represent as dict over (P|D, P|D)
def prod(d1, d2, conj2=False):
    a = d2 if not conj2 else (sp.conjugate(d2[0]), sp.conjugate(d2[1]))
    return {('P', 'P'): sp.expand(d1[0] * a[0]), ('P', 'D'): sp.expand(d1[0] * a[1]),
            ('D', 'P'): sp.expand(d1[1] * a[0]), ('D', 'D'): sp.expand(d1[1] * a[1])}
opp = prod(E, E, conj2=True)          # gluons on opposite sides of the cut
std_opp = prod(Ef, Ef, conj2=True)
anom = sp.factor(opp[('D', 'D')] - std_opp[('D', 'D')])
check('A2 opposite sides: delta(l1+)delta(l2+) anomaly = 4 pi^2 g2 (g2 + g1)  (C07 eq. (4); VF-GLA-7)',
      sp.simplify(anom - 4 * PI ** 2 * g2 * (g2 + g1)) == 0, str(anom))
check('A2 opposite sides: PV PV part = g1^2 (standard)', sp.simplify(opp[('P', 'P')] - g1 ** 2) == 0)
check('A2 opposite sides: delta PV cross terms i pi g1 (2g2+g1)[delta1 PV2 - PV1 delta2] (C07 eq. (3))',
      sp.simplify(opp[('D', 'P')] - I * PI * g1 * (2 * g2 + g1)) == 0 and sp.simplify(opp[('P', 'D')] + I * PI * g1 * (2 * g2 + g1)) == 0)
same = prod(E, E)
std_same = prod(Ef, Ef)
anom_same = sp.factor(same[('D', 'D')] - std_same[('D', 'D')])
check('A2 same side: anomaly = -4 pi^2 g2 (g2+g1) (minus the opposite-side one)', sp.simplify(anom_same + 4 * PI ** 2 * g2 * (g2 + g1)) == 0, str(anom_same))
# C07 eq. (7): g2^2 terms of the same-side graphs = (-2 pi i g2 delta)^2 = -4 pi^2 g2^2 delta delta
g2sq = sp.Poly(same[('D', 'D')], g2).coeff_monomial(g2 ** 2)
check('A2 same side: g2^2 delta-delta coefficient = -4 pi^2 (C07 eq. (7))', sp.simplify(g2sq + 4 * PI ** 2) == 0)
check('A2 abelian anomaly vanishes iff g2 = 0 or g2 = -g1', set(sp.solve(anom, g2)) == {0, -g1})

# ------------------------------------------------------------------------------------------- A3/A4
print('=== A3/A4 model functions F, G ===')
def F_closed(k, mg, mq):
    # (pi/sqrt L) ln((s+sqrt L)/(s-sqrt L)) = (2 pi/sqrt L) ln((s+sqrt L)/(2 mg mq)), since s^2 - L = 4 mg^2 mq^2;
    # the second form is free of the cancellation in s - sqrt L at large k; at L -> 0 use the series 2pi/s (1+L/(3s^2)).
    s = k * k + mg * mg + mq * mq; Lam = s * s - 4 * mg * mg * mq * mq
    if Lam < 1e-10 * s * s:
        return 2 * np.pi / s * (1 + Lam / (3 * s * s) + Lam ** 2 / (5 * s ** 4))
    r = np.sqrt(Lam)
    return 2 * np.pi / r * np.log((s + r) / (2 * mg * mq))
# symbolic check of the identity between the two closed forms
_s, _r, _a = sp.symbols('s r a', positive=True)
check('A0 (pi/r) ln((s+r)/(s-r)) = (2pi/r) ln((s+r)/(2 mg mq)) when s^2 - r^2 = 4 mg^2 mq^2',
      sp.simplify(sp.expand_log(sp.log((_s + _r) / (_s - _r)) - 2 * sp.log((_s + _r) / _a), force=True)
                  .subs(_s - _r, _a ** 2 / (_s + _r))) == 0 or
      abs(float((sp.log((_s + _r) / (_s - _r)) - 2 * sp.log((_s + _r) / sp.sqrt(_s ** 2 - _r ** 2))).subs({_s: 2.7, _r: 1.3}))) < 1e-14)
def F_feyn(k, mg, mq):
    return np.pi * integrate.quad(lambda x: 1.0 / (x * (1 - x) * k * k + x * mg * mg + (1 - x) * mq * mq), 0, 1, epsabs=0, epsrel=1e-13)[0]
def G_feyn(k, mg, mq):
    f = lambda y, x: 1.0 / (x * (1 - x) * (y * (1 - y) * k * k + (1 - y) * mg * mg) + y * (x * mq * mq + (1 - x) * mg * mg))
    return np.pi ** 2 * integrate.dblquad(f, 0, 1, 0, 1, epsabs=0, epsrel=1e-11)[0]
def hankel(fb, k):
    # 2D Fourier transform of a radial function fb(b): int d^2b e^{-ik.b} fb(b)/(2pi)^2 ... here return
    # int d^2b/(2pi)^2 e^{i k.b} fb(b) = (1/2pi) int_0^inf b J0(kb) fb(b) db
    if k == 0:
        return integrate.quad(lambda b: b * fb(b), 0, np.inf, limit=400)[0] / (2 * np.pi)
    val = 0.0
    zeros = special.jn_zeros(0, 4000) / k
    edges = np.concatenate(([0.0], zeros))
    terms = []
    for a, bb in zip(edges[:-1], edges[1:]):
        terms.append(integrate.quad(lambda b: b * special.j0(k * b) * fb(b), a, bb, limit=200)[0])
        if len(terms) > 60 and abs(terms[-1]) < 1e-16:
            break
    return sum(terms) / (2 * np.pi)
for (mg, mq) in [(0.5, 1.0), (1.0, 1.0), (0.2, 0.7)]:
    ks = [0.0, 0.3, 0.8, 1.5, 3.0]
    dF = max(abs(F_closed(k, mg, mq) / F_feyn(k, mg, mq) - 1) for k in ks)
    check('A3 (mg,mq)=(%.1f,%.1f): F closed form = Feynman-parameter form' % (mg, mq), dF < 1e-11, 'max rel %.1e' % dF)
    Ft = lambda b: (2 * np.pi) ** 2 * special.k0(mg * b) * special.k0(mq * b)
    Gt = lambda b: (2 * np.pi) ** 3 * special.k0(mg * b) ** 2 * special.k0(mq * b)
    dFh = max(abs(hankel(Ft, k) / F_closed(k, mg, mq) - 1) for k in [0.0, 0.8, 1.5])
    dGh = max(abs(hankel(Gt, k) / G_feyn(k, mg, mq) - 1) for k in [0.0, 0.8, 1.5])
    check('A4 (mg,mq)=(%.1f,%.1f): F = FT of (2pi)^2 K0g K0q ; G = FT of (2pi)^3 K0g^2 K0q' % (mg, mq),
          dFh < 1e-7 and dGh < 1e-7, 'max rel F %.1e, G %.1e' % (dFh, dGh))

# ------------------------------------------------------------------------------------------- A5/A6/A7
print('=== A5-A7 Parseval, Cauchy-Schwarz, numbers ===')
for (mg, mq) in [(0.5, 1.0), (1.0, 1.0), (0.2, 0.7)]:
    bint = integrate.quad(lambda b: b * special.k0(mg * b) ** 2 * special.k0(mq * b) ** 2, 0, np.inf, limit=400)[0]
    bspace = (2 * np.pi) ** 3 * bint
    kF2 = 2 * np.pi * integrate.quad(lambda k: k * F_closed(k, mg, mq) ** 2, 0, np.inf, limit=400)[0]
    # G on a grid via the 1D x-integrated form would be slow; use G(k) from the dblquad on a log grid + spline
    kg = np.concatenate(([0.0], np.logspace(-3, 3, 70)))
    Gv = np.array([G_feyn(k, mg, mq) for k in kg])
    from scipy.interpolate import PchipInterpolator
    Gi = PchipInterpolator(kg, Gv)
    kmax = kg[-1]
    kG = 2 * np.pi * integrate.quad(lambda k: k * Gi(k) / (k * k + mq * mq), 0, kmax, limit=800, points=list(kg[1:20]))[0]
    # tail beyond kmax: G ~ (2pi^2/k^2) ln-type decay; estimate with the last value scaling ~ 1/k^2 log
    tail = 2 * np.pi * Gv[-1] * kmax ** 2 * integrate.quad(lambda k: k / (k * k) / (k * k + mq * mq), kmax, np.inf)[0]
    kG += tail
    check('A5 (mg,mq)=(%.1f,%.1f): int d^2k F^2 = (2pi)^3 int b K0g^2K0q^2 = int d^2k G/(k^2+mq^2)' % (mg, mq),
          abs(kF2 / bspace - 1) < 1e-8 and abs(kG / bspace - 1) < 2e-4, 'F2 %.8f, G-part %.6f, b-space %.8f' % (kF2, kG, bspace))
    # Cauchy-Schwarz
    mu_tot = integrate.quad(lambda b: b * special.k0(mq * b), 0, np.inf)[0]          # = int d mu = 1/mq^2
    F0 = integrate.quad(lambda b: b * special.k0(mq * b) * 2 * np.pi * special.k0(mg * b), 0, np.inf, limit=400)[0]
    G0 = integrate.quad(lambda b: b * special.k0(mq * b) * (2 * np.pi * special.k0(mg * b)) ** 2, 0, np.inf, limit=400)[0]
    check('A6 (mg,mq)=(%.1f,%.1f): int dmu = 1/mq^2; F(0), G(0) as mu-moments; F(0)^2 < G(0)/mq^2' % (mg, mq),
          abs(mu_tot - 1 / mq ** 2) < 1e-10 and abs(F0 / F_closed(0, mg, mq) - 1) < 1e-9 and abs(G0 / G_feyn(0, mg, mq) - 1) < 1e-8
          and F0 ** 2 < G0 / mq ** 2, 'F0^2=%.6f  G0/mq^2=%.6f  (I1+I2)(0)/N=%.4f' % (F0 ** 2, G0 / mq ** 2, F0 ** 2 - G0 / mq ** 2))
mg, mq = 0.5, 1.0
vals = []
for k in [0.0, 0.3, 0.8, 1.5, 3.0, 6.0]:
    vals.append(F_closed(k, mg, mq) ** 2 - G_feyn(k, mg, mq) / (k * k + mq * mq))
print('      (I1+I2)/N at k = 0, 0.3, 0.8, 1.5, 3, 6 :', ['%.4g' % v for v in vals])
check('A7 (I1+I2)/N = -21.0, -17.7, -7.19, -0.70, +0.38, +0.089 (changes sign)',
      all(abs(a - b) / abs(b) < 3e-3 for a, b in zip(vals, [-21.01, -17.73, -7.19, -0.70, 0.377, 0.0890])) and vals[0] < 0 < vals[-1])

# ------------------------------------------------------------------------------------------- A8
print('=== A8 mass dimensions ===')
# [k] = M; [F] = int d^2l/(M^2 M^2) = M^-2; [G] = M^4/M^6 = M^-2; G/(k^2+m^2) ~ M^-4;  F^2 ~ M^-4.
# scalar model: trilinear scalar coupling lambda ~ M, scalar QED-like coupling g_i dimensionless -> [N] = M^2,
# I1, I2 ~ M^-2 (a TMD density).  An extra factor prod_{j=1,2}(k^2+mq^2) multiplies by M^4.
dimF, dimG, dimN = -2, -2, 2
check('A8 [I1] = [N] + 2[F] = -2 = [I2] = [N] + [G] - 2 ; printed extra factor shifts the dimension by +4',
      dimN + 2 * dimF == -2 and dimN + dimG - 2 == -2 and dimN + 2 * dimF + 4 == 2)

print('\nSUMMARY: %d/%d PASS' % (sum(1 for _, o in RES if o), len(RES)))
