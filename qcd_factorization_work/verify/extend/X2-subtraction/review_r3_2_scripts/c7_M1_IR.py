# Reviewer r3_2: (M1) is IR-divergent beyond one loop when a self-energy sits on the soft gluon line.
# Effective one-loop integrands F_n = 1/(D_g^n D_1 D_2): n=2 is the MS-bar counterterm insertion of the one-loop
# psi-bubble on the gluon line (the renormalised bubble gives ln(D_g)/D_g^2, worse by a log); n=3 is the k-integrand of
# the three-loop graph with the UV-finite massless two-loop 'kite' self-energy, Sigma_2(k^2) ~ g^4 6 zeta3/(16pi^2)^2/(-k^2).
# Fibered density for 0<x<P (close on the D_1 pole): rho_n = (P-x)^(n-1)/(A^n D2hat); rho_n >= 0.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 20
P = Pp = 1/mp.sqrt(2); m2 = mp.mpf('0.01'); Qt2 = 2*P*Pp
def rho(n, x, k):
    u = x/P; A = P*k + x*m2*(1-u); e2 = m2 + 2*Pp*x
    D2 = e2*(1 + m2/Qt2 + k/(Qt2*(1-u))) + k
    return (P-x)**(n-1)/(A**n*D2)
def I(n, d):
    f = lambda x: mp.quad(lambda k: rho(n, x, k), [0, x*m2, 1, mp.inf])
    pts = [d] + [mp.mpf(10)**j for j in range(int(mp.log10(d))+1, 0) if mp.mpf(10)**j < P] + [P]
    return mp.quad(f, pts)
for n in [1, 2, 3]:
    vals = [(d, I(n, mp.mpf(d))) for d in ['1e-3', '1e-5', '1e-7']]
    print(f"n={n}: " + ";  ".join(f"int_(x>{d}) rho = {mp.nstr(v, 8)}" for d, v in vals))
