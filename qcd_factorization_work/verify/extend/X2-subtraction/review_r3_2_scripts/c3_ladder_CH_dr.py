# Reviewer r3_2: is the ladder C_H (whole-integrand value quoted in the report) equal to the DR-linearity value
# T_H Gamma (massless-target one-rung ladder, analytically continued from eps<0), with T_H C_R1 scaleless?
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 25
def THGamma(eps, x):
    cx = 1 - 1/mp.mpf(x)
    B = mp.gamma(-eps)*mp.gamma(2-eps)/mp.gamma(2-2*eps)
    Iy = mp.quad(lambda y: y*(y + (1-y)*cx)**(-1-eps), [0, 1])
    return mp.gamma(1+eps)*B*Iy
for e in ['0.1', '0.2', '0.3']:
    print(f"eps={e}: T_H Gamma (continued) = {mp.nstr(THGamma(mp.mpf(e), 2), 15)}")
