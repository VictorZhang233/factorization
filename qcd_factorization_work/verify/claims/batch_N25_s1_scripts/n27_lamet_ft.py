# -*- coding: utf-8 -*-
"""
n27_lamet_ft.py -- independent checks for claim N27 (one-loop quasi-PDF kernels = Fourier transforms of coordinate kernels).
Run: python3 -I n27_lamet_ft.py

Inputs (READ from the papers, arXiv sources):
  coordinate kernel  IJJSZ arXiv:1801.03917 eq. (ps-c) + Delta C_{gamma^z} = 2a(1-alpha);  ratio = MSbar / C_0(z)
  momentum kernels   IJJSZ eq. (quasi-matching) [MSbar] and eq. (quasi-matching-alt) [ratio], + gamma^z additions.
  a = alpha_s C_F/(2 pi) set to 1 (O(a) coefficients compared);  L(zeta) = ln zeta^2 + ell + 2 gamma_E, ell = ln(mu^2/(4 p_z^2)).

Method A (xi space, no zeta integral at all):
  FT[ln zeta^2](u) = -2 gamma_E delta(u) - [1/|u|]_R, <[1/|u|]_R, psi> = int_{|u|<1} (psi(u)-psi(0))/|u| + int_{|u|>1} psi/|u|.
  For C(alpha, L) = A(alpha) L + B(alpha):  <C_mom, phi> = ell <A,phi> + <B,phi> - <A, R_phi>,  R_phi(alpha) = <[1/|u|]_R, phi(alpha+u)>.
Method B (zeta space with EXACT closed-form Phi for slowly decaying test functions):
  phi(x) = (1+((x-x0)/s)^2)^(-nu):  Phi(zeta) = int phi e^{i x zeta} dx = s e^{i x0 zeta} (2 sqrt(pi)/Gamma(nu)) (s|zeta|/2)^(nu-1/2) K_{nu-1/2}(s|zeta|)
  <C_mom, phi> = int dzeta/(2pi) G(zeta) Phi(zeta),  G(zeta) = int_0^1 dalpha C(alpha, L(zeta)) e^{-i alpha zeta}, built from Ein/E1 closed forms.
Test functions: Gaussians (incl. centred at 1), Lorentzians (nu=1), and power-law tails |x|^{-2nu} with nu = 0.35, 0.2
(the latter decay like |x|^{-0.7}, |x|^{-0.4}: they do NOT vanish fast at large |x| -- probes the 'delta functions at infinity').
Also: momentum-RGE consistency P^z dC/dP^z.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np, sympy as sp, mpmath as mp
from scipy import integrate, special

RES = []
def rep(name, ok, extra=''):
    RES.append(bool(ok)); print('[%s] %s %s' % ('PASS' if ok else 'FAIL', name, extra), flush=True)
gE = float(mp.euler)

def Q(f, a, b, pts=None):
    return integrate.quad(f, a, b, points=pts, limit=1000, epsabs=1e-13, epsrel=1e-12)[0]
def Qinf(f, a, b):
    return integrate.quad(f, a, b, limit=1000, epsabs=1e-13, epsrel=1e-12)[0]

# ---------------------------------------------------------------- momentum-space kernels as printed (IJJSZ)
def g1(x): return (1 + x*x)/(1 - x)*np.log(x/(x - 1)) + 1
def g3(x): return -(1 + x*x)/(1 - x)*np.log(-x/(1 - x)) - 1
def mom_pair(phi, ell, sigma, scheme, tail_split=50.0):
    p1 = phi(1.0); t = 0.0
    if scheme == 'msbar':
        f1 = lambda x: (g1(x) + 1.5/x)*(phi(x) - p1)
        t += Q(f1, 1, 2) + Q(f1, 2, tail_split) + Qinf(f1, tail_split, np.inf)
        t -= Q(lambda x: 1.5/x*phi(x), 1, tail_split) + Qinf(lambda x: 1.5/x*phi(x), tail_split, np.inf)
        g2 = lambda x: (1 + x*x)/(1 - x)*(-ell + np.log(x*(1 - x))) - x*(1 + x)/(1 - x)
        t += Q(lambda x: g2(x)*(phi(x) - p1), 0, 1)
        f3 = lambda x: (g3(x) + 1.5/(1 - x))*(phi(x) - p1)
        t += Q(f3, -1, 0) + Q(f3, -tail_split, -1) + Qinf(f3, -np.inf, -tail_split)
        t -= Q(lambda x: 1.5/(1 - x)*phi(x), -tail_split, 0) + Qinf(lambda x: 1.5/(1 - x)*phi(x), -np.inf, -tail_split)
        t += (1.5*ell + 2.5)*p1
        if sigma == 1: t += Q(lambda x: 2*(1 - x)*phi(x), 0, 1)
        return t
    r1 = lambda x: (g1(x) - 1.5/(1 - x))*(phi(x) - p1)
    r2 = lambda x: ((1 + x*x)/(1 - x)*(-ell + np.log(x*(1 - x)) - 1) + 1 + 1.5/(1 - x))*(phi(x) - p1)
    r3 = lambda x: (g3(x) + 1.5/(1 - x))*(phi(x) - p1)
    t += Q(r1, 1, 2) + Q(r1, 2, tail_split) + Qinf(r1, tail_split, np.inf)
    t += Q(r2, 0, 1)
    t += Q(r3, -1, 0) + Q(r3, -tail_split, -1) + Qinf(r3, -np.inf, -tail_split)
    if sigma == 1: t += Q(lambda x: 2*(1 - x)*(phi(x) - p1), 0, 1)
    return t

# ---------------------------------------------------------------- Method A: xi-space evaluation of the FT of the coordinate kernel
def R_phi(phi, al, tail_split=50.0):
    f = lambda u: (phi(al + u) - phi(al))/abs(u)
    near = Q(f, -1, 0) + Q(f, 0, 1)
    far = Q(lambda u: phi(al + u)/u, 1, tail_split) + Qinf(lambda u: phi(al + u)/u, tail_split, np.inf) \
        + Q(lambda u: phi(al - u)/u, 1, tail_split) + Qinf(lambda u: phi(al - u)/u, tail_split, np.inf)
    return near + far
def plusB(F):      # <[(1+a^2)/(1-a)]_+, F>
    F1 = F(1.0); return Q(lambda a: (1 + a*a)/(1 - a)*(F(a) - F1), 0, 1)
def plusL(F):      # <[ln(1-a)/(1-a)]_+, F>
    F1 = F(1.0); return Q(lambda a: np.log(1 - a)/(1 - a)*(F(a) - F1), 0, 1)
def methodA(phi, ell, sigma, scheme):
    # cache R_phi on a Gauss-Legendre-friendly callable (smooth in alpha)
    cache = {}
    def R(al):
        k = round(al, 15)
        if k not in cache: cache[k] = R_phi(phi, al)
        return cache[k]
    if scheme == 'msbar':
        A_phi = 1.5*phi(1.0) - plusB(phi)
        A_R = 1.5*R(1.0) - plusB(R)
        B_phi = 1.5*phi(1.0) - plusB(phi) - 4*plusL(phi) + 2*(1 + sigma)*Q(lambda a: (1 - a)*phi(a), 0, 1)
    else:
        A_phi = -plusB(phi)
        A_R = -plusB(R)
        B_phi = -plusB(phi) - 4*plusL(phi) + (1 + sigma)*Q(lambda a: 2*(1 - a)*(phi(a) - phi(1.0)), 0, 1)
    return ell*A_phi + B_phi - A_R

# ---------------------------------------------------------------- Method B: zeta space with closed-form G(zeta) and Phi(zeta)
def _ser(iz, coef, nmax=40):
    tot = 0j; term = 1.0 + 0j
    for n in range(1, nmax):
        term = term*iz          # (iz)^n
        tot += term*coef(n)
    return tot
from math import factorial
def G_closed(zeta, ell, sigma, scheme):
    L = np.log(zeta**2) + ell + 2*gE
    ez = np.exp(-1j*zeta); iz = 1j*zeta
    if abs(zeta) < 1.0:     # power series (no cancellation): E0 = sum (iz)^n/(n n!), m1 = sum (iz)^n/(n+1)!, m2 = sum (iz)^n/(n! (n+2))
        E0 = _ser(iz, lambda n: 1.0/(n*factorial(n)))
        m1 = _ser(iz, lambda n: 1.0/factorial(n + 1))
        m2 = _ser(iz, lambda n: 1.0/(factorial(n)*(n + 2)))
        I3 = 2*(0.5 + _ser(-1j*zeta, lambda n: 1.0/factorial(n + 2)))   # 2 sum_{n>=0} c^n/(n+2)!, c=-i zeta
    else:
        w = -1j*zeta
        E0 = -(special.exp1(w) + np.log(w) + gE)                    # int_0^1 (e^{iuz}-1)/u du = -Ein(-iz), Ein(w)=E1(w)+ln w+gamma
        m1 = (np.exp(iz) - 1)/iz - 1                                # int_0^1 (e^{iuz}-1) du
        m2 = np.exp(iz)*(1/iz - 1/iz**2) + 1/iz**2 - 0.5            # int_0^1 u (e^{iuz}-1) du
        c = -1j*zeta
        I3 = 2*(np.exp(c) - 1 - c)/c**2                             # int_0^1 2(1-a) e^{-i a z} da
    I1 = ez*(2*E0 - 2*m1 + m2)
    if abs(zeta) < 1.0:     # int_0^1 ln u/u (e^{iuz}-1) du = -sum (iz)^n/(n! n^2)
        I2 = -ez*_ser(iz, lambda n: 1.0/(factorial(n)*n*n))
    else:
        f2r = lambda u: np.log(u)/u*(np.cos(zeta*u) - 1); f2i = lambda u: np.log(u)/u*np.sin(zeta*u)
        I2 = ez*(Q(f2r, 0, 1) + 1j*Q(f2i, 0, 1))
    if scheme == 'msbar':
        return 1.5*(L + 1)*ez - (L + 1)*I1 - 4*I2 + (1 + sigma)*I3
    return -(L + 1)*I1 - 4*I2 + (1 + sigma)*(I3 - ez)
def Phi_pow(zeta, x0, s, nu):
    az = abs(zeta)
    return s*np.exp(1j*x0*zeta)*(2*np.sqrt(np.pi)/special.gamma(nu))*(s*az/2)**(nu - 0.5)*special.kv(nu - 0.5, s*az)
def methodB(x0, s, nu, ell, sigma, scheme):
    f = lambda z: (G_closed(z, ell, sigma, scheme)*Phi_pow(z, x0, s, nu)).real/(2*np.pi)
    # f(-z) = f(z)^* in the complex sense -> real integrand is even? No: use both half lines explicitly.
    Z = 45.0/s
    tot = 0.0
    for sgn in (+1, -1):
        p = max(1.0, 1.0/(2*nu))                                 # zeta = t^p removes the |zeta|^{2nu-1} endpoint singularity
        z0 = 0.05
        tot += Q(lambda t: f(sgn*t**p)*p*t**(p - 1), 0, z0**(1.0/p))
        for a_, b_ in [(z0, 0.5), (0.5, 2), (2, 6), (6, 15), (15, Z)]:
            tot += Q(lambda z: f(sgn*z), a_, b_)
    return tot

# ---------------------------------------------------------------- run: Method A vs printed kernels
gauss = lambda x0, s: (lambda x: np.exp(-(x - x0)**2/(2*s*s)))
lor = lambda x0, s: (lambda x: 1.0/(1 + ((x - x0)/s)**2))
powl = lambda x0, s, nu: (lambda x: (1 + ((x - x0)/s)**2)**(-nu))
tests = [('gauss(1.0,0.5)', gauss(1.0, 0.5)), ('gauss(0.3,0.4)', gauss(0.3, 0.4)), ('gauss(-0.6,0.8)', gauss(-0.6, 0.8)),
         ('lorentz(0.7,0.6)', lor(0.7, 0.6)), ('lorentz(1.0,1.5)', lor(1.0, 1.5)), ('pow(0.5,0.8,nu=0.35)', powl(0.5, 0.8, 0.35))]
worstA = 0.0
for sigma in ((0, 1) if not os.environ.get('N27_SKIP_A') else ()):
    for scheme in ('msbar', 'ratio'):
        for (nm, phi) in tests:
            for ell in (0.4, -1.1):
                m = mom_pair(phi, ell, sigma, scheme); a = methodA(phi, ell, sigma, scheme)
                d = abs(m - a)/max(1.0, abs(m)); worstA = max(worstA, d)
                rep('A  %-5s sigma=%d %-22s ell=%+.1f: printed kernel = FT of coordinate kernel' % (scheme, sigma, nm, ell), d < 1e-7,
                    '(printed %.12f, FT %.12f, rel %.1e)' % (m, a, d))
print('worst relative deviation, Method A: %.2e' % worstA)

# ---------------------------------------------------------------- Method B (zeta space) for slowly decaying test functions
worstB = 0.0
for sigma in (0, 1):
    for scheme in ('msbar', 'ratio'):
        for (x0, s, nu) in [(0.7, 0.6, 1.0), (0.5, 0.8, 0.35), (1.0, 1.0, 0.2)]:
            ell = 0.4
            phi = powl(x0, s, nu)
            m = mom_pair(phi, ell, sigma, scheme)
            b = methodB(x0, s, nu, ell, sigma, scheme)
            d = abs(m - b)/max(1.0, abs(m)); worstB = max(worstB, d)
            rep('B  %-5s sigma=%d phi=(1+((x-%.1f)/%.1f)^2)^-%.2f (tail |x|^-%.1f): printed kernel = zeta-space FT' % (scheme, sigma, x0, s, nu, 2*nu), d < 1e-6,
                '(printed %.10f, zeta-space %.10f, rel %.1e)' % (m, b, d))
print('worst relative deviation, Method B: %.2e' % worstB)

# ---------------------------------------------------------------- FT[ln zeta^2] identity used in Method A (sanity, closed form Phi of a Lorentzian)
x0, s = 0.3, 0.7
lhs = float(mp.quad(lambda z: mp.log(z**2)*(mp.pi*s*mp.e**(-s*abs(z))*mp.cos(x0*z))/(2*mp.pi), [-mp.inf, 0, mp.inf]))
phiL = lor(x0, s)
rhs = -2*gE*phiL(0.0) - (Q(lambda u: (phiL(u) - phiL(0.0))/abs(u), -1, 0) + Q(lambda u: (phiL(u) - phiL(0.0))/abs(u), 0, 1)
                       + Qinf(lambda u: phiL(u)/u, 1, np.inf) + Qinf(lambda u: phiL(-u)/u, 1, np.inf))
rep('FT[ln zeta^2](u) = -2 gamma_E delta(u) - [1/|u|]_R checked on a Lorentzian', abs(lhs - rhs) < 1e-9, '(%.12f vs %.12f)' % (lhs, rhs))

# ---------------------------------------------------------------- momentum RGE: P^z dC/dP^z from ell = ln(mu^2/(4 p_z^2)), d ell/d ln P^z = -2
xi, ellS = sp.symbols('xi ell', real=True)
g2S = (1 + xi**2)/(1 - xi)*(-ellS + sp.log(xi*(1 - xi))) - xi*(1 + xi)/(1 - xi)
d_inside = sp.simplify(sp.diff(g2S, ellS)*(-2))     # coefficient multiplying [ ]_+ on [0,1]
d_delta = sp.diff(sp.Rational(3, 2)*ellS + sp.Rational(5, 2), ellS)*(-2)
rep('RGE: P^z dC^MSbar/dP^z = a[2((1+xi^2)/(1-xi))_+ - 3 delta(1-xi)] = (alpha_s C_F/pi)[((1+xi^2)/(1-xi))_+ - (3/2) delta(1-xi)]  (RMP eq. (32))',
    sp.simplify(d_inside - 2*(1 + xi**2)/(1 - xi)) == 0 and d_delta == -3, '[inside: %s, delta: %s]' % (d_inside, d_delta))
g2r = (1 + xi**2)/(1 - xi)*(-ellS + sp.log(xi*(1 - xi)) - 1) + 1 + sp.Rational(3, 2)/(1 - xi)
rep('RGE (ratio scheme, for contrast): P^z dC^ratio/dP^z = a 2[(1+xi^2)/(1-xi)]_+ with NO -(3/2) delta term',
    sp.simplify(sp.diff(g2r, ellS)*(-2) - 2*(1 + xi**2)/(1 - xi)) == 0)

print('\nSUMMARY n27: %d/%d PASS' % (sum(RES), len(RES)))
