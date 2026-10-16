# Stage-2 check of E02, LFWF part, INCLUDING imaginary parts (i0 prescriptions), using the journal
# PRD 105 (2022) 076014 one-loop expressions: eq. (63) LFWF psi^pm, eq. (69) quasi-WF psi~^pm,
# eq. (72) S_r1 = -(as CF/pi) Lb, eq. (60) K = -(as CF/pi) Lb, eq. (76) h^(1) (matching kernel),
# and the factorization eq. (74):  psi~ S_r^{1/2} = H e^{c ln((-/+ zeta_z - i0)/zeta) K} psi.
# Units: a = as CF/(2 pi).  Logs of negative numbers: ln(-X + s i0) = ln X + s i pi (X>0).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
Lb, lmu, lz, lzb, lr, c = sp.symbols('L_b lnmu2 lnzz lnzzb lnr c', real=True)
I, pi = sp.I, sp.pi
def LN_neg(lnX, s):   # ln(-X + s*i0)
    return lnX + s*I*pi
for s in (+1, -1):
    # quasi-WF (69): ln(mu^2/(-sqrt(zz zzb) +/- i0)) and ln((-zz +/- i0)/mu^2)
    lsq_z = (lz+lzb)/2
    psit = (-Lb**2/2 + Lb*(sp.Rational(5,2) + lmu - LN_neg(lsq_z, s)) - sp.Rational(3,2) - pi**2/2
            + (-sp.Rational(1,4)*(LN_neg(lz, s)-lmu)**2 + sp.Rational(1,2)*(LN_neg(lz, s)-lmu))
            + (-sp.Rational(1,4)*(LN_neg(lzb, s)-lmu)**2 + sp.Rational(1,2)*(LN_neg(lzb, s)-lmu)))
    # LFWF (63): ln(mu^2/(+/- sqrt(zeta zetab) - i0)); zeta = zz/r, zetab = zzb/r
    lsq = lsq_z - lr
    ln_den = lsq if s == +1 else lsq - I*pi   # ln(+Y - i0)=lnY ; ln(-Y - i0) = lnY - i pi
    psi = -Lb**2/2 + Lb*(sp.Rational(3,2) + lmu - ln_den) + sp.Rational(1,2) - pi**2/12
    Sr = -2*Lb
    K = -2*Lb
    # printed exponent argument ln((-/+ zz - i0)/zeta): upper s=+1 -> ln(-zz - i0) = ln zz - i pi
    ln_arg_printed = (lz - I*pi if s == +1 else lz) - (lz - lr)
    # alternative prescription (-/+ zz + s i0)... i.e. ln((-zz + i0)/zeta) for upper
    ln_arg_alt = (lz + I*pi if s == +1 else lz) - (lz - lr)
    # matching kernel (76): h = as c1 + (as CF/4pi)[l + lb - (l^2+lb^2)/2], c1 = CF/(2pi)(-5pi^2/12 - 2)
    l, lbar = LN_neg(lz, s) - lmu, LN_neg(lzb, s) - lmu
    H = (-5*pi**2/12 - 2) + sp.Rational(1,2)*(l + lbar - (l**2 + lbar**2)/2)
    for name, larg in (('printed (-/+zz - i0)', ln_arg_printed), ('alternative (-zz + i0) for upper', ln_arg_alt)):
        res = sp.expand(psit + Sr/2 - (H + c*K*larg + psi))
        # collect Lb-dependent part
        resLb = sp.expand(res - res.subs(Lb, 0))
        sol_re = sp.solve(sp.Eq(sp.re(sp.expand(resLb.coeff(Lb)).subs({}) ), 0), c)
        print("sign %+d, exponent %s:" % (s, name))
        print("   Lb-dependent residual =", sp.simplify(resLb))
        print("   residual with c=1/2:  ", sp.simplify(sp.expand(res.subs(c, sp.Rational(1,2)))))
        print("   residual with c=1:    ", sp.simplify(sp.expand(resLb.subs(c, 1))))
