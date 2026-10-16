"""X2/T13: abelian one-loop vertex with massive photon (mass M), on-shell massless legs p1=(P,0,0), p2=(0,-P',0),
Q^2 = 2PP'.  Gamma = 1/(G t1 t2), G = M^2-k^2, t1 = 2P k^- - k^2, t2 = 2P' k^+ - k^2, h1 = 2P k^-, h2 = 2P' k^+, g0=-k^2.
Light-like Collins approximators: T_S:(t1,t2)->(h1,h2); T_C1: t2->h2; T_C2: t1->h1; T_H: G->g0.
  C_S = 1/(G h1 h2), C_C1 = (1/(G h2))(1/t1-1/h1), C_C2 = (1/(G h1))(1/t2-1/h2), C_H = (1/g0)(1/t1-1/h1)(1/t2-1/h2),
  r = (1/G - 1/g0)(1/t1-1/h1)(1/t2-1/h2) = -M^2 g0/(G t1 h1 t2 h2).
Rapidity-regulated soft approximator (REPORT Def. D.9):  h1 -> h1Y = 2P(k^- - e^{-2Y} k^+), h2 -> h2Y = 2P'(k^+ - e^{-2Y} k^-)
in T_S only (collinear approximators light-like).
Checks: (1) int rho_Gamma = exact Jantzen formula; (2) rho_{C_S} is not integrable (rapidity divergence), for every eps;
(3) the light-like remainder is integrable: int r and int|rho_r| vs lambda=M/Q; (4) regulated version vs Y."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, mpmath as mp, warnings
from scipy import integrate
from lcpt import Factor, iterated_residue
warnings.filterwarnings('ignore')
P = Pp = 1/np.sqrt(2)    # Q^2 = 1

def facs(name, x, kap, M2, Y=None):
    """factors (a + b km - i eta w)^(-e) at base (x=k^+, kap=kT^2)."""
    G = Factor(M2 + kap + 0*x, [-2*x], 1.03)
    g0 = Factor(kap + 0*x, [-2*x], 0.97)
    t1 = Factor(kap + 0*x, [2*P - 2*x], 1.11)
    t2 = Factor(2*Pp*x + kap, [-2*x], 0.89)
    h1 = Factor(0*x, [2*P + 0*x], 1.21)
    h2 = Factor(2*Pp*x, [0*x], 0.79)
    if Y is not None:
        e = np.exp(-2*Y)
        h1Y = Factor(-2*P*e*x, [2*P + 0*x], 1.21)
        h2Y = Factor(2*Pp*x, [-2*Pp*e + 0*x], 0.79)
    else:
        h1Y, h2Y = h1, h2
    num_g0 = Factor(kap + 0*x, [-2*x], 0.0, e=-1)
    T = {
     'Gamma': [(1, [G, t1, t2])],
     'C_S':   [(1, [G, h1Y, h2Y])],
     'C_C1':  [(1, [G, t1, h2]), (-1, [G, h1Y, h2])] if Y is not None else [(1, [G, t1, h2]), (-1, [G, h1, h2])],
     'C_C2':  [(1, [G, h1, t2]), (-1, [G, h1, h2Y])] if Y is not None else [(1, [G, h1, t2]), (-1, [G, h1, h2])],
    }
    if Y is None:
        T['C_H'] = [(1, [num_g0, t1, h1, t2, h2])]          # (1/g0) d1 d2 with d_i = -g0/(t_i h_i)  -> g0/(t1h1t2h2)
        T['r'] = [(-M2, [num_g0, G, t1, h1, t2, h2])]
    else:
        # C_H = T_H (Gamma - C_S - C_C1 - C_C2) computed term by term: T_H: G -> g0 (h's unchanged)
        gq = lambda lst: [g0 if f is G else f for f in lst]
        T['C_H'] = [(c, gq(l)) for (c, l) in T['Gamma'] + [(-c, l) for c, l in T['C_S'] + T['C_C1'] + T['C_C2']]]
        T['r'] = (T['Gamma'] + [(-c, l) for c, l in T['C_S'] + T['C_C1'] + T['C_C2'] + T['C_H']])
    return T[name]

def rho(name, x, kap, M2, Y=None):
    tot = 0.0
    for c, lst in facs(name, x, kap, M2, Y):
        fl = [Factor(f.a + 0*x, f.b, f.w, f.e) for f in lst]
        tot = tot + c*iterated_residue(fl, 1)
    return np.atleast_1d(np.real(tot/(1j*np.pi)))*np.ones_like(x)

def exact(M2):   # Jantzen 6.30 (Q^2=1)
    return 0.5*np.log(1/M2)**2 + np.log(1/M2)*np.log(1 - M2) - float(mp.polylog(2, M2)) + np.pi**2/3

def int2(f, xr=(-40, 8), kr=(-40, 8), absval=False):
    """int dx dkap f over x>0 (log vars) ; x<0 contributions checked separately"""
    g = lambda lk, lx: (abs(f(np.exp(lx), np.exp(lk))) if absval else f(np.exp(lx), np.exp(lk)))*np.exp(lx)*np.exp(lk)
    return integrate.dblquad(g, xr[0], xr[1], lambda t: kr[0], lambda t: kr[1], epsrel=1e-8)[0]

if __name__ == "__main__":
    # sanity: densities vanish for x<0 ?
    xs = -np.logspace(-6, 1, 50); ks = np.logspace(-6, 1, 50)
    for nm in ['Gamma', 'r']:
        v = np.array([rho(nm, np.array([a]), np.array([b]), 1e-2) for a in xs for b in ks])
        print(f"max |rho_{nm}| at x<0: {np.max(np.abs(v)):.2e}")
    for M2 in [1e-2, 1e-3, 1e-4]:
        fG = lambda x, k: rho('Gamma', np.array([x]), np.array([k]), M2)[0]
        IG = int2(fG)
        print(f"M2={M2:.0e}: int rho_Gamma = {IG:.10f}  exact (Jantzen) = {exact(M2):.10f}")
    # rapidity divergence of C_S: int over |y|<Y_c, with y = 0.5 ln(k^+/k^-_os) ; show growth ~ linear in Y_c
    M2 = 1e-2
    fS = lambda x, k: rho('C_S', np.array([x]), np.array([k]), M2)[0]
    for Xc in [4, 8, 12, 16]:
        v = integrate.dblquad(lambda lk, lx: fS(np.exp(lx), np.exp(lk))*np.exp(lx)*np.exp(lk), -Xc, Xc, lambda t: -30, lambda t: 6, epsrel=1e-7)[0]
        print(f"   C_S: int over |ln k^+| < {Xc}: {v:.6f}  (per unit ln k^+: {v/(2*Xc):.6f}; expected density 1/(4PP') * int dkap/(kap+M2) diverges -> cut)")
    print("light-like remainder r = -M^2 g0/(G t1 h1 t2 h2):")
    for M2 in [1e-2, 1e-3, 1e-4, 1e-5, 1e-6]:
        fr = lambda x, k: rho('r', np.array([x]), np.array([k]), M2)[0]
        Ir = int2(fr); Nr = int2(fr, absval=True)
        L = np.log(1/M2)
        print(f"   lam^2=M2={M2:.0e}: int r = {Ir:+.6e} ({Ir/M2:+.4f} lam^2, {Ir/(M2*L):+.4f} lam^2 L, {Ir/(M2*L*L):+.4f} lam^2 L^2);"
              f"  norm = {Nr:.6e} ({Nr/(M2*L*L):.4f} lam^2 L^2)")
