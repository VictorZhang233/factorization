"""X2/T2b: fast evaluation (scipy, float64 + mpmath spot checks) of the triangle remainder density:
signed integral vs exact UD remainder, integral norm, and the (H1)/(H2) items on the 2x2 cover
  U_S={0<x<=s, y<=s}, U_C1={s<x<=X0, y<=s}, U_C2={0<x<=s, s<y<=Y0} U {sliver -a/2<x<0}, U_H = rest,
  y = kap/(2x), s = lambda^theta.   Units Qt^2 = 2PP' = 1."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from scipy import integrate
import mpmath as mp

def dens(P, Pp, m2):
    a2 = m2/Pp
    def rG_mid(x, k):
        u = x/P
        A = x*m2*(1-u) + P*k
        e2 = m2 + 2*Pp*x
        D2h = e2*(1 + m2/(2*P*Pp) + k/(2*P*Pp*(1-u))) + k
        return 1.0/(A*D2h)
    def rS(x, k):
        return 1.0/((x*m2 + P*k)*(m2 + 2*Pp*x))
    def rC1_mid(x, k):
        u = x/P
        A = x*m2*(1-u) + P*k; B = x*m2 + P*k
        return x*m2/(2*P*Pp*A*B)
    def rC1_big(x, k):
        return -1.0/(2*Pp*x*(x*m2 + P*k))
    def rC2_pos(x, k):
        e2 = m2 + 2*Pp*x
        return -1.0/(P*e2*(e2 + k))
    def rH_mid(x, k):
        h2 = 2*Pp*x
        return -x/(P*(h2 + k)*(h2*(P - x) + P*k))
    def rH_big(x, k):
        h2 = 2*Pp*x
        return 1.0/(P*(h2 + k)*h2)
    def rG_neg(x, k):
        w = 2*x + a2
        kmv = (m2 + 2*Pp*x + k)/w
        Dg = -2*x*kmv + k
        D1 = m2 + 2*P*kmv - (m2/P)*x - (2*x*kmv - k)
        return 2.0/(w*Dg*D1)
    def rC2_neg(x, k):
        w = 2*x + a2
        kmv = (m2 + 2*Pp*x + k)/w
        Dg = -2*x*kmv + k
        h1 = 2*P*kmv
        return 2.0/(w*Dg*h1)
    def terms(x, k):
        """returns dict of densities at (x,k)"""
        if x <= -a2/2: return dict(G=0,S=0,C1=0,C2=0,H=0)
        if x < 0: return dict(G=rG_neg(x,k), S=0.0, C1=0.0, C2=rC2_neg(x,k), H=0.0)
        if x < P: return dict(G=rG_mid(x,k), S=rS(x,k), C1=rC1_mid(x,k), C2=rC2_pos(x,k), H=rH_mid(x,k))
        return dict(G=0.0, S=rS(x,k), C1=rC1_big(x,k), C2=rC2_pos(x,k), H=rH_big(x,k))
    return terms

def remainder_mid_stable(P, Pp, m2):
    """remainder density for 0<x<P in a cancellation-free grouped form (see REPORT eq. (B.12))"""
    def r(x, k):
        u = x/P
        A = x*m2*(1-u) + P*k; B = x*m2 + P*k
        e2 = m2 + 2*Pp*x; h2 = 2*Pp*x
        Qt2 = 2*P*Pp
        D2h = e2*(1 + m2/Qt2 + k/(Qt2*(1-u))) + k
        # Gamma - S - C1 = (1/A)(1/D2h - 1/h2) - (1/B)(1/e2 - 1/h2)
        t1 = (1/A)*(h2 - D2h)/(D2h*h2) + (1/B)*m2/(e2*h2)
        # -C2 - H
        t2 = 1.0/(P*e2*(e2 + k)) + x/(P*(h2 + k)*(h2*(P - x) + P*k))
        return t1 + t2
    return r

def UD(t):
    t = mp.mpf(t)
    lam = mp.sqrt(1 - 4*t); rho = 2/(1 - 2*t + lam)
    return (4*mp.polylog(2, -rho*t) + mp.log(rho*t)**2 + mp.pi**2/3)/lam

def int_xy(f, xlo, xhi, ylo, yhi, n=200):
    """int dx dkap f(x,kap) over xlo<x<xhi, ylo<y<yhi with kap=2xy, in log variables (x>0)"""
    def g(ly, lx):
        x = np.exp(lx); y = np.exp(ly)
        k = 2*x*y
        return f(x, k) * 2*x * x * y   # dkap = 2x dy ; dx dy = x y dlx dly
    val, err = integrate.dblquad(g, np.log(xlo), np.log(xhi), lambda lx: np.log(ylo), lambda lx: np.log(yhi),
                                 epsabs=0, epsrel=1e-9)
    return val, err

def run(P, Pp, lam2, theta=1.0, X0=None, Y0=None):
    m2 = lam2*(2*P*Pp)
    terms = dens(P, Pp, m2)
    rmid = remainder_mid_stable(P, Pp, m2)
    s = lam2**(theta/2)
    X0 = X0 or 2*P; Y0 = Y0 or 2*Pp
    BIG = 1e12; TINY = 1e-30
    def rem(x, k):
        if 0 < x < P: return rmid(x, k)
        t = terms(x, k); return t['G'] - t['S'] - t['C1'] - t['C2'] - t['H']
    out = {}
    # signed integral over x>0 and the sliver
    tot = 0.0; nrm = 0.0
    xr = [(TINY, s), (s, P), (P, X0), (X0, BIG)]
    yr = [(TINY, s), (s, Y0), (Y0, BIG)]
    pieces = {}
    for (xa, xb) in xr:
        for (ya, yb) in yr:
            v, _ = int_xy(rem, xa, xb, ya, yb)
            a_, _ = int_xy(lambda x, k: abs(rem(x, k)), xa, xb, ya, yb)
            pieces[(xa, xb, ya, yb)] = (v, a_)
            tot += v; nrm += a_
    # sliver -a/2 < x < 0 : variables w=2x+a in (0,a), kap in (0,inf)
    a2 = m2/Pp
    def gs(lk, w):
        x = (w - a2)/2; k = np.exp(lk)
        t = terms(x, k); return (t['G'] - t['C2'])*k*0.5
    def gsa(lk, w):
        x = (w - a2)/2; k = np.exp(lk)
        t = terms(x, k); return abs(t['G'] - t['C2'])*k*0.5
    def gG(lk, w):
        x = (w - a2)/2; k = np.exp(lk)
        t = terms(x, k); return t['G']*k*0.5
    sl, _ = integrate.dblquad(gs, 0, a2, lambda w: np.log(1e-30), lambda w: np.log(1e12), epsrel=1e-9)
    sla, _ = integrate.dblquad(gsa, 0, a2, lambda w: np.log(1e-30), lambda w: np.log(1e12), epsrel=1e-9)
    slG, _ = integrate.dblquad(gG, 0, a2, lambda w: np.log(1e-30), lambda w: np.log(1e12), epsrel=1e-9)
    tot += sl; nrm += sla
    Qt2 = 2*P*Pp
    Q2 = (Qt2 + m2)**2/Qt2
    exact = float(UD(m2/Q2)/Q2 - (mp.log(Qt2/m2)**2 + mp.pi**2/3)/Qt2)
    return tot, nrm, exact, sl, sla, slG, pieces

if __name__ == "__main__":
    for (P, Pp) in [(1/np.sqrt(2), 1/np.sqrt(2)), (0.8, 1.3/(2*0.8*1.3)**0 )]:
        pass
    P, Pp = 1/np.sqrt(2), 1/np.sqrt(2)
    print("P=P'=1/sqrt2 (Qt=1). Columns: lam2, int r (num), exact, rel.diff, norm, norm/lam2, norm/(lam2*L), sliver: int r, int|r|, int rho_G")
    for k in [2, 3, 4, 5, 6, 7, 8]:
        lam2 = 10.0**(-k)
        tot, nrm, ex, sl, sla, slG, pcs = run(P, Pp, lam2)
        L = np.log(1/lam2)
        print(f"  1e-{k}: {tot:.10e} {ex:.10e} {abs(tot-ex)/abs(ex):.1e}  norm={nrm:.6e}  n/l2={nrm/lam2:.5f}  n/(l2 L)={nrm/(lam2*L):.5f}  sliver: {sl:.3e} {sla:.3e} {slG:.4f}")
