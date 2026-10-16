"""X2 / T2: one-loop off-shell triangle -- remainder density rho_r = rho_Gamma - sum_R rho_{C_R}
 (a) simplified closed forms on the three x-ranges (sympy, exact),
 (b) integral norm  N(lambda) = int dx dkap |rho_r|  at eps=0, and the signed integral (must equal I - (D.32)),
 (c) the (H1)/(H2) items on the 2x2 partition  U_S={x<=s, y<=s}, U_C1={x>s, y<=s}, U_C2={x<=s, y>s}, U_H={x>s,y>s},
     y = kap/(2x) (on-shell minus momentum of the gluon), s = lambda (=m/Qt), Qt^2 = 2PP'.
     For x<0 (sliver -m2/(2P')<x<0) we use |x|,|y|.
Units: P = P' = 1/sqrt(2)  (Qt = 1) by default; also an asymmetric point.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

x, kap, m2, P, Pp = sp.symbols('x kap m2 P Pp', positive=True)
A = x*m2*(1 - x/P) + P*kap
B = x*m2 + P*kap
e2 = m2 + 2*Pp*x; h2 = 2*Pp*x
a2 = m2/Pp
# Gamma, mid range: rho = 1/((P-x) Dg D2) at k1m
km = sp.symbols('km')
k2 = 2*x*km - kap
Dg = -k2
D1 = m2 + 2*P*km - (m2/P)*x - k2
D2 = m2 + 2*Pp*x - (m2/Pp)*km - k2
h1 = 2*P*km
k1m = -(m2*(1 - x/P) + kap)/(2*(P - x))
k2m = (m2 + 2*Pp*x + kap)/(a2 + 2*x)
rhoG_mid = sp.together(1/((P - x)*Dg*D2)).subs(km, k1m)
rhoG_neg = sp.together(2/((a2 + 2*x)*Dg*D1)).subs(km, k2m)
rhoS = 1/(B*e2)
rhoC1_mid = x*m2/(2*P*Pp*A*B); rhoC1_big = -1/(2*Pp*x*B)
rhoC2_pos = -(1/P)/((e2 + kap)*e2)
rhoC2_neg = sp.together(2/((a2 + 2*x)*Dg*h1)).subs(km, k2m)
rhoH_mid = -x/(P*(h2 + kap)*(h2*(P - x) + P*kap)); rhoH_big = 1/(P*(h2 + kap)*h2)

r_mid = sp.factor(sp.together(rhoG_mid - rhoS - rhoC1_mid - rhoC2_pos - rhoH_mid))
r_big = sp.factor(sp.together(-rhoS - rhoC1_big - rhoC2_pos - rhoH_big))
r_neg = sp.factor(sp.together(rhoG_neg - rhoC2_neg))
print("rho_r (0<x<P)  =", r_mid)
print()
print("rho_r (x>P)    =", r_big)
print()
print("rho_r (-m2/(2P')<x<0) =", r_neg)
print()
# leading behaviour of r_big at large kap (must be O(kap^-2) for d=4 integrability)
lead_big = sp.limit(r_big*kap**2, kap, sp.oo)
print("lim kap^2 rho_r(x>P) =", sp.simplify(lead_big))
lead_mid = sp.limit(r_mid*kap**2, kap, sp.oo)
print("lim kap^2 rho_r(0<x<P) =", sp.simplify(lead_mid))

f_mid = sp.lambdify((x, kap, m2, P, Pp), r_mid, 'mpmath')
f_big = sp.lambdify((x, kap, m2, P, Pp), r_big, 'mpmath')
f_neg = sp.lambdify((x, kap, m2, P, Pp), r_neg, 'mpmath')
fG_mid = sp.lambdify((x, kap, m2, P, Pp), rhoG_mid, 'mpmath')
fG_neg = sp.lambdify((x, kap, m2, P, Pp), rhoG_neg, 'mpmath')

mp.mp.dps = 40

def UD(t):
    lam = mp.sqrt(1 - 4*t); rho = 2/(1 - 2*t + lam)
    return (4*mp.polylog(2, -rho*t) + mp.log(rho*t)**2 + mp.pi**2/3)/lam

def integrate(fun_xk, xlo, xhi, xbreaks, kbreaks_of_x):
    """int_{xlo}^{xhi} dx int dkap fun, using log variables where useful"""
    def inner(xv):
        kb = kbreaks_of_x(xv)
        return mp.quad(lambda kv: fun_xk(xv, kv), kb)
    pts = [xlo] + [b for b in xbreaks if xlo < b < xhi] + [xhi]
    return mp.quad(inner, pts)

def norms(m2v, Pv, Ppv):
    Qt2 = 2*Pv*Ppv
    lam = mp.sqrt(m2v/Qt2)
    kb = lambda xv: [0, m2v**2, m2v*abs(xv), m2v, abs(xv), 1, 10, mp.inf]
    xb = [m2v**2, m2v, mp.sqrt(m2v), Pv/2, Pv, 2*Pv, 10*Pv]
    # signed and absolute integrals
    S_mid = integrate(lambda a, b: f_mid(a, b, m2v, Pv, Ppv), 0, Pv, xb, kb)
    N_mid = integrate(lambda a, b: abs(f_mid(a, b, m2v, Pv, Ppv)), 0, Pv, xb, kb)
    S_big = integrate(lambda a, b: f_big(a, b, m2v, Pv, Ppv), Pv, mp.inf, xb, kb)
    N_big = integrate(lambda a, b: abs(f_big(a, b, m2v, Pv, Ppv)), Pv, mp.inf, xb, kb)
    xn = -m2v/(2*Ppv)
    S_neg = integrate(lambda a, b: f_neg(a, b, m2v, Pv, Ppv), xn, 0, [xn/2], kb)
    N_neg = integrate(lambda a, b: abs(f_neg(a, b, m2v, Pv, Ppv)), xn, 0, [xn/2], kb)
    Q2 = (Qt2 + m2v)**2/Qt2
    exact = UD(m2v/Q2)/Q2 - (mp.log(Qt2/m2v)**2 + mp.pi**2/3)/Qt2
    return S_mid + S_big + S_neg, N_mid + N_big + N_neg, exact, (S_mid, S_big, S_neg), (N_mid, N_big, N_neg)

print("\n(b) signed integral vs exact remainder, and integral norm (eps=0):")
print(" Qt=1 (P=P'=1/sqrt2) unless stated;  lam^2 = m2/Qt^2")
rows = []
for (Pv, Ppv) in [(1/mp.sqrt(2), 1/mp.sqrt(2)), (mp.mpf('0.8'), mp.mpf('1.3'))]:
    for k in [2, 3, 4, 5, 6, 8, 10]:
        m2v = mp.mpf(10)**(-k)*2*Pv*Ppv
        S, N, ex, Sp, Np = norms(m2v, Pv, Ppv)
        lam2 = m2v/(2*Pv*Ppv)
        L = mp.log(1/lam2)
        print(f" P={mp.nstr(Pv,3)},P'={mp.nstr(Ppv,3)} lam2=1e-{k}: int r = {mp.nstr(S,12)}  exact = {mp.nstr(ex,12)}"
              f"  |diff|={mp.nstr(abs(S-ex),3)} ; norm = {mp.nstr(N,10)} ; norm/lam2 = {mp.nstr(N/lam2,8)}"
              f" ; norm/(lam2 L) = {mp.nstr(N/(lam2*L),6)}; pieces N(mid,big,neg)/lam2 = "
              f"{', '.join(mp.nstr(v/lam2,6) for v in Np)}")
