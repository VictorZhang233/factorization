#!/usr/bin/env python3
"""E18 stage-2: Collins arXiv:0708.4410v1 eqs. (10),(11).
(1) dimension count (sympy scaling) of first line of (10), printed second line of (10), eq. (11);
(2) l^- residue and prefactor bookkeeping from the first line (symbolic, independent);
(3) momentum-space numerics: F(k) via Feynman parameter, G(k) = int d^2l F(|k-l|)/(l^2+mg^2) by direct
    quadrature; check int d^2k F^2 = int d^2k G/(k^2+mq^2) (corrected I1+I2 integrates to 0);
    printed numerator makes int d^2k (k^2+mq^2)^2 F^2 diverge; sign of I1(0)+I2(0).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
from scipy import integrate
ok = []
def check(n, c):
    ok.append(bool(c)); print(('PASS ' if c else 'FAIL ') + n)

# (1) dimensions: assign mass dimension via scaling s -> every dimensionful quantity times s^dim
s = sp.symbols('s', positive=True)
dim = {'lam': 1, 'g': 0, 'p': 1, 'k': 1, 'l': 1, 'm': 1}
# first line: lam^2 g^4 x p^+ int dk^- d^4l1 d^4l2 [p][p] /(D^4) * delta(l1+) delta(l2+) delta(M^2) /(D^2)
d_first = 2*dim['lam'] + dim['p'] + 1 + 8 + 2 - 4*2 - 1 - 1 - 2 - 2*2   # lam^2, p+, dk-, d4l1 d4l2, numerators, 4 denominators, 2 delta(l+), delta(M^2), 2 denominators
# second line printed: lam^2 * int d^2l1 d^2l2 prod (k^2+m^2)/(M^2 M^2)
d_second_pr = 2*dim['lam'] + 4 + 2*(2 - 4)
d_second_ok = 2*dim['lam'] + 4 + 2*(0 - 4)
d_I2 = 2*dim['lam'] + 4 - 4*2
print(f'   mass dims: first line {d_first}, printed second line {d_second_pr}, without numerator {d_second_ok}, eq.(11) {d_I2}')
check('first line of (10), corrected second line and (11) all have dimension M^-2 (TMD density); printed second line has M^+2',
      d_first == -2 and d_second_ok == -2 and d_I2 == -2 and d_second_pr == 2)

# (2) l^- integral at l^+=0 with spectator on shell (M=0): residue
u, x, pp, A, B, eps = sp.symbols('u x p_plus A B epsilon', positive=True)
km = -B/(2*(1 - x)*pp)          # from 2pi delta((p-k)^2 - mq^2), B = kT^2 + mq^2
D1 = -2*x*pp*u + 2*x*pp*km - A  # (k-l)^2 - mq^2, A = (kT-lT)^2 + mq^2
D2 = 2*(1 - x)*pp*u - 2*(1 - x)*pp*km - A   # (p-k+l)^2 - mq^2
u1 = sp.solve(sp.Eq(D1, 0), u)[0]      # pole of D1 + i eps lies in the upper half plane
res = sp.simplify(1/sp.diff(D1, u) / D2.subs(u, u1))
print('   residue at the D1 pole:', res)
check('int du /[(D1+i0)(D2+i0)] = 2 pi i * 1/(2 p^+ A) = i pi/(p^+ A): independent of B = kT^2+mq^2', sp.simplify(res - 1/(2*pp*A)) == 0)
# numeric confirmation of the l^- integral
xv, pv, Av, Bv, ev = 0.3, 1.7, 0.9, 2.3, 1e-3
f = lambda uu: 1/((-2*xv*pv*uu + 2*xv*pv*(-Bv/(2*(1 - xv)*pv)) - Av + 1j*ev)*(2*(1 - xv)*pv*uu - 2*(1 - xv)*pv*(-Bv/(2*(1 - xv)*pv)) - Av + 1j*ev))
re_ = integrate.quad(lambda uu: f(uu).real, -200, 200, points=[float(u1.subs({x: xv, pp: pv, A: Av, B: Bv})), (Av - Bv)/(2*(1 - xv)*pv)], limit=2000)[0]
im_ = integrate.quad(lambda uu: f(uu).imag, -200, 200, points=[float(u1.subs({x: xv, pp: pv, A: Av, B: Bv})), (Av - Bv)/(2*(1 - xv)*pv)], limit=2000)[0]
print(f'   numeric l^- integral = {re_:.5f}{im_:+.5f}i ; i pi/(p+ A) = {np.pi/(pv*Av):.5f}i')
check('numeric l^- integral agrees with i pi/(p^+ A)', abs(re_) < 2e-2 and abs(im_ - np.pi/(pv*Av)) < 2e-2)
# prefactor bookkeeping: C x p+ (2pi)^2 * [2pi/(2(1-x)p+)] * prod_j [2(1-x)p+ * (-1) ] * (i pi/(p+))(-i pi/(p+))
C = sp.symbols('C', positive=True)
pref = C*x*pp*(2*sp.pi)**2*(2*sp.pi/(2*(1 - x)*pp))*(2*(1 - x)*pp)**2*(-1)**2*(sp.I*sp.pi/pp)*(-sp.I*sp.pi/pp)
pref = sp.simplify(pref.subs(C, 1/(2*sp.pi)**12))
print('   I1 = (lam^2 g1^2 g2(g2+g1)) *', pref, '* F(kT)^2')
check('prefactor = x(1-x)/(256 pi^7) exactly (conjugate side with -i0); no (kT^2+mq^2) factor arises', sp.simplify(pref - x*(1 - x)/(256*sp.pi**7)) == 0)

# (3) numerics
mg, mq = 0.5, 1.0
ga, gw = np.polynomial.legendre.leggauss(200)
al = 0.5*(ga + 1); aw = 0.5*gw
def F_gl(q):
    q = np.atleast_1d(q)[:, None]
    return np.pi*np.sum(aw/(al*(1 - al)*q**2 + al*mq**2 + (1 - al)*mg**2), axis=1)
def F(q):
    # closed form pi/sqrt(Delta) ln[a+(1-a-)/((a+ - 1)(-a-))], roots of D(a) = -q^2 a^2 + (q^2+mq^2-mg^2) a + mg^2
    q = np.atleast_1d(np.asarray(q, float))
    out = np.empty_like(q)
    small = q < 1e-3
    out[small] = F_gl(q[small]) if np.any(small) else out[small]
    qq = q[~small]
    b = qq**2 + mq**2 - mg**2
    sD = np.sqrt(b**2 + 4*qq**2*mg**2)
    ap = (b + sD)/(2*qq**2)
    am = -mg**2/(qq**2*ap)
    apm1 = mq**2/(qq**2*(1 - am))
    out[~small] = np.pi/sD*np.log(ap*(1 - am)/(apm1*(-am)))
    return out
# closed-form check at q=0
check('F(0) = pi ln(mq^2/mg^2)/(mq^2-mg^2)', abs(F(0.0)[0] - np.pi*np.log(mq**2/mg**2)/(mq**2 - mg**2)) < 1e-10)
check('closed-form F agrees with Feynman-parameter quadrature at q = 0.01, 0.7, 5', np.allclose(F(np.array([0.01, 0.7, 5.0])), F_gl(np.array([0.01, 0.7, 5.0])), rtol=1e-9))
# G(k) = int_0^inf l dl/(l^2+mg^2) int_0^{2pi} dphi F(|k-l|)
phg, phw = np.polynomial.legendre.leggauss(96); ph = np.pi*(phg + 1); phw = np.pi*phw
tg, tw = np.polynomial.legendre.leggauss(400)
def G(k):
    # l-integral split at l = k: [0,k] with a sinh-type map clustering at both ends, [k,inf) with l = k + m t/(1-t)
    t = 0.5*(tg + 1); w = 0.5*tw
    segs = []
    if k > 0:
        # [0, k]: l = k * (1 - cos(pi t))/2 clusters nodes at l=0 and l=k
        l1 = k*(1 - np.cos(np.pi*t))/2; d1 = k*np.pi*np.sin(np.pi*t)/2
        segs.append((l1, w*d1))
    m_ = max(mg, mq)
    l2 = k + m_*t/(1 - t); d2 = m_/(1 - t)**2
    segs.append((l2, w*d2))
    tot = 0.0
    for l, wl in segs:
        q = np.sqrt(np.maximum(k**2 + l[:, None]**2 - 2*k*l[:, None]*np.cos(ph[None, :]), 0))
        Fq = F(q.ravel()).reshape(q.shape)
        ang = np.sum(Fq*phw[None, :], axis=1)
        tot += np.sum(wl*l/(l**2 + mg**2)*ang)
    return tot
# radial integrals over k with map k = mq t/(1-t)
tk = 0.5*(tg + 1); wk = 0.5*tw
kk = mq*tk/(1 - tk); dk = mq/(1 - tk)**2
Fk = F(kk)
IF2 = 2*np.pi*np.sum(wk*dk*kk*Fk**2)
Gk = np.array([G(k) for k in kk])
IG = 2*np.pi*np.sum(wk*dk*kk*Gk/(kk**2 + mq**2))
print(f'   int d^2k F^2 = {IF2:.9f} ;  int d^2k G/(k^2+mq^2) = {IG:.9f} ; rel diff {abs(IF2 - IG)/IF2:.1e}')
check('corrected I1 + I2 integrates to zero over kT (momentum-space quadrature)', abs(IF2 - IG)/IF2 < 1e-7)
I0 = F(0.0)[0]**2 - G(0.0)/mq**2
print(f'   [I1(0)+I2(0)]/N = F(0)^2 - G(0)/mq^2 = {F(0.0)[0]**2:.6f} - {G(0.0)/mq**2:.6f} = {I0:.6f}')
check('I1(0)+I2(0) < 0 (as stated by Collins)', I0 < 0)
for (a_, b_) in [(0.2, 2.0), (1.0, 1.0), (2.0, 0.3)]:
    mg, mq = a_, b_
    I0b = F(0.0)[0]**2 - G(0.0)/mq**2
    print(f'   (mg,mq)=({a_},{b_}): [I1(0)+I2(0)]/N = {I0b:.6f}')
mg, mq = 0.5, 1.0
# printed numerator: cut-off integrals grow without bound
for K in [10, 100, 1000]:
    val = integrate.quad(lambda k: 2*np.pi*k*(k**2 + mq**2)**2*F(k)[0]**2, 0, K, limit=400)[0]
    print(f'   printed form: int_(k<{K}) d^2k (k^2+mq^2)^2 F^2 = {val:.4e}')
val_k = [integrate.quad(lambda k: 2*np.pi*k*(k**2 + mq**2)**2*F(k)[0]**2, 0, K, limit=400)[0] for K in (100, 1000)]
check('printed second line of (10): int d^2kT I1 diverges (grows ~ K^2 ln^2 K), so the stated cancellation is impossible', val_k[1]/val_k[0] > 50)
print(f'\nSUMMARY: {sum(ok)}/{len(ok)} checks passed')
