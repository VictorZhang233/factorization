# -*- coding: utf-8 -*-
# w04_r2.py (writer W04, resumed session): checks for the corrected estimate in the proof of thm:ir-landau-alpha
# (App D, steps (iii)-(iv)): with z_j = alpha_j [1 - i tau eta w_j], w_j = dF_j - c, c = sum alpha_k dF_k,
#   Im F(z) = -tau eta V + O((tau eta)^3)   (uniformly in tau in [0,1]),
# i.e. the remainder is odd in (tau eta) and starts at third order, so that
#   Im F(z) <= -tau eta (delta - C eta^2) < 0 for every tau in (0,1] wherever V >= delta.
# Also: a homotopy scan for the massive vertex above the q-qbar threshold (no zero of F - i0 for tau in (0,1]).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np

npass = 0; nfail = 0
def check(name, ok):
    global npass, nfail
    if ok:
        npass += 1; print('PASS', name)
    else:
        nfail += 1; print('FAIL', name)

# ---------------------------------------------------------------------------------------------------------
# R1: exact structure of F(z) for the massive vertex (quark mass m, gluon mass mg, on-shell external quarks)
a0, a1, a2, s, m, mg, t = sp.symbols('alpha0 alpha1 alpha2 s m m_g t', real=True)   # t = tau*eta
al = [a0, a1, a2]
U = a0 + a1 + a2
# F = -sum_{2-forests} (prod alpha) s_T + U sum alpha_j m_j^2 for the vertex with p_i^2 = m^2, q^2 = s
F = -(a1*a2*s + a0*a1*m**2 + a0*a2*m**2) + U*(a0*mg**2 + a1*m**2 + a2*m**2)
dF = [sp.diff(F, x) for x in al]
c = sum(al[i]*dF[i] for i in range(3))
w = [dF[i] - c for i in range(3)]
z = [al[i]*(1 - sp.I*t*w[i]) for i in range(3)]
Fz = sp.expand(F.subs({a0: z[0], a1: z[1], a2: z[2]}, simultaneous=True))
V = sum(al[i]*dF[i]**2 for i in range(3)) - c**2
ImF = sp.expand(sp.im(Fz.subs({a0: a0, a1: a1, a2: a2})))
# work on the simplex: sum alpha = 1 (the constraint is preserved by the deformation)
poly_t = sp.Poly(sp.expand((Fz - F)), t)
coeffs = poly_t.all_coeffs()[::-1]       # coefficient of t^0, t^1, ...
ok_parity = True
for k, ck in enumerate(coeffs):
    ck = sp.expand(ck)
    re_k, im_k = sp.expand(sp.re(ck)), sp.expand(sp.im(ck))
    if k % 2 == 0 and im_k != 0:
        ok_parity = False
    if k % 2 == 1 and re_k != 0:
        ok_parity = False
check('R1 F(z)-F(alpha): even orders in tau*eta real, odd orders purely imaginary (massive vertex)', ok_parity)
lin = sp.expand(sp.im(coeffs[1]))
check('R1 first-order term = -i (tau eta) V on the simplex', sp.simplify((lin + V).subs(a2, 1 - a0 - a1)) == 0)
check('R1 no t^2 imaginary part: Im F(z) + tau eta V = O((tau eta)^3)', sp.expand(sp.im(coeffs[2])) == 0 if len(coeffs) > 2 else True)

# ---------------------------------------------------------------------------------------------------------
# R2: homotopy scan, massive vertex above threshold (m=1, mg=0.3, s=5): for all tau in (0,1] and all alpha,
#     either |F(z)| >= delta/2 or Im F(z) < 0  (no zero of F - i0 is crossed).
fF = sp.lambdify((a0, a1, a2, s, m, mg), F, 'numpy')
fFz = sp.lambdify((a0, a1, a2, s, m, mg, t), Fz, 'numpy')
fV = sp.lambdify((a0, a1, a2, s, m, mg), V, 'numpy')
eta = 0.05
n = 160
grid = []
for i in range(n + 1):
    for j in range(n + 1 - i):
        x0, x1 = i/n, j/n
        grid.append((x0, x1, 1 - x0 - x1))
G = np.array(grid)
pars = (5.0, 1.0, 0.3)
Fa = fF(G[:, 0], G[:, 1], G[:, 2], *pars)
Va = fV(G[:, 0], G[:, 1], G[:, 2], *pars)
delta = 0.5*np.min(np.abs(Fa) + Va)
worst = []
bad = 0
for tau in np.linspace(1e-4, 1.0, 60):
    Fz_ = fFz(G[:, 0], G[:, 1], G[:, 2], *pars, tau*eta)
    near = np.abs(Fa) < delta
    if np.any(near):
        worst.append(np.max(np.imag(Fz_[near])/(tau*eta)))
        bad += int(np.any(np.imag(Fz_[near]) >= 0))
    far = ~near
    bad += int(np.any(np.abs(Fz_[far]) < 0.5*delta))
print('   delta = %.3e ; max over grid of Im F(z)/(tau eta) on {|F|<delta}: %.3e (must be < 0)' % (delta, max(worst)))
check('R2 massive vertex, s=5m^2: Im F(z) < 0 near F=0 for all tau in (0,1] (eta=0.05), |F(z)| bounded away elsewhere', bad == 0 and max(worst) < 0)

# ---------------------------------------------------------------------------------------------------------
# R3: one loop: F has degree L+1 = 2, so the Taylor series stops at second order and Im F(z) = -tau eta V exactly.
#     Two loops (degree 3): the remainder is exactly (tau eta)^3 * (1/6) D^3F[a,a,a] with a_j = alpha_j w_j (odd order),
#     hence |Im F(z) + tau eta V| <= C (tau eta)^3 uniformly in tau.
rem1 = sp.simplify(sp.expand(sp.im(Fz) + t*V).subs(a2, 1 - a0 - a1))
check('R3a one loop (F quadratic): Im F(z) + tau eta V == 0 identically on the simplex', rem1 == 0)
import random
random.seed(7)
b = sp.symbols('b0:4', real=True)
mons = [b[i]*b[j]*b[k] for i in range(4) for j in range(i, 4) for k in range(j, 4)]
Fc = sum(sp.Rational(random.randint(-9, 9), random.randint(1, 5))*mo for mo in mons)
dFc = [sp.diff(Fc, x) for x in b]
cc = sum(b[i]*dFc[i] for i in range(4))
wc = [dFc[i] - cc for i in range(4)]
zc = [b[i]*(1 - sp.I*t*wc[i]) for i in range(4)]
Fcz = sp.expand(Fc.subs({b[i]: zc[i] for i in range(4)}, simultaneous=True))
Vc = sum(b[i]*dFc[i]**2 for i in range(4)) - cc**2
ac = [b[i]*wc[i] for i in range(4)]
D3 = sum(sp.diff(Fc, b[i], b[j], b[k])*ac[i]*ac[j]*ac[k] for i in range(4) for j in range(4) for k in range(4))
remc = sp.expand(sp.im(Fcz) + t*Vc - t**3*D3/6)
remc_s = sp.expand(remc.subs(b[3], 1 - b[0] - b[1] - b[2]))
check('R3b two loops (random cubic F): Im F(z) = -tau eta V + (tau eta)^3 D^3F[a,a,a]/6 exactly (on the simplex)', remc_s == 0)
print('\nSUMMARY: %d/%d checks passed' % (npass, npass + nfail))
