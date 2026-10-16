"""R-M4 (second, independent verification run): Feynman rules of straight Wilson lines from the path-ordered
exponential, CONTEXT conventions: D = d - i g A^a t^a, W[b,a] = P exp(i g Int_a^b dz.A) (points closer to b on the left).
Gluon fields with momentum k_j flowing INTO the line: A_j(x) ~ eps_j t^{a_j} exp(-i k_j.x); adiabatic damping.

 past   W[0,-inf n] = P exp(i g Int_{-inf}^0 dl n.A(l n)),  vertices l_1 < ... < l_m < 0 (k_1 farthest):
        claimed: (ig)^m t^{a_m}...t^{a_1} prod_j n^{mu_j} * prod_{j=1}^m i/(n.(k_1+...+k_j) + i0)
 future W[inf n,0]  = P exp(i g Int_0^{inf} dl n.A(l n)),   vertices 0 < l_1 < ... < l_m (k_m farthest):
        claimed: (ig)^m t^{a_m}...t^{a_1} prod_j n^{mu_j} * prod_{j=1}^m (-i)/(n.(k_j+...+k_m) - i0)
Also: the reference's (2.7) W^(+-)(x) = P exp(-i g Int_0^{+-inf} dl v.A(x+l v)) (far points on the right) at first
order, compared with its Fig. 4 ('vertex i g v t, propagator i/(v.k +- i0), +/- = future/past').
The ordered integrals are evaluated symbolically (sympy) with x_j = n.k_j and damping eps > 0, then eps -> 0.
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
LOG = []
def rep(tag, ok, msg=''):
    s = f"[{'PASS' if ok else 'FAIL'}] {tag}: {msg}"; LOG.append(s); print(s, flush=True)

eps = sp.symbols('epsilon', positive=True)
x = sp.symbols('x1:4', real=True)       # x_j = n.k_j
l = sp.symbols('l1:4', real=True)

# Iterated integrals of pure exponentials, done with the exact antiderivative rule (checked numerically below):
#   Int_{-inf}^{u} e^{c l} dl = e^{c u}/c  (Re c > 0),   Int_{u}^{inf} e^{c l} dl = -e^{c u}/c  (Re c < 0).
def past_integral(m):
    # Int_{l_1<...<l_m<0} prod_j exp(c_j l_j), c_j = -i x_j + eps  (integrate l_1 up to l_2, ..., l_m up to 0)
    coef = sp.Integer(1); c_acc = 0
    for j in range(m):
        c_acc = c_acc + (-sp.I*x[j] + eps)
        coef = coef/c_acc          # e^{c_acc l_{j+1}} remains; last step evaluated at l = 0
    return sp.simplify(coef)
def future_integral(m):
    # Int_{0<l_1<...<l_m} prod_j exp(c_j l_j), c_j = -i x_j - eps (integrate l_m from l_{m-1} to inf, ..., l_1 from 0)
    coef = sp.Integer(1); c_acc = 0
    for j in reversed(range(m)):
        c_acc = c_acc + (-sp.I*x[j] - eps)
        coef = -coef/c_acc
    return sp.simplify(coef)
# numerical spot check of the rule against brute-force quadrature (m = 2)
import mpmath as mp
xv = [mp.mpf('0.7'), mp.mpf('-1.3')]; ev = mp.mpf('0.4')
bf_p = mp.quad(lambda l2: mp.exp((-1j*xv[1]+ev)*l2)*mp.quad(lambda l1: mp.exp((-1j*xv[0]+ev)*l1), [-60, l2]), [-60, 0])
bf_f = mp.quad(lambda l1: mp.exp((-1j*xv[0]-ev)*l1)*mp.quad(lambda l2: mp.exp((-1j*xv[1]-ev)*l2), [l1, l1+60]), [0, 60])
sub = {x[0]: sp.Float('0.7'), x[1]: sp.Float('-1.3'), eps: sp.Float('0.4')}
okn = abs(complex(past_integral(2).subs(sub)) - complex(bf_p)) < 1e-8 and abs(complex(future_integral(2).subs(sub)) - complex(bf_f)) < 1e-8
rep('antiderivative rule vs brute-force quadrature (m=2, finite damping)', okn, f'past {complex(bf_p):.8f}, future {complex(bf_f):.8f}')

for m in (1, 2, 3):
    P = past_integral(m)
    claim_P = sp.prod([sp.I/(sum(x[:j+1]) + sp.I*eps*(j+1)) for j in range(m)])
    okP = sp.simplify(P - claim_P) == 0
    F = future_integral(m)
    claim_F = sp.prod([(-sp.I)/(sum(x[j:m]) - sp.I*eps*(m-j)) for j in range(m)])
    okF = sp.simplify(F - claim_F) == 0
    rep(f'm={m}: past W[0,-inf n] ordered integral = prod_j i/(n.(k_1+..+k_j)+i0)', okP, f'{sp.simplify(P)}')
    rep(f'm={m}: future W[inf n,0] ordered integral = prod_j (-i)/(n.(k_j+..+k_m)-i0)', okF, f'{sp.simplify(F)}')
# (the damping accumulates j*eps along the partial sums: any positive multiple of eps is the same i0)

# Reference (2.7) at first order, incoming k (exp(-i k.x)), vertex factor written as (i g v t) * propagator:
X = sp.symbols('X', real=True)    # X = v.k
lam = sp.symbols('lam', real=True)
fut_27 = -sp.I*(-1/(-sp.I*X - eps))      # -ig Int_0^inf e^{(-iX-eps) l} dl
past_27 = sp.I*(1/(-sp.I*X + eps))       # -ig Int_0^{-inf} = +ig Int_{-inf}^0 e^{(-iX+eps) l} dl
# divide by the vertex i (g v t stripped): propagator = term/(i)
prop_fut_27 = sp.simplify(fut_27/sp.I); prop_past_27 = sp.simplify(past_27/sp.I)
rep('(2.7) W^(+) [future], incoming k: propagator = i/(v.k - i0) with vertex +i g v t', sp.simplify(prop_fut_27 - sp.I/(X - sp.I*eps)) == 0, f'{prop_fut_27}')
rep('(2.7) W^(-) [past], incoming k: propagator = i/(v.k + i0) with vertex +i g v t', sp.simplify(prop_past_27 - sp.I/(X + sp.I*eps)) == 0, f'{prop_past_27}')
# outgoing k (exp(+i k.x)) for comparison
fut_27o = sp.simplify(-sp.I*(-1/(sp.I*X - eps))/sp.I)
past_27o = sp.simplify(sp.I*(1/(sp.I*X + eps))/sp.I)
rep('(2.7) outgoing k: future -> -i/(v.k + i0), past -> -i/(v.k - i0) (numerator sign opposite to Fig. 4)',
    sp.simplify(fut_27o + sp.I/(X + sp.I*eps)) == 0 and sp.simplify(past_27o + sp.I/(X - sp.I*eps)) == 0, f'future {fut_27o}, past {past_27o}')
# Fig. 4 last row: incoming quark u(p) absorbing soft k: i(p+k)/((p+k)^2+i0) i g gamma t u(p) -> -g p/(p.k+i0) t u(p)
# = (i g p t) * i/(p.k + i0): '+i0' belongs to an incoming (past-pointing) line, opposite to Fig. 4 row 1 labelling.
pk = sp.symbols('pk', real=True)
row3 = (sp.I*sp.I)/(pk + sp.I*eps)      # (i g p t)(i/(p.k+i0)) / (g p t) = -1/(p.k + i0)
rep('Fig. 4 last row (incoming quark absorbing k) = vertex i g p t x i/(p.k + i0): +i0 <-> past line', sp.simplify(row3 + 1/(pk + sp.I*eps)) == 0,
    'matches (2.7) past with incoming k; Fig. 4 row 1 assigns +i0 to the future line')
print('\nSUMMARY:', sum('PASS' in s for s in LOG), 'PASS,', sum('FAIL' in s for s in LOG), 'FAIL')
