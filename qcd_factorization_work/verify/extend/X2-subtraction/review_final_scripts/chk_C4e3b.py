import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 25

def angavg(a, b2, eps):
    return mp.hyp2f1(mp.mpf(1)/2, 1, 2 - eps, b2/a**2)/a

def fib_CH(eps, xB, T=1):
    # split: int_0^T t^{-1-eps}[<h0>-1/A] + int_T^inf t^{-1-eps}<h0> - (1/A) T^{-eps}/eps
    def inner(xi):
        A = 1 - xi/xB
        f1 = lambda t: t**(-1 - eps)*(angavg(A + t/(1 - xi), 4*t, eps) - 1/A)
        f2 = lambda t: t**(-1 - eps)*angavg(A + t/(1 - xi), 4*t, eps)
        I = mp.quad(f1, [0, (1 - xi)*mp.mpf('1e-3'), T]) + mp.quad(f2, [T, 10, 100, mp.inf]) - T**(-eps)/(eps*A)
        return (1 - xi)*I
    return mp.quad(inner, [0, mp.mpf(1)/2, 1])/mp.gamma(2 - eps)

def closed_CH(eps, xB):
    c = 1 - 1/mp.mpf(xB)
    J = ((1 - c**(1 - eps))/(1 - eps) + (c - c**(1 - eps))/eps)/(1 - c)**2
    return mp.gamma(1 + eps)*mp.gamma(-eps)*mp.gamma(2 - eps)/mp.gamma(2 - 2*eps)*J

def fib_THG(eps, xB):
    # fibered T_H Gamma for -1<eps<0: (1/Gamma(2-eps)) int dxi (1-xi) int dt t^{-1-eps} <h0>
    def inner(xi):
        A = 1 - xi/xB
        f = lambda t: t**(-1 - eps)*angavg(A + t/(1 - xi), 4*t, eps)
        return (1 - xi)*mp.quad(f, [0, (1 - xi)*mp.mpf('1e-3'), 1, 10, mp.inf])
    return mp.quad(inner, [0, mp.mpf(1)/2, 1])/mp.gamma(2 - eps)

for eps in ['0.1', '0.2', '0.3']:
    eps = mp.mpf(eps)
    f = fib_CH(eps, 2); c = closed_CH(eps, 2)
    print(f"(e3) eps={eps}: fib {mp.nstr(f, 20)}  closed {mp.nstr(c, 20)}  rel {mp.nstr(abs(f/c - 1), 3)}")
for eps in ['-0.3', '-0.6']:
    eps = mp.mpf(eps)
    f = fib_THG(eps, 2); c = closed_CH(eps, 2)
    print(f"(T_H Gamma, eps<0) eps={eps}: fib {mp.nstr(f, 20)}  closed-form continuation {mp.nstr(c, 20)}  rel {mp.nstr(abs(f/c - 1), 3)}")
# second x value
for eps in ['0.15']:
    eps = mp.mpf(eps)
    f = fib_CH(eps, mp.mpf('1.3')); c = closed_CH(eps, mp.mpf('1.3'))
    print(f"(e3) x=1.3 eps={eps}: fib {mp.nstr(f, 20)}  closed {mp.nstr(c, 20)}  rel {mp.nstr(abs(f/c - 1), 3)}")
