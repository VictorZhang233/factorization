# -*- coding: utf-8 -*-
"""
s8_meson.py -- item (3): LO hard exclusive meson electroproduction  gamma*(q) N(p) -> M(p_M) N'(p'),
quark-exchange graphs (one-gluon exchange), leading twist, for a pseudoscalar (pi+) and a longitudinal vector
meson (rho_L).  Hadronic amplitude A^nu = <M N'| J^nu(0) |N>, physical amplitude ~ e eps_nu A^nu.

Leading-region form (same reordering sign as for F_pi, s4):
  A^nu = - (C_F/N_c) sum_graphs int dx dz Tr[ X M_N(x) Y M_M(z) ] (-i/l^2),
  M_N(x)  = (1/4)[ g^- calH(x) + g5 g^- calHt(x) ]       (nucleon transition correlator, s7)
  M_pi(z) = (i f_pi/4) p_M-slash g5 phi_pi(z),  M_rho(z) = (f_rho/4) p_M-slash phi_rho(z)   (z = quark fraction)
X = string of the line from the nucleon quark a (momentum k=(x+xi)Pbar) to the meson quark (z p_M),
Y = string of the line from the meson antiquark (zbar p_M) to the quark b returned to the nucleon (k'=(x-xi)Pbar).
Kinematics (leading power): Pbar=(P,0,0), Delta=(-2 xi P,0,0), q=(-2 xi P, q^-, 0), p_M = q - Delta = (0,q^-,0),
Q^2 = 4 xi P q^-, eps_L(q) = (q^+, -q^-, 0_T)/Q.
Run:  python3 -I s8_meson.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

ck = Checker('s8_meson')
x, z, xi, P, qm, g, f = sp.symbols('x z xi P q_m g f', positive=True)
ea, eb = sp.symbols('e_a e_b', real=True)
Nc = sp.symbols('N_c', positive=True)
CF = (Nc ** 2 - 1) / (2 * Nc)
zb = 1 - z

k = lc((x + xi) * P, 0)
kp = lc((x - xi) * P, 0)
q = lc(-2 * xi * P, qm)
Delta = lc(-2 * xi * P, 0)
pM = sub(q, Delta)
Q2 = sp.simplify(-dot(q, q))
Q = sp.sqrt(Q2)
ck.zero('Q^2 = 4 xi P q^-, p_M^2 = 0', (Q2 - 4 * xi * P * qm) ** 2 + dot(pM, pM) ** 2)
epsL = lc(plus(q) / Q, -minus(q) / Q)
ck.zero('eps_L^2 = +1, eps_L.q = 0', (dot(epsL, epsL) - 1) ** 2 + dot(epsL, q) ** 2)
low = lambda v: [METRIC[i] * v[i] for i in range(4)]


def S(kk):
    return I * slash(kk) / dot(kk, kk)


def amplitude(MN, MM):
    """A^nu for all nu, per unit [calH or calHt] * phi(z)"""
    l12 = sub(add(k, q), scal(z, pM))      # gluon, graphs 1,2
    l34 = sub(k, scal(z, pM))              # gluon, graphs 3,4
    res = {}
    for nu in range(4):
        gnu = G[nu]
        tot = {1: 0, 2: 0, 3: 0, 4: 0}
        for a_ in range(4):
            X1 = (I * g * G[a_]) * S(add(k, q)) * (ea * gnu); Y1 = I * g * GL[a_]
            X2 = (ea * gnu) * S(sub(scal(z, pM), q)) * (I * g * G[a_]); Y2 = I * g * GL[a_]
            X3 = I * g * G[a_]; Y3 = (eb * gnu) * S(sub(kp, q)) * (I * g * GL[a_])
            X4 = I * g * G[a_]; Y4 = (I * g * GL[a_]) * S(sub(q, scal(zb, pM))) * (eb * gnu)
            tot[1] += tr(X1 * MN * Y1 * MM) * (-I / dot(l12, l12))
            tot[2] += tr(X2 * MN * Y2 * MM) * (-I / dot(l12, l12))
            tot[3] += tr(X3 * MN * Y3 * MM) * (-I / dot(l34, l34))
            tot[4] += tr(X4 * MN * Y4 * MM) * (-I / dot(l34, l34))
        res[nu] = {kk: sp.simplify(-CF / Nc * vv) for kk, vv in tot.items()}
    return res


MNV = sp.Rational(1, 4) * gm            # per calH
MNA = sp.Rational(1, 4) * g5 * gm       # per calHt
Mpi = I * f / 4 * slash(pM) * g5
Mrho = f / 4 * slash(pM)

print('=== 1. parity selection ===')
A_piV = amplitude(MNV, Mpi)
A_rhoA = amplitude(MNA, Mrho)
ck.check('pseudoscalar meson does not couple to the vector GPDs (H, E) at leading twist', all(sp.simplify(sum(A_piV[nu].values())) == 0 for nu in range(4)))
ck.check('longitudinal vector meson does not couple to the axial GPDs (Ht, Et) at leading twist', all(sp.simplify(sum(A_rhoA[nu].values())) == 0 for nu in range(4)))

print('=== 2. pseudoscalar meson (Ht, Et): longitudinal photon ===')
A_pi = amplitude(MNA, Mpi)
AL_graphs = {kk: sp.factor(sp.simplify(sum(low(epsL)[nu] * A_pi[nu][kk] for nu in range(4)))) for kk in (1, 2, 3, 4)}
for kk in (1, 2, 3, 4):
    print('   graph %d: eps_L.A = %s' % (kk, AL_graphs[kk]))
AL = sp.factor(sp.simplify(sum(AL_graphs.values())))
print('   eps_L.A (per calHt phi) =', AL)
# expected structure: (C_F/N_c) g^2 f / Q * [ e_a/(zbar (x - xi)) + e_b/(z (x + xi)) ] * const
AL_red = sp.simplify(AL / (CF / Nc * g ** 2 * f / Q))
print('   reduced kernel =', sp.factor(AL_red))
# fit to c1 e_a/(zbar (x-xi)) + c2 e_b/(z (x+xi))
c1, c2 = sp.symbols('c1 c2')
sol = sp.solve(sp.Poly(sp.numer(sp.together(AL_red - (c1 * ea / (zb * (x - xi)) + c2 * eb / (z * (x + xi))))), x, z, ea, eb).coeffs(), [c1, c2], dict=True)
print('   fit:', sol)
ck.check('eps_L.A_pi = (C_F/N_c) (g^2 f_pi/Q) c [e_a/(zbar (x - xi)) + e_b/(z (x + xi))] calHt   (single poles; the double pole of graph 1 cancels)',
         len(sol) == 1 and sp.simplify(sol[0][c1] - sol[0][c2]) == 0)
cpi = sol[0][c1] if sol else None
print('   overall constant c =', cpi)

print('=== 3. longitudinal vector meson (H, E) ===')
A_rho = amplitude(MNV, Mrho)
ALr = sp.factor(sp.simplify(sum(low(epsL)[nu] * sum(A_rho[nu].values()) for nu in range(4))))
ALr_red = sp.simplify(ALr / (CF / Nc * g ** 2 * f / Q))
sol_r = sp.solve(sp.Poly(sp.numer(sp.together(ALr_red - (c1 * ea / (zb * (x - xi)) + c2 * eb / (z * (x + xi))))), x, z, ea, eb).coeffs(), [c1, c2], dict=True)
print('   eps_L.A_rho reduced kernel =', sp.factor(ALr_red), '  fit:', sol_r)
ck.check('eps_L.A_rho = (C_F/N_c)(g^2 f_rho/Q) c\' [e_a/(zbar (x - xi)) + e_b/(z (x + xi))] calH', len(sol_r) == 1 and sp.simplify(sol_r[0][c1] - sol_r[0][c2]) == 0)

print('=== 4. C-parity cross-checks for neutral mesons (e_a = e_b, symmetric DA) ===')
# after int dz phi(z) with phi(z)=phi(zbar): 1/zbar and 1/z give the same factor I; kernel ~ 1/(x-xi) + 1/(x+xi): odd in x
Kx = 1 / (x - xi) + 1 / (x + xi)
ck.zero('neutral mesons: kernel 1/(x-xi) + 1/(x+xi) is odd in x', sp.simplify(Kx.subs(x, -x) + Kx))
print('   => rho0_L selects H^q(x) - H^q(-x) (C-even, forward q + qbar): t-channel C = +1 = C(gamma*) C(rho0) = (-1)(-1)  OK')
print('   => pi0    selects Ht^q(x) - Ht^q(-x) (C-odd, forward Delta q - Delta qbar): t-channel C = -1 = C(gamma*) C(pi0) = (-1)(+1)  OK')
# genuine check, starting from the COMPUTED reduced kernels (not from the hand-written Kx above):
# integrate over z with a symmetric DA phi(z) = 6 z zbar [1 + a2 C_2^{3/2}(2z-1)] (a2 arbitrary)
a2s = sp.symbols('a2s', real=True)
phi_sym = 6 * z * zb * (1 + a2s * sp.gegenbauer(2, sp.Rational(3, 2), 2 * z - 1))
def z_integrated(red):
    return sp.simplify(sp.integrate(sp.expand(sp.cancel(red * phi_sym)), (z, 0, 1)))
K_pi0 = z_integrated(AL_red.subs({ea: 1, eb: 1}))
K_rho0 = z_integrated(ALr_red.subs({ea: 1, eb: 1}))
K_pip = z_integrated(AL_red.subs({ea: sp.Rational(2, 3), eb: -sp.Rational(1, 3)}))
print('   z-integrated pi0 kernel (e_a = e_b = 1):', sp.factor(K_pi0))
ck.check('C-parity from the computed amplitudes: for e_a = e_b and a symmetric DA (any a_2) the z-integrated pi0 and rho0 '
         'kernels are odd in x [so pi0 -> Ht(x)-Ht(-x), rho0 -> H(x)-H(-x)], while the pi+ kernel (e_a != e_b) has no definite parity',
         sp.simplify(K_pi0.subs(x, -x) + K_pi0) == 0 and sp.simplify(K_rho0.subs(x, -x) + K_rho0) == 0
         and sp.simplify(K_pip.subs(x, -x) + K_pip) != 0 and sp.simplify(K_pip.subs(x, -x) - K_pip) != 0)

print('=== 5. transverse photons decouple at leading twist ===')
eT1 = lc(0, 0, 1, 0)
eT2 = lc(0, 0, 0, 1)
okT = True
for A_ in (A_pi, A_rho):
    for eT in (eT1, eT2):
        val = sp.simplify(sum(low(eT)[nu] * sum(A_[nu].values()) for nu in range(4)))
        okT &= (val == 0)
ck.check('eps_T.A = 0 for pi and rho_L at leading twist: gamma*_T amplitudes start at twist 3 (power suppressed)', okT)

print('=== 5b. transverse photons at twist 3: the Mankiewicz-Piller integrals (literature cross-check) ===')
# Mankiewicz & Piller, PRD 61 (2000) 074013 [hep-ph/9905287v1], eqs. (3)-(5), (10), Wandzura-Wilczek approximation:
#  Phi(t) = 1/2 [ tb int_0^t du phi/ub - t int_t^1 du phi/u ],  g^v(t) = 1/2 [ int_0^t du phi/ub + int_t^1 du phi/u ],
#  g^a(t) = 2 [ tb int_0^t du phi/ub + t int_t^1 du phi/u ],
#  I_1 = int_0^1 dt/t ( 4 g^v - 2 Phi/t + g^a/(2 t tb) ),  I_2 = int_0^1 dt/t ( 2 g^v + g^a/(2 t tb) ).
tt, uu = sp.symbols('tau u', positive=True)
def mp_integrands(phi):
    A0 = sp.integrate(phi / (1 - uu), (uu, 0, tt))
    A1 = sp.integrate(phi / uu, (uu, tt, 1))
    Phi = sp.Rational(1, 2) * ((1 - tt) * A0 - tt * A1)
    gv = sp.Rational(1, 2) * (A0 + A1)
    ga = 2 * ((1 - tt) * A0 + tt * A1)
    i1 = (4 * gv - 2 * Phi / tt + ga / (2 * tt * (1 - tt))) / tt
    i2 = (2 * gv + ga / (2 * tt * (1 - tt))) / tt
    return sp.simplify(gv.subs(tt, 0)), sp.limit(tt * i1, tt, 0), sp.limit(tt * i2, tt, 0)
gv0_as, r1_as, r2_as = mp_integrands(6 * uu * (1 - uu))
print('   asymptotic DA 6u(1-u):     g^v(0) = %s ; tau*integrand(I_1) -> %s ; tau*integrand(I_2) -> %s' % (gv0_as, r1_as, r2_as))
gv0_s, r1_s, r2_s = mp_integrands(30 * uu ** 2 * (1 - uu) ** 2)
print('   endpoint-suppressed 30u^2(1-u)^2: g^v(0) = %s ; tau*integrand(I_1) -> %s ; tau*integrand(I_2) -> %s' % (gv0_s, r1_s, r2_s))
ck.check('MP integrals I_1, I_2 diverge logarithmically (integrand ~ const/tau, tau -> 0) because g^v(0) = (1/2) int phi/u != 0; '
         'for phi = 6u(1-u): constants 12 and 6 [MP text says "12/tau and 9/tau"; 9 would need 4 g^v instead of 2 g^v in their I_2]; '
         'endpoint suppression (phi ~ u^2) does not remove it',
         gv0_as == sp.Rational(3, 2) and r1_as == 12 and r2_as == 6
         and gv0_s == sp.Rational(5, 4) and r1_s != 0 and r2_s != 0)

print('=== 6. scaling ===')
QQ = sp.symbols('QQ', positive=True)
ck.check('eps_L.A scales as 1/Q at fixed x, xi, z (=> d sigma_L/dt ~ 1/Q^6)', sp.simplify(AL.subs(qm, QQ ** 2 / (4 * xi * P)) * QQ).free_symbols.isdisjoint({QQ}))

ck.summary()
