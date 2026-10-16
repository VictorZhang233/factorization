# Cross-check with the delta-regulator (Echevarria-Idilbi-Scimemi 2012, as re-expressed in
# Collins-Rogers 2013 eqs. (9),(37),(41)): light-like Wilson-line propagators 1/(-k^+ + i delta^+),
# 1/(k^- + i delta^-).  One loop, massless on-shell quark target, pure DR.
# Virtual graphs: the unsubtracted-TMD vertex with delta^+ only is scaleless (invariant under l^- -> k l^-, lT -> sqrt(k) lT)
# and vanishes; the soft-factor virtual graph with BOTH delta^+, delta^- is NOT scaleless (scale delta^+ delta^-), but
# unitarity S~(b=0) = 1 gives S~(b) = int d^{2-2eps}l (e^{il.b} - 1) rho(l), and replacing the exact rapidity integral
# rho by its small-delta form changes S~(b) only by O(b^2 delta^+ delta^-): so the real-graph treatment below is exact
# in the limit delta -> 0 (see DERIVATION.md Sec. 3.10).
#  (i)  unsubtracted TMD, Wilson-line graph:  2x(1-x)/((1-x)^2 + r^2), r = delta^+/p^+
#       -> 2x[1/(1-x)]_+ + 2 delta(1-x) ln(p^+/delta^+)            [checked in rapidity_checks.py (4)]
#  (ii) soft factor, real graph at fixed lT: rapidity integral of the regulated eikonal factor
#       R(lT) = int dy  l+ l- /((l+^2 + d+^2)(l-^2 + d-^2)) * (lT^2/2)  -> ln(lT^2/(2 d+ d-))
#  => A_0/sqrt(S_0): delta(1-x) coefficient  c_S FT[ ln(zeta/kT^2)/kT^2 ],  zeta = 2 (p^+)^2 delta^-/delta^+
#     identical to the JCC result with zeta = 2(p^+)^2 e^{-2 y_n}   (CR13 eq. (41): y_n <-> ln sqrt(d+/d-))
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from scipy.integrate import quad

ok = True
print('(ii) soft rapidity integral with delta^+-, delta^- regulators')
for lT, dp, dm in [(1.0, 1e-4, 1e-4), (0.3, 1e-5, 3e-4), (2.0, 1e-6, 1e-5)]:
    def f(y):
        lp, lm = lT * np.exp(y) / np.sqrt(2), lT * np.exp(-y) / np.sqrt(2)
        return lp * lm / ((lp**2 + dp**2) * (lm**2 + dm**2)) * lT**2 / 2
    ymin, ymax = np.log(np.sqrt(2) * dp / lT), np.log(lT / (np.sqrt(2) * dm))
    v, _ = quad(f, ymin - 30, ymax + 30, points=[ymin, ymax], limit=400)
    pred = np.log(lT**2 / (2 * dp * dm))
    print('  lT=%.2f d+=%.0e d-=%.0e  R=%.8f  ln(lT^2/(2 d+ d-))=%.8f  diff=%.1e' % (lT, dp, dm, v, pred, v - pred))
    ok &= abs(v - pred) < 1e-6
# (iii) algebra of the combination (coefficients of c_S FT[1/kT^2] and c_S FT[ln kT^2/kT^2]):
#  unsub: 2 ln(p+/d+) * FT[1/k^2]  ;  -1/2 soft: -1/2 * 2 * FT[ ln(k^2/(2 d+ d-))/k^2 ]
import sympy as sp
pp, dp_, dm_, k2 = sp.symbols('p_plus delta_p delta_m k2', positive=True)
comb = 2 * sp.log(pp / dp_) - sp.log(k2 / (2 * dp_ * dm_))
target = sp.log(2 * pp**2 * dm_ / dp_ / k2)
print('(iii) combination = ln(zeta/kT^2) with zeta = 2 p+^2 d-/d+ :', sp.simplify(sp.expand_log(comb - target, force=True)) == 0)
ok &= sp.simplify(sp.expand_log(comb - target, force=True)) == 0
print('delta-regulator cross-check:', 'PASS' if ok else 'FAIL')
