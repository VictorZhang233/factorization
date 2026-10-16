"""validate lcpt engine on the one-loop triangle (closed forms of T1) with random generic weights."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from lcpt import Factor, iterated_residue
rng = np.random.default_rng(7)
N = 2000
P, Pp, m2 = 0.8, 1.3, 0.02
x = np.concatenate([rng.uniform(-m2/(2*Pp), 0, N//4), rng.uniform(0, P, N//2), rng.uniform(P, 3*P, N - N//4 - N//2)])
kap = 10**rng.uniform(-5, 1, N)
W = lambda: rng.uniform(0.5, 2.0)
# factors as functions of km: D = a + b*km - i eta w
def Dg(): return Factor(kap, [-2*x], W())
def D1(): return Factor(m2 - (m2/P)*x + kap, [2*P - 2*x], W())
def D2(): return Factor(m2 + 2*Pp*x + kap, [-(m2/Pp) - 2*x], W())
def e1(): return Factor(m2 + 0*x, [2*P + 0*x], W())
def h1(): return Factor(0*x, [2*P + 0*x], W())
def t1(): return Factor(kap, [2*P - 2*x], W())
def e2(): return Factor(m2 + 2*Pp*x, [0*x], W())
def h2(): return Factor(2*Pp*x, [0*x], W())
def t2(): return Factor(2*Pp*x + kap, [-2*x], W())
def num(F): # rho = (1/(i pi)) int dkm F
    return iterated_residue(F, 1)/(1j*np.pi)
rG = num([Dg(), D1(), D2()])
rS = num([Dg(), e1(), e2()])
rC1 = num([Dg(), D1(), h2()]) - num([Dg(), e1(), h2()])
rC2 = num([Dg(), h1(), D2()]) - num([Dg(), h1(), e2()])
rH = num([Factor(kap, [-2*x], 0.0, e=-1), t1(), h1(), t2(), h2()])
# closed forms
A = x*m2*(1 - x/P) + P*kap; B = x*m2 + P*kap; E2 = m2 + 2*Pp*x; H2 = 2*Pp*x; a2 = m2/Pp
mid = (x > 0) & (x < P); big = x >= P; neg = x <= 0
k1m = -(m2*(1 - x/P) + kap)/(2*(P - x))
def Dgv(km): return -(2*x*km - kap)
def D2v(km): return m2 + 2*Pp*x - (m2/Pp)*km - (2*x*km - kap)
def D1v(km): return m2 + 2*P*km - (m2/P)*x - (2*x*km - kap)
k2m = (m2 + 2*Pp*x + kap)/(a2 + 2*x)
cG = np.where(mid, 1/((P - x)*Dgv(k1m)*D2v(k1m)), np.where(neg, 2/((a2 + 2*x)*Dgv(k2m)*D1v(k2m)), 0))
cS = np.where(x > 0, 1/(B*E2), 0)
cC1 = np.where(mid, x*m2/(2*P*Pp*A*B), np.where(big, -1/(2*Pp*x*B), 0))
cC2 = np.where(x > 0, -(1/P)/((E2 + kap)*E2), 2/((a2 + 2*x)*Dgv(k2m)*2*P*k2m))
cH = np.where(mid, -x/(P*(H2 + kap)*(H2*(P - x) + P*kap)), np.where(big, 1/(P*(H2 + kap)*H2), 0))
for nm, a, b in [('Gamma', rG, cG), ('C_S', rS, cS), ('C_C1', rC1, cC1), ('C_C2', rC2, cC2), ('C_H', rH, cH)]:
    err = np.max(np.abs(a - b)/(np.abs(b) + 1e-12*np.max(np.abs(b))))
    print(f"{nm:6s}: max rel deviation engine vs closed form over {N} points: {err:.2e}; max |Im| = {np.max(np.abs(np.imag(a))):.1e}")
