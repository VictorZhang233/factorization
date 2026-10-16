"""W12 (Ch10) -- prop:disall-scale and prop:disall-dis-scheme in Mellin space (symbolic).

 1. mu_F and mu_R dependence of the O(a)-truncated F_2 (a = alpha_s/2pi), VF-DIS-10.
 2. DIS scheme: F_2 = sum e^2 (q+qbar)^DIS + O(a^2) with C^DIS = L P; momentum sum rule exactly preserved
    for every N; C_L unchanged; NLO kernels P'^(1) = P^(1) + Z P^(0) - P^(0) Z - (beta0/2) Z (matrices),
    non-singlet P'^(1)_NS = P^(1)_NS - (beta0/2) C_2^q  (VF-DIS-11).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

a, b0, L = sp.symbols('a beta0 L')
Sig, g = sp.symbols('Sigma_N g_N')          # moments of (q+qbar) of one flavour and of g
C2q, C2g, CLq, CLg = sp.symbols('C2q C2g CLq CLg')
Pqq, Pqg, Pgq, Pgg = sp.symbols('Pqq Pqg Pgq Pgg')
lnmu = sp.Symbol('lnmu2')

print('1. scale dependence')
# F_N(mu) = Sig + a [ (C2q + L Pqq) Sig + 2 (C2g + L Pqg) g ],  L = ln Q^2 - lnmu
F = Sig + a * ((C2q + L * Pqq) * Sig + 2 * (C2g + L * Pqg) * g)
dSig = a * (Pqq * Sig + 2 * Pqg * g)     # d/dln mu^2 at O(a)
dg = a * (Pgq * Sig + Pgg * g)
da = -b0 / 2 * a ** 2
dL = -1
dF = sp.diff(F, Sig) * dSig + sp.diff(F, g) * dg + sp.diff(F, a) * da + sp.diff(F, L) * dL
dF = sp.expand(dF)
print('   dF/dln mu^2 at O(a)   :', sp.simplify(dF.coeff(a, 1)), '(must be 0)')
print('   O(a^2) remainder      :', sp.factor(dF.coeff(a, 2)))
# separate mu_R: only through a(mu_R) in the O(a) term
FR = Sig + a * ((C2q + L * Pqq) * Sig + 2 * (C2g + L * Pqg) * g)
dFR = sp.expand(sp.diff(FR, a) * da)
print('   dF/dln mu_R^2         :', sp.factor(dFR), '  = -(beta0/2) a^2 [C2q Sig + 2 C2g g] at L=0:',
      sp.simplify(dFR.subs(L, 0) + b0 / 2 * a ** 2 * (C2q * Sig + 2 * C2g * g)) == 0)
FLN = a * (CLq * Sig + 2 * CLg * g)
dFL = sp.expand(sp.diff(FLN, Sig) * dSig + sp.diff(FLN, g) * dg + sp.diff(FLN, a) * da)
print('   dF_L/dln mu^2 at O(a) :', dFL.coeff(a, 1), ' (F_L mu independent at O(a))')

print('2. DIS scheme')
nf = sp.Symbol('n_f', positive=True)
# flavour-singlet bookkeeping: Sigma = sum_i (q_i+qbar_i);  q_i^DIS = q_i + a [C2q q_i + C2g g]
SigT, gT = sp.symbols('SigmaTot gTot')
SigD = SigT + a * (C2q * SigT + 2 * nf * C2g * gT)
gD = gT - a * (C2q * SigT + 2 * nf * C2g * gT)
print('   momentum sum (any N): Sigma^DIS + g^DIS - (Sigma + g) =', sp.simplify(SigD + gD - SigT - gT))
# F_2 of one flavour in the DIS scheme: (q+qbar)^DIS = (q+qbar) + a[C2q (q+qbar) + 2 C2g g]
qqD = Sig + a * (C2q * Sig + 2 * C2g * g)
F_DIS = qqD + a * L * (Pqq * Sig + 2 * Pqg * g)      # claimed DIS-scheme form, with PDFs re-expressed
diff = sp.expand(F - F_DIS)
print('   F_2 (MSbar) - [ (q+qbar)^DIS + a L (Pqq ... ) ] =', sp.simplify(diff), '  -> C_2^DIS = L P')
print('   C_L unchanged at O(a): the O(a) term of F_L contains no PDF change at this order (shift is O(a^2)).')
# NLO kernel transformation, matrices in the (Sigma, g) basis
P0 = sp.Matrix(2, 2, sp.symbols('p0_11 p0_12 p0_21 p0_22'))
P1 = sp.Matrix(2, 2, sp.symbols('p1_11 p1_12 p1_21 p1_22'))
Z = sp.Matrix([[C2q, 2 * nf * C2g], [-C2q, -2 * nf * C2g]])
fvec = sp.Matrix(sp.symbols('fS fG'))
# df/dln mu^2 = (a P0 + a^2 P1) f ;  f' = (1 + a Z) f
fp = (sp.eye(2) + a * Z) * fvec
dfp = (sp.eye(2) + a * Z) * (a * P0 + a ** 2 * P1) * fvec + da * Z * fvec
finv = (sp.eye(2) - a * Z + a ** 2 * Z * Z) * sp.Matrix(sp.symbols('gS gG'))   # f in terms of f' (to O(a^2))
dfp_in_fp = sp.expand(dfp.subs({fvec[0]: finv[0], fvec[1]: finv[1]}))
Pp1 = P1 + Z * P0 - P0 * Z - b0 / 2 * Z
expect = sp.expand(a * P0 * sp.Matrix(sp.symbols('gS gG')) + a ** 2 * Pp1 * sp.Matrix(sp.symbols('gS gG')))
res = sp.simplify((dfp_in_fp - expect).applyfunc(lambda e: sp.expand(e).coeff(a, 1) + sp.expand(e).coeff(a, 2)))
print('   P\'^(1) = P^(1) + Z P^(0) - P^(0) Z - (beta0/2) Z  :', res == sp.zeros(2, 1))
# non-singlet: scalars commute
p0ns, p1ns = sp.symbols('p0ns p1ns')
print('   non-singlet: P\'^(1)_NS - P^(1)_NS =', sp.simplify((p1ns + C2q * p0ns - p0ns * C2q - b0 / 2 * C2q) - p1ns))
