#!/usr/bin/env python3
"""W24 / Ch21 -- exact large-beta0 coefficients of the Adler function from the closed form
(Beneke 1999, eq. (5.10); Beneke 1993, Broadhurst 1993), and comparison with the n_f^n terms of
independent multi-loop results.

Book conventions (def:power-borel, VF-EE-9):
  D/R_0 = 1 + sum_n d_n a^n,  a = alpha_s/pi;  b_0 = beta0/4,  beta0 = 11/3 C_A - 4/3 T_F n_f.
  Large-beta0:  D/R_0 - 1 = (3 C_F/4) a sum_n dhat_n (b_0 a)^n,
  Bhat(u) = sum_n dhat_n u^n/n! = 32/(3(2-u)) (mu^2 e^{5/3}/Q^2)^u S(u),
  S(u) = sum_{k>=2} (-1)^k k/(k^2-(1-u)^2)^2
       = [psi1((1+u)/2) - psi1((2+u)/2) - psi1((3-u)/2) + psi1((4-u)/2)] / (16 (1-u)).

The n_f^n part of the exact coefficient d_{n+1} equals (3 C_F/4) dhat_n (-T_F n_f/3)^n, i.e. for SU(3)
(C_F = 4/3, T_F = 1/2): dhat_n (-n_f/6)^n.

Independent checks:
 (A) d_2 (= r_2) n_f-term (VF-EE-10, SU(3), status V): -(11/12 - 2/3 zeta3) n_f.
 (B) d_3 n_f^2-term: from r_3 = d_3 - (pi^2/3) b_0^2 d_1 (VF-EE-9) and the published
     r_3 n_f^2 coefficient -0.00518 (Baikov-Chetyrkin-Kuhn 2008, eq. (5); originally GKL 1991, SS 1991).
 (C) d_4 n_f^3-term: BCK 2008 eq. (4): -6131/5832 + 203/324 zeta3 + 5/18 zeta5   (analytic match).
 (D) r_4 n_f^3-term from VF-EE-9 relation vs BCK eq. (5): +0.0215.
 (E) the trigamma representation equals the k-sum (numerically, several u).
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

u = sp.symbols('u')
z3, z5, z7 = sp.zeta(3), sp.zeta(5), sp.zeta(7)

# ---- (E) trigamma form vs k-sum (numerical, mpmath) ----
mp.mp.dps = 40
def S_sum(x):
    a = 1 - mp.mpf(x)
    return mp.nsum(lambda k: (-1)**int(k)*k/(k**2 - a**2)**2, [2, mp.inf])
def S_tri(x):
    x = mp.mpf(x)
    p1 = lambda w: mp.psi(1, w)
    return (p1((1+x)/2) - p1((2+x)/2) - p1((3-x)/2) + p1((4-x)/2))/(16*(1-x))
check("(E) trigamma representation of S(u) equals the k-sum at u = 0.3, -0.7, 1.6, 2.5",
      all(abs(S_sum(x) - S_tri(x)) < mp.mpf(10)**-30 for x in ['0.3', '-0.7', '1.6', '2.5']))

# ---- exact Taylor coefficients with sympy ----
S_expr = (sp.polygamma(1, (1+u)/2) - sp.polygamma(1, (2+u)/2) - sp.polygamma(1, (3-u)/2)
          + sp.polygamma(1, (4-u)/2))/(16*(1-u))
Bhat = sp.Rational(32, 3)/(2-u)*sp.exp(sp.Rational(5, 3)*u)*S_expr   # mu = Q
N = 4
ser = sp.series(Bhat, u, 0, N+1).removeO()
def psi_half3(m):
    # exact: psi^{(m)}(3/2) = psi^{(m)}(1/2) + (-1)^m m! 2^{m+1},  psi^{(m)}(1/2) = (-1)^{m+1} m! (2^{m+1}-1) zeta(m+1)
    return (-1)**(m+1)*sp.factorial(m)*(2**(m+1)-1)*sp.zeta(m+1) + (-1)**m*sp.factorial(m)*2**(m+1)
def to_zeta(expr):
    for m in range(1, 8):
        expr = expr.subs(sp.polygamma(m, sp.Rational(3, 2)), psi_half3(m))
    return sp.simplify(sp.expand(expr))
dhat = []
for n in range(N+1):
    c = to_zeta(ser.coeff(u, n)*sp.factorial(n))
    dhat.append(c)
    print(f"   dhat_{n} = {c}   = {sp.N(c, 12)}")

check("dhat_0 = 1", sp.simplify(dhat[0] - 1) == 0)
check("dhat_1 = 11/2 - 4 zeta3", sp.simplify(dhat[1] - (sp.Rational(11, 2) - 4*z3)) == 0)
check("dhat_2 = 302/9 - 76/3 zeta3", sp.simplify(dhat[2] - (sp.Rational(302, 9) - sp.Rational(76, 3)*z3)) == 0)
check("dhat_3 = 6131/27 - 406/3 zeta3 - 60 zeta5",
      sp.simplify(dhat[3] - (sp.Rational(6131, 27) - sp.Rational(406, 3)*z3 - 60*z5)) == 0)
print("   dhat_4 (exact) =", sp.simplify(dhat[4]), "=", sp.N(dhat[4], 12))

# Beneke 1999 Table 4 (read in the arXiv text): 1, 0.6918, 3.1035, 2.1800, 30.740
tab4 = [1, 0.6918, 3.1035, 2.1800, 30.740]
check("dhat_0..4 agree with Beneke 1999 Table 4", all(abs(float(dhat[n]) - tab4[n]) < 6e-4*max(1, abs(tab4[n])) for n in range(5)))

# ---- independent n_f^n checks (SU(3)) ----
nf = sp.symbols('n_f')
CF, TF = sp.Rational(4, 3), sp.Rational(1, 2)
def nf_top(n):   # n_f^n coefficient of d_{n+1} predicted by the closed form
    return sp.simplify(sp.Rational(3, 4)*CF*dhat[n]*(-TF/3)**n)
# (A)
check("(A) n_f-term of d_2: -(11/12 - 2/3 zeta3)  [VF-EE-10]", sp.simplify(nf_top(1) + (sp.Rational(11, 12) - sp.Rational(2, 3)*z3)) == 0)
# (B)
d3nf2 = nf_top(2)
print("   n_f^2 term of d_3 (closed form):", d3nf2, "=", sp.N(d3nf2, 10))
check("     equals 151/162 - 19/27 zeta3", sp.simplify(d3nf2 - (sp.Rational(151, 162) - sp.Rational(19, 27)*z3)) == 0)
b0 = (11 - sp.Rational(2, 3)*nf)/4
kin_nf2 = sp.expand(-(sp.pi**2/3)*b0**2*1).coeff(nf, 2)   # d_1 = 1 for SU(3)
r3nf2 = sp.N(d3nf2 + kin_nf2, 8)
print("   predicted r_3 n_f^2 coefficient:", r3nf2, " (BCK 2008 eq. (5): -0.00518)")
check("(B) r_3 n_f^2 coefficient = -0.00518 (4 digits)", abs(float(r3nf2) + 0.00518) < 5e-6)
# (C)
d4nf3_bck = -sp.Rational(6131, 5832) + sp.Rational(203, 324)*z3 + sp.Rational(5, 18)*z5
check("(C) n_f^3 term of d_4 equals BCK 2008 eq. (4) exactly", sp.simplify(nf_top(3) - d4nf3_bck) == 0)
print("   n_f^3 term of d_4 =", sp.N(d4nf3_bck, 10))
# (D) r_4 = d_4 - pi^2 (b_0^2 d_2 + 5/6 b_0 b_1 d_1), n_f^3 part; d_2 = 365/24 - 11 zeta3 - n_f(11/12 - 2/3 zeta3)
d2 = sp.Rational(365, 24) - 11*z3 - nf*(sp.Rational(11, 12) - sp.Rational(2, 3)*z3)
b1 = (102 - sp.Rational(38, 3)*nf)/16
r4nf3 = sp.N(d4nf3_bck + sp.expand(-sp.pi**2*(b0**2*d2 + sp.Rational(5, 6)*b0*b1*1)).coeff(nf, 3), 8)
print("   r_4 n_f^3 coefficient from VF-EE-9 relation:", r4nf3, " (BCK 2008 eq. (5): +0.0215)")
check("(D) r_4 n_f^3 coefficient = 0.0215", abs(float(r4nf3) - 0.0215) < 6e-5)

# ---- comparison table for n_f = 3 (coefficients of a^{n+1}) ----
for nfv in [3, 4, 5]:
    b0v = sp.Rational(11, 4) - sp.Rational(nfv, 6)
    vals = [float(sp.Rational(3, 4)*CF*dhat[n]*b0v**n) for n in range(4)]
    print(f"   n_f={nfv}: large-beta0 coefficients of a^1..a^4: " + ", ".join(f"{v:.4f}" for v in vals))
# exact: d_2 = 1.9857 - 0.1153 n_f (VF-EE-10); d_3(n_f=3) = pi^2 (1.5919 - 0.9464) (Beneke Table 4); d_4(n_f=3) = 49.08 (BCK eq. (8))
print("   exact (n_f=3): a^2: %.4f ; a^3: %.4f (Beneke Table 4: pi^2 (1.5919-0.9464)) ; a^4: 49.08 (BCK eq. (8))"
      % (1.9857 - 0.1153*3, float(sp.pi**2*(1.5919 - 0.9464))))

# ---- value at u = 1 (no pole) ----
B1 = to_zeta(sp.limit(Bhat, u, 1))
print("   Bhat(1) =", sp.simplify(B1), "=", sp.N(B1, 12))
check("Bhat(1) = (32/3) e^{5/3} (1 - 3 zeta3/4)  (finite: no pole at u = 1)",
      abs(sp.N(B1 - sp.Rational(32, 3)*sp.exp(sp.Rational(5, 3))*(1 - sp.Rational(3, 4)*z3), 30)) < 1e-25)
# S(2) = 3/16 -> residue of the u=2 pole of Bhat is 2 e^{10/3}
S2 = sp.N(S_expr.subs(u, 2), 30)
check("S(2) = 3/16 (so Bhat ~ 2 e^{10/3}/(2-u) at u=2)", abs(S2 - sp.Rational(3, 16)) < 1e-25)
print("ALL PASS" if OK else "SOME CHECKS FAILED")
