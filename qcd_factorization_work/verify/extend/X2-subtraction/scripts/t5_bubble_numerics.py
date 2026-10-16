"""X2/T5: bubble-chain (log-insertion) class.  Gluon propagator 1/D_g -> ln^j(D_g)/D_g (renormalized bubble chain at
mu = Qt, eps=0).  T_R do not act on the gluon, so in 4D  C_R Gamma^(j) = ln^j(D_g) C_R Gamma.  Fibered densities via the
"four-shell" representation (REPORT (B.20)): line 1 put on its exact/soft/massless/eikonal shell D,e,t,h:
  rho_r^(j) = lD^j (v/DG - 1/u)/(u m2 v+kap) + le^j m2/(u(m2+u)(u m2+kap)) + lt^j /(u(uv+kap))
              + lh^j [1/((m2+u)(m2+u+kap)) - 1/(u(u+kap))]      (0<u<1),
  lD = ln((u m2 v + kap)/v), le = ln(u m2 + kap), lt = ln(kap/v), lh = ln(kap);  u>1 and the sliver similarly.
Check j=0 against the closed form, then the norms for j=0,1,2."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np, warnings
from scipy import integrate
warnings.filterwarnings('ignore')

def rho_r(u, k, m2, j):
    if u <= 0 or u >= 1: raise ValueError
    v = 1 - u
    DG = (m2 + u)*(v*(1 + m2) + k) + k*v
    lD = np.log((u*m2*v + k)/v); le = np.log(u*m2 + k); lt = np.log(k/v); lh = np.log(k)
    return (lD**j*(v/DG - 1/u)/(u*m2*v + k) + le**j*m2/(u*(m2 + u)*(u*m2 + k)) + lt**j/(u*(u*v + k))
            + lh**j*(1/((m2 + u)*(m2 + u + k)) - 1/(u*(u + k))))

def rho_r_closed(u, k, m2):
    v = 1 - u
    DG = (m2 + u)*(v*(1 + m2) + k) + k*v
    rG = v/((u*m2*v + k)*DG); rS = 1/((u*m2 + k)*(m2 + u)); rC1 = u*m2/((u*m2*v + k)*(u*m2 + k))
    rC2 = -1/((m2 + u + k)*(m2 + u)); rH = -u/((u + k)*(u*v + k))
    return rG - rS - rC1 - rC2 - rH

def rho_r_big(u, k, m2, j):
    # u>1: only e-shell and h-shell terms survive: -S - C1(e part) - C2 - H(h part)
    le = np.log(u*m2 + k); lh = np.log(k)
    return le**j*m2/(u*(m2 + u)*(u*m2 + k)) + lh**j*(1/((m2 + u)*(m2 + u + k)) - 1/(u*(u + k)))

def rho_r_sliver(w, k, m2, j):
    """sliver -m2<u<0, w = u + m2 in (0,m2) (normalised: x = u/sqrt2, a = sqrt2 m2 -> 2x+a = sqrt2 w).
    Close lower on the D2 pole: km = (m2 + u + k)/(sqrt2 w) (normalised P=P'=1/sqrt2).  r = (2/(w' Dg))(1/D1 - 1/h1),
    log insertion: ln^j(Dg) multiplies both (same residue point)."""
    P = 1/np.sqrt(2); Pp = P
    x = (w - m2)/np.sqrt(2)
    a2 = m2/Pp
    ww = 2*x + a2
    km = (m2 + 2*Pp*x + k)/ww
    Dg = -2*x*km + k
    D1 = m2 + 2*P*km - (m2/P)*x - (2*x*km - k)
    h1 = 2*P*km
    val = (2/(ww*Dg))*(1/D1 - 1/h1)*np.log(Dg)**j
    return val/np.sqrt(2)    # density w.r.t. du dk (dx = du/sqrt2)

def norm_and_int(m2, j):
    tot = 0; nrm = 0
    lo = np.log(1e-30); hi = np.log(1e14)
    for (ua, ub, f) in [(1e-30, 0.5, rho_r), (0.5, 1 - 1e-15, rho_r), (1 + 1e-15, 1e12, rho_r_big)]:
        g = lambda lk, lu: f(np.exp(lu), np.exp(lk), m2, j)*np.exp(lu)*np.exp(lk)
        ga = lambda lk, lu: abs(g(lk, lu))
        if ua >= 0.5 and ub < 1:
            g = lambda lk, lv: rho_r(1 - np.exp(lv), np.exp(lk), m2, j)*np.exp(lv)*np.exp(lk)
            ga = lambda lk, lv: abs(g(lk, lv))
            a, b = np.log(1e-15), np.log(0.5)
        else:
            a, b = np.log(ua), np.log(ub)
        tot += integrate.dblquad(g, a, b, lambda t: lo, lambda t: hi, epsrel=1e-8)[0]
        nrm += integrate.dblquad(ga, a, b, lambda t: lo, lambda t: hi, epsrel=1e-8)[0]
    gs = lambda lk, w: rho_r_sliver(w, np.exp(lk), m2, j)*np.exp(lk)
    tot += integrate.dblquad(gs, 0, m2, lambda w: lo, lambda w: hi, epsrel=1e-8)[0]
    nrm += integrate.dblquad(lambda lk, w: abs(gs(lk, w)), 0, m2, lambda w: lo, lambda w: hi, epsrel=1e-8)[0]
    return tot, nrm

# consistency of four-shell form with closed form
rng = np.random.default_rng(3)
mx = 0
for _ in range(2000):
    u = rng.uniform(0.001, 0.999); k = 10**rng.uniform(-8, 2); m2 = 10**rng.uniform(-6, -1)
    a = rho_r(u, k, m2, 0); b = rho_r_closed(u, k, m2)
    mx = max(mx, abs(a - b)/(abs(a) + abs(b) + 1e-300))
print("four-shell (j=0) vs closed form: max rel diff over 2000 random points:", mx)
for j in [0, 1, 2]:
    print(f"j = {j}:")
    for kk in [4, 6, 8, 10]:
        m2 = 10.0**(-kk); L = np.log(1/m2)
        tot, nrm = norm_and_int(m2, j)
        print(f"   lam2=1e-{kk}: int r^(j) = {tot:+.6e} = {tot/m2:+.4f} lam2 = {tot/(m2*L**j):+.4f} lam2 L^{j};"
              f"   norm = {nrm:.6e} = {nrm/(m2*L**(j+1)):.4f} lam2 L^{j+1}")
