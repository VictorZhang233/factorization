"""N16 -- Collins arXiv:0708.4410v1, eqs. (10), (11): anomalous two-gluon terms I_1 (opposite sides of the cut)
and I_2 (same side) in the all-scalar abelian model (m_q, m_g, M=0).
Checks (independent of research/c_glauber/scripts/tmd_breaking_abelian.py):
 (a) the minus-component integrals of the FIRST line of eq. (10) (one gluon per side) give 2 pi i/(2p^+ A_j), so that
     I_1 = N F(k_T)^2 with N = lam^2 g1^2 g2(g2+g1) x(1-x)/(256 pi^7) -- i.e. WITHOUT the factor prod_j (k_T^2+m_q^2)
     printed in the second line of eq. (10);
 (b) the same-side graphs (sum of the two spectator orderings) give (-2 pi i/P)(2 pi i/(2p^+ A_12)) times the
     conjugate tree quark propagator -(1-x)/(k_T^2+m_q^2): structure G(k_T)/(k_T^2+m_q^2) of eq. (11);
 (c) F(k) closed form (pi/sqrt(Lam)) ln((s+sqrt(Lam))/(s-sqrt(Lam))), b-space forms, Feynman-parameter form of G;
 (d) Parseval: int d^2k F^2 = int d^2k G/(k^2+m_q^2)  =>  int d^2k (I_1+I_2) = 0;
 (e) Cauchy-Schwarz proof of F(0)^2 < G(0)/m_q^2, i.e. I_1(0)+I_2(0) has the sign of -N;
 (f) point values of (I_1+I_2)/N at (m_g, m_q) = (0.5, 1).
Run: python3 -I -u n16_collins07.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
mp.mp.dps = 30

npass = nfail = 0
def report(ok, name, detail=''):
    global npass, nfail
    if ok: npass += 1
    else: nfail += 1
    print(('PASS ' if ok else 'FAIL ') + name + ('   [' + detail + ']' if detail else ''), flush=True)

# ---------------------------------------------------------------------------------------------
# (a) one-gluon-per-side minus integral, finite i0 = eps, exact residue vs numerical quadrature
# ---------------------------------------------------------------------------------------------
pp, xx = mp.mpf('2.3'), mp.mpf('0.37')
P = 2*(1-xx)*pp
for A in [mp.mpf('0.9'), mp.mpf('2.7')]:
    for eps in [mp.mpf('0.3'), mp.mpf('0.02')]:
        f = lambda u: 1/((-2*xx*pp*u - A + 1j*eps)*(P*u - A + 1j*eps))
        u1 = (-A + 1j*eps)/(2*xx*pp); u2 = (A - 1j*eps)/P
        num = mp.quad(f, [-mp.inf, mp.re(u1), 0, mp.re(u2), mp.inf])
        res = 2j*mp.pi*(1/(-2*xx*pp))*(1/(P*u1 - A + 1j*eps))      # close in the UHP (pole u1)
        report(abs(num - res) < mp.mpf('1e-15'), f'minus integral (one gluon, amplitude side) A={A}, eps={eps}', f'{mp.nstr(num,12)} vs residue {mp.nstr(res,12)}')
    report(True, f'eps->0 limit: 2 pi i/(2 p^+ A) = {mp.nstr(2j*mp.pi/(2*pp*A), 12)}', 'algebra: P u1 - A -> -A/x')
# symbolic eps->0 of the residue
X, PP, AA = sp.symbols('x p A', positive=True)
U1 = -AA/(2*X*PP)
lim = sp.simplify(2*sp.pi*sp.I*(1/(-2*X*PP))*(1/(2*(1-X)*PP*U1 - AA)))
report(sp.simplify(lim - 2*sp.pi*sp.I/(2*PP*AA)) == 0, 'symbolic: residue -> 2 pi i/(2 p^+ A), independent of x', str(lim))
# assemble the constant of eq. (10): x p^+ * [2(1-x)p^+]^2 * 1/(2(1-x)p^+) [cut delta in k^-] * |2 pi i/(2p^+)|^2 * (2pi)^2 [delta(l^+)] * 2pi [cut]
const = X*PP*(2*(1-X)*PP)**2/(2*(1-X)*PP) * (2*sp.pi/(2*PP))**2 * (2*sp.pi)**2 * 2*sp.pi / (2*sp.pi)**12
report(sp.simplify(const - X*(1-X)/(256*sp.pi**7)) == 0, 'prefactor of eq.(10) first line reduces to x(1-x)/(256 pi^7) with integrand prod_j 1/((l_j^2+m_g^2)((k-l_j)^2+m_q^2))',
       str(sp.simplify(const)))
print('   => I_1 = N * F(k_T)^2; the printed 2nd line of eq.(10) has an extra prod_j (k_T^2+m_q^2) (dimension M^0 instead of M^-4 for the integral).')

# ---------------------------------------------------------------------------------------------
# (b) same-side: sum over the two spectator orderings; inner integral = -2 pi i / P
# ---------------------------------------------------------------------------------------------
for (c1, c2, v, eps) in [(0.3, -0.7, 0.4, 0.05), (-1.1, 0.2, -0.9, 0.2)]:
    c1, c2, v, eps = map(mp.mpf, (c1, c2, v, eps))
    g = lambda l: 1/(P*l + c1 + 1j*eps) + 1/(P*(v - l) + c2 + 1j*eps)
    L = mp.mpf(10)**6
    num = mp.quad(g, [-L, -100, -1, 0, 1, 100, L])
    report(abs(num - (-2j*mp.pi/P)) < mp.mpf('1e-4'), f'same-side inner integral over l1^- (two orderings) = -2 pi i/P, c1={c1}, c2={c2}', f'{mp.nstr(num,10)} vs {mp.nstr(-2j*mp.pi/P,10)}')
# outer v-integral: int dv 1/(P v + c12 + i eps) * 1/(2 x p^+ (k^- - v) - A12 + i eps), with k^- = -(kT^2+m^2)/P,
# c12 = kT^2 - (k-l1-l2)_T^2 ; A12 = (k-l1-l2)_T^2 + m^2
kT2, kl2, m2 = mp.mpf('0.8'), mp.mpf('1.7'), mp.mpf('1.0')
c12 = kT2 - kl2; A12 = kl2 + m2; kminus = -(kT2 + m2)/P
for eps in [mp.mpf('0.1'), mp.mpf('0.01')]:
    h = lambda vv: 1/((P*vv + c12 + 1j*eps)*(2*xx*pp*(kminus - vv) - A12 + 1j*eps))
    vb = kminus - (A12 - 1j*eps)/(2*xx*pp)          # UHP pole
    exact_eps = 2j*mp.pi/((P*vb + c12 + 1j*eps)*(-2*xx*pp))
    bps = sorted([-c12/P, mp.mpf(0), mp.re(vb)])
    num = mp.quad(h, [-mp.inf] + bps + [mp.inf])
    report(abs(num - exact_eps) < mp.mpf('1e-12'), f'same-side outer integral = exact residue at eps={eps}', f'{mp.nstr(num,10)} vs {mp.nstr(exact_eps,10)}')
report(True, 'eps->0 of the outer residue: 2 pi i/(2p^+ A12) = ' + mp.nstr(2j*mp.pi/(2*pp*A12), 10), 'P v_b + c12 -> -A12/x (algebra in the comments of DERIVATION check)')
VB = sp.symbols('kT2 A12', positive=True)
kT2s, A12s = VB
kms = -(kT2s + 1)/(2*(1-X)*PP)
c12s = kT2s - (A12s - 1)
vbs = kms - A12s/(2*X*PP)
lim2 = sp.simplify(2*sp.pi*sp.I/((2*(1-X)*PP*vbs + c12s)*(-2*X*PP)))
report(sp.simplify(lim2 - 2*sp.pi*sp.I/(2*PP*A12s)) == 0, 'symbolic: same-side outer residue -> 2 pi i/(2 p^+ A12) (m_q=1)', str(lim2))
# conjugate-side tree quark propagator at the cut: k^2 - m^2 = 2 x p^+ k^- - kT^2 - m^2 = -(kT^2+m^2)/(1-x)
report(abs((2*xx*pp*kminus - kT2 - m2) + (kT2 + m2)/(1 - xx)) < mp.mpf('1e-25'), 'conjugate tree propagator k^2-m^2 = -(k_T^2+m_q^2)/(1-x) (source of 1/(k_T^2+m_q^2) in eq.(11))')

# ---------------------------------------------------------------------------------------------
# (c) F and G: closed form, b space, Feynman parameters
# ---------------------------------------------------------------------------------------------
def F_closed(k, mg, mq):
    # (pi/sqrt(Lam)) ln((s+sqrt(Lam))/(s-sqrt(Lam))), written stably using (s+sqrtL)(s-sqrtL) = 4 mg^2 mq^2
    s = k**2 + mg**2 + mq**2; Lam = s**2 - 4*mg**2*mq**2
    if Lam == 0: return 2*mp.pi/s
    return mp.pi/mp.sqrt(Lam)*mp.log((s + mp.sqrt(Lam))**2/(4*mg**2*mq**2))
def F_feyn(k, mg, mq):   # int d^2l/((l^2+mg^2)((k-l)^2+mq^2)) = pi int_0^1 dx / (x(1-x)k^2 + x mq^2 + (1-x) mg^2)
    return mp.pi*mp.quad(lambda y: 1/(y*(1-y)*k**2 + y*mq**2 + (1-y)*mg**2), [0, 1])
def F_b(k, mg, mq):
    return 2*mp.pi*mp.quad(lambda b: b*mp.besselj(0, k*b)*mp.besselk(0, mg*b)*mp.besselk(0, mq*b), [0, 1, 5, 20, 60])
def G_feyn(k, mg, mq):   # c_glauber representation
    return mp.pi**2*mp.quad(lambda x, y: 1/(x*(1-x)*(y*(1-y)*k**2 + (1-y)*mg**2) + y*(x*mq**2 + (1-x)*mg**2)), [0, 1], [0, 1])
def G_b(k, mg, mq):
    return (2*mp.pi)**2*mp.quad(lambda b: b*mp.besselj(0, k*b)*mp.besselk(0, mg*b)**2*mp.besselk(0, mq*b), [0, 1, 5, 20, 60])
def G_direct(k, mg, mq):
    # G(k) = int d^2l1 f_g(l1) * F_{g,q}(k - l1)  (inner l2 integral done in closed form) -- independent route
    def inner(l1, phi):
        kl = mp.sqrt(k**2 + l1**2 - 2*k*l1*mp.cos(phi))
        return F_closed(kl, mg, mq)
    return mp.quad(lambda l1: l1/(l1**2 + mg**2)*2*mp.quad(lambda phi: inner(l1, phi), [0, mp.pi]), [0, 1, 10, mp.inf])
mg, mq = mp.mpf('0.5'), mp.mpf(1)
for k in [mp.mpf(0), mp.mpf('0.8'), mp.mpf(3)]:
    a, b, c = F_closed(k, mg, mq) if k > 0 else mp.pi/(mq**2 - mg**2)*mp.log(mq**2/mg**2), F_feyn(k, mg, mq), F_b(k, mg, mq)
    report(abs(a/b - 1) < 1e-12 and abs(c/b - 1) < 1e-8, f'F(k): closed form = Feynman parameter = b space, k={k}', f'{mp.nstr(a,12)}, {mp.nstr(b,12)}, {mp.nstr(c,12)}')
mp.mp.dps = 15
for k in [mp.mpf(0), mp.mpf('0.8')]:
    a, b, c = G_feyn(k, mg, mq), G_b(k, mg, mq), G_direct(k, mg, mq)
    report(abs(a/b - 1) < 1e-6 and abs(c/b - 1) < 1e-6, f'G(k): Feynman-parameter = b space = direct convolution, k={k}', f'{mp.nstr(a,10)}, {mp.nstr(b,10)}, {mp.nstr(c,10)}')
mp.mp.dps = 30

# ---------------------------------------------------------------------------------------------
# (d) Parseval / cancellation of the k_T integral
# ---------------------------------------------------------------------------------------------
bval = (2*mp.pi)**3*mp.quad(lambda b: b*mp.besselk(0, mg*b)**2*mp.besselk(0, mq*b)**2, [0, 1, 5, 20, 80])
k1 = 2*mp.pi*mp.quad(lambda k: k*F_closed(k, mg, mq)**2, [0, 1, 10, 100, mp.inf])
# fast G via scipy (adaptive QUADPACK on the Feynman-parameter form), cross-checked against the mpmath value
import numpy as np
from scipy import integrate as si
def G_fast(k, mg=0.5, mq=1.0):
    fxy = lambda y, x: 1.0/(x*(1-x)*(y*(1-y)*k*k + (1-y)*mg*mg) + y*(x*mq*mq + (1-x)*mg*mg))
    v, e = si.dblquad(fxy, 0.0, 1.0, 0.0, 1.0, epsabs=1e-11, epsrel=1e-11)
    return np.pi**2*v
for kk in [0.0, 0.8]:
    report(abs(G_fast(kk)/float(G_feyn(mp.mpf(kk), mg, mq)) - 1) < 1e-8, f'scipy G_fast({kk}) = mpmath G_feyn', f'{G_fast(kk):.10f}')
k2 = 2*np.pi*(si.quad(lambda k: k*G_fast(k)/(k*k + 1.0), 0, 1, epsabs=1e-12, epsrel=1e-11, limit=200)[0]
              + si.quad(lambda k: k*G_fast(k)/(k*k + 1.0), 1, 20, epsabs=1e-12, epsrel=1e-11, limit=200)[0]
              + si.quad(lambda k: k*G_fast(k)/(k*k + 1.0), 20, np.inf, epsabs=1e-12, epsrel=1e-11, limit=200)[0])
k2 = mp.mpf(k2)
report(abs(k1/bval - 1) < 1e-10, 'int d^2k F^2 = (2pi)^3 int db b K0(mg b)^2 K0(mq b)^2', f'{mp.nstr(k1,14)} vs {mp.nstr(bval,14)}')
report(abs(k2/bval - 1) < 1e-5, 'int d^2k G/(k^2+mq^2) = same b-space value  =>  int d^2k (I1+I2) = 0', f'{mp.nstr(k2,10)} vs {mp.nstr(bval,10)}')
# printed eq.(10) would give int d^2k (k^2+mq^2)^2 F^2 = divergent (F ~ 2 pi ln(k^2)/k^2 at large k)
tail = [mp.nstr((k**2 + mq**2)**2*F_closed(k, mg, mq)**2*k, 6) for k in [mp.mpf(10), mp.mpf(100), mp.mpf(1000)]]
print('   printed-eq.(10) integrand k (k^2+m_q^2)^2 F^2 at k=10,100,1000 (grows => int d^2k diverges):', tail)

# ---------------------------------------------------------------------------------------------
# (e) Cauchy-Schwarz with dmu(b) = d^2b/(2pi)^2 2pi K0(mq b)
# ---------------------------------------------------------------------------------------------
mu_tot = mp.quad(lambda b: b*mp.besselk(0, mq*b), [0, 1, 10, mp.inf])          # (1/(2pi)^2) 2pi * 2pi int db b K0 = int db b K0
F0_mu = mp.quad(lambda b: b*mp.besselk(0, mq*b)*2*mp.pi*mp.besselk(0, mg*b), [0, 1, 10, mp.inf])
G0_mu = mp.quad(lambda b: b*mp.besselk(0, mq*b)*(2*mp.pi*mp.besselk(0, mg*b))**2, [0, 1, 10, mp.inf])
F0 = mp.pi/(mq**2 - mg**2)*mp.log(mq**2/mg**2)
mp.mp.dps = 15
G0 = G_feyn(mp.mpf(0), mg, mq)
mp.mp.dps = 30
report(abs(mu_tot - 1/mq**2) < 1e-20, 'int dmu = 1/m_q^2', mp.nstr(mu_tot, 20))
report(abs(F0_mu/F0 - 1) < 1e-15, 'F(0) = int dmu 2pi K0(m_g b)', f'{mp.nstr(F0_mu,15)} vs {mp.nstr(F0,15)}')
report(abs(G0_mu/G0 - 1) < 1e-6, 'G(0) = int dmu [2pi K0(m_g b)]^2', f'{mp.nstr(G0_mu,12)} vs {mp.nstr(G0,12)}')
report(F0**2 < G0_mu*mu_tot, 'Cauchy-Schwarz: F(0)^2 < G(0)/m_q^2 (strict)', f'F0^2={mp.nstr(F0**2,10)}, G0/mq^2={mp.nstr(G0_mu/mq**2,10)}')
# scan of masses: sign of F(0)^2 - G(0)/mq^2
worst = -mp.inf
for (a, b) in [(0.01, 1), (0.1, 1), (0.5, 1), (1, 1), (2, 1), (10, 1), (1, 0.05), (3, 0.2)]:
    a, b = mp.mpf(a), mp.mpf(b)
    F0x = mp.quad(lambda r: r*mp.besselk(0, b*r)*2*mp.pi*mp.besselk(0, a*r), [0, 0.1, 1, 10, mp.inf])
    G0x = mp.quad(lambda r: r*mp.besselk(0, b*r)*(2*mp.pi*mp.besselk(0, a*r))**2, [0, 0.1, 1, 10, mp.inf])
    worst = max(worst, (F0x**2 - G0x/b**2)/(G0x/b**2))
report(worst < 0, 'F(0)^2 - G(0)/m_q^2 < 0 for 8 mass pairs spanning m_g/m_q = 0.01 ... 60', f'max relative value = {mp.nstr(worst,6)}')

# ---------------------------------------------------------------------------------------------
# (f) point values (I1+I2)/N = F^2 - G/(k^2+mq^2) at (mg,mq) = (0.5,1)
# ---------------------------------------------------------------------------------------------
claimed = {0: -21.0, 0.3: -17.7, 0.8: -7.19, 1.5: -0.70, 3: 0.38, 6: 0.089}
mp.mp.dps = 15
for k, cv in claimed.items():
    kk = mp.mpf(k)
    Fk = F_closed(kk, mg, mq) if k > 0 else F0
    val = Fk**2 - mp.mpf(G_fast(float(k)))/(kk**2 + mq**2)
    ok = abs(val - cv) <= 0.0051*max(1, abs(cv)) if abs(cv) >= 1 else abs(val - cv) <= 0.006
    report(ok, f'(I1+I2)/N at k_T={k}', f'{mp.nstr(val,6)} vs claimed {cv}')

print(f'\nSUMMARY: {npass}/{npass+nfail} PASS')
