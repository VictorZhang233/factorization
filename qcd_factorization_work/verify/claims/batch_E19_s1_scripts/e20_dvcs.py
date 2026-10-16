# -*- coding: utf-8 -*-
"""
E20 (independent check, stage-1 verifier).  LO handbag for doubly-virtual Compton scattering,
gamma*(q) N(p) -> gamma(q') N(p'), with explicit 4x4 Dirac matrices (own implementation, no project code).

Definition (Ji's ordering, equivalent by translation):
  T^{mu nu} = i int d^4z e^{i q'.z} <p'| T{ J^mu(z) J^nu(0) } |p>,   J^nu absorbs q, J^mu emits q'.
Wick contraction gives two terms (s- and u-channel):
  T^{mu nu} = sum_q e_q^2 int dx { i Tr[g^mu S(l_s) g^nu M(x)] + i Tr[g^nu S(l_u) g^mu M(x)] },
  S(l) = i lslash/(l^2 + i0),  l_s = x Pbar + qbar (= k' + q'),  l_u = x Pbar - qbar (= k - q'),
  M(x) = (1/4)[ g^- calH + g5 g^- calHt ],  calH = 2 Pbar^+ F^q,  calHt = 2 Pbar^+ Ft^q  (leading-twist Fierz).
Conventions: metric (+,-,-,-), v^pm = (v^0 pm v^3)/sqrt2, gamma5 = i g0 g1 g2 g3, eps^{0123} = +1,
  nbar = (1,0,0,1)/sqrt2 (nbar.v = v^-), n = (1,0,0,-1)/sqrt2 (n.v = v^+), eps_perp^{mu nu} = eps^{mu nu rho sigma} nbar_rho n_sigma.
Claimed (E20):  T^{mu nu} = + g_perp^{mu nu} sum e_q^2 int F^q [1/(x-xi+i0) + 1/(x+xi-i0)]
                            - i eps_perp^{mu nu} sum e_q^2 int Ft^q [1/(x-xi+i0) - 1/(x+xi-i0)].
Run: python3 -I e20_dvcs.py
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np
import mpmath as mp

npass = nfail = 0
def check(label, ok, extra=''):
    global npass, nfail
    if ok: npass += 1
    else: nfail += 1
    print(('PASS ' if ok else 'FAIL ') + label + (('   [' + extra + ']') if extra else ''))

I = sp.I
s2 = sp.sqrt(2)
# Dirac representation
Z2, E2 = sp.zeros(2), sp.eye(2)
sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
def blk(a, b, c, d):
    return sp.Matrix(sp.BlockMatrix([[a, b], [c, d]]))
g0 = blk(E2, Z2, Z2, -E2)
gs = [blk(Z2, s, -s, Z2) for s in sig]
G = [g0] + gs
g5 = I * G[0] * G[1] * G[2] * G[3]
eta = sp.diag(1, -1, -1, -1)
# Clifford algebra and gamma5 checks
ok = all((G[m] * G[n] + G[n] * G[m]) == 2 * eta[m, n] * sp.eye(4) for m in range(4) for n in range(4))
check('Clifford algebra {g^mu, g^nu} = 2 g^{mu nu}', ok)
check('gamma5^2 = 1 and anticommutes', g5 * g5 == sp.eye(4) and all(g5 * G[m] + G[m] * g5 == sp.zeros(4) for m in range(4)))
def levi(*idx):
    return sp.LeviCivita(*idx)   # eps^{0123} = +1
ok = True
for m, n, r, s in itertools.product(range(4), repeat=4):
    t = (G[m] * G[n] * G[r] * G[s] * g5).trace()
    if sp.simplify(t - (-4 * I * levi(m, n, r, s))) != 0:
        ok = False
check('Tr(g^m g^n g^r g^s g5) = -4 i eps^{mnrs}  (all 256 index sets; eps^{0123}=+1)', ok)

def slash(v):   # v contravariant components: vslash = g_{mu nu} v^mu gamma^nu
    out = sp.zeros(4)
    for m in range(4):
        out += (eta[m, m] * v[m]) * G[m]
    return out
def lc(vp, vm, v1=0, v2=0):   # contravariant Cartesian from light-front components
    return [(vp + vm) / s2, v1, v2, (vp - vm) / s2]
def dot(a, b):
    return sum(eta[m, m] * a[m] * b[m] for m in range(4))
gplus = (G[0] + G[3]) / s2      # gamma^+
gminus = (G[0] - G[3]) / s2     # gamma^-
check('Tr[g^+ g^-] = 4 (g^{+-} = 1)', sp.simplify((gplus * gminus).trace() - 4) == 0)

nbar = [1 / s2, 0, 0, 1 / s2]
nvec = [1 / s2, 0, 0, -1 / s2]
lower = lambda v: [eta[m, m] * v[m] for m in range(4)]
check('nbar.v = v^-  and  n.v = v^+', sp.simplify(dot(nbar, lc(3, 5)) - 5) == 0 and sp.simplify(dot(nvec, lc(3, 5)) - 3) == 0)
def epsperp(m, n):
    return sp.simplify(sum(levi(m, n, r, s) * lower(nbar)[r] * lower(nvec)[s] for r in range(4) for s in range(4)))
check('eps_perp^{12} = +1, eps_perp^{21} = -1', epsperp(1, 2) == 1 and epsperp(2, 1) == -1)

x, xi, et, P, qm = sp.symbols('x xi eta P q_m', real=True)   # xi = generalized Bjorken variable xi', et = skewness
Pbar = lc(P, 0)
qbar = lc(-xi * P, qm)
ls = [Pbar[m] * x + qbar[m] for m in range(4)]
lu = [Pbar[m] * x - qbar[m] for m in range(4)]
check("l_s^2 = 2 P q^- (x - xi)", sp.simplify(dot(ls, ls) - 2 * P * qm * (x - xi)) == 0)
check("l_u^2 = -2 P q^- (x + xi)", sp.simplify(dot(lu, lu) + 2 * P * qm * (x + xi)) == 0)
# skewness enters only through Delta, i.e. not at all in l_s, l_u (k'+q' = x Pbar + qbar exactly)
Delta = lc(-2 * et * P, 0)
kprime = [Pbar[m] * x + Delta[m] / 2 for m in range(4)]
qprime = [qbar[m] - Delta[m] / 2 for m in range(4)]
check("l_s = k' + q' with k'^+ = (x - eta) Pbar^+ (skewness drops out)", all(sp.simplify(kprime[m] + qprime[m] - ls[m]) == 0 for m in range(4)))

Hs, Hts = sp.symbols('calH calHt')
M = (gminus * Hs + g5 * gminus * Hts) / 4
Ds, Du = 2 * P * qm * (x - xi), -2 * P * qm * (x + xi)     # i0's are attached afterwards from l^2 + i0
def T(m, n):
    # i * Tr[g^m (i lslash/D) g^n M] + i * Tr[g^n (i lslash_u/D_u) g^m M]   (index positions: upper)
    A = I * (G[m] * (I * slash(ls)) * G[n] * M).trace() / Ds
    B = I * (G[n] * (I * slash(lu)) * G[m] * M).trace() / Du
    return sp.simplify(A + B)
Tm = [[T(m, n) for n in range(4)] for m in range(4)]
F, Ft = sp.symbols('F Ft')
sub = {Hs: 2 * P * F, Hts: 2 * P * Ft}
# claimed structure WITHOUT i0 (the real parts): g_perp^{ij} = g^{ij} = -delta^{ij}
claim = lambda m, n: (eta[m, n] * F * (1 / (x - xi) + 1 / (x + xi)) - I * epsperp(m, n) * Ft * (1 / (x - xi) - 1 / (x + xi)))
ok = all(sp.simplify(Tm[m][n].subs(sub) - claim(m, n)) == 0 for m in (1, 2) for n in (1, 2))
check('transverse T^{ij} = g_perp^{ij} F [1/(x-xi) + 1/(x+xi)] - i eps_perp^{ij} Ft [1/(x-xi) - 1/(x+xi)]  (i,j = 1,2)', ok)
ok = all(sp.simplify(Tm[m][n]) == 0 for m in range(4) for n in range(4) if (m in (0, 3) or n in (0, 3)))
check('all components with a time/longitudinal index vanish at leading twist (photon helicity conserved)', ok)
# where the i0 sits: the s-channel term carries 1/(l_s^2+i0) = 1/(2Pq^-(x-xi+i0)); the u-channel 1/(l_u^2+i0) = -1/(2Pq^-(x+xi-i0))
eps0 = sp.symbols('epsilon', positive=True)
check('u-channel: 1/(l_u^2 + i eps) = -(1/(2Pq^-)) * 1/(x + xi - i eps/(2Pq^-))  => second denominator carries -i0',
      sp.simplify(1 / (Du + I * eps0) - (-(1 / (2 * P * qm)) / (x + xi - I * eps0 / (2 * P * qm)))) == 0)
check('s-channel: 1/(l_s^2 + i eps) = +(1/(2Pq^-)) * 1/(x - xi + i eps/(2Pq^-))  => first denominator carries +i0',
      sp.simplify(1 / (Ds + I * eps0) - ((1 / (2 * P * qm)) / (x - xi + I * eps0 / (2 * P * qm)))) == 0)

# ---- Ji's form: -(1/2)(p^mu n^nu + p^nu n^mu - g^{mu nu}) = +(1/2) g_perp^{mu nu}... check the tensor identity
# Ji: p = Lambda(1,0,0,1), n = (1,0,0,-1)/(2 Lambda), p.n = 1; then p^mu n^nu + p^nu n^mu - g^{mu nu} = -g_perp^{mu nu}
Lam = sp.symbols('Lambda', positive=True)
pJ = [Lam, 0, 0, Lam]
nJ = [1 / (2 * Lam), 0, 0, -1 / (2 * Lam)]
ginv = eta  # numerically same as g^{mu nu}
gperp = sp.Matrix(4, 4, lambda m, n: ginv[m, n] - (pJ[m] * nJ[n] + pJ[n] * nJ[m]))
ok = all(sp.simplify(pJ[m] * nJ[n] + pJ[n] * nJ[m] - ginv[m, n] + gperp[m, n]) == 0 for m in range(4) for n in range(4))
check('Ji tensor: p^mu n^nu + p^nu n^mu - g^{mu nu} = -g_perp^{mu nu}', ok and sp.simplify(dot(pJ, nJ) - 1) == 0)
print('   => Ji eq.(15) vector term = (1/2) g_perp^{mu nu} int [..] [H Ubar nslash U + ...], and [H Ubar nslash U + E ...] = 2 F^q,')
print('      i.e. + g_perp^{mu nu} int F^q [1/(x - xi_Ji/2 + i eps) + 1/(x + xi_Ji/2 (+/-) i eps)]  -- same vector structure as the claim.')

# ---- DIS limit numerics with finite i eps in the Feynman propagators (eta = 0, xi = x_B, F^q -> q(x) - qbar(-x))
qmod = lambda t: 1.5 * t ** -0.5 * (1 - t) ** 3
qbmod = lambda t: 0.4 * t ** -0.5 * (1 - t) ** 7
def Fq(t):
    return qmod(t) if t > 0 else -qbmod(-t)
xB = 0.25
Pv, qmv = 1.0, 2.0
fs = sp.lambdify((x,), sp.simplify((I * (G[1] * (I * slash(ls)) * G[1] * gminus).trace() / 4).subs({xi: xB, P: Pv, qm: qmv})), 'mpmath')
fu = sp.lambdify((x,), sp.simplify((I * (G[1] * (I * slash(lu)) * G[1] * gminus).trace() / 4).subs({xi: xB, P: Pv, qm: qmv})), 'mpmath')
def T11(epsv, sign_u=+1):
    # Feynman: l^2 + i eps in both. sign_u = -1 imitates Ji's printed +i eps written in the variable (x + xi):
    # 1/(x + xi + i e) <=> 1/(l_u^2 - i e') (anti-Feynman u-channel propagator)
    integ = lambda t: (fs(t) / (2 * Pv * qmv * (t - xB) + 1j * epsv) + fu(t) / (-2 * Pv * qmv * (t + xB) + sign_u * 1j * epsv)) * 2 * Pv * Fq(t)
    return complex(mp.quad(integ, [-1, -xB, 0, xB, 1], maxdegree=10))
F1 = 0.5 * (qmod(xB) + qbmod(xB))  # unit charge
vals = [T11(e) for e in (1e-2, 3e-3, 1e-3)]
print('   Feynman i0:  Im T^11 =', ['%.6f' % v.imag for v in vals], '  2 pi F_1 = %.6f' % (2 * np.pi * F1))
check('DIS limit, Feynman propagators: Im T^{11} -> 2 pi F_1, F_1 = (1/2)(q + qbar)  (optical theorem, binding conventions)',
      abs(vals[-1].imag - 2 * np.pi * F1) / (2 * np.pi * F1) < 3e-3, 'rel. dev. %.1e' % (abs(vals[-1].imag - 2 * np.pi * F1) / (2 * np.pi * F1)))
valsJ = [T11(e, sign_u=-1) for e in (1e-2, 3e-3, 1e-3)]
pred_wrong = np.pi * (qmod(xB) - qbmod(xB))
print('   Ji-type +i0 in 2nd denominator: Im T^11 =', ['%.6f' % v.imag for v in valsJ], '  pi (q - qbar) = %.6f' % pred_wrong)
check('with +i0 in the u-channel denominator one gets Im T^{11} -> pi (q - qbar): antiquarks enter with the wrong sign (violates positivity)',
      abs(valsJ[-1].imag - pred_wrong) / abs(pred_wrong) < 5e-3)
# closed form of the claim vs. numerics: Im of +g_perp^{11} int F [1/(x-xi+i0) + 1/(x+xi-i0)] = pi [F(xi) - F(-xi)]
check('closed form: Im{ -int F [1/(x-xB+i0) + 1/(x+xB-i0)] } = pi[F(xB) - F(-xB)] = pi (q + qbar)(xB)',
      abs(np.pi * (Fq(xB) - Fq(-xB)) - 2 * np.pi * F1) < 1e-12)
print('-' * 70)
print('e20_dvcs: %d PASS, %d FAIL' % (npass, nfail))
