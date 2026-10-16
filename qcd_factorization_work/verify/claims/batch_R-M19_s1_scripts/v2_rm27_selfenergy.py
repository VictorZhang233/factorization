# R-M27 (independent check, verifier s1 v2): self-energies of space-like rapidity-regulator Wilson lines.
# Reference Def. D.21 / Aybat-Rogers (1101.5057) eq. (nLLdir): n_A = (n^+, n^-, 0_T) = (1, -e^{-2 y_A}, 0_T), n_A^2 = -2 e^{-2y_A}.
# Real gluon k = (k_T e^{y}/sqrt2, k_T e^{-y}/sqrt2, k_T).  Cut self-energy of line A (amplitude x conjugate):
#   eikonal factor n_A^2 / ((n_A.k + i0)(n_A.k - i0)) -> pinched double pole at n_A.k = 0, i.e. at y = y_A.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np
from scipy.integrate import quad

y, yA, kT, L, x = sp.symbols('y y_A k_T L x', real=True)
kp, km = kT * sp.exp(y) / sp.sqrt(2), kT * sp.exp(-y) / sp.sqrt(2)
nAp, nAm = 1, -sp.exp(-2 * yA)              # space-like
nA2 = 2 * nAp * nAm
nAk = nAp * km + nAm * kp
print('n_A.k + sqrt2 kT e^{-yA} sinh(y-yA) =', sp.simplify((nAk + sp.sqrt(2) * kT * sp.exp(-yA) * sp.sinh(y - yA)).rewrite(sp.exp)), ' (so n_A.k = 0 at y = y_A, inside the real-gluon phase space)')
ratio = sp.simplify((nA2 / nAk**2 - (-1 / (kT**2 * sp.sinh(y - yA)**2))).rewrite(sp.exp))
print('n_A^2/(n_A.k)^2 + 1/(kT^2 sinh^2(y-y_A)) =', ratio)
# time-like comparison n_A = (1, +e^{-2y_A})
nAk_t = 1 * km + sp.exp(-2 * yA) * kp
ratio_t = sp.simplify((2 * sp.exp(-2 * yA) / nAk_t**2 - 1 / (kT**2 * sp.cosh(y - yA)**2)).rewrite(sp.exp))
print('time-like: n_A^2/(n_A.k)^2 - 1/(kT^2 cosh^2(y-y_A)) =', ratio_t)
print('time-like self-energy rapidity integral  int dy / cosh^2 =', sp.integrate(1 / sp.cosh(y)**2, (y, -sp.oo, sp.oo)), '(finite)')

# space-like: excise |y - y_A| < eta, show divergence ~ 2/eta (non-integrable double pole)
for eta in (1e-1, 1e-2, 1e-3, 1e-4):
    val = 2 * quad(lambda u: 1 / np.sinh(u)**2, eta, 50, limit=200)[0]
    print('  space-like: int_{|u|>eta} du / sinh^2 u = %.6e   (2/eta = %.6e)' % (val, 2 / eta))
# finite-length regulator: Wilson line of length L: int_0^L dlam e^{i lam x} = (e^{iLx}-1)/(ix);  |.|^2 integrated over x
for Lv in (10.0, 100.0, 1000.0):
    f = lambda xx: (2 - 2 * np.cos(Lv * xx)) / xx**2 if xx != 0 else Lv**2
    # oscillatory integrand; ~1e-5 relative accuracy suffices; tail |x| > 200 added analytically (cos averages to 0)
    val = quad(f, -200, 200, limit=20000, points=[0.0])[0] + 2 * quad(lambda xx: 2 / xx**2, 200, np.inf)[0]
    print('  length-L regulator: int dx |(e^{iLx}-1)/x|^2 = %.4f   2 pi L = %.4f' % (val, 2 * np.pi * Lv))
print('  => the cut self-energy of a space-like line grows linearly with the line length (length divergence).')

# Collins' combination (reference (D.22)): arbitrary self-energy factors exp(sigma(y)) per line cancel identically.
s = sp.Function('sigma')
yB, yn, yAA = sp.symbols('y_B y_n y_AA', real=True)
lnS = lambda y1, y2: s(y1) + s(y2)            # self-energy part of ln S(y1, y2): one term per line
lnf_unsub_A = s(yB)                             # staple along n(y_B)
lnfA = lnf_unsub_A + sp.Rational(1, 2) * (lnS(yAA, yn) - lnS(yAA, yB) - lnS(yn, yB))
lnf_unsub_B = s(yAA)
lnfB = lnf_unsub_B + sp.Rational(1, 2) * (lnS(yn, yB) - lnS(yAA, yB) - lnS(yAA, yn))
print('(D.22): self-energy part of ln f_A =', sp.simplify(lnfA), ' ; of ln f_B =', sp.simplify(lnfB))
