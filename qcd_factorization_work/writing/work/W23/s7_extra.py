# -*- coding: utf-8 -*-
"""
s7_extra.py -- Ch20: additional checks of formulas printed in the chapter that s1-s6 do not cover.
 A. Exact-in-eps one-loop threshold vertex and on-shell Z_2 (Feynman gauge, D = 4 - 2 eps, our MSbar factor
    mu^{2eps} e^{eps gamma_E}), written in closed form:
      delta_V  = a e^{eps gE} (mu^2/m^2)^eps { Gamma(eps)(1-eps)/(1-2eps)
                                               + Gamma(1+eps)[ 2/(eps(1+2eps)) - 1/(1-2eps) ] },
      delta Z2 = -a e^{eps gE} (mu^2/m^2)^eps Gamma(eps) (3-2eps)/(1-2eps),
      c_v - 1  = -8 a Gamma(1+eps) e^{eps gE} (mu^2/m^2)^eps/(1 - 4 eps^2)      (exact),
    a = alpha_s C_F/(4 pi).  Cross-checked against the independent Feynman-parameter evaluation of s5_cv.py
    (rebuilt here from the reduced numerator r0(a) = -2m^2[2-(1-eps)a^2], r2 = 2(1-eps)^2/(2-eps)).
 B. Traces with the threshold spin projectors Pi_S = (pslash+m) Gamma_S (pslash-m)/(2 sqrt2 m):
      Tr[gamma^mu Pi_1] = -2 sqrt2 m eps^mu   (3S1);
      polarization-averaged lepton tensor (1/3)(-g + PP/M^2)_{mu nu} Tr[k1 g^mu k2 g^nu] = 4 M^2/3;
      1S0 -> gamma gamma: T^{mu nu} = Tr[(g^nu S(p-k1) g^mu + g^mu S(p-k2) g^nu) Pi_0] = c eps^{mu nu a b} k1_a k2_b / m^2
      with c = i sqrt2, and sum_pol |eps1 eps2 T|^2 = 2 |c|^2 (k1.k2)^2/m^4 = 16.
    Then Gamma(3S1 -> e+e-) and Gamma(1S0 -> gamma gamma) reproduce VF-NRQ-2/3 analytically.
 C. Tree-level photon spectrum from the shape function: mean E = m_b/2 + <omega>/2, variance <omega^2>/4 = -lambda_1/12,
    checked on a two-parameter model with prescribed moments.
 D. Time dilation: <m/E> = 1 - <p^2>/(2 m^2) + O(p^4) for an arbitrary isotropic momentum distribution (series).
 E. Manohar-Wise (1994) eq. (5.7), rho -> 0: 1 + 5E_b - 6K_b - 2G_b with E_b = K_b + G_b; MW use [D,D] = +i g G, so
    in our convention G_b = -3 lambda_2/(2 m_b^2) for the B (d_B = 3); K_b = -lambda_1/(2 m_b^2):
    Gamma/Gamma_b = 1 + (lambda_1 - 9 lambda_2)/(2 m_b^2); size of -9 lambda_2/(2 m_b^2) for lambda_2 = 0.12, m_b = 4.8.
Run: python3 -I s7_extra.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w23common import *
import numpy as np

ck = Check('s7_extra: exact-eps c_v, threshold traces, photon-spectrum moments, time dilation, MW total rate')

# ------------------------------------------------------------------------------------------- A
eps = sp.symbols('epsilon')
a_, m, mu = sp.symbols('a m mu', positive=True)
gE = sp.EulerGamma
D = 4 - 2 * eps
r0 = -2 * m**2 * (2 - (1 - eps) * a_**2)
r2 = 2 * (1 - eps)**2 / (2 - eps)
def meas(poly, p):
    """int_{-1}^{1} da (1-|a|) |a|^p * poly(a) for even poly"""
    P = sp.Poly(sp.expand(poly), a_)
    res = 0
    for (n,), c in P.terms():
        if n % 2:
            continue
        res += c * 2 / ((n + p + 1) * (n + p + 2))
    return sp.simplify(res)
pref = sp.exp(eps * gE) * (mu**2 / m**2)**eps
# T2 term: (+i)(-i) prefactor -> +1 ; integral i/(4pi)^{D/2} (D/4) Gamma(eps) Delta^{-eps};  Delta = a^2 m^2
uv = (D / 4) * sp.gamma(eps) * r2 * meas(sp.S(1), -2 * eps)
# T0 term: (-i)(-i) -> -1 ; integral -i/(4pi)^{D/2} Gamma(1+eps)/2 Delta^{-1-eps}
ir = -(sp.gamma(1 + eps) / 2) * meas(r0 / m**2, -2 - 2 * eps)
dV = pref * (uv + ir)
dV_closed = pref * (sp.gamma(eps) * (1 - eps) / (1 - 2 * eps) + sp.gamma(1 + eps) * (2 / (eps * (1 + 2 * eps)) - 1 / (1 - 2 * eps)))
ck('closed form of delta_V equals the Feynman-parameter evaluation (exact in eps)', sp.simplify(sp.gammasimp(dV - dV_closed)) == 0)
L = sp.symbols('L')
ser = lambda e: sp.expand(sp.simplify(sp.series(sp.simplify(e.subs(mu, m * sp.exp(L / 2))), eps, 0, 1).removeO()))
ck('delta_V = a (3/eps - 4 + 3L) + O(eps)', sp.simplify(ser(dV_closed) - (3 / eps - 4 + 3 * L)) == 0, ser(dV_closed))
dZ2_closed = -pref * sp.gamma(eps) * (3 - 2 * eps) / (1 - 2 * eps)
ck('delta Z_2^OS = -a (3/eps + 4 + 3L) + O(eps)', sp.simplify(ser(dZ2_closed) - (-(3 / eps + 4 + 3 * L))) == 0, ser(dZ2_closed))
# cross-check of the Z_2 closed form against the standard on-shell integral representation
x = sp.symbols('x', positive=True)
# Sigma(p) = a e^{eps gE} mu^{2eps} Gamma(eps) int dx [-(D-2)(1-x) pslash + D m] Delta(x,p^2)^{-eps},
# Delta = x^2 p^2 + x (m^2 - p^2);  dZ2 = dSigma/dpslash at pslash = m (A + 2 m^2 (A' + B')).
# Beta-function integrals, continued from the convergent region (int_0^1 x^p (1-x)^q = B(p+1, q+1)):
Bf = lambda p, q: sp.gamma(p + 1) * sp.gamma(q + 1) / sp.gamma(p + q + 2)
A_on = -(D - 2) * Bf(-2 * eps, 1)                                   # int -(D-2)(1-x) x^{-2eps}
dA = (-(D - 2)) * (-eps) * (-Bf(-2 * eps - 1, 2)) / m**2           # (x^2 - x)(1-x) = -x (1-x)^2
dB = D * (-eps) * (Bf(-2 * eps, 0) - Bf(-2 * eps - 1, 0)) / m**2   # (x^2 - x) x^{-2eps-2} = x^{-2eps} - x^{-2eps-1}
dZ2_int = pref * sp.gamma(eps) * (A_on + 2 * m**2 * (dA + dB))
ck('closed form of delta Z_2 equals the Feynman-parameter self-energy derivative (exact in eps)',
   sp.simplify(sp.gammasimp(sp.simplify(dZ2_int - dZ2_closed))) == 0)
cv1 = sp.simplify(sp.gammasimp(dV_closed + dZ2_closed))
cv_closed = -8 * sp.gamma(1 + eps) * sp.exp(eps * gE) * (mu**2 / m**2)**eps / (1 - 4 * eps**2)
ck('c_v - 1 = -8 a Gamma(1+eps) e^{eps gE} (mu^2/m^2)^eps/(1-4 eps^2) exactly', sp.simplify(sp.gammasimp(cv1 - cv_closed)) == 0, sp.simplify(cv1))
ck('  -> -8 a at eps -> 0 (finite, mu independent): c_v = 1 - 2 C_F alpha_s/pi', sp.limit(cv_closed, eps, 0) == -8)
# UV/IR bookkeeping: UV part of delta_V has residue 1, IR part residue 2; Z_2: total residue -3
ck('pole bookkeeping: residues UV(delta_V) = 1, IR(delta_V) = 2, Z_2 = -3',
   sp.simplify(sp.residue(sp.simplify(pref * uv), eps, 0) - 1) == 0 and sp.simplify(sp.residue(sp.simplify(pref * ir), eps, 0) - 2) == 0
   and sp.simplify(sp.residue(dZ2_closed, eps, 0) + 3) == 0)

# ------------------------------------------------------------------------------------------- B
I2 = np.eye(2); Z2 = np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
G = [np.block([[I2, Z2], [Z2, -I2]]).astype(complex)] + [np.block([[Z2, s], [-s, Z2]]) for s in (sx, sy, sz)]
G5 = 1j * G[0] @ G[1] @ G[2] @ G[3]
met = np.diag([1., -1, -1, -1])
I4 = np.eye(4, dtype=complex)
def sl(v):
    vl = met @ v
    return sum(G[i] * vl[i] for i in range(4))
mq = 1.37
p = np.array([mq, 0, 0, 0.])
Pi = lambda Gs: (sl(p) + mq * I4) @ Gs @ (sl(p) - mq * I4) / (2 * np.sqrt(2) * mq)
okB1 = True
for epsv in (np.array([0, 1., 0, 0]), np.array([0, 0, 1., 0]), np.array([0, 0, 0, 1.]), np.array([0, 0.6, 0.8j, 0])):
    tr = np.array([np.trace(G[mu_] @ Pi(sl(epsv))) for mu_ in range(4)])
    okB1 = okB1 and np.allclose(tr, -2 * np.sqrt(2) * mq * epsv)
ck('Tr[gamma^mu Pi_1] = -2 sqrt2 m eps^mu (3S1 projector)', okB1)
M = 2 * mq
n = np.array([0.36, -0.48, 0.8])
k1 = np.concatenate([[M / 2], M / 2 * n]); k2 = np.concatenate([[M / 2], -M / 2 * n]); P = k1 + k2
Lmn = np.array([[np.trace(sl(k1) @ G[a] @ sl(k2) @ G[b]) for b in range(4)] for a in range(4)])
proj = (-met + np.outer(met @ P, met @ P) / M**2) / 3          # lower indices
ck('polarization-averaged lepton tensor = 4 M^2/3', abs(np.einsum('ab,ab->', proj, Lmn) - 4 * M**2 / 3) < 1e-10)
def S(q):
    return (sl(q) + mq * I4) / (q @ met @ q - mq**2)
T = np.array([[np.trace((G[b] @ S(p - k1) @ G[a] + G[a] @ S(p - k2) @ G[b]) @ Pi(G5)) for b in range(4)] for a in range(4)])
# Levi-Civita eps^{mu nu a b} k1_a k2_b with eps^{0123} = +1
import itertools
def lc(i, j, k, l):
    perm = [i, j, k, l]
    if len(set(perm)) < 4:
        return 0
    s = 1
    for x_ in range(4):
        for y_ in range(x_ + 1, 4):
            if perm[x_] > perm[y_]:
                s = -s
    return s
k1l = met @ k1; k2l = met @ k2
E_ = np.array([[sum(lc(a, b, c, d) * k1l[c] * k2l[d] for c in range(4) for d in range(4)) for b in range(4)] for a in range(4)])
cfit = T[1, 2] / (E_[1, 2] / mq**2) if abs(E_[1, 2]) > 1e-12 else None
idx = np.unravel_index(np.argmax(abs(E_)), E_.shape)
cfit = T[idx] / (E_[idx] / mq**2)
ck('1S0 -> gamma gamma: T^{mu nu} = c eps^{mu nu a b} k1_a k2_b / m^2 with c = i sqrt2', np.allclose(T, cfit * E_ / mq**2) and abs(cfit - 1j * np.sqrt(2)) < 1e-10,
   'c = %s' % np.round(cfit, 12))
Tl = met @ T @ met
pol = np.einsum('ab,ab->', T, Tl.conj()).real
ck('sum over photon polarizations |eps1 eps2 T|^2 = 2|c|^2 (k1.k2)^2/m^4 = 16', abs(pol - 16) < 1e-9, pol)
# analytic widths from these pieces (symbols)
Nc, eQ, al, psi2 = sp.symbols('N_c e_Q alpha psi2', positive=True)
ms = sp.symbols('m', positive=True); Ms = 2 * ms
e2 = 4 * sp.pi * al
pref2 = 2 * Ms / (4 * ms**2) * Nc * psi2
Gee = sp.Rational(1, 1) / (2 * Ms) * pref2 * e2**2 * eQ**2 * (2 * sp.sqrt(2) * ms)**2 / Ms**4 * (4 * Ms**2 / 3) / (8 * sp.pi)
ck('Gamma(3S1->e+e-) from the traces = (16 pi N_c/3) e_Q^2 alpha^2 |psi(0)|^2/M^2 (VF-NRQ-2)', sp.simplify(Gee - 16 * sp.pi * Nc / 3 * eQ**2 * al**2 * psi2 / Ms**2) == 0)
Ggg = sp.Rational(1, 2) / (2 * Ms) * pref2 * e2**2 * eQ**4 * 16 / (8 * sp.pi)
ck('Gamma(1S0->gamma gamma) from the traces = 16 pi N_c e_Q^4 alpha^2 |psi(0)|^2/M^2 (VF-NRQ-3)', sp.simplify(Ggg - 16 * sp.pi * Nc * eQ**4 * al**2 * psi2 / Ms**2) == 0)

# ------------------------------------------------------------------------------------------- C
om = sp.symbols('omega', real=True); sig = sp.symbols('sigma', positive=True)
mb, l1 = sp.symbols('m_b lambda_1', real=True)
# model: S(omega) = Gaussian with mean 0 and variance -lambda_1/3 (tree-level moments); photon energy E = (m_b + omega)/2
Sg = sp.exp(-om**2 / (2 * sig**2)) / sp.sqrt(2 * sp.pi * sig**2)
sigv = sp.sqrt(-l1 / 3)
mom = lambda f: sp.simplify(sp.integrate(f * Sg, (om, -sp.oo, sp.oo)))
Emean = mom((mb + om) / 2)
Evar = sp.simplify(mom(((mb + om) / 2)**2) - Emean**2)
ck('tree level: <E_gamma> = m_b/2 and Var(E_gamma) = <omega^2>/4 = -lambda_1/12', sp.simplify(Emean - mb / 2) == 0 and sp.simplify(Evar.subs(sig, sigv) + l1 / 12) == 0)

# ------------------------------------------------------------------------------------------- D
pv = sp.symbols('p', positive=True); mm = sp.symbols('m', positive=True)
ser_td = sp.series(mm / sp.sqrt(mm**2 + pv**2), pv, 0, 5).removeO()
ck('time dilation: m/E = 1 - p^2/(2m^2) + 3p^4/(8m^4) + ...', sp.simplify(ser_td - (1 - pv**2 / (2 * mm**2) + 3 * pv**4 / (8 * mm**4))) == 0)
# average over a normalized isotropic distribution with <p^2> = -lambda_1 (to O(1/m^2))
ck('  averaged: Gamma_0 <m/E> = Gamma_0 [1 + lambda_1/(2 m^2) + O(1/m^4)] for <p^2> = -lambda_1',
   sp.simplify((1 - (-l1) / (2 * mm**2)) - (1 + l1 / (2 * mm**2))) == 0)

# ------------------------------------------------------------------------------------------- E
Kb, Gb, l2 = sp.symbols('K_b G_b lambda_2', real=True)
rate = (1 + 5 * (Kb + Gb) - 6 * Kb - 2 * Gb).subs({Kb: -l1 / (2 * mb**2), Gb: -3 * l2 / (2 * mb**2)})
ck('MW (5.7) at rho -> 0 in our convention: 1 + (lambda_1 - 9 lambda_2)/(2 m_b^2)', sp.simplify(rate - (1 + (l1 - 9 * l2) / (2 * mb**2))) == 0)
lam2 = (5.325**2 - 5.280**2) / 4
print('   lambda_2 from (m_B*^2 - m_B^2)/4 with m_B* = 5.325, m_B = 5.280 GeV: %.4f GeV^2' % lam2)
print('   -9 lambda_2/(2 m_b^2) for m_b = 4.8 GeV: %.4f' % (-9 * lam2 / (2 * 4.8**2)))
ck('lambda_2 ~ 0.12 GeV^2 and -9 lambda_2/(2 m_b^2) ~ -2.3% (m_b = 4.8 GeV)', abs(lam2 - 0.119) < 0.002 and abs(-9 * lam2 / (2 * 4.8**2) + 0.0233) < 0.0005)

ok = ck.summary()
sys.exit(0 if ok else 1)
