#!/usr/bin/env python3
"""
s2_crs_yukawa_pdf.py -- checks for the MS-bar positivity section of OTHERS.md.

Collins-Rogers-Sato, PRD 105 (2022) 076010 [arXiv:2111.01170], Sec. VIII: Yukawa model
L_int = -lambda Psibar_N psi_q phi + h.c., one-loop quark-in-"proton" pdf.  Their Eq. (58):
   f_bare ~ a_lambda (1-xi) * Int_0^inf dk^2 (k^2)^(-eps) [k^2 + (m_q + xi m_p)^2] / [k^2 + Delta]^2
(with the MS-bar normalisation S_eps = (4 pi)^eps e^{-eps gamma_E}/... absorbed), and their Eq. (55):
   f_ren(xi; mu) = a_lambda (1-xi) [ ln(mu^2/Delta) - 1 + (m_q + xi m_p)^2/Delta ],
   Delta(xi) = xi m_s^2 + (1-xi) m_q^2 - xi (1-xi) m_p^2 .
We (i) re-derive (55) from (58) in dimensional regularisation with MS-bar subtraction (sympy),
(ii) check the cut-off version (59) agrees with (55) up to O(m^2/mu^2) at k_cut = mu,
(iii) reproduce the qualitative statements: negative at low mu and moderate/large xi for
     m_q=0.3, m_p=1.0, m_s=1.5 GeV, positive at large mu; xi->0 threshold mu < m_q; xi->1 threshold.
Run: python3 -I s2_crs_yukawa_pdf.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np
from scipy.integrate import quad

PASS = FAIL = 0
def check(name, ok, info=""):
    global PASS, FAIL
    if ok: PASS += 1
    else:  FAIL += 1
    print(("[PASS] " if ok else "[FAIL] ") + name + ("  " + info if info else ""))

eps = sp.symbols('epsilon')
mu2, Dl, A = sp.symbols('mu2 Delta A', positive=True)
# DR integrals:  Int_0^inf dk (k)^(-eps) k/(k+Delta)^2 = Delta^(-eps) Gamma(2-eps) Gamma(eps)
#               Int_0^inf dk (k)^(-eps) 1/(k+Delta)^2 = Delta^(-1-eps) Gamma(1-eps) Gamma(1+eps)
# MS-bar measure factor for d^{2-2eps}k_T / pi^{1-eps}: mu^{2 eps} e^{eps gamma_E} / Gamma(1-eps)
pref = mu2 ** eps * sp.exp(eps * sp.EulerGamma) / sp.gamma(1 - eps)
I1 = pref * Dl ** (-eps) * sp.gamma(2 - eps) * sp.gamma(eps)
I2 = pref * Dl ** (-1 - eps) * sp.gamma(1 - eps) * sp.gamma(1 + eps)
bare = I1 + A * I2                       # times a_lambda (1-xi)
ser = sp.series(bare, eps, 0, 1).removeO()
pole = sp.simplify(sp.limit(eps * ser, eps, 0))
finite = sp.simplify(sp.expand(ser - pole / eps))
target = sp.log(mu2 / Dl) - 1 + A / Dl
check("DR: UV pole of the bare one-loop pdf is a_lambda (1-xi)/eps (MS-bar counterterm, CRS Eq. 57)",
      sp.simplify(pole - 1) == 0, f"pole coefficient = {pole}")
check("DR + MS-bar: finite part = ln(mu^2/Delta) - 1 + (m_q+xi m_p)^2/Delta  (CRS Eq. 55)",
      sp.simplify(finite - target) == 0, f"finite = {sp.simplify(finite)}")

# numeric model
mq, mp, ms = 0.3, 1.0, 1.5
Delta = lambda x: x * ms**2 + (1 - x) * mq**2 - x * (1 - x) * mp**2
f55 = lambda x, mu: (1 - x) * (np.log(mu**2 / Delta(x)) - 1 + (mq + x * mp)**2 / Delta(x))
def fcut(x, kc2):
    g = lambda k2: (1 - x) * (k2 + (mq + x * mp)**2) / (k2 + Delta(x))**2
    return quad(g, 0, kc2, limit=200)[0]
xs = np.linspace(0.02, 0.98, 49)
check("Delta(xi) > 0 on (0,1) for m_p < m_q + m_s (stable target)", np.all(Delta(xs) > 0))
# (ii) cutoff vs MS-bar at large mu
mu = 30.0
dev = max(abs(fcut(x, mu**2) - f55(x, mu)) for x in xs)
check("cut-off pdf (CRS Eq. 59) with k_cut = mu equals MS-bar (55) up to O(m^2/mu^2) at mu = 30 GeV",
      dev < 5e-3, f"max |diff| = {dev:.2e}")
check("cut-off pdf is positive for all xi (positive integrand)", all(fcut(x, 0.5**2) > 0 for x in xs))
# (iii) sign pattern
neg_08 = [x for x in xs if f55(x, 0.8) < 0]
neg_12 = [x for x in xs if f55(x, 1.2) < 0]
neg_25 = [x for x in xs if f55(x, 2.5) < 0]
check("MS-bar pdf negative for moderate/large xi at mu = 0.8 GeV", len(neg_08) > 0,
      f"negative for xi in [{min(neg_08):.2f},{max(neg_08):.2f}]" if neg_08 else "")
check("negativity region shrinks from mu = 0.8 to 1.2 GeV", len(neg_12) < len(neg_08),
      f"#neg points: {len(neg_08)} -> {len(neg_12)}")
check("MS-bar pdf positive for all xi at mu = 2.5 GeV", len(neg_25) == 0)
# xi -> 0 : f -> ln(mu^2/m_q^2) (bracket), negative iff mu < m_q
x0 = 1e-7
check("xi->0: bracket -> ln(mu^2/m_q^2): negative for mu = 0.25 < m_q, positive for mu = 0.35",
      f55(x0, 0.25) < 0 and f55(x0, 0.35) > 0)
# xi -> 1 : bracket -> ln(mu^2/m_s^2) - 1 + (m_q+m_p)^2/m_s^2 ; threshold
mu_star = ms * np.exp(0.5 * (1 - (mq + mp)**2 / ms**2))
x1 = 1 - 1e-7
check("xi->1: sign change at mu* = m_s exp[(1-(m_q+m_p)^2/m_s^2)/2]",
      f55(x1, 0.99 * mu_star) < 0 and f55(x1, 1.01 * mu_star) > 0, f"mu* = {mu_star:.3f} GeV")
print(f"\nTOTAL: {PASS} PASS, {FAIL} FAIL")
