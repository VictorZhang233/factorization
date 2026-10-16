# -*- coding: utf-8 -*-
"""
lo_check.py -- Drell-Yan at leading order: every factor of
    dsigma/dQ^2 = 4 pi alpha^2/(3 N_c Q^2 s) sum_q e_q^2 int dx1 dx2 delta(x1 x2 - tau)[q(x1)qbar(x2)+qbar(x1)q(x2)]
and of its rapidity-differential version.

Checks:
 (A) lepton tensor integrated over the 2-body phase space (4D, massless leptons):
        int dPhi_2 L_{mu nu} = (1/(6 pi)) (q_mu q_nu - q^2 g_{mu nu}),  L_{mu nu} = Tr[l1 g_mu l2 g_nu]
     -- exact (sympy, angular average in the q rest frame) and numerically in a boosted frame;
 (B) sigma(q qbar -> gamma* -> l+ l-) = 4 pi alpha^2 e_q^2 /(3 N_c shat) from explicit 4x4 Dirac matrices and
     explicit spinors (independent of dtrace.py), incl. colour average; angular distribution (1+cos^2 theta);
 (C) general master formula  shat dsigma/dQ^2 = (2 alpha^2/(3 Q^2)) int dPhi_{gamma* X} <-g_{mu nu} H^mu H^nu*>,
     derived step by step; Born limit reproduces sigma_0 e_q^2 delta(1-z), sigma_0 = 4 pi alpha^2/(3 N_c Q^2);
 (D) hadronic formulae (mass and rapidity) with toy PDFs: int dy d^2sigma/dQ^2 dy = dsigma/dQ^2 (numerically),
     and the light-front kinematics of CONTEXT.md (x1 = q^+/P_A^+, x2 = q^-/P_B^-, y = (1/2) ln(q^+/q^-)).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
from scipy import integrate

PASS = []


def report(name, ok, extra=''):
    PASS.append((name, ok))
    print('[%s] %s %s' % ('PASS' if ok else 'FAIL', name, extra))


# ---------------------------------------------------------------- (A) lepton tensor
Q = sp.Symbol('Q', positive=True)
th, ph = sp.symbols('theta phi', real=True)
g4 = sp.diag(1, -1, -1, -1)
n = sp.Matrix([sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)])
l1 = sp.Matrix([Q / 2, *(Q / 2 * n)])
l2 = sp.Matrix([Q / 2, *(-Q / 2 * n)])
low = lambda v: g4 * v
dot4 = lambda a, b: (a.T * g4 * b)[0]
L = sp.zeros(4, 4)  # L_{mu nu} with lower indices
for m in range(4):
    for nn in range(4):
        L[m, nn] = 4 * (low(l1)[m] * low(l2)[nn] + low(l1)[nn] * low(l2)[m] - g4[m, nn] * dot4(l1, l2))
# dPhi_2 (massless, 4D, q rest frame) = (1/(8 pi)) dOmega/(4 pi)
Lint = sp.zeros(4, 4)
for m in range(4):
    for nn in range(4):
        Lint[m, nn] = sp.simplify(sp.integrate(sp.integrate(L[m, nn] * sp.sin(th), (th, 0, sp.pi)), (ph, 0, 2 * sp.pi)) / (4 * sp.pi) / (8 * sp.pi))
qv = sp.Matrix([Q, 0, 0, 0])
target = sp.zeros(4, 4)
for m in range(4):
    for nn in range(4):
        target[m, nn] = (low(qv)[m] * low(qv)[nn] - Q**2 * g4[m, nn]) / (6 * sp.pi)
report('(A) int dPhi_2 L_{mu nu} = (q_mu q_nu - q^2 g_{mu nu})/(6 pi)  [exact, rest frame]', sp.simplify(Lint - target) == sp.zeros(4, 4))

# numerical check in a boosted frame (Monte Carlo over the rest-frame angles, then boost)
rng = np.random.default_rng(7)
Qn = 3.7
beta = np.array([0.3, -0.2, 0.6])
gam = 1 / np.sqrt(1 - beta @ beta)
def boost(p):
    E, v = p[0], p[1:]
    bp = beta @ v
    E2 = gam * (E + bp)
    v2 = v + ((gam - 1) * bp / (beta @ beta) + gam * E) * beta
    return np.array([E2, *v2])
G = np.diag([1., -1, -1, -1])
Nmc = 200000
ct = rng.uniform(-1, 1, Nmc); phi = rng.uniform(0, 2 * np.pi, Nmc)
st = np.sqrt(1 - ct**2)
nvec = np.stack([st * np.cos(phi), st * np.sin(phi), ct], axis=1)
L1 = np.concatenate([np.full((Nmc, 1), Qn / 2), Qn / 2 * nvec], axis=1)
L2 = np.concatenate([np.full((Nmc, 1), Qn / 2), -Qn / 2 * nvec], axis=1)
def boostv(P):
    E = P[:, 0]; v = P[:, 1:]
    bp = v @ beta
    E2 = gam * (E + bp)
    v2 = v + (((gam - 1) * bp / (beta @ beta) + gam * E)[:, None]) * beta[None, :]
    return np.concatenate([E2[:, None], v2], axis=1)
L1b, L2b = boostv(L1), boostv(L2)
l1low = L1b @ G; l2low = L2b @ G
l1l2 = np.einsum('ni,ij,nj->n', L1b, G, L2b)
Lmc = 4 * (np.einsum('ni,nj->ij', l1low, l2low) + np.einsum('ni,nj->ij', l2low, l1low) - G * l1l2.sum()) / Nmc / (8 * np.pi)
qb = boost(np.array([Qn, 0, 0, 0])); qlow = G @ qb
Ltarget = (np.outer(qlow, qlow) - Qn**2 * G) / (6 * np.pi)
err = np.max(np.abs(Lmc - Ltarget)) / np.max(np.abs(Ltarget))
report('(A) same identity in a boosted frame (Monte Carlo, %d points)' % Nmc, err < 1e-2, '(max rel. dev. %.1e, statistical)' % err)

# ---------------------------------------------------------------- (B) partonic cross section from explicit matrices
g0 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]], dtype=complex)  # Dirac rep.
sx = np.array([[0, 1], [1, 0]], dtype=complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], dtype=complex)
def gk(s):
    m = np.zeros((4, 4), dtype=complex); m[:2, 2:] = s; m[2:, :2] = -s; return m
GAM = [g0, gk(sx), gk(sy), gk(sz)]
def slash(p):
    return GAM[0] * p[0] - GAM[1] * p[1] - GAM[2] * p[2] - GAM[3] * p[3]
def u_spinors(p):
    """massless u(p,s), s=1,2 (Dirac rep., normalised u^dag u = 2E)"""
    E = p[0]; out = []
    for chi in (np.array([1, 0], dtype=complex), np.array([0, 1], dtype=complex)):
        sp_ = p[1] * sx + p[2] * sy + p[3] * sz
        out.append(np.concatenate([np.sqrt(E) * chi, (sp_ @ chi) / np.sqrt(E)]) )
    return out
def v_spinors(p):
    E = p[0]; out = []
    for chi in (np.array([1, 0], dtype=complex), np.array([0, 1], dtype=complex)):
        sp_ = p[1] * sx + p[2] * sy + p[3] * sz
        out.append(np.concatenate([(sp_ @ chi) / np.sqrt(E), np.sqrt(E) * chi]))
    return out
bar = lambda w: w.conj() @ g0
# completeness checks
pt = np.array([2.0, 0.6, -1.2, np.sqrt(4 - 0.36 - 1.44)])
okc = np.allclose(sum(np.outer(w, bar(w)) for w in u_spinors(pt)), slash(pt)) and np.allclose(sum(np.outer(w, bar(w)) for w in v_spinors(pt)), slash(pt))
report('(B) explicit massless spinors satisfy sum u ubar = sum v vbar = pslash', okc)

alpha = 1 / 137.0; e2 = 4 * np.pi * alpha; Nc = 3; eq = 2 / 3
shat = 10.0; E = np.sqrt(shat) / 2
p1 = np.array([E, 0, 0, E]); p2 = np.array([E, 0, 0, -E])
def msq_avg(cth, phi_=0.3):
    sth = np.sqrt(1 - cth**2)
    l1_ = np.array([E, E * sth * np.cos(phi_), E * sth * np.sin(phi_), E * cth])
    l2_ = np.array([E, -l1_[1], -l1_[2], -l1_[3]])
    tot = 0.0
    for up in u_spinors(p1):
        for vb in v_spinors(p2):
            for ul in u_spinors(l1_):
                for vl in v_spinors(l2_):
                    # M = (e^2 e_q / shat) [vbar(p2) g^mu u(p1)] [ubar(l1) g_mu v(l2)]  (|M| independent of overall phase)
                    amp = 0
                    for mu in range(4):
                        sgn = 1 if mu == 0 else -1
                        amp += sgn * (bar(vb) @ GAM[mu] @ up) * (bar(ul) @ GAM[mu] @ vl)
                    tot += abs(e2 * eq / shat * amp)**2
    # colour: (1/N_c^2) sum_{ij} delta_ij delta_ij = 1/N_c ; spin average 1/4
    return tot / 4 / Nc
cths = np.linspace(-0.9, 0.9, 7)
vals = np.array([msq_avg(c) for c in cths])
ang = vals / vals[3]
report('(B) angular distribution  |M|^2 ~ (1+cos^2 theta)', np.allclose(ang, (1 + cths**2) / (1 + cths[3]**2)))
sig, _ = integrate.quad(lambda c: msq_avg(c) * 2 * np.pi / (64 * np.pi**2 * shat), -1, 1, epsabs=0, epsrel=1e-10)
sig_exp = 4 * np.pi * alpha**2 * eq**2 / (3 * Nc * shat)
report('(B) sigma(q qbar -> l+ l-) = 4 pi alpha^2 e_q^2/(3 N_c shat)', abs(sig / sig_exp - 1) < 1e-9, '(ratio %.12f)' % (sig / sig_exp))

# ---------------------------------------------------------------- (C) master formula, symbolic bookkeeping
al, Q2, sh, Ncs, eqs = sp.symbols('alpha Q2 shat N_c e_q', positive=True)
# |M|^2 summed over lepton spins = (e^4/Q^4) L_{mu nu} H^mu H^nu*  ; int dPhi_ll L = (Q^2/(6pi)) (-g) on conserved H
e4 = (4 * sp.pi * al)**2
lept = e4 / Q2**2 * Q2 / (6 * sp.pi)          # multiplies <-g_{mu nu} H^mu H^nu*>
# d^4q/(2pi)^4 = dQ^2/(2pi) * d^3q/((2pi)^3 2q^0) ; flux 1/(2 shat)
pref = sp.simplify(sh * (1 / (2 * sh)) * (1 / (2 * sp.pi)) * lept)   # shat dsigma/dQ^2 = pref * int dPhi <-gHH>
report('(C) shat dsigma/dQ^2 = (2 alpha^2/(3 Q^2)) int dPhi_{gamma* X} <-g H H*>', sp.simplify(pref - 2 * al**2 / (3 * Q2)) == 0, '  [pref = %s]' % pref)
# Born: int dPhi_{gamma*} = 2 pi delta(shat - Q^2);  <-gHH*> = e_q^2 (D-2) 2 shat /(4 N_c) -> e_q^2 shat/N_c in D=4
born = pref * 2 * sp.pi * eqs**2 * sh / Ncs     # times delta(shat - Q^2) ; shat delta(shat-Q^2) = delta(1-z) (z=Q^2/shat)
sigma0 = 4 * sp.pi * al**2 / (3 * Ncs * Q2)
report('(C) Born: shat dsigma/dQ^2 = sigma_0 e_q^2 shat delta(shat-Q^2) = sigma_0 e_q^2 delta(1-z)', sp.simplify(born / sh - sigma0 * eqs**2) == 0)

# ---------------------------------------------------------------- (D) hadronic formulae with toy PDFs
def q_toy(x):  return 1.7 * x**-0.4 * (1 - x)**3.2
def qb_toy(x): return 0.4 * x**-1.1 * (1 - x)**7.0
s_had = 1.0e4; Q2v = 100.0; tau = Q2v / s_had; Nc_ = 3
pref_h = 4 * np.pi * alpha**2 / (3 * Nc_ * Q2v * s_had) * eq**2
# mass distribution: int dx1 dx2 delta(x1 x2 - tau) F = int_tau^1 dx1/x1 F(x1, tau/x1)
F = lambda x1, x2: q_toy(x1) * qb_toy(x2) + qb_toy(x1) * q_toy(x2)
mass, _ = integrate.quad(lambda x1: F(x1, tau / x1) / x1, tau, 1, epsabs=0, epsrel=1e-11, limit=200)
dsdQ2 = pref_h * mass
# rapidity distribution: x1,2 = sqrt(tau) e^{+-y}, |y| <= (1/2) ln(1/tau), Jacobian 1
ymax = 0.5 * np.log(1 / tau)
d2 = lambda y: pref_h * F(np.sqrt(tau) * np.exp(y), np.sqrt(tau) * np.exp(-y))
yint, _ = integrate.quad(d2, -ymax, ymax, epsabs=0, epsrel=1e-11, limit=200)
report('(D) int dy d^2sigma/dQ^2dy = dsigma/dQ^2 (Jacobian dx1 dx2 = dy d(x1x2))', abs(yint / dsdQ2 - 1) < 1e-9, '(ratio %.12f)' % (yint / dsdQ2))
# Jacobian symbolically
x1, x2, y, T = sp.symbols('x1 x2 y T', positive=True)
J = sp.Matrix([[sp.diff(sp.sqrt(T) * sp.exp(y), y), sp.diff(sp.sqrt(T) * sp.exp(y), T)], [sp.diff(sp.sqrt(T) * sp.exp(-y), y), sp.diff(sp.sqrt(T) * sp.exp(-y), T)]]).det()
report('(D) |d(x1,x2)/d(y,x1x2)| = 1', sp.simplify(sp.Abs(J) - 1) == 0, '(det = %s)' % sp.simplify(J))
# light-front kinematics (CONTEXT): P_A = (P^+, M^2/(2P^+), 0), P_B along -z ; q^+ = x1 P_A^+, q^- = x2 P_B^-
PAp, PBm, MA, MB = sp.symbols('P_A^+ P_B^- M_A M_B', positive=True)
PA = (PAp, MA**2 / (2 * PAp)); PB = (MB**2 / (2 * PBm), PBm)   # (plus, minus) components, T = 0
s_exact = MA**2 + MB**2 + 2 * (PA[0] * PB[1] + PA[1] * PB[0])
qp, qm = x1 * PAp, x2 * PBm
Q2_lf = 2 * qp * qm
yLF = sp.Rational(1, 2) * sp.log(qp / qm)
ok_lf = sp.simplify(Q2_lf.subs(PBm, PAp) - x1 * x2 * 2 * PAp**2) == 0 and sp.simplify(sp.expand_log(yLF.subs(PBm, PAp), force=True) - sp.Rational(1, 2) * sp.log(x1 / x2)) == 0
report('(D) LF kinematics: Q^2 = 2q^+q^- = x1 x2 (2P_A^+P_B^-), y = (1/2)ln(x1/x2) in the frame P_A^+ = P_B^-', ok_lf)
ratio = sp.simplify(sp.series((2 * PAp * PBm / s_exact).subs({MA: sp.Symbol('m') * sp.Symbol('lam'), MB: sp.Symbol('m') * sp.Symbol('lam')}), sp.Symbol('lam'), 0, 3).removeO())
print('      2P_A^+P_B^-/s = %s   (hadron masses: x1 x2 = tau [1 + O(M^2/s)])' % ratio)
print('      numbers: tau=%.3g, dsigma/dQ^2 = %.6e GeV^-4 (alpha=1/137, single flavour e_q=2/3, toy PDFs)' % (tau, dsdQ2))

print()
print('SUMMARY lo_check: %d/%d PASS' % (sum(ok for _, ok in PASS), len(PASS)))
