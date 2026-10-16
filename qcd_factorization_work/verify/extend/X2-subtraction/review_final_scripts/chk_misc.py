import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
mp.mp.dps = 30

# ---- Prop B.2: sum of Collins terms -> Lt^2 + pi^2/3 (Qt = 1) ----
e, L = sp.symbols('epsilon L', positive=True)
m2 = sp.exp(-L)
CS = sp.gamma(e)**2*sp.gamma(1 - e)*m2**(-2*e)
CC = -sp.gamma(1 + e)*sp.gamma(1 - e)**2/(e**2*sp.gamma(1 - 2*e))*m2**(-e)
CH = sp.gamma(1 + e)*sp.gamma(1 - e)**2/(e**2*sp.gamma(1 - 2*e))
tot = sp.series(CS + 2*CC + CH, e, 0, 1).removeO()
print("B.2: sum C_R as eps->0 =", sp.simplify(sp.expand(tot)))

# ---- Prop B.4: sliver integrals at eps = 0 (P = P' = 1/sqrt2, Qt = 1) ----
def sliver(m2v):
    m2v = mp.mpf(m2v); P = Pp = 1/mp.sqrt(2); a = m2v/Pp
    def rhoG(xx, k):
        w = 2*xx + a; km = Pp + k/w
        Dg = -2*xx*km + k; D1 = 2*(P - xx)*(m2v/(2*P) + km) + k
        return 2/(w*Dg*D1)
    def rhoC2(xx, k):
        w = 2*xx + a
        return w/(P*((a - w)*Pp*w + a*k)*(Pp*w + k))
    IG = mp.quad(lambda xx: mp.quad(lambda k: rhoG(xx, k), [0, m2v, 1, mp.inf]), [-a/2, -a/4, 0])
    IC = mp.quad(lambda xx: mp.quad(lambda k: rhoC2(xx, k), [0, m2v, 1, mp.inf]), [-a/2, -a/4, 0])
    return IG, IC
for m2v in ['1e-3', '1e-5']:
    IG, IC = sliver(m2v)
    print(f"B.4 m2={m2v}: int_sl rho_CC2 - zeta2 = {mp.nstr(IC - mp.zeta(2), 5)};  int_sl rho_G - zeta2 = {mp.nstr(IG - mp.zeta(2), 5)};"
          f"  int_sl r / m2 = {mp.nstr((IG - IC)/mp.mpf(m2v), 8)}")

# ---- Thm D.1: int r = -M^2 int_1^inf ln(u/M^2)/(u(u-M^2)) vs series ----
for M2 in ['1e-3', '1e-6']:
    M2 = mp.mpf(M2); Lm = -mp.log(M2)
    I = -M2*mp.quad(lambda uu: mp.log(uu/M2)/(uu*(uu - M2)), [1, 10, mp.inf])
    ser = -M2*(Lm + 1) - M2**2*(Lm/2 + mp.mpf(1)/4)
    print(f"D.1 M2={M2}: int r = {mp.nstr(I, 15)}  series(2 terms) = {mp.nstr(ser, 15)}  diff/(M^6 L) = {mp.nstr((I - ser)/(M2**3*Lm), 5)}")
    # kappa-integral of the 0<u<1 bracket at a sample u
    uu = mp.mpf('0.37')
    b = mp.quad(lambda k: (1 - uu)/((M2*(1 - uu) + k)*(uu*(1 - uu) + k)) - 1/((M2 + k)*(uu + k)), [0, M2, 1, mp.inf])
    print(f"    kappa-integral of bracket at u=0.37: {mp.nstr(b, 5)}")

# ---- Thm E.3(v): NLP coefficient by series of the UD closed form ----
mm = sp.symbols('m2', positive=True)
Lt = -sp.log(mm)
LP = Lt**4/4 + sp.pi**2*Lt**2/2 + 7*sp.pi**4/60
Phi = (1 + mm)*(12*sp.polylog(4, -mm) + LP)/((1 - mm)*(1 + mm)**4)
# expand in m2 treating Lt as independent symbol
Ls = sp.symbols('Ls')
Phi_s = (1 + mm)*(12*sp.polylog(4, -mm) + (Ls**4/4 + sp.pi**2*Ls**2/2 + 7*sp.pi**4/60))/((1 - mm)*(1 + mm)**4)
ser = sp.series(Phi_s, mm, 0, 2).removeO()
nlp = sp.expand(ser - (Ls**4/4 + sp.pi**2*Ls**2/2 + 7*sp.pi**4/60))
print("E.3 NLP coefficient of m2:", sp.simplify(nlp.coeff(mm, 1)))
