# Numerical checks of the rapidity-regulator limits used in DERIVATION.md
#  (1) F_b = 2x(1-x)/((1-x)^2 + s d^2) -> 2x[1/(1-x)]_+ + 2 delta(1-x) ln(1/d)     (s=+1 time-like; s=-1 space-like, PV)
#  (2) F_c(time-like) = -2 d^2 (1-x)/((1-x)^2+d^2)^2 -> -delta(1-x)
#  (3) soft cusp rapidity integral  int dy  lT^2 nA.nB/((nA.l)(nB.l)) = 2 Y coth Y  (both signatures, PV for space-like)
#  (4) delta-regulator (EIS) analogue of (1): 2x(1-x)/((1-x)^2 + r^2), r = delta^+/p^+ -> same with ln(1/r)
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from scipy.integrate import quad

def g(x):  # generic smooth test function
    return np.exp(x) * (1 + x**2)

def plus_part():
    val, _ = quad(lambda x: (2 * x * g(x) - 2 * g(1.0)) / (1 - x), 0, 1, limit=200)
    return val

ok_all = True
print('(1) F_b limit')
for s in (+1, -1):
    for d in (1e-2, 1e-3, 1e-4):
        if s == +1:
            lhs, _ = quad(lambda x: g(x) * 2 * x * (1 - x) / ((1 - x)**2 + d**2), 0, 1, limit=400, points=[1 - d])
        else:
            # PV: write in u=1-x : 2(1-u) g(1-u) u/((u-d)(u+d)) = h(u)/(u-d) with h = 2(1-u)g(1-u)u/(u+d)
            h = lambda u: 2 * (1 - u) * g(1 - u) * u / (u + d)
            lhs, _ = quad(h, 0, 1, weight='cauchy', wvar=d, limit=400)
        rhs = plus_part() + 2 * g(1.0) * np.log(1 / d)
        print('  s=%+d d=%.0e  lhs=%.8f  rhs=%.8f  diff=%.2e' % (s, d, lhs, rhs, lhs - rhs))
    ok_all &= abs(lhs - rhs) < (100 * d if s == +1 else 1000 * d**2)   # O(d) resp. O(d^2) convergence
print('(2) F_c (time-like) limit -> -g(1)')
for d in (1e-2, 1e-3, 1e-4):
    val, _ = quad(lambda x: -g(x) * 2 * d**2 * (1 - x) / ((1 - x)**2 + d**2)**2, 0, 1, limit=400, points=[1 - d, 1 - 10 * d])
    print('  d=%.0e  int = %.8f   -g(1) = %.8f' % (d, val, -g(1.0)))
ok_all &= abs(val + g(1.0)) < 100 * d   # O(d) convergence

print('(3) soft cusp rapidity integral')
def cusp_integral(yA, yB, sig):
    # lT = 1; l = (e^y/sqrt2, e^-y/sqrt2, lT)
    # time-like: nA=(1, e^{-2yA}), nB=(e^{2yB},1); space-like: nA=(1,-e^{-2yA}), nB=(-e^{2yB},1)
    sA = +1 if sig == 't' else -1
    nAnB = 1 + np.exp(2 * (yB - yA))
    nAl = lambda y: np.exp(-y) / np.sqrt(2) + sA * np.exp(-2 * yA) * np.exp(y) / np.sqrt(2)
    nBl = lambda y: np.exp(y) / np.sqrt(2) + sA * np.exp(2 * yB) * np.exp(-y) / np.sqrt(2)
    f = lambda y: nAnB / (nAl(y) * nBl(y))
    L = 40.0
    if sig == 't':
        v, _ = quad(f, -L, L, limit=400, points=[yA, yB])
        return v
    # PV at y=yA and y=yB: subtract poles analytically via symmetric excision
    tot = 0.0
    eta = 1e-7
    pts = sorted([yA, yB])
    edges = [-L, pts[0] - eta, pts[0] + eta, pts[1] - eta, pts[1] + eta, L]
    for a, b in [(edges[0], edges[1]), (edges[2], edges[3]), (edges[4], edges[5])]:
        v, _ = quad(f, a, b, limit=800)
        tot += v
    return tot
for (yA, yB) in [(1.0, -1.0), (3.0, 0.5), (0.3, 0.1), (6.0, -4.0)]:
    Y = yA - yB
    exact = 2 * Y / np.tanh(Y)
    vt = cusp_integral(yA, yB, 't')
    vs = cusp_integral(yA, yB, 's')
    print('  Y=%.2f  time-like=%.8f  space-like(PV)=%.6f  2Y coth Y=%.8f' % (Y, vt, vs, exact))
    ok_all &= abs(vt - exact) < 1e-6 and abs(vs - exact) < 1e-4

print('(4) delta-regulator analogue: same limit with ln(1/r), r=delta^+/p^+')
for r in (1e-3, 1e-4):
    lhs, _ = quad(lambda x: g(x) * 2 * x * (1 - x) / ((1 - x)**2 + r**2), 0, 1, limit=400, points=[1 - r])
    print('  r=%.0e diff=%.2e' % (r, lhs - plus_part() - 2 * g(1.0) * np.log(1 / r)))
print('ALL PASS' if ok_all else 'SOME FAIL')
