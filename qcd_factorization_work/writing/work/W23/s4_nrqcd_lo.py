# -*- coding: utf-8 -*-
"""
s4_nrqcd_lo.py -- Ch20 sec:heavy-nrqcd: velocity power counting (VF-NRQ-1), P-wave counting, BBL convention
 (G^BBL = -G), Foldy-Wouthuysen identity (sigma.D)^2 = D^2 + sigma^k (i/2) eps^{kij}[D_i, D_j] (convention-free
 Fermi term), and the LO electromagnetic widths from explicit threshold amplitudes (VF-NRQ-2, VF-NRQ-3) with the
 BBL normalization Im f_ee = pi e_Q^2 alpha^2/3, Im f_gg = pi e_Q^4 alpha^2; para-positronium limit.
Run: python3 -I s4_nrqcd_lo.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w23common import *
import numpy as np

ck = Check('s4_nrqcd_lo: velocity rules, conventions, FW identity, LO EM widths and BBL normalization')

# ------------------------------------------------------------------------------------------- A velocity rules
m, v = sp.symbols('m v', positive=True)
sc = {'psi': (m * v)**sp.Rational(3, 2), 'D': m * v, 'Dt': m * v**2, 'gE': m**2 * v**3, 'gB': m**2 * v**4, 'as': v}
vpow = lambda e: sp.degree(sp.expand(e).subs(m, 1), v)
LO = sc['psi']**2 * sc['Dt']
ck('normalization int d^3x psi^dag psi ~ 1 over volume (mv)^-3  =>  psi ~ (mv)^{3/2}', sp.simplify(sc['psi']**2 * (m * v)**-3) == 1)
ck('Schroedinger balance: psi^dag D^2/(2m) psi ~ psi^dag i D_t psi  (D_t ~ m v^2)', sp.simplify(sc['psi']**2 * sc['D']**2 / m - LO) == 0)
ck('Gauss law D.gE ~ g^2 psi^dag psi:  gE ~ alpha_s(mv) (mv)^2 ~ m^2 v^3', sp.simplify(sc['D'] * sc['gE'] - sc['as'] * sc['psi']**2) == 0)
ck('Ampere law D x gB ~ D_t gE ~ g^2 j, j ~ psi^dag D psi/m:  gB ~ m^2 v^4',
   vpow(sc['D'] * sc['gB']) == vpow(sc['Dt'] * sc['gE']) == vpow(sc['as'] * sc['psi']**2 * sc['D'] / m))
bil = {'D^4/(8m^3)': sc['psi']**2 * sc['D']**4 / m**3, 'Fermi gB/(2m)': sc['psi']**2 * sc['gB'] / m,
       'Darwin [D.,gE]/(8m^2)': sc['psi']**2 * sc['D'] * sc['gE'] / m**2, 'spin-orbit D x gE/(8m^2)': sc['psi']**2 * sc['D'] * sc['gE'] / m**2}
ck('all bilinear corrections are O(v^2) relative to the LO terms', all(vpow(e) - vpow(LO) == 2 for e in bil.values()),
   ', '.join('%s: v^%d' % (kk, vpow(e) - vpow(LO)) for kk, e in bil.items()))
S_wave = (m * v)**3 / m**2          # <O_1(S)> ~ |psi(0)|^2 ~ (mv)^3, divided by m^{d-4} = m^2
P_wave = (m * v)**5 / m**4          # dimension-8 P-wave singlet
octet_in_chiJ = v**2 * (m * v)**3 / m**2
ck('Gamma(S wave) ~ m v^3; Gamma(P-wave singlet) ~ m v^5 ~ Gamma(octet 3S1 component of chi_J)',
   vpow(S_wave) == 3 and vpow(P_wave) == 5 and vpow(octet_in_chiJ) == 5)

# ------------------------------------------------------------------------------------------- B conventions
# Abelian check of the commutator conventions with explicit functions; non-abelian structure is identical.
X = sp.symbols('x0:4'); gc = sp.symbols('g', positive=True)
Afun = [sp.Function('A%d' % i)(*X) for i in range(4)]
fn = sp.Function('f')(*X)
D_ours = lambda mu_, F: sp.diff(F, X[mu_]) - sp.I * gc * Afun[mu_] * F          # D = d - i g A  (lower index)
D_BBL = lambda mu_, F: sp.diff(F, X[mu_]) + sp.I * gc * (-Afun[mu_]) * F       # D = d + i g A^BBL, A^BBL = -A
same = all(sp.simplify(D_ours(mu_, fn) - D_BBL(mu_, fn)) == 0 for mu_ in range(4))
ck('D = d - i g A (ours) and D = d + i g A^BBL are the same operator iff A^BBL = -A', same)
comm = sp.simplify(D_ours(0, D_ours(1, fn)) - D_ours(1, D_ours(0, fn)))
G01 = sp.diff(Afun[1], X[0]) - sp.diff(Afun[0], X[1])
ck('[D_0, D_1] = -i g G_01 (ours)  and  = +i g G^BBL_01 with G^BBL = -G', sp.simplify(comm - (-sp.I * gc * G01 * fn)) == 0 and
   sp.simplify(comm - (sp.I * gc * (-G01) * fn)) == 0)
# FW identity: (sigma.D)^2 = D^2 + sigma^k (i/2) eps^{kij} [D_i, D_j]  (any convention) -- check with Pauli matrices
s1 = sp.Matrix([[0, 1], [1, 0]]); s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]]); s3 = sp.Matrix([[1, 0], [0, -1]])
sig = [s1, s2, s3]
Dc = sp.symbols('D1:4', commutative=False)
lhs = sum((sig[i] * Dc[i] for i in range(3)), sp.zeros(2, 2))
lhs2 = sp.expand(lhs * lhs)
rhs = sp.eye(2) * sum(Dc[i] * Dc[i] for i in range(3))
for kidx in range(3):
    for i in range(3):
        for j in range(3):
            e = sp.LeviCivita(kidx + 1, i + 1, j + 1)
            if e != 0:
                rhs += sig[kidx] * (sp.I / 2) * e * (Dc[i] * Dc[j] - Dc[j] * Dc[i])
ck('(sigma.D)^2 = D^2 + sigma^k (i/2) eps^{kij} [D_i, D_j] (non-commuting D_i)', sp.expand(lhs2 - rhs) == sp.zeros(2, 2))
# in our convention (i/2) eps^{kij}[D_i,D_j] = (i/2) eps^{kij} (-i g G_ij) = g (1/2) eps^{kij} G^{ij} = g B^k
ck('our convention: (i/2) eps^{kij}[D_i,D_j] = (g/2) eps^{kij} G^{ij} =: g B^k  (Fermi term + c_F g sigma.B/(2m))',
   sp.simplify(sp.I / 2 * (-sp.I * gc) - gc / 2) == 0)
ck('BBL convention: the same commutator equals -(g/2) eps^{kij} G^{BBL ij} = -g B^k_BBL', sp.simplify(sp.I / 2 * (sp.I * gc) + gc / 2) == 0)

# ------------------------------------------------------------------------------------------- C LO widths (numerics)
I2 = np.eye(2); Z2 = np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
G0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
Gi = [np.block([[Z2, s], [-s, Z2]]) for s in (sx, sy, sz)]
Gam = [G0] + Gi
G5 = 1j * Gam[0] @ Gam[1] @ Gam[2] @ Gam[3]
metric = np.diag([1., -1, -1, -1])
def sl(pv):
    pl = metric @ pv
    return sum(Gam[i] * pl[i] for i in range(4))
I4 = np.eye(4, dtype=complex)
def bar(M):
    return G0 @ M.conj().T @ G0
mq = 1.6
p = np.array([mq, 0, 0, 0.])
def Pi_in(Gs):              # sum CG u(p,s) vbar(pbar,sbar), incoming Q Qbar at threshold (ubar u = 2m)
    return (sl(p) + mq * I4) @ Gs @ (sl(p) - mq * I4) / (2 * np.sqrt(2) * mq)
eps = [np.array([0, 1., 0, 0]), np.array([0, 0, 1., 0]), np.array([0, 0, 0, 1.])]
P0 = Pi_in(G5); P1 = [Pi_in(sl(e)) for e in eps]
ck('projector normalization Tr[Pibar Pi] = -4 m^2 (singlet and triplets), triplets orthogonal, singlet orthogonal to triplet',
   abs(np.trace(bar(P0) @ P0) + 4 * mq**2) < 1e-12 and all(abs(np.trace(bar(P1[i]) @ P1[j]) + 4 * mq**2 * (i == j)) < 1e-12 for i in range(3) for j in range(3))
   and all(abs(np.trace(bar(P0) @ P)) < 1e-12 for P in P1))
# spinors to confirm Pi lies in span{u vbar}
def u_sp(pv, s):
    E = pv[0]; pvec = pv[1:]; chi = np.array([1, 0], complex) if s == 0 else np.array([0, 1], complex)
    sp_ = sum(pvec[i] * [sx, sy, sz][i] for i in range(3))
    return np.sqrt(E + mq) * np.concatenate([chi, sp_ @ chi / (E + mq)])
def v_sp(pv, s):
    E = pv[0]; pvec = pv[1:]; chi = np.array([0, 1], complex) if s == 0 else np.array([-1, 0], complex)
    sp_ = sum(pvec[i] * [sx, sy, sz][i] for i in range(3))
    return np.sqrt(E + mq) * np.concatenate([sp_ @ chi / (E + mq), chi])
basis = np.array([np.outer(u_sp(p, s), v_sp(p, t).conj() @ G0).flatten() for s in (0, 1) for t in (0, 1)]).T
res = max(np.linalg.norm(basis @ np.linalg.lstsq(basis, Pm.flatten(), rcond=None)[0] - Pm.flatten()) for Pm in [P0] + P1)
ck('projectors are linear combinations of u(p,s) vbar(p,sbar)', res < 1e-12, '%.1e' % res)
alpha = 1 / 137.036; eQ = 2. / 3; Nc = 3; e2 = 4 * np.pi * alpha
psi0 = 0.31; M = 2 * mq
pref = np.sqrt(2 * M) / (2 * mq) * np.sqrt(Nc) * psi0
xg, wg = np.polynomial.legendre.leggauss(40)
phis = np.linspace(0, 2 * np.pi, 40, endpoint=False)
# 3S1 -> e+ e- : M = pref * e^2 eQ * [ubar(k1) gamma_mu v(k2)] (1/s) Tr[gamma^mu Pi]
s_ = M**2
def width_ee(Pi):
    J = np.array([np.trace(Gam[mu] @ Pi) for mu in range(4)])        # Tr[gamma^mu Pi] (upper index)
    Jl = metric @ J
    tot = 0.
    for ct, wct in zip(xg, wg):
        st = np.sqrt(1 - ct**2)
        for ph in phis:
            n = np.array([st * np.cos(ph), st * np.sin(ph), ct])
            k1 = np.concatenate([[M / 2], M / 2 * n]); k2 = np.concatenate([[M / 2], -M / 2 * n])
            # sum over lepton spins: L^{mu nu} = Tr[k1slash gamma^mu k2slash gamma^nu] (massless)
            Lmn = np.array([[np.trace(sl(k1) @ Gam[a] @ sl(k2) @ Gam[b]) for b in range(4)] for a in range(4)])
            amp2 = np.einsum('a,b,ab->', Jl, Jl.conj(), Lmn).real
            tot += wct * (2 * np.pi / len(phis)) * amp2
    msq = pref**2 * e2**2 * eQ**2 / s_**2 * tot           # integrated over dOmega
    return msq / (2 * M) / (32 * np.pi**2)
G_ee = np.mean([width_ee(P) for P in P1])
G_ee_formula = 16 * np.pi * Nc / 3 * eQ**2 * alpha**2 * psi0**2 / M**2
ck('Gamma(3S1 -> e+e-) = (16 pi N_c/3) e_Q^2 alpha^2 |psi(0)|^2/M^2  (VF-NRQ-2)', abs(G_ee / G_ee_formula - 1) < 1e-10, '%.12f' % (G_ee / G_ee_formula))
R0sq = 4 * np.pi * psi0**2
ck('  = N_c e_Q^2 alpha^2 |R(0)|^2/(3 m_Q^2), M = 2 m_Q', abs(G_ee / (Nc * eQ**2 * alpha**2 * R0sq / (3 * mq**2)) - 1) < 1e-10)
ck('spin singlet does not couple to a single photon (C parity)', width_ee(P0) < 1e-20 * G_ee)
# 1S0 -> gamma gamma : M = pref * e^2 eQ^2 eps1*_mu eps2*_nu Tr[(g^nu S(p-k1) g^mu + g^mu S(p-k2) g^nu) Pi]
def S_prop(q):
    return (sl(q) + mq * I4) / (q @ metric @ q - mq**2)
def width_gg(Pi):
    tot = 0.
    for ct, wct in zip(xg, wg):
        st = np.sqrt(1 - ct**2)
        for ph in phis:
            n = np.array([st * np.cos(ph), st * np.sin(ph), ct])
            k1 = np.concatenate([[M / 2], M / 2 * n]); k2 = np.concatenate([[M / 2], -M / 2 * n])
            T = np.array([[np.trace((Gam[b] @ S_prop(p - k1) @ Gam[a] + Gam[a] @ S_prop(p - k2) @ Gam[b]) @ Pi)
                           for b in range(4)] for a in range(4)])      # upper indices a (photon 1), b (photon 2)
            # polarization sums -g_{mu mu'} -g_{nu nu'} (Ward identity)
            Tl = metric @ T @ metric
            amp2 = np.einsum('ab,ab->', T, Tl.conj()).real
            tot += wct * (2 * np.pi / len(phis)) * amp2
    msq = pref**2 * e2**2 * eQ**4 * tot
    return 0.5 * msq / (2 * M) / (32 * np.pi**2)               # identical photons: 1/2
G_gg = width_gg(P0)
G_gg_formula = 16 * np.pi * Nc * eQ**4 * alpha**2 * psi0**2 / M**2
ck('Gamma(1S0 -> gamma gamma) = 16 pi N_c e_Q^4 alpha^2 |psi(0)|^2/M^2 (VF-NRQ-3)', abs(G_gg / G_gg_formula - 1) < 1e-10, '%.12f' % (G_gg / G_gg_formula))
ck('  = 4 N_c e_Q^4 alpha^2 |R(0)|^2/M^2', abs(G_gg / (4 * Nc * eQ**4 * alpha**2 * R0sq / M**2) - 1) < 1e-10)
ck('spin triplet does not decay into two photons (Landau-Yang, C parity)', max(width_gg(P) for P in P1) < 1e-20 * G_gg)
# BBL normalization: Gamma = 2 Im f <O>/m^2 with <O_1> = 2 N_c |psi(0)|^2 = (N_c/2pi)|R(0)|^2
O1 = 2 * Nc * psi0**2
Imf_ee = G_ee * mq**2 / (2 * O1); Imf_gg = G_gg * mq**2 / (2 * O1)
ck('Im f_ee(3S1) = pi e_Q^2 alpha^2/3 (BBL (A34))', abs(Imf_ee / (np.pi * eQ**2 * alpha**2 / 3) - 1) < 1e-10)
ck('Im f_gg(1S0) = pi e_Q^4 alpha^2 (BBL (A31))', abs(Imf_gg / (np.pi * eQ**4 * alpha**2) - 1) < 1e-10)
ck('<O_1> = 2 N_c |psi(0)|^2 = (N_c/2pi)|R(0)|^2', abs(O1 - Nc / (2 * np.pi) * R0sq) < 1e-14)
# QED limit: para-positronium N_c = e_Q = 1, |psi(0)|^2 = (m alpha)^3/(8 pi), M = 2m  ->  Gamma = alpha^5 m/2
me = 0.000511
Gps = 16 * np.pi * alpha**2 * (me * alpha)**3 / (8 * np.pi) / (2 * me)**2
ck('QED limit: Gamma(p-Ps -> gamma gamma) = alpha^5 m/2', abs(Gps / (alpha**5 * me / 2) - 1) < 1e-12)
ck('spin-symmetry ratio Gamma(eta_c->gg)/Gamma(J/psi->ee) = 3 e_Q^2 = 4/3 at LO', abs(G_gg_formula / G_ee_formula - 3 * eQ**2) < 1e-12)

ok = ck.summary()
sys.exit(0 if ok else 1)
