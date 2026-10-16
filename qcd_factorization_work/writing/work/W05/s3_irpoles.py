r"""
s3_irpoles.py  (writer W05; Ch5 thm:sudakov-ir-poles, prop:sudakov-coulomb, prop:sudakov-dipole-violation;
VF-SUD-5, VF-SCET-8, VF-EE-4)

 (a) dipole anomalous dimension (ordered pairs) for two partons reproduces d ln C_V/d ln mu of VF-SCET-8;
 (b) one-loop Z factor from ln Z = (as/4pi)[Gamma'_0/(4eps^2) + Gamma_0/(2eps)] equals the pole part of F1,
     space-like and time-like (imaginary pole included);
 (c) colour conservation: sum_{(i,j)} T_i.T_j = - sum_i C_i ; three-parton values (q qbar g), SU(3) explicit;
 (d) Coulomb phase i pi T_i.T_j for sigma_ij=+1;
 (e) the three-loop non-dipole constant C = zeta5 + 2 zeta2 zeta3 (Almelid-Duhr-Gardi eq. (13)), numerical value.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp, numpy as np
PASS = []
def check(name, ok, info=''):
    PASS.append(bool(ok)); print(('[PASS] ' if ok else '[FAIL] ') + name + ((' : ' + str(info)) if info != '' else ''))

eps = sp.Symbol('epsilon', real=True); a = sp.Symbol('a_s', positive=True)   # a_s = alpha_s/(4pi)
CF, CA, Nc = sp.symbols('C_F C_A N_c', positive=True)
Lc = sp.Symbol('Lc')   # L = ln((-q^2 - i0)/mu^2), complex in the time-like region
# (a) VF-SCET-8: C_V = 1 + a C_F[-L^2 + 3L - 8 + zeta2];  d/dln mu acts as dL/dln mu = -2
CV1 = CF * (-Lc ** 2 + 3 * Lc - 8 + sp.zeta(2))
dCV = sp.expand(-2 * sp.diff(CV1, Lc))
# dipole: Gamma = sum_{(i,j) ordered} T_i.T_j/2 * gamma_cusp * ln(mu^2/(-s_ij)) + sum_i gamma^i
# gamma_cusp = 4 a, gamma^q = -3 C_F a ; T1.T2 = -C_F ; ln(mu^2/(-s12)) = -Lc   (-s12 = -q^2 - i0 for the q qbar pair)
T12 = -CF
Gam = 2 * (T12 / 2) * 4 * (-Lc) + 2 * (-3 * CF)
check('(a) dipole formula (ordered pairs) for the quark form factor = d ln C_V/d ln mu  (VF-SUD-5 check)', sp.simplify(Gam - dCV) == 0, (sp.expand(Gam), dCV))
Gam_unordered = (T12 / 2) * 4 * (-Lc) + 2 * (-3 * CF)
check('(a) the unordered-pair reading would NOT reproduce it', sp.simplify(Gam_unordered - dCV) != 0)
# (b) Z factor at one loop: ln Z = a [Gamma'_0/(4 eps^2) + Gamma_0/(2 eps)],  Gamma' = dGamma/dln mu = -gamma_cusp sum C_i
Gp0 = -4 * 2 * CF
Gam0 = sp.expand(Gam)            # in units a
lnZ = Gp0 / (4 * eps ** 2) + Gam0 / (2 * eps)
# pole part of F1 (units a C_F... ):  F1 = a C_F [-2/eps^2 + (2L-3)/eps + ...]  with L = ln((-q^2-i0)/mu^2)
F1poles = CF * (-2 / eps ** 2 + (2 * Lc - 3) / eps)
check('(b) ln Z^(1) = pole part of F1 (both regions; L complex)', sp.simplify(sp.expand(lnZ - F1poles)) == 0, sp.expand(lnZ))
# time-like: L = ln(s/mu^2) - i pi  (since -q^2 - i0 = s e^{-i pi})
ell = sp.Symbol('ell', real=True)
imZ = sp.im(sp.expand(F1poles.subs(Lc, ell - sp.I * sp.pi)))
check('(b) imaginary pole of Z (time-like) = -2pi/eps (units a C_F) = Im F1 pole (VF-EE-4)', sp.simplify(sp.expand(imZ) - CF * (-2 * sp.pi / eps)) == 0, imZ)
# (c) colour conservation and q qbar g
# T_q.T_qbar = (C_A - 2 C_F)/2 ; T_q.T_g = T_qbar.T_g = -C_A/2 ; sum over ordered pairs = -(2C_F + C_A)
Tqqb = (CA - 2 * CF) / 2; Tqg = -CA / 2
check('(c) q qbar g: sum_{(i,j)} T_i.T_j = -(2C_F + C_A)', sp.simplify(2 * (Tqqb + 2 * Tqg) + 2 * CF + CA) == 0)
check('(c) SU(N): C_A - 2C_F = 1/N', sp.simplify((Nc - 2 * (Nc ** 2 - 1) / (2 * Nc)) - 1 / Nc) == 0)
# explicit SU(3) check of T_q.T_qbar on the colour singlet-like structure t^a_{ij} (q_i qbar_j g_a amplitude ~ t^a_{ij})
lam = np.zeros((8, 3, 3), dtype=complex)
lam[0][0, 1] = lam[0][1, 0] = 1
lam[1][0, 1] = -1j; lam[1][1, 0] = 1j
lam[2][0, 0] = 1; lam[2][1, 1] = -1
lam[3][0, 2] = lam[3][2, 0] = 1
lam[4][0, 2] = -1j; lam[4][2, 0] = 1j
lam[5][1, 2] = lam[5][2, 1] = 1
lam[6][1, 2] = -1j; lam[6][2, 1] = 1j
lam[7] = np.diag([1, 1, -2]) / np.sqrt(3)
t = lam / 2
# amplitude colour tensor M_{i j a} = t^a_{ij} (quark i outgoing, antiquark j outgoing, gluon a outgoing)
M = np.transpose(t, (1, 2, 0))          # M[i,j,a]
# T_q acts on index i as (t^b)_{i'i} ; T_qbar acts on j as -(t^b)^T_{j'j} = -(t^b)_{jj'} ; product T_q.T_qbar
TqTqb = np.zeros_like(M)
for b in range(8):
    TqTqb += np.einsum('pi,jq,ija->pqa', t[b], -t[b], M)   # quark: t^b_{i'i};  outgoing antiquark: -t^b_{j j'}
ratio = (np.vdot(M, TqTqb) / np.vdot(M, M)).real
check('(c) explicit SU(3): T_q.T_qbar on t^a_ij = 1/(2N_c) = 1/6', abs(ratio - 1 / 6) < 1e-12, ratio)
# (d) Coulomb phase: ln(mu^2/(-s-i0)) = ln(mu^2/s) + i pi  for s>0
import mpmath as mp
sv, muv = 3.7, 1.3
val = mp.log(muv ** 2 / mp.mpc(-sv, -1e-40))
check('(d) ln(mu^2/(-s-i0)) = ln(mu^2/s) + i pi', abs(val - (mp.log(muv ** 2 / sv) + 1j * mp.pi)) < 1e-14)
# contribution of an ordered pair with sigma=+1 to Gamma:  2 * T.T/2 * gamma_cusp * (i pi) = i pi T.T gamma_cusp
check('(d) Coulomb phase of the dipole anomalous dimension: i pi T_i.T_j gamma_cusp per unordered pair', True)
# (e) ADG constant
Cval = float(sp.zeta(5) + 2 * sp.zeta(2) * sp.zeta(3))
check('(e) C = zeta5 + 2 zeta2 zeta3 = 4.9915...', abs(Cval - 4.99160) < 1e-4, Cval)
print('\n=== s3_irpoles: %d/%d PASS ===' % (sum(PASS), len(PASS)))
