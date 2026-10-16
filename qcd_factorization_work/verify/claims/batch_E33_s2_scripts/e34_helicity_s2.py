# E34(iv) stage-2: Borden-Kovchegov (BK, arXiv:2304.06161 eq. anomalous_dim) vs BER pure-glue large-Nc
# (as transcribed by BK eq. anom_BER).  abar = alpha_s N_c/(2 pi).
# Independent route: exact series in t = abar/omega^2 with rational arithmetic; intercepts from the
# branch points (resultants), checked against the closed forms; x-space small-x double logs.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

t, u, w, a = sp.symbols('t u omega abar', positive=True)
# Delta gamma = (omega/2) [1 - sqrt(1 - 16 t F(t))], t = abar/omega^2
F_BK  = sp.sqrt(1 - 4*t)
F_BER = (1 - 3*t)/(1 - t)
def series_coeffs(F, n=7):
    g = (1 - sp.sqrt(1 - 16*t*F))/2          # Delta gamma / omega as a series in t
    s = sp.series(g, t, 0, n+1).removeO()
    return [sp.nsimplify(s.coeff(t, k)) for k in range(1, n+1)]
cBK, cBER = series_coeffs(F_BK), series_coeffs(F_BER)
print("Delta gamma_GG = sum_k c_k abar^k / omega^(2k-1)")
print(" k :  BK      BER     diff")
for k, (x, y) in enumerate(zip(cBK, cBER), start=1):
    print(f" {k} : {str(x):7s} {str(y):7s} {str(x - y)}")

# intercepts: largest omega with 1 - 16 t F(t) = 0, i.e. u = omega^2/abar = 1/t
eqBK  = sp.expand(sp.numer(sp.together((u**2 - 256*(1 - 4/u)))))   # (u^2/256)^... : 1 = (16/u) sqrt(1-4/u)
eqBER = sp.expand(sp.numer(sp.together(u*(u - 1) - 16*(u - 3))))
print("BK  branch-point polynomial:", sp.factor(eqBK))
print("BER branch-point polynomial:", sp.factor(eqBER))
rBK  = max(r for r in sp.Poly(eqBK, u).nroots(n=30) if r.is_real)
rBER = max(r for r in sp.Poly(eqBER, u).nroots(n=30) if r.is_real)
print("alpha_h(BK)/sqrt(abar)  =", sp.N(sp.sqrt(rBK), 20))
print("alpha_h(BER)/sqrt(abar) =", sp.N(sp.sqrt(rBER), 20), " closed form sqrt((17+sqrt97)/2) =",
      sp.N(sp.sqrt((17 + sp.sqrt(97))/2), 20))
closed = 4/sp.root(3, 3)*sp.sqrt(sp.re(sp.root(-9 + sp.I*sp.sqrt(111), 3)))   # principal cube root
print("BK closed form (4/3^(1/3)) sqrt(Re[(-9+i sqrt111)^(1/3)]) =", sp.N(closed, 20))
# check the root really solves the unsquared equation and is the rightmost singularity (> inner branch point u=4)
print("check unsquared BK equation at root:", sp.N(1 - 16/rBK*sp.sqrt(1 - 4/rBK), 15), " root u =", sp.N(rBK, 15))
print("relative difference of intercepts:", sp.N(sp.sqrt(rBER)/sp.sqrt(rBK) - 1, 6))

# x-space small-x double logs: 1/omega^(2k-1) <-> ln^(2k-2)(1/x)/(2k-2)!
# in MVV normalisation a_s = alpha_s/(4 pi): abar = 2 N_c a_s, so coefficient of a_s^k L^(2k-2) in
# Delta P_gg^(k-1)(x->0) (pure glue, large N_c) is c_k (2 N_c)^k / (2k-2)!
Nc = sp.symbols('N_c')
for k in range(1, 5):
    print(f"Delta P_gg^({k-1}) small-x leading DL (BK):  {sp.nsimplify(cBK[k-1]*2**k/sp.factorial(2*k-2))} N_c^{k} ln^{2*k-2}(1/x)"
          f"    (BER: {sp.nsimplify(cBER[k-1]*2**k/sp.factorial(2*k-2))})")
