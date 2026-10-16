"""
W07 / Ch7 -- s4_wilson_rg.py   (prop:dis-c-oneloop, ex:dis-oneloop-ope, cor:dis-scaling, ex:dis-n2, thm:dis-bjorken,
                                rem:dis-crewther, prop:dis-ope-rg, thm:dis-moments-np(i))
 (1) independent re-derivation of the one-loop Mellin moments (VF-DIS-8) from the exact-in-eps cut results
     VF-DIS-3 (virtual), VF-DIS-4 (real, quark), VF-DIS-5 (photon-gluon fusion): Mellin moments of
     z^eps (1-z)^(-1-eps) z^k are Beta functions; expand in eps; check 1/eps^2 cancels, 1/eps = -P_{qq,N} (resp. -2P_{qg,N}),
     eps^0 = C^q_{2,N} (resp. 2 C^g_{2,N}); and C_L.  N = 1..8, exact (rationals and zeta_2).
 (2) closed forms (VF-DIS-8) -> table N=1..8; Adler C^q_{2,1}=0; Bjorken-nu C^q_{1,1}=C^q_{2,1}-C^q_{L,1}=-C_F;
     MVV normalization c^(1)_{2,q} = 2 C^q_{2,N}; mu-independence of sum_i C^(2)_i A^(2)_i at O(alpha_s).
 (3) N=2 singlet matrix: eigenvalues 0, -(4C_F+2n_fT_F)/3; asymptotic fraction 3n_f/(16+3n_f); LO non-singlet evolution
     exponent -2 gamma_qq(n)/beta0 (solve the ODE); numbers with the VF-QCD-7 one-loop alpha_s values.
 (4) RG solution C(mu) = C(Q) P exp(-int_mu^Q gamma dmu'/mu') with gamma = -2 Gamma solves mu dC/dmu = C gamma.
 (5) Bjorken: a^2 coefficient -(55/12 - n_f/3) = -3.5833 at n_f=3; Crewther: C_Bjp D_NS = 1 + beta0 (7/8 - zeta3) a^2
     = 1 - (beta0/4) K1 a^2 with K1 = C_F(-21/8 + 3 zeta3); uses r_2^NS = d_2 (VF-EE-9/10).
 (6) beta_xi = mu d xi_R/d mu from xi_0 = Z_3 xi_R (VF-QCD-4): (alpha_s/2pi) xi[(13/6 - xi/2)C_A - 4/3 T_F n_f];
     at xi=1, SU(3): (alpha_s/2pi)(5 - 2n_f/3).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

ok_all = True
def check(name, ok, extra=''):
    global ok_all
    ok_all &= bool(ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name} {extra}")

eps = sp.symbols('epsilon')
CF, TF, CA, nf = sp.symbols('C_F T_F C_A n_f', positive=True)
z2 = sp.zeta(2)

def S(k, N):
    return sum(sp.Rational(1, j**k) for j in range(1, N + 1))

# closed forms (VF-DIS-8), units alpha_s/2pi
def C2q(N):
    S1, S2 = S(1, N), S(2, N)
    return CF * (S1**2 - S2 + sp.Rational(3, 2) * S1 - S1 / (N * (N + 1)) + sp.Rational(3, 2 * N) + sp.Rational(2, N + 1)
                 + sp.Rational(1, N**2) - sp.Rational(9, 2))
def C2g(N):
    S1 = S(1, N)
    return TF * (-sp.Rational(N**2 + N + 2, N * (N + 1) * (N + 2)) * S1 + sp.Rational(1, N**2) - sp.Rational(1, N)
                 + sp.Rational(6, (N + 1) * (N + 2)))
def CLq(N): return 2 * CF / (N + 1)
def CLg(N): return 4 * TF / ((N + 1) * (N + 2))
def Pqq(N): return CF * (sp.Rational(3, 2) + sp.Rational(1, N * (N + 1)) - 2 * S(1, N))
def Pqg(N): return TF * sp.Rational(N**2 + N + 2, N * (N + 1) * (N + 2))
def Pgq(N): return CF * sp.Rational(N**2 + N + 2, (N - 1) * N * (N + 1))
def Pgg(N): return 2 * CA * (sp.Rational(1, N * (N - 1)) + sp.Rational(1, (N + 1) * (N + 2)) - S(1, N)) + (sp.Rational(11, 3) * CA - sp.Rational(4, 3) * TF * nf) / 2

# ---------------------------------------------------------------- (1) from the exact cut results
print("(1) Mellin moments of the exact-in-eps cut results (VF-DIS-3/4/5), mu = Q")
# exact truncated power series in eps: dict power -> coefficient ; we need orders up to eps^2 inside products
ORD = 3
def ps_mul(a, b):
    c = {}
    for i, x in a.items():
        for j, y in b.items():
            if i + j <= ORD:
                c[i + j] = sp.expand(c.get(i + j, 0) + x * y)
    return c
def ps_exp(a):
    # exp of a series with a[0] = 0
    res = {0: sp.Integer(1)}; term = {0: sp.Integer(1)}
    for k in range(1, ORD + 1):
        term = ps_mul(term, a); term = {i: v / k for i, v in term.items()}
        for i, v in term.items():
            res[i] = sp.expand(res.get(i, 0) + v)
    return res
def ps_scale(a, f):
    return {i: sp.expand(v * f) for i, v in a.items()}
z3 = sp.zeta(3)
def psi_k(n, k):
    # polygamma(k, n) for integer n >= 1 : psi(n) = -gE + S1(n-1); psi^(k)(n) = (-1)^(k+1) k! (zeta(k+1) - S_{k+1}(n-1))
    if k == 0:
        return -sp.EulerGamma + S(1, n - 1)
    return (-1)**(k + 1) * sp.factorial(k) * (sp.zeta(k + 1) - S(k + 1, n - 1))
def lnGamma_ratio(n, c):
    """series of ln[Gamma(n + c*eps)/Gamma(n)] for integer n>=1, coefficient c"""
    return {k: psi_k(n, k - 1) * c**k / sp.factorial(k) for k in range(1, ORD + 1)}
def Gratio(n, c):
    return ps_exp(lnGamma_ratio(n, c))
def ps_add(*args):
    c = {}
    for a in args:
        for i, v in a.items():
            c[i] = sp.expand(c.get(i, 0) + v)
    return c
def poly_eps(coeffs):    # polynomial in eps -> series
    return {i: sp.Integer(c) if isinstance(c, int) else c for i, c in enumerate(coeffs)}
# Gamma(-eps) = -Gamma(1-eps)/eps  -> handle the 1/eps factors explicitly
expgE = ps_exp({1: sp.EulerGamma})                    # e^{eps gamma_E}
G1m = Gratio(1, -1)                                    # Gamma(1-eps)
G1p = Gratio(1, 1)                                     # Gamma(1+eps)
G1m2 = Gratio(1, -2)                                   # Gamma(1-2eps)
inv_G1m2 = ps_exp({k: -v for k, v in lnGamma_ratio(1, -2).items()})
# Gamma(2-2eps) = (1-2eps) Gamma(1-2eps) ; Gamma(2-eps) = (1-eps)Gamma(1-eps)
def inv_series(a):
    # 1/a for a[0] != 0
    a0 = sp.Integer(a[0]) if isinstance(a[0], int) else a[0]; b = {0: 1 / a0}
    for k in range(1, ORD + 1):
        b[k] = sp.expand(-sum(a.get(j, 0) * b[k - j] for j in range(1, k + 1)) / a0)
    return b
inv_1m2e = inv_series({0: 1, 1: -2})
inv_1me = inv_series({0: 1, 1: -1})
def lead(series_dict, shift):
    """multiply by eps^shift (shift negative): returns dict with shifted keys"""
    return {i + shift: v for i, v in series_dict.items()}
for N in range(1, 9):
    # R2q = e^{eps gE} Gamma(-eps)/(2 Gamma(2-2eps)) * sum_k c_k Gamma(N+eps+k)Gamma(-eps)/Gamma(N+k)
    #     = e^{eps gE} Gamma(1-eps)^2/(2 eps^2 Gamma(2-2eps)) * sum_k c_k Gamma(N+k+eps)/Gamma(N+k)
    poly = {0: {0: 2, 1: -7, 2: 1}, 1: {1: 2}, 2: {0: 2}}
    summ = {}
    for k, cpoly in poly.items():
        summ = ps_add(summ, ps_mul({i: sp.Integer(v) for i, v in cpoly.items()}, Gratio(N + k, 1)))
    R2q = ps_mul(ps_mul(ps_mul(expgE, ps_mul(G1m, G1m)), ps_mul(inv_1m2e, inv_G1m2)), summ)
    R2q = {i - 2: v / 2 for i, v in R2q.items()}            # 1/(2 eps^2)
    # virtual: e^{eps gE} Gamma(1+eps)Gamma(1-eps)^2/Gamma(1-2eps) * [-(2 - eps + 2 eps^2)/(eps^2 (1-2eps))]
    Vp = ps_mul(ps_mul(expgE, ps_mul(G1p, ps_mul(G1m, G1m))), inv_G1m2)
    Vp = ps_mul(Vp, ps_mul({0: -2, 1: 1, 2: -2}, inv_1m2e))
    Vp = {i - 2: v for i, v in Vp.items()}
    tot = ps_add(R2q, Vp)
    m2_, m1_, m0_ = sp.simplify(tot.get(-2, 0)), sp.simplify(CF * tot.get(-1, 0)), sp.simplify(CF * tot.get(0, 0))
    ok = (m2_ == 0) and sp.simplify(m1_ + Pqq(N)) == 0 and sp.simplify(m0_ - C2q(N)) == 0
    check(f"quark N={N}: no 1/eps^2; 1/eps = -P_qq,N; eps^0 = C^q_2,N", ok, f"(C^q_2/C_F = {sp.nsimplify(sp.simplify(m0_ / CF))})")
    # R_L^q = e^{eps gE} Gamma(2-eps)/Gamma(2-2eps) 2 Gamma(N+1+eps)Gamma(1-eps)/Gamma(N+2)
    #       = e^{eps gE} (1-eps)Gamma(1-eps)^2/((1-2eps)Gamma(1-2eps)) * 2 Gamma(N+1+eps)/((N+1) Gamma(N+1))
    RL = ps_mul(ps_mul(expgE, ps_mul({0: 1, 1: -1}, ps_mul(G1m, G1m))), ps_mul(inv_1m2e, inv_G1m2))
    RL = ps_scale(ps_mul(RL, Gratio(N + 1, 1)), sp.Rational(2, N + 1))
    check(f"quark N={N}: C^q_L,N = 2C_F/(N+1)", sp.simplify(CF * RL[0] - CLq(N)) == 0)
for N in range(1, 9):
    # R2g = 2 e^{eps gE} Gamma(-eps)/Gamma(2-2eps) /(1-eps)^2 * sum_k c_k Gamma(N+eps+k)Gamma(1-eps)/Gamma(N+k+1)
    #     = -2 e^{eps gE} Gamma(1-eps)^2/(eps (1-2eps)Gamma(1-2eps)(1-eps)^2) * sum_k c_k Gamma(N+k+eps)/(Gamma(N+k)(N+k))
    poly = {0: {0: 1, 1: -3, 2: 4, 3: -2}, 1: {0: -2}, 2: {0: 2}}
    summ = {}
    for k, cpoly in poly.items():
        summ = ps_add(summ, ps_scale(ps_mul({i: sp.Integer(v) for i, v in cpoly.items()}, Gratio(N + k, 1)), sp.Rational(1, N + k)))
    R2g = ps_mul(ps_mul(expgE, ps_mul(G1m, G1m)), ps_mul(ps_mul(inv_1m2e, inv_G1m2), ps_mul(inv_1me, inv_1me)))
    R2g = ps_mul(R2g, summ)
    R2g = {i - 1: -2 * v for i, v in R2g.items()}
    g1_, g0_ = sp.simplify(TF * R2g.get(-1, 0)), sp.simplify(TF * R2g.get(0, 0))
    ok = sp.simplify(g1_ + 2 * Pqg(N)) == 0 and sp.simplify(g0_ - 2 * C2g(N)) == 0
    check(f"gluon N={N}: 1/eps = -2 P_qg,N; eps^0 = 2 C^g_2,N", ok, f"(C^g_2/T_F = {sp.nsimplify(sp.simplify(g0_ / (2 * TF)))})")
    # R_L^g = e^{eps gE} Gamma(1-eps)/Gamma(2-2eps) 8/(1-eps) [Gamma(N+1+eps)Gamma(1-eps)/Gamma(N+2) - Gamma(N+2+eps)Gamma(1-eps)/Gamma(N+3)]
    pre = ps_mul(ps_mul(expgE, ps_mul(G1m, G1m)), ps_mul(ps_mul(inv_1m2e, inv_G1m2), inv_1me))
    br = ps_add(ps_scale(Gratio(N + 1, 1), sp.Rational(1, N + 1)), ps_scale(Gratio(N + 2, 1), -sp.Rational(1, N + 2)))
    RLg = ps_scale(ps_mul(pre, br), 8)
    check(f"gluon N={N}: 2 C^g_L,N = 8T_F/((N+1)(N+2))", sp.simplify(TF * RLg[0] - 2 * CLg(N)) == 0)

# ---------------------------------------------------------------- (2) table and sum rules
print("(2) table, sum rules, normalizations")
table = {1: (0, sp.Rational(1, 3)), 2: (sp.Rational(1, 6), -sp.Rational(1, 4)), 3: (sp.Rational(29, 24), -sp.Rational(7, 20)),
         4: (sp.Rational(91, 40), -sp.Rational(133, 360)), 5: (sp.Rational(589, 180), -sp.Rational(23, 63)),
         6: (sp.Rational(5281, 1260), -sp.Rational(1777, 5040)), 7: (sp.Rational(50791, 10080), -sp.Rational(27, 80)),
         8: (sp.Rational(58703, 10080), -sp.Rational(16231, 50400))}
for N, (cq, cg) in table.items():
    check(f"N={N}: VF-DIS-8 table", sp.simplify(C2q(N) / CF - cq) == 0 and sp.simplify(C2g(N) / TF - cg) == 0,
          f"(P_qq/C_F={sp.simplify(Pqq(N) / CF)}, P_qg/T_F={sp.simplify(Pqg(N) / TF)}, C_L^q/C_F={CLq(N) / CF}, C_L^g/T_F={CLg(N) / TF})")
check("Adler: C^q_{2,1} = 0", sp.simplify(C2q(1)) == 0)
check("Bjorken nu: C^q_{1,1} = C^q_{2,1} - C^q_{L,1} = -C_F", sp.simplify(C2q(1) - CLq(1) + CF) == 0)
print("   -> 1 + (alpha_s/2pi)(-C_F) = 1 - (2/3) alpha_s/pi for C_F = 4/3")
L, a2pi = sp.symbols('L a')     # L = ln(Q^2/mu^2), a = alpha_s/2pi
Aq, Ag, eq2 = sp.symbols('A_q A_g e_q2')
# d/dln mu^2: dL = -1 ; dA_q = a [gqq A_q + 2 gqg A_g] (per flavour, q+qbar) ; dA_g = a[gqg-terms] (O(a) irrelevant for C_g at O(a))
N = 2
Cq = eq2 * (1 + a2pi * (C2q(N) + Pqq(N) * L))
Cg = eq2 * a2pi * 2 * (C2g(N) + Pqg(N) * L)
dsum = sp.expand(sp.diff(Cq * Aq + Cg * Ag, L) * (-1) + Cq * a2pi * (Pqq(N) * Aq + 2 * Pqg(N) * Ag))
dsum_Oa = sp.expand(dsum).coeff(a2pi, 1)
check("n=2: sum_i C^(2)_i A^(2)_i is mu-independent at O(alpha_s)", sp.simplify(dsum_Oa) == 0)

# ---------------------------------------------------------------- (3) singlet n=2 and LO evolution
print("(3) N=2 singlet and LO non-singlet evolution")
Mmat = sp.Matrix([[Pqq(2), 2 * nf * Pqg(2)], [Pgq(2), Pgg(2)]]).subs(CA, 3)
check("N=2 matrix = [[-4C_F/3, 2n_fT_F/3],[4C_F/3, -2n_fT_F/3]]",
      sp.simplify(Mmat - sp.Matrix([[-sp.Rational(4, 3) * CF, sp.Rational(2, 3) * nf * TF], [sp.Rational(4, 3) * CF, -sp.Rational(2, 3) * nf * TF]])) == sp.zeros(2))
ev = Mmat.eigenvals()
check("eigenvalues {0, -(4C_F+2n_fT_F)/3}", set(sp.simplify(e) for e in ev) == {0, sp.simplify(-(4 * CF + 2 * nf * TF) / 3)}, f"{ev}")
v0 = Mmat.nullspace()[0]
frac = sp.simplify(v0[0] / (v0[0] + v0[1]))
check("asymptotic quark momentum fraction = n_f T_F/(2C_F + n_f T_F) -> 3n_f/(16+3n_f) (SU(3))",
      sp.simplify(frac.subs({CF: sp.Rational(4, 3), TF: sp.Rational(1, 2)}) - 3 * nf / (16 + 3 * nf)) == 0, f"({frac})")
for nfv in [3, 4, 5, 6]:
    print(f"     n_f={nfv}: <x>_Sigma -> {sp.Rational(3 * nfv, 16 + 3 * nfv)} = {float(sp.Rational(3 * nfv, 16 + 3 * nfv)):.4f},"
          f"  <x>_g -> {float(sp.Rational(16, 16 + 3 * nfv)):.4f}")
# column sums zero (momentum conservation): (1,1) is a left eigenvector with eigenvalue 0
check("momentum conservation: (1,1) M = 0", sp.simplify((sp.Matrix([[1, 1]]) * Mmat)) == sp.zeros(1, 2))
# LO NS evolution: dA/dln mu^2 = (alpha/2pi) g A, dalpha/dln mu^2 = -(b0/4pi) alpha^2
al = sp.symbols('alpha', positive=True); gq, b0 = sp.symbols('gamma b0')
Afun = sp.Function('A')
Cc = sp.symbols('Cc')
ans = Cc * al**(-2 * gq / b0)
ode = sp.diff(ans, al) - (al / (2 * sp.pi) * gq * ans) / (-(b0 / (4 * sp.pi)) * al**2)
check("LO: A(alpha) = C alpha^(-2 gamma/beta0) solves dA/dalpha = [(alpha/2pi) gamma A]/[-(beta0/4pi) alpha^2]", sp.simplify(ode) == 0)
# numbers: alpha_s one loop n_f=5 (VF-QCD-7): Q=10 GeV 0.1731, Q=91.19 GeV 0.1180
r = sp.Rational(1180, 1731)
beta0_5 = sp.Rational(23, 3)
for n in [2, 4, 6, 8]:
    gam = Pqq(n).subs(CF, sp.Rational(4, 3))
    expo = -2 * gam / beta0_5
    print(f"     n={n}: gamma_qq={gam} = {float(gam):.5f}, exponent -2gamma/beta0 = {float(expo):.5f}, "
          f"M_n(91.19)/M_n(10) = {float(r**expo):.4f}")

# ---------------------------------------------------------------- (4) RG solution
print("(4) RG solution with path ordering (lower scales to the right)")
# 1x1 check with symbolic gamma(t), t = ln mu
t, tQ = sp.symbols('t t_Q'); gfun = sp.Function('g')
U = sp.exp(-sp.Integral(gfun(sp.Symbol('s')), (sp.Symbol('s'), t, tQ)))
check("dU/dln mu = U gamma(mu), U(Q) = 1", sp.simplify(sp.diff(U, t) - U * gfun(t)) == 0 and U.subs(t, tQ).doit() == 1)
print("   gamma = -2 Gamma: mu dC/dmu = 2 dC/dln mu^2 = -2 C Gamma = C gamma (prop:dis-ope-rg) ; GW: gamma_O = -(alpha_s/pi) gamma_qq(N) > 0")

# ---------------------------------------------------------------- (5) Bjorken and Crewther
print("(5) Bjorken sum rule coefficient and Crewther relation")
a = sp.symbols('a')
for nfv in [3, 4, 5]:
    cbjp = 1 - a - (sp.Rational(55, 12) - sp.Rational(nfv, 3)) * a**2
    r2 = sp.Rational(365, 24) - 11 * sp.zeta(3) - nfv * (sp.Rational(11, 12) - sp.Rational(2, 3) * sp.zeta(3))
    dns = 1 + a + r2 * a**2
    prod = sp.expand(cbjp * dns)
    beta0 = 11 - sp.Rational(2, 3) * nfv
    target = 1 + beta0 * (sp.Rational(7, 8) - sp.zeta(3)) * a**2
    c2 = sp.simplify(prod.coeff(a, 2) - target.coeff(a, 2))
    K1 = sp.Rational(4, 3) * (-sp.Rational(21, 8) + 3 * sp.zeta(3))
    ok = (sp.simplify(prod.coeff(a, 1)) == 0) and c2 == 0 and sp.simplify(-beta0 / 4 * K1 - beta0 * (sp.Rational(7, 8) - sp.zeta(3))) == 0
    check(f"n_f={nfv}: C_Bjp D_NS = 1 + beta0 (7/8 - zeta3) a^2 + O(a^3) = 1 - (beta0/4) K1 a^2", ok,
          f"(C_Bjp a^2 coeff = {float(-(sp.Rational(55, 12) - sp.Rational(nfv, 3))):.4f}, r2 = {float(r2):.4f})")
# parton-model normalization: int (g1p - g1n) = g_A/6
du, dd, ds = sp.symbols('Du Dd Ds')
g1p = sp.Rational(1, 2) * (sp.Rational(4, 9) * du + sp.Rational(1, 9) * dd + sp.Rational(1, 9) * ds)
g1n = sp.Rational(1, 2) * (sp.Rational(4, 9) * dd + sp.Rational(1, 9) * du + sp.Rational(1, 9) * ds)
check("parton model: int(g1p - g1n) = (Du - Dd)/6 = g_A/6", sp.simplify(g1p - g1n - (du - dd) / 6) == 0)

# ---------------------------------------------------------------- (6) beta_xi
print("(6) beta_xi from xi_0 = Z_3 xi_R")
alpha_s, xi = sp.symbols('alpha_s xi', positive=True)
dZ3 = (sp.Rational(13, 6) - xi / 2) * CA - sp.Rational(4, 3) * TF * nf
# mu d alpha_s/d mu = -2 eps alpha_s + O(alpha^2) ; ln Z3 = alpha_s dZ3/(4 pi eps) ; mu d xi/dmu = -xi mu d ln Z3/dmu
dlnZ3 = dZ3 / (4 * sp.pi * eps) * (-2 * eps * alpha_s)
beta_xi = sp.simplify(-xi * dlnZ3)
check("beta_xi = (alpha_s/2pi) xi [(13/6 - xi/2) C_A - (4/3) T_F n_f]", sp.simplify(beta_xi - alpha_s / (2 * sp.pi) * xi * dZ3) == 0)
check("xi=1, SU(3): (alpha_s/2pi)(5 - 2n_f/3), nonzero for every n_f",
      sp.simplify(beta_xi.subs({xi: 1, CA: 3, TF: sp.Rational(1, 2)}) - alpha_s / (2 * sp.pi) * (5 - sp.Rational(2, 3) * nf)) == 0)

print("ALL PASS" if ok_all else "SOME CHECKS FAILED")
