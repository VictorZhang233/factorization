# 4D squared matrix elements (summed over all spins/polarizations/colours; couplings
# e^2 e_q^2 g^2 and colour factor C_F N_c stripped) for
#   q(pa) qbar(pb) -> gamma*(q) g(k):  s=(pa+pb)^2, t=(pa-k)^2, u=(pb-k)^2
#   q(pa) g(pb)    -> gamma*(q) q(k):  s=(pa+pb)^2, t=(pa-q)^2, u=(pb-q)^2
# Polarization sums -g for both vector bosons (valid: both currents conserved at this order).
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
from dirac import Dots, trace, contract, D

s, t, u, Q2 = sp.symbols('s t u Q2')

def trace_lin(slots, dot):
    """slots: list; each item is a vector name or a list of (coef, name)"""
    sl = [[(1, x)] if isinstance(x, str) else x for x in slots]
    res = 0
    for combo in itertools.product(*sl):
        c = 1
        for cc, _ in combo:
            c *= cc
        res += c * trace([nm for _, nm in combo], dot)
    return sp.expand(res)

def contract_all(expr, pairs, vecs):
    for (e, f) in pairs:
        expr = contract(expr, e, f, vecs + [p for pr in pairs for p in pr if p not in (e, f)])
    return expr

def msq_qqbar():
    tab = {('pa', 'pa'): 0, ('pb', 'pb'): 0, ('k', 'k'): 0, ('pa', 'pb'): s / 2, ('pa', 'k'): -t / 2, ('pb', 'k'): -u / 2}
    dot = Dots(tab)
    vecs = ['pa', 'pb', 'k']
    A = [(1, 'pa'), (-1, 'k')]          # pa - k  (propagator 1/t)
    B = [(1, 'k'), (-1, 'pb')]          # pa - q = k - pb (propagator 1/u)
    # Tr[ pb Gamma pa Gammabar ],  Gamma = g2 A g1 / t + g1 B g2 / u   (g1: photon, g2: gluon)
    terms = []
    G = [(['e2', A, 'e1'], 1 / t), (['e1', B, 'e2'], 1 / u)]
    Gb = [(['f1', A, 'f2'], 1 / t), (['f2', B, 'f1'], 1 / u)]
    tot = 0
    for (g, cg) in G:
        for (gb, cgb) in Gb:
            tr = trace_lin(['pb'] + g + ['pa'] + gb, dot)
            tot += cg * cgb * tr
    tot = contract(tot, 'e1', 'f1', vecs + ['e2', 'f2'])
    tot = contract(tot, 'e2', 'f2', vecs)
    rep = {}
    for (a, b_), val in tab.items():
        x1, x2 = sorted([a, b_])
        rep[sp.Symbol('dot_%s_%s' % (x1, x2))] = val
    return sp.simplify(tot.subs(rep).subs(D, 4))

def msq_qg():
    # q(pa) g(pb) -> gamma*(q) q(k);  pa.pb=s/2, (pa-k)^2 = (q-pb)^2 = u -> pa.k=-u/2, (pb-k)^2=(q-pa)^2=t -> pb.k=-t/2
    tab = {('pa', 'pa'): 0, ('pb', 'pb'): 0, ('k', 'k'): 0, ('pa', 'pb'): s / 2, ('pa', 'k'): -u / 2, ('pb', 'k'): -t / 2}
    dot = Dots(tab)
    vecs = ['pa', 'pb', 'k']
    S_ = [(1, 'pa'), (1, 'pb')]          # pa + pb  (1/s)
    T_ = [(1, 'k'), (-1, 'pb')]          # pa - q = k - pb (1/t)
    # amplitude ubar(k)[ g1 S g2 / s + g2 T g1 / t ] u(pa)
    G = [(['e1', S_, 'e2'], 1 / s), (['e2', T_, 'e1'], 1 / t)]
    Gb = [(['f2', S_, 'f1'], 1 / s), (['f1', T_, 'f2'], 1 / t)]
    tot = 0
    for (g, cg) in G:
        for (gb, cgb) in Gb:
            tot += cg * cgb * trace_lin(['k'] + g + ['pa'] + gb, dot)
    tot = contract(tot, 'e1', 'f1', vecs + ['e2', 'f2'])
    tot = contract(tot, 'e2', 'f2', vecs)
    rep = {}
    for (a, b_), val in tab.items():
        x1, x2 = sorted([a, b_])
        rep[sp.Symbol('dot_%s_%s' % (x1, x2))] = val
    return sp.simplify(tot.subs(rep).subs(D, 4))

if __name__ == '__main__':
    m1 = msq_qqbar()
    m1Q = sp.factor(sp.simplify(m1.subs(s, Q2 - t - u)))
    print('qqbar -> gamma* g :', m1Q)
    ref1 = 8 * (t / u + u / t + 2 * Q2 * (Q2 - t - u) / (t * u))
    print('  == 8[t/u + u/t + 2 Q^2 s/(t u)] :', sp.simplify(m1Q - ref1) == 0)
    m2 = msq_qg()
    m2Q = sp.factor(sp.simplify(m2.subs(u, Q2 - s - t)))
    print('q g -> gamma* q   :', m2Q)
    ref2 = -8 * (s / t + t / s + 2 * Q2 * (Q2 - s - t) / (s * t))
    print('  == -8[s/t + t/s + 2 Q^2 u/(s t)] :', sp.simplify(m2Q - ref2) == 0)
