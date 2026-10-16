#!/usr/bin/env python3
"""W24 / Ch21 -- large-beta0 Adler function: closed form, normalization, poles, checks.

Conventions of the book (WRITER_SPEC_v2 Sec.3, def:power-borel):
  mu^2 d alpha_s/d mu^2 = -beta0/(4 pi) alpha_s^2,   beta0 = 11/3 C_A - 4/3 T_F n_f
  R = sum_n r_n alpha_s^{n+1},  B[R](t) = sum_n r_n t^n/n!,  u = beta0 t/(4 pi)
  D(Q^2)/R_0 = 1 + sum_n r_n alpha_s^{n+1}   (Adler function, D = -12 pi^2 Q^2 dPi/dQ^2)

Large-beta0 normalisation used in the text (Beneke 1999, eq. (5.9),(5.10), converted):
  D/R_0 = 1 + (3 C_F/4)(alpha_s/pi) sum_n d_n (beta0 alpha_s/(4 pi))^n
  => r_n = (3 C_F/(4 pi)) d_n (beta0/(4 pi))^n,   B[D](t) = (3 C_F/(4 pi)) Bhat(u),
  Bhat(u) = sum_n d_n u^n/n! = 32/(3(2-u)) (mu^2 e^{5/3}/Q^2)^u S(u),
  S(u) = sum_{k>=2} (-1)^k k / (k^2-(1-u)^2)^2.

Checks:
 (1) Bhat(0)=1, S(0)=3/16 exactly.
 (2) d_1 = 11/2 - 4 zeta3 exactly  <=>  sum_{k>=2} (-1)^k k/(k^2-1)^3 = (6 zeta3 - 5)/32;
     equals the n_f term of the two-loop R ratio (VF-EE-10) after naive non-abelianization.
 (3) d_2 = 302/9 - 76/3 zeta3  <=> n_f^2 term of the O(a^3) Adler coefficient 151/162-19/27 zeta3 (SU(3)).
 (4) d_0..d_8 against Beneke 1999 Table 4.
 (5) Laurent expansions at u=2 (simple pole, residue -2e^{10/3}), u=-1 (double), u=-2, u=3 (double); regular at u=1.
 (6) Beneke 1999 eq. (5.11) leading-pole decomposition and Table 5.
 (7) small-/large-khat behaviour of F <-> poles (consistency with Beneke eqs. (2.20),(2.21)).
 (8) soft gluon condensate check: 3 C_F/(2 pi) = (2 pi^2/N_c) * 3 N_c C_F/(4 pi^3).
 (9) ambiguity of the Borel integral from u=2 (mu independence) and numbers of Beneke (5.12).
 (10) symmetry Bhat(u)/u * (mu^2 e^{5/3}/Q^2)^{-u} invariant under u -> 2-u.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import sympy as sp

mp.mp.dps = 50
OK = True
def check(name, cond):
    global OK
    print(("PASS " if cond else "FAIL ") + name)
    OK = OK and cond

def S_direct(u):
    a = 1 - mp.mpmathify(u)
    return mp.nsum(lambda k: (-1)**int(k) * k / (k**2 - a**2)**2, [2, mp.inf])

def S(u):
    """closed form via trigamma: k/(k^2-a^2)^2 = [1/(k-a)^2 - 1/(k+a)^2]/(4a),
    sum_{j>=0} (-1)^j/(j+c)^2 = [psi1(c/2) - psi1((c+1)/2)]/4, a = 1-u"""
    u = mp.mpmathify(u)
    if abs(u - 1) < mp.mpf(10)**(-mp.mp.dps//3):
        return S_direct(u)
    p1 = lambda z: mp.psi(1, z)
    return (p1((1+u)/2) - p1((2+u)/2) - p1((3-u)/2) + p1((4-u)/2))/(16*(1-u))

def Bhat(u, L=0):
    """L = ln(mu^2/Q^2); MSbar scheme constant 5/3"""
    u = mp.mpmathify(u)
    return mp.mpf(32)/(3*(2-u)) * mp.e**((mp.mpf(5)/3 + L)*u) * S(u)

# (0) closed form of S vs direct sum
check("trigamma closed form of S(u) = direct sum (u=0.37, -0.61, 2.4+0.3i)",
      all(abs(S(x)-S_direct(x)) < mp.mpf(10)**-40 for x in [mp.mpf('0.37'), mp.mpf('-0.61'), mp.mpf('2.4')+mp.mpf('0.3')*1j]))
# (1)
check("S(0) = 3/16", abs(S(0) - mp.mpf(3)/16) < mp.mpf(10)**-45)
check("Bhat(0) = 1", abs(Bhat(0) - 1) < mp.mpf(10)**-45)

# (2) exact d_1
z3 = mp.zeta(3)
T3 = mp.nsum(lambda k: (-1)**int(k)*k/(k**2-1)**3, [2, mp.inf])
check("sum_{k>=2}(-1)^k k/(k^2-1)^3 = (6 zeta3 - 5)/32", abs(T3 - (6*z3-5)/32) < mp.mpf(10)**-45)
taylor = mp.taylor(lambda u: Bhat(u), 0, 8)
d = [taylor[n]*mp.factorial(n) for n in range(9)]
check("d_1 = 11/2 - 4 zeta3", abs(d[1] - (mp.mpf(11)/2 - 4*z3)) < mp.mpf(10)**-30)
# two-loop n_f term (VF-EE-10): R/R0 contains a^2 * ( - C_F T_F n_f (11/8 - zeta3) ); T_F n_f -> -3 beta0/4
CF, b0, TFnf = sp.symbols('C_F beta0 TFnf')
coef_a2_from_VF = sp.expand((-CF*TFnf*(sp.Rational(11, 8) - sp.zeta(3))).subs(TFnf, -sp.Rational(3, 4)*b0))
coef_a2_from_d1 = sp.expand(sp.Rational(3, 4)*CF*(sp.Rational(11, 2) - 4*sp.zeta(3))*b0/4)
check("a^2 coefficient: (3C_F/4) d_1 beta0/4 = NNA of VF-EE-10 n_f term", sp.simplify(coef_a2_from_VF - coef_a2_from_d1) == 0)

# (3) d_2
d2_exact = mp.mpf(302)/9 - mp.mpf(76)/3*z3
check("d_2 = 302/9 - 76/3 zeta3 (n_f^2 term 151/162-19/27 zeta3 of the a^3 Adler coefficient)", abs(d[2] - d2_exact) < mp.mpf(10)**-25)
# relation: a^3 coefficient (3C_F/4) d_2 (beta0/4)^2, n_f^2 part with beta0 = 11 - 2n_f/3, C_F = 4/3
nf = sp.symbols('n_f')
a3_nf2 = sp.expand(sp.Rational(3, 4)*sp.Rational(4, 3)*(sp.Rational(302, 9) - sp.Rational(76, 3)*sp.zeta(3))*((11 - sp.Rational(2, 3)*nf)/4)**2).coeff(nf, 2)
check("n_f^2 coefficient = 151/162 - 19/27 zeta3", sp.simplify(a3_nf2 - (sp.Rational(151, 162) - sp.Rational(19, 27)*sp.zeta(3))) == 0)
print("   n_f^2 coefficient numerically:", sp.N(a3_nf2, 10))

# (4) Beneke Table 4
tab4 = [1, 0.6918, 3.1035, 2.1800, 30.740, -34.534, 759.74, -3691.4, 42251]
for n in range(9):
    print(f"   d_{n} = {mp.nstr(d[n], 12):>22s}   Beneke Table 4: {tab4[n]}")
check("d_0..d_8 agree with Beneke 1999 Table 4 (4-5 significant digits)",
      all(abs(float(d[n]) - tab4[n]) <= 0.6e-4*max(1, abs(tab4[n])) + 1e-4 for n in range(9)))

# (5) Laurent expansions
def laurent(u0, order=2, eps=mp.mpf('1e-12')):
    # coefficients c_{-2}, c_{-1} via contour integrals around u0
    r = mp.mpf('0.25')
    f = lambda th: Bhat(u0 + r*mp.e**(1j*th))
    cm1 = mp.quad(lambda th: f(th)*r*mp.e**(1j*th), [0, 2*mp.pi])/(2*mp.pi)
    cm2 = mp.quad(lambda th: f(th)*(r*mp.e**(1j*th))**2, [0, 2*mp.pi])/(2*mp.pi)
    cm3 = mp.quad(lambda th: f(th)*(r*mp.e**(1j*th))**3, [0, 2*mp.pi])/(2*mp.pi)
    return cm3, cm2, cm1
mp.mp.dps = 30
for u0 in [2, 3, 4, -1, -2, -3, 1]:
    cm3, cm2, cm1 = laurent(u0)
    print(f"   u0={u0:>2d}: c_-3={mp.nstr(cm3.real,10):>14s} c_-2={mp.nstr(cm2.real,12):>16s}  c_-1={mp.nstr(cm1.real,12):>16s}")
cm3, cm2, cm1 = laurent(2)
check("u=2 simple pole, residue -2 e^{10/3} [i.e. 2e^{10/3}/(2-u)]", abs(cm2) < 1e-15 and abs(cm1 + 2*mp.e**(mp.mpf(10)/3)) < 1e-15)
cm3, cm2, cm1 = laurent(1)
check("u=1: no pole", abs(cm2) < 1e-15 and abs(cm1) < 1e-15)
print("   Bhat(1) =", mp.nstr(Bhat(1), 15), "; (32/3) e^{5/3} (1 - 3 zeta3/4) =", mp.nstr(mp.mpf(32)/3*mp.e**(mp.mpf(5)/3)*(1-3*mp.zeta(3)/4), 15))
check("Bhat(1) = (32/3) e^{5/3} (1 - 3zeta3/4)", abs(Bhat(1) - mp.mpf(32)/3*mp.e**(mp.mpf(5)/3)*(1-3*mp.zeta(3)/4)) < 1e-20)
cm3, cm2, cm1 = laurent(-1)
check("u=-1 double pole: (4/9)e^{-5/3}/(1+u)^2 + (10/9)e^{-5/3}/(1+u)",
      abs(cm2 - mp.mpf(4)/9*mp.e**(-mp.mpf(5)/3)) < 1e-15 and abs(cm1 - mp.mpf(10)/9*mp.e**(-mp.mpf(5)/3)) < 1e-15)
cm3, cm2, cm1 = laurent(-2)
check("u=-2 double pole: -(2/9)e^{-10/3}/(2+u)^2 - (1/2)e^{-10/3}/(2+u)",
      abs(cm2 + mp.mpf(2)/9*mp.e**(-mp.mpf(10)/3)) < 1e-15 and abs(cm1 + mp.mpf(1)/2*mp.e**(-mp.mpf(10)/3)) < 1e-15)
cm3, cm2, cm1 = laurent(3)
print("   u=3: double-pole coefficient c_-2 =", mp.nstr(cm2.real, 15), "  compare analytic (32/3)e^5 * (1/(2-3)) * (+1)/(4*2)*... ")
# analytic: near u=1+k (k>=2): k/(k^2-a^2)^2 with a=1-u -> a = -k + delta, delta = -(u-(1+k)):  k/((k-a)^2 (k+a)^2) ~ k/((2k)^2 delta^2) = 1/(4k delta^2)
# => S ~ (-1)^k/(4k (u-1-k)^2); Bhat ~ 32/(3(1-k)) e^{5(1+k)/3} (-1)^k/(4k) /(u-1-k)^2 at leading order
for k in [2, 3]:
    u0 = 1 + k
    lead = mp.mpf(32)/(3*(2-u0))*mp.e**(mp.mpf(5)*u0/3)*(-1)**k/(4*k)
    cm3, cm2, cm1 = laurent(u0)
    check(f"u={u0} double pole leading coefficient = 32/(3(2-u0)) e^(5u0/3) (-1)^k/(4k)", abs(cm2 - lead) < 1e-12*abs(lead))
for k in [2, 3]:
    u0 = 1 - k
    lead = mp.mpf(32)/(3*(2-u0))*mp.e**(mp.mpf(5)*u0/3)*(-1)**k/(4*k)
    cm3, cm2, cm1 = laurent(u0)
    check(f"u={u0} double pole leading coefficient = 32/(3(2-u0)) e^(5u0/3) (-1)^k/(4k)", abs(cm2 - lead) < 1e-12*abs(lead))

# (6) leading-pole contributions to d_n (Beneke Table 5)
mp.mp.dps = 30
e = mp.e
def contrib_UVm1(n):  # e^{-5/3}{4/9/(1+u)^2 + 10/9/(1+u)}
    return mp.factorial(n)*e**(-mp.mpf(5)/3)*((-1)**n*(n+1)*mp.mpf(4)/9 + (-1)**n*mp.mpf(10)/9)
def contrib_IR2(n):   # 2 e^{10/3}/(2-u) = e^{10/3} sum (u/2)^n
    return mp.factorial(n)*e**(mp.mpf(10)/3)/mp.mpf(2)**n
def contrib_UVm2(n):  # e^{-10/3}{-2/9/(2+u)^2 - 1/2/(2+u)}
    # 1/(2+u) = 1/2 sum (-u/2)^n ; 1/(2+u)^2 = 1/4 sum (n+1)(-u/2)^n
    return mp.factorial(n)*e**(-mp.mpf(10)/3)*(-mp.mpf(2)/9*(n+1)*(-1)**n/mp.mpf(4)/mp.mpf(2)**n - mp.mpf(1)/2*(-1)**n/mp.mpf(2)/mp.mpf(2)**n)
tab5_UV1 = [0.294, -0.378, 0.923, -3.27, 15.1, -85.6, 574, -4442, 38923]
tab5_IR2 = [28.03, 14.02, 14.02, 21.02, 42.05, 105.1, 315.4, 1104, 4415]
tab5_UV2 = [-0.011, 0.006, -0.007, 0.013, -0.028, 0.078, -0.256, 0.975, -4.214]
okt5 = True
for n in range(9):
    a, b, c = contrib_UVm1(n), contrib_IR2(n), contrib_UVm2(n)
    print(f"   n={n}: UV(-1)={mp.nstr(a,6):>10s} [{tab5_UV1[n]}]  IR(2)={mp.nstr(b,6):>10s} [{tab5_IR2[n]}]  UV(-2)={mp.nstr(c,5):>10s} [{tab5_UV2[n]}]")
    okt5 &= abs(float(a)-tab5_UV1[n]) <= 0.006*max(1, abs(tab5_UV1[n]))
    okt5 &= abs(float(b)-tab5_IR2[n]) <= 0.006*max(1, abs(tab5_IR2[n]))
    okt5 &= abs(float(c)-tab5_UV2[n]) <= 0.002
check("leading-pole contributions reproduce Beneke 1999 Table 5 (UV(-1), IR(2), UV(-2))", okt5)

# (7) small/large khat <-> poles.  B = (3C_F/4pi)^{-1} Int dkh2/kh2 F(kh2) (kh2 e^{-5/3})^{-u}, mu=Q
#   small: F ~ (3C_F/(2pi)) kh^4  -> (3C_F/2pi)/(3C_F/4pi) e^{5u/3}/(2-u) = 2 e^{10/3}/(2-u) + regular
#   large: F ~ (C_F/(3pi)) (ln kh2 + 5/6)/kh2 -> (4/9) e^{5u/3} [1/(1+u)^2 + (5/6)/(1+u)] near u=-1
u = sp.symbols('u')
small = sp.Rational(3, 2)/sp.Rational(3, 4)  # (3C_F/2pi)/(3C_F/4pi)
check("small-khat coefficient 3C_F/(2pi) <-> residue 2 e^{10/3}", small == 2)
large = sp.Rational(1, 3)/sp.Rational(3, 4)   # (C_F/3pi)/(3C_F/4pi) = 4/9
ser = sp.series(large*sp.exp(sp.Rational(5, 3)*u)*(1/(1+u)**2 + sp.Rational(5, 6)/(1+u)), u, -1, 1).removeO()
c2 = sp.simplify(sp.limit(ser*(1+u)**2, u, -1))
c1 = sp.simplify(sp.limit(sp.diff(ser*(1+u)**2, u), u, -1))
check("large-khat (C_F/3pi)(ln kh2+5/6)/kh2 <-> e^{-5/3}{(4/9)/(1+u)^2+(10/9)/(1+u)}",
      sp.simplify(c2 - sp.Rational(4, 9)*sp.exp(-sp.Rational(5, 3))) == 0 and sp.simplify(c1 - sp.Rational(10, 9)*sp.exp(-sp.Rational(5, 3))) == 0)

# (8) soft condensate: <G^a G^a>_soft = 2(N^2-1)*3*Int d^4k/(2pi)^4 = 3(N^2-1)/(8 pi^2) Int dk2 k2
Nc, aS, CF_ = sp.symbols('N_c alpha_s C_F', positive=True)
G2soft_density = 3*(2*Nc*CF_)/(8*sp.pi**2)          # coefficient of Int dk^2 k^2 ; N^2-1 = 2 N C_F
aG2 = aS/sp.pi*G2soft_density
cond_term = (2*sp.pi**2/Nc)*aG2                       # D/R_0 contains (2pi^2/N_c) <(alpha_s/pi) G^2>/Q^4
skel_term = aS*sp.Rational(3, 2)*CF_/sp.pi             # alpha_s * Int dkh2/kh2 F, F=(3C_F/2pi) kh^4 -> alpha_s (3C_F/2pi) Int dk2 k2 /Q^4
check("soft condensate: (2pi^2/N_c)(alpha_s/pi)<G^2>_soft = alpha_s (3C_F/2pi) Int dk^2 k^2/Q^4", sp.simplify(cond_term - skel_term) == 0)

# (9) ambiguity of the Borel integral from the u=2 pole: D/R0-1 = (4pi/beta0) Int du e^{-4pi u/(beta0 alpha(mu))} B(u)
#   B(u) ~ (3C_F/4pi) * 2 e^{10/3} (mu^2/Q^2)^2 /(2-u)  ; Im part = pi*residue*(4pi/beta0)
LamQ = sp.symbols('Lambda_over_Q', positive=True)
Im_part = sp.pi*(4*sp.pi/b0)*(3*CF/(4*sp.pi))*2*sp.exp(sp.Rational(10, 3))*LamQ**4
print("   Im(Borel integral) from u=2:", sp.simplify(Im_part), "  ; /pi ->", sp.simplify(Im_part/sp.pi))
val = (Im_part/sp.pi).subs({CF: sp.Rational(4, 3), b0: 9})
Lam = 0.215
num = float(val.subs(LamQ, 1))*Lam**4
print(f"   n_f=3, Lambda=0.215 GeV (one loop, Beneke 1999 fn.42): Im/pi = {num:.4f} GeV^4/Q^4  (Beneke (5.12): ~0.06)")
check("ambiguity estimate ~0.05-0.06 GeV^4/Q^4 as in Beneke (5.12)", 0.045 < num < 0.065)
# mu independence: e^{-4pi u/(beta0 alpha(mu))} (mu^2)^u = e^{-4 pi u/(beta0 alpha(Q))} (Q^2)^u
amu, Q2, mu2 = sp.symbols('a_mu Q2 mu2', positive=True)
aQ = amu/(1 + b0*amu/(4*sp.pi)*sp.log(Q2/mu2))
lhs = sp.exp(-4*sp.pi*u/(b0*amu))*mu2**u
rhs = sp.exp(-4*sp.pi*u/(b0*aQ))*Q2**u
# (log of both sides, expanded with positive symbols; the earlier .equals() call returned None -> spurious FAIL)
diff_log = sp.expand(-4*sp.pi*u/(b0*amu) + u*sp.log(mu2) - (-4*sp.pi*u/(b0*aQ) + u*sp.log(Q2)))
check("one-loop: e^{-4pi u/(beta0 a(mu))} mu^{2u} = e^{-4pi u/(beta0 a(Q))} Q^{2u}", sp.simplify(diff_log) == 0)

# (10) symmetry
mp.mp.dps = 30
def Bpi(u):  # Bhat(u)/u without the exponential factor
    return Bhat(u, L=0)/mp.e**(mp.mpf(5)/3*u)/u
okS = all(abs(Bpi(1+x) - Bpi(1-x)) < 1e-20 for x in [mp.mpf('0.3'), mp.mpf('0.77'), mp.mpf('1.5')+mp.mpf('0.2')*1j])
check("Bhat(u) e^{-5u/3}/u symmetric under u -> 2-u", okS)

# extra: d_n table in the r_n normalisation for n_f = 3,5 at mu = Q (for the worked example)
for nfv in [3, 5]:
    b0v = 11 - mp.mpf(2)/3*nfv
    print(f"   n_f={nfv}: beta0={mp.nstr(b0v,5)};  r_n alpha^(n+1) series coefficients a^(n+1) [a=alpha_s/pi]:")
    for n in range(9):
        cn = mp.mpf(3)/4*mp.mpf(4)/3*d[n]*(b0v/4)**n   # coefficient of a^{n+1} in D/R0 (C_F=4/3)
        print(f"      n={n}: coefficient of a^{n+1} = {mp.nstr(cn, 8)}")

print("ALL PASS" if OK else "SOME CHECKS FAILED")
