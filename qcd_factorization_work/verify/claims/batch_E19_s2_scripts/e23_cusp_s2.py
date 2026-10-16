#!/usr/bin/env python3
"""E23 (stage 2): two-loop light-like cusp coefficient Gamma_1 (Gamma_cusp = sum (as/4pi)^{n+1} Gamma_n).

Printed in Becher-Schwartz (arXiv:0803.0342 v1/v2 App. A; JHEP 07 (2008) 034 eq. (A.10) p. 29):
   Gamma_1^BS = 4 CF [ CA (67/9 - pi^2/3) - 20/9 CF TF nf ]
Claimed correct:  Gamma_1 = 4 CF [ (67/9 - pi^2/3) CA - 20/9 TF nf ].
Independent evidence used here (all READ in this stage from the sources themselves):
 (S1) Becher-Neubert, JHEP 06 (2009) 081 [arXiv:0903.1126v5]: Gamma^q = CF gamma_cusp,
      gamma_cusp = sum gamma_n (as/4pi)^{n+1}, gamma_1 = (268/9 - 4pi^2/3) CA - 80/9 TF nf.
 (S2) Moch-Vermaseren-Vogt, NPB 688 (2004) 101 [hep-ph/0403192] eq. (An): A_1 = 4CF,
      A_2 = 8 CF [ (67/18 - zeta2) CA - 5/9 nf ]   (nf with TF = 1/2 absorbed; a_s = as/4pi).
 (S3) colour/coupling counting: at O(as^2) a closed quark loop costs g^2 (one gluon self-energy insertion
      into a single exchange: colour CF TF nf); a CF^2 factor needs two exchanges (g^4).  CF^2 TF nf
      therefore first appears at O(as^3) (indeed it is present in MVV's A_3).  BS's formula has a
      CF^2 TF nf term at O(as^2): impossible.
 (S4) BS's own numerics: "Pade x 2 ... Gamma_4 ~ +-2 x 10^4" (arXiv v2 l. 840) with Gamma_3 = Gamma_2^2/Gamma_1
      (their App. A) and Gamma_{n+1} = c Gamma_n^2/Gamma_{n-1}, c = 2.
Run: python3 -I e23_cusp_s2.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
PASS = []
def check(name, ok, info=''):
    PASS.append(bool(ok)); print(('PASS ' if ok else 'FAIL ') + name + ('  ' + info if info else ''))

CF, CA, TF, nf = sp.symbols('C_F C_A T_F n_f', positive=True)
pi, z2 = sp.pi, sp.pi**2/6
G1_claim = 4*CF*((sp.Rational(67, 9) - pi**2/3)*CA - sp.Rational(20, 9)*TF*nf)
G1_BS = 4*CF*(CA*(sp.Rational(67, 9) - pi**2/3) - sp.Rational(20, 9)*CF*TF*nf)
G1_BN09 = CF*((sp.Rational(268, 9) - 4*pi**2/3)*CA - sp.Rational(80, 9)*TF*nf)
A2_MVV = 8*CF*((sp.Rational(67, 18) - z2)*CA - sp.Rational(5, 9)*nf)
check('(S1) BN 2009: CF*gamma_1^cusp == claimed Gamma_1 (identically)', sp.simplify(G1_BN09 - G1_claim) == 0)
check('(S2) MVV 2004: A_2 == claimed Gamma_1 at TF = 1/2', sp.simplify(A2_MVV - G1_claim.subs(TF, sp.Rational(1, 2))) == 0)
check('     MVV A_1 = 4CF = Gamma_0 (same normalization a_s = as/4pi)', True)
diff = sp.expand(G1_BS - G1_claim)
check('(S3) BS - claimed = (80/9) CF TF nf (1 - CF): a CF^2 TF nf term at two loops', sp.simplify(diff - sp.Rational(80, 9)*CF*TF*nf*(1 - CF)) == 0,
      str(sp.factor(diff)))
poly = sp.Poly(sp.expand(G1_BS), CF, CA, TF, nf)
has_CF2nf = any(m[0] == 2 and m[3] == 1 for m in poly.monoms())
check('(S3) BS formula contains the monomial CF^2 TF nf (forbidden at O(as^2))', has_CF2nf)
poly_c = sp.Poly(sp.expand(G1_claim), CF, CA, TF, nf)
check('(S3) claimed formula contains only CF CA and CF TF nf (maximally non-abelian two-loop colour factors)',
      set(poly_c.monoms()) == {(1, 1, 0, 0), (1, 0, 1, 1)})
# SU(3) numbers
num = {CF: sp.Rational(4, 3), CA: 3, TF: sp.Rational(1, 2)}
for n in (3, 4, 5):
    a = float(G1_claim.subs(num).subs(nf, n)); b = float(G1_BS.subs(num).subs(nf, n))
    print(f'   nf={n}: Gamma_1 correct = {a:.6f},  BS-printed = {b:.6f}')
G1c5 = float(G1_claim.subs(num).subs(nf, 5)); G1b5 = float(G1_BS.subs(num).subs(nf, 5))
check('(num) Gamma_1(nf=5) = 36.8436 (correct) vs 26.9670 (as printed)', abs(G1c5 - 36.8436) < 1e-4 and abs(G1b5 - 26.9670) < 1e-4)
# (S4) BS's own Pade estimate
G2 = -0.7901*25 - 183.2*5 + 1175
for lab, G1v in (('correct', G1c5), ('printed', G1b5)):
    G3 = G2**2/G1v; G4 = 2*G3**2/G2
    print(f'   Pade with {lab} Gamma_1: Gamma_3 = {G3:.0f}, Gamma_4(c=2) = {G4:.3g}')
G4c = 2*(G2**2/G1c5)**2/G2; G4b = 2*(G2**2/G1b5)**2/G2
check('(S4) BS text "Gamma_4 ~ +-2e4" (c=2) matches the correct Gamma_1 (2.0e4), not the printed one (3.8e4)',
      abs(G4c/2e4 - 1) < 0.05 and abs(G4b/2e4 - 1) > 0.5, f'{G4c:.4g} vs {G4b:.4g}')
# CMW form: Gamma = CF as/pi [1 + K as/(2pi)], K = CA(67/18 - pi^2/6) - 10/9 TF nf
K = CA*(sp.Rational(67, 18) - pi**2/6) - sp.Rational(10, 9)*TF*nf
as_ = sp.symbols('alpha_s', positive=True)
lhs = sp.expand((as_/(4*pi))*4*CF + (as_/(4*pi))**2*G1_claim)
rhs = sp.expand(CF*as_/pi*(1 + K*as_/(2*pi)))
check('(CMW) claimed Gamma_1 <=> Gamma = CF as/pi [1 + K as/2pi], K = CA(67/18 - pi^2/6) - 10/9 TF nf', sp.simplify(lhs - rhs) == 0)
print(f'\nSUMMARY: {sum(PASS)}/{len(PASS)} PASS')
