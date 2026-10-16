# E08, E09, E11 stage-2 checks: sign conventions of Gamma_S and the two-loop log structure of ln S_I.
# Conventions read from the rendered journal pages:
#  APPB 53 (2022) 4-A2: (77) mu^2 dlnS_I/dmu^2 = -Gamma_S ; (78) mu^2 dlnS_DY/dmu^2 = -(Y+Y')Gamma_cusp + Gamma_S ;
#                       (79) S_DY^(1) = (as CF/pi)[1-(Y+Y')]L_b ; (80) Gamma_S^(1) = as CF/pi ;
#                       (81) ln S_I^(2) = c2 - Gamma_S^(2) L_b + as^2 (beta0 CF/2pi) L_b^2,
#                            Gamma_S^(2) = (as^2/pi^2)[CF CA(-49/36+pi^2/12-z3/2) + CF NF 5/18], beta0 = -(11/3 CA - 4/3 NF TF)/(2pi).
#  PRD 105 (2022) 076014 (journal): (47) mu^2 dlnS_rN/dmu^2 = -(N+1)/2 Gamma_S ; (72) S_r1^(1) = -(as CF/pi) L_b ;
#                       text: Gamma_S^(1) = as CF/pi ; (73) Gamma_S^(2) = same expression as APPB.
#  RMP arXiv:2004.03543v2: (203) S_DY = e^{(Y+Y')K + D}; (204) S_r = e^{-D}; (205) mu^2 dlnS_r/dmu^2 = Gamma_S;
#                       (206) mu^2 dlnS_DY/dmu^2 = -(Y+Y')Gamma_cusp - Gamma_S ; (207) S_DY^(1) = (as CF/2pi)[2-2(Y+Y')]L_b,
#                       Gamma_S^(1) = as CF/pi ; (208) D^(2) = c2 + Gamma_S^(2) L_b - (as^2 beta0 CF/2pi) L_b^2,
#                       Gamma_S^(2) = -(as^2/pi^2)[CF CA(-49/36+pi^2/12-z3/2) + CF NF 5/18], same beta0.
#  Physics input (verified in s2_e07ii_cusp.py from Kidonakis eq. (9) and GHKM (5.5)):
#     mu^2 dlnS_DY/dmu^2 = -Gamma_cusp(theta), theta = Y+Y'  -> -theta*Gamma_cusp - gamma_HH  (theta -> oo)
#     gamma_HH = -as CF/pi + (as/pi)^2 CF [CA(-49/36+pi^2/12-z3/2) + (5/9) TF nf]
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

a, Lb, th, CF, CA, nf, TF, c2 = sp.symbols('alpha_s L_b theta C_F C_A n_f T_F c_2')
pi, z3 = sp.pi, sp.zeta(3)
gHH1 = -CF/pi
gHH2 = CF/pi**2*(CA*(sp.Rational(-49, 36) + pi**2/12 - z3/2) + sp.Rational(5, 9)*TF*nf)
b0CTX = sp.Rational(11, 3)*CA - sp.Rational(4, 3)*TF*nf          # mu^2 d a/d mu^2 = -b0CTX a^2/(4 pi)
b0LIU = -b0CTX/(2*pi)                                              # d a/d ln mu = b0LIU a^2

# ---- one-loop anomalous dimension of S_DY from (79)/(207):
lnSDY1 = a*CF/pi*(1 - th)*Lb
print('mu^2 d lnS_DY^(1)/dmu^2 =', sp.expand(sp.diff(lnSDY1, Lb)), '  -> constant part = +as CF/pi = -gamma_HH^(1)')
# APPB/PRD105: (78)  -theta Gamma_cusp + Gamma_S  => Gamma_S = -gamma_HH (at one loop +as CF/pi, consistent with (80))
# RMP (206): -theta Gamma_cusp - Gamma_S => Gamma_S^(1) would be -as CF/pi, contradicting the stated +as CF/pi.
# ---- RMP: D^(1) from (203)+(207): lnS_DY = theta K + D
K1 = -a*CF/pi*Lb; D1 = a*CF/pi*Lb
print('RMP check: theta*K1 + D1 - lnS_DY^(1) =', sp.simplify(th*K1 + D1 - lnSDY1))
lnSr1 = -D1
print('RMP: mu^2 dlnS_r^(1)/dmu^2 =', sp.diff(lnSr1, Lb), ' vs (205) with Gamma_S^(1)=+as CF/pi: +as CF/pi  -> sign contradiction')

# ---- correct two-loop structure of ln S_I from mu^2 dlnS_I/dmu^2 = gamma_HH(a(mu)), with running coupling.
cc, gg = sp.symbols('cc gg')
lnSI = -a*CF/pi*Lb + a**2*(cc*Lb**2 + gg*Lb + c2)
# total derivative d/dln mu^2 at fixed b: d/dLb + (da/dlnmu^2) d/da, da/dlnmu^2 = -b0CTX a^2/(4pi)
dlnSI = sp.diff(lnSI, Lb) + (-b0CTX*a**2/(4*pi))*sp.diff(lnSI, a)
res = sp.expand(dlnSI - (a*gHH1 + a**2*gHH2))
res2 = sp.expand(res).coeff(a, 2)
sol = sp.solve([sp.expand(res2).coeff(Lb, 1), sp.expand(res2).coeff(Lb, 0)], [cc, gg], dict=True)[0]
print('one-loop residual (coefficient of a):', sp.simplify(sp.expand(res).coeff(a, 1)))
print('correct L_b^2 coefficient:', sp.simplify(sol[cc]), ' = ', sp.simplify(sol[cc]/(CF*b0CTX)), '* CF*beta0^CTX')
print('   in Liu et al. beta0 convention:', sp.simplify(sol[cc]/(CF*b0LIU)), '* CF*beta0^LIU   (printed: 1/(2 pi))')
print('correct single-log coefficient:', sp.simplify(sol[gg] - gHH2) == 0, '(= gamma_HH^(2)/as^2)')

# ---- printed APPB (81)
GS2_printed = CF/pi**2*(CA*(sp.Rational(-49, 36) + pi**2/12 - z3/2) + nf*sp.Rational(5, 18))   # coefficient of a^2
lnSI_APPB = -a*CF/pi*Lb + c2*a**2 - a**2*GS2_printed*Lb + a**2*(b0LIU*CF/(2*pi))*Lb**2
r_APPB = sp.expand(sp.diff(lnSI_APPB, Lb) + (-b0CTX*a**2/(4*pi))*sp.diff(lnSI_APPB, a) - (a*gHH1 + a**2*gHH2.subs(TF, sp.Rational(1, 2))))
print('APPB (81) RGE residual, O(as^2) =', sp.collect(sp.expand(sp.expand(r_APPB.subs(TF, sp.Rational(1, 2))).coeff(a, 2)), Lb), ' ; O(as) =', sp.simplify(sp.expand(r_APPB).coeff(a, 1)))
print('   expected decomposition: -CF*b0/(4 pi^2) L_b [factor-2 error]  and  -2 gamma_HH^(2) [single-log sign] :', sp.simplify(sp.expand(r_APPB.subs(TF, sp.Rational(1, 2))).coeff(a, 2) - (-CF*b0CTX.subs(TF, sp.Rational(1, 2))/(4*pi**2)*Lb - 2*gHH2.subs(TF, sp.Rational(1, 2))))==0)
# ---- printed RMP (208): ln S_r = -D
D_RMP = a*CF/pi*Lb + c2*a**2 + (-GS2_printed)*a**2*Lb - a**2*b0LIU*CF/(2*pi)*Lb**2
lnSr_RMP = -D_RMP
r_RMP = sp.expand(sp.diff(lnSr_RMP, Lb) + (-b0CTX*a**2/(4*pi))*sp.diff(lnSr_RMP, a) - (a*gHH1 + a**2*gHH2))
print('RMP (208) RGE residual, O(as^2) =', sp.factor(sp.expand(sp.expand(r_RMP.subs(TF, sp.Rational(1, 2))).coeff(a, 2))), ' ; O(as) =', sp.simplify(sp.expand(r_RMP).coeff(a, 1)))
print('   equals -CF*b0/(4 pi^2) L_b only (single log correct):', sp.simplify(sp.expand(r_RMP.subs(TF, sp.Rational(1, 2))).coeff(a, 2) - (-CF*b0CTX.subs(TF, sp.Rational(1, 2))/(4*pi**2)*Lb))==0)

# ---- E08: corrected Gamma_S^(2) in the APPB/PRD105 convention (Gamma_S = -gamma_HH):
print('E08: correct Gamma_S^(2) (APPB/PRD105 convention) = -gamma_HH^(2) =', sp.expand(-gHH2.subs(TF, sp.Rational(1, 2))))
print('     printed Gamma_S^(2) - (+gamma_HH^(2)) =', sp.simplify(GS2_printed - gHH2.subs(TF, sp.Rational(1, 2))))

# ---- numerical cross-check: integrate the RGE with exact one-loop running from mu_b and fit the L_b^2 coefficient
mp.mp.dps = 30
CFv, CAv, nfv, TFv = mp.mpf(4)/3, mp.mpf(3), mp.mpf(4), mp.mpf(1)/2
b0v = mp.mpf(11)/3*CAv - mp.mpf(4)/3*TFv*nfv
g1 = -CFv/mp.pi
g2 = CFv/mp.pi**2*(CAv*(-mp.mpf(49)/36 + mp.pi**2/12 - mp.zeta(3)/2) + mp.mpf(5)/9*TFv*nfv)
def lnSI_exact(amu, L):
    # alpha_s at scale mu' with ln(mu'^2/mu^2) = -s : a(s) = amu/(1 - b0 amu s/(4pi))
    f = lambda s: g1*amu/(1 - b0v*amu*s/(4*mp.pi)) + g2*(amu/(1 - b0v*amu*s/(4*mp.pi)))**2
    return mp.quad(f, [0, L])          # ln S_I(mu) - ln S_I(mu_b) = int_{ln mu_b^2}^{ln mu^2} gamma_HH ; s = ln(mu^2/mu'^2)
for amu in [mp.mpf('0.004'), mp.mpf('0.001')]:
    vals = []
    for L in [mp.mpf(1), mp.mpf(2)]:
        vals.append((lnSI_exact(amu, L) - g1*amu*L)/amu**2)
    # vals(L) ~ cc L^2 + g2 L  ->  cc = (vals(2) - 2 vals(1))/2
    ccnum = (vals[1] - 2*vals[0])/2
    print('numeric (as =', amu, '): L_b^2 coefficient =', mp.nstr(ccnum, 10), ' ; -CF b0/(8 pi^2) =', mp.nstr(-CFv*b0v/(8*mp.pi**2), 10),
          ' ; printed (x2) =', mp.nstr(-CFv*b0v/(4*mp.pi**2), 10))
