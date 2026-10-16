import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
from sympy import Rational as R, zeta, symbols, expand, N, log, pi, EulerGamma
nf = symbols('n_f')
CF, CA, TF = R(4,3), 3, R(1,2)
z3 = zeta(3)
# BCK 2010 (PRL 104, 132004), eq. for d2 with T_f = T n_f, a_s = alpha_s/pi, MSbar, mu^2 = Q^2
d2 = -R(3,32)*CF**2 + CF*TF*nf*(z3 - R(11,8)) + CF*CA*(R(123,32) - R(11,4)*z3)
d2 = expand(d2)
c0, c1 = d2.subs(nf, 0), d2.coeff(nf)
print('r2(MSbar) = %.6f + (%.6f) n_f' % (float(N(c0, 20)), float(N(c1, 20))))
print('  exact:', c0, '+', c1, 'n_f')
# MS (no bar) value: alpha_MSbar = alpha_MS * (1 + (beta0/4)(ln4pi - gammaE) a) at one loop => r2(MS) = r2(MSbar) + (beta0/4)(ln 4pi - gamma_E)
beta0 = 11 - R(2,3)*nf      # in units where mu^2 d a/d mu^2 = -(beta0/4) a^2, a = alpha_s/pi
shift = expand(beta0/4*(log(4*pi) - EulerGamma))
r2MS = expand(d2 + shift)
print('r2(MS)    = %.4f + (%.4f) n_f   [DS 1979 SLAC-PUB-2332 eq. (11): 7.35 - .442 N_f (MS); 1.98 - .115 N_f (MSbar)]' % (float(N(r2MS.subs(nf,0), 15)), float(N(r2MS.coeff(nf), 15))))
for n in (3, 4, 5, 6):
    print('  n_f=%d: r2(MSbar) = %.5f' % (n, float(N(d2.subs(nf, n), 15))))
