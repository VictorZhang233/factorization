import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
L, l, t, c = sp.symbols('L l t c', positive=True)
# BFH eq. (thelog): int_{tau Q}^{Q} dkT/kT int_{kT/Q}^{1} dtheta/theta 2 u(k) L2 ((-i pi) ln(kT/tau Q))^2,
# l = ln(kT/(tau Q)) in [0,L], t = ln(1/theta) in [0, L-l]; u(k)=Theta(tau - kT theta/Q) <=> t > l ; L2 = l^2
I = 2*sp.integrate(l**4*sp.integrate(1, (t, l, L-l)), (l, 0, L/2))
print("BFH LL integral (u = Theta(t>l)):", sp.factor(I), " -> coefficient 1/480 ?", sp.simplify(I/L**6) == sp.Rational(1, 480))
# variant u = Theta(tau - kT theta/(2Q)) <=> t > l - ln2 : changes only subleading powers
# region: for l<c the t-range is [0, L-l]; for c<l<(L+c)/2 it is [l-c, L-l]   (L > c)
I2 = 2*sp.integrate(l**4*(L - l), (l, 0, c)) + 2*sp.integrate(l**4*((L - l) - (l - c)), (l, c, (L + c)/2))
I2 = sp.expand(I2)
print("variant with shift c (=ln2):", I2)
# BHNS (arXiv:2603.12383) iterated scale integral, omega_c = sqrt(Q omega): L' = ln(omega_c/omega) = ell/2
x1, x2, x3, x4, Lp = sp.symbols('x1 x2 x3 x4 Lp', positive=True)
J = sp.integrate((Lp - x1)*sp.integrate(sp.integrate(sp.integrate(x4, (x4, 0, x3)), (x3, 0, x2)), (x2, 0, x1)), (x1, 0, Lp))
ell = sp.symbols('ell', positive=True)
print("BHNS integral:", sp.factor(J), "-> with L'=ell/2:", sp.factor(J.subs(Lp, ell/2)))
