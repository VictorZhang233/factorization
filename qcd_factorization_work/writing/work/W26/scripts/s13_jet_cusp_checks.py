# W26 / Ch23 -- s13: (A) renormalized one-loop space-like jet function from the bare DR expression of Ji-Liu-Su
#   (JHEP 08 (2023) 037, eq. before (3.9)):  J~ = 1 + g^2 C_F Gamma(D/2-1) (mu0 |z|)^{4-D} / (4 pi^{D/2})
#                                                  * ( 2/(D-4)^2 - 1/((D-4)(D-3)) ),
#   MSbar: mu^2 = 4 pi mu0^2 e^{-gamma_E}; expected J~ = 1 + a (L_z^2/2 + L_z + pi^2/12 + 2), L_z = ln(mu^2 z^2 e^{2gE}/4),
#   a = alpha_s C_F/(2 pi);  RGE  dlnJ/dln mu = Gamma_cusp L_z - gamma_J,  Gamma_cusp = 2a, gamma_J^(1) = -2a.
# (B) Becher-Neubert two-loop velocity-dependent cusp (PRD 79 (2009) 125004, eqs. (13)-(15)):
#   C_A bracket B(beta): B(0) = zeta3 - 1 (zero recoil) and B(beta) -> 0 exponentially as beta -> infinity,
#   so that the large-angle constant gamma_HH^(2) equals 2 gamma^Q_1 (heavy-quark field AD) in (alpha_s/pi)^2 units.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp, mpmath as mp

# ---------------- (A) ----------------
eps, g, CF, mu0, z, mu = sp.symbols('epsilon g C_F mu0 z mu', positive=True)
D = 4 - 2*eps
bare1 = g**2*CF*sp.gamma(D/2 - 1)*(mu0*z)**(4 - D)/(4*sp.pi**(D/2))*(2/(D - 4)**2 - 1/((D - 4)*(D - 3)))
# express mu0 through the MSbar scale: mu0^2 = mu^2 e^{gE}/(4 pi)
bare1 = bare1.subs(mu0, sp.sqrt(mu**2*sp.exp(sp.EulerGamma)/(4*sp.pi)))
alpha = g**2/(4*sp.pi)
ser = sp.series(sp.simplify(bare1/(alpha*CF/(2*sp.pi))), eps, 0, 1).removeO()
ser = sp.expand(sp.simplify(ser))
pole2 = sp.simplify(ser.coeff(eps, -2)); pole1 = sp.simplify(ser.coeff(eps, -1)); fin = sp.simplify(ser.coeff(eps, 0))
Lz = sp.Symbol('L_z')
fin_L = sp.simplify(sp.expand(sp.expand_log(fin.subs(z, sp.sqrt(4*sp.exp(Lz - 2*sp.EulerGamma))/mu), force=True)))
print('bare one-loop / a : 1/eps^2 coefficient =', pole2, ' ; 1/eps coefficient =', sp.simplify(sp.expand_log(pole1.subs(z, sp.sqrt(4*sp.exp(Lz - 2*sp.EulerGamma))/mu), force=True)))
print('finite part (MSbar, poles subtracted) =', sp.expand(fin_L))
target = Lz**2/2 + Lz + sp.pi**2/12 + 2
okA = sp.simplify(fin_L - target) == 0
print('equals L_z^2/2 + L_z + pi^2/12 + 2 :', okA)
# RGE at fixed alpha: d/dln mu (L_z^2/2+L_z) with dL_z/dln mu = 2 -> 2 L_z + 2 = Gamma_cusp/a * L_z - gamma_J/a with Gamma=2a, gamma_J=-2a
print('dJ^(1)/dln mu / a =', sp.expand(sp.diff(target, Lz)*2), ' = 2 L_z + 2  (Gamma_cusp = 2a, gamma_J^(1) = -2a)')

# ---------------- (B) ----------------
mp.mp.dps = 40
z3, pi2 = mp.zeta(3), mp.pi**2
def Bbr(b):
    e = mp.e**(-2*b); c = mp.coth(b)
    return (c**2*(mp.polylog(3, e) + b*mp.polylog(2, e) - z3 + pi2/6*b + b**3/3)
            + c*(mp.polylog(2, e) - 2*b*mp.log(1 - e) - pi2/6*(1 + b) - b**2 - b**3/3) + pi2/6 + z3 + b**2)
for b in ['1e-3', '1e-2', '0.1']:
    print('B(beta=%s) = %s   (zeta3-1 = %s)' % (b, mp.nstr(Bbr(mp.mpf(b)), 15), mp.nstr(z3 - 1, 15)))
for b in [5, 10, 20, 40]:
    print('B(beta=%d) = %s' % (b, mp.nstr(Bbr(mp.mpf(b)), 6)))
okB = abs(Bbr(mp.mpf('1e-4')) - (z3 - 1)) < 1e-6 and abs(Bbr(mp.mpf(40))) < 1e-25
# 2 gamma^Q_1 in (alpha_s/pi)^2 units, C_F stripped: gamma^Q_1 = C_F[C_A(2pi^2/3-98/9-4z3) + 40/9 T_F n_f] in (alpha_s/4pi)^2
twogQ_CA = 2*(2*pi2/3 - mp.mpf(98)/9 - 4*z3)/16
print('2 gamma^Q_1 (C_A part, (alpha_s/pi)^2) =', mp.nstr(twogQ_CA, 20), ' ; -49/36 + pi^2/12 - z3/2 =', mp.nstr(-mp.mpf(49)/36 + pi2/12 - z3/2, 20))
okB = okB and abs(twogQ_CA - (-mp.mpf(49)/36 + pi2/12 - z3/2)) < 1e-30
print('PASS' if (okA and okB) else 'FAIL')
