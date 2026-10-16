# Final review (2026-10-11): (e1) check only. The (e2) t-integral is an exact Beta integral; the (e3) check with the
# large-t tail treated analytically is chk_C4e3b.py (a naive quadrature of the t^(-1-eps) tail is inaccurate at small eps).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 25

def angavg(a, b2, eps):
    # <1/(a + b cos th)> over S^{3-2eps} (D = 4-2eps transverse dims), b2 = b^2
    return mp.hyp2f1(mp.mpf(1)/2, 1, 2 - eps, b2/a**2)/a

def fib_Gamma(m2, eps, xB):
    # (1/Gamma(2-eps)) int dxi/(1-xi) int dt t^{1-eps} <1/(A+v+2k.q)>/v^2,  v = xi m2 + t/(1-xi), |q| = 1, Q = 1
    def inner(xi):
        A = 1 - xi/xB
        f = lambda t: t**(1 - eps)*angavg(A + xi*m2 + t/(1 - xi), 4*t, eps)/(xi*m2 + t/(1 - xi))**2
        return mp.quad(f, [0, xi*(1 - xi)*m2, 1, mp.inf])/(1 - xi)
    return mp.quad(inner, [0, mp.mpf('1e-3'), mp.mpf(1)/2, 1])/mp.gamma(2 - eps)

def cov_Gamma(m2, eps, xB):
    # Gamma(1+eps) int_simplex x1 [x2(x1+x3) m2 + x3(x1 + x2 c)]^{-1-eps}, own (x2, x1) nesting
    c = 1 - 1/mp.mpf(xB)
    def inner(x2):
        f = lambda x1: x1*(x2*(1 - x2)*m2 + (1 - x1 - x2)*(x1 + x2*c))**(-1 - eps)
        return mp.quad(f, [0, (1 - x2)/2, 1 - x2])
    return mp.gamma(1 + eps)*mp.quad(inner, [0, mp.mpf('1e-3'), mp.mpf(1)/2, 1])

def fib_CR1(m2, eps, xB):
    # C_R1: hard factor 1/A -> (1/Gamma(2-eps)) int dxi/(1-xi) (1/A) int dt t^{1-eps}/v^2  (numerical)
    def inner(xi):
        A = 1 - xi/xB
        f = lambda t: t**(1 - eps)/(xi*m2 + t/(1 - xi))**2
        return mp.quad(f, [0, xi*(1 - xi)*m2, 1, mp.inf])/((1 - xi)*A)
    return mp.quad(inner, [0, mp.mpf('1e-3'), mp.mpf(1)/2, 1])/mp.gamma(2 - eps)

def closed_CR1(m2, eps, xB):
    return mp.gamma(eps)*mp.quad(lambda xi: (1 - xi)**(1 - eps)*(xi*m2)**(-eps)/(1 - xi/xB), [0, 1])

def fib_CH(eps, xB):
    # (1/Gamma(2-eps)) int dxi (1-xi) int dt t^{-1-eps} [<h0> - 1/A],  v0 = t/(1-xi)
    def inner(xi):
        A = 1 - xi/xB
        def f(t):
            a = A + t/(1 - xi)
            return t**(-1 - eps)*(angavg(a, 4*t, eps) - 1/A)
        return (1 - xi)*mp.quad(f, [0, (1 - xi)*mp.mpf('1e-3'), (1 - xi), 10, mp.inf])
    return mp.quad(inner, [0, mp.mpf(1)/2, 1])/mp.gamma(2 - eps)

def closed_CH(eps, xB):
    c = 1 - 1/mp.mpf(xB)
    J = ((1 - c**(1 - eps))/(1 - eps) + (c - c**(1 - eps))/eps)/(1 - c)**2
    J2 = mp.quad(lambda y: y*(y + (1 - y)*c)**(-1 - eps), [0, 1])
    return mp.gamma(1 + eps)*mp.gamma(-eps)*mp.gamma(2 - eps)/mp.gamma(2 - 2*eps)*J, J/J2 - 1

for (m2, eps) in [('0.01', '0.1'), ('0.05', '0.25')]:
    m2 = mp.mpf(m2); eps = mp.mpf(eps)
    f = fib_Gamma(m2, eps, 2); c = cov_Gamma(m2, eps, 2)
    print(f"(e1) m2={m2} eps={eps}: fib {mp.nstr(f, 18)}  cov {mp.nstr(c, 18)}  rel {mp.nstr(abs(f/c - 1), 3)}")
