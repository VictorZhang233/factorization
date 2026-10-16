# -*- coding: utf-8 -*-
"""
s3_nrqcd.py -- Part (3): NRQCD velocity scaling, LO electromagnetic decay widths from explicit
threshold amplitudes, NRQCD matching normalization (BBL), and the one-loop vector-current matching
coefficient c_v at threshold (hard region, D dims) giving Gamma(V->e+e-) ~ (1 - 4 C_F alpha_s/pi).

Conventions: BBL (Bodwin-Braaten-Lepage 1995): Gamma(H) = sum_n 2 Im f_n/m^{d_n-4} <H|O_n|H>,
 NR normalization <H(P')|H(P)> = (2pi)^3 delta^3(P-P'); O_1(1S0) = psi^dag chi chi^dag psi,
 O_1(3S1) = psi^dag sigma chi . chi^dag sigma psi ; <O_1>_H = (N_c/2pi)|R(0)|^2 = 2 N_c |psi(0)|^2 (vac. sat.)
Run:  python3 -I s3_nrqcd.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

ck = Check('s3_nrqcd: velocity scaling, LO widths (VRW, gamma gamma), BBL normalization, one-loop c_v')

# =============================================================================== A. velocity scaling
m, v = sp.symbols('m v', positive=True)
sc = {'psi': (m * v) ** sp.Rational(3, 2), 'D': m * v, 'Dt': m * v ** 2, 'gE': m ** 2 * v ** 3, 'gB': m ** 2 * v ** 4, 'as': v}
def order(e):
    """power of v of a monomial in m, v"""
    return sp.Poly(sp.expand(e).subs(m, 1), v).degree() if e.has(v) else 0
LO = sc['psi'] ** 2 * sc['Dt']
ck('normalization int d^3x psi^dag psi ~ 1 over volume (mv)^-3  =>  psi ~ (mv)^{3/2}', sp.simplify(sc['psi'] ** 2 * (m * v) ** -3) == 1)
ck('kinetic term psi^dag D^2/2m psi ~ psi^dag iD_t psi  (Schrodinger: D_t ~ D^2/m ~ m v^2)', sp.simplify(sc['psi'] ** 2 * sc['D'] ** 2 / m - LO) == 0)
ck('Gauss law  D.gE = g^2 psi^dag T psi :  gE ~ alpha_s m^2 v^2 ~ m^2 v^3  (alpha_s(mv) ~ v)',
   sp.simplify(sc['D'] * sc['gE'] - sc['as'] * sc['psi'] ** 2) == 0)
ck('Ampere law  D x gB = D_t gE + g^2 j,  j ~ psi^dag D psi/m  :  gB ~ m^2 v^4',
   order(sc['D'] * sc['gB']) == order(sc['Dt'] * sc['gE']) == order(sc['as'] * sc['psi'] ** 2 * sc['D'] / m))
rel = {
    'c_F psi^dag sigma.gB psi/(2m)': sc['psi'] ** 2 * sc['gB'] / m,
    'c_D psi^dag [D.,gE] psi/(8m^2)': sc['psi'] ** 2 * sc['D'] * sc['gE'] / m ** 2,
    'c_S psi^dag i sigma.(D x gE - gE x D) psi/(8m^2)': sc['psi'] ** 2 * sc['D'] * sc['gE'] / m ** 2,
    'psi^dag D^4 psi/(8m^3)': sc['psi'] ** 2 * sc['D'] ** 4 / m ** 3,
}
ok = all(order(e) - order(LO) == 2 for e in rel.values())
ck('all 1/m^2-type bilinears (Fermi, Darwin, spin-orbit, D^4) are O(v^2) relative to LO', ok,
   ', '.join(f'{k}: v^{order(e) - order(LO)}' for k, e in rel.items()))
# four-fermion operators: contribution to the width ~ <O>/m^{d-4}
S_wave = sc['psi'] ** 2 * sc['psi'] ** 2 / sc['psi'] ** 2 / m ** 2     # <H|O_1(S)|H> ~ |psi(0)|^2 ~ (mv)^3 ; /m^2
P_wave = (m * v) ** 3 * (m * v) ** 2 / m ** 4                           # dim-8 P-wave singlet: (mv)^5/m^4
oct_P = v ** 2 * (m * v) ** 3 / m ** 2                                  # <chi_J|O_8(3S1)|chi_J> ~ v^2 (mv)^3 ; /m^2
ck('Gamma(S-wave, colour singlet) ~ m v^3 ;  Gamma(P-wave singlet) ~ m v^5 ~ Gamma(octet 3S1 in chi_J)  (same order: BBL 1992)',
   order(S_wave) == 3 and order(P_wave) == 5 and order(oct_P) == 5)

# =============================================================================== B. LO widths from threshold amplitudes
# Projectors (relativistic spinor normalization ubar u = 2m), incoming Q(p) Qbar(pb) at threshold p = pb = (m,0):
#   sum_{s,sb} <1/2 s 1/2 sb|S S_z> u(p,s) vbar(pb,sb) = (1/(2 sqrt2 m)) (pslash + m) Gamma_S (pbslash - m),
#   Gamma_S = gamma5 (spin singlet) or epsslash (spin triplet).  Normalization: Tr[Pibar Pi] = -4 m^2.
mq = 1.7
p = np.array([mq, 0, 0, 0.0]); pb = p.copy()
def Pi_in(G):
    return (slash(p) + mq * ID4) @ G @ (slash(pb) - mq * ID4) / (2 * np.sqrt(2) * mq)
def dbar(M):
    return G0 @ M.conj().T @ G0
eps_list = [np.array([0, 1, 0, 0.0]), np.array([0, 0, 1, 0.0]), np.array([0, 0, 0, 1.0])]
P0 = Pi_in(G5)
P1 = [Pi_in(slash(e)) for e in eps_list]
ck('projector norms: Tr[Pibar Pi] = -4m^2 (singlet and each triplet state); triplet states orthogonal',
   abs(np.trace(dbar(P0) @ P0) + 4 * mq ** 2) < 1e-12 and all(abs(np.trace(dbar(P1[i]) @ P1[j]) + 4 * mq ** 2 * (i == j)) < 1e-12 for i in range(3) for j in range(3)))
# check: projector = explicit sum over spin states built from spinors (any orthonormal triplet basis works):
#   Pi_in(eps) lies in span{u(p,s) vbar(pb,sb)} and singlet is orthogonal to triplet
U = [u_spinor(p, s, mq) for s in (0, 1)]; V = [v_spinor(pb, s, mq) for s in (0, 1)]
basis = [np.outer(U[s], bar(V[t])) for s in (0, 1) for t in (0, 1)]
B = np.array([b.flatten() for b in basis]).T
okspan = all(np.linalg.lstsq(B, Pm.flatten(), rcond=None)[1].size == 0 or np.linalg.lstsq(B, Pm.flatten(), rcond=None)[1][0] < 1e-20 for Pm in [P0] + P1)
res_ = [np.linalg.norm(B @ np.linalg.lstsq(B, Pm.flatten(), rcond=None)[0] - Pm.flatten()) for Pm in [P0] + P1]
ck('projectors are combinations of u(p,s) vbar(pb,sb) (physical QQbar spin states)', max(res_) < 1e-12, f'max residual {max(res_):.1e}')
ck('singlet orthogonal to triplet: Tr[Pibar_0 Pi_1(eps)] = 0', all(abs(np.trace(dbar(P0) @ P)) < 1e-12 for P in P1))

alpha, eQ, Nc = 1 / 137.0, 2 / 3, 3
e2 = 4 * np.pi * alpha
psi0 = 0.37          # |psi(0)| (arbitrary units, GeV^{3/2})
Mb = 2 * mq
# bound-state amplitude:  M(H->f) = sqrt(2M)/(2m) * sqrt(N_c) * psi(0) * Tr[Gamma_f Pi_in]   (colour singlet, E_k ~ m)
pref = np.sqrt(2 * Mb) / (2 * mq) * np.sqrt(Nc) * psi0
# lepton directions: Gauss-Legendre in cos(theta), uniform phi
ct, wt = np.polynomial.legendre.leggauss(24)
phis = np.linspace(0, 2 * np.pi, 24, endpoint=False)
def width_ee(Pi):
    E = Mb / 2
    tot = 0.0
    for c, w in zip(ct, wt):
        sn = np.sqrt(1 - c * c)
        for ph in phis:
            k1 = E * np.array([1, sn * np.cos(ph), sn * np.sin(ph), c]); k2 = E * np.array([1, -sn * np.cos(ph), -sn * np.sin(ph), -c])
            # hadronic current J^mu = e eQ Tr[gamma^mu Pi], photon propagator 1/s, lepton current e ubar gamma_mu v
            J = np.array([e2 ** 0.5 * eQ * np.trace(GAM[mu] @ Pi) for mu in range(4)]) * pref / Mb ** 2
            Jl = lower(J)
            amp2 = 0.0
            for s1 in (0, 1):
                for s2 in (0, 1):
                    a = e2 ** 0.5 * bar(u_spinor(k1, s1)) @ slash(J) @ v_spinor(k2, s2)
                    amp2 += abs(a) ** 2
            tot += w * amp2 / (4 * np.pi) * (2 * np.pi / len(phis))   # angular average weight dOmega/(4pi)
    # int dPhi_2 = (1/8pi) <...>_Omega
    return tot / (8 * np.pi) / (2 * Mb)
G_ee = np.mean([width_ee(P) for P in P1])
G_ee_ref = 16 * np.pi * Nc / 3 * eQ ** 2 * alpha ** 2 * psi0 ** 2 / Mb ** 2
ck('Gamma(3S1 -> e+e-) = (16 pi N_c/3) e_Q^2 alpha^2 |psi(0)|^2/M^2  [= Van Royen-Weisskopf for N_c = 3]', abs(G_ee / G_ee_ref - 1) < 1e-10,
   f'ratio {G_ee / G_ee_ref:.12f}')
ck('spin-singlet does not couple to the vector current at LO (C-parity)', width_ee(P0) < 1e-20 * G_ee)
def width_gg(Pi):
    E = Mb / 2
    tot = 0.0
    for c, w in zip(ct, wt):
        sn = np.sqrt(1 - c * c)
        for ph in phis:
            k1 = E * np.array([1, sn * np.cos(ph), sn * np.sin(ph), c]); k2 = E * np.array([1, -sn * np.cos(ph), -sn * np.sin(ph), -c])
            # photon polarizations: two transverse vectors for each photon
            def pols(k):
                kh = k[1:] / np.linalg.norm(k[1:])
                a = np.array([1.0, 0, 0]) if abs(kh[0]) < 0.9 else np.array([0, 1.0, 0])
                e1 = np.cross(kh, a); e1 /= np.linalg.norm(e1); e2_ = np.cross(kh, e1)
                return [np.concatenate([[0], e1]), np.concatenate([[0], e2_])]
            amp2 = 0.0
            for ea in pols(k1):
                for eb in pols(k2):
                    S1 = slash(p - k1) + mq * ID4; S2 = slash(p - k2) + mq * ID4
                    d1 = mdot(p - k1, p - k1) - mq ** 2; d2 = mdot(p - k2, p - k2) - mq ** 2
                    # vbar(pb)[ eb (p-k1+m) ea /d1 + ea (p-k2+m) eb /d2 ] u(p)  -> Tr[ ... Pi_in ]
                    G = slash(eb) @ S1 @ slash(ea) / d1 + slash(ea) @ S2 @ slash(eb) / d2
                    a = (e2 * eQ ** 2) * np.trace(G @ Pi) * pref
                    amp2 += abs(a) ** 2
            tot += w * amp2 / (4 * np.pi) * (2 * np.pi / len(phis))
    return 0.5 * tot / (8 * np.pi) / (2 * Mb)        # 1/2 for identical photons
G_gg = width_gg(P0)
G_gg_ref = 16 * np.pi * Nc * eQ ** 4 * alpha ** 2 * psi0 ** 2 / Mb ** 2
ck('Gamma(1S0 -> gamma gamma) = 16 pi N_c e_Q^4 alpha^2 |psi(0)|^2/M^2 = 4 N_c e_Q^4 alpha^2 |R(0)|^2/M^2  [12 e_Q^4 alpha^2|R(0)|^2/M^2 for N_c=3]',
   abs(G_gg / G_gg_ref - 1) < 1e-10, f'ratio {G_gg / G_gg_ref:.12f}')
ck('spin-triplet does not decay to two photons (Landau-Yang / C-parity)', max(width_gg(P) for P in P1) < 1e-20 * G_gg)
# QED limits: positronium Gamma(p-Ps -> 2gamma) = alpha^5 m/2 ; true-muonium 3S1 -> e+e- = alpha^5 m/6  (|psi(0)|^2 = (m alpha)^3/(8 pi))
mm = 0.105; psiPs2 = (mm * alpha) ** 3 / (8 * np.pi)
ck('QED limit: 16 pi alpha^2 |psi(0)|^2/M^2 = alpha^5 m/2 (para-positronium, N_c = e_Q = 1)',
   abs(16 * np.pi * alpha ** 2 * psiPs2 / (2 * mm) ** 2 / (alpha ** 5 * mm / 2) - 1) < 1e-12)
# ratio of widths
ck('LO ratio Gamma(eta_c->gamma gamma)/Gamma(J/psi->e+e-) = 3 e_Q^2 (= 4/3 for charm), using <O(1S0)> = <O(3S1)> (spin symmetry)',
   abs(G_gg / G_ee * (G_ee_ref / G_gg_ref) * 3 * eQ ** 2 - 3 * eQ ** 2) < 1e-9 and abs(G_gg_ref / G_ee_ref - 3 * eQ ** 2) < 1e-12)

# BBL matching: <O_1>_H = 2 N_c |psi(0)|^2 = (N_c/2pi)|R(0)|^2 ;  Gamma = 2 Im f <O>/m^2
O1 = 2 * Nc * psi0 ** 2
Imf_ee = G_ee * mq ** 2 / (2 * O1)
Imf_gg = G_gg * mq ** 2 / (2 * O1)
ck('BBL: Im f_ee(3S1) = pi e_Q^2 alpha^2/3', abs(Imf_ee / (np.pi * eQ ** 2 * alpha ** 2 / 3) - 1) < 1e-10)
ck('BBL: Im f_gamma gamma(1S0) = pi e_Q^4 alpha^2', abs(Imf_gg / (np.pi * eQ ** 4 * alpha ** 2) - 1) < 1e-10)
# 2x2 algebra behind <0|chi^dag sigma^i psi|V> = sqrt(2N_c) psi(0) eps^i : orthonormal basis {1, sigma^i}/sqrt2
Mtrip = [sig[i] / np.sqrt(2) for i in range(3)]
ok = all(abs(np.trace(sig[i] @ Mtrip[j]) - np.sqrt(2) * (i == j)) < 1e-14 for i in range(3) for j in range(3)) and \
     all(abs(np.trace(Mtrip[i].conj().T @ Mtrip[j]) - (i == j)) < 1e-14 for i in range(3) for j in range(3))
ck('<0|chi^dag sigma^i psi|V(eps)> = sqrt(2 N_c) psi(0) eps^i  =>  <V|O_1(3S1)|V> = 2 N_c |psi(0)|^2 = (N_c/2pi)|R(0)|^2', ok)

# =============================================================================== C. one-loop c_v at threshold (hard region)
eps = sp.Symbol('epsilon'); Ms = sp.Symbol('m', positive=True); u = sp.Symbol('u', real=True)
Dd = 4 - 2 * eps
# trace with massive factors: factors are lists of (coef, slot|None)
def mtrace(factors, indices, dotsub):
    import itertools
    tot = sp.Integer(0)
    for combo in itertools.product(*factors):
        coef = sp.Integer(1); slots = []
        for c, sl in combo:
            coef *= c
            if sl is not None:
                slots.append(sl)
        if coef == 0:
            continue
        tot += coef * dtrace(tuple(slots), indices)
    return sp.expand(sp.expand(tot).subs(dotsub).subs(D, Dd))
# vertex numerator at threshold (p1 = p2 = p), k = l + u p:
#   gamma^a (p - k + m) gamma^mu (-p - k + m) gamma_a ,  projected with Pi_out = (p - m) epsstar (p + m), contracted with eps_mu
dsub = {dot('p', 'p'): Ms ** 2, dot('p', 'e'): 0, dot('p', 'es'): 0, dot('e', 'es'): -1, dot('e', 'e'): 0, dot('es', 'es'): 0}
L2 = sp.Symbol('L2')
def sym_l(expr):
    """symmetric integration over l: l.a l.b -> L2 a.b/D ; l.l -> L2 ; odd -> 0"""
    expr = sp.expand(expr)
    out = sp.Integer(0)
    for t in sp.Add.make_args(expr):
        ls = []; rest = sp.Integer(1)
        for f_ in sp.Mul.make_args(t):
            b_, e_ = f_.as_base_exp()
            if isinstance(b_, sp.Symbol) and (b_.name.startswith('l.') or b_.name == 'l^2' or b_.name.endswith('.l')):
                ls += [b_] * int(e_)
            else:
                rest *= f_
        nl = sum(2 if b_.name == 'l^2' else 1 for b_ in ls)
        if nl == 0:
            out += rest
        elif nl == 2:
            if len(ls) == 1:
                out += rest * L2
            else:
                vv = []
                for b_ in ls:
                    a1, a2 = b_.name.split('.')
                    vv.append(a2 if a1 == 'l' else a1)
                out += rest * L2 * dot(vv[0], vv[1]) / D
        elif nl % 2 == 1:
            continue
        else:
            raise ValueError
    return sp.expand(out)
# use 'e' for eps (contracted with gamma^mu) and 'es' for eps* in the projector; index a contracted
fac_A = [(1, 'a')]
fac_q = [(1 - u, 'p'), (-1, 'l'), (Ms, None)]       # p - k + m
fac_mu = [(1, 'e')]                                 # gamma^mu eps_mu
fac_qb = [(-(1 + u), 'p'), (-1, 'l'), (Ms, None)]   # -p - k + m
fac_A2 = [(1, 'a')]
proj = [[(1, 'p'), (-Ms, None)], [(1, 'es')], [(1, 'p'), (Ms, None)]]
num = mtrace([fac_A, fac_q, fac_mu, fac_qb, fac_A2] + proj, ('a',), {})
num = sym_l(num)
num = sp.expand(num.subs(dsub).subs(D, Dd))
tree = mtrace([[(1, 'e')]] + proj, (), dsub)
N0 = sp.expand(num.coeff(L2, 0)); N2 = sp.expand(num.coeff(L2, 1))
# integrals: Delta = u^2 m^2 ;  dGamma = -i g^2 C_F * 2 int_simplex [N0 I0 + N2 I2]
#   I0 = -i/(4pi)^{D/2} Gamma(1+eps)/2 Delta^{-1-eps} ;  I2 = i/(4pi)^{D/2} (D/2) Gamma(eps)/2 Delta^{-eps}
#   int_simplex f(x-y) = int_{-1}^{1} du (1-|u|)/2 f(u) ; even part only: int_0^1 du (1-u) f(u)
def u_int(poly, power):
    """int_0^1 du (1-u) poly(u) * u^{power}  for the even part of poly"""
    P = sp.Poly(sp.expand(poly), u)
    tot = sp.Integer(0)
    for (k_,), c in P.terms():
        if k_ % 2 == 1:
            continue
        a_ = k_ + power
        tot += c / ((a_ + 1) * (a_ + 2))
    return tot
# (Delta)^{-1-eps} = (m^2)^{-1-eps} (u^2)^{-1-eps} = m^{-2-2eps} u^{-2-2eps}
vert = (-sp.I) * 2 * ((-sp.I) * sp.gamma(1 + eps) / 2 * Ms ** (-2 - 2 * eps) * u_int(N0, -2 - 2 * eps)
                       + (sp.I) * (Dd / 2) * sp.gamma(eps) / 2 * Ms ** (-2 * eps) * u_int(N2, -2 * eps))
vert_ratio = sp.simplify(vert / tree)          # times g^2 C_F mu^{2eps}/(4pi)^{D/2}
# on-shell Z_2:  Sigma = K [ (2-D) (1-x) pslash A_int + D m B_int ],  K = g^2 C_F Gamma(eps)/(4pi)^{D/2}
x = sp.Symbol('x', positive=True); p2 = sp.Symbol('p2', positive=True)
Delta_se = x * Ms ** 2 - x * (1 - x) * p2
# dSigma/dpslash at pslash = m :  A + 2 m^2 (A' + B'),  A = (2-D) int (1-x) Delta^-eps, B = D int Delta^-eps
#   A' = (2-D) eps int x (1-x)^2 Delta^{-1-eps} ; B' = D eps int x(1-x) Delta^{-1-eps}   at p2 = m^2: Delta = x^2 m^2
Aval = (2 - Dd) * sp.gamma(2 - 2 * eps) * sp.gamma(2) / sp.gamma(4 - 2 * eps) * 0   # placeholder replaced below
def beta_x(a_, b_):
    return sp.gamma(a_) * sp.gamma(b_) / sp.gamma(a_ + b_)
# A(m^2) = (2-D) m^{-2eps} int (1-x) x^{-2eps} = (2-D) m^{-2eps} B(1-2eps, 2)
A_m = (2 - Dd) * Ms ** (-2 * eps) * beta_x(1 - 2 * eps, 2)
Ap = (2 - Dd) * eps * Ms ** (-2 - 2 * eps) * beta_x(-2 * eps, 3)         # int x (1-x)^2 x^{-2-2eps}
Bp = Dd * eps * Ms ** (-2 - 2 * eps) * beta_x(-2 * eps, 2)               # int x (1-x) x^{-2-2eps}
dZ2 = sp.simplify(sp.gamma(eps) * (A_m + 2 * Ms ** 2 * (Ap + Bp)))       # times g^2 C_F mu^{2eps}/(4pi)^{D/2}
# c_v - 1 = vert_ratio + dZ2  (Z_2 = 1 + dSigma/dpslash ; sqrt(Z_2) per leg, two legs)
tot = sp.simplify(vert_ratio + dZ2)
# normalize: g^2 C_F mu^{2eps}/(4pi)^{D/2} = (alpha_s C_F/4pi) (4 pi mu^2)^eps ; MSbar factor e^{eps gE}(4pi)^{-eps}
musym = sp.Symbol('mu', positive=True)
cv1 = sp.simplify(tot * sp.exp(eps * sp.EulerGamma) * musym ** (2 * eps))
cv1_ser = sp.expand(sp.series(cv1, eps, 0, 1).removeO())
dZ2_ser = sp.expand(sp.series(sp.simplify(dZ2 * sp.exp(eps * sp.EulerGamma) * musym ** (2 * eps)), eps, 0, 1).removeO())
ck('on-shell Z_2 (DR, eps_UV = eps_IR): delta Z_2 = -(a_s C_F/4pi)[3/eps + 4 + 3 ln(mu^2/m^2)]',
   sp.simplify(dZ2_ser - (-(3 / eps + 4 + 3 * sp.log(musym ** 2 / Ms ** 2)))) == 0, str(sp.simplify(dZ2_ser)))
ck('one-loop matching of the vector current at threshold: c_v = 1 + (a_s C_F/4pi)(-8) = 1 - 2 C_F a_s/pi (finite, mu-independent)',
   sp.simplify(cv1_ser + 8) == 0, f'c_v^(1) [units a_s C_F/4pi] = {sp.simplify(cv1_ser)}')
ck('=> Gamma(V->e+e-) = Gamma_LO |c_v|^2 = Gamma_LO (1 - 4 C_F a_s/pi) = Gamma_LO (1 - 16 a_s/(3 pi))  [Barbieri et al. 1975; Celmaster 1979]',
   sp.simplify(2 * (-8) * sp.Rational(4, 3) / (4 * sp.pi) - (-sp.Rational(16, 3) / sp.pi)) == 0)
# the vertex alone: IR poles present, cancelled by Z_2
vser = sp.expand(sp.series(sp.simplify(vert_ratio * sp.exp(eps * sp.EulerGamma) * musym ** (2 * eps)), eps, 0, 1).removeO())
ck('threshold vertex alone has a mixed UV/IR pole 3/eps (= 1/eps_UV + 2/eps_IR); it cancels the Z_2 pole: c_v^(1) finite (no 1-loop anomalous dim.)',
   sp.simplify(vser.coeff(eps, -1) - 3) == 0, f'vertex: {sp.simplify(vser)}')

ok = ck.summary()
sys.exit(0 if ok else 1)
