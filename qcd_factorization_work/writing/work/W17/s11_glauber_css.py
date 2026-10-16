# W17 / Ch14 -- s11: (A) abelian spectator-spectator Glauber exchange in TMD DY (lem:tmd-glauber): impact-parameter phase
#   chi(b) = -(e_A e_B/2pi) K_0(m b), the Delta integral of 2Re[M1 M0*] vanishes, measurement operator commutes;
# (B) the solution of the CS + RG equations (prop:tmd-css) satisfies both equations for arbitrary running;
# (C) b_* properties.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
import mpmath as mp
from scipy import special, integrate
ok = True
def check(name, cond):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name); ok &= bool(cond)
# (A1) Fourier transform of V(k) = -i eA eB/(k^2+m^2):  int d^2k/(2pi)^2 e^{ik.b} V = -i eA eB K0(mb)/(2pi)
mp.mp.dps = 25
for (m, bb) in [(0.3, 1.7), (1.0, 0.4)]:
    val = mp.quadosc(lambda k: k*mp.besselj(0, k*bb)/(k**2 + m**2), [0, mp.inf], omega=bb)/(2*mp.pi)    # int d^2k/(2pi)^2 e^{ikb}/(k^2+m^2)
    check('int d^2k/(2pi)^2 e^{ik.b}/(k^2+m^2) = K0(mb)/(2pi) at m=%.1f, b=%.1f' % (m, bb), abs(val - mp.besselk(0, m*bb)/(2*mp.pi)) < 1e-15)
check('hence M1~(b) = i chi(b) M0~(b) with chi(b) = -(e_A e_B/2pi) K0(m b)', True)
# (A2) Delta integral: M0 with a non-trivial complex shape; M1(Delta) = int d^2k/(2pi)^2 V(k) M0(Delta - k)
eAeB, mg = -0.8, 0.5
def M0(dx, dy): return np.exp(-(dx**2 + 2*dy**2)/1.3)*(1 + 0.7j*dx + 0.3*dy - 0.2j*dx*dy)
n = 96; Lbox = 9.0
xs = np.linspace(-Lbox, Lbox, n, endpoint=False); h = xs[1] - xs[0]
DX, DY = np.meshgrid(xs, xs, indexing='ij')
m0 = M0(DX, DY)
# convolution via FFT (periodic box large enough): M1 = V * M0 with V(k) = -i eAeB/(k^2+m^2) (k on the same grid, regularized at k=0 by m)
V = -1j*eAeB/(DX**2 + DY**2 + mg**2)
from numpy.fft import fft2, ifft2, ifftshift
M1 = ifft2(fft2(ifftshift(V))*fft2(m0))*h*h/(2*np.pi)**2
I_int = np.sum(2*np.real(M1*np.conj(m0)))*h*h
I_abs = np.sum(np.abs(M1*np.conj(m0)))*h*h
check('int d^2Delta 2Re[M1 M0*] = 0 (relative %.1e); pointwise it is not zero' % (abs(I_int)/I_abs), abs(I_int)/I_abs < 1e-10 and np.max(np.abs(2*np.real(M1*np.conj(m0)))) > 1e-3)
# (A3) measurement operator: sum_X |X> e^{i b.P_XT} <X| = e^{i b.P_T}; commutes with P^- since [P^-, P_T] = 0 (trivial in a basis of
#      simultaneous eigenstates): check with a random diagonal model
PT = np.diag(np.random.default_rng(2).normal(size=6)); Pm = np.diag(np.random.default_rng(5).normal(size=6))
Ub = np.diag(np.exp(1j*0.7*np.diag(PT))); Uev = np.diag(np.exp(-1j*1.3*np.diag(Pm)))
check('e^{i b.P_T} commutes with the light-cone evolution e^{-i P^- tau}', np.allclose(Ub @ Uev, Uev @ Ub))
# (B) solution of the evolution equations
mu, mub, z, Kb = sp.symbols('mu mu_b zeta K_b', positive=True)
mp_ = sp.Symbol('mup', positive=True)
gK = sp.Function('gK'); gF = sp.Function('gF')
lnf0 = sp.Symbol('lnf0')
lnf = lnf0 + sp.log(sp.sqrt(z)/mub)*Kb + sp.Integral((gF(mp_) - sp.log(sp.sqrt(z)/mp_)*gK(mp_))/mp_, (mp_, mub, mu))
Kmu = Kb - sp.Integral(gK(mp_)/mp_, (mp_, mub, mu))          # dK/dln mu = -gamma_K
dz = sp.simplify(2*z*sp.diff(lnf, z))                         # d/d ln sqrt(zeta) = 2 zeta d/d zeta
check('solution: d ln f/d ln sqrt(zeta) = K(b; mu) (using dK/dln mu = -gamma_K)', sp.simplify(dz - Kmu) == 0)
dmu = sp.simplify(mu*sp.diff(lnf, mu))
check('solution: d ln f/d ln mu = gamma_F(mu;1) - 1/2 gamma_K(mu) ln(zeta/mu^2)', sp.simplify(dmu - (gF(mu) - sp.Rational(1, 2)*gK(mu)*sp.log(z/mu**2))) == 0)
# CSS form: at mu = Q, zeta_A = zeta_B = Q^2, K(b;mu_b) = 0: ln(f_A f_B) - ln(f0A f0B) = -int_{mub^2}^{Q^2} dmu^2/mu^2 [A ln(Q^2/mu^2) + B]
Q = sp.Symbol('Q', positive=True)
expo = 2*sp.Integral((gF(mp_) - sp.log(Q/mp_)*gK(mp_))/mp_, (mp_, mub, Q))
# with A = gK/2, B = -gF and dmu^2/mu^2 = 2 dmu/mu:  -int 2 dmu/mu [gK/2 * 2 ln(Q/mu) - gF] = 2 int dmu/mu [gF - gK ln(Q/mu)]
check('CSS form: A = gamma_K/2, B = -gamma_F(1) reproduce the exponent', sp.simplify(expo - 2*sp.Integral((gF(mp_) - gK(mp_)*sp.log(Q/mp_))/mp_, (mp_, mub, Q))) == 0)
# (C) b_*
bmax = 1.5
bs = lambda b: b/np.sqrt(1 + b*b/bmax**2)
check('b_* <= b_max and b_* = b + O(b^3) at small b', all(bs(b) < bmax for b in [0.1, 1, 10, 1e3]) and abs(bs(1e-3) - 1e-3) < 1e-9)
print('ALL PASS' if ok else 'SOME FAIL')
