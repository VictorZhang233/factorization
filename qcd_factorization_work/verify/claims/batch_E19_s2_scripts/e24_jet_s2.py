#!/usr/bin/env python3
"""E24 (stage 2): normalization of the Becher-Schwartz jet function, JHEP 07 (2008) 034 eq. (2.6)
(identical in arXiv:0803.0342 v1, v2):
    J(p^2) = 1/(nbar.p) (1/pi) Im[ i int d^4x e^{-ipx} <0|T{ chibar_n(x) (nbarslash/2) chi_n(0) }|0> ]  "= delta(p^2) + O(as)".
Method (different from stage 1): canonical MODE EXPANSION of the free massless field, explicit
theta-function decomposition of the fermionic T-product, explicit spinor sums in the Dirac representation,
explicit time integrals with convergence factor e^{-eta|t|}; no Feynman-propagator shortcut.
Also: Becher-Neubert PLB 637 (2006) 251 [hep-ph/0603140] eqs. (eq:Jscet), (J = Im[i calJ]/pi), and the
cut definition sum_X (2pi)^4 delta^4(p - p_X) <0|chi|X><X|chibar|0> = 2pi (nslash/2) nbar.p J(p^2) 1_c.
Run: python3 -I e24_jet_s2.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
PASS = []
def check(name, ok, info=''):
    PASS.append(bool(ok)); print(('PASS ' if ok else 'FAIL ') + name + ('  ' + info if info else ''))

# ---------- Dirac representation
I2 = np.eye(2); Z2 = np.zeros((2, 2))
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.array([[1, 0], [0, -1]], complex)]
g0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
gam = [g0] + [np.block([[Z2, s], [-s, Z2]]) for s in sig]
eta_m = np.diag([1., -1., -1., -1.])
def sl(v): vl = eta_m @ v; return sum(gam[m]*vl[m] for m in range(4))
n = np.array([1, 0, 0, 1.]); nb = np.array([1, 0, 0, -1.])           # n.nbar = 2 (BS / SCET convention)
Pn = sl(n) @ sl(nb)/4; Pnb = sl(nb) @ sl(n)/4
rng = np.random.default_rng(7)
ok = True
for _ in range(20):
    p = rng.normal(size=4)                                            # off shell
    ok &= np.allclose(Pn @ sl(p) @ Pnb, sl(n)/2*(p @ eta_m @ nb))
check('(1) P_n pslash Pbar_n = (nslash/2) nbar.p, exactly, off shell (20 random p)', ok)
check('(2) Dirac trace tr[(nbarslash/2)(nslash/2)] = n.nbar = 2', np.isclose(np.trace(sl(nb)/2 @ sl(n)/2), 2))
check('(2b) chibar = psibar Pbar_n with Pbar_n = gamma0 P_n^dagger gamma0', np.allclose(g0 @ Pn.conj().T @ g0, Pnb))

# ---------- massless spinors and spin sums (Dirac rep.)
def u_sp(k, s):
    E = k[0]; kv = k[1:]; chi = np.eye(2)[s]
    return np.sqrt(E)*np.concatenate([chi, (sum(kv[i]*sig[i] for i in range(3)) @ chi)/E])
def v_sp(k, s):
    E = k[0]; kv = k[1:]; eta_ = np.eye(2)[s]
    return np.sqrt(E)*np.concatenate([(sum(kv[i]*sig[i] for i in range(3)) @ eta_)/E, eta_])
kv = rng.normal(size=3); k = np.concatenate([[np.linalg.norm(kv)], kv])
Suu = sum(np.outer(u_sp(k, s), u_sp(k, s).conj() @ g0) for s in (0, 1))
Svv = sum(np.outer(v_sp(k, s), v_sp(k, s).conj() @ g0) for s in (0, 1))
check('(3) massless spin sums: sum u ubar = kslash, sum v vbar = kslash (m = 0)', np.allclose(Suu, sl(k)) and np.allclose(Svv, sl(k)))

# ---------- mode expansion of <0|T chibar_a(x) Gamma_ab chi_b(0)|0>, fermionic T-ordering
#  x0>0 : <0|chibar_a(x) chi_b(0)|0> Gamma_ab = int dk~ tr[Gamma Pn (sum v vbar) Pnb] e^{-ik.x}
#  x0<0 : -<0|chi_b(0) chibar_a(x)|0> Gamma_ab = - int dk~ tr[Gamma Pn (sum u ubar) Pnb] e^{+ik.x}
# Fourier transform i int d^4x e^{-ip.x}: spatial integrals fix kvec = -pvec (first) and kvec = +pvec (second);
# time integrals with e^{-eta|t|}:
t, p0, E, eta = sp.symbols('t p0 E eta', positive=True)
T1 = sp.integrate(sp.exp(-sp.I*(p0 + E)*t - eta*t), (t, 0, sp.oo), conds='none')        # theta(t) e^{-i(p0+E)t}
T2 = sp.integrate(sp.exp(sp.I*(E - p0)*t + eta*t), (t, -sp.oo, 0), conds='none')        # theta(-t) e^{+i(E-p0)t}
check('(4) time integrals: -i/(p0+E-i eta) and +i/(p0-E+i eta)',
      sp.simplify(T1 - (-sp.I/(p0 + E - sp.I*eta))) == 0 and sp.simplify(T2 - (sp.I/(p0 - E + sp.I*eta))) == 0)
V0, Vx, Vy, Vz, px, py, pz = sp.symbols('V0 Vx Vy Vz px py pz', real=True)
Ev = sp.sqrt(px**2 + py**2 + pz**2)
def trGk(k0, kx, ky, kz):              # tr[Gamma kslash] = V.k  with V^mu = tr[Gamma gamma^mu] (generic linear functional)
    return V0*k0 - (Vx*kx + Vy*ky + Vz*kz)
T1s, T2s = sp.simplify(T1), sp.simplify(T2)                # bring to -i/(p0+E-i eta), i/(p0-E+i eta) before eta -> 0
first = sp.I*(1/(2*E))*trGk(E, -px, -py, -pz)*T1s          # i * [ +theta(t) term ]
second = sp.I*(-1)*(1/(2*E))*trGk(E, px, py, pz)*T2s       # i * [ -theta(-t) term ]
tot = sp.simplify(sp.limit(first + second, eta, 0).subs(E, Ev))
p2 = p0**2 - Ev**2
target = (V0*p0 - (Vx*px + Vy*py + Vz*pz))/p2
check('(5) i int d^4x e^{-ipx} <T psibar(x) Gamma psi(0)> = tr[Gamma pslash]/(p^2 + i0)  (eta -> 0)', sp.simplify(tot - target) == 0)
# sign of i0: near p0 = +E, denominator of the second term is p0 - E + i eta  ->  p^2 + i0
check('(5b) i0 prescription: (p0+E-i eta)(p0-E+i eta) = p^2 + 2 i eta E + O(eta^2)  ->  p^2 + i0',
      sp.simplify(sp.expand((p0 + E - sp.I*eta)*(p0 - E + sp.I*eta)) - (p0**2 - E**2 + 2*sp.I*eta*E + eta**2)) == 0)

# ---------- assemble BS literal: Gamma = nbarslash/2, chi = P_n psi, colour trace N_c
#  tr[Gamma Pn pslash Pnb] = tr[(nbarslash/2)(nslash/2)] nbar.p = 2 nbar.p
Nc, nbp, P2 = sp.symbols('N_c nbarp P2', positive=True)
x_ = sp.symbols('x', real=True)
# (1/pi) Im[1/(p^2 + i eta)] -> -delta(p^2): check numerically against a test function
f = lambda s: np.exp(-(s - 0.3)**2)*(1 + s**2)
grid = np.linspace(-40, 40, 4000001); hgrid = grid[1] - grid[0]
for et in (1e-2, 1e-3):
    val = np.sum(f(grid)*(1/np.pi)*np.imag(1/(grid + 1j*et)))*hgrid
    print(f'   (1/pi) int ds f(s) Im[1/(s + i{et:g})] = {val:.6f}   (-f(0) = {-f(0):.6f})')
check('(6) (1/pi) Im 1/(p^2 + i0) = -delta(p^2)', abs(val + f(0)) < 2e-3)
J_literal = (1/nbp)*(1/sp.pi)*(2*Nc*nbp)*(-sp.pi)        # coefficient of delta(p^2)
check('(7) BS eq. (2.6) read literally gives J = -2 N_c delta(p^2)  (not +delta)', sp.simplify(J_literal + 2*Nc) == 0, f'J = {J_literal} delta(p^2)')
J_opposite_FT = (1/nbp)*(1/sp.pi)*(2*Nc*(-nbp))*(-sp.pi)
check('(7b) with e^{+ipx} instead: +2 N_c delta(p^2); the factor 2N_c is there in any reading', sp.simplify(J_opposite_FT - 2*Nc) == 0)
# ---------- Becher-Neubert 2006 normalization: (nslash/2) nbar.p calJ = int e^{-ipx} <T chi(0) chibar(x)>
#  <T psi_b(0) psibar_a(x)> = - <T psibar_a(x) psi_b(0)> (fermionic T) => int e^{-ipx}<T psi(0) psibar(x)> = (1/i)(-1)(-1)... :
#  from (5): i int e^{-ipx}<T psibar_a(x) psi_b(0)> = pslash_ba/(p^2+i0) => int e^{-ipx}<T psi_b(0)psibar_a(x)> = i pslash_ba/(p^2+i0)
calJ = sp.I/(P2 + sp.I*eta)                               # (nslash/2) nbar.p calJ = i (nslash/2) nbar.p/(p^2+i0)
J_BN = sp.limit((1/sp.pi)*sp.im(sp.expand_complex(sp.I*calJ)), eta, 0, '+')
print('   BN 2006: (1/pi) Im[i calJ] at p^2 != 0 ->', J_BN, '; the eta -> 0 limit is +delta(p^2) since Im[-1/(s+i eta)] = +pi delta(s)')
check('(8) Becher-Neubert 2006 definition (matrix-valued, chi(0) chibar(x) order): J = +delta(p^2)',
      sp.simplify((1/sp.pi)*sp.im(sp.expand_complex(sp.I*calJ)) - (1/sp.pi)*eta/(P2**2 + eta**2)) == 0)
# ---------- cut definition: one-quark states, sum_X = sum_{s,c} int d^3k/((2pi)^3 2E)
#  => (2pi) delta(p^2) theta(p0) Pn pslash Pnb 1_c = 2pi (nslash/2) nbar.p delta(p^2) 1_c   => J^(0) = delta(p^2)
p = np.concatenate([[1.7], 1.7*np.array([0.3, -0.4, np.sqrt(1 - 0.25)])])
lhs = sum(Pn @ np.outer(u_sp(p, s), u_sp(p, s).conj() @ g0) @ Pnb for s in (0, 1))
check('(9) cut definition: sum_s Pn u ubar Pnb = (nslash/2) nbar.p  =>  J^(0) = delta(p^2) theta(p0)',
      np.allclose(lhs, sl(n)/2*(p @ eta_m @ nb)))
check('(10) implicit normalization of BS eq. (2.6): multiply by -1/(2N_c) (T-ordering sign, 1/2 Dirac, 1/N_c colour)',
      sp.simplify(J_literal*(-1/(2*Nc)) - 1) == 0)
print(f'\nSUMMARY: {sum(PASS)}/{len(PASS)} PASS')
