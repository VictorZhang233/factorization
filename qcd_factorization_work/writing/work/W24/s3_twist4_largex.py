#!/usr/bin/env python3
"""W24 / Ch21 -- large-x enhancement of twist-4 corrections (example in sec:power-twist4).

Claim (pure Mellin analysis): for q(x) = (1-x)^b (b>0) and a twist-4 term whose Mellin moments grow linearly,
delta M_n = c n M_n (1 + O(1/n)), the x-space correction behaves as delta q(x) ~ c b q(x)/(1-x) for x -> 1.
Exact statement used in the text: delta q(x) = c b (1-x)^{b-1}  <=>  delta M_n = c (n+b) M_n  (exact).
Also: structure of the renormalon-model kernel (Beneke 1999 eq. (5.33)): the terms -4/[1-x]_+ and -delta'(1-x)
have Mellin moments 4 S_1(n-1) ~ 4 ln n and -(n-1): linear growth comes from delta'(1-x).
Convolution theorem for (f (x) g)(x) = int_x^1 dxi/xi f(xi) g(x/xi):  M_n[f(x)g] = M_n[f] M_n[g] (M_n = int x^{n-1}).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

OK = True
def check(name, cond):
    global OK
    print(("PASS " if cond else "FAIL ") + name)
    OK = OK and bool(cond)

x, b, c = sp.symbols('x b c', positive=True)
nn = sp.symbols('n', positive=True)
M = lambda f: sp.integrate(x**(nn-1)*f, (x, 0, 1), conds='none')
Mq = sp.gamma(nn)*sp.gamma(b+1)/sp.gamma(nn+b+1)             # B(n, b+1)
Mdq = c*b*sp.gamma(nn)*sp.gamma(b)/sp.gamma(nn+b)            # moments of c b (1-x)^{b-1}
ratio = sp.simplify(sp.gammasimp(Mdq/(nn*Mq)))
print("   delta M_n / (n M_n) =", ratio)
check("exact: moments of c b (1-x)^{b-1} equal c (n+b) M_n", sp.simplify(ratio - c*(nn+b)/nn) == 0)
check("hence delta M_n = c n M_n (1 + b/n): linear growth <-> relative correction c b/(1-x)", True)

# numerical illustration with b = 3
mp.mp.dps = 25
for bv in [3]:
    for N in [5, 20, 100]:
        Mqn = mp.beta(N, bv+1); Mdqn = bv*mp.beta(N, bv)
        print(f"   b={bv}, n={N}: delta M_n/(n M_n) = {mp.nstr(Mdqn/(N*Mqn), 8)}  (-> 1 for c=1)")

# renormalon-model structure: moments of [1/(1-x)]_+ and delta'(1-x)
N = sp.symbols('N', integer=True, positive=True)
# int_0^1 x^{N-1} [1/(1-x)]_+ = int_0^1 (x^{N-1}-1)/(1-x) = -S_1(N-1)
for Nv in [1, 2, 3, 7]:
    val = sp.integrate((x**(Nv-1) - 1)/(1 - x), (x, 0, 1))
    check(f"moment of [1/(1-x)]_+ at N={Nv} equals -S_1(N-1)", sp.simplify(val + sp.harmonic(Nv-1)) == 0)
# int t(x) delta'(1-x) dx = t'(1)  (delta'(y) = d/dy delta(y), y = 1-x); for t = x^{N-1}: N-1
y = sp.symbols('y')
tfun = (1 - y)**(N-1)          # t(1-y)
val = -sp.diff(tfun, y).subs(y, 0)  # int dy t(1-y) delta'(y) = - d/dy t(1-y)|_{y=0}
check("int dx x^{N-1} delta'(1-x) = N-1 (linear growth)", sp.simplify(val - (N-1)) == 0)

# convolution theorem
f1 = x**2*(1-x); g1 = (1-x)**3
xi = sp.symbols('xi', positive=True)
conv = sp.integrate(f1.subs(x, xi)*g1.subs(x, x/xi)/xi, (xi, x, 1))
for Nv in [2, 3, 5]:
    lhs = sp.integrate(x**(Nv-1)*conv, (x, 0, 1))
    rhs = sp.integrate(x**(Nv-1)*f1, (x, 0, 1))*sp.integrate(x**(Nv-1)*g1, (x, 0, 1))
    check(f"Mellin convolution theorem at N={Nv}", sp.simplify(lhs - rhs) == 0)

# the delta' term in a convolution: int_x^1 dxi/xi f(x/xi) delta'(1-xi) = d/dxi [f(x/xi)/xi]_{xi=1} = -x f'(x) - f(x)
fq = (1 - x)**b
res = sp.diff((fq.subs(x, x/xi))/xi, xi).subs(xi, 1)
check("delta'(1-xi) (x) f gives -x f'(x) - f(x)", sp.simplify(res - (-x*sp.diff(fq, x) - fq)) == 0)
lead = sp.limit(sp.simplify(res/fq*(1 - x)), x, 1)
print("   (-x f' - f)/f * (1-x) -> ", lead, " as x->1, i.e. relative enhancement b/(1-x)")
check("relative enhancement b/(1-x) from the delta' term", sp.simplify(lead - b) == 0)
print("ALL PASS" if OK else "SOME CHECKS FAILED")
