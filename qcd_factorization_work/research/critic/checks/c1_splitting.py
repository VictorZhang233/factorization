# Check LO splitting functions: Mellin moments, closed forms, number & momentum sum rules.
import sys,os; sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
z=sp.symbols('z',positive=True)
CF,CA,TR=sp.Rational(4,3),sp.Integer(3),sp.Rational(1,2)
nf=sp.symbols('n_f')
def S1(n): return sp.harmonic(n)
def plus_whole(g,n):   # <[g(z)/(1-z)]_+ , z^{n-1}> = int g(z)(z^{n-1}-1)/(1-z)
    return sp.integrate(sp.cancel(g*(z**(n-1)-1)/(1-z)),(z,0,1))
def g_times_plus(g,n): # <g(z) [1/(1-z)]_+ , z^{n-1}> = int (g z^{n-1} - g(1))/(1-z)
    return sp.integrate(sp.cancel((g*z**(n-1)-g.subs(z,1))/(1-z)),(z,0,1))
def reg(r,n): return sp.integrate(r*z**(n-1),(z,0,1))
for n in range(1,7):
    gqq = CF*plus_whole(1+z**2,n)
    gqq_alt = CF*(g_times_plus(1+z**2,n)+sp.Rational(3,2))   # (1+z^2)/(1-z)_+ + 3/2 delta
    closed = CF*(sp.Rational(3,2)+sp.Rational(1,n*(n+1))-2*S1(n))
    gqg = TR*reg(z**2+(1-z)**2,n)
    ggq = CF*reg((1+(1-z)**2)/z,n) if n>1 else None
    ggg = 2*CA*(g_times_plus(z,n)+reg((1-z)/z+z*(1-z),n)) + (11*CA-4*nf*TR)/6 if n>1 else None
    print(f"n={n}: gamma_qq={sp.nsimplify(gqq)}  alt={sp.nsimplify(gqq_alt)}  closed={closed}  ok={sp.simplify(gqq-closed)==0 and sp.simplify(gqq-gqq_alt)==0}")
    if n==2:
        print("   momentum sum rule (quark column) gamma_qq+gamma_gq =",sp.simplify(gqq+ggq))
        print("   momentum sum rule (gluon column) 2 n_f gamma_qg+gamma_gg =",sp.simplify(2*nf*gqg+ggg))
