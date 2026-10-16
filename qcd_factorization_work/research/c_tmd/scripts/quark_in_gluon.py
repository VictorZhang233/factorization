# One-loop TMD of a quark in an on-shell gluon (D = 4-2eps), real graph g -> q qbar, the quark
# enters the operator.  Target-gluon polarizations: physical transverse ones (eps^+ = eps^- = 0),
# averaged over D-2 = 2-2eps states (MSbar convention for gluon targets, cf. blueprint 0.4(5)).
# With n.eps = 0 the Wilson-line term ~ n.eps/(n.p) vanishes.
#   f(x,kT) = g^2 T_F/(2(2pi)^(D-1) 2 l^+) * (1/(D-2)) sum_T Tr[ lslash eps* kslash gamma^+ kslash eps ]/k^4
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
from dirac import Dots, trace, contract, D

x, pp, kT2, eps = sp.symbols('x p_plus kT2 epsilon', real=True)
lp = (1 - x) * pp
lm = kT2 / (2 * lp)
# vectors: p (gluon target), l (antiquark), k = p - l, v (v.a = a^+), w (w.a = a^-)
# components (plus, minus, T):  p=(pp,0,0), l=(lp,lm,-kT), k=(x pp,-lm,kT), v=(0,1,0), w=(1,0,0)
def lc(a, b):
    return a[0] * b[1] + a[1] * b[0] - a[2] * b[2]
kT = sp.sqrt(kT2)
comp = {'p': (pp, 0, 0), 'l': (lp, lm, -kT), 'k': (x * pp, -lm, kT), 'v': (0, 1, 0), 'w': (1, 0, 0)}
names = list(comp)
tab = {}
for i, a in enumerate(names):
    for b_ in names[i:]:
        tab[(a, b_)] = sp.simplify(lc(comp[a], comp[b_]))
dot = Dots(tab)
def subs_dots(expr):
    rep = {}
    for (a, b_), val in tab.items():
        s1, s2 = sorted([a, b_])
        rep[sp.Symbol('dot_%s_%s' % (s1, s2))] = val
    return sp.simplify(expr.subs(rep))

ksq = tab[('k', 'k')]
# -g_T^{mu nu} X_mu Y_nu = -X.Y + (X.v)(Y.w) + (X.w)(Y.v)
full = contract(trace(['l', 'f', 'k', 'v', 'k', 'e'], dot), 'e', 'f', names)   # g_{mu nu} contraction
t_vw = trace(['l', 'w', 'k', 'v', 'k', 'v'], dot)    # e->v (index mu), f->w (index nu)
t_wv = trace(['l', 'v', 'k', 'v', 'k', 'w'], dot)
TgT = subs_dots(-full + t_vw + t_wv)
TgT = sp.simplify(TgT.subs(D, 4 - 2 * eps))
F = sp.simplify(TgT / (2 - 2 * eps) / ksq**2 / (4 * lp) * kT2)   # coefficient of g^2 T_F/(2pi)^(D-1)/kT^2
print('F_{q/g}(x) =', sp.factor(F))
expected = (x**2 + (1 - x)**2 - eps) / (1 - eps)
print('PASS F == [x^2+(1-x)^2-eps]/(1-eps) = 1 - 2x(1-x)/(1-eps):', sp.simplify(F - expected) == 0)
# b space: multiply by A(eps) = -1/eps - L_b - eps(L_b^2/2 + c) ; finite part:
Lb = sp.Symbol('L_b')
A = -1 / eps - Lb + eps * sp.Symbol('c2')
fin = sp.series(sp.expand(A * expected), eps, 0, 1).removeO()
print('b-space one-loop (units alpha_s T_F/2pi):', sp.collect(sp.expand(fin), eps))
print('=> pole -(x^2+(1-x)^2)/eps = -P_qg/(T_F eps) [IR, matches PDF]; finite: -L_b P_qg/T_F + 2x(1-x)')
print('PASS C~_{q/g}(mu_b) = (alpha_s T_F/2pi) 2x(1-x):',
      sp.simplify(fin.coeff(eps, 0).subs(Lb, 0) - 2 * x * (1 - x)) == 0)
