# W17 / Ch14 -- s04: one-loop TMD soft factor with non-light-like lines.
# time-like: n_A=(1, e^{-2yA}), n_B=(e^{2yB}, 1); space-like (Collins): n_A=(1,-e^{-2yA}), n_B=(-e^{2yB},1).
# -J.J/(g^2 C_F) = 2 nA.nB/((nA.l)(nB.l)) - nA^2/(nA.l)^2 - nB^2/(nB.l)^2 ;  int dy l_T^2 (...) = 4 (Y coth Y - sigma)
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
mp.mp.dps = 30
ok = True
def check(name, cond):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name); ok &= bool(cond)

y, yA, yB, lT = sp.symbols('y y_A y_B l_T', real=True)
def dot(a, b): return a[0]*b[1] + a[1]*b[0]
l = (lT*sp.exp(y)/sp.sqrt(2), lT*sp.exp(-y)/sp.sqrt(2))
Y = yA - yB
for kind, sA, sB in [('time-like', 1, 1), ('space-like', -1, -1)]:
    nA = (1, sA*sp.exp(-2*yA)); nB = (sB*sp.exp(2*yB), 1)
    cross = sp.simplify(lT**2*dot(nA, nB)/(dot(nA, l)*dot(nB, l)))
    if kind == 'time-like':
        target = sp.cosh(Y)/(sp.cosh(y - yA)*sp.cosh(y - yB))
    else:
        target = -sp.cosh(Y)/(sp.sinh(y - yA)*sp.sinh(y - yB))
    check('%s cross term = %s' % (kind, target), sp.simplify((cross - target).rewrite(sp.exp)) == 0)
    selfA = sp.simplify(lT**2*dot(nA, nA)/dot(nA, l)**2)
    if kind == 'time-like':
        check('time-like self energy l^2 nA^2/(nA.l)^2 = 1/cosh^2(y-yA)', sp.simplify((selfA - 1/sp.cosh(y - yA)**2).rewrite(sp.exp)) == 0)
    else:
        check('space-like self energy = -1/sinh^2(y-yA) (non-integrable double pole)', sp.simplify((selfA + 1/sp.sinh(y - yA)**2).rewrite(sp.exp)) == 0)

# numeric rapidity integrals
def int_cross_time(YA, YB):
    f = lambda yy: mp.cosh(YA - YB)/(mp.cosh(yy - YA)*mp.cosh(yy - YB))
    return mp.quad(f, [-mp.inf, YB, YA, mp.inf])
def int_cross_space_PV(YA, YB, eta=mp.mpf('1e-15')):
    f = lambda yy: -mp.cosh(YA - YB)/(mp.sinh(yy - YA)*mp.sinh(yy - YB))
    # symmetric excision around both simple poles
    pts = sorted([YA, YB]); a, b = pts
    h = min(mp.mpf('0.5'), (b - a)/3)
    I = mp.quad(f, [-mp.inf, a - h, a - eta]) + mp.quad(f, [a + eta, a + h, (a + b)/2, b - h, b - eta]) + mp.quad(f, [b + eta, b + h, mp.inf])
    return I
for (YA, YB) in [(mp.mpf('1.3'), mp.mpf('-0.4')), (mp.mpf('3.0'), mp.mpf('-2.5')), (mp.mpf('0.2'), mp.mpf('0.05'))]:
    Yv = YA - YB
    exp_ = 2*Yv*mp.coth(Yv)
    it = int_cross_time(YA, YB); isp = int_cross_space_PV(YA, YB)
    check('int cross (time-like) = 2Y coth Y at Y=%s' % mp.nstr(Yv, 3), abs(it - exp_) < 1e-15)
    check('PV int cross (space-like) = 2Y coth Y at Y=%s' % mp.nstr(Yv, 3), abs(isp - exp_) < 1e-9)
check('int 1/cosh^2 = 2', abs(mp.quad(lambda yy: 1/mp.cosh(yy)**2, [-mp.inf, mp.inf]) - 2) < 1e-25)
print('=> int dy l_T^2 (-J.J)/(g^2 C_F) = 2*(2Y coth Y) - sigma*(2+2) = 4(Y coth Y - sigma), sigma=1 time-like, 0 space-like (no S.I.)')

# Fourier factor: c_S FT[1/k^2]/(a S_eps) = A(eps) = -e^{eps L_b} e^{-gamma eps} Gamma(1-eps)/eps
eps, mu, b, als, CF = sp.symbols('epsilon mu b alpha_s C_F', positive=True)
d = 2 - 2*eps
cS = 4*sp.pi*als*mu**(2*eps)*CF/(2*sp.pi)**(3 - 2*eps)
FT = sp.pi**(d/2)*2**(d - 2)*sp.gamma(d/2 - 1)/sp.gamma(1)*(b**2)**(1 - d/2)
a = als*CF/(2*sp.pi)
Seps = (4*sp.pi)**eps*sp.exp(-eps*sp.EulerGamma)
b0 = 2*sp.exp(-sp.EulerGamma)
Lb = sp.log(mu**2*b**2/b0**2)
A_claim = -sp.exp(eps*Lb)*sp.exp(-sp.EulerGamma*eps)*sp.gamma(1 - eps)/eps
ratio = sp.simplify(sp.expand_log(sp.expand_power_base((cS*FT/(a*Seps))/A_claim, force=True), force=True))
check('c_S FT[1/k^2]/(a S_eps) = A(eps)', sp.simplify(sp.logcombine(sp.expand_log(ratio, force=True), force=True)) == 1 or abs(complex(ratio.subs({eps: 0.13, mu: 1.7, b: 0.4}).evalf())-1) < 1e-12)
print('   numeric ratio check:', sp.N(ratio.subs({eps: sp.Rational(13, 100), mu: sp.Rational(17, 10), b: sp.Rational(2, 5)})))
L = sp.Symbol('L')
Aser = sp.series(-sp.exp(eps*L)*sp.exp(-sp.EulerGamma*eps)*sp.gamma(1 - eps)/eps, eps, 0, 2).removeO()
Aexp = -1/eps - L - eps*(L**2/2 + sp.pi**2/12)
check('A(eps) = -1/eps - L_b - eps(L_b^2/2 + pi^2/12) + O(eps^2)', sp.simplify(sp.expand(Aser - Aexp)) == 0)
# Collins S_eps: A^C = A e^{-gamma eps} Gamma(1-eps) -> pi^2/12 -> pi^2/6
AserC = sp.series(-sp.exp(eps*L)*(sp.exp(-sp.EulerGamma*eps)*sp.gamma(1 - eps))**2/eps, eps, 0, 2).removeO()
check('Collins S_eps: pi^2/12 -> pi^2/6', sp.simplify(sp.expand(AserC - (-1/eps - L - eps*(L**2/2 + sp.pi**2/6)))) == 0)
# S_eps ratio: S_eps/S_eps^C = e^{-eps gamma} Gamma(1-eps) = 1 + pi^2/12 eps^2
check('S_eps/S^C_eps = 1 + pi^2 eps^2/12 + O(eps^3)', sp.simplify(sp.series(sp.exp(-eps*sp.EulerGamma)*sp.gamma(1 - eps), eps, 0, 3).removeO() - (1 + sp.pi**2*eps**2/12)) == 0)

# renormalized one-loop soft factor and Ktilde from the soft factor alone
Yv, sig, yn = sp.symbols('Y sigma y_n', real=True)
S1 = -(als*CF/sp.pi)*(Yv*sp.coth(Yv) - sig)*L
# large-Y: Y coth Y = |Y| + O(e^{-2Y})
lead = sp.limit(Yv*sp.coth(Yv) - Yv, Yv, sp.oo)
check('Y coth Y - Y -> 0 as Y -> +inf', lead == 0)
# K from soft factor: K = 1/2 d/dyn [ S1(yn - yB) - S1(yA - yn) ]  in the limit yA->+inf, yB->-inf
yA_, yB_ = sp.symbols('yA yB', real=True)
expr = sp.Rational(1, 2)*sp.diff(S1.subs(Yv, yn - yB_) - S1.subs(Yv, yA_ - yn), yn)
Klim = sp.limit(sp.limit(expr, yA_, sp.oo), yB_, -sp.oo)
check('Ktilde from the soft factor alone = -(alpha_s C_F/pi) L_b (sigma-independent)', sp.simplify(Klim + als*CF/sp.pi*L) == 0)
# cusp: UV pole of time-like soft factor (sigma=1): Z_S = 1 + (alpha_s CF/pi)(Y coth Y -1)/eps ; gamma_S = dlnZ/dlnmu with dals/dlnmu=-2eps als
ZS1 = (als*CF/sp.pi)*(Yv*sp.coth(Yv) - 1)/eps
gS = sp.simplify(-2*eps*als*sp.diff(ZS1, als))
check('soft-factor anomalous dimension = -2 x one-loop cusp (alpha_s C_F/pi)(Y coth Y - 1)', sp.simplify(gS + 2*(als*CF/sp.pi)*(Yv*sp.coth(Yv) - 1)) == 0)
# cusp angle of the space-like pair: nA.nB/sqrt(nA^2 nB^2) = cosh(Y)
nA = (1, -sp.exp(-2*yA)); nB = (-sp.exp(2*yB), 1)
cosY = dot(nA, nB)/sp.sqrt(dot(nA, nA)*dot(nB, nB))
check('space-like pair: n_A.n_B/sqrt(n_A^2 n_B^2) = cosh(y_A-y_B)', sp.simplify((cosY - sp.cosh(yA - yB)).rewrite(sp.exp)) == 0)
print('ALL PASS' if ok else 'SOME FAIL')
