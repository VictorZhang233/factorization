"""W13 / s5b: photon-gluon box contribution to g1 with FOUR-dimensional regulators (prop:coll-anomaly-scheme).
 hat g1 in units (alpha_s e_q^2 T_F/(2 pi)), helicity-weighted, same normalization and tensor ordering as s5
 (W^{mu nu} ~ M^{mu*} M^{nu}; hat g1 = i (k.q)/(2[(k.q)^2 - q^2 k^2]) eps_{mu nu al be} q^al k^be W_A^{mu nu}).
 (i)  massless quarks, off-shell gluon k^2 = -P^2 (P^2 << Q^2): hat g1 = (2x-1) ln(Q^2/P^2) + B_off(x) + O(P^2/Q^2);
 (ii) quarks of mass m, on-shell gluon:                          hat g1 = (2x-1) ln(Q^2/m^2) + B_m(x)   + O(m^2/Q^2);
 first moments int_0^1 hat g1 dx (the logarithm drops out since int (2x-1) = 0).
 Expected (to be tested): B_m(x) = (2x-1) ln((1-x)/x) + 3 - 4x  [= Delta C_g^HVBM(mu=Q)/T_F, first moment 0];
                          int_0^1 B_off = -1 (the anomaly value).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from scipy import integrate

npass = 0; nfail = 0
def check(name, ok):
    global npass, nfail
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    if ok: npass += 1
    else: nfail += 1

I2 = np.eye(2); Z2 = np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
G = [np.block([[I2, Z2], [Z2, -I2]]).astype(complex)] + [np.block([[Z2, s], [-s, Z2]]) for s in (sx, sy, sz)]
eta = np.diag([1., -1., -1., -1.])
def sl(v): return sum(eta[m, m]*v[m]*G[m] for m in range(4))
def dot(a, b): return a @ eta @ b
LC = np.zeros((4, 4, 4, 4))
import itertools
for p in itertools.permutations(range(4)):
    s = 1
    pl = list(p)
    for i in range(4):
        for j in range(i + 1, 4):
            if pl[i] > pl[j]: s = -s
    LC[p] = s          # eps^{0123} = +1 (upper)
LClow = -LC            # eps_{0123} = -1
ONE = np.eye(4)

def g1_integrand(xv, cth, phi, rho, m):
    """Q^2 = 1; rho = P^2 (off-shell gluon), m = quark mass.  Returns hat g1 integrand per (1/8pi) dPhi normalization
    such that hat g1 = int_0^1 dv f(v) [azimuth-averaged], in units alpha_s e^2 T_F/(2 pi)."""
    kq = 1/(2*xv)
    shat = 1/xv - 1 - rho          # (k+q)^2 = k^2 + 2kq + q^2
    rs = np.sqrt(shat)
    k0 = (kq - rho)/rs; kz = np.sqrt(k0**2 + rho)
    k = np.array([k0, 0, 0, kz]); q = np.array([rs - k0, 0, 0, -kz])
    E = rs/2; pabs = np.sqrt(max(E**2 - m**2, 0)); beta = pabs/E
    sth = np.sqrt(1 - cth**2)
    p1 = np.array([E, pabs*sth*np.cos(phi), pabs*sth*np.sin(phi), pabs*cth])
    p2 = np.array([rs, 0, 0, 0]) - p1
    P1 = sl(p1) + m*ONE; P2 = sl(p2) - m*ONE          # u ubar, v vbar
    l1 = p1 - q; l2 = p1 - k
    S1 = (sl(l1) + m*ONE)/(dot(l1, l1) - m**2); S2 = (sl(l2) + m*ONE)/(dot(l2, l2) - m**2)
    def Gam(gmu, ge): return gmu @ S1 @ ge + ge @ S2 @ gmu
    def Gbar(gnu, gec): return gec @ S1 @ gnu + gnu @ S2 @ gec
    ep = np.array([0, 1, 1j, 0])/np.sqrt(2); em = np.array([0, 1, -1j, 0])/np.sqrt(2)
    Pmn = np.einsum('mnab,a,b->mn', LClow, q, k)
    tot = 0
    for sgn, e in ((+1, ep), (-1, em)):
        ge = sl(e); gec = sl(np.conj(e))
        for mu in range(4):
            for nu in range(4):
                if Pmn[mu, nu] == 0: continue
                # W^{mu nu} ~ M^{mu*} M^{nu}:  Tr[ p1 Gamma^{nu} p2 Gammabar^{mu} ]
                t = np.trace(P1 @ Gam(G[nu], ge) @ P2 @ Gbar(G[mu], gec))
                tot += sgn*Pmn[mu, nu]*t
    WA = tot/2.0                                      # [W(+)-W(-)]/2 contracted with the projector
    norm = 1j*kq/(2*(kq**2 - dot(q, q)*dot(k, k)))
    # prefactor: (T_F e^2 g^2/4pi) dPhi2 ; dPhi2 = beta/(8 pi) dv dphi/(2pi);  (T_F e^2 4pi a_s/(4pi))(1/8pi) = (a_s e^2 T_F/2pi)/4
    return (norm*WA).real*beta/4.0

def hat_g1(xv, rho, m):
    f = lambda v: np.mean([g1_integrand(xv, 1 - 2*v, ph, rho, m) for ph in (0.0, np.pi/2, np.pi/4)])
    val, err = integrate.quad(f, 0, 1, limit=400, epsabs=1e-13, epsrel=1e-12, points=[1e-6, 1e-3, 0.5, 1 - 1e-3, 1 - 1e-6])
    return val

# azimuth independence check
xv = 0.3
vals = [g1_integrand(xv, 0.2, ph, 1e-4, 0.0) for ph in (0.0, 0.7, 2.1)]
check('azimuthal independence of the helicity-weighted integrand (off-shell case)', np.ptp(vals) < 1e-9*max(1, abs(vals[0])))
vals = [g1_integrand(xv, 0.2, ph, 0.0, 1e-2) for ph in (0.0, 0.7, 2.1)]
check('azimuthal independence of the helicity-weighted integrand (massive case)', np.ptp(vals) < 1e-9*max(1, abs(vals[0])))

# (ii) massive quarks: extract B_m(x) = hat g1 - (2x-1) ln(1/m^2)
print('(ii) massive quarks, on-shell gluon')
okB = True
for xv in (0.2, 0.45, 0.7):
    res = []
    for m in (1e-3, 3e-4):
        g = hat_g1(xv, 0.0, m)
        res.append(g - (2*xv - 1)*np.log(1/m**2))
    Bexp = (2*xv - 1)*np.log((1 - xv)/xv) + 3 - 4*xv
    print('   x=%.2f  B_m(m=1e-3)=%.8f  B_m(m=3e-4)=%.8f  expected %.8f' % (xv, res[0], res[1], Bexp))
    okB &= abs(res[1] - Bexp) < 5e-5
check('(ii) B_m(x) = (2x-1) ln((1-x)/x) + 3 - 4x  (equals Delta C_g^HVBM(mu=Q)/T_F)', okB)
# first moment (finite m, exact): int_0^xmax hat g1 dx
def first_moment(rho, m):
    xmax = 1/(1 + 4*m**2) if m > 0 else 1.0
    val, err = integrate.quad(lambda xv: hat_g1(xv, rho, m), 1e-9, xmax*(1 - 1e-12), limit=200, epsabs=1e-10)
    return val
for m in (0.05, 0.01):
    fm = first_moment(0.0, m)
    print('   first moment, m = %.3f :  %.8f' % (m, fm))
check('(ii) first moment of the massive box vanishes (m = 0.05, 0.01)', abs(first_moment(0.0, 0.05)) < 1e-6 and abs(first_moment(0.0, 0.01)) < 1e-6)

# (i) off-shell gluon
print('(i) massless quarks, off-shell gluon')
Boff = {}
for xv in (0.2, 0.45, 0.7):
    res = []
    for rho in (1e-5, 1e-7):
        g = hat_g1(xv, rho, 0.0)
        res.append(g - (2*xv - 1)*np.log(1/rho))
    Boff[xv] = res[1]
    cand = (2*xv - 1)*np.log((1 - xv)/xv) + 3 - 4*xv - (2*xv - 1)*np.log(xv*(1-xv)) if False else None
    print('   x=%.2f  B_off(rho=1e-5)=%.8f  B_off(rho=1e-7)=%.8f' % (xv, res[0], res[1]))
# candidate closed form: B_off = (2x-1)[ln((1-x)/x) + ln(1/(x(1-x)))... ] fitted below via the first moment
for rho in (1e-4, 1e-6):
    fm = first_moment(rho, 0.0)
    print('   first moment, rho = %.0e :  %.8f' % (rho, fm))
fm6 = first_moment(1e-6, 0.0)
check('(i) first moment of the off-shell-gluon box = -1 (+O(P^2/Q^2))', abs(fm6 + 1) < 1e-4)
# candidate for B_off: (2x-1) ln(1/(x^2)) + ... test the known structure B_off = (2x-1)(ln((1-x)/x) - 1) + 2(1-x) - 2(1-x) ... print differences
for xv, b in Boff.items():
    c1 = (2*xv - 1)*(np.log(1/xv**2) - 2) + 2*(1 - xv)     # trial
    c2 = (2*xv - 1)*(np.log((1 - xv)/xv) - 1)              # 'CI' form
    c3 = (2*xv - 1)*(np.log(1/(xv*(1 - xv))) - 1) + 0      # trial
    print('   x=%.2f  B_off=%.8f   trial1=%.8f  CI=(2x-1)(ln((1-x)/x)-1)=%.8f  trial3=%.8f' % (xv, b, c1, c2, c3))
print('\nSUMMARY s5b: %d PASS, %d FAIL' % (npass, nfail))
