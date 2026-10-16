# Fast version of the rotated-contour cross-check (numpy, Gauss-Legendre in (log r, phi) per quadrant).
# Valid when no final-state energy of jet B is positive (rotation k^+ -> i kappa crosses no singularity).
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np

def E(pT, m, pplus):
    return (pT[0]**2 + pT[1]**2 + m**2) / (2*pplus)

def jet_params(M, ma, ms, xs, sT, k1T, k2T):
    P = M**2/2
    sub = lambda u, v: (u[0]-v[0], u[1]-v[1])
    s0T = sub(sub(sT, k1T), k2T); s1T = sub(sT, k2T); s2T = sub(sT, k1T)
    aT = (-s0T[0], -s0T[1])
    Ea = E(aT, ma, 1-xs); Es = E(sT, ms, xs)
    Es0 = E(s0T, ms, xs); Es1 = E(s1T, ms, xs); Es2 = E(s2T, ms, xs)
    return dict(d0=P-Ea-Es0, d10=P-Ea-Es1, d20=P-Ea-Es2, beta=Ea+Es-P, al0=Es-Es0, al1=Es-Es1, al2=Es-Es2)

def FA(k1, k2, pa, a1, a2, col, q):
    d0, d10, d20, beta, al0, al1, al2 = (pa[k] for k in ('d0','d10','d20','beta','al0','al1','al2'))
    i3 = (1j)**3
    z1 = a1/(2*k1); z2 = a2/(2*k2); r1 = 1/(2*k1); r2 = 1/(2*k2)
    if q == (1, 1):
        J = i3/(d0*(al0 - z1 - z2)*((al1 - z2) if col == '12' else (al2 - z1)))
        return -r1*r2*J
    if q == (-1, -1):
        J = i3/(d0*((d10 + z1) if col == '12' else (d20 + z2))*(z1 + z2 - beta))
        return -r1*r2*J
    if q == (-1, 1):
        return np.zeros_like(k1) if col == '21' else r1*r2*i3/(d0*(d10 + z1)*(al1 - z2))
    if q == (1, -1):
        return np.zeros_like(k1) if col == '12' else r1*r2*i3/(d0*(d20 + z2)*(al2 - z1))

def JB(p1, p2, pb, col):
    d0, beta, al0, al1, al2 = (pb[k] for k in ('d0','beta','al0','al1','al2'))
    den3 = (al1 - p2) if col == '12' else (al2 - p1)
    return (1j)**3/((p1 + p2 - beta)*(al0 - p1 - p2)*den3)

def Irot(pa, pb, a1, a2, cA, cB, theta=np.pi/2, nt=4000, nphi=1200, tmin=-45, tmax=25):
    ph = np.exp(1j*theta)
    xt, wt = np.polynomial.legendre.leggauss(nt)
    t = 0.5*(tmax - tmin)*xt + 0.5*(tmax + tmin); wt = wt*0.5*(tmax - tmin)
    xp, wp = np.polynomial.legendre.leggauss(nphi)
    phi = 0.25*np.pi*(xp + 1); wp = wp*0.25*np.pi
    T, PHI = np.meshgrid(t, phi, indexing='ij'); W = np.outer(wt, wp)
    r = np.exp(T)
    tot = 0
    for q in itertools.product((1, -1), repeat=2):
        x1 = q[0]*r*np.cos(PHI); x2 = q[1]*r*np.sin(PHI)
        k1, k2 = ph*x1, ph*x2
        f = FA(k1, k2, pa, a1, a2, cA, q)*JB(-k1, -k2, pb, cB)*r*r
        tot += np.sum(W*f)
    return tot*ph**2/(2*np.pi)**2

sets = {
  'base':  ((0.9,0.5,0.7,0.4,(0.3,0.2)),  (0.8,0.6,0.5,0.55,(-0.25,0.4))),
  'apole': ((0.9,0.5,0.7,0.4,(-0.3,1.0)), (0.8,0.6,0.5,0.55,(-0.25,0.4))),
  'alt':   ((0.9,0.5,0.7,0.4,(0.3,0.2)),  (0.8,0.6,0.5,0.55,(-0.9,1.1))),
  'altswap': ((0.8,0.6,0.5,0.55,(0.9,-1.1)), (0.9,0.5,0.7,0.4,(-0.3,-0.2))),
  'baseswap': ((0.8,0.6,0.5,0.55,(0.25,-0.4)), (0.9,0.5,0.7,0.4,(-0.3,-0.2))),
}
if __name__ == '__main__':
    lam = float(sys.argv[1]); name = sys.argv[2]; theta = float(sys.argv[3])*np.pi if len(sys.argv) > 3 else np.pi/2
    sc = lambda v: (lam*v[0], lam*v[1])
    k1T = sc((0.8, 0.1)); k2T = sc((-0.3, 0.9))
    k1Tm = (-k1T[0], -k1T[1]); k2Tm = (-k2T[0], -k2T[1])
    (MA, maA, msA, xA, sTA), (MB, maB, msB, xB, sTB) = sets[name]
    pa = jet_params(MA*lam, maA*lam, msA*lam, xA, sc(sTA), k1T, k2T)
    pb = jet_params(MB*lam, maB*lam, msB*lam, xB, sc(sTB), k1Tm, k2Tm)
    a1 = k1T[0]**2 + k1T[1]**2; a2 = k2T[0]**2 + k2T[1]**2
    res = {}
    for cA, cB in itertools.product(('12','21'), repeat=2):
        res[(cA, cB)] = Irot(pa, pb, a1, a2, cA, cB, theta=theta)
    N = sum(res.values()); N0 = (1j/pa['d0'])*(1j/pb['d0'])/(a1*a2)
    print(f"lam={lam} set={name} theta/pi={theta/np.pi:.3f} ROTATED: N/N0={N/N0:.10f}")
    for k, v in res.items(): print(f"   W{k} = {v/N:.10f}")
    print(f"   p_opp = {(res[('12','21')]+res[('21','12')])/N:.10f}", flush=True)
