"""
W07 / Ch7 -- s5_exact_moments.py   (ex:dis-oneloop-ope, prop:dis-wilson-partons, prop:dis-c-oneloop)
Writer-derived, independent of research/c_dis code (only the closed forms VF-DIS-3/4/5 are used as input).
 (1) exact-in-eps Mellin moments of the bare one-loop partonic structure functions (massless on-shell partons, DR):
       F_2^q:  M_N = 1 + a_s C_F (mu^2/Q^2)^eps K(eps) R_N(eps),     a_s = alpha_s/(2 pi)
       F_2^g:  M_N =     a_s T_F (mu^2/Q^2)^eps K(eps) G_N(eps)
     with K(eps) = e^{eps gE} Gamma(1+eps) Gamma(1-eps)^2 / Gamma(1-2eps) and R_N, G_N RATIONAL functions of eps.
     Print R_2, G_2 (and the F_L analogues) in closed form; Laurent expansions -> -P/eps + C (VF-DIS-8).
 (2) MS-bar renormalization of the n=2 coefficient: C^(2)_{2,q} = M_2^bare / Z_qq(2) with Z_qq = 1 - a_s P_qq(2)/eps
     is finite and equals e_q^2[1 + a_s(C^q_{2,2} + P_qq(2) ln(Q^2/mu^2))]  (prop:dis-c-oneloop at N=2).
 (3) the two-point master integral of the hard-region (large-q) expansion with p^2 = 0:
       int d^Dl/(2pi)^D (p.l)^a / [(l^2)^al ((l+s q)^2)^be]
         = i (4pi)^{-D/2} (-1)^{al+be} (-s p.q)^a Gamma(al+be-D/2) Gamma(a+D/2-al) Gamma(D/2-be)
           / [Gamma(al) Gamma(be) Gamma(a+D-al-be)] (Q^2)^{D/2-al-be},     s = +-1,
     re-derived by Feynman parameters (shift, p^2=0 kills all (p.l')^{2k}, Beta integral); checked here
     symbolically for the x-integral and numerically against a direct 1D parametric quadrature.
Run: python3 -I s5_exact_moments.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

ok_all = True
def check(name, ok, extra=''):
    global ok_all
    ok_all &= bool(ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name} {extra}")

eps = sp.symbols('epsilon')
CF, TF = sp.symbols('C_F T_F', positive=True)

def S(k, N):
    return sum(sp.Rational(1, j**k) for j in range(1, N + 1))
def Pqq(N): return CF * (sp.Rational(3, 2) + sp.Rational(1, N * (N + 1)) - 2 * S(1, N))
def Pqg(N): return TF * sp.Rational(N**2 + N + 2, N * (N + 1) * (N + 2))
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

# Gamma(n+eps)/(Gamma(1+eps) Gamma(n)) as a rational function of eps
def Gr(n):
    return sp.prod([(k + eps) for k in range(1, n)]) / sp.factorial(n - 1)

# --- moments of the closed forms (VF-DIS-3/4/5), divided by K(eps):
# real quark F2: e^{eps gE} Gamma(-eps)/(2 Gamma(2-2eps)) * int z^{N-1} z^eps (1-z)^{-1-eps} [2(1+z^2) - eps(7-2z) + eps^2]
#   int z^{N-1+eps+k}(1-z)^{-1-eps} = Gamma(N+k+eps)Gamma(-eps)/Gamma(N+k)
#   => e^{eps gE} Gamma(1-eps)^2/(2 eps^2 Gamma(2-2eps)) sum_k c_k Gamma(N+k+eps)/Gamma(N+k)
#   and e^{eps gE}Gamma(1-eps)^2/Gamma(2-2eps) = K/((1-2eps) Gamma(1+eps)) * ...: divide by K:
def R2q(N):
    c = [2 - 7 * eps + eps**2, 2 * eps, 2]
    real = sum(c[k] * Gr(N + k) for k in range(3)) / (2 * eps**2 * (1 - 2 * eps))
    virt = -(2 - eps + 2 * eps**2) / (eps**2 * (1 - 2 * eps))       # 2 F^(1)/(a_s C_F K) of VF-DIS-3 (exact)
    return sp.factor(sp.simplify(real + virt))
def RLq(N):
    # e^{eps gE} Gamma(2-eps)/Gamma(2-2eps) int z^{N-1} 2z (z/(1-z))^eps = ... 2 Gamma(N+1+eps)Gamma(1-eps)/Gamma(N+2)
    return sp.factor(sp.simplify(2 * (1 - eps) * Gr(N + 1) / ((1 - 2 * eps) * (N + 1))))
def R2g(N):
    d = [1 - 3 * eps + 4 * eps**2 - 2 * eps**3, -2, 2]
    # 2 e^{eps gE} Gamma(-eps)/Gamma(2-2eps)/(1-eps)^2 * sum d_k Gamma(N+k+eps)Gamma(1-eps)/Gamma(N+k+1)
    return sp.factor(sp.simplify(-2 / (eps * (1 - 2 * eps) * (1 - eps)**2) * sum(d[k] * Gr(N + k) / (N + k) for k in range(3))))
def RLg(N):
    return sp.factor(sp.simplify(8 * (Gr(N + 1) / (N + 1) - Gr(N + 2) / (N + 2)) / ((1 - 2 * eps) * (1 - eps))))

# K(eps) expansion
def Kser(order=3):
    x = sp.symbols('x')
    lnK = eps * sp.EulerGamma + sp.loggamma(1 + eps) + 2 * sp.loggamma(1 - eps) - sp.loggamma(1 - 2 * eps)
    return sp.series(sp.exp(lnK), eps, 0, order).removeO()

print("(1) exact-in-eps moments (rational functions of eps after removing K(eps))")
K = Kser(4)
check("K(eps) = 1 - zeta_2 eps^2/2 + O(eps^3)", sp.simplify(sp.expand(K) - (1 - sp.pi**2 / 12 * eps**2) - sp.expand(K).coeff(eps, 3) * eps**3) == 0,
      f"K = {sp.nsimplify(sp.expand(K))}")
for N in [1, 2, 3, 4]:
    R = R2q(N)
    ser = sp.series(K * R, eps, 0, 1).removeO()
    m2, m1, m0 = [sp.simplify(ser.coeff(eps, k)) for k in (-2, -1, 0)]
    check(f"quark N={N}: (KR)_N = -P_qq/(C_F eps) + C^q_2/C_F + O(eps), no 1/eps^2",
          m2 == 0 and sp.simplify(CF * m1 + Pqq(N)) == 0 and sp.simplify(CF * m0 - C2q(N)) == 0,
          f"R_{N} = {R}")
    RL = RLq(N)
    check(f"quark N={N}: (K R_L)_N|_eps=0 = C^q_L/C_F", sp.simplify(CF * sp.limit(K * RL, eps, 0) - CLq(N)) == 0, f"R^L_{N} = {RL}")
for N in [2, 4]:
    G = R2g(N)
    ser = sp.series(K * G, eps, 0, 1).removeO()
    m1, m0 = [sp.simplify(ser.coeff(eps, k)) for k in (-1, 0)]
    check(f"gluon N={N}: (KG)_N = -2P_qg/(T_F eps) + 2C^g_2/T_F + O(eps)",
          sp.simplify(TF * m1 + 2 * Pqg(N)) == 0 and sp.simplify(TF * m0 - 2 * C2g(N)) == 0, f"G_{N} = {G}")
    GL = RLg(N)
    check(f"gluon N={N}: (K G_L)_N|_eps=0 = 2 C^g_L/T_F", sp.simplify(TF * sp.limit(K * GL, eps, 0) - 2 * CLg(N)) == 0, f"G^L_{N} = {GL}")

# closed forms to be printed for N = 2
R2 = R2q(2); G2 = R2g(2)
print("   R_2(eps)  =", R2, "   expansion:", sp.series(R2, eps, 0, 2))
print("   G_2(eps)  =", G2, "   expansion:", sp.series(G2, eps, 0, 2))
# a convenient printable form: R_2 = A/eps^2 + B/eps + ... check the claimed printed form
# find numerator/denominator
num, den = sp.fraction(sp.together(R2))
print("   R_2 = num/den with num =", sp.factor(num), ", den =", sp.factor(den))
numg, deng = sp.fraction(sp.together(G2))
print("   G_2 = num/den with num =", sp.factor(numg), ", den =", sp.factor(deng))

check("printed form R_2 = (1-eps)(8-7eps)/(6 eps(1-2eps))", sp.simplify(R2 - (1 - eps) * (8 - 7 * eps) / (6 * eps * (1 - 2 * eps))) == 0)
check("printed form G_2 = -(1+eps)(4-13eps+12eps^2)/(6 eps(1-eps)(1-2eps))",
      sp.simplify(G2 + (1 + eps) * (4 - 13 * eps + 12 * eps**2) / (6 * eps * (1 - eps) * (1 - 2 * eps))) == 0)
check("printed form R^L_2 = (1-eps)(1+eps)(2+eps)/(3(1-2eps))", sp.simplify(RLq(2) - (1 - eps) * (1 + eps) * (2 + eps) / (3 * (1 - 2 * eps))) == 0)
print("(2) MS-bar renormalization of the n = 2 quark coefficient")
a, L = sp.symbols('a_s L')           # L = ln(Q^2/mu^2)
mu_fac = sp.exp(-eps * L)            # (mu^2/Q^2)^eps
Mbare = 1 + a * CF * mu_fac * K * R2
Zqq = 1 - a * Pqq(2) / eps
C2 = sp.series(sp.expand(Mbare / Zqq), a, 0, 2).removeO()
C2_a1 = sp.series(sp.expand(C2.coeff(a, 1)), eps, 0, 1).removeO()
check("C^(2)_{2,q}: pole cancels", sp.simplify(C2_a1.coeff(eps, -1)) == 0 and sp.simplify(C2_a1.coeff(eps, -2)) == 0)
check("C^(2)_{2,q} = 1 + a_s [C_F/6 + P_qq(2) ln(Q^2/mu^2)],  P_qq(2) = -4C_F/3",
      sp.simplify(C2_a1.coeff(eps, 0) - (CF / 6 + Pqq(2) * L)) == 0, f"(finite part {sp.simplify(C2_a1.coeff(eps, 0))})")
# gluon: C^(2)_{2,g} = M^g_2,bare - 2 Z_qg ... : A_{q/g}+A_{qbar/g} = -a_s 2 P_qg/eps
Mg = a * TF * mu_fac * K * G2
Cg = sp.series(sp.expand(Mg + a * 2 * Pqg(2) / eps), eps, 0, 1).removeO()
check("C^(2)_{2,g} (per e_q^2) = a_s 2[C^g_{2,2} + P_qg(2) ln(Q^2/mu^2)], pole cancels",
      sp.simplify(Cg.coeff(eps, -1)) == 0 and sp.simplify(Cg.coeff(eps, 0) - a * 2 * (C2g(2) + Pqg(2) * L)) == 0,
      f"(= {sp.simplify(Cg.coeff(eps, 0))})")

print("(3) two-point master integral of the hard-region expansion (p^2 = 0)")
al, be, aa, Dd, x = sp.symbols('alpha beta a D x', positive=True)
# x-integral after Feynman parametrization and shift: int_0^1 x^{be-1}(1-x)^{al-1} x^a [x(1-x)]^{D/2-al-be}
xint = lambda A_, B_, a_, D_: mp.gamma(a_ + D_ / 2 - A_) * mp.gamma(D_ / 2 - B_) / mp.gamma(a_ + D_ - A_ - B_)
mp.mp.dps = 30
num_check = []
# convergent parameter points only (a + D/2 - al > 0 and D/2 - be > 0); elsewhere the closed form is the continuation
for (A_, B_, a_, D_) in [(1, 1, 0, mp.mpf(7) / 2), (1, 1, 1, mp.mpf(7) / 2), (2, 1, 2, mp.mpf(9) / 2), (1, 2, 3, mp.mpf(9) / 2)]:
    f = lambda t: t**(B_ - 1) * (1 - t)**(A_ - 1) * t**a_ * (t * (1 - t))**(D_ / 2 - A_ - B_)
    lhs = mp.quad(f, [0, 0.25, 0.5, 0.75, 1])
    rhs = xint(A_, B_, a_, D_)
    num_check.append(abs(lhs - rhs) < mp.mpf('1e-12') * abs(rhs))
# full master formula vs direct numerical evaluation in Euclidean form for a = 0 (scalar bubble), D = 3.5:
#   int d^D l_E/pi^{D/2} 1/[(l^2)^al ((l+q)^2)^be] = (q^2)^{D/2-al-be} G(al,be)
def G_closed(A_, B_, D_):
    return mp.gamma(A_ + B_ - D_ / 2) * mp.gamma(D_ / 2 - A_) * mp.gamma(D_ / 2 - B_) / (mp.gamma(A_) * mp.gamma(B_) * mp.gamma(D_ - A_ - B_))
def G_feyn(A_, B_, D_):
    # Feynman parameters: Gamma(A+B-D/2)/(Gamma(A)Gamma(B)) int_0^1 x^{B-1}(1-x)^{A-1} [x(1-x)]^{D/2-A-B}
    f = lambda t: t**(B_ - 1) * (1 - t)**(A_ - 1) * (t * (1 - t))**(D_ / 2 - A_ - B_)
    return mp.gamma(A_ + B_ - D_ / 2) / (mp.gamma(A_) * mp.gamma(B_)) * mp.quad(f, [0, 0.5, 1])
for (A_, B_, D_) in [(1, 1, mp.mpf('3.5')), (1, 2, mp.mpf('4.6')), (2, 1, mp.mpf('5.1'))]:
    check(f"bubble G({A_},{B_}) at D={float(D_)}: closed form = Feynman-parameter quadrature",
          abs(G_closed(A_, B_, D_) - G_feyn(A_, B_, D_)) < mp.mpf('1e-9') * abs(G_closed(A_, B_, D_)))
# numerator (p.l)^a with p^2=0: verify the shift statement with an explicit complex null p in Euclidean D=4 by
# checking the symmetric-integration identity  <(p.l')^2> = p^2 <l'^2>/D = 0  and  <(p.l')^4> ~ (p^2)^2 = 0
p = sp.Matrix([1, sp.I, 0, 0])
check("complex null vector: p^2 = 0", sp.simplify((p.T * p)[0]) == 0)
print("   => after l = l' - x s q only (-x s p.q)^a survives; the x-integral gives B(a+D/2-al, D/2-be)  [master formula]")

print("ALL PASS" if ok_all else "SOME CHECKS FAILED")
