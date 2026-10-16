# Third, fully independent evaluation of the k^+ integral (after exact k^- residues): brute-force
# 2D quadrature on the REAL k^+ contour with finite eta in every denominator (scipy), at lam = 1,
# followed by extrapolation eta -> 0.  Compares with twoexch_rotated_fast (rotated contour, eta = 0)
# and twoexch_exact (real contour, log-residue inner + PV outer).
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from scipy import integrate
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from twoexch_rotated_fast import jet_params, sets

def FA_eta(y, x, pa, a1, a2, col, eta):
    d0, d10, d20, beta, al0, al1, al2 = (pa[k] for k in ('d0','d10','d20','beta','al0','al1','al2'))
    ie = 1j*eta; i3 = (1j)**3
    z1 = (a1 - ie)/(2*y); z2 = (a2 - ie)/(2*x); r1 = 1/(2*y); r2 = 1/(2*x)
    if y > 0 and x > 0:
        J = i3/(d0*(al0 - z1 - z2 + ie)*((al1 - z2 + ie) if col == '12' else (al2 - z1 + ie)))
        return -r1*r2*J
    if y < 0 and x < 0:
        J = i3/(d0*((d10 + z1 + ie) if col == '12' else (d20 + z2 + ie))*(z1 + z2 - beta + ie))
        return -r1*r2*J
    if y < 0 and x > 0:
        return 0j if col == '21' else r1*r2*i3/(d0*(d10 + z1 + ie)*(al1 - z2 + ie))
    if y > 0 and x < 0:
        return 0j if col == '12' else r1*r2*i3/(d0*(d20 + z2 + ie)*(al2 - z1 + ie))

def JB_eta(p1, p2, pb, col, eta):
    d0, beta, al0, al1, al2 = (pb[k] for k in ('d0','beta','al0','al1','al2'))
    ie = 1j*eta
    den3 = (al1 - p2 + ie) if col == '12' else (al2 - p1 + ie)
    return (1j)**3/((p1 + p2 - beta + ie)*(al0 - p1 - p2 + ie)*den3)

def brute(pa, pb, a1, a2, cA, cB, eta, L=60.0):
    # map each half-line with x = s*tan(u)^2-like? use x = sgn * exp(t) in log variables, t in [-12, log L*...]
    def f(t2, t1, s1, s2, part):
        y = s1*np.exp(t1); x = s2*np.exp(t2)
        v = FA_eta(y, x, pa, a1, a2, cA, eta)*JB_eta(-y, -x, pb, cB, eta)*np.exp(t1 + t2)
        return v.real if part == 0 else v.imag
    tot = 0j
    for s1, s2 in itertools.product((1, -1), repeat=2):
        for part in (0, 1):
            val, err = integrate.dblquad(lambda t2, t1: f(t2, t1, s1, s2, part), -14, 9, -14, 9, epsabs=1e-10, epsrel=1e-7)
            tot += val if part == 0 else 1j*val
    return tot/(2*np.pi)**2

if __name__ == '__main__':
    name = sys.argv[1] if len(sys.argv) > 1 else 'base'
    lam = 1.0
    sc = lambda v: (lam*v[0], lam*v[1])
    k1T = sc((0.8, 0.1)); k2T = sc((-0.3, 0.9))
    k1Tm = (-k1T[0], -k1T[1]); k2Tm = (-k2T[0], -k2T[1])
    (MA, maA, msA, xA, sTA), (MB, maB, msB, xB, sTB) = sets[name]
    pa = jet_params(MA*lam, maA*lam, msA*lam, xA, sc(sTA), k1T, k2T)
    pb = jet_params(MB*lam, maB*lam, msB*lam, xB, sc(sTB), k1Tm, k2Tm)
    a1 = k1T[0]**2 + k1T[1]**2; a2 = k2T[0]**2 + k2T[1]**2
    for eta in [float(e) for e in sys.argv[2:]] or [0.2, 0.1, 0.05]:
        res = {}
        for cA, cB in itertools.product(('12','21'), repeat=2):
            res[(cA, cB)] = brute(pa, pb, a1, a2, cA, cB, eta)
        N = sum(res.values())
        print(f"set={name} lam=1 eta={eta}: N={N:.8f}  " + "  ".join(f"W{k}={v/N:.6f}" for k, v in res.items()), flush=True)
