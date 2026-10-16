import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
from sympy import Rational as R
def S(k, n): return sum(R(1, j**k) for j in range(1, n+1))
def bbdm_B2_over_CF_no_ln4pi(n):   # BBDM preprint eq. (3.9), without the gamma0~ (ln4pi - gammaE) term
    s1, s2 = S(1, n), S(2, n)
    nested = sum(S(1, s)/s for s in range(1, n+1))
    return 3*s1 - 4*s2 - R(2, n*(n+1))*s1 + 4*nested + R(3, n) + R(4, n+1) + R(2, n**2) - 9
def cdis_C2q_over_CF(n):           # c_dis section 11 (alpha_s/2pi normalisation)
    s1, s2 = S(1, n), S(2, n)
    return s1**2 - s2 + R(3,2)*s1 - s1/(n*(n+1)) + R(3, 2*n) + R(2, n+1) + R(1, n**2) - R(9,2)
def gt0(n):                        # BBDM (3.10): gamma0~^n
    return 1 - R(2, n*(n+1)) + 4*sum(R(1, j) for j in range(2, n+1))
def Pqq_over_CF(n):                # c_dis P_qq,N / C_F
    return R(3,2) + R(1, n*(n+1)) - 2*S(1, n)
ok = True
for n in range(1, 21):
    a, b = bbdm_B2_over_CF_no_ln4pi(n), 2*cdis_C2q_over_CF(n)
    ok &= (a == b)
    # MS -> MSbar: the (ln4pi-gammaE) coefficient gamma0~ should equal -2 P_qq,N/C_F ... check relation
    rel = gt0(n) / (-2*Pqq_over_CF(n)) if Pqq_over_CF(n) != 0 else None
    if n <= 8: print(n, 'B2(BBDM, MSbar part)/CF =', a, ' 2*C2q(c_dis)/CF =', b, ' equal:', a == b, ' gt0 =', gt0(n), ' gt0/(-2Pqq/CF) =', rel)
print('ALL N=1..20 EQUAL:', ok)
# C_L check: BBDM (3.8) C_L = (g^2/16pi^2) C_F 4/(n+1) -> alpha_s/4pi * 4 C_F/(n+1) = alpha_s/2pi * 2C_F/(n+1)
print('C_L: BBDM 4/(n+1) in alpha_s/4pi units == 2 * c_dis 2/(n+1) in alpha_s/2pi units: True by inspection')
# Bjorken sum rule relative correction: C_1 = C_2 - C_L at n=1 (alpha_s/2pi units): 0 - 2*C_F/2
print('C^q_{1,1}/C_F =', cdis_C2q_over_CF(1) - R(2,2), ' -> relative correction -(alpha_s/2pi) C_F = -(2/3) alpha_s/pi; BBDM (4.12): 8/((33-2f) ln) = (2/3)(alpha_s/pi) with alpha_s/pi = 12/((33-2f) ln)')
