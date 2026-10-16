"""W12 (Ch10): quark channel gamma*(q)+q(p)->q(pp)+g(k): the physical (light-cone) polarization sum
   -g_{rho sigma} + (k_rho n_sigma + n_rho k_sigma)/(n.k) gives the same projected |M|^2 as -g_{rho sigma}
   (both projections, D dims).  Same conventions and trace engine as w12_nlo.py.
Run:  python3 -I w12_nlo_polcheck.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
from dtrace import trace, V, I, D

eps, Q2 = sp.symbols('epsilon Q2', positive=True)
s, t, u = sp.symbols('s t u')
nk, np_, npp, nq = sp.symbols('nk np npp nq')

def dot_q(a, b):
    a, b = sorted((a, b))
    tab = {('p', 'p'): 0, ('k', 'k'): 0, ('pp', 'pp'): 0, ('q', 'q'): -Q2,
           ('p', 'q'): (s + Q2) / 2, ('k', 'p'): -t / 2, ('p', 'pp'): -u / 2,
           ('k', 'q'): -(u + Q2) / 2, ('k', 'pp'): s / 2, ('pp', 'q'): (s + u) / 2,
           ('n', 'n'): 0, ('n', 'p'): np_, ('k', 'n'): nk, ('n', 'pp'): npp, ('n', 'q'): nq}
    return tab[(a, b)]

def string_q(proj, polsum):
    A = [('p', 1), ('q', 1)]        # s-channel numerator p+q
    B = [('p', 1), ('k', -1)]       # t-channel numerator p-k
    mu = I('mu') if proj == 'g' else V('p')
    amp = [([I('rho'), 'A', mu], 1 / s), ([mu, 'B', I('rho')], 1 / t)]
    cnj = [([mu, 'A', I('sig')], 1 / s), ([I('sig'), 'B', mu], 1 / t)]
    def expand(seq):
        out = [([], 1)]
        for el in seq:
            if el in ('A', 'B'):
                lst = A if el == 'A' else B
                out = [(sl + [V(v)], c * w) for sl, c in out for v, w in lst]
            else:
                out = [(sl + [el], c) for sl, c in out]
        return out
    res = sp.Integer(0)
    sgn_proj = -1 if proj == 'g' else 1
    for ga, ca in amp:
        for gc, cc in cnj:
            for sa, wa in expand(ga):
                for sc, wc in expand(gc):
                    base = [V('pp')] + sa + [V('p')] + sc
                    # -g_{rho sigma} part
                    sl = [(I('rho') if x == I('sig') else x) for x in base]
                    res += sgn_proj * (-1) * ca * cc * wa * wc * trace(sl, dot_q)
                    if polsum == 'lc':
                        for (r1, r2) in (('k', 'n'), ('n', 'k')):
                            sl2 = [(V(r1) if x == I('rho') else (V(r2) if x == I('sig') else x)) for x in base]
                            res += sgn_proj * ca * cc * wa * wc * trace(sl2, dot_q) / nk
    return sp.expand(res)

for proj in ('g', 'pp'):
    d = string_q(proj, 'lc') - string_q(proj, 'g')
    # momentum conservation for the auxiliary vector: n.pp = n.p + n.q - n.k
    d = sp.simplify(d.subs(npp, np_ + nq - nk).subs(u, -Q2 - s - t).subs(D, 4 - 2 * eps))
    print('quark channel, projection', proj, ': light-cone sum - (-g) sum =', d, '->', 'PASS' if d == 0 else 'FAIL')
