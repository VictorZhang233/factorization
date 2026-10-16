import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

# ---------- (1) residues derived from scratch (general P, P', m2) ----------
x, km, kap, P, Pp, m2 = sp.symbols('x km kappa P Pp m2', real=True)
Dg = -2*x*km + kap
D1 = 2*(P - x)*(m2/(2*P) + km) + kap
D2 = 2*(m2/(2*Pp) + x)*(Pp - km) + kap
F = 1/(Dg*D1*D2)
# 0<x<P : only D1 pole in the upper half plane -> rho = (1/(i pi)) * 2 pi i * Res = 2*Res
pole1 = sp.solve(sp.Eq(D1, 0), km)[0]
res1 = sp.simplify(sp.limit((km - pole1)*F, km, pole1))
rho_main = sp.simplify(2*res1)
# sliver -a/2<x<0 : only D2 pole in the lower half plane -> rho = (1/(i pi)) * (-2 pi i) Res = -2*Res
pole2 = sp.solve(sp.Eq(D2, 0), km)[0]
res2 = sp.simplify(sp.limit((km - pole2)*F, km, pole2))
rho_sl = sp.simplify(-2*res2)
print("rho_main =", rho_main)
print("rho_sl   =", rho_sl)

# compare with the report's Prop B.1 forms
u = x/P; e2 = m2 + 2*Pp*x; Qt2 = 2*P*Pp
A = x*m2*(1 - u) + P*kap
D2hat = e2*(1 + m2/Qt2 + kap/(Qt2*(1 - u))) + kap
print("main = 1/(A D2hat)?", sp.simplify(rho_main - 1/(A*D2hat)) == 0)
a = m2/Pp; w = 2*x + a
print("sliver = 2/(w Dg D1) at km = P'+kap/w ?",
      sp.simplify(rho_sl - (2/(w*Dg*D1)).subs(km, Pp + kap/w)) == 0)

# ---------- (2) high-precision quadratures at (P,P',m2,eps) ----------
mp.mp.dps = 30
def check(Pv, Ppv, m2v, epsv):
    Pv, Ppv, m2v, epsv = map(mp.mpf, (Pv, Ppv, m2v, epsv))
    fm = sp.lambdify((x, kap, P, Pp, m2), rho_main, 'mpmath')
    fs = sp.lambdify((x, kap, P, Pp, m2), rho_sl, 'mpmath')
    norm = 1/mp.gamma(1 - epsv)
    def inner_main(xx):
        return mp.quad(lambda k: k**(-epsv)*fm(xx, k, Pv, Ppv, m2v), [0, m2v, 1, mp.inf])
    fib_main = norm*mp.quad(inner_main, [0, m2v/10, m2v, Pv/2, Pv])
    av = m2v/Ppv
    def inner_sl(xx):
        return mp.quad(lambda k: k**(-epsv)*fs(xx, k, Pv, Ppv, m2v), [0, m2v, 1, mp.inf])
    fib_sl = norm*mp.quad(inner_sl, [-av/2, -av/4, 0])
    # covariant, own parametrization: x2 outer, x1 inner
    Qt2v = 2*Pv*Ppv; Q2v = (Qt2v + m2v)**2/Qt2v; tau = m2v/Qt2v
    Fp = lambda x1, x2: (1 - x1 - x2)*m2v*(x1 + x2) + x1*x2*Q2v
    g = mp.gamma(1 + epsv)
    def cov_main_in(x2):
        lo = tau*x2; hi = 1 - x2
        return mp.quad(lambda x1: Fp(x1, x2)**(-1 - epsv), [lo, lo + (hi - lo)*mp.mpf('1e-3'), (lo+hi)/2, hi])
    cov_main = g*mp.quad(cov_main_in, [0, mp.mpf('1e-4'), mp.mpf('1e-2'), 1/(1 + tau)])
    def cov_sl_in(x2):
        hi = min(tau*x2, 1 - x2)
        return mp.quad(lambda x1: Fp(x1, x2)**(-1 - epsv), [0, hi/2, hi])
    cov_sl = g*mp.quad(cov_sl_in, [0, mp.mpf('1e-4'), mp.mpf('1e-2'), 1/(1 + tau), 1])
    # full covariant (third independent route: polar coordinates around soft corner not needed; whole simplex)
    print(f"(P,P',m2,eps)=({Pv},{Ppv},{m2v},{epsv})")
    print("   main : fib", mp.nstr(fib_main, 20), " cov", mp.nstr(cov_main, 20), " rel", mp.nstr(abs(fib_main/cov_main - 1), 3))
    print("   sliv : fib", mp.nstr(fib_sl, 20), " cov", mp.nstr(cov_sl, 20), " rel", mp.nstr(abs(fib_sl/cov_sl - 1), 3))
    print("   total: fib", mp.nstr(fib_main + fib_sl, 20), " cov", mp.nstr(cov_main + cov_sl, 20))

check('0.8', '1.3', '0.1', '0.3')
check('0.5', '0.9', '0.02', '-0.4')
