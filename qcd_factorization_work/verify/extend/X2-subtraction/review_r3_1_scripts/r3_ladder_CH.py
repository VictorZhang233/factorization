"""Review r3_1 -- independent derivation of the covariant (whole-integrand Feynman-parameter) value of the one-rung
ladder's C_H in (M2), d = 6 - 2 eps, Q = 1, x_B = 2, measure int d^dk/(i pi^{d/2}) (Prop 5.1'(e)).

C_H = S(k)^2 Rhat(k) (H0 - Hhat),  S = 1/(-k^2), Rhat = 1/(-(phat-k)^2), H0 = 1/(-(k+q)^2), Hhat = 1/(Q^2 - 2 n.k),
phat = (p+,0,0_T), n = (0,q-,0_T), q = (0,q-,q_T), q_T^2 = Q^2, 2 p+ q- = Q^2/x_B.
H0 - Hhat = (k^2 + 2 k.q_perp) H0 Hhat   ->   C_H = N / (A1^2 A2 A3 A4),  N = k^2 + 2 k.q_perp,
A1 = -k^2, A2 = -k^2 + 2 phat.k, A3 = -k^2 - 2 k.q + Q^2, A4 = Q^2 - 2 n.k (linear).
Feynman/Cheng-Wu: 1/(A1^2 A2 A3 A4) = 24 int_simplex(x1,x2,x3) x1 int_0^oo dlam [x1 A1 + x2 A2 + x3 A3 + lam A4]^-5.
Shift k = l + b, b = x2 phat - x3 q - lam n:  b^2 = -Q^2 [x3^2 + x2 x3/x_B + x2 lam/x_B],
Delta = Q^2 [ x3 (x1 + x2 c_x) + lam (1 - x2/x_B) ]  (= a + b' lam, times Q^2),
even part of N = l^2 + Delta + (x3 - lam) Q^2.
l-integral (d/2 = 3 - eps):  24 int (l^2 + C)/(-l^2+Delta)^5 = Gamma(1+eps)(2eps-2) Delta^{-1-eps} + Gamma(2+eps) (x3-lam) Q^2 Delta^{-2-eps}.
lam-integrals: int Delta^{-1-eps} = Q^{-2-2eps} a^{-eps}/(eps b'),
               int (x3-lam) Delta^{-2-eps} = Q^{-4-2eps} [ x3 a^{-1-eps}/((1+eps) b') - a^{-eps}/(eps (1+eps) b'^2) ].
=> C_H^cov = Gamma(1+eps) Q^{-2-2eps} int_simplex x1 [ (2eps-2) a^{-eps}/(eps b') + x3 a^{-1-eps}/b' - a^{-eps}/(eps b'^2) ],
   a = x3 (x1 + x2 c_x), b' = 1 - x2/x_B.
The report's form: -Gamma(eps) Q^{-2-2eps} int_simplex a^{-eps}/b' + 2 Gamma(1+eps) Q^{-2-2eps} int_simplex x1 x3 a^{-1-eps}/b'.
Both are compared with the report's fibered values (-6.58496209517625, -3.57272130934841, -2.60783786095414).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 20
xB = mp.mpf(2); cx = 1 - 1/xB

def simplex(f):
    # x2 in (0,1); x3 = (1-x2) s; x1 = (1-x2)(1-s); Jacobian (1-x2)
    return mp.quad(lambda x2: mp.quad(lambda s: (1 - x2)*f((1 - x2)*(1 - s), x2, (1 - x2)*s), [0, mp.mpf(1)/2, 1]),
                   [0, mp.mpf(1)/2, 1])

def mine(e):
    def f(x1, x2, x3):
        a = x3*(x1 + x2*cx); bp = 1 - x2/xB
        return x1*((2*e - 2)*a**(-e)/(e*bp) + x3*a**(-1 - e)/bp - a**(-e)/(e*bp**2))
    return mp.gamma(1 + e)*simplex(f)

def report(e):
    f1 = lambda x1, x2, x3: (x3*(x1 + x2*cx))**(-e)/(1 - x2/xB)
    f2 = lambda x1, x2, x3: x1*x3**(-e)*(x1 + x2*cx)**(-1 - e)/(1 - x2/xB)
    return -mp.gamma(e)*simplex(f1) + 2*mp.gamma(1 + e)*simplex(f2)

fib = {'0.1': mp.mpf('-6.58496209517625'), '0.2': mp.mpf('-3.57272130934841'), '0.3': mp.mpf('-2.60783786095414')}
for es, fv in fib.items():
    e = mp.mpf(es)
    a, b = mine(e), report(e)
    print(f"eps={es}: mine {mp.nstr(a, 14)}   report-formula {mp.nstr(b, 14)}   report fibered {mp.nstr(fv, 14)}   "
          f"|mine/fib-1| = {mp.nstr(abs(a/fv - 1), 3)}", flush=True)
