# One-loop real-emission graphs of the (unsubtracted) TMD of a quark in an on-shell
# massless quark, Feynman gauge, D = 4-2eps, Wilson line along a general vector n
# (n^+, n^-, 0_T).  Conventions: binding conventions of CONTEXT.md.
#   f(x,kT) = (g^2 C_F/(2pi)^(D-1)) * T/(4 l^+),   l = p - k  (real gluon), l^+=(1-x)p^+
#   T = (1/2) sum_s sum_pol  Mbar gamma^+ M   (colour factor C_F and g^2 stripped)
# M^mu = -[ kslash gamma^mu/(k^2) + n^mu/(n.l + i0) ] u(p)   (SIDIS; DY: n.l - i0)
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
from dirac import Dots, trace, contract, D

x, pp, kT2, npl, nmi, eps = sp.symbols('x p_plus kT2 n_plus n_minus epsilon', real=True)
lm = kT2 / (2 * (1 - x) * pp)          # l^- of the on-shell gluon
lp = (1 - x) * pp                       # l^+
ksq = -2 * pp * lm                      # k^2 = (p-l)^2 = -2 p.l
tab = {('p', 'p'): 0, ('p', 'k'): -pp * lm, ('p', 'n'): pp * nmi, ('p', 'v'): pp,
       ('k', 'k'): ksq, ('k', 'n'): -npl * lm + nmi * x * pp, ('k', 'v'): x * pp,
       ('n', 'n'): 2 * npl * nmi, ('n', 'v'): npl, ('v', 'v'): 0}
dot = Dots(tab)
vecs = ['p', 'k', 'n', 'v']

def subs_dots(expr):
    rep = {}
    for (a, b), val in tab.items():
        s1, s2 = sorted([a, b])
        rep[sp.Symbol('dot_%s_%s' % (s1, s2))] = val
    return sp.simplify(expr.subs(rep))

# (a) quark-quark:  -g_{mu nu} (1/2) Tr[p f k v k e] / k^4
Taa = -sp.Rational(1, 2) * contract(trace(['p', 'f', 'k', 'v', 'k', 'e'], dot), 'e', 'f', vecs) / ksq**2
Taa = subs_dots(Taa.subs(D, 4 - 2 * eps))
# (b) quark-Wilson (+ mirror); the two traces are equal -> 2*PV(1/n.l)
tr_b1 = -sp.Rational(1, 2) * contract(trace(['p', 'f', 'k', 'v'], dot) * sp.Symbol('dot_e_n'), 'e', 'f', vecs)
tr_b2 = -sp.Rational(1, 2) * contract(trace(['p', 'v', 'k', 'e'], dot) * sp.Symbol('dot_f_n'), 'e', 'f', vecs)
tr_b1, tr_b2 = subs_dots(tr_b1), subs_dots(tr_b2)
nl = npl * lm + nmi * lp                # n.l
Tab_numer = sp.simplify(tr_b1 / ksq)    # multiplies [1/(n.l+i0) + 1/(n.l-i0)] = 2 PV/(n.l)
# (c) Wilson-Wilson
Tbb_numer = subs_dots(-sp.Rational(1, 2) * sp.Symbol('dot_n_n') * trace(['p', 'v'], dot))  # times 1/|n.l|^2

F_a = sp.simplify(Taa / (4 * lp) * kT2)
F_b = sp.simplify(Tab_numer * 2 / nl / (4 * lp) * kT2)
F_c = sp.simplify(Tbb_numer / nl**2 / (4 * lp) * kT2)
print('trace check b1 == b2 :', sp.simplify(tr_b1 - tr_b2) == 0)
print('F_a (coefficient of g^2 C_F/(2pi)^(D-1)/kT^2):', sp.factor(F_a))
print('F_b general n                               :', sp.factor(F_b))
print('F_c general n                               :', sp.factor(F_c))
# light-like n = (0,1,0): n.l = l^+
print('F_b light-like (n^+=0, n^-=1):', sp.simplify(F_b.subs({npl: 0, nmi: 1})))
print('F_c light-like               :', sp.simplify(F_c.subs({npl: 0, nmi: 1})))
# non-light-like n_B(y_B) = (s*exp(2yB), 1, 0); s=-1 space-like (Collins), s=+1 time-like
yB, s, dlt = sp.symbols('y_B s delta', real=True)
FbB = sp.simplify(F_b.subs({npl: s * sp.exp(2 * yB), nmi: 1}))
FcB = sp.simplify(F_c.subs({npl: s * sp.exp(2 * yB), nmi: 1}))
# express through delta^2 = e^{2 yB} kT^2/(2 p+^2)
rep = {kT2: 2 * pp**2 * dlt**2 * sp.exp(-2 * yB)}
print('F_b(n_B) in terms of delta:', sp.factor(sp.simplify(FbB.subs(rep))))
print('F_c(n_B) in terms of delta:', sp.factor(sp.simplify(FcB.subs(rep))))
# expected forms
exp_a = (1 - eps) * (1 - x)
exp_b = 2 * x * (1 - x) / ((1 - x)**2 + s * dlt**2)
exp_c = -s * 2 * dlt**2 * (1 - x) / ((1 - x)**2 + s * dlt**2)**2
print('PASS F_a == (1-eps)(1-x)            :', sp.simplify(F_a - exp_a) == 0)
print('PASS F_b == 2x(1-x)/((1-x)^2+s d^2) :', sp.simplify(FbB.subs(rep) - exp_b) == 0)
print('PASS F_c == -2 s d^2(1-x)/(...)^2   :', sp.simplify(FcB.subs(rep) - exp_c) == 0)
