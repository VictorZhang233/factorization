import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 25
# NLO P_{q qbar}^{V(1)}(x) (Curci-Furmanski-Petronzio 1980; ESW eq. (4.108)), units (alpha_s/2pi)^2:
#   C_F (C_F - C_A/2) [ 2 p_qq(-x) S_2(x) + 2(1+x) ln x + 4(1-x) ],
#   p_qq(x) = 2/(1-x) - 1 - x,  S_2(x) = int_{x/(1+x)}^{1/(1+x)} dz/z ln((1-z)/z)
def S2(x):
    return mp.quad(lambda t: mp.log((1-t)/t)/t, [x/(1+x), mp.mpf(1)/2, 1/(1+x)])
def S2_closed(x):
    return -2*mp.polylog(2,-x) + mp.log(x)**2/2 - 2*mp.log(x)*mp.log(1+x) - mp.pi**2/6
print('S2 closed-form check at x=0.3:', mp.nstr(S2(mp.mpf('0.3')),15), mp.nstr(S2_closed(mp.mpf('0.3')),15))
pqq = lambda x: 2/(1-x) - 1 - x
f = lambda x: 2*pqq(-x)*S2_closed(x) + 2*(1+x)*mp.log(x) + 4*(1-x)
for N in (1,2,3,4):
    print('N=%d  int x^{N-1} [P_qqbar^V(1)/(CF(CF-CA/2))] =' % N, mp.nstr(mp.quad(lambda x: x**(N-1)*f(x), [0,1]),15))
print('13/2-6 zeta2+4 zeta3 =', mp.nstr(mp.mpf(13)/2 - 6*mp.zeta(2) + 4*mp.zeta(3),15))
