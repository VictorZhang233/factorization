"""R1 check 1: off-shell Sudakov triangle, refdoc eqs. (3.3)-(3.6) (PDF p.15-17).

I = int d^dk/(i pi^{d/2}) 1/[(-k^2)(-(p1-k)^2)(-(p2+k)^2)],  -p1^2=-p2^2=m^2, -(p1+p2)^2=Q^2.
In d=4: Feynman parameters x0 (gluon), x1 (p1-k), x2 (p2+k):
  F = m^2 x0 (x1+x2) + Q^2 x1 x2 ,  I = int_simplex 1/F .
Claims checked:
  (3.6)  Q^2 I = ln^2(Q^2/m^2) + O(ln^0)   [actual constant: pi^2/3]
  (3.5)  region scalings; 1/eps^2 coefficients (c,-c,-c,c) with c=1
  hard-region formula with Gamma(1+eps)Gamma(1-eps)^2/Gamma(1-2eps)/eps^2.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import sympy as sp

mp.mp.dps = 30

def I_exact(t):
    # Q^2 I with Q=1, m^2=t ; integrate over simplex x1,x2>=0, x1+x2<=1 ; x0 = 1-x1-x2
    # do the x0 direction analytically: use u = x1/(x1+x2), r = x1+x2 ; Jacobian r
    # F = t (1-r) r + r^2 u(1-u) = r [ t(1-r) + r u(1-u) ]
    # int_0^1 dr r / (r [t(1-r) + r a]) = int_0^1 dr / (t + r (a - t)) = ln(a/t)/(a-t)
    f = lambda u: (mp.log(u*(1-u)/t)/(u*(1-u)-t)) if abs(u*(1-u)-t) > mp.mpf('1e-25') else 1/t
    return mp.quad(f, [0, mp.mpf(1)/2 - mp.sqrt(mp.mpf(1)/4 - t), mp.mpf(1)/2, mp.mpf(1)/2 + mp.sqrt(mp.mpf(1)/4 - t), 1])

print("== (3.6): Q^2 I vs ln^2(Q^2/m^2) + pi^2/3 ==")
for t in [mp.mpf('1e-2'), mp.mpf('1e-4'), mp.mpf('1e-6'), mp.mpf('1e-8')]:
    v = I_exact(t)
    L = mp.log(1/t)
    print(f"t=m^2/Q^2={mp.nstr(t,3):>8}  Q^2 I = {mp.nstr(v,15):>22}  ln^2+pi^2/3 = {mp.nstr(L**2+mp.pi**2/3,15):>22}  diff/(t ln^2 t) = {mp.nstr((v-L**2-mp.pi**2/3)/(t*L**2),6)}")

# Region closed forms (each times 1/Q^2; mu=Q; e^{eps gamma_E} normalisation dropped, it cancels in the sum)
eps = sp.symbols('epsilon')
L = sp.symbols('L')  # L = ln(m^2/Q^2)
G = sp.gamma
H  = G(1+eps)*G(-eps)**2/G(1-2*eps)                    # (mu^2/Q^2)^eps = 1
C1 = -sp.exp(-eps*L)*G(1+eps)*G(-eps)**2/G(1-2*eps)    # (mu^2/m^2)^eps = e^{-eps L}
S  = -sp.exp(-2*eps*L)*G(1+eps)*G(eps)*G(-eps)          # (mu^2 Q^2/m^4)^eps = e^{-2 eps L}
# doc's quoted hard-region normalisation: Gamma(1+eps)Gamma(1-eps)^2/Gamma(1-2eps) * 1/eps^2
H_doc = G(1+eps)*G(1-eps)**2/G(1-2*eps)/eps**2
print("\n== hard region: doc formula (with Gamma(1-eps)^2) equals Gamma(1+eps)Gamma(-eps)^2/Gamma(1-2eps)? ==")
print(sp.simplify(sp.gammasimp(H - H_doc)))
tot = 0
print("\n== Laurent expansions (mu=Q, L=ln(m^2/Q^2)) ==")
for name, expr in [('H', H), ('C1', C1), ('C2', C1), ('S', S)]:
    ser = sp.series(expr, eps, 0, 1).removeO()
    ser = sp.expand(sp.simplify(ser))
    c2 = sp.simplify(ser.coeff(eps, -2)); c1 = sp.simplify(ser.coeff(eps, -1)); c0 = sp.simplify(ser.coeff(eps, 0))
    print(f"{name:>3}: 1/eps^2: {c2},  1/eps: {c1},  eps^0: {sp.nsimplify(sp.expand(c0))}")
    tot += ser
tot = sp.expand(sp.simplify(tot))
print("sum: 1/eps^2:", sp.simplify(tot.coeff(eps,-2)), " 1/eps:", sp.simplify(tot.coeff(eps,-1)), " eps^0:", sp.simplify(tot.coeff(eps,0)))
print("expected eps^0: L^2 + pi^2/3 ->", sp.simplify(tot.coeff(eps,0) - (L**2 + sp.pi**2/3)) == 0)

# The doc's consistency argument: a=ln(mu^2/Q^2), b=ln(mu^2/m^2); soft log 2b-a; double log (1/2)[a^2-2b^2+(2b-a)^2]=(a-b)^2
a, b = sp.symbols('a b')
print("\n(1/2)[a^2-2b^2+(2b-a)^2] - (a-b)^2 =", sp.expand(sp.Rational(1,2)*(a**2-2*b**2+(2*b-a)**2)-(a-b)**2))
