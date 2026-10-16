#!/usr/bin/env python3
"""W27 / Ch24 prop:front-msbar-negative proof, last step (writer-derived exact relation):
   f_cut(k_T < mu) / [a (1-xi)] = Int_0^{mu^2} dk (k + A)/(k + D)^2
                                = [ln(mu^2/D) - 1 + A/D] + ln(1 + D/mu^2) - (A - D)/(mu^2 + D)
   hence  f_MSbar = f_cut - a(1-xi)[ ln(1+D/mu^2) - (A-D)/(mu^2+D) ]  exactly (one loop),
   with A = (m_q + xi m_p)^2, D = Delta(xi)."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp, mpmath as mp
k, A, D, mu2 = sp.symbols('k A D mu2', positive=True)
lhs = sp.integrate((k + A) / (k + D)**2, (k, 0, mu2))
rhs = (sp.log(mu2 / D) - 1 + A / D) + sp.log(1 + D / mu2) - (A - D) / (mu2 + D)
ok = sp.simplify(sp.expand_log(lhs - rhs, force=True)) == 0
print(("[PASS] " if ok else "[FAIL] ") + "cut-off integral = MSbar bracket + ln(1+D/mu^2) - (A-D)/(mu^2+D)")
# numerical spot check at the book's masses
mq, mpp, ms = 0.3, 1.0, 1.5
for xi in [0.2, 0.5, 0.9]:
    for mu in [0.8, 2.5, 30.0]:
        Dv = xi*ms**2 + (1-xi)*mq**2 - xi*(1-xi)*mpp**2; Av = (mq + xi*mpp)**2
        num = mp.quad(lambda q: (q + Av)/(q + Dv)**2, [0, mu**2])
        an = (mp.log(mu**2/Dv) - 1 + Av/Dv) + mp.log(1 + Dv/mu**2) - (Av - Dv)/(mu**2 + Dv)
        assert abs(num - an) < 1e-12
print("[PASS] numerical spot checks (xi in {0.2,0.5,0.9}, mu in {0.8,2.5,30} GeV)")
