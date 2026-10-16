# -*- coding: utf-8 -*-
"""
E24 (independent check).  Becher-Schwartz 2008, eq. (2.6) of JHEP 07 (2008) 034 (same in arXiv v1/v2):
   J(p^2) = (1/nbar.p) (1/pi) Im[ i int d^4x e^{-ipx} <0| T{ chibar_n(x) (nbarslash/2) chi_n(0) } |0> ] = delta(p^2) + O(alpha_s).
Free fields (chi_n = xi_n = P_n psi, P_n = nslash nbarslash/4):
   S(z) = <0|T chi(z) chibar(0)|0> = int d^4k/(2pi)^4 e^{-ikz} P_n (i kslash/(k^2+i0)) Pbar_n,   Pbar_n = nbarslash nslash/4
        = int d^4k/(2pi)^4 e^{-ikz} (nslash/2) i nbar.k/(k^2+i0)                (checked below, exact off shell)
   <T chibar_a(x) G_ab chi_b(0)> = - G_ab <T chi_b(0) chibar_a(x)> = - tr[G S(-x)] * N_c   (fermionic T-ordering; colour trace)
   => i int d^4x e^{-ipx}(...) = -i N_c tr[G (nslash/2)] i nbar.p/(p^2+i0) = N_c tr[(nbarslash/2)(nslash/2)] nbar.p/(p^2+i0)
   => J_literal = (1/nbar.p)(1/pi) Im[...] = -N_c tr[(nbarslash/2)(nslash/2)] delta(p^2) = -2 N_c delta(p^2).
Comparison: Becher-Neubert PLB 637 (2006) 251 [hep-ph/0603140] eq. (Jscet): (nslash/2) nbar.p calJ = int d^4x e^{-ipx}<0|T{X(0) Xbar(x)}|0>,
   J = (1/pi) Im[i calJ]  -> delta(p^2) at tree level (properly normalized).
Cut definition (CLAIMS.md E24): sum_X (2pi)^D delta^D(p - p_X) <0|chi|X><X|chibar|0> = 2pi (nslash/2) nbar.p J 1_c  -> J^(0) = delta(p^2).
Run: python3 -I e24_jet.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp

npass = nfail = 0
def check(label, ok, extra=''):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(('PASS ' if ok else 'FAIL ') + label + (('   [' + str(extra) + ']') if extra else ''))

I2 = np.eye(2); Z2 = np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
g0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
gk = [np.block([[Z2, s], [-s, Z2]]) for s in (sx, sy, sz)]
G = [g0] + gk
met = np.diag([1., -1., -1., -1.])
def slash(v):
    return sum(met[m, m] * v[m] * G[m] for m in range(4))
def dot(a, b):
    return float(np.real(sum(met[m, m] * a[m] * b[m] for m in range(4))))
n = np.array([1., 0, 0, 1.]); nb = np.array([1., 0, 0, -1.])      # SCET: n = (1,0,0,1), nbar = (1,0,0,-1), n.nbar = 2
ns, nbs = slash(n), slash(nb)
Pn = ns @ nbs / 4; Pnb = nbs @ ns / 4
check('n.nbar = 2, P_n + Pbar_n... projector P_n^2 = P_n', abs(dot(n, nb) - 2) < 1e-14 and np.allclose(Pn @ Pn, Pn))
rng = np.random.default_rng(1)
ok = True
for _ in range(20):
    p = rng.normal(size=4)          # generic off-shell momentum
    ok &= np.allclose(Pn @ slash(p) @ Pnb, dot(nb, p) * ns / 2)
check('P_n pslash Pbar_n = (nslash/2) nbar.p for generic off-shell p  => collinear propagator (nslash/2) i nbar.p/(p^2+i0)', ok)
trD = np.trace((nbs / 2) @ (ns / 2))
check('Dirac trace tr[(nbarslash/2)(nslash/2)] = n.nbar = 2', abs(trD - 2) < 1e-14, trD.real)

# literal BS evaluation: coefficient multiplying nbar.p/(p^2 + i0) in  i * int e^{-ipx} <T chibar G chi>
Nc = sp.symbols('N_c', positive=True)
coef = sp.I * (-Nc) * sp.nsimplify(trD.real) * sp.I      # i * ( - N_c tr[G (nslash/2)] i )
check('i int d^4x e^{-ipx}<T chibar (nbarslash/2) chi> = +2 N_c nbar.p/(p^2+i0)  (free field)', sp.simplify(coef - 2 * Nc) == 0, coef)
# (1/pi) Im[1/(p^2 + i delta)] -> -delta(p^2): integrate over p^2
xr, dl = sp.symbols('x delta', positive=True)
xr_ = sp.Symbol('xr', real=True)
area = sp.integrate(sp.im(1 / (xr_ + sp.I * dl)).simplify(), (xr_, -sp.oo, sp.oo))
check('int dp^2 Im 1/(p^2 + i delta) = -pi, i.e. Im 1/(p^2+i0) = -pi delta(p^2)', sp.simplify(area + sp.pi) == 0)
J_lit = sp.simplify(coef * area / sp.pi)     # (1/nbar.p)(1/pi) * coef * nbar.p * Im[1/(p^2+i0)] integrated
check('BS eq. (2.6) read literally: J^(0) = -2 N_c delta(p^2)  (not delta(p^2))', sp.simplify(J_lit + 2 * Nc) == 0, J_lit)
check('needed normalisation factor -1/(2N_c) (sign from fermionic T-ordering, 1/2 from the Dirac trace, 1/N_c from colour)',
      sp.simplify(J_lit * (-1 / (2 * Nc)) - 1) == 0)
# with the opposite Fourier sign (e^{+ipx}) the result would be +2 N_c: still not delta(p^2)
coef_plus = sp.I * (-Nc) * sp.nsimplify(trD.real) * sp.I * (-1)   # k = -p: nbar.k = -nbar.p
check('even with e^{+ipx} (or without the fermion sign) |J^(0)| = 2 N_c delta(p^2): the normalisation is off in any reading',
      abs(sp.simplify(coef_plus * area / sp.pi)) == 2 * Nc)

# Becher-Neubert 2006 normalised definition: (nslash/2) nbar.p calJ = int e^{-ipx} <T X(0) Xbar(x)> = (nslash/2) i nbar.p/(p^2+i0)
calJ_coef = sp.I                                           # calJ = i/(p^2+i0)
J_BN = sp.simplify(sp.I * calJ_coef * area / sp.pi)        # (1/pi) Im[i calJ] = (1/pi) Im[-1/(p^2+i0)]
check('Becher-Neubert 2006 definition gives J^(0) = +delta(p^2)', sp.simplify(J_BN - 1) == 0, J_BN)

# cut definition: sum_s P_n u ubar Pbar_n = (nslash/2) nbar.p for on-shell p; phase space int d^Dk/(2pi)^{D-1} delta^+(k^2)
def u_spinor(p, s):
    E = p[0]; pv = p[1:]
    chi = np.array([1, 0], complex) if s == 0 else np.array([0, 1], complex)
    sigp = pv[0] * sx + pv[1] * sy + pv[2] * sz
    return np.sqrt(E) * np.concatenate([chi, (sigp @ chi) / E])   # massless, Dirac rep (normalisation ubar gamma^0 u = 2E)
ok = True
for _ in range(10):
    k3 = rng.normal(size=3); p = np.concatenate([[np.linalg.norm(k3)], k3])
    uu = sum(np.outer(u_spinor(p, s), u_spinor(p, s).conj() @ g0) for s in (0, 1))
    ok &= np.allclose(uu, slash(p)) and np.allclose(Pn @ uu @ Pnb, dot(nb, p) * ns / 2)
check('sum_s u ubar = pslash and P_n (sum u ubar) Pbar_n = (nslash/2) nbar.p (on shell)', ok)
print('   => sum_X (2pi)^D delta^D(p-p_X)<0|chi|X><X|chibar|0> = int d^Dk/(2pi)^{D-1} delta^+(k^2) (2pi)^D delta^D(p-k) (nslash/2) nbar.k 1_c')
print('      = 2pi delta(p^2) theta(p^0) (nslash/2) nbar.p 1_c  => J^(0) = delta(p^2) with the cut definition (normalised).')
print('-' * 70)
print('e24_jet: %d PASS, %d FAIL' % (npass, nfail))
