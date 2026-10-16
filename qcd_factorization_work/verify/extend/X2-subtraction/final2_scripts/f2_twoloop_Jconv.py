"""X2 final2 / f2_twoloop_Jconv.py -- does the pure-DR (delta = 0) Feynman-parametric integral of a two-loop single
converge absolutely for some real eps?  (Checks the route proposed by the final review, Fix 4(a).)

Feynman (projective) form:  I_R = Gamma(|a| - 2t)/prod Gamma(a_l) * J,  J = int_simplex x^{a-1} U^{|a|-3t} F^{2t-|a|},
t = d/2 = 2 - eps, a = 1 + delta.  U, F have positive coefficients (f2_twoloop_polytopes.py), so on R^6_+ each is
comparable, within constant factors, to its largest monomial; in homogeneous log coordinates x = e^X the modulus of the
integrand is comparable to exp(psi(X)),
     psi(r) = <Re a, r> + (|Re a| - 3 Re t) h_U(r) + (2 Re t - |Re a|) h_F(r),   h_V(r) = max_{v in supp V} <v, r>,
which is positively homogeneous and invariant under r -> r + c(1,...,1).  J converges absolutely iff psi(r) < 0 for
every r not in R(1,...,1) (sufficiency: psi <= -c|r| off the diagonal direction; necessity: if psi(r0) >= 0, psi >= -C on
a tube around the ray R_+ r0, which has infinite measure).  At delta = 0: psi_eps(r) = A(r) + eps B(r) with
A = <1,r> - 2 h_F(r), B = 3 h_U(r) - 2 h_F(r).
DIVERGENCE CERTIFICATE: a finite set of rays r_j with  for every real eps some j has A(r_j) + eps B(r_j) >= 0
(exact rational arithmetic).  Candidate rays: all r in {-1,0,1}^6 and {-2,...,2}^6 (mod the diagonal) .
For eps in (-1, 0) the LP/Feynman equivalence (0 < |a| - 2t < t) gives the same answer as f2_twoloop_polytopes.py."""
import sys, os, json, itertools
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
D = json.load(open(os.path.join(os.path.dirname(HERE), 'final2_logs', 'f2_twoloop_polytopes.json')))
X = sp.symbols('x_g1 x_g2 x_a1 x_a2 x_b1 x_b2', positive=True)
P, Pp, m2 = sp.symbols('P Pp m2', positive=True)

def supp(expr):
    return [tuple(m) for m in sp.Poly(sp.sympify(expr, locals={str(s): s for s in list(X) + [P, Pp, m2]}), *X).monoms()]

def h(S, r): return max(sum(a*b for a, b in zip(v, r)) for v in S)

def analyse(R, rng):
    SU = supp(D[R]['U']); SF = supp(D[R]['F'])
    lo_cover = None; hi_cover = None; whole = None
    best_lo = None; best_hi = None
    for r in itertools.product(rng, repeat=6):
        if len(set(r)) == 1: continue                      # diagonal direction
        A = sum(r) - 2*h(SF, r); B = 3*h(SU, r) - 2*h(SF, r)
        if B == 0:
            if A >= 0: whole = r
            continue
        e0 = Fr(-A, B)
        if B > 0:   # divergent for eps >= e0
            if best_lo is None or e0 < best_lo[0]: best_lo = (e0, r)
        else:       # divergent for eps <= e0
            if best_hi is None or e0 > best_hi[0]: best_hi = (e0, r)
    return whole, best_lo, best_hi

for R in ['HH', 'HC1', 'C1C1', 'HS', 'C1S', 'SS', 'HC2', 'C2C2', 'C2S']:
    for rng in ([-1, 0, 1], [-2, -1, 0, 1, 2]):
        whole, lo, hi = analyse(R, rng)
        if whole is not None:
            verdict = f"divergent for ALL eps (ray {whole}: B = 0, A >= 0)"; cover = True
        else:
            cover = (lo is not None and hi is not None and lo[0] <= hi[0])
            verdict = (f"divergent for eps >= {lo[0]} (ray {lo[1]}) and for eps <= {hi[0]} (ray {hi[1]})"
                       if lo and hi else f"lo={lo}, hi={hi}")
        print(f"{R:5s} rays in {rng[0]}..{rng[-1]}: {verdict}  =>  "
              f"{'NO eps with absolute convergence (certificate)' if cover else 'possible convergence for eps in (' + str(hi[0] if hi else '-oo') + ', ' + str(lo[0] if lo else 'oo') + ') [candidate rays only]'}")
        if cover: break
