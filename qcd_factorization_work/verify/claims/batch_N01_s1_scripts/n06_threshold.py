# Independent check of N06 (one-loop threshold factorization of the LaMET MS-bar kernel, Gamma = gamma^t).
# Exact one-loop coordinate kernel (IJJSZ 2018 / Radyushkin 2018), a = alpha_s C_F/(2 pi), l = ln(e^{2gE} mu^2 z^2/4):
#   C(alpha) = delta(1-alpha) (3/2)(l+1) - (l+1)[(1+alpha^2)/(1-alpha)]_+ - [4 ln(1-alpha)/(1-alpha)]_+ + 2(1-alpha)
#   Gt(lam)  = int_0^1 dalpha C(alpha) e^{-i alpha lam},  lam = z p^z  (tree: e^{-i lam}).
# Claim (JLS 2023 eqs. (hardoneloop),(jetoneloop),(JetoneloopIM)):
#   e^{i lam} Gt(lam) -> H1 + Jt1 + i pi sgn(lam) (L_z - 1) + o(1),  H1 = -2 + pi^2/12 - L_z^2/2 + L_z,
#   Jt1 = l^2/2 + l + pi^2/12 + 2,  l = 2 ln|lam| + 2 gE - L_z.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

# ---------- (1) exact asymptotics, symbolic ----------
Lam, Lz = sp.symbols('Lambda L_z', real=True)       # Lambda = ln(lam) + gE  (lam > 0)
l = 2*Lam - Lz
E0 = -Lam + sp.I*sp.pi/2                             # int_0^1 (e^{iu lam}-1)/u du -> -gE - ln lam + i pi/2
IB = 2*E0 + sp.Rational(3, 2)                        # int_0^1 [(2-2u+u^2)/u](e^{iu lam}-1) du, asymptotic
IL = sp.Rational(1, 2)*(Lam - sp.I*sp.pi/2)**2 + sp.pi**2/12   # int_0^1 ln(u)/u (e^{iu lam}-1) du, asymptotic
asym = sp.Rational(3, 2)*(l + 1) - (l + 1)*IB - 4*IL   # 2u-term is O(1/lam)
H1 = -2 + sp.pi**2/12 - Lz**2/2 + Lz
J1 = l**2/2 + l + sp.pi**2/12 + 2
print("symbolic: Re[asym - (H1+J1)] =", sp.simplify(sp.re(sp.expand(asym)) - (H1 + J1)),
      ";  Im[asym] - pi(L_z-1) =", sp.simplify(sp.im(sp.expand(asym)) - sp.pi*(Lz - 1)))
# mu-dependence: d/dln mu of the threshold limit at fixed lam: dl/dlnmu = 2, dL_z/dlnmu = -2
dmu = sp.diff(asym, Lz)*(-2)          # asym depends on mu only through L_z at fixed Lambda (l = 2Lambda - L_z)
print("symbolic: d/dln mu [threshold limit] =", sp.simplify(sp.expand(dmu)), " (expect 2[2 Lambda - i pi] = Gamma_cusp/a [ln(lam^2 e^{2gE}) - i pi])")
# anomalous dimensions of the pieces (one loop, units of a):
dH = sp.diff(H1, Lz)*(-2); dJ = sp.diff(J1.subs(Lam, (sp.Symbol('l') + Lz)/2), sp.Symbol('l'))*2
print("dlnH/dlnmu =", sp.expand(dH), "  (Gamma_cusp L_z + gtilde_H with Gamma_cusp=2a, gtilde_H=-2a)")
lsym = sp.Symbol('l')
Jl = lsym**2/2 + lsym + sp.pi**2/12 + 2
print("dlnJ/dlnmu =", sp.expand(sp.diff(Jl, lsym)*2), "  (Gamma_cusp l - gtilde_J with gtilde_J=-2a)")
print("phase: d/dlnmu[i pi (L_z-1)] =", sp.diff(sp.I*sp.pi*(Lz - 1), Lz)*(-2), " (= -i pi Gamma_cusp)")

# ---------- (2) numerical, independent of the asymptotic formulas ----------
mp.mp.dps = 30
def Ttail(lam):
    """T(lam) = int_1^inf ln(u)/u e^{i u lam} du by contour rotation u = 1 + i s t/|lam|, s = sgn(lam)
       (exponentially convergent; independent of oscillatory-weight quadrature)."""
    lam = mp.mpf(lam); s = mp.sign(lam); L = abs(lam)
    f = lambda t: (1j*s/L)*mp.log(1 + 1j*s*t/L)/(1 + 1j*s*t/L)*mp.e**(1j*lam)*mp.e**(-t)
    return mp.quad(f, [0, 1, 10, 50, mp.inf])

def eilamG(lam, LzV, use_hyp=False):
    lam = mp.mpf(lam); LzV = mp.mpf(LzV)
    s = mp.sign(lam); L = abs(lam)
    lv = 2*mp.log(L) + 2*mp.euler - LzV
    w = 1j*lam                                        # e^{i u lam} = e^{u w}
    if use_hyp:   # series representations (valid, but slow for large |lam|)
        E0n = w*mp.hyp2f2(1, 1, 2, 2, w)              # int_0^1 (e^{uw}-1)/u du
        ILn = -w*mp.hyper([1, 1, 1], [2, 2, 2], w)    # int_0^1 ln u (e^{uw}-1)/u du
    else:         # exact special functions + analytic constant + rotated tail
        E0n = mp.ci(L) - mp.euler - mp.log(L) + 1j*s*mp.si(L)
        lns = mp.log(L) - 1j*s*mp.pi/2               # ln(-i lam)
        ILn = (mp.euler + lns)**2/2 + mp.pi**2/12 - Ttail(lam)
    J0 = (mp.e**w - 1)/w
    J1n = mp.e**w/w - (mp.e**w - 1)/w**2
    IBn = 2*E0n + (J1n - mp.mpf(1)/2) - 2*(J0 - 1)      # int_0^1 [(2-2u+u^2)/u](e^{uw}-1) du
    I3n = 2*J1n
    return mp.mpf(3)/2*(lv + 1) - (lv + 1)*IBn - 4*ILn + I3n

def pred(lam, LzV):
    lv = 2*mp.log(abs(lam)) + 2*mp.euler - LzV
    h = -2 + mp.pi**2/12 - LzV**2/2 + LzV
    j = lv**2/2 + lv + mp.pi**2/12 + 2
    return h + j + 1j*mp.sign(lam)*mp.pi*(LzV - 1)

# sanity: hypergeometric representation vs direct quadrature at moderate lambda
for lam in (5.0, -12.0):
    LzV = 0.3
    lv = 2*mp.log(abs(lam)) + 2*mp.euler - LzV
    f = lambda al: (1 + al**2)/(1 - al)*(mp.e**(-1j*al*lam) - mp.e**(-1j*lam))
    g = lambda al: mp.log(1 - al)/(1 - al)*(mp.e**(-1j*al*lam) - mp.e**(-1j*lam))
    h = lambda al: 2*(1 - al)*mp.e**(-1j*al*lam)
    direct = (mp.mpf(3)/2*(lv + 1)*mp.e**(-1j*lam) - (lv + 1)*mp.quad(f, [0, 0.5, 1]) - 4*mp.quad(g, [0, 0.5, 1])
              + mp.quad(h, [0, 1]))*mp.e**(1j*lam)
    print("lam=%6.1f  series = %s  special-fn+rotated tail = %s  direct quadrature = %s  |diffs| = %s, %s"
          % (lam, mp.nstr(eilamG(lam, LzV, True), 15), mp.nstr(eilamG(lam, LzV), 15), mp.nstr(direct, 15),
             mp.nstr(abs(eilamG(lam, LzV, True) - direct), 3), mp.nstr(abs(eilamG(lam, LzV) - direct), 3)))

for LzV in (0.0, 1.3, -0.8):
    for lam in (1e2, -1e2, 1e3, -1e3, 1e4, -1e4, 1e5, -1e5):
        d = eilamG(lam, LzV) - pred(lam, LzV)
        print("Lz=%5.2f lam=%9.0e  exact - predicted = %s   |d| = %.2e"
              % (LzV, lam, mp.nstr(d, 4), float(abs(d))))
