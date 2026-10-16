"""
n24_msbar.py -- MSbar expansion of the massless vector correlator (claim N24), from Grozin's d-dimensional formulas
(hep-ph/0508242, eqs. (Photon1:Res1), (Photon2:Pi)); Laurent coefficients extracted by contour integration in eps
(trapezoidal rule on |eps| = 0.1, exponentially accurate since the nearest other singularities are at |eps| >= 1/3).
Conventions: Pi_here = -Pi_Grozin/e0^2; MSbar: Pi_hat = mu_MS^{2eps} Pi_bare, mu_MS^2 = mu^2 e^{gamma_E}/(4pi), g0^2 = 4 pi alpha_s mu_MS^{2eps};
the additive (contact) counterterm removes pure poles.  Expected (per N_c e_q^2):
   Pi^(0) = (1/12pi^2)(5/3 - L),   Pi^(1) = (1/12pi^2)(alpha_s/pi)(3 C_F/4)(55/12 - 4 zeta3 - L),  L = ln(Q^2/mu^2).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 50
RES = []
def check(name, ok, info=''):
    RES.append(bool(ok)); print(('PASS ' if ok else 'FAIL ') + name + (('   [' + info + ']') if info else ''), flush=True)
def G(a, b, Dd):
    return mp.gamma(a + b - Dd/2)*mp.gamma(Dd/2 - a)*mp.gamma(Dd/2 - b)/(mp.gamma(a)*mp.gamma(b)*mp.gamma(Dd - a - b))
def Pi0(e, L):
    Dd = 4 - 2*e; muMS2 = mp.e**mp.euler/(4*mp.pi)
    return muMS2**e*mp.e**(-e*L)/(4*mp.pi)**(Dd/2)*2*(Dd - 2)/(Dd - 1)*G(1, 1, Dd)
def Pi1_over_as_CF(e, L):
    Dd = 4 - 2*e; muMS2 = mp.e**mp.euler/(4*mp.pi)
    br = 2*(Dd - 2)/((Dd - 1)*(Dd - 4))*(-(Dd**2 - 7*Dd + 16)*G(1, 1, Dd)**2 + 4*(Dd - 3)*(Dd**2 - 4*Dd + 8)/(Dd - 4)*G(1, 1, Dd)*G(1, e, Dd))
    return -br*(4*mp.pi*muMS2**e)*muMS2**e*mp.e**(-2*e*L)/(4*mp.pi)**Dd
def laurent(f, kmin=-3, kmax=1, r=mp.mpf('0.1'), N=128):
    pts = [r*mp.e**(2j*mp.pi*(j + mp.mpf(1)/2)/N) for j in range(N)]
    vals = [f(z) for z in pts]
    return {k: sum(v*z**(-k) for v, z in zip(vals, pts))/N for k in range(kmin, kmax + 1)}
norm = 1/(12*mp.pi**2)
for L in [mp.mpf(0), mp.mpf('1.7'), mp.mpf('-0.6')]:
    c0 = laurent(lambda z: Pi0(z, L))
    c1 = laurent(lambda z: Pi1_over_as_CF(z, L))
    fin0 = mp.re(c0[0]); fin1 = mp.re(c1[0])
    check('L=%s: one loop MSbar finite part = (1/12pi^2)(5/3 - L)' % mp.nstr(L, 3), abs(fin0/norm - (mp.mpf(5)/3 - L)) < 1e-30, mp.nstr(fin0/norm, 20))
    target = (1/mp.pi)*mp.mpf(3)/4*(mp.mpf(55)/12 - 4*mp.zeta(3) - L)
    check('L=%s: two loop MSbar finite part = (1/12pi^2)(alpha_s/pi)(3C_F/4)(55/12 - 4 zeta3 - L)' % mp.nstr(L, 3), abs(fin1/norm - target) < 1e-30,
          'got %s, expected %s' % (mp.nstr(fin1/norm, 20), mp.nstr(target, 20)))
    check('L=%s: two loop: no 1/eps^2 or 1/eps^3 pole; simple pole = (1/12pi^2)(3/(8 pi)) independent of L (local counterterm)' % mp.nstr(L, 3),
          abs(c1[-2]) < 1e-35 and abs(c1[-3]) < 1e-35 and abs(c1[-1]/norm - 3/(8*mp.pi)) < 1e-30, 'pole/norm = %s' % mp.nstr(c1[-1]/norm, 15))
print('      (55/12 - 4 zeta3 = %s)' % mp.nstr(mp.mpf(55)/12 - 4*mp.zeta(3), 15))
# Adler function from the L-dependence: -dPi/dL = (1/12pi^2)[1 + (3 C_F/4) alpha_s/pi]  -> R = 12 pi Im Pi(s+i0) = 1 + alpha_s/pi for C_F = 4/3
print('\nSUMMARY n24_msbar: %d/%d PASS' % (sum(RES), len(RES)))
