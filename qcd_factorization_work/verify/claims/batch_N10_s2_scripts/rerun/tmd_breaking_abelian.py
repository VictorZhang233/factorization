"""
tmd_breaking_abelian.py  --  Part (2) of research/c_glauber: eikonal algebra of the Collins-Qiu (2007) and
Collins (2007) counterexamples to standard TMD factorization, the Rogers-Mulders (2010) eikonal sums, and
the anomaly functions I1, I2 (non-cancellation point-by-point in k_T, cancellation after the k_T integral).

Sources (texts verified; equation numbers refer to these arXiv versions):
  CQ   = Collins & Qiu, PRD 75 (2007) 114014, arXiv:0705.2141v2, eqs.(4.1)-(4.3);
  C07  = Collins, arXiv:0708.4410v1 (not published in a journal), eqs.(2)-(11);
  RM   = Rogers & Mulders, PRD 81 (2010) 094006, arXiv:1001.2977v2, eqs.(25)-(28), (35), (36).

A1  C07 eq.(2) (= CQ eqs.(4.1)-(4.3) up to an overall sign convention):
      E(l) = g2/(l+i0) + g2/(-l+i0) + g1/(-l+i0) = -2 pi i g2 delta(l) + g1/(-l+i0)
           = -i pi (2 g2 + g1) delta(l) - g1 PV(1/l)              (test-function check)
    the g1 part is the future-pointing Wilson line of the standard (SIDIS-like) TMD of hadron 1.
A2  building blocks 1/(-l+i0)+1/(l+i0) = -2 pi i delta(l), 1/(-l-i0)+1/(l-i0) = +2 pi i delta(l); hence
    C07 eq.(7) = -(2pi)^2 g2^2 delta delta ; RM eqs.(25)/(26)/(35)/(36) = +-4 pi^2 delta delta (symbolic).
A3  C07 eq.(4): anomaly of E(l1)E(l2)^* relative to the standard (charge g1) Wilson line: 4 pi^2 g2(g2+g1)
    delta(l1)delta(l2); C07 eq.(8): the g1 g2 terms of the same-side graphs = E(l1)E(l2)-type product.
A4  C07 eqs.(10),(11) / RM eqs.(27),(28) (scalar model, massive abelian gluon mg, quark mass mq):
      I1(kT) = N F(kT)^2,  I2(kT) = -N G(kT)/(kT^2+mq^2),   N = lambda^2 g1^2 g2(g2+g1) x(1-x)/(256 pi^7),
      F(k) = int d^2l [(l^2+mg^2)((k-l)^2+mq^2)]^-1 = pi int_0^1 dx [x(1-x)k^2 + x mq^2 + (1-x) mg^2]^-1,
      G(k) = int d^2l1 d^2l2 [(l1^2+mg^2)(l2^2+mg^2)((k-l1-l2)^2+mq^2)]^-1
           = pi^2 int_0^1 dx int_0^1 dy [x(1-x)(y(1-y)k^2 + (1-y)mg^2) + y(x mq^2 + (1-x) mg^2)]^-1  (derived here).
    Checks: Feynman forms = Hankel (b-space) forms; int d^2k (I1+I2) = 0 exactly (Parseval);
    I1(0)+I2(0) < 0 (C07 states it 'can be proved analytically'; proof here by Cauchy-Schwarz);
    I1+I2 != 0 pointwise and changes sign.
    NB: as printed in arXiv:0708.4410v1, eq.(10) carries an extra factor prod_j (kT^2+mq^2) in the numerator; this is
    inconsistent with the first line of the same equation, with eq.(11) (mass dimension) and with the stated
    cancellation; the form without it (cf. RM eq.(27), massless-gluon analogue) is the one verified here.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
import warnings
warnings.simplefilter('ignore')
from scipy import integrate, special

RESULTS = []
def check(name, ok, detail=''):
    RESULTS.append((name, bool(ok)))
    print(('PASS' if ok else 'FAIL') + '  ' + name + ('   [' + detail + ']' if detail else ''))

def dist_apply(kernel, phi, eps, L=40.0):
    pts = [-L, -1.0, -0.1, -0.01, -1e-3, 0.0, 1e-3, 0.01, 0.1, 1.0, L]
    tot = 0j
    for a, b in zip(pts[:-1], pts[1:]):
        tot += integrate.quad(lambda t: (kernel(t, eps)*phi(t)).real, a, b, limit=2000)[0]
        tot += 1j*integrate.quad(lambda t: (kernel(t, eps)*phi(t)).imag, a, b, limit=2000)[0]
    return tot
phi = lambda t: np.exp(-(t - 0.25)**2)*(1.0 + 0.4*t + 0.1*t**2)
def PV(phi, L=40.0):
    return integrate.quad(lambda t: (phi(t) - phi(-t))/t, 0, L, limit=2000)[0]

print('=== A1: one-gluon eikonal sum (C07 eq.2, CQ eqs.4.1-4.3) ===')
g1, g2 = 0.8, -1.3
E = lambda l, e: g2/(l + 1j*e) + g2/(-l + 1j*e) + g1/(-l + 1j*e)
for eps in [1e-3, 1e-4]:
    lhs = dist_apply(E, phi, eps)
    rhs = -1j*np.pi*(2*g2 + g1)*phi(0) - g1*PV(phi)
    print('   eps=%g: <E,phi> = %s ; -i pi(2g2+g1)phi(0) - g1 PV = %s' % (eps, lhs, rhs))
check('A1 E(l) = -i pi (2 g2 + g1) delta(l) - g1 PV(1/l): T-odd (Sivers) coefficient 2g2+g1, not g1', abs(lhs - rhs) < 5e-3*abs(rhs))
check('A1b the g2 principal parts cancel between the incoming (k2) and outgoing (k4) lines; only the g1 future-pointing line survives in the real part',
      abs(dist_apply(lambda l, e: g2/(l + 1j*e) + g2/(-l + 1j*e), phi, 1e-4).real) < 5e-3)

print('\n=== A2: eikonal building blocks (C07 eq.7; RM eqs.25,26,35,36) ===')
v1 = dist_apply(lambda l, e: 1/(-l + 1j*e) + 1/(l + 1j*e), phi, 1e-4)
v2 = dist_apply(lambda l, e: 1/(-l - 1j*e) + 1/(l - 1j*e), phi, 1e-4)
check('A2a 1/(-l+i0)+1/(l+i0) = -2 pi i delta(l)', abs(v1 + 2j*np.pi*phi(0)) < 3e-3, 'num=%s' % v1)
check('A2b 1/(-l-i0)+1/(l-i0) = +2 pi i delta(l)', abs(v2 - 2j*np.pi*phi(0)) < 3e-3, 'num=%s' % v2)
l1, l2, e = sp.symbols('l1 l2 epsilon', real=True)
c7 = (1/(l1 + sp.I*e)/(l2 + sp.I*e) + 1/(l1 + sp.I*e)/(-l2 + sp.I*e) + 1/(-l1 + sp.I*e)/(l2 + sp.I*e) + 1/(-l1 + sp.I*e)/(-l2 + sp.I*e))
fac = (1/(l1 + sp.I*e) + 1/(-l1 + sp.I*e))*(1/(l2 + sp.I*e) + 1/(-l2 + sp.I*e))
check('A2c C07 eq.(7): the four g2^2 eikonal products factorize into (-2 pi i delta)^2 = -4 pi^2 delta delta', sp.simplify(c7 - fac) == 0)
rm35 = (1/(-l1 + sp.I*e)/(-l2 + sp.I*e) + 1/(l1 + sp.I*e)/(-l2 + sp.I*e) + 1/(-l1 + sp.I*e)/(l2 + sp.I*e) + 1/(l1 + sp.I*e)/(l2 + sp.I*e))
check('A2d RM eq.(35) (same side of the cut) = (-2 pi i delta)(-2 pi i delta) = -4 pi^2 delta(l1+) delta(l2-)',
      sp.simplify(rm35 - (1/(-l1 + sp.I*e) + 1/(l1 + sp.I*e))*(1/(-l2 + sp.I*e) + 1/(l2 + sp.I*e))) == 0)
rm36 = (1/(-l1 - sp.I*e)/(-l2 + sp.I*e) + 1/(l1 - sp.I*e)/(-l2 + sp.I*e) + 1/(-l1 - sp.I*e)/(l2 + sp.I*e) + 1/(l1 - sp.I*e)/(l2 + sp.I*e))
check('A2e RM eq.(36) (opposite sides) = (+2 pi i delta)(-2 pi i delta) = +4 pi^2 delta delta',
      sp.simplify(rm36 - (1/(-l1 - sp.I*e) + 1/(l1 - sp.I*e))*(1/(-l2 + sp.I*e) + 1/(l2 + sp.I*e))) == 0)
# C07 eq.(5): two gluons on the same line, abelian: eikonal identity
g = sp.symbols('g')
lhs5 = g**2/((-l1 - l2 + sp.I*e)*(-l1 + sp.I*e)) + g**2/((-l1 - l2 + sp.I*e)*(-l2 + sp.I*e))
rhs5 = g**2/((-l1 + sp.I*e)*(-l2 + sp.I*e))
check('A2f C07 eq.(5): abelian eikonal identity for two gluons on one line (algebraic; exact when the i0 of the sum denominator is the sum of the two i0)',
      sp.simplify(lhs5.subs(e, 0) - rhs5.subs(e, 0)) == 0)

print('\n=== A3: anomaly coefficients (C07 eqs.4 and 8) ===')
G1, G2, d1, d2, P1, P2 = sp.symbols('g1 g2 delta1 delta2 PV1 PV2', real=True)
Eamp = -sp.I*sp.pi*(2*G2 + G1)*d1 - G1*P1
Econ = sp.conjugate(-sp.I*sp.pi*(2*G2 + G1)*d2 - G1*P2)
Estd_amp = -sp.I*sp.pi*G1*d1 - G1*P1
Estd_con = sp.conjugate(-sp.I*sp.pi*G1*d2 - G1*P2)
prod = sp.expand(Eamp*Econ)
check('A3a C07 eq.(3): E(l1)E(l2)^* = g1^2 PV PV + i pi g1(2g2+g1)[delta1 PV2 - PV1 delta2] + pi^2 (2g2+g1)^2 delta1 delta2',
      sp.simplify(prod - (G1**2*P1*P2 + sp.I*sp.pi*G1*(2*G2 + G1)*(d1*P2 - P1*d2) + sp.pi**2*(2*G2 + G1)**2*d1*d2)) == 0)
anom = sp.expand(Eamp*Econ - Estd_amp*Estd_con)
check('A3b C07 eq.(4): T-even anomaly = 4 pi^2 g2 (g2+g1) delta(l1+) delta(l2+)', sp.simplify(anom.coeff(d1*d2) - 4*sp.pi**2*G2*(G2 + G1)) == 0,
      'delta.delta coefficient = %s' % sp.factor(anom.coeff(d1*d2)))
check('A3c it vanishes iff g2 = 0 or g2 = -g1', set(sp.solve(sp.Eq(anom.coeff(d1*d2), 0), G2)) == {-G1, 0})
# C07 eq.(8): g1 g2 same-side terms = -(2pi)^2 g1 g2 dd + 2 pi i g1 g2 [d1 PV2 + d2 PV1] and equal the cross terms of E(l1)E(l2)
E1 = -2*sp.pi*sp.I*G2*d1 + G1*(-sp.I*sp.pi*d1 - P1)      # g2 part + g1/(-l+i0)
E2 = -2*sp.pi*sp.I*G2*d2 + G1*(-sp.I*sp.pi*d2 - P2)
cross = sp.expand(E1*E2).coeff(G1, 1).coeff(G2, 1)
check('A3d C07 eq.(8): the g1 g2 terms of the same-side graphs equal the g1 g2 part of E(l1)E(l2) (generalized exponentiation)',
      sp.simplify(cross - (-(2*sp.pi)**2*d1*d2 + 2*sp.pi*sp.I*(d1*P2 + d2*P1))) == 0, 'g1 g2 coefficient = %s' % cross)

print('\n=== A4: anomaly functions I1, I2 ===')
def bubble2d(k, m1, m2):
    """closed form of int d^2l [(l^2+m1^2)((k-l)^2+m2^2)]^-1 = (pi/sqrt(L)) ln[(s+sqrt(L))/(s-sqrt(L))],
    s = k^2+m1^2+m2^2, L = s^2 - 4 m1^2 m2^2 (derived here; checked against the Feynman-parameter form)"""
    s_ = k*k + m1*m1 + m2*m2
    L = s_*s_ - 4*m1*m1*m2*m2
    if L < 1e-14*s_*s_:
        return 2*np.pi/s_
    r = np.sqrt(L)
    return np.pi/r*2*np.log((s_ + r)/(2*m1*m2))          # stable: (s+r)(s-r) = 4 m1^2 m2^2
def F_feyn1d(k, mg, mq):
    return np.pi*integrate.quad(lambda x: 1.0/(x*(1 - x)*k*k + x*mq*mq + (1 - x)*mg*mg), 0, 1, epsabs=0, epsrel=1e-11, limit=200)[0]
def F_feyn(k, mg, mq):
    return bubble2d(k, mg, mq)
def G_feyn(k, mg, mq):
    """G(k) = pi int_0^1 dx [x(1-x)]^-1 B(k; mg, M_x),  M_x^2 = (x mq^2 + (1-x) mg^2)/(x(1-x))  (log endpoint singularities)"""
    def integrand(x):
        if x*(1 - x) < 1e-300:
            return 0.0                      # integrable log endpoint singularity; measure-zero point
        Mx = np.sqrt((x*mq*mq + (1 - x)*mg*mg)/(x*(1 - x)))
        return bubble2d(k, mg, Mx)/(x*(1 - x))
    return np.pi*integrate.quad(integrand, 0, 1, epsabs=0, epsrel=1e-10, limit=400, points=[1e-6, 1e-3, 0.5, 1 - 1e-3, 1 - 1e-6])[0]
def G_feyn2d(k, mg, mq):
    f = lambda y, x: 1.0/(x*(1 - x)*(y*(1 - y)*k*k + (1 - y)*mg*mg) + y*(x*mq*mq + (1 - x)*mg*mg))
    return np.pi**2*integrate.dblquad(f, 0, 1, 0, 1, epsabs=1e-9, epsrel=1e-6)[0]
def hankel(fun_b, k, rate):
    """2 pi int_0^inf b db J0(k b) fun_b(b) for exponentially decaying fun_b"""
    bmax = 50.0/rate
    if k == 0:
        return 2*np.pi*integrate.quad(lambda x: x*fun_b(x), 0, bmax, limit=500, points=[1e-3, 1e-1, 1.0])[0]
    zeros = special.jn_zeros(0, int(k*bmax/np.pi) + 2)/k
    edges = np.concatenate([[0.0], zeros[zeros < bmax], [bmax]])
    tot = 0.0
    for a, b in zip(edges[:-1], edges[1:]):
        tot += integrate.quad(lambda x: x*special.j0(k*x)*fun_b(x), a, b, limit=200, epsabs=1e-14, epsrel=1e-10)[0]
    return 2*np.pi*tot
def kint(fun):
    def g_(t):
        if t > 1 - 1e-9:
            return 0.0                      # k > 1e9: integrand ~ ln^2 k / k^3 dk, negligible
        return 2*np.pi*(t/(1 - t))*fun(t/(1 - t))/(1 - t)**2
    return integrate.quad(g_, 0, 1, limit=300, epsabs=1e-12, epsrel=1e-8, points=[0.2, 0.5, 0.8, 0.95])[0]
for mg, mq in [(0.5, 1.0), (1.0, 1.0), (0.2, 0.7)]:
    K0g = lambda b: special.k0(mg*b); K0q = lambda b: special.k0(mq*b)
    # Feynman forms vs Hankel forms (b space: F~(b) = (2pi)^2 K0g K0q, G~(b) = (2pi)^3 K0g^2 K0q)
    errF = max(abs(hankel(lambda b: K0g(b)*K0q(b), k, mg + mq) - F_feyn(k, mg, mq))/F_feyn(k, mg, mq) for k in [0.0, 0.7, 2.3])
    errG = max(abs(2*np.pi*hankel(lambda b: K0g(b)**2*K0q(b), k, 2*mg + mq) - G_feyn(k, mg, mq))/G_feyn(k, mg, mq) for k in [0.0, 1.1])
    check('A4a (mg,mq)=(%.1f,%.1f): F and G, Feynman-parameter forms = Hankel/K0 forms' % (mg, mq), errF < 1e-7 and errG < 1e-6,
          'max rel diff F %.1e, G %.1e' % (errF, errG))
    errB = max(abs(F_feyn(k, mg, mq) - F_feyn1d(k, mg, mq))/F_feyn1d(k, mg, mq) for k in [0.0, 0.4, 3.3, 20.0])
    errG2 = abs(G_feyn(0.9, mg, mq) - G_feyn2d(0.9, mg, mq))/G_feyn(0.9, mg, mq)
    check('A4a2 (mg,mq)=(%.1f,%.1f): closed-form 2D bubble = Feynman 1D form; 1D (x) form of G = 2D (x,y) form' % (mg, mq),
          errB < 1e-9 and errG2 < 1e-5, 'rel diff bubble %.1e, G %.1e' % (errB, errG2))
    I1 = lambda k: F_feyn(k, mg, mq)**2
    I2 = lambda k: -G_feyn(k, mg, mq)/(k*k + mq*mq)
    # Cauchy-Schwarz proof of I1(0)+I2(0) < 0: with dmu(b) = d^2b/(2pi)^2 * 2pi K0(mq b) (positive, total mass 1/mq^2),
    # F(0) = int dmu * 2pi K0(mg b), G(0) = int dmu * (2pi K0(mg b))^2  =>  F(0)^2 <= G(0) int dmu = G(0)/mq^2.
    mass = integrate.quad(lambda b: b*K0q(b), 0, 60/mq, limit=500, points=[1e-3, 1e-1, 1.0])[0]          # int dmu
    Fmu = integrate.quad(lambda b: b*K0q(b)*2*np.pi*K0g(b), 0, 60/mq, limit=500, points=[1e-3, 1e-1, 1.0])[0]
    Gmu = integrate.quad(lambda b: b*K0q(b)*(2*np.pi*K0g(b))**2, 0, 60/mq, limit=500, points=[1e-3, 1e-1, 1.0])[0]
    F0, G0 = F_feyn(0.0, mg, mq), G_feyn(0.0, mg, mq)
    F0_closed = np.pi*np.log(mq**2/mg**2)/(mq**2 - mg**2) if mg != mq else np.pi/mq**2
    check('A4b (mg,mq)=(%.1f,%.1f): measure identities int dmu = 1/mq^2, F(0)=int dmu f_g~, G(0)=int dmu f_g~^2; F(0) closed form' % (mg, mq),
          abs(mass - 1/mq**2) < 1e-9 and abs(Fmu - F0) < 1e-8*F0 and abs(Gmu - G0) < 1e-7*G0 and abs(F0 - F0_closed) < 1e-10*F0)
    s0 = I1(0.0) + I2(0.0)
    check('A4c (mg,mq)=(%.1f,%.1f): Cauchy-Schwarz: I1(0)+I2(0) = F(0)^2 - G(0)/mq^2 < 0 (strict: K0(mg b) is not constant)' % (mg, mq),
          s0 < 0 and F0**2 < G0/mq**2, 'F(0)^2=%.6f  G(0)/mq^2=%.6f' % (F0**2, G0/mq**2))
    # exact integrated cancellation (Parseval): int d^2k I1 = (2pi)^3 int b K0g^2 K0q^2 db = - int d^2k I2
    intI_b = (2*np.pi)**3*integrate.quad(lambda b: b*K0g(b)**2*K0q(b)**2, 0, 80.0/(mg + mq), limit=500, points=[1e-3, 1e-1, 1.0])[0]
    i1 = kint(I1); i2 = kint(I2)
    check('A4d (mg,mq)=(%.1f,%.1f): int d^2k I1 = +(2pi)^3 int b K0g^2 K0q^2 db = -int d^2k I2  =>  int d^2k (I1+I2) = 0 (collinear factorization survives)' % (mg, mq),
          abs(i1 - intI_b) < 1e-6*intI_b and abs(i2 + intI_b) < 1e-6*intI_b, 'k-space %.8f, %.8f ; b-space %.8f' % (i1, i2, intI_b))
    ks = [0.0, 0.3, 0.8, 1.5, 3.0, 6.0]
    vals = [I1(k) + I2(k) for k in ks]
    check('A4e (mg,mq)=(%.1f,%.1f): I1+I2 is non-zero point by point and changes sign (standard TMD factorization violated)' % (mg, mq),
          min(vals) < 0 < max(vals), 'I1+I2 at k=%s : %s' % (ks, ['%.3g' % v for v in vals]))
# mass-dimension bookkeeping of the printed C07 eq.(10) vs eq.(11)
Mdim = sp.symbols('M', positive=True)
dim_I1_printed = Mdim**4*(Mdim**2/(Mdim**2*Mdim**2))**2       # d^2l1 d^2l2 * prod_j (kT^2+mq^2)/[(l^2+mg^2)((k-l)^2+mq^2)]
dim_I1_correct = Mdim**4*(1/(Mdim**2*Mdim**2))**2
dim_I2 = Mdim**4/(Mdim**2*Mdim**2*Mdim**2*Mdim**2)
check('A4f mass dimensions: printed C07 eq.(10) ~ M^0, eq.(11) ~ M^-4, corrected eq.(10) ~ M^-4',
      sp.simplify(dim_I1_printed) == 1 and sp.simplify(dim_I1_correct - dim_I2) == 0)

print('\nSUMMARY: %d/%d PASS' % (sum(ok for _, ok in RESULTS), len(RESULTS)))
