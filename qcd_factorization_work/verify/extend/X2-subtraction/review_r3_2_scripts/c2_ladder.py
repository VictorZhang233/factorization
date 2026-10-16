# Reviewer r3_2: one-rung DIS ladder (M2) checks: c1(x), the exact odd-part integral, C_R1 closed form, C_H parametric value.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 25
# c1(x) = 4 int_0^1 xi^(1/2) (1-xi)^(3/2) / (1-xi/x)^2
c1 = lambda x: 4*mp.quad(lambda z: mp.sqrt(z)*(1-z)**1.5/(1-z/x)**2, [0, 1])
for x in [2, 1.3, 5]:
    print(f"c1({x}) = {mp.nstr(c1(mp.mpf(x)), 10)}")
# odd-part exact integral: int_0^inf t^(3/2)(t^-2-(t+1)^-2) dt = 3 pi/2 ; <|cos|>_S3 = 4/(3 pi)
I = mp.quad(lambda t: t**1.5*(t**-2 - (t+1)**-2), [0, 1, mp.inf])
print("int t^(3/2)(t^-2-(t+1)^-2) =", mp.nstr(I, 15), " 3pi/2 =", mp.nstr(3*mp.pi/2, 15))
avg = mp.quad(lambda c: c*mp.sqrt(1-c**2), [0, 1])/mp.quad(lambda c: mp.sqrt(1-c**2), [0, 1])
print("<|cos theta|>_S3 =", mp.nstr(avg, 15), " 4/(3pi) =", mp.nstr(4/(3*mp.pi), 15))
# C_R1 closed form (reviewer re-derived it by Feynman parameters): Gamma(eps) int (1-xi)^(1-eps) (xi m2)^(-eps)/(Q2 (1-xi/x))
def CR1(m2, eps, x, Q2=1):
    return mp.gamma(eps)*mp.quad(lambda z: (1-z)**(1-eps)*(z*m2)**(-eps)/(Q2*(1-z/x)), [0, 1])
for x in [2, 1.5, 3]:
    print(f"x={x}: C_R1(m2=0.01,eps=0.1) = {mp.nstr(CR1(mp.mpf('0.01'), mp.mpf('0.1'), mp.mpf(x)), 16)},  C_R1(m2=0.001,eps=0.3) = {mp.nstr(CR1(mp.mpf('0.001'), mp.mpf('0.3'), mp.mpf(x)), 16)}")
# C_H parametric formula of the report (Q=1):
def CH(eps, x):
    cx = 1 - 1/mp.mpf(x)
    f1 = lambda x1, x2: (((1-x1-x2)*(x1 + x2*cx))**(-eps))/(1 - x2/x)
    f2 = lambda x1, x2: x1*(1-x1-x2)**(-eps)*(x1 + x2*cx)**(-1-eps)/(1 - x2/x)
    I1 = mp.quad(lambda a: mp.quad(lambda b: f1(a, b), [0, 1-a]), [0, 1])
    I2 = mp.quad(lambda a: mp.quad(lambda b: f2(a, b), [0, 1-a]), [0, 1])
    return -mp.gamma(eps)*I1 + 2*mp.gamma(1+eps)*I2
for e in ['0.1', '0.2', '0.3']:
    print(f"C_H(eps={e}, x=2) [report's parametric formula] = {mp.nstr(CH(mp.mpf(e), 2), 15)}")
