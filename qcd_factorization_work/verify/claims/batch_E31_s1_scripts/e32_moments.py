"""
E32 independent check (verifier stage 1, batch E31).
One-loop MS-bar quark coefficient function of F_2, normalisation a_s = alpha_s/(4 pi):
  x-space (VVM, NPB 724 (2005) 3, eq. (4.3) [arXiv:hep-ph/0504242, label eq:c2ns1], quoting BBDM 1978):
  c(x) = CF{ 4 D1 - 3 D0 - (9+4 z2) delta(1-x) - 2(1+x)(L1 - L0) - 4 L0/(1-x) + 6 + 4x }.
  N-space (VVM eq. (A.3)): CF( 9(S1-1) + 2 g_qq (S11 + 2 S1 - S2) - 7 (N_- + 1) S1 ), g_qq = N_+ + N_-,
  N_{+-} S(N) = S(N+-1).
Checks:
 (1) high-precision numerical Mellin moments (mpmath, 40 digits) of the x-space distribution, N = 1..12,
     vs the exact rational closed form CF[2S1^2 - 2S2 + 3S1 - 2S1/(N(N+1)) + 3/N + 4/(N+1) + 2/N^2 - 9];
 (2) VVM (A.3) shift-operator form vs closed form (exact rationals), N = 1..30 (S(0) = 0);
 (3) N=1 values of the closed form and of the 'variant' (2/(N+1) + 1/N^2 in place of 4/(N+1) + 2/N^2);
     and whether the variant coincides with another standard one-loop moment (F_1-type, F_3-type);
 (4) non-integer N: numerical Mellin transform vs analytic continuation S1 = psi(N+1)+gE, S2 = z2 - psi'(N+1);
 (5) large-N limit: CF[2 ln^2 Nbar + 3 ln Nbar - 9 - 2 z2] + O(ln N / N).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
from fractions import Fraction as Fr
import mpmath as mp
mp.mp.dps = 40
CF = Fr(4, 3)

def S(k, n): return sum(Fr(1, j**k) for j in range(1, n+1))
def S11(n): return sum(Fr(1, i)*S(1, i) for i in range(1, n+1))

def closed(n):
    s1, s2 = S(1, n), S(2, n)
    return CF*(2*s1**2 - 2*s2 + 3*s1 - 2*s1/(n*(n+1)) + Fr(3, n) + Fr(4, n+1) + Fr(2, n**2) - 9)

def variant(n):
    s1, s2 = S(1, n), S(2, n)
    return CF*(2*s1**2 - 2*s2 + 3*s1 - 2*s1/(n*(n+1)) + Fr(3, n) + Fr(2, n+1) + Fr(1, n**2) - 9)

def vvm_A3(n):
    f = lambda m: S11(m) + 2*S(1, m) - S(2, m)
    return CF*(9*(S(1, n) - 1) + 2*(f(n+1) + f(n-1)) - 7*(S(1, n-1) + S(1, n)))

def mellin_num(N):
    cf = mp.mpf(4)/3
    D1 = mp.quad(lambda t: mp.log(1-t)/(1-t)*(t**(N-1) - 1), [0, 0.5, 0.9, 1])
    D0 = mp.quad(lambda t: (t**(N-1) - 1)/(1-t), [0, 0.5, 0.9, 1])
    reg = mp.quad(lambda t: t**(N-1)*(-2*(1+t)*(mp.log(1-t) - mp.log(t)) - 4*mp.log(t)/(1-t) + 6 + 4*t), [0, 0.1, 0.5, 0.9, 1])
    return cf*(4*D1 - 3*D0 - (9 + 4*mp.zeta(2)) + reg)

print("(1) numerical Mellin moments of the x-space c(x) vs exact closed form")
worst = 0
for n in range(1, 13):
    num = mellin_num(mp.mpf(n)); cl = closed(n)
    d = abs(num - mp.mpf(cl.numerator)/cl.denominator); worst = max(worst, d)
    print(f"  N={n:2d}: closed/CF = {str(cl/CF):>22s}   |numeric - closed| = {mp.nstr(d, 3)}   variant/CF = {variant(n)/CF}")
print("  worst residual:", mp.nstr(worst, 3))

print("(2) VVM (A.3) vs closed form, exact rationals, N = 1..30:",
      all(vvm_A3(n) == closed(n) for n in range(1, 31)))

print("(3) N = 1:  closed =", closed(1), "   variant =", variant(1), "  (variant = -2 CF:", variant(1) == -2*CF, ")")
cL = lambda n: CF*Fr(4, n+1)                  # c_L^(1)(N) = 4CF/(N+1)  [c_L(x) = 4 CF x]
c3 = lambda n: closed(n) - CF*(Fr(2, n) + Fr(2, n+1))   # c_3 = c_2 - 2CF(1+x)
print("    variant == c_2 - c_L (2xF_1-type) for N=1..10?", all(variant(n) == closed(n) - cL(n) for n in range(1, 11)))
print("    variant == c_3 (F_3-type) for N=1..10?", all(variant(n) == c3(n) for n in range(1, 11)))
print("    c_2 - c_L at N=1:", closed(1) - cL(1), "(= -2 CF: Bjorken sum rule for F1, 1-(2/3)alpha_s/pi)", "  c_3 at N=1:", c3(1), "(= -3 CF: GLS, 1-alpha_s/pi)")
print("    closed - variant = CF[2/(N+1) + 1/N^2]; N=1..4:", [closed(n) - variant(n) for n in range(1, 5)])

def S1c(N): return mp.digamma(N+1) + mp.euler
def S2c(N): return mp.zeta(2) - mp.psi(1, N+1)
def closed_c(N):
    s1, s2 = S1c(N), S2c(N)
    return mp.mpf(4)/3*(2*s1**2 - 2*s2 + 3*s1 - 2*s1/(N*(N+1)) + 3/N + 4/(N+1) + 2/N**2 - 9)
print("(4) non-integer N:")
for N in ['0.7', '1.5', '2.25', '5.5', '13.3']:
    N = mp.mpf(N); a, b = mellin_num(N), closed_c(N)
    print(f"  N={mp.nstr(N,4)}: numeric {mp.nstr(a,20)}  closed {mp.nstr(b,20)}  diff {mp.nstr(a-b,3)}")
print("(5) large N: closed - CF[2 ln^2 Nbar + 3 ln Nbar - 9 - 2 z2]  (should -> 0 like ln N / N)")
for e in [3, 5, 7, 9]:
    N = mp.mpf(10)**e; Lb = mp.log(N) + mp.euler
    print(f"  N=1e{e}: {mp.nstr(closed_c(N) - mp.mpf(4)/3*(2*Lb**2 + 3*Lb - 9 - 2*mp.zeta(2)), 6)}")
