# First super-leading logarithm for qq -> qq from Becher-Neubert-Shao, PRL 127 (2021) 212002 [arXiv:2107.01212], eqs. (14), (19),
# compared with Forshaw-Kyrieleis-Seymour 2006 eq. (3.24) and FKS 2008 eq. (2.22) / Keates-Seymour 2009 eq. (3.2).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
from sympy import symbols, Rational as R, factorial, simplify, factor, pi, expand, hyper, series, KroneckerDelta
Nc, dY, aS, L, sB = symbols('N_c DeltaY alpha_s L sigma_B', positive=True)
CF = (Nc**2 - 1)/(2*Nc)
J2 = dY; J43 = 2*dY                      # forward scattering: J_2 = J_43/2 = DeltaY (BNS)
def C_octet(r, n):                       # BNS eq. (19), octet
    return sB * 2**(8-r) * pi**2 * (4*Nc)**n * (CF*J43 + J2/Nc*(Nc**2 - 2**(r+1) + 1)*(1 - KroneckerDelta(r, 0)))
def C_singlet(r, n):                     # BNS eq. (19), singlet
    return sB * 2**(8-r) * pi**2 * (4*Nc)**n * CF * (-J43 + 2*J2*(1 - KroneckerDelta(r, 0)))
def sigma_n(C, n):                       # BNS eq. (14)
    pref = (aS/(4*pi))**(n+3) * L**(2*n+3) * (-4)**n * factorial(n) / factorial(2*n+3)
    return pref * sum(factorial(2*r)/(4**r*factorial(r)**2) * C(r, n) for r in range(n+1))
s1 = simplify(sigma_n(C_octet, 1))
fks_norm = sB * (2*aS/pi)**4 * L**5 * pi**2 * dY
print('octet  n=1:  sigma_1 / [sigma_B (2 alpha_s/pi)^4 L^5 pi^2 DeltaY] =', factor(simplify(s1/fks_norm)))
print('   FKS 2006 eq.(3.24): -(3N^2-4)/480  [one side of the gap, y>0];  FKS 2008 eq.(2.22), KS 2009 eq.(3.2): -(3N^2-4)/240 [both sides]')
# consistency check against BNS eq. (21) for the singlet: expansion of -sigma_B 4C_F/(3 pi) a^3 L^3 DeltaY 2F2(1,1;2,5/2;-w), w = Nc a L^2/pi
w = symbols('w')
for n in (0, 1, 2):
    lhs = simplify(sigma_n(C_singlet, n))
    coeff_w = (R(1,1) if n == 0 else None)
    print('singlet n=%d from (14),(19):' % n, factor(lhs))
# 2F2(1,1;2,5/2;-w) series: sum_k (1)_k (1)_k/((2)_k (5/2)_k) (-w)^k/k!
from sympy import rf
ser = sum(rf(1,k)*rf(1,k)/(rf(2,k)*rf(R(5,2),k))*(-w)**k/factorial(k) for k in range(3))
expr21 = expand(-sB*4*CF/(3*pi)*aS**3*L**3*dY*ser.subs(w, Nc*aS*L**2/pi))
print('BNS eq.(21) expanded to O(w^2):', factor(expr21))
