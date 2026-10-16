"""X2/T4z: exact LP certificate for the triangle on the negative-k^+ sliver -m2/(2P') < k^+ < 0 (part of U_C2).
Coordinates w = 2k^+ + m2/P' in (0, m2/P'), kap = kT^2.  With P = P' = 1/sqrt2 (a = sqrt2 m2):
  k^- = (P'w + kap)/w, Dg = ((a-w)P'w + a kap)/w, D1 = m2(1 - x/P) + kap + 2k^-(P - x), h1 = 2P k^-,
  rho_Gamma = 2/(w Dg D1), rho_C2 = 2/(w Dg h1), r = rho_Gamma - rho_C2 = -(2/(w Dg)) (m2(1-x/P) + Dg)/(D1 h1).
Positive structure: write a-w = c (also positive, c in (0,a)): split the sliver into w <= a/2 (c ~ a) and w >= a/2 (w ~ a)."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
from fractions import Fraction
from tropical import monomials_of, positive_form
from exact_verify import build, solve_exact
w, c, kap, m2 = sp.symbols('w c kap m2', positive=True)
s2 = sp.sqrt(2)
P = Pp = 1/s2
a = s2*m2
x = (w - a)/2                     # k^+ (negative)
km = (Pp*w + kap)/w
# write all factors as explicitly positive polynomials (times monomials) using c = a - w  (c, w > 0)
Dg_num = c*Pp*w + a*kap          # Dg = Dg_num / w
# D1 = m2(1 - x/P) + kap + 2 km (P - x) ; with -x = c/2 (since x = (w-a)/2 = -c/2): 1 - x/P = 1 + c/(2P), P - x = P + c/2
D1_num = (m2*(1 + c/(2*P)) + kap)*w + 2*(Pp*w + kap)*(P + c/2)        # D1 = D1_num / w
h1_num = 2*P*(Pp*w + kap)                                               # h1 = h1_num / w
# r = -(2/(w Dg))(m2(1-x/P) + Dg)/(D1 h1) = -2 w^2 (m2(1 + c/(2P)) w + Dg_num) / (Dg_num D1_num h1_num) * (1/w)... careful:
# 1/(w Dg) = 1/Dg_num ; (m2(1-x/P) + Dg) = (m2(1+c/(2P)) w + Dg_num)/w ; 1/(D1 h1) = w^2/(D1_num h1_num)
num = -2*(m2*(1 + c/(2*P))*w + Dg_num)*w
dens = [Dg_num, D1_num, h1_num]
num = sp.expand(num); dens = [sp.expand(d) for d in dens]
for d in dens:
    print("den factor:", d)
# measure: dk^+ dkap = (dw/2) dkap ; sub-domain A: w <= a/2 -> c ~ a (freeze c -> m2), local (w, kap), Xw <= -1
# sub-domain B: w >= a/2 -> w ~ a (freeze w -> m2), local (c, kap), Xc <= -1
def cert(label, local, frozen, cons):
    N = sp.expand(num.subs(frozen)); dl = [sp.expand(d.subs(frozen)) for d in dens]
    # numerical constants sqrt2 are fine (positive); positive_form checks signs
    mons = monomials_of(N, local, m2); forms = [positive_form(g, local, m2) for g in dl]
    G = [list(cc) for cc, _ in cons]; h = [r for _, r in cons]
    worst = None; fails = 0
    for cf, al in mons:
        rows, rhs, cc, const = build(al, forms, [1]*len(local), G, h, len(local))
        out, msg = solve_exact(rows, rhs, cc, const)
        if out is None: fails += 1; continue
        worst = out[0] if (worst is None or out[0] > worst) else worst
    print(f"[{label}] exact phi* = {worst} -> lambda^{-2*worst};  failures {fails}")
cert('sliver A (w<=a/2)', [w, kap], {c: m2}, [([1, 0], -1)])
cert('sliver B (w>=a/2)', [c, kap], {w: m2}, [([1, 0], -1)])
