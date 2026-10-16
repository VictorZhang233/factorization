# W26 / Ch23 -- s07: one-loop check of the quasi-LFWF factorization including i0 prescriptions (prop:yzliu-lfwf (ii))
# Inputs: Ji-Liu, arXiv:2106.05310v1 (rendered pages 13-15): one-loop LFWF amplitude eq. (62), quasi-WF amplitude eq. (68),
# reduced soft function eq. (71), CS kernel eq. (59), matching kernel eq. (75)  [journal PRD 105 076014: eqs. (63),(69),(72),(60),(76)].
# Tested ansatz: psi~^+-  sqrt(S_r) = H^+- exp[ c ln((-/+ zeta_z + s i0)/zeta) K ] psi^+-   (c = 1/2 expected)
# Units a = alpha_s C_F/(2 pi); only the coefficients of delta(x-x0) matter (the [F]_+ parts agree on both sides).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

Lb, lmu, lz, lzb, lr, c = sp.symbols('L_b lnmu2 lnzetaz lnzetazb lnr c', real=True)   # lr = ln(zeta_z/zeta) = ln(zetab_z/zetab)
I, pi = sp.I, sp.pi
def ln_neg(lnX, s):          # ln(-X + s i0), X>0
    return lnX + s*I*pi

results = {}
for upper in (True, False):  # upper sign: psi^+, lower: psi^-
    sig = +1 if upper else -1
    # quasi-WF (68): L_b [5/2 + ln(mu^2/(-sqrt(zz zzb) +- i0))] - L_b^2/2 - 3/2 - pi^2/2 + [-1/4 l^2 + 1/2 l + (zb)], l = ln((-zz +- i0)/mu^2)
    lsq = (lz + lzb)/2
    l, lbar = ln_neg(lz, sig) - lmu, ln_neg(lzb, sig) - lmu
    psit = (-Lb**2/2 + Lb*(sp.Rational(5, 2) + lmu - ln_neg(lsq, sig)) - sp.Rational(3, 2) - pi**2/2
            + (-l**2/4 + l/2) + (-lbar**2/4 + lbar/2))
    # LFWF (62): L_b [3/2 + ln(mu^2/(+- sqrt(zeta zetab) - i0))] - L_b^2/2 + 1/2 - pi^2/12 ; sqrt(zeta zetab) = sqrt(zz zzb) e^{-lr}
    lsq_lc = lsq - lr
    ln_den = lsq_lc if upper else (lsq_lc - I*pi)      # ln(+Y - i0) = ln Y ; ln(-Y - i0) = ln Y - i pi
    psi = -Lb**2/2 + Lb*(sp.Rational(3, 2) + lmu - ln_den) + sp.Rational(1, 2) - pi**2/12
    Sr = -2*Lb; K = -2*Lb
    # matching kernel (75): h = c1 + (1/2)[l + lbar - (l^2 + lbar^2)/2] in units of a, c1 = -5pi^2/12 - 2
    H = -5*pi**2/12 - 2 + sp.Rational(1, 2)*(l + lbar - (l**2 + lbar**2)/2)
    for s in (+1, -1):
        # exponent argument ln((-/+ zz + s i0)/zeta): upper -> -zz, lower -> +zz (positive, i0 irrelevant)
        larg = (ln_neg(lz, s) if upper else lz) - (lz - lr)
        res = sp.expand(psit + Sr/2 - (H + c*K*larg + psi))
        results[(upper, s)] = (sp.simplify(res.subs(c, sp.Rational(1, 2))), sp.simplify(sp.expand(res - res.subs(Lb, 0)).subs(c, 1)))
        print('%s, exponent with %+d i0:  residual(c=1/2) = %s ;  L_b-part of residual(c=1) = %s'
              % ('psi^+' if upper else 'psi^-', s, results[(upper, s)][0], results[(upper, s)][1]))
assert results[(True, +1)][0] == 0 and results[(False, +1)][0] == 0 and results[(False, -1)][0] == 0
assert results[(True, -1)][0] != 0
print('PASS: consistent form  psi~^+- sqrt(S_r) = H^+- exp[(1/2) ln((-/+ zeta_z + i0)/zeta) K] psi^+-  (cf. Liu-Su JHEP 02 (2024) 204, eq. (4.4));')
print('      the printed (-/+ zeta_z - i0) leaves -2 i pi a L_b for psi^+ (b-dependent, cannot be absorbed into H).')
