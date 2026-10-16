"""Independent check of Example F.3: one-loop forward triangle, lines k^2 (a_x), (k+p)^2, (k+p+q)^2, p^2=0, q^2=-Q^2=-1.
F = Q^2 [alpha_2 alpha_3 + alpha_1 alpha_3 (1-omega)] for lines (1: k, 2: k+p, 3: k+p+q).
Compare Feynman-parameter quadrature with the report's closed form for every assignment of (a1,a2,a3) to lines."""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 20
def closed(a1, a2, a3, D, w):
    a = a1 + a2 + a3
    return mp.gamma(a - D/2) / (mp.gamma(a1) * mp.gamma(a2) * mp.gamma(a3)) * mp.beta(D/2 - a2, D/2 - a1 - a3) * mp.beta(a1, a3) * mp.hyp2f1(a - D/2, a1, a1 + a3, w)
def param(b1, b2, b3, D, w):
    # b_i = power of line i (1: k, 2: k+p, 3: k+p+q); simplex alpha1+alpha2+alpha3 = 1 (U = 1)
    a = b1 + b2 + b3
    def f(x, y):   # alpha1 = x*(1-y), alpha2 = (1-x)*(1-y), alpha3 = y ; Jacobian (1-y)
        al1 = x * (1 - y); al2 = (1 - x) * (1 - y); al3 = y
        F = al2 * al3 + al1 * al3 * (1 - w)
        return al1 ** (b1 - 1) * al2 ** (b2 - 1) * al3 ** (b3 - 1) * F ** (D/2 - a) * (1 - y)
    val = mp.quad(f, [0, 1], [0, 1])
    return mp.gamma(a - D/2) / (mp.gamma(b1) * mp.gamma(b2) * mp.gamma(b3)) * val
a1, a2, a3, D = mp.mpf('0.6'), mp.mpf('0.7'), mp.mpf('0.5'), mp.mpf('3.3')
for w in (mp.mpf('0.3'), mp.mpc('0.2', '0.5'), mp.mpc('-1.5', '0.4')):
    c = closed(a1, a2, a3, D, w)
    best = []
    for perm in itertools.permutations([(1, a1), (2, a2), (3, a3)]):
        # perm assigns powers to lines 1,2,3
        b = [p[1] for p in perm]
        v = param(b[0], b[1], b[2], D, w)
        best.append((abs(v / c - 1), [p[0] for p in perm]))
    best.sort(key=lambda t: t[0])
    print("omega =", w, " closed =", mp.nstr(c, 12), " best assignment (a-index on lines k, k+p, k+p+q):", best[0][1], " rel.dev = %.2e" % float(best[0][0]))
