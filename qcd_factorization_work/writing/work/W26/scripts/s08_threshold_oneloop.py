# W26 / Ch23 -- s08: one-loop check of the threshold factorization of the quasi-PDF kernel
# (thm:yzliu-threshold, ex:yzliu-threshold-oneloop; VF-LAM-4, VF-LAM-8, VF-LAM-14; claim N06 re-derived)
# (A) momentum space: singular terms of the MSbar one-loop kernel (VF-LAM-8) near xi -> 1 vs p^z J_f^(1)
# (B) coordinate space: large-|lambda| asymptotics of e^{-i lambda} h(lambda) for a quark target (VF-LAM-4 kernel)
#     must equal 1 + a [H^(1) + J~^(1) + i pi sgn(z)(L_zeta - 1)],  lambda = P.z = -p^z z,
#     L_z = ln(-z^2 mu^2 e^{2gE}/4) = ln(lambda^2 e^{2gE}) - L_zeta,  L_zeta = ln(4 p_z^2/mu^2).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp, mpmath as mp

xi, Lz_, u = sp.symbols('xi L_zeta u', real=True)
# (A)
k_in = (1 + xi**2)/(1 - xi)*(Lz_ + sp.log(xi*(1 - xi))) - xi*(1 + xi)/(1 - xi)          # 0<xi<1 (inside [.]_+)
k_out = (1 + xi**2)/(1 - xi)*sp.log(xi/(xi - 1)) + 1 + sp.Rational(3, 2)/xi                # xi>1 (inside [.]_+)
sing_in = 2/(1 - xi)*(Lz_ + sp.log(1 - xi) - 1)
sing_out = 2*sp.log(xi - 1)/(xi - 1)
r_in = sp.limit(sp.simplify((k_in - sing_in)*(1 - xi)), xi, 1, '-')
r_out = sp.limit(sp.simplify((k_out - sing_out)*(xi - 1)), xi, 1, '+')
print('0<xi<1: (1-xi)*[kernel - 2/(1-xi)(L_zeta+ln(1-xi)-1)] ->', sp.simplify(r_in), ' (remainder is next-to-leading power: O(ln(1-xi)))')
print('xi>1  : (xi-1)*[kernel - 2 ln(xi-1)/(xi-1)]        ->', sp.simplify(r_out))
assert r_in == 0 and r_out == 0
# J_f^(1) singular part: P ln(1-y)^2/|1-y| + (L_zeta-1)(P 1/(1-y) + P 1/|1-y|)
Jin = sp.log((1 - xi)**2)/(1 - xi) + (Lz_ - 1)*(1/(1 - xi) + 1/(1 - xi))
Jout = sp.log((xi - 1)**2)/(xi - 1) + (Lz_ - 1)*(1/(1 - xi) + 1/(xi - 1))
print('J_f^(1) singular part, xi<1 minus kernel singular part:', sp.simplify(sp.expand_log(Jin - sing_in, force=True)))
print('J_f^(1) singular part, xi>1 minus kernel singular part:', sp.simplify(sp.expand_log(Jout - sing_out, force=True)))

# (B) analytic large-lambda limit (derived in the text):
#  int_0^1 du (e^{-iu lam}-1)/u -> -l ,  int_0^1 du ln u/u (e^{-iu lam}-1) -> l^2/2 + pi^2/12 ,  l = ln(i lam) + gE
X, s, Lzc = sp.symbols('X s L_z', real=True)   # X = ln(lambda^2 e^{2gE}) = L_z + L_zeta ; s = sgn(lambda)
l = X/2 + sp.I*sp.pi*s/2
asym = (sp.Rational(3, 2)*Lzc + sp.Rational(3, 2)) + (-Lzc - 1)*(-2*l + sp.Rational(3, 2)) - 4*(l**2/2 + sp.pi**2/12)
asym = sp.expand(asym.subs(X, Lzc + Lz_))
H1 = -2 + sp.pi**2/12 - Lz_**2/2 + Lz_
J1 = Lzc**2/2 + Lzc + sp.pi**2/12 + 2
target = H1 + J1 + sp.I*sp.pi*(-s)*(Lz_ - 1)       # sgn(z) = -sgn(lambda)
print('analytic: e^{-i lam} h - 1 - a[H + J~ + i pi sgn(z)(L_zeta-1)] =', sp.simplify(sp.expand(asym.subs(s, 1) - target.subs(s, 1))),
      ',', sp.simplify(sp.expand(asym.subs(s, -1) - target.subs(s, -1))))
s = sp.Symbol('s')

# exact closed forms (c = i lambda, l = ln c + gE):
#   I1 = int_0^1 (e^{-cu}-1)/u du = -(E1(c) + ln c + gE)
#   I2 = int_0^1 ln u/u (e^{-cu}-1) du = l^2/2 + pi^2/12 + ln c E1(c) - e^{-c} int_0^oo ln(c+r)/(c+r) e^{-r} dr
#   P0 = int_0^1 e^{-cu} du = (1-e^{-c})/c ,  P1 = int_0^1 u e^{-cu} du = (1 - e^{-c}(1+c))/c^2
mp.mp.dps = 30
gE = mp.euler
def I1(c): return -(mp.e1(c) + mp.log(c) + gE)
def I2(c):
    l = mp.log(c) + gE
    tail = mp.e**(-c)*mp.quad(lambda r: mp.log(c + r)/(c + r)*mp.e**(-r), [0, 1, 10, mp.inf])
    return l**2/2 + mp.pi**2/12 + mp.log(c)*mp.e1(c) - tail
def P0(c): return (1 - mp.e**(-c))/c
def P1(c): return (1 - mp.e**(-c)*(1 + c))/c**2
# cross-check of the closed forms against direct quadrature at moderate lambda
lam = mp.mpf(37); c = 1j*lam
n = 400; pts = [mp.mpf(k)/n for k in range(n + 1)]
d1 = mp.quad(lambda t: (mp.e**(-c*t) - 1)/t, pts); d2 = mp.quad(lambda t: mp.log(t)/t*(mp.e**(-c*t) - 1), pts)
print('closed forms vs quadrature (lambda=37): |dI1| = %.1e, |dI2| = %.1e' % (abs(d1 - I1(c)), abs(d2 - I2(c))))
Lzeta = mp.mpf('0.7')
for lamv in [100, -100, 1000, -1000, 10**4, -10**4, 10**5, -10**5]:
    lam = mp.mpf(lamv); c = 1j*lam
    Lzv = mp.log(lam**2*mp.e**(2*gE)) - Lzeta
    # int_0^1 du (1+(1-u)^2)/u (e^{-cu}-1) = 2 I1 + int_0^1 (-2+u)(e^{-cu}-1) du
    B = 2*I1(c) + (-2*P0(c) + P1(c) - (-2 + mp.mpf(1)/2))
    val = (mp.mpf(3)/2*Lzv + mp.mpf(3)/2) + (-Lzv - 1)*B - 4*I2(c) + 2*P1(c)
    H1v = -2 + mp.pi**2/12 - Lzeta**2/2 + Lzeta
    J1v = Lzv**2/2 + Lzv + mp.pi**2/12 + 2
    pred = H1v + J1v + 1j*mp.pi*(-mp.sign(lam))*(Lzeta - 1)
    print('lambda=%8s: [e^{-i lam} h - 1]/a = %-34s prediction %-34s |diff| = %.2e  (|diff|*|lam|/ln^2|lam| = %.2f)'
          % (lamv, mp.nstr(val, 12), mp.nstr(pred, 12), abs(val - pred), abs(val - pred)*abs(lam)/mp.log(abs(lam))**2))
# summed one-loop anomalous dimension: d/dln mu of [H + J~ + i pi sgn(z)(L_zeta-1)] (alpha fixed) = 0
mu = sp.Symbol('lnmu')
Lzeta_mu = sp.Symbol('c1') - 2*mu; Lz_mu = sp.Symbol('c2') + 2*mu
tot = (-2 + sp.pi**2/12 - Lzeta_mu**2/2 + Lzeta_mu) + (Lz_mu**2/2 + Lz_mu + sp.pi**2/12 + 2) + sp.I*sp.pi*sp.Symbol('sz')*(Lzeta_mu - 1)
d = sp.expand(sp.diff(tot, mu))
print('d/dln mu [H+J~+i pi sgn z (L_zeta-1)] in units of a =', sp.simplify(d.subs({sp.Symbol('c1'): sp.Symbol('Lzeta0'), sp.Symbol('c2'): sp.Symbol('Lz0')})),
      ' -> 2(L_z+L_zeta) - 2 i pi sgn(z) = 2[ln(lambda^2 e^{2gE}) - i pi sgn z] : mu-independent at fixed alpha')
print('PASS (inspect numbers above)')
