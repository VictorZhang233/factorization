import sys,os; sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps=40
z3=mp.zeta(3); pi2=mp.pi**2
# Becher-Neubert (0904.1021) two-loop velocity-dependent cusp AD (colour-stripped), C_A bracket B(beta):
def B(b):
    e=mp.e**(-2*b); c=mp.coth(b)
    return c**2*(mp.polylog(3,e)+b*mp.polylog(2,e)-z3+pi2/6*b+b**3/3) \
         + c*(mp.polylog(2,e)-2*b*mp.log(1-e)-pi2/6*(1+b)-b**2-b**3/3) + pi2/6+z3+b**2
for b in [mp.mpf('1e-3'),mp.mpf('1e-2'),5,10,20,40]:
    print('beta=',b,' B(beta)=',mp.nstr(B(b),15))
# zero-recoil check: Gamma_hh(0)=0 => C_A part: C_F[(67/36-pi^2/12) + B(0)/2] + 2 gammaQ2_CA/CF = 0  (units (as/pi)^2)
gQ2_CA = (2*pi2/3-mp.mpf(98)/9-4*z3)/16   # gamma^Q two-loop C_F C_A coefficient in (as/pi)^2 units (BN normalisation (as/4pi)^2)
B0=B(mp.mpf('1e-8'))
print('zero recoil C_A check (should be 0):', mp.nstr((mp.mpf(67)/36-pi2/12)+B0/2+2*gQ2_CA,12))
# large-beta constant of Gamma_hh = C_F gamma_cusp(beta) + 2 gamma^Q -> constant = C_F*C_A*B(inf)/2 + 2 gamma^Q
GS2_CA = -( B(mp.mpf(60))/2 + 2*gQ2_CA )   # Gamma_S = -(constant)   [mu^2 dlnS/dmu^2 = -Gamma_hh(theta)]
print('Gamma_S^(2) C_F C_A coefficient (as/pi)^2 :', mp.nstr(GS2_CA,15))
print('   49/36 - pi^2/12 + zeta3/2 =', mp.nstr(mp.mpf(49)/36-pi2/12+z3/2,15))
print('   Liu APPB eq.(81) value -49/36+pi^2/12-zeta3/2 =', mp.nstr(-mp.mpf(49)/36+pi2/12-z3/2,15))
# n_f part from running-coupling argument: Gamma_S^(2)_nf = -(5/9) C_F T_F n_f = -(5/18) C_F n_f
print('Gamma_S^(2) n_f coefficient (C_F n_f, T_F=1/2): -5/18 =', mp.nstr(-mp.mpf(5)/18,10), '; Liu eq.(81): +5/18')
