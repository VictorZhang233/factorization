# -*- coding: utf-8 -*-
"""
s7_dvcs.py -- item (3): LO handbag amplitude for (doubly) virtual Compton scattering gamma*(q) N(p) -> gamma(q') N(p').

  T^{mu nu} = i int d^4z e^{i q'.z} <p'| T{J^mu(z) J^nu(0)} |p>      (J^nu absorbs q, J^mu emits q')
In the forward limit this is the DIS Compton amplitude with Im T^{mu nu} = 2 pi W^{mu nu}, W as in CONTEXT.md / c_dis.
Leading-twist correlator (Fierz, s1):
  <p'|qbar_a(-w/2) q_b(w/2)|p> -> int dx e^{-i x Pbar.w} (1/4)[ g^- calH(x) + g5 g^- calHt(x) ]_{ba},
  calH = H ubar g^+ u + E ubar i sigma^{+a} Delta_a/(2M) u = 2 Pbar^+ F^q ,  calHt = Ht ubar g^+ g5 u + ... = 2 Pbar^+ Ft^q.
Hence  T^{mu nu} = i sum_q e_q^2 int dx Tr{[g^mu S(k'+q') g^nu + g^nu S(k-q') g^mu](1/4)[g^- calH + g5 g^- calHt]}
with k = (x+eta) Pbar, k' = (x-eta) Pbar (plus components).
Kinematics: Pbar = (P,0,0_T); Delta^+ = -2 eta P; qbar = (q+q')/2 = (-xi' P, qbar^-, 0_T);
  eta = skewness, xi' = -qbar^2/(2 Pbar.qbar) = generalized Bjorken variable. DVCS: xi' = eta = xi; DIS: eta = 0, xi' = x_B.
Transverse tensors: g_perp^{ij} = g^{ij}, eps_perp^{mu nu} = eps^{mu nu rho sigma} nbar_rho n_sigma (nbar along +z, n along -z),
  so eps_perp^{12} = +1 with eps^{0123} = +1.
Run:  python3 -I s7_dvcs.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
import numpy as np
import mpmath as mp

ck = Checker('s7_dvcs')
x, eta, xp, P, qm = sp.symbols('x eta xi_p P q_m', real=True)

nbar = lc(1, 0)
nvec = lc(0, 1)
low = lambda v: [METRIC[i] * v[i] for i in range(4)]
epsperp12 = sum(levi(1, 2, r_, s_) * low(nbar)[r_] * low(nvec)[s_] for r_ in range(4) for s_ in range(4))
ck.check('eps_perp^{12} = eps^{12 rho sigma} nbar_rho n_sigma = +1  (eps^{0123}=+1)', sp.simplify(epsperp12 - 1) == 0)

k = lc((x + eta) * P, 0)
kp = lc((x - eta) * P, 0)
qbar = lc(-xp * P, qm)
Delta = lc(-2 * eta * P, 0)
q = add(qbar, scal(sp.Rational(1, 2), Delta))
qq = sub(qbar, scal(sp.Rational(1, 2), Delta))
ls = add(kp, qq)
lu = sub(k, qq)
ck.zero('s-channel virtuality (k\'+q\')^2 = 2 (x - xi\') P qbar^-', dot(ls, ls) - 2 * (x - xp) * P * qm)
ck.zero('u-channel virtuality (k-q\')^2 = -2 (x + xi\') P qbar^-', dot(lu, lu) + 2 * (x + xp) * P * qm)
ck.zero('xi\' = -qbar^2/(2 Pbar.qbar)', sp.simplify(-dot(qbar, qbar) / (2 * dot(lc(P, 0), qbar)) - xp))
ck.zero('q^2 = -2(xi\'+eta) P qbar^-, q\'^2 = -2(xi\'-eta) P qbar^-  (DVCS q\'^2 = 0 <=> xi\' = eta)',
        (dot(q, q) + 2 * (xp + eta) * P * qm) ** 2 + (dot(qq, qq) + 2 * (xp - eta) * P * qm) ** 2)


def numerators(Gam):
    Ns = [[tr(G[m] * slash(ls) * G[n] * Gam) for n in range(4)] for m in range(4)]
    Nu = [[tr(G[n] * slash(lu) * G[m] * Gam) for n in range(4)] for m in range(4)]
    return Ns, Nu


NsV, NuV = numerators(gm)
NsA, NuA = numerators(g5 * gm)
Ds, Du = 2 * (x - xp) * P * qm, -2 * (x + xp) * P * qm
# T^{mu nu} = i * (1/4) * i * [Ns/Ds + Nu/Du] * calH  = -(1/4)[Ns/Ds + Nu/Du] calH
TV = [[sp.simplify(-sp.Rational(1, 4) * (NsV[m][n] / Ds + NuV[m][n] / Du)) for n in range(4)] for m in range(4)]
TA = [[sp.simplify(-sp.Rational(1, 4) * (NsA[m][n] / Ds + NuA[m][n] / Du)) for n in range(4)] for m in range(4)]

print('=== 1. tensor structure at leading twist ===')
ck.check('vector part: only T^{11} = T^{22} nonzero among transverse components; T^{12} = 0',
         sp.simplify(TV[1][1] - TV[2][2]) == 0 and TV[1][2] == 0 and TV[2][1] == 0)
ck.check('axial part: only T^{12} = -T^{21} among transverse components; T^{11} = 0',
         sp.simplify(TA[1][2] + TA[2][1]) == 0 and TA[1][1] == 0 and TA[2][2] == 0)
ok = all(TV[m][n] == 0 and TA[m][n] == 0 for m in range(4) for n in range(4) if (m in (0, 3) or n in (0, 3)))
ck.check('all components with a longitudinal index vanish: longitudinal gamma* decouples at leading twist (sigma_L/sigma_T power suppressed)', ok)
# V defined by T^{ij} = -g_perp^{ij} V  =>  V = T^{11} ;  A defined by T^{ij} = i eps_perp^{ij} A => A = -i T^{12}
Vker = sp.simplify(TV[1][1])            # coefficient of calH
Aker = sp.simplify(-I * TA[1][2])       # coefficient of calHt
print('   V kernel (per calH)  =', sp.factor(Vker))
print('   A kernel (per calHt) =', sp.factor(Aker))
# in terms of F^q = calH/(2P): coefficient functions
CV = sp.simplify(Vker * 2 * P)
CA = sp.simplify(Aker * 2 * P)
ck.zero('vector:  T^{ij} = -g_perp^{ij} sum e_q^2 int dx F^q [1/(xi\'-x) - 1/(xi\'+x)]   (i0 attached below)', sp.simplify(CV - (1 / (xp - x) - 1 / (xp + x))))
ck.zero('axial:   T^{ij} = i eps_perp^{ij} sum e_q^2 int dx Ft^q [1/(xi\'-x) + 1/(xi\'+x)]', sp.simplify(CA - (1 / (xp - x) + 1 / (xp + x))))
ck.check('kernels depend on xi\' only (not on the skewness eta) at LO', (sp.diff(CV, eta) == 0) and (sp.diff(CA, eta) == 0))
print('   i0: (k\'+q\')^2 + i0 = 2 P qbar^- (x - xi\' + i0)  and  (k-q\')^2 + i0 = -2 P qbar^- (x + xi\' - i0), P qbar^- > 0, so')
print('   C_V = 1/(xi\'-x-i0) - 1/(xi\'+x-i0) = -[1/(x-xi\'+i0) + 1/(x+xi\'-i0)],  C_A = 1/(xi\'-x-i0) + 1/(xi\'+x-i0) = -[1/(x-xi\'+i0) - 1/(x+xi\'-i0)]')

print('=== 2. symmetry: C-even combinations ===')
ck.zero('C_V(-x) = -C_V(x): only H^q(x) - H^q(-x) (forward: q + qbar) contributes', sp.simplify(CV.subs(x, -x) + CV))
ck.zero('C_A(-x) = +C_A(x): only Ht^q(x) + Ht^q(-x) (forward: Delta q + Delta qbar) contributes', sp.simplify(CA.subs(x, -x) - CA))


print('=== 3. DIS limit with the i0 taken from the Feynman propagators (finite epsilon numerics) ===')
# forward: eta = 0, xi' = x_B, calH = 2 P^+ q(x) (spin averaged).  Use a model q(x) for x>0 and qbar for x<0:
#   H(x) = q(x) for x>0, -qbar(-x) for x<0.
qmod = lambda t: 3 * t ** -0.5 * (1 - t) ** 3 / 2.0 if t > 0 else 0.0
qbmod = lambda t: 0.4 * t ** -0.5 * (1 - t) ** 7 if t > 0 else 0.0
Hmod = lambda t: qmod(t) if t > 0 else -qbmod(-t)
def T11_numeric(xB, epsv, Pv=1.0, qmv=3.0):
    # V = T^{11} = int dx [ -(1/4) (Ns/(Ds + i eps) + Nu/(Du + i eps)) ] * calH,  calH = 2 P H(x)
    fV = sp.lambdify((x,), sp.simplify(-sp.Rational(1, 4) * NsV[1][1].subs({eta: 0, xp: xB, P: Pv, qm: qmv})), 'mpmath')
    fU = sp.lambdify((x,), sp.simplify(-sp.Rational(1, 4) * NuV[1][1].subs({eta: 0, xp: xB, P: Pv, qm: qmv})), 'mpmath')
    Dsn = lambda t: 2 * (t - xB) * Pv * qmv
    Dun = lambda t: -2 * (t + xB) * Pv * qmv
    integrand = lambda t: (fV(t) / (Dsn(t) + 1j * epsv) + fU(t) / (Dun(t) + 1j * epsv)) * 2 * Pv * Hmod(t)
    return complex(mp.quad(integrand, [-1, -xB, 0, xB, 1], maxdegree=12))
xB = 0.3
F1 = 0.5 * (4.0 / 9) * (qmod(xB) + qbmod(xB))     # single flavour with e_q = 2/3: F_1 = (1/2) e_q^2 (q + qbar)
vals = [T11_numeric(xB, e_) * 4.0 / 9 for e_ in (1e-2, 3e-3, 1e-3)]
print('   Im T^{11}(eps) =', ['%.6f' % v.imag for v in vals], ' ;  2 pi F_1 =', '%.6f' % (2 * np.pi * F1))
ck.close('Im T^{11} -> 2 pi W^{11} = 2 pi F_1 with F_1 = (1/2) sum e_q^2 (q + qbar)  [binding DIS conventions]', vals[-1].imag, 2 * np.pi * F1, tol=2e-2)
ck.check('sign of Im T^{11} positive (optical theorem) with the Feynman i0', vals[-1].imag > 0)

print('=== 4. DVCS: imaginary part from the crossover line ===')
# GPD model at fixed xi (DD model of s6, valence-like + an antiquark part via -q(-x) symmetric DD); use H(x,xi) from s6 formulas
xi_v = 0.2
X, XI = sp.symbols('X XI', real=True)
b = sp.symbols('beta', real=True)
Fba = sp.Rational(3, 4) * ((1 - b) ** 2 - ((X - b) / XI) ** 2)
H_dg = sp.lambdify((X, XI), sp.simplify(sp.integrate(Fba, (b, (X - XI) / (1 - XI), (X + XI) / (1 + XI))) / XI), 'mpmath')
H_er = sp.lambdify((X, XI), sp.simplify(sp.integrate(Fba, (b, 0, (X + XI) / (1 + XI))) / XI), 'mpmath')
def Hq(t, xi_):          # quark DD part
    if t >= xi_:
        return H_dg(t, xi_)
    if t > -xi_:
        return H_er(t, xi_)
    return 0.0
Hfull = lambda t, xi_: Hq(t, xi_) - 0.3 * Hq(-t, xi_)      # add an antiquark-like component: -0.3 H_q(-x)
def V_dvcs(epsv, Pv=1.0, qmv=3.0):
    fV = sp.lambdify((x,), sp.simplify(-sp.Rational(1, 4) * NsV[1][1].subs({eta: xi_v, xp: xi_v, P: Pv, qm: qmv})), 'mpmath')
    fU = sp.lambdify((x,), sp.simplify(-sp.Rational(1, 4) * NuV[1][1].subs({eta: xi_v, xp: xi_v, P: Pv, qm: qmv})), 'mpmath')
    integrand = lambda t: (fV(t) / (2 * (t - xi_v) * Pv * qmv + 1j * epsv) + fU(t) / (-2 * (t + xi_v) * Pv * qmv + 1j * epsv)) * 2 * Pv * Hfull(t, xi_v)
    return complex(mp.quad(integrand, [-1, -xi_v, 0, xi_v, 1], maxdegree=12))
vv = V_dvcs(1e-3)
ImPred = np.pi * (Hfull(xi_v, xi_v) - Hfull(-xi_v, xi_v))
print('   Im V (eps=1e-3) = %.6f ;  pi [H(xi,xi) - H(-xi,xi)] = %.6f' % (vv.imag, ImPred))
ck.close('Im of the vector CFF = pi sum e_q^2 [H^q(xi,xi,t) - H^q(-xi,xi,t)]  (per unit charge)', vv.imag, ImPred, tol=1e-2)
# real part = principal value
def PV_dvcs():
    f = lambda t: Hfull(t, xi_v) * (1 / (xi_v - t) - 1 / (xi_v + t))
    # subtract the poles
    g = lambda t: (Hfull(t, xi_v) - Hfull(xi_v, xi_v)) / (xi_v - t) - (Hfull(t, xi_v) - Hfull(-xi_v, xi_v)) / (xi_v + t)
    val = mp.quad(g, [-1, -xi_v, 0, xi_v, 1])
    val += Hfull(xi_v, xi_v) * mp.log((1 + xi_v) / (1 - xi_v)) - Hfull(-xi_v, xi_v) * mp.log((1 + xi_v) / (1 - xi_v))
    return float(val)
ck.close('Re of the vector CFF = PV int dx H [1/(xi-x) - 1/(xi+x)]  (finite-eps limit)', vv.real, PV_dvcs(), tol=1e-2)

ck.summary()
