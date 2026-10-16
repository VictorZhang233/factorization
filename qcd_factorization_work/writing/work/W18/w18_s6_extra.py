# -*- coding: utf-8 -*-
"""
w18_s6_extra.py -- additional checks for Ch15 (SCET), written in the resumed W18 session.

 R1  eta-regulated one-loop TMD soft function (quark Wilson lines) in p_T space:
     S^(1)(p) = 2 g^2 C_F nu^eta I(eta) / ((2pi)^3 p^2 |p|^eta),  I(eta) = int dy |2 sinh y|^{-eta};
     nu d/dnu S^(1) -> (4 alpha_s C_F/pi) * 1/(2 pi p^2)  for p != 0  (= (4 alpha_s C_F/pi) L_0, CJNR eq. (5.62)).
 R2  the same in b space with the (2-2eps)-dimensional Fourier transform, MSbar:
     nu d/dnu S~^(1) = (2 alpha_s C_F/pi) (-1/eps - L_b) + O(eps),  L_b = ln(mu^2 b^2 e^{2 gamma_E}/4).
 R3  numerical check of the n-dimensional Fourier formula used in R2.
 R4  kernel relations at one loop: K~ = gamma_nu^S/2 = -F_qqbar = -2 D and their mu derivatives
     (BN eqs. (16), (40); EIS eqs. (5.14), (5.15)).
 Z   thrust zero-bin: integrating nbar.k with delta(nbar.k n.k - k_T^2) leaves (1/n.k) int d^{2-2eps}k_perp / k_T^2
     (scaleless) and the a-scaling degree is -eps.
 G   Glauber potential: P_perp^2 -> q_perp^2 = -q_T^2 (metric (+,-,-,-)); the L_G coefficient
     8 pi alpha_s / P_perp^2 reproduces i M = -i 8 pi alpha_s/q_T^2 [..][..].
 B   RS box/cross box with one regulator factor |2k^z|^{-eta} per Glauber potential (two factors):
     cross box vanishes (poles on one side), box -> pure phase (principal value part -> 0 as eta -> 0).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
import mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w18_common import Check

C = Check('W18 s6: rapidity anomalous dimension (p and b space), Fourier formula, kernels, zero-bin, Glauber sign, box')

eta, eps = sp.symbols('eta epsilon')
p, b, mu, nu, aS, CF = sp.symbols('p b mu nu alpha_s C_F', positive=True)
gE = sp.EulerGamma

# ------------------------------------------------------------------ R1: p_T space
I_eta = 2**(-eta) * sp.gamma(eta / 2) * sp.gamma(sp.Rational(1, 2) - eta / 2) / sp.sqrt(sp.pi)
# numerical check of the rapidity integral I(eta) = int_{-inf}^{inf} dy |2 sinh y|^{-eta}
mp.mp.dps = 40
for ev in (mp.mpf('0.3'), mp.mpf('0.55')):
    # substitution y = u^(1/(1-ev)) removes the integrable endpoint singularity y^(-ev) at y = 0
    q = 1 / (1 - ev)
    num = 2 * (mp.quad(lambda u: (2 * mp.sinh(u**q))**(-ev) * q * u**(q - 1), [0, 1]) +
               mp.quad(lambda y: (2 * mp.sinh(y))**(-ev), [1, mp.inf]))
    ana = 2**(-ev) * mp.gamma(ev / 2) * mp.gamma(mp.mpf(1) / 2 - ev / 2) / mp.sqrt(mp.pi)
    C(f'R1a I(eta) = int dy |2 sinh y|^(-eta) = 2^(-eta) Gamma(eta/2) Gamma(1/2-eta/2)/sqrt(pi) at eta={mp.nstr(ev, 3)}',
      abs(num - ana) < mp.mpf('1e-25') * abs(ana), f'{mp.nstr(num, 20)} vs {mp.nstr(ana, 20)}')
mp.mp.dps = 15
ser = sp.series(I_eta, eta, 0, 2).removeO()
C('R1b I(eta) = 2/eta + 0 + O(eta)  (both rapidity ends regulated by one pole)',
  sp.simplify(sp.expand(ser) - (2 / eta + sp.pi**2 * eta / 6)) == 0, sp.expand(ser))
g2 = 4 * sp.pi * aS
S1p = 2 * g2 * CF * nu**eta * I_eta / ((2 * sp.pi)**3 * p**2 * p**eta)   # eps -> 0, delta^(2)-normalized density
dS1p = sp.limit(sp.simplify(nu * sp.diff(S1p, nu)), eta, 0)
C('R1c nu d/dnu S^(1)(p) -> (4 alpha_s C_F/pi) * 1/(2 pi p^2)  (p != 0)',
  sp.simplify(dS1p - (4 * aS * CF / sp.pi) / (2 * sp.pi * p**2)) == 0, sp.simplify(dS1p))

# ------------------------------------------------------------------ R2: b space, d-2 = 2-2eps dimensions
nT = 2 - 2 * eps
aexp = 1 + eta / 2
FT = sp.pi**(nT / 2) * 2**(nT - 2 * aexp) * sp.gamma(nT / 2 - aexp) / sp.gamma(aexp) * (b**2)**(aexp - nT / 2)
mu0sq = mu**2 * sp.exp(gE) / (4 * sp.pi)        # MSbar: mu0^2 -> mu^2 e^{gamma_E}/(4 pi)
S1b = 2 * g2 * CF * mu0sq**eps * nu**eta * I_eta / (2 * sp.pi)**(3 - 2 * eps) * FT
dS1b = nu * sp.diff(S1b, nu)                      # = eta * S1b
dS1b_eta0 = sp.limit(sp.simplify(dS1b / (aS * CF)), eta, 0)   # finite as eta -> 0
ser_b = sp.series(dS1b_eta0, eps, 0, 1).removeO()
Lb = sp.log(mu**2 * b**2 * sp.exp(2 * gE) / 4)
target = (2 / sp.pi) * (-1 / eps - Lb)
C('R2 b space, MSbar: nu d/dnu S~^(1) = (2 alpha_s C_F/pi)(-1/eps - L_b) + O(eps)',
  sp.simplify(sp.expand(sp.expand_log(ser_b - target, force=True))) == 0, sp.simplify(ser_b))
gamma_nu_S = -(2 * aS * CF / sp.pi) * Lb          # after removing the pole
Ktilde = -(aS * CF / sp.pi) * Lb                  # VF-TMD-1 (WRITER_SPEC_v2 Sec. 3 row 29)
C('R2b gamma_nu^S = -(2 alpha_s C_F/pi) L_b = 2 K~  (K~ = -(alpha_s C_F/pi) L_b)',
  sp.simplify(gamma_nu_S - 2 * Ktilde) == 0)

# ------------------------------------------------------------------ R3: numerical check of the Fourier formula
def ft_formula(n, a, bb):
    return mp.pi**(n / 2) * 2**(n - 2 * a) * mp.gamma(n / 2 - a) / mp.gamma(a) * (bb**2)**(a - n / 2)

def ft_schwinger(n, a, bb):
    # (p^2)^(-a) = (1/Gamma(a)) int_0^inf ds s^(a-1) e^(-s p^2);  n-dim FT of e^(-s p^2) = (pi/s)^(n/2) e^(-b^2/(4s))
    # => FT = pi^(n/2)/Gamma(a) int_0^inf ds s^(a-1-n/2) e^(-b^2/(4s))   (convergent for 0 < a < n/2)
    # substitute s = 1/t: int_0^inf ds s^(a-1-n/2) e^(-b^2/(4s)) = int_0^inf dt t^(n/2-a-1) e^(-b^2 t/4)
    # and u = t^(n/2-a) removes the endpoint singularity: = q int_0^inf du exp(-b^2 u^q/4), q = 1/(n/2-a)
    q = 1 / (n / 2 - a)
    return mp.pi**(n / 2) / mp.gamma(a) * q * mp.quad(lambda u: mp.exp(-bb**2 * u**q / 4), [0, 1, mp.inf])

def gauss_ft_numeric(n, s, bb):
    # check of the Gaussian step in n = 2 by a direct radial Bessel integral: 2 pi int_0^inf dp p J0(p b) e^(-s p^2)
    return 2 * mp.pi * mp.quad(lambda pp: pp * mp.besselj(0, pp * bb) * mp.exp(-s * pp**2), [0, mp.inf])

mp.mp.dps = 30
gs = gauss_ft_numeric(2, mp.mpf('0.6'), mp.mpf('1.3'))
C('R3a Gaussian step in n=2: 2 pi int dp p J0(pb) e^(-s p^2) = (pi/s) e^(-b^2/(4s))',
  abs(gs - mp.pi / mp.mpf('0.6') * mp.exp(-mp.mpf('1.3')**2 / (4 * mp.mpf('0.6')))) < mp.mpf('1e-20'), mp.nstr(gs, 15))
for (n_, a_, b_) in ((2, 0.7, 1.3), (1.8, 0.65, 0.8), (2.2, 0.8, 2.0), (2.0, 0.35, 0.5)):
    fA = ft_formula(mp.mpf(n_), mp.mpf(a_), mp.mpf(b_))
    fN = ft_schwinger(mp.mpf(n_), mp.mpf(a_), mp.mpf(b_))
    C(f'R3b n-dim Fourier transform of (p^2)^(-a): closed form = Schwinger-parameter integral (n={n_}, a={a_}, b={b_})',
      abs(fA - fN) < mp.mpf('1e-20') * abs(fA), f'{mp.nstr(fA, 16)} vs {mp.nstr(fN, 16)}')
mp.mp.dps = 15

# ------------------------------------------------------------------ R4: kernel relations
F_BN = (CF * aS / sp.pi) * Lb                      # BN eq. (40), L_perp = L_b
D_EIS = (aS / (4 * sp.pi)) * 2 * CF * Lb           # EIS eq. (5.15): d_1 = 2 C_F L_T, L_T = L_b
C('R4a one loop: K~ = gamma_nu^S/2 = -F_qqbar = -2D',
  all(sp.simplify(x) == 0 for x in (Ktilde - gamma_nu_S / 2, Ktilde + F_BN, Ktilde + 2 * D_EIS)))
Gcusp = aS * CF / sp.pi                            # one loop, Gamma_0 = 4 C_F
dlnmu = lambda f: sp.diff(f, mu) * mu
C('R4b dK~/dln mu = -2 Gamma_cusp, dF/dln mu = +2 Gamma_cusp (BN (16)), dD/dln mu = Gamma_cusp (EIS (5.14))',
  all(sp.simplify(x) == 0 for x in (dlnmu(Ktilde) + 2 * Gcusp, dlnmu(F_BN) - 2 * Gcusp, dlnmu(D_EIS) - Gcusp)))
# Q^2 dependence: BN product ~ (b^2 Q^2/b0^2)^(-F)  =>  d ln/d ln Q^2 = -F ; EIS: each TMD -D, two TMDs -2D;
# Collins: f_A f_B with zeta_A = zeta_B = Q^2, d ln f/d ln zeta = K~/2 => d ln(f f)/d ln Q^2 = K~
Q2 = sp.symbols('Q2', positive=True)
bn_prod = (b**2 * Q2 * sp.exp(2 * gE) / 4)**(-F_BN)
C('R4c Q^2 slopes: BN -F, EIS -2D, Collins K~ coincide', sp.simplify(
  sp.diff(sp.log(bn_prod), Q2) * Q2 - Ktilde) == 0 and sp.simplify(-2 * D_EIS - Ktilde) == 0)

# ------------------------------------------------------------------ Z: thrust zero-bin
nbk, kap, kT, a_ = sp.symbols('nbk kappa k_T a', positive=True)
# int d(nbar.k) delta(kappa nbar.k - kT^2) / (kappa nbar.k) = [1/(kappa nbk)]_{nbk = kT^2/kappa} / kappa
red = (1 / (kap * nbk)).subs(nbk, kT**2 / kap) / kap
C('Z1 integrating nbar.k: zero-bin -> (1/n.k) * 1/k_T^2  (then int d^{2-2eps}k_perp k_T^-2 = 0, scaleless)',
  sp.simplify(red - 1 / (kap * kT**2)) == 0, sp.simplify(red))
# scaling degree: delta(k^2) -> a^-1, 1/nbar.k -> a^-1, measure d nbar.k d^{2-2eps} k_perp -> a^{1 + (2-2eps)/2}
deg = -1 - 1 + 1 + (2 - 2 * eps) / 2
C('Z2 a-scaling degree of the zero-bin integral = -eps (homogeneous, hence zero in DR)', sp.simplify(deg + eps) == 0, deg)

# ------------------------------------------------------------------ G: Glauber potential sign
qT = 0.37
qperp = np.array([0.0, qT * np.cos(0.4), qT * np.sin(0.4), 0.0])
qperp2 = qperp[0]**2 - qperp[1]**2 - qperp[2]**2 - qperp[3]**2
C('G1 P_perp^2 eigenvalue q_perp^2 = -q_T^2 (metric +,-,-,-)', abs(qperp2 + qT**2) < 1e-15, qperp2)
# L_G = O_n (1/P^2) [8 pi as P^2] (1/P^2) O_nbar  ->  coefficient 8 pi as/q_perp^2 = -8 pi as/q_T^2;
# vertex = i * L_G  ->  i M = -i 8 pi as/q_T^2 [..][..], the tree amplitude checked in w18_s5 (D1)
coef = 8 * np.pi * 0.2 / qperp2
C('G2 i*L_G coefficient = -i 8 pi alpha_s/q_T^2, matching the QCD tree amplitude of w18_s5 D1',
  abs(coef + 8 * np.pi * 0.2 / qT**2) < 1e-12, coef)

# ------------------------------------------------------------------ B: RS box with two regulator factors
# (B0) k^0 integrals at fixed k^z (finite +i delta): crossed box has both poles below the real axis -> 0;
#      box has the poles on opposite sides -> -2 pi i/(sum of the two denominators' constants)
dl = mp.mpf('0.01')
A1, A2 = mp.mpf('1.3'), mp.mpf('-0.4')
cross = mp.quad(lambda k0: 1 / ((k0 - A1 + 1j * dl) * (k0 - A2 + 1j * dl)), [-mp.inf, A2, A1, mp.inf])
C('B0a crossed box: int dk^0 1/[(k^0-A1+i0)(k^0-A2+i0)] = 0 (both poles in the lower half plane)',
  abs(cross) < 1e-9, mp.nstr(cross, 6))
box0 = mp.quad(lambda k0: 1 / ((k0 - A1 + 1j * dl) * (-k0 + A2 + 1j * dl)), [-mp.inf, A2, A1, mp.inf])
box0_ana = -2j * mp.pi / (A2 - A1 + 2j * dl)
C('B0b box: int dk^0 1/[(k^0-A1+i0)(-k^0+A2+i0)] = -2 pi i/(A2-A1+2i0) (poles on opposite sides)',
  abs(box0 - box0_ana) < 1e-9 * abs(box0_ana), f'{mp.nstr(box0, 8)} vs {mp.nstr(box0_ana, 8)}')
# (B1) remaining k^z integral with two regulator factors |k^z|^{-eta} (one per Glauber potential):
#      int dk |k|^{-2eta}/(-2k-2Delta+i0) = PV part + delta part;  PV part = -(pi/2)|Delta|^{-2eta} tan(pi eta) -> 0
mp.mp.dps = 30
for etav in (mp.mpf('0.05'), mp.mpf('0.02'), mp.mpf('0.005')):
    Dl = mp.mpf('0.7')
    # PV int_{-inf}^{inf} dk |k|^{-2eta}/(-2k-2Dl) = int_0^inf k^{-2eta} [1/(2k-2Dl) - 1/(2k+2Dl)] dk  (PV at k = Dl)
    sing = mp.quad(lambda k: (k**(-2 * etav) - Dl**(-2 * etav)) / (2 * k - 2 * Dl), [0, Dl, 2 * Dl])  # pole subtracted
    reg = mp.quad(lambda k: -k**(-2 * etav) / (2 * k + 2 * Dl), [0, 2 * Dl])
    tail = mp.quad(lambda k: k**(-2 * etav) * (1 / (2 * k - 2 * Dl) - 1 / (2 * k + 2 * Dl)), [2 * Dl, mp.inf])
    pv_num = sing + reg + tail          # Dl^{-2eta} PV int_0^{2Dl} dk/(2k-2Dl) = 0 by symmetry
    pv_ana = -(mp.pi / 2) * Dl**(-2 * etav) * mp.tan(mp.pi * etav)
    C(f'B1 PV part of the doubly regulated box k^z integral = -(pi/2)|Delta|^(-2eta) tan(pi eta) -> 0 (eta={mp.nstr(etav, 3)})',
      abs(pv_num - pv_ana) < mp.mpf('1e-18'), f'{mp.nstr(pv_num, 14)} vs {mp.nstr(pv_ana, 14)}')
mp.mp.dps = 15
# (B2) delta part: 1/(x+i0) -> -i pi delta(x), x = -2k-2Delta: -i pi |Delta|^{-2eta}/2 -> -i pi/2 (finite imaginary)
etav = mp.mpf('1e-6')
delta_part = -1j * mp.pi * mp.mpf('0.7')**(-2 * etav) / 2
C('B2 delta-function part -> -i pi/2 as eta -> 0: the regulated box is a pure (imaginary) phase factor',
  abs(delta_part + 1j * mp.pi / 2) < 1e-5, mp.nstr(delta_part, 10))

ok = C.summary()
sys.exit(0 if ok else 1)
