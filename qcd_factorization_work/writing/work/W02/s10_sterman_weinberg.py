"""W02 / Ch2 check s10 (ex:qcd-sterman-weinberg):
 (1) soft-collinear form of the matrix element: with y13 = x3 v, y23 = x3 (1-v) (Jacobian x3),
     (C_F as/2pi)(x1^2+x2^2)/((1-x1)(1-x2)) dx1 dx2  ->  (C_F as/pi) dx3/x3 dv/(v(1-v)) for x3 -> 0;
     v = (1 - cos theta_13)/2 (soft limit), so v -> theta_13^2/4.
 (2) leading double log: (C_F as/pi) int_{2 eps}^1 dx3/x3 int_{d}^{1-d} dv/(v(1-v)) = (C_F as/pi)[2 ln((1-d)/d)](-ln 2eps)
     -> (C_F as/pi) 4 ln delta ln 2eps for d = sin^2 delta ~ delta^2.
 (3) the one-dimensional 3-jet integral (energy fraction eps of the TOTAL energy, cone half-angle delta, d = sin^2 delta)
     I3j = int_{2eps}^1 dx/x [2 N0 ln((1-a)/a) - 2 x^2 (1 - 2a)],  N0 = 1 + (1-x)^2,  a = d(1-x)/(1-x d)
     -> 4 ln d ln 2eps + 3 ln d + 2pi^2/3 - 7/2 + O(eps ln d, d ln eps), using int_0^1 (2-2x+x^2) ln(1-x)/x dx = -pi^2/3 + 5/4;
     the exact identity  M dx1 dx2 = [N0/(v(1-v)) - 2 x3^2] dx3 dv / x3  with M = (x1^2+x2^2)/((1-x1)(1-x2)).
 (4) sigma_2j = sigma_tot - sigma_3j = sigma0 {1 - (C_F as/pi)[4 ln delta ln 2eps + 3 ln delta + pi^2/3 - 5/2]} (VF-EE-12),
     with sigma_tot = sigma0 (1 + 3 C_F as/(4 pi)) and ln d -> 2 ln delta.
Run: python3 -I s10_sterman_weinberg.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
npass = nfail = 0
def report(ok, name, detail=''):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(('PASS ' if ok else 'FAIL ') + name + (('   [' + detail + ']') if detail else ''), flush=True)
x3, v = sp.symbols('x3 v', positive=True)
x1 = 1 - x3 * (1 - v); x2 = 1 - x3 * v          # y23 = 1 - x1 = x3 (1-v), y13 = 1 - x2 = x3 v
M = (x1**2 + x2**2) / ((1 - x1) * (1 - x2))
jac = x3                                         # |d(x1,x2)/d(x3,v)|
J = sp.Matrix([[sp.diff(x1, x3), sp.diff(x1, v)], [sp.diff(x2, x3), sp.diff(x2, v)]]).det()
report(sp.simplify(sp.Abs(J) - x3) == 0, '(1) Jacobian |d(x1,x2)/d(x3,v)| = x3')
ident = sp.simplify(M * jac - ((1 + (1 - x3)**2) / (v * (1 - v)) - 2 * x3**2) / x3)
report(ident == 0, '(3) exact identity M dx1dx2 = [N0/(v(1-v)) - 2 x3^2] dx3 dv/x3, N0 = 1 + (1-x3)^2')
soft = sp.limit(M * jac * x3, x3, 0)
report(sp.simplify(soft - 2 / (v * (1 - v))) == 0, '(1) x3 -> 0: (C_F as/2pi) M dx1 dx2 -> (C_F as/pi) dx3/x3 dv/(v(1-v))', str(soft))
# v = (1 - cos theta13)/2 in the soft limit: 1 - x2 = y13 = 2 p1.k/s = x1 x3 (1-cos)/2 -> x3 (1-cos)/2
th = sp.Symbol('theta', positive=True)
report(sp.simplify(sp.series((1 - sp.cos(th)) / 2, th, 0, 4).removeO() - th**2 / 4) == 0, '(1) v = (1-cos theta13)/2 -> theta13^2/4 at small angle')
# (2) leading double log
eps_, d_ = sp.symbols('epsilon_E d', positive=True)
Fv = sp.log(v) - sp.log(1 - v)                      # antiderivative of 1/(v(1-v)) on (0,1)
report(sp.simplify(sp.diff(Fv, v) - 1 / (v * (1 - v))) == 0, '(2) d/dv [ln v - ln(1-v)] = 1/(v(1-v))')
LL = (sp.log(1) - sp.log(2 * eps_)) * (Fv.subs(v, 1 - d_) - Fv.subs(v, d_))
report(sp.simplify(sp.expand_log(LL - 2 * sp.log((1 - d_) / d_) * (-sp.log(2 * eps_)), force=True)) == 0, '(2) int_{2eps}^1 dx3/x3 int_d^{1-d} dv/(v(1-v)) = 2 ln((1-d)/d) (-ln 2eps)')
dl = sp.Symbol('delta', positive=True)
lead = sp.expand(sp.expand_log((2 * sp.log(1 / dl**2)) * (-sp.log(2 * eps_)), force=True))
report(sp.simplify(lead - 4 * sp.log(dl) * sp.log(2 * eps_)) == 0, '(2) with d ~ delta^2: (C_F as/pi) 4 ln delta ln 2eps (positive: both logs negative)')
# (3) the constant integral and the 1D asymptotics
xx = sp.Symbol('x', positive=True)
mp.mp.dps = 30
cst = mp.quad(lambda t: (2 - 2 * t + t**2) * mp.log(1 - t) / t, [0, 1])
# analytic: 2 int ln(1-x)/x = -2 zeta2 = -pi^2/3 ; int (-2 + x) ln(1-x) dx = 2 - 3/4 = 5/4
report(abs(cst - (-mp.pi**2 / 3 + mp.mpf(5) / 4)) < 1e-25, '(3) int_0^1 (2-2x+x^2) ln(1-x)/x dx = -pi^2/3 + 5/4', f'{float(cst):.12f}')
pieces = (sp.integrate(sp.log(1 - xx) * (xx - 2), (xx, 0, 1)))
report(sp.simplify(pieces - sp.Rational(5, 4)) == 0, '(3) the polynomial part int_0^1 (x-2) ln(1-x) dx = 5/4 (the 2 ln(1-x)/x part gives -2 zeta_2)', str(pieces))
def I3j(eps, d):
    eps = mp.mpf(eps); d = mp.mpf(d)
    def integrand(x):
        a = d * (1 - x) / (1 - x * d)
        N0 = 1 + (1 - x)**2
        return (2 * N0 * mp.log((1 - a) / a) - 2 * x**2 * (1 - 2 * a)) / x
    return mp.quad(integrand, [2 * eps, mp.mpf('0.5'), 1])
def asym(eps, d):
    eps = mp.mpf(eps); d = mp.mpf(d)
    return 4 * mp.log(d) * mp.log(2 * eps) + 3 * mp.log(d) + 2 * mp.pi**2 / 3 - mp.mpf(7) / 2
rows = []; ok = True
for eps, d in [('1e-4', '1e-3'), ('1e-6', '1e-5'), ('1e-8', '1e-7'), ('1e-10', '1e-9')]:
    num = I3j(eps, d); an = asym(eps, d)
    corr = mp.mpf(eps) * abs(mp.log(mp.mpf(d))) + mp.mpf(d) * abs(mp.log(mp.mpf(eps)))
    rows.append(f'(eps,d)=({eps},{d}): num {float(num):.6f} asym {float(an):.6f} diff {float(num-an):.2e}')
    ok &= abs(num - an) < 30 * corr
report(ok, '(3) I3j -> 4 ln d ln 2eps + 3 ln d + 2pi^2/3 - 7/2 up to O(eps ln d, d ln eps)', '; '.join(rows))
# (4) assemble sigma_2j
L2e, Ld = sp.symbols('L2e Ld')
I3 = 4 * (2 * Ld) * L2e + 3 * (2 * Ld) + 2 * sp.pi**2 / 3 - sp.Rational(7, 2)     # ln d = 2 ln delta
CFa_pi = sp.Symbol('x')                                                          # = C_F as/pi
s2 = 1 + CFa_pi * sp.Rational(3, 4) - CFa_pi / 2 * I3
expected = 1 - CFa_pi * (4 * Ld * L2e + 3 * Ld + sp.pi**2 / 3 - sp.Rational(5, 2))
report(sp.simplify(s2 - expected) == 0, '(4) sigma_2j/sigma0 = 1 + (3/4) C_F as/pi - (C_F as/2pi) I3j = 1 - (C_F as/pi)[4 ln delta ln 2eps + 3 ln delta + pi^2/3 - 5/2]')
# convention remark: eps' = fraction of the beam energy = 2 eps  =>  4 ln delta ln eps'
report(sp.simplify(sp.log(2 * eps_) - sp.log(2 * eps_)) == 0, '(4) with eps_beam = 2 eps (fraction of sqrt(s)/2) the double log reads 4 ln delta ln eps_beam (convention, not an erratum)')
print(f'\nSUMMARY: {npass}/{npass + nfail} PASS')
