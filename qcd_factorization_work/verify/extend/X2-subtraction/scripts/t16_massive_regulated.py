"""X2/T16: massive-photon one-loop vertex with rapidity-regulated soft approximator.
 time-like  : h1Y = 2P(k^- + e^{-2Y} k^+),  h2Y = 2P'(k^+ + e^{-2Y} k^-)   (n_A = (1, e^{-2Y}, 0) time-like)
 space-like : h1Y = 2P(k^- - e^{-2Y} k^+),  h2Y = 2P'(k^+ - e^{-2Y} k^-)
T_S: (t1,t2) -> (h1Y,h2Y); T_C1: t2 -> h2 (light-like); T_C2: t1 -> h1; T_H: G -> g0.  C_R by the recursion.
Checks at fixed (x=k^+, kap): (a) rapidity integrability of C_S in x (fixed kap); (b) the space-like pinch: rho_{C_S}
has a pole at 2 e^{-2Y} x^2 = M^2 + kap; (c) remainder norm vs Y and lambda."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, warnings
from scipy import integrate
from lcpt import Factor, iterated_residue
warnings.filterwarnings('ignore')
P = Pp = 1/np.sqrt(2)

def terms(x, kap, M2, Y, sgn):
    e = sgn*np.exp(-2*Y)
    mk = {
     'G':   lambda: Factor(M2 + kap + 0*x, [-2*x], 1.03),
     'g0':  lambda: Factor(kap + 0*x, [-2*x], 0.97),
     't1':  lambda: Factor(kap + 0*x, [2*P - 2*x], 1.11),
     't2':  lambda: Factor(2*Pp*x + kap, [-2*x], 0.89),
     'h1':  lambda: Factor(0*x, [2*P + 0*x], 1.21),
     'h2':  lambda: Factor(2*Pp*x, [0*x], 0.79),
     'h1Y': lambda: Factor(2*P*e*x, [2*P + 0*x], 1.17),
     'h2Y': lambda: Factor(2*Pp*x, [2*Pp*e + 0*x], 0.83),
    }
    Gam = [(1, ['G', 't1', 't2'])]
    CS = [(1, ['G', 'h1Y', 'h2Y'])]
    CC1 = [(1, ['G', 't1', 'h2']), (-1, ['G', 'h1Y', 'h2'])]
    CC2 = [(1, ['G', 'h1', 't2']), (-1, ['G', 'h1', 'h2Y'])]
    X = Gam + [(-c, fl) for c, fl in CS + CC1 + CC2]
    CH = [(c, ['g0' if t == 'G' else t for t in fl]) for c, fl in X]
    r = X + [(-c, fl) for c, fl in CH]
    tab = {'Gamma': Gam, 'C_S': CS, 'C_C1': CC1, 'C_C2': CC2, 'C_H': CH, 'r': r}
    return {k: [(c, [mk[t]() for t in fl]) for c, fl in v] for k, v in tab.items()}

def rho(name, x, kap, M2, Y, sgn):
    tot = 0.0
    for c, fl in terms(np.atleast_1d(x), np.atleast_1d(kap), M2, Y, sgn)[name]:
        tot = tot + c*iterated_residue(fl, 1)
    return np.real(np.atleast_1d(tot)/(1j*np.pi))

if __name__ == "__main__":
    M2 = 1e-3
    print("(a) rapidity integrability at fixed kap=0.01: int dx rho_{C_S} over x in (e^-30, e^X):")
    for sgn, lab in [(1, 'time-like'), (-1, 'space-like')]:
        for Y in [3.0, 6.0]:
            vals = []
            for Xc in [5, 10, 20]:
                f = lambda lx: rho('C_S', np.exp(lx), 0.01, M2, Y, sgn)[0]*np.exp(lx)
                pts = None
                v = integrate.quad(f, -30, Xc, limit=400)[0]
                vals.append(v)
            print(f"   {lab:10s} Y={Y}: cutoffs e^5,e^10,e^20 -> {vals}")
    # (b) pinch for space-like: scan rho_{C_S} near x0 = sqrt((M2+kap) e^{2Y}/2)
    Y = 3.0; kap = 0.01; x0 = np.sqrt((M2 + kap)*np.exp(2*Y)/2)
    xs = x0*(1 + np.array([-1e-2, -1e-3, -1e-4, 1e-4, 1e-3, 1e-2]))
    print("(b) space-like rho_{C_S} near x0=%.4f:" % x0, rho('C_S', xs, kap, M2, Y, -1))
    print("    time-like  rho_{C_S} near x0     :", rho('C_S', xs, kap, M2, Y, +1))
    # (c) remainder norms, time-like, vs Y
    print("(c) time-like regulated remainder: int r, int|r| (eps=0), lambda^2 = M2")
    for M2 in [1e-2, 1e-3, 1e-4]:
        L = np.log(1/M2)
        for Y in [0.5*L, 1.0*L, 1.5*L, 2.0*L, 4.0*L]:
            f = lambda lk, lx: rho('r', np.exp(lx), np.exp(lk), M2, Y, 1)[0]*np.exp(lx)*np.exp(lk)
            fa = lambda lk, lx: abs(f(lk, lx))
            I = integrate.dblquad(f, -40, 3*Y + 10, lambda t: -40, lambda t: 10, epsrel=1e-6)[0]
            N = integrate.dblquad(fa, -40, 3*Y + 10, lambda t: -40, lambda t: 10, epsrel=1e-6)[0]
            print(f"   M2={M2:.0e} Y={Y:6.2f} (Y/L={Y/L:.1f}): int r = {I:+.5e} ({I/M2:+.3f} lam^2)  norm = {N:.5e} ({N/(M2*L):.3f} lam^2 L)", flush=True)
