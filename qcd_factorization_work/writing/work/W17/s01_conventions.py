# W17 / Ch14 -- s01: light-front conventions, regulator vectors, zeta normalization, Fourier sign chain.
# Book conventions: v^\pm=(v^0\pm v^3)/sqrt2, v.w = v^+w^- + v^-w^+ - vT.wT ;  n_A=(1^+,0^-), n_B=(0^+,1^-)
# space-like regulators n_A(y_A)=(1^+,-e^{-2y_A}), n_B(y_B)=(-e^{2y_B},1^-)  (Collins 2011 / Aybat-Rogers convention)
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np
from scipy import integrate, special

ok = True
def check(name, cond):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name)
    ok &= bool(cond)

yA, yB, y, kT, P, M, x, yn, Q = sp.symbols('y_A y_B y k_T P M x y_n Q', real=True)
def dot(a, b):  # a=(plus,minus) only (transverse handled separately)
    return a[0]*b[1] + a[1]*b[0]
nA_y = (sp.Integer(1), -sp.exp(-2*yA))
nB_y = (-sp.exp(2*yB), sp.Integer(1))
nA = (1, 0); nB = (0, 1)
# rapidity of a vector: 1/2 ln|v+/v-|
check('rapidity of n_A(y_A) = y_A', sp.simplify(sp.Rational(1, 2)*sp.log(1/sp.exp(-2*yA)) - yA) == 0)
check('rapidity of n_B(y_B) = y_B', sp.simplify(sp.Rational(1, 2)*sp.log(sp.exp(2*yB)/1) - yB) == 0)
check('n_A(y_A)^2 = -2 e^{-2y_A} <0 (space-like)', sp.simplify(dot(nA_y, nA_y) + 2*sp.exp(-2*yA)) == 0)
check('n_B(y_B)^2 = -2 e^{2y_B} <0 (space-like)', sp.simplify(dot(nB_y, nB_y) + 2*sp.exp(2*yB)) == 0)
check('n_A(y_A).n_B(y_B) = 1 + e^{2(y_B-y_A)}', sp.simplify(dot(nA_y, nB_y) - (1 + sp.exp(2*(yB - yA)))) == 0)
# on-shell gluon k with rapidity y and |kT|
k = (kT*sp.exp(y)/sp.sqrt(2), kT*sp.exp(-y)/sp.sqrt(2))
check('on-shell k: 2k^+k^- = kT^2', sp.simplify(2*k[0]*k[1] - kT**2) == 0)
lhs = dot(nA_y, k)
rhs = -sp.sqrt(2)*kT*sp.exp(-yA)*sp.sinh(y - yA)
check('VF-REF-19: n_A(y_A).k = -sqrt2 |kT| e^{-y_A} sinh(y-y_A)', sp.simplify((lhs - rhs).rewrite(sp.exp)) == 0)
lhsB = dot(nB_y, k)
rhsB = sp.sqrt(2)*kT*sp.exp(yB)*sp.sinh(y - yB)
check('n_B(y_B).k = +sqrt2 |kT| e^{y_B} sinh(y-y_B)', sp.simplify((lhsB - rhsB).rewrite(sp.exp)) == 0)
# zeta normalization: M^2 x^2 e^{2(y_P - y_n)} = 2 (x P^+)^2 e^{-2 y_n} with M^2 = 2 P^+ P^-, y_P = 1/2 ln(P+/P-)
Pp, Pm = sp.symbols('P_p P_m', positive=True)
yP = sp.Rational(1, 2)*sp.log(Pp/Pm)
zA1 = (2*Pp*Pm)*x**2*sp.exp(2*(yP - yn))
zA2 = 2*(x*Pp)**2*sp.exp(-2*yn)
check('zeta_A: M^2x^2 e^{2(yP-yn)} = 2(xP^+)^2 e^{-2yn}', sp.simplify(sp.expand_log(zA1 - zA2, force=True)) == 0)
xA, xB, PAp, PBm = sp.symbols('x_A x_B P_Ap P_Bm', positive=True)
zetaA = 2*(xA*PAp)**2*sp.exp(-2*yn)
zetaB = 2*(xB*PBm)**2*sp.exp(2*yn)
Q2 = 2*(xA*PAp)*(xB*PBm)   # leading power: Q^2 = 2 q^+ q^-, q^+ = xA PA^+, q^- = xB PB^-
check('zeta_A zeta_B = Q^4 (independent of y_n)', sp.simplify(zetaA*zetaB - Q2**2) == 0)
# Aybat-Rogers eq.(3) printed zeta_F = 2 M^2 x^2 e^{2(yP-ys)}: twice ours -> sqrt(zeta_F zeta_D) = 2 Q^2
check('Aybat-Rogers printed form is 2x ours (App Q row 2)', sp.simplify(2*zA1/zA2 - 2) == 0)

# --- Fourier sign chain (VF-CONV-11)
# f(x,kT) = int dw^- d^2 wT/(16 pi^3) e^{-i x P+ w-} e^{+i kT.wT} <...(w)>,  ft(x,b) = int d^2k e^{-ik.b} f(x,k)
# => ft(x,b) = int dw^-/(4pi) e^{-ixP+w-} <...> at wT=b, because int d^2k e^{-ik.b} e^{ik.wT} = (2pi)^2 delta^2(wT-b)
check('1/(16 pi^3) * (2 pi)^2 = 1/(4 pi)', sp.simplify(sp.Rational(1, 16)/sp.pi**3*(2*sp.pi)**2 - 1/(4*sp.pi)) == 0)
# parton momentum: <P|psibar(w)|X><X|psi(0)|P> ~ e^{i(P-pX).w}; with k=P-pX the phase e^{i k.w}
# at w^+=0: k.w = k^+ w^- - kT.wT, so e^{ik.w} = e^{i k+ w-} e^{-i kT.wT}; the w^- integral with e^{-ixP+w-} fixes k+=xP+,
# and the wT integral with e^{+i kT'.wT} fixes kT'=kT: the definition is the density in the parton's kT. (sign chain ok)
print('note: phase e^{ik.w} = e^{ik^+w^-} e^{-ik_T.w_T} at w^+=0  -> f(x,k_T) is the density in the parton k_T')

# DY cross section Fourier form: delta^2(q-kA-kB) = int d^2b/(2pi)^2 e^{i(q-kA-kB).b}
# int d^2kA d^2kB fA fB delta^2(...) = int d^2b/(2pi)^2 e^{iq.b} ftA(b) ftB(b)  -- numerical check with Gaussians
a1, a2 = 0.7, 1.3
fA = lambda k2: np.exp(-k2/a1)/(np.pi*a1)      # normalized 2D Gaussians in k
fB = lambda k2: np.exp(-k2/a2)/(np.pi*a2)
qT = 0.9
# convolution of two Gaussians: Gaussian with width a1+a2
conv = np.exp(-qT**2/(a1 + a2))/(np.pi*(a1 + a2))
# b-space: ftA(b) = exp(-a1 b^2/4), ftB = exp(-a2 b^2/4); int d^2b/(2pi)^2 e^{iq.b} ... = (1/2pi) int b db J0(qb) ...
val = integrate.quad(lambda b: b*special.j0(qT*b)*np.exp(-(a1 + a2)*b*b/4), 0, np.inf)[0]/(2*np.pi)
check('cross-section Fourier form reproduces the kT convolution', abs(val/conv - 1) < 1e-9)

# --- FT[k^i g(k^2)] = 2 i b^i d gt/d(b^2) in the convention ft(b) = int d^2k e^{-ik.b} f(k)
# test with g(k2)=exp(-k2/a): gt(b) = pi a exp(-a b^2/4); claim: FT[k^1 g] = 2 i b^1 d gt/d b^2 = 2 i b1 (-a/4) pi a e^{-a b^2/4}
aa = 0.8
b1, b2 = 0.6, -0.35
def ft_k1g(b1, b2):
    re = integrate.dblquad(lambda k2_, k1_: k1_*np.exp(-(k1_**2 + k2_**2)/aa)*np.cos(-(k1_*b1 + k2_*b2)), -12, 12, -12, 12)[0]
    im = integrate.dblquad(lambda k2_, k1_: k1_*np.exp(-(k1_**2 + k2_**2)/aa)*np.sin(-(k1_*b1 + k2_*b2)), -12, 12, -12, 12)[0]
    return re + 1j*im
lhs_ft = ft_k1g(b1, b2)
bb2 = b1*b1 + b2*b2
rhs_ft = 2j*b1*(-aa/4)*np.pi*aa*np.exp(-aa*bb2/4)
check('FT[k^i g(k^2)] = 2 i b^i dgt/db^2 (e^{-ik.b} convention)', abs(lhs_ft - rhs_ft) < 1e-8)
print('   FT value', lhs_ft, 'expected', rhs_ft)
# consequence: Sivers term in b space is purely imaginary; f(b)^* = f(-b)
# first moment: ft_{1T}^{perp(1)}(x,0) = int d^2k k^2/(2M^2) f_1T^perp  with ft^{(1)} = -(2/M^2) d ft/d b^2
# check with g = exp(-k2/a): -(2/M^2) d/db^2 [pi a e^{-a b^2/4}] at b=0 = (2/M^2) pi a^2/4 ; int d^2k k^2 g/(2M^2) = pi a^2/(2 M^2)
Mm = 1.1
lhs1 = -(2/Mm**2)*(np.pi*aa*(-aa/4))
rhs1 = integrate.quad(lambda kk: 2*np.pi*kk*kk**2*np.exp(-kk*kk/aa), 0, np.inf)[0]/(2*Mm**2)
check('ft^{perp(1)}(b=0) = int d^2k k^2/(2M^2) f', abs(lhs1 - rhs1) < 1e-10)

print('ALL PASS' if ok else 'SOME FAIL')
