# high-precision recheck of rv21_box.py part (3) at |omega| = 0.8: the alternating sums in the naive
# coefficients lose ~n digits, so the coefficients are computed at high working precision.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 150
a1, a2, a3, a4, D = mp.mpf('1.0'), mp.mpf('1.2'), mp.mpf('0.9'), mp.mpf('1.1'), mp.mpf('5.3')
def G(al, be, m):
    return (mp.gamma(al+be-D/2)*mp.gamma(m+D/2-al)*mp.gamma(D/2-be)/(mp.gamma(al)*mp.gamma(be)*mp.gamma(m+D-al-be)))
def bg(x, k):
    r = mp.mpf(1)
    for i in range(k): r *= (x-i)/(i+1)
    return r
def c_mom(n):
    tot = mp.mpf(0)
    for i in range(n+1):
        j = n-i
        s = mp.fsum(mp.binomial(j, l)*(-1)**(j-l)*G(a1+a2+i, a3+a4+j, i+l) for l in range(j+1))
        tot += bg(-a2, i)*bg(-a3, j)*s
    return tot
Nmax = 160
coef = [c_mom(n) for n in range(Nmax+1)]
mp.mp.dps = 20
a = a1+a2+a3+a4; c = a-D/2
pref = mp.gamma(c)/(mp.gamma(a1)*mp.gamma(a2)*mp.gamma(a3)*mp.gamma(a4))*mp.beta(a1+a2-c, a3+a4-c)
om = mp.mpc(0, 0.8)
f = lambda y, z: y**(a1-1)*(1-y)**(a2-1)*z**(a3-1)*(1-z)**(a4-1)*(1-om*(y+z-1))**(-c)
full = pref*mp.quad(f, [0, 0.5, 1], [0, 0.5, 1])
for Ncut in [40, 80, 120, 160]:
    ser = mp.fsum(coef[n]*om**n for n in range(Ncut+1))
    print("omega=0.8i  N=%3d  series=%s  full=%s  rel=%.2e" % (Ncut, mp.nstr(ser, 13), mp.nstr(full, 13), abs(ser/full-1)))
print("|c_n| at n=20,80,160:", [mp.nstr(abs(coef[n]), 5) for n in (20, 80, 160)], "(expected ~ n^{c-1-min(a1+a3,a2+a4)} decay)")
