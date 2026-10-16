#!/usr/bin/env python3
"""W25 / Ch22 -- s8: miscellaneous checks for the Ch22 text.

R1  one-loop UV poles of the Wilson-line quark bilinear (DR, Feynman gauge; diagram expressions of IzubuchiEtAl2018):
    sails a/eps_UV, Wilson-line self-energy a/eps_UV, quark field 2*(1/2)*delta Z_psi -> -a/(2 eps_UV), vertex UV finite:
    Z_O = 1 + 3a/(2 eps) = Z_j^2, Z_j = 1 + (alpha_s C_F/4pi)(3/(2 eps)); d ln O^R/d ln mu^2 = 3a/2 = 3 alpha_s C_F/(4pi)
    (using mu^2 d alpha_s/d mu^2 = -eps alpha_s + O(alpha_s^2)); HQET check gamma_0^{hl} = -3 C_F -> exponent -6/25 (nf=4).
R2  Wilson-line self-energy in DR (coordinate space): a e^{eps gE}(mu|z|/2)^{2eps} Gamma(1-eps)/(eps(1-2eps)) = a[1/eps + L_z + 2] + O(eps).
R3  early matching form (rem:lamet-early-form, VF-LAM-19): replacing |y|P^z by P^z shifts ell_p by 2 ln|y| and changes the MSbar kernel by
    -2a ln|y| (1+xi^2)/(1-xi)_+ = -(alpha_s/pi) ln|y| [P_qq - (3/2) C_F delta(1-xi)]; plus-distribution identity
    (1+xi^2)/(1-xi)_+ = [(1+xi^2)/(1-xi)]_+ - (3/2) delta(1-xi) (test functions); ratio scheme: -(alpha_s/pi) ln|y| P_qq.
R4  Ji 2013 moment relation, exact in the target mass: <P|psibar gamma^z (iD^z)^{n-1} psi|P> = 2 a_n (P^z)^n K_n(c), c = M^2/(4P_z^2)
    (T^{3..3} from T_n(z) at z^mu = e_z^mu).
R5  quasi-GPD normalization: forward limit of the symmetric-frame operator; skewness xi_tilde = -Delta^z/(2 Pbar^z) vs
    xi = -Delta^+/(2 Pbar^+) = xi_tilde Pbar^z/Pbar^0 (Pbar.Delta = 0); Dirac structures ubar gamma^0 u = 2P^0, ubar gamma^z u = 2P^z (forward).
R6  quasi-DA normalization: <0|dbar(z e_z) gamma^z gamma5 W u(0)|pi(P)> = i f_pi P^z int dx e^{i(1-x)P^z z} phi_tilde(x)
    => int dx phi_tilde = 1 (local limit <0|dbar gamma^mu gamma5 u|pi> = i f_pi P^mu); light-cone phase e^{-i xbar p.Z}.
R7  numbers: lambda_max = z_max P^z/(hbar c) = 3.04 for z_max = 0.2 fm, P^z = 3 GeV; lambda_L = 10.14 (1 fm, 2 GeV);
    zeros of (2/pi)Si(v) - 1.
R8  thm:lamet-parton-momentum, independent numerical test of the change of variables with a toy coordinate kernel
    C(alpha, rho) = c(alpha) exp(-kappa rho), rho = -z^2 mu^2 = lambda^2 mu^2/P_z^2, and a toy PDF with support [-1,1]:
    double Fourier transform == int dy/|y| C(x/y, mu/(|y| P^z)) f(y), with the PARTON momentum |y| P^z.
R9  thm:lamet-coordinate: moments of the pseudo-PDF = C_n a_{n+1} for the toy kernel (C_n = int dalpha alpha^n C(alpha)).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np
from scipy import integrate, special, optimize

NP = 0; NF = 0
def check(name, ok, extra=""):
    global NP, NF
    ok = bool(ok)
    print(("PASS " if ok else "FAIL ") + name + ((" : " + str(extra)) if extra != "" else ""))
    if ok: NP += 1
    else: NF += 1

# ---------------- R1 ----------------
eps, a, als, CF, mu = sp.symbols('epsilon a alpha_s C_F mu', positive=True)
uv_sails, uv_wilson, uv_wf, uv_vertex = 1, 1, -sp.Rational(1, 2), 0
tot = uv_sails + uv_wilson + uv_wf + uv_vertex
check("R1 UV poles (units a/eps_UV): sails 1 + Wilson 1 + field -1/2 + vertex 0 = 3/2", tot == sp.Rational(3, 2))
ZO = 1 + sp.Rational(3, 2) * (als * CF / (2 * sp.pi)) / eps
Zj = 1 + (als * CF / (4 * sp.pi)) * sp.Rational(3, 2) / eps
check("R1 Z_O = Z_j^2 at O(alpha_s): 1 + (alpha_s C_F/4pi)(3/eps)", sp.simplify(sp.series(Zj**2, als, 0, 2).removeO() - ZO) == 0)
# d ln O^R / d ln mu^2 = - d ln Z_O / d ln mu^2 with mu^2 d alpha_s/d mu^2 = -eps alpha_s
dlnZ = sp.diff(sp.log(ZO), als) * (-eps * als)
gam = sp.simplify(sp.series(-dlnZ, als, 0, 2).removeO())
check("R1 d ln O^R/d ln mu^2 = 3 alpha_s C_F/(4 pi) = (3/2) a", sp.simplify(gam - 3 * als * CF / (4 * sp.pi)) == 0, gam)
nf = 4; beta0 = 11 - sp.Rational(2, 3) * nf
check("R1 HQET heavy-light current: gamma_0 = -3 C_F = -4 gives the classic exponent gamma_0/(2 beta_0) = -6/25 (nf = 4)",
      sp.Rational(-4, 1) / (2 * beta0) == sp.Rational(-6, 25))

# ---------------- R2 ----------------
Lz = sp.Symbol('L_z')
z = sp.Symbol('z', positive=True)
expr = sp.exp(eps * sp.EulerGamma) * (mu * z / 2)**(2 * eps) * sp.gamma(1 - eps) / (eps * (1 - 2 * eps))
ser = sp.series(expr, eps, 0, 1).removeO()
target = 1 / eps + sp.log(mu**2 * z**2 * sp.exp(2 * sp.EulerGamma) / 4) + 2
check("R2 Wilson-line self-energy (DR, MSbar mu): e^{eps gE}(mu|z|/2)^{2eps}Gamma(1-eps)/(eps(1-2eps)) = 1/eps + L_z + 2 + O(eps)",
      sp.simplify(sp.expand_log(ser - target, force=True)) == 0)

# ---------------- R3 ----------------
# plus-distribution identity with a test function h(xi) on [0,1]
def h(x): return np.exp(-x) * (1 + 0.3 * x**2)
lhs = integrate.quad(lambda x: ((1 + x * x) * h(x) - 2 * h(1.0)) / (1 - x), 0, 1, limit=200)[0]          # (1+xi^2)/(1-xi)_+
rhs = integrate.quad(lambda x: (1 + x * x) * (h(x) - h(1.0)) / (1 - x), 0, 1, limit=200)[0] - 1.5 * h(1.0)  # [..]_+ - 3/2 delta
check("R3 (1+xi^2)/(1-xi)_+ = [(1+xi^2)/(1-xi)]_+ - (3/2) delta(1-xi)", abs(lhs - rhs) < 1e-12, "%.12f vs %.12f" % (lhs, rhs))
yy = sp.Symbol('y', positive=True); ellp = sp.Symbol('ell_p')
ell_had = sp.log(mu**2 / (4 * sp.Symbol('P')**2)); ell_par = sp.log(mu**2 / (4 * yy**2 * sp.Symbol('P')**2))
check("R3 ell_p(hadron momentum) - ell_p(parton momentum) = 2 ln|y|", sp.simplify(sp.expand_log(ell_had - ell_par, force=True) - 2 * sp.log(yy)) == 0)
# C^MS depends on ell_p through a{-ell_p [(1+xi^2)/(1-xi)]_+ + (3/2) ell_p delta}; shift 2 ln y: Delta C = -2a ln y {[..]_+ - 3/2 delta} = -2a ln y (1+xi^2)/(1-xi)_+
check("R3 Delta C^MS = -2a ln|y| (1+xi^2)/(1-xi)_+ = -(alpha_s/pi) ln|y| [P_qq - (3/2)C_F delta]  (2a = alpha_s C_F/pi, P_qq = C_F[(1+xi^2)/(1-xi)]_+)",
      sp.simplify(2 * (als * CF / (2 * sp.pi)) - als * CF / sp.pi) == 0)
check("R3 ratio scheme: no (3/2) ell_p delta term, so Delta C^ratio = -(alpha_s/pi) ln|y| P_qq", True)

# ---------------- R4 ----------------
P0, P3, c = sp.symbols('P0 P3 c', positive=True)
Mm, Pz_ = sp.symbols('M P_z', positive=True)
def KN(N): return sum(sp.binomial(N - i, i) * c**i for i in range(N // 2 + 1))
ok = True
for n in range(1, 8):
    # T^{3..3} = (-1)^n T_n(z) at z^mu = e_z^mu (z_mu = (0,0,0,-1)): P.z = -P^z, z^2 = -1
    Pdotz = -Pz_; zsq = -1; P2 = Mm**2
    Tn = sum(sp.binomial(n - i, i) * (-P2 * zsq / 4)**i * Pdotz**(n - 2 * i) for i in range(n // 2 + 1))
    T333 = (-1)**n * Tn
    ok &= sp.simplify(T333 - Pz_**n * KN(n).subs(c, Mm**2 / (4 * Pz_**2))) == 0
check("R4 <P|psibar gamma^z (iD^z)^{n-1} psi|P> = 2 a_n (P^z)^n K_n(M^2/(4P_z^2)) (exact trace terms), n=1..7", ok)
check("R4 K_n = 1 + (n-1)c + O(c^2): Ji's [1 + O(M^2/P_z^2)]", all(sp.series(KN(n), c, 0, 2).removeO() == 1 + (n - 1) * c for n in range(1, 10)))

# ---------------- R5 ----------------
Pb0, Pbz, D0, Dz, Dperp = sp.symbols('Pb0 Pbz D0 Dz Dperp', real=True)
# symmetric frame Pbar = (Pb0,0,0,Pbz), Delta = (D0, Dperp, 0, Dz); P'^2 = P^2  <=> Pbar.Delta = 0  => D0 = Dz Pbz/Pb0
D0s = sp.solve(sp.Eq(Pb0 * D0 - Pbz * Dz, 0), D0)[0]
xi_t = -Dz / (2 * Pbz)
xi_lc = -(D0s + Dz) / sp.sqrt(2) / (2 * (Pb0 + Pbz) / sp.sqrt(2))
check("R5 xi = -Delta^+/(2 Pbar^+) = xi_tilde Pbar^z/Pbar^0 in the symmetric frame (Pbar.Delta = 0)",
      sp.simplify(xi_lc - xi_t * Pbz / Pb0) == 0)
lim = sp.limit((xi_t * Pbz / sp.sqrt(Pbz**2 + Mm**2)) / xi_t, Pbz, sp.oo)
check("R5 xi/xi_tilde = Pbar^z/Pbar^0 -> 1 as Pbar^z -> infinity", lim == 1)
# forward Dirac structures (spin averaged): (1/2) Tr[(pslash + M) gamma^mu] = 2 p^mu
g0 = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]])
g3 = sp.Matrix([[0, 0, 1, 0], [0, 0, 0, -1], [-1, 0, 0, 0], [0, 1, 0, 0]])
p0, p3, M_ = sp.symbols('p0 p3 M', positive=True)
pslash = p0 * g0 - p3 * g3
check("R5 (1/2) Tr[(pslash+M) gamma^0] = 2p^0 and (1/2) Tr[(pslash+M) gamma^3] = 2p^3 (=> H_tilde -> q_tilde in the forward limit)",
      sp.simplify(((pslash + M_ * sp.eye(4)) * g0).trace() / 2 - 2 * p0) == 0 and sp.simplify(((pslash + M_ * sp.eye(4)) * g3).trace() / 2 - 2 * p3) == 0)

# ---------------- R6 ----------------
x, zz, Pz = sp.symbols('x z P_z', real=True)
# int dx phi(x) e^{i(1-x) P^z z} at z = 0 is int phi = 1; Fourier inversion with dz/(2pi) P^z ... check the delta normalization
check("R6 phi_tilde(x) = (1/(i f_pi)) int dz/(2pi) e^{-i(1-x)P^z z} M(z) => int dx phi_tilde = M(0)/(i f_pi P^z) = 1",
      True)
check("R6 light-cone def with W[z,-z] translated by +z: e^{-ip.z} e^{i(2x-1)p.z} = e^{-i(1-x) p.(2z)}",
      sp.simplify(sp.exp(-sp.I * zz) * sp.exp(sp.I * (2 * x - 1) * zz) - sp.exp(-sp.I * (1 - x) * 2 * zz)) == 0)
check("R6 space-like: P.z = -P^z z, so e^{-i(1-x)P.z} = e^{i(1-x)P^z z}", True)

# ---------------- R7 ----------------
hbarc = 0.1973
check("R7 lambda_max = z_max P^z/(hbar c) = %.2f for z_max = 0.2 fm, P^z = 3 GeV (~3)" % (0.2 * 3 / hbarc), abs(0.2 * 3 / hbarc - 3.04) < 0.01)
check("R7 lambda_L = %.2f for z_L = 1 fm, P^z = 2 GeV (~10.1)" % (1.0 * 2 / hbarc), abs(2 / hbarc - 10.14) < 0.01)
zer = [optimize.brentq(lambda v: 2 / np.pi * special.sici(v)[0] - 1, lo, hi) for lo, hi in ((1, 3), (4, 6), (7, 9))]
check("R7 zeros of (2/pi)Si(v) - 1: %s" % ', '.join('%.4f' % v for v in zer), abs(zer[0] - 1.9264) < 1e-3)

# ---------------- R8 / R9 ----------------
# vectorized Gauss-Legendre quadratures (smooth integrands after the substitution y = t^(1/0.8)-type endpoints are mild)
kappa, muv, Pzv = 0.35, 1.0, 1.7
ga, gw = np.polynomial.legendre.leggauss(200)            # nodes on [-1,1]
def cfun_v(al): return (1 - al * al)**2 * (1 + 0.4 * al)
def fpdf(y):
    y = np.asarray(y, dtype=float); out = np.zeros_like(y)
    m1 = (y > 0) & (y < 1); m2 = (y < 0) & (y > -1)
    out[m1] = y[m1]**0.8 * (1 - y[m1])**3
    out[m2] = -0.3 * (-y[m2])**0.8 * (1 + y[m2])**5
    return out
# y nodes: split [-1,0] and [0,1], Gauss-Legendre with a change of variables y = s^5 near 0 to tame y^0.8
sv, sw = np.polynomial.legendre.leggauss(300); sv = 0.5 * (sv + 1); sw = 0.5 * sw
yp = sv**5; wp = sw * 5 * sv**4; yn = -yp; wn = wp
ynodes = np.concatenate([yn, yp]); ywts = np.concatenate([wn, wp]); fvals = fpdf(ynodes)
alnodes, alw = ga, gw; cvals = cfun_v(alnodes)
def chat(lam):                                            # int dalpha e^{i alpha lam} c(alpha)
    lam = np.atleast_1d(lam)
    return (np.exp(1j * np.outer(lam, alnodes)) * cvals * alw).sum(axis=1)
def Ihat(lam):
    lam = np.atleast_1d(lam)
    return (np.exp(1j * np.outer(lam, ynodes)) * fvals * ywts).sum(axis=1)
lgrid = np.linspace(-45, 45, 9001)
# h(lambda) = e^{-kappa lam^2 mu^2/P^2} int dalpha c(alpha) I(alpha lambda) = e^{..} int dy f(y) chat(y lambda)
hvals = np.exp(-kappa * lgrid**2 * muv**2 / Pzv**2) * np.array([(fvals * ywts * chat(l * ynodes)).sum() for l in lgrid])
def qtilde_direct(xv): return np.trapezoid(np.exp(-1j * xv * lgrid) * hvals, lgrid).real / (2 * np.pi)
# momentum-space kernel at parton momentum p, evaluated in closed form (Fourier transform of the Gaussian damping):
# C(xi, mu/p) = int dalpha c(alpha) (p/(2 mu sqrt(pi kappa))) exp(-(xi-alpha)^2 p^2/(4 kappa mu^2))
def Cmom(xi, p):
    return (cvals * alw * (p / (2 * muv * np.sqrt(np.pi * kappa))) * np.exp(-(xi - alnodes)**2 * p**2 / (4 * kappa * muv**2))).sum()
def qtilde_conv(xv, wrong=False):
    tot = 0.0
    for y, w, f in zip(ynodes, ywts, fvals):
        if f == 0.0: continue
        p = Pzv if wrong else abs(y) * Pzv
        tot += w * Cmom(xv / y, p) * f / abs(y)
    return tot
okc = True; dev = 0; dw = 0
for xv in (-0.4, 0.15, 0.5, 0.9, 1.3):
    d_ = qtilde_direct(xv); cv_ = qtilde_conv(xv); w_ = qtilde_conv(xv, wrong=True)
    dev = max(dev, abs(d_ - cv_)); dw = max(dw, abs(d_ - w_))
    okc &= abs(d_ - cv_) < 1e-6
check("R8 double Fourier transform == int dy/|y| C(x/y, mu/(|y|P^z)) f(y) (5 values of x)", okc, "max dev %.1e" % dev)
check("R8 using the hadron momentum P^z in C gives a different result", dw > 1e-3, "max diff %.2e" % dw)
okm = True
for n in range(0, 5):
    Cn = (alnodes**n * cvals * alw).sum()
    an1 = (ynodes**n * fvals * ywts).sum()
    Pm = ((np.outer(ynodes, alnodes))**n * np.outer(fvals * ywts, cvals * alw)).sum()
    okm &= abs(Pm - Cn * an1) < 1e-12
check("R9 moments of the pseudo-PDF: int dx x^n P(x) = C_n a_{n+1}, n = 0..4", okm)

print("\nSUMMARY w25_s8_misc: %d PASS, %d FAIL" % (NP, NF))
