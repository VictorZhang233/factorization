# W26 / Ch23 -- s04: two-loop logarithmic structure of ln S_I from mu^2 dlnS_I/dmu^2 = gamma_HH
# (prop:yzliu-sI-twoloop, ex:yzliu-sI-rge; VF-YZL-3).  Book conventions: mu^2 d alpha/dmu^2 = -(beta0/4pi) alpha^2,
# beta0 = 11/3 C_A - 4/3 T_F n_f ; L_b = ln(mu^2 b^2/b0^2), mu^2 dL_b/dmu^2 = 1.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp, mpmath as mp

al, Lb, CF, CA, nf, TF, b0, c, gh, c2 = sp.symbols('alpha L_b C_F C_A n_f T_F beta0 c gammahat c2')
lnSI = -al*CF/sp.pi*Lb + al**2*(c*Lb**2 + gh*Lb + c2)
dlnSI = sp.diff(lnSI, al)*(-b0/(4*sp.pi)*al**2) + sp.diff(lnSI, Lb)
ghat_HH = CF/sp.pi**2*(CA*(-sp.Rational(49, 36) + sp.pi**2/12 - sp.zeta(3)/2) + sp.Rational(5, 9)*TF*nf)
gammaHH = -al*CF/sp.pi + al**2*ghat_HH
eq = sp.expand(dlnSI - gammaHH)
sol = sp.solve([eq.coeff(al, 2).coeff(Lb, 1), eq.coeff(al, 2).coeff(Lb, 0)], [c, gh], dict=True)[0]
print('L_b^2 coefficient c =', sp.simplify(sol[c]), ' ; single log =', sp.simplify(sol[gh] - ghat_HH), '+ ghat_HH')
assert sp.simplify(sol[c] + CF*b0/(8*sp.pi**2)) == 0 and sp.simplify(sol[gh] - ghat_HH) == 0
# ex:yzliu-sI-rge: the term -C_F/pi * mu^2 dalpha/dmu^2 * L_b = + C_F beta0/(4 pi^2) alpha^2 L_b cancels 2 c alpha^2 L_b
print('ex:yzliu-sI-rge: -C_F/pi * (-beta0/(4pi)) =', sp.simplify(-CF/sp.pi*(-b0/(4*sp.pi))), ' = -2c ->', sp.simplify(-2*sol[c]))
# conversion to Liu's convention (a): d alpha/d ln mu = beta0^(a) alpha^2, beta0^(a) = -beta0/(2 pi):
b0a = -b0/(2*sp.pi)
print('c in terms of beta0^(a):', sp.simplify(sol[c].subs(b0, -2*sp.pi*sp.Symbol('b0a'))), ' (Liu APPB (81) prints b0a*C_F/(2pi): factor 2 too large)')
# numerical check with one-loop running (n_f = 4)
mp.mp.dps = 30
CFv = mp.mpf(4)/3; nfv = 4; b0v = mp.mpf(11) - mp.mpf(2)*nfv/3
def alpha(mu2, amu, mu2ref):
    return amu/(1 + b0v/(4*mp.pi)*amu*mp.log(mu2/mu2ref))
mu2 = mp.mpf(100)
for amu in [mp.mpf('0.02'), mp.mpf('0.002')]:
    Lbv = mp.mpf(1)
    mub2 = mu2*mp.e**(-Lbv)
    # ln S_I(mu) - ln S_I(mu_b) = int_{mu_b}^{mu} gamma_HH^(1)(alpha) dln mu^2 at one-loop anomalous dimension
    exact = -CFv/mp.pi*mp.quad(lambda t: alpha(mp.e**t, amu, mu2), [mp.log(mub2), mp.log(mu2)])
    oneloop = -CFv/mp.pi*amu*Lbv
    coef = (exact - oneloop)/(amu**2*Lbv**2)
    print('alpha=%s: numeric L_b^2 coefficient %s ; -C_F beta0/(8 pi^2) = %s' % (amu, mp.nstr(coef, 8), mp.nstr(-CFv*b0v/(8*mp.pi**2), 8)))
print('PASS')
