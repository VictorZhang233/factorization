import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
x, kap, m2, P, Pp, u = sp.symbols('x kap m2 P Pp u', positive=True)
A = x*m2*(1 - x/P) + P*kap
B = x*m2 + P*kap
e2 = m2 + 2*Pp*x; h2 = 2*Pp*x
Qt2 = 2*P*Pp
# Gamma mid: 1/(A * Dhat2),  Dhat2 = e2*(1 + m2/Qt2 + kap/(Qt2*(1-x/P))) + kap
Dhat2 = e2*(1 + m2/Qt2 + kap/(Qt2*(1 - x/P))) + kap
rhoG = 1/(A*Dhat2)
# check against residue form
km = sp.symbols('km')
k2 = 2*x*km - kap
Dg = -k2; D2 = m2 + 2*Pp*x - (m2/Pp)*km - k2
k1m = -(m2*(1 - x/P) + kap)/(2*(P - x))
rhoG_res = (1/((P - x)*Dg*D2)).subs(km, k1m)
print("Gamma mid closed form check:", sp.simplify(rhoG - rhoG_res))
rhoS = 1/(B*e2)
rhoC1 = x*m2/(2*P*Pp*A*B)
rhoC2 = -(1/P)/((e2 + kap)*e2)
rhoH = -x/(P*(h2 + kap)*(h2*(P - x) + P*kap))
r_mid = sp.together(rhoG - rhoS - rhoC1 - rhoC2 - rhoH)
num, den = sp.fraction(r_mid)
num = sp.expand(num)
print("den factors:", sp.factor(den))
print("numerator degree in m2:", sp.Poly(num, m2).degree(), " lowest power of m2:", min(mon[0] for mon in sp.Poly(num, m2).monoms()))
# coefficient structure
P_ = sp.Poly(num, m2)
for (deg,), c in zip(P_.monoms(), P_.coeffs()):
    print("  m2^%d coefficient: %s" % (deg, sp.factor(c)))
