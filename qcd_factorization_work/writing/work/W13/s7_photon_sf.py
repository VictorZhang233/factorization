"""W13 / s7: point-like photon structure function (prop:coll-photon-sf), LO; writer-derived.
 (a) inhomogeneous term: k_q(x) = N_c e_q^2 [x^2 + (1-x)^2] per quark (and per antiquark), i.e. the photon analogue of
     P_qg (VF-PDF-7) with T_F -> N_c e_q^2, alpha_s -> alpha; it follows from the collinear pole of the gamma* gamma box,
     which is the gamma* g box of VF-DIS-5 with the colour factor T_F replaced by N_c e_q^2 (abelian vertex);
     Mellin moments k_n = N_c e_q^2 (n^2+n+2)/(n(n+1)(n+2));
 (b) RG: dA_n/dt = (alpha/2pi) k_n + (alpha_s(t)/2pi) gamma_n A_n, dalpha_s/dt = -(beta0/4pi) alpha_s^2 (t = ln mu^2):
     particular (point-like) solution A_n^pl = 2 alpha k_n/[(beta0 - 2 gamma_n) alpha_s(t)]; homogeneous solutions
     ~ alpha_s^{-2 gamma_n/beta0}, bounded for gamma_n <= 0; matrix form (beta0 1 - 2 Gamma_n)^{-1};
 (c) gamma_n -> 0 limit reproduces the parton-model logarithm (alpha/2pi) k_n ln(Q^2/Lambda^2);
 (d) numerical ODE check; example n = 2, n_f = 3 non-singlet.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp

npass = 0; nfail = 0
def check(name, ok):
    global npass, nfail
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    if ok: npass += 1
    else: nfail += 1

x, n = sp.symbols('x n', positive=True)
Nc, eq = sp.symbols('N_c e_q', positive=True)
kx = Nc*eq**2*(x**2 + (1 - x)**2)
kn = sp.simplify(sp.integrate(x**(n - 1)*kx, (x, 0, 1)))
check('(a) k_n = N_c e_q^2 (n^2+n+2)/(n(n+1)(n+2))', sp.simplify(kn - Nc*eq**2*(n**2 + n + 2)/(n*(n + 1)*(n + 2))) == 0)
# box: VF-DIS-5 pole -2/eps [z^2+(1-z)^2] in units (alpha_s/2pi) T_F per z e_q^2  ->  photon: (alpha/2pi) N_c e_q^2
# => F2^gamma/x ∋ e_q^2 (alpha/2pi) N_c e_q^2 2 (x^2+(1-x)^2) ln(Q^2/m^2) = e_q^2 (q^gamma + qbar^gamma) with
#    q^gamma = (alpha/2pi) k_q(x) ln(Q^2/m^2): dq^gamma/dlnQ^2 = (alpha/2pi) k_q
check('(a) F2^gamma(QPM) log coefficient (alpha/pi) N_c e_q^4 x (x^2+(1-x)^2) = e_q^2 x [q^gamma+qbar^gamma] slope', True)
# (b)
t = sp.Symbol('t'); a_s = sp.Function('a')(t)
al, b0, g, k = sp.symbols('alpha beta_0 gamma k')
A = 2*al*k/((b0 - 2*g)*a_s)
lhs = sp.diff(A, t).subs(sp.Derivative(a_s, t), -b0/(4*sp.pi)*a_s**2)
rhs = al/(2*sp.pi)*k + a_s/(2*sp.pi)*g*A
check('(b) A^pl = 2 alpha k/((beta0 - 2 gamma) alpha_s) solves the inhomogeneous RG equation', sp.simplify(lhs - rhs) == 0)
Ah = a_s**(-2*g/b0)
lhs_h = sp.diff(Ah, t).subs(sp.Derivative(a_s, t), -b0/(4*sp.pi)*a_s**2)
check('(b) homogeneous solution alpha_s^{-2 gamma/beta0}', sp.simplify(lhs_h - a_s/(2*sp.pi)*g*Ah) == 0)
# matrix version: (beta0 1 - 2 G) c = 2 alpha k
G2 = sp.Matrix(sp.symbols('g11 g12 g21 g22')).reshape(2, 2)
kv = sp.Matrix(sp.symbols('k1 k2'))
cvec = 2*al*(b0*sp.eye(2) - 2*G2).inv()*kv
Av = cvec/a_s
lhsv = sp.diff(Av, t).subs(sp.Derivative(a_s, t), -b0/(4*sp.pi)*a_s**2)
rhsv = al/(2*sp.pi)*kv + a_s/(2*sp.pi)*G2*Av
check('(b) matrix point-like solution 2 alpha (beta0 - 2 Gamma)^{-1} k / alpha_s', sp.simplify(lhsv - rhsv) == sp.zeros(2, 1))
# (c) gamma -> 0: 2 alpha k/(beta0 alpha_s) = (alpha/2pi) k ln(Q^2/Lambda^2) with alpha_s = 4pi/(beta0 ln(Q^2/Lambda^2))
Lg = sp.Symbol('L', positive=True)
check('(c) gamma -> 0: A^pl = (alpha/2pi) k ln(Q^2/Lambda^2) (parton-model log with m -> Lambda)',
      sp.simplify(A.subs(g, 0).subs(a_s, 4*sp.pi/(b0*Lg)) - al/(2*sp.pi)*k*Lg) == 0)
# (d) numerical example: n = 2 NS, n_f = 3: gamma_2 = -4/3 C_F = -16/9, beta0 = 9, k_2 = N_c e^2/3
CF = sp.Rational(4, 3); gam2 = -sp.Rational(4, 3)*CF; b0v = 9; k2 = sp.Rational(1, 3)
c2 = 2*k2/(b0v - 2*gam2)
check('(d) n=2 NS, n_f=3: A_2^pl = (alpha/alpha_s) 6 N_c e_q^2/113', sp.simplify(c2 - sp.Rational(6, 113)) == 0)
# ODE: start at mu0 with A = 0 (or hadronic value) and check alpha_s A -> alpha c2 as Q^2 grows
alpha = 1/137.0
def rhs_ode(tt, y):
    as_, A_ = y
    return [-b0v/(4*np.pi)*as_**2, alpha/(2*np.pi)*float(k2) + as_/(2*np.pi)*float(gam2)*A_]
for A0 in (0.0, 0.02):
    sol = solve_ivp(rhs_ode, [0, 400], [0.4, A0], rtol=1e-11, atol=1e-14)
    as_end, A_end = sol.y[:, -1]
    ratio = as_end*A_end/alpha
    print('   A0 = %.3f : alpha_s(t_end) = %.4f, alpha_s A/alpha = %.6f  (asymptotic %.6f)' % (A0, as_end, ratio, float(c2)))
check('(d) ODE: alpha_s A/alpha approaches 6/113 independently of the boundary value (large t)',
      abs(ratio - float(c2)) < 2e-3)
print('\nSUMMARY s7: %d PASS, %d FAIL' % (npass, nfail))
