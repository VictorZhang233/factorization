# W26 / Ch23 -- s12: (a) factorial enhancement in the super-renormalizable 2D O(N) model (prop:yzliu-on-factorial, VF-YZL-14):
#   D_n(r) = d^n/dt^n [ r^t psi(1-n-t) - 1/t ]_{t=0},  r = m^2/p^2  ->  -n! r + (-1)^n n!/r + ... (poles of psi at t = +-1)
# (b) single-line power counting of the quasi-TMD (prop:yzliu-qtmd-powercount, VF-YZL-8)
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 50

def Dn(n, r):
    f = lambda t: r**t*mp.digamma(1 - n - t) - 1/t
    # Taylor coefficients around t=0 via contour (Cauchy) integral on |t| = 1/2 (radius < 1, the nearest poles are at t = +-1)
    R = mp.mpf('0.5'); M = 4096
    s = mp.mpf(0)
    for k in range(M):
        th = 2*mp.pi*k/M
        tt = R*mp.expj(th)
        s += f(tt)*mp.expj(-n*th)
    coeff = s/M/R**n
    return mp.re(coeff)*mp.factorial(n)
r = mp.mpf('0.3')
for n in [4, 8, 12, 16, 20]:
    d = Dn(n, r)
    asym = -mp.factorial(n)*r + (-1)**n*mp.factorial(n)/r
    print('n=%2d: D_n = %s ; -n! r + (-1)^n n!/r = %s ; ratio = %s' % (n, mp.nstr(d, 12), mp.nstr(asym, 12), mp.nstr(d/asym, 10)))
print('=> with prefactor (p^2)^{-n} (g/4pi)^{n+1}: -n! g^{n+1}/(4pi)^{n+1} m^2/(p^2)^{n+1} + (-1)^n n! g^{n+1}/(4pi)^{n+1} /(m^2 (p^2)^{n-1})')

# (b) power counting:  F(H) = sum_{s=0,1}[N(CH,1,s)+N(SH,1,s)] + N(CH,3/2,1/2) + 3/2 sum_s N(SH,3/2,s) - N(CH,1,l) - 7/2
def FH(N_CH1=0, N_SH1=0, N_CHq=0, N_SHdip=0, N_CHlong=0):
    return N_CH1 + N_SH1 + N_CHq + mp.mpf(3)/2*N_SHdip - N_CHlong - mp.mpf(7)/2
print('leading region (2 collinear quarks, 1 dipole line, k longitudinal gluons counted in N(CH,1,s) and N(CH,1,l)):')
for k in range(4):
    print('  k=%d longitudinal gluons: F(H) = %s' % (k, FH(N_CH1=k, N_CHq=2, N_SHdip=1, N_CHlong=k)))
print('  one extra soft gluon into H: F(H) =', FH(N_SH1=1, N_CHq=2, N_SHdip=1), '(costs +1)')
print('  one transverse collinear gluon into H: F(H) =', FH(N_CH1=1, N_CHq=2, N_SHdip=1), '(costs +1)')
print('  no dipole line (hard momentum between 0 and b): F(H) =', FH(N_CHq=2), ' -> needs N(SH,3/2,.) >= 1 for F(H)>=0?')
print('PASS')
