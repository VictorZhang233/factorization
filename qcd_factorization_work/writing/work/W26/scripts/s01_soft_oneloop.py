# W26 / Ch23 -- s01: one-loop off-light-cone soft function, CS kernel, D, S_r (ex:yzliu-soft-oneloop)
# Conventions: a = alpha_s C_F/(2 pi); L_b = ln(mu^2 b^2/b0^2); Ycal = Y+Y' (total rapidity / hyperbolic angle)
# One-loop soft factor (lem:tmd-soft-oneloop, VF-TMD-8):  S^(1) = -(alpha_s C_F/pi) (Ycal coth Ycal - sigma) L_b
#   sigma = 1: time-like lines with self-energies (Ji-Liu-Liu normalisation, def:lamet-soft-offlc)
#   sigma = 0: space-like lines without self-interactions (Collins, def:tmd-soft)
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

Y, Lb, a = sp.symbols('Ycal L_b a', positive=True)
alphaCFpi = 2*a          # alpha_s C_F/pi = 2a
out = []
for sigma in (1, 0):
    S1 = -alphaCFpi*(Y*sp.coth(Y) - sigma)*Lb
    # large-Ycal expansion: coth Y = 1 + 2 e^{-2Y} + ...
    S1_asym = sp.expand(-alphaCFpi*(Y - sigma)*Lb)
    rem = sp.simplify(S1 - S1_asym)
    remY = sp.limit(rem*sp.exp(Y), Y, sp.oo)   # should be 0 => remainder is O(Y e^{-2Y})
    K1 = sp.expand(S1_asym).coeff(Y, 1)
    D1 = sp.expand(S1_asym).coeff(Y, 0)
    Sr1 = -D1
    out.append((sigma, sp.simplify(S1_asym), sp.simplify(K1), sp.simplify(D1), sp.simplify(Sr1), remY))
    print('sigma=%d: S^(1) -> %s ; Ktilde^(1) = %s ; D^(1) = %s ; S_r^(1) = -D^(1) = %s ; lim e^Y*remainder = %s'
          % (sigma, out[-1][1], out[-1][2], out[-1][3], out[-1][4], remY))
# checks against VF-YZL-2 / VF-LAM-15 / def:lamet-soft-offlc
s1 = out[0]
assert sp.simplify(s1[1] - a*(2 - 2*Y)*Lb) == 0, 'S^(1) != a[2-2(Y+Y\')]L_b'
assert sp.simplify(s1[2] + 2*a*Lb) == 0, 'K^(1) != -2 a L_b'
assert sp.simplify(s1[4] + 2*a*Lb) == 0, 'S_r^(1) != -2 a L_b'
assert sp.simplify(out[1][3]) == 0, 'sigma=0 constant should vanish'
print('PASS: sigma=1 gives S^(1)=a[2-2(Y+Y\')]L_b, K^(1)=-2aL_b, D^(1)=2aL_b, S_r^(1)=-2aL_b=-(alpha_s C_F/pi)L_b; sigma=0 gives D^(1)=0 (trap)')

# mu-dependence: mu^2 d/dmu^2 ln S = -Gamma(Ycal) with Gamma(beta)=(alpha_s C_F/pi)(beta coth beta -1) (two cusps, d/dlnmu each)
mu2dS = sp.diff(-alphaCFpi*(Y*sp.coth(Y) - 1)*Lb, Lb)
GammaCusp = alphaCFpi*(Y*sp.coth(Y) - 1)
assert sp.simplify(mu2dS + GammaCusp) == 0
# large-angle limit: Gamma(theta) -> theta*Gamma_cusp + gamma_HH, gamma_HH^(1) = -alpha_s C_F/pi
lim_const = sp.limit(GammaCusp - alphaCFpi*Y, Y, sp.oo)
print('large-angle constant of the one-loop cusp: gamma_HH^(1) =', lim_const, '(= -alpha_s C_F/pi)')
assert sp.simplify(lim_const + alphaCFpi) == 0
# => mu^2 d ln S_I/dmu^2 = +gamma_HH, S_I = e^{-D}
print('PASS: mu^2 dlnS/dmu^2 = -Gamma(Y+Y\'), Gamma -> (Y+Y\')Gamma_cusp + gamma_HH, hence mu^2 dKtilde/dmu^2=-Gamma_cusp, mu^2 dlnS_I/dmu^2 = gamma_HH')

# D = 2 D1 - D2 and the check (1/2) ln S_I = (1/2) ln S2 - ln S1 (thm:yzliu-intrinsic-soft (b))
K, D1s, D2s, d, dp, Yp = sp.symbols('K D1 D2 delta deltap Yp')
lnS1 = (Yp - sp.log(d))*K + D1s          # S_1(b,delta,Y')
lnS2 = -sp.log(d*dp)*K + D2s             # S_2(b,delta,delta')
# S_I = S_2(delta,delta') / [S_1(delta,Y'=0) S_1(delta',Y=0)]  (Ji:2019sxk eq. (19))
lnSI = lnS2 - lnS1.subs(Yp, 0) - lnS1.subs({Yp: 0, d: dp})
lnSI = sp.simplify(sp.expand(sp.expand_log(lnSI, force=True)))
print('ln S_I =', lnSI, '  => D = -ln S_I =', sp.simplify(-lnSI))
assert sp.simplify(lnSI - (D2s - 2*D1s)) == 0
print('PASS: K cancels; S_I = e^{-D} with D = 2 D1 - D2  <=>  D1 = (D + D2)/2')
