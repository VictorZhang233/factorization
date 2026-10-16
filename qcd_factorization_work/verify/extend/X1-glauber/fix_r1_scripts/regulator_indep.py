# X1 fix round 1 -- independent implementation (closed-form multi-pole weights, own quadrature) of
#  (A) the half-coincident weight W12 with an analytic k^- regulator on the A side      [T3 restatement]
#  (B) the fully coincident p_opp with analytic regulators on k^+ (B side) and k^- (A side)  [T2/T2'/P2]
# at leading power in lambda_A (jet A localized: only its ordering weights enter).
#
# Multi-pole localization (Lemma L1' of the revised report): an external factor R_e(k) chi(k) with
# chi(k) = K^2/(k^2+K^2) has poles z_e = a_e/(2 k_e^+) (final if k_e^+ > 0, initial if k_e^+ < 0), +iK (initial)
# and -iK (final).  Normalized pole weights (sum = 1):
#     u_z = K^2/(z^2+K^2),   u_+ = z/(2(z - iK)),   u_- = z/(2(z + iK)),
# and the localized A-side weight of colour order (12) is  W_(12) = sum_{p1,p2} u_{1,p1} u_{2,p2} w_(12)(p1,p2)
# with the race weights w_(12) = p1/(p1+p2) (both final), p2/(p1+p2) (both initial), 1 (1 initial, 2 final),
# 0 (1 final, 2 initial).  K = infinity gives the race weights of L1/L2.
# Integrals over k^+ = u in R^2 are done on the rotated contour u = e^{i theta} x (valid under NF_B, L5),
# per quadrant; diagonal quadrants on a product log grid, off-diagonal quadrants in strip-adapted variables
# (U = x1 + x2, v), which resolves the strip |u1 + u2| <~ lambda_B of the fully coincident B functions.
# Units: lambda = 1 (transverse momenta in units of lambda, light-cone energies in units of lambda^2).
import sys, os, itertools, time
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np

def E(pT, m, pp):
    return (pT[0]**2 + pT[1]**2 + m**2)/(2*pp)

def gl(n, a, b):
    x, w = np.polynomial.legendre.leggauss(n)
    return 0.5*(b - a)*x + 0.5*(b + a), 0.5*(b - a)*w

# ----------------------------------------------------------------------------- weights
def pole_options(u, a, K, q):
    """list of (pole value p, type 'F'/'B', weight) for one insertion; u complex k^+, q = sign of real k^+"""
    z = a/(2*u)
    tz = 'F' if q > 0 else 'B'
    if K is None:
        return [(z, tz, np.ones_like(z))]
    return [(z, tz, K**2/(z**2 + K**2)), (1j*K*np.ones_like(z), 'B', z/(2*(z - 1j*K))),
            (-1j*K*np.ones_like(z), 'F', z/(2*(z + 1j*K)))]

def race12(p1, t1, p2, t2):
    if t1 == 'F' and t2 == 'F': return p1/(p1 + p2)
    if t1 == 'B' and t2 == 'B': return p2/(p1 + p2)
    if t1 == 'B' and t2 == 'F': return np.ones_like(p1)
    return np.zeros_like(p1)

def W12(u1, u2, a1, a2, K, q):
    tot = 0
    for (p1, t1, w1) in pole_options(u1, a1, K, q[0]):
        for (p2, t2, w2) in pole_options(u2, a2, K, q[1]):
            tot = tot + w1*w2*race12(p1, t1, p2, t2)
    return tot

def lorentz(u, Kp):
    return 1.0 if Kp is None else Kp**2/(u**2 + Kp**2)

# ----------------------------------------------------------------------------- quadrature on rotated contour
def integrate(fun, theta, n_diag=900, n_v=700, n_U=900, tlo=-38.0, thi=26.0):
    """int d^2u/(2pi)^2 fun(u1, u2, q) over R^2 rotated by theta, quadrant by quadrant"""
    ph = np.exp(1j*theta)
    tot = 0
    t, wt = gl(n_diag, tlo, thi)
    T1, T2 = np.meshgrid(t, t, indexing='ij'); W = np.outer(wt, wt)
    for q in ((1, 1), (-1, -1)):
        x1 = q[0]*np.exp(T1); x2 = q[1]*np.exp(T2)
        tot += np.sum(W*np.exp(T1 + T2)*fun(ph*x1, ph*x2, q))
    tv, wv = gl(n_v, tlo, thi)
    sg, wsg = gl(n_U, 0.0, thi - tlo + 8.0)           # U = v e^{-sigma}, 0 < U < v
    tU, wU = gl(n_U, tlo - 8.0, thi)                   # U = -e^{tau} < 0
    for q in ((-1, 1), (1, -1)):
        # v = |x of the positive variable|, U = x1 + x2;  quadrant (-,+): x2 = v, x1 = U - v;  (+,-): x1 = v, x2 = U - v
        TV, SG = np.meshgrid(tv, sg, indexing='ij'); v = np.exp(TV); U = v*np.exp(-SG)
        Wp = np.outer(wv, wsg)*v*U                     # dv dU = (v dt_v)(U d sigma)
        TV2, TAU = np.meshgrid(tv, tU, indexing='ij'); v2 = np.exp(TV2); U2 = -np.exp(TAU)
        Wm = np.outer(wv, wU)*v2*np.exp(TAU)
        for (vv, UU, WW) in ((v, U, Wp), (v2, U2, Wm)):
            if q == (-1, 1):
                x2 = vv; x1 = UU - vv
            else:
                x1 = vv; x2 = UU - vv
            tot += np.sum(WW*fun(ph*x1, ph*x2, q))
    return tot*ph**2/(2*np.pi)**2

# ----------------------------------------------------------------------------- (A) half-coincident
def halfcoinc_model(variant):
    if variant == 'author':          # parameters of scripts/halfcoinc.py (lambda = 1)
        k1T, k2T = (0.8, 0.1), (-0.3, 0.9)
        MB, mb, m1, m2 = 1.1, 0.5, 0.4, 0.6; x1, x2 = 0.3, 0.35
        s1T, s2T = (-0.2, 0.3), (0.25, -0.15)
    else:                            # 'Basym' of scripts/halfcoinc_sym.py
        k1T, k2T = (0.8, 0.1), (0.1, 0.8)
        MB, mb, m1, m2 = 1.1, 0.5, 0.4, 0.4; x1, x2 = 0.3, 0.3
        s1T, s2T = (-0.2, 0.3), (0.5, -0.4)
    xb = 1 - x1 - x2
    s1b = (s1T[0] + k1T[0], s1T[1] + k1T[1]); s2b = (s2T[0] + k2T[0], s2T[1] + k2T[1])
    bT = (-(s1b[0] + s2b[0]), -(s1b[1] + s2b[1]))
    al1 = E(s1T, m1, x1) - E(s1b, m1, x1); al2 = E(s2T, m2, x2) - E(s2b, m2, x2)
    beta = E(bT, mb, xb) + E(s1T, m1, x1) + E(s2T, m2, x2) - MB**2/2
    a1 = k1T[0]**2 + k1T[1]**2; a2 = k2T[0]**2 + k2T[1]**2
    return dict(al1=al1, al2=al2, beta=beta, d0=al1 + al2 - beta, a1=a1, a2=a2)

def JB_half(p1, p2, m):
    return (1j)**3/((p1 + p2 - m['beta'])*(m['al1'] - p1)*(m['al2'] - p2))

def run_A(out):
    for variant in ('author', 'Basym'):
        m = halfcoinc_model(variant)
        lamB = abs(m['d0']); a = np.sqrt(m['a1']*m['a2'])
        out(f"(A) half-coincident [{variant}]: alpha1={m['al1']:.4f} alpha2={m['al2']:.4f} beta={m['beta']:.4f} "
            f"d0={m['d0']:.4f} (NF_B: alphas<0)  a1={m['a1']:.3f} a2={m['a2']:.3f}")
        for th in (np.pi/8, np.pi/4, 3*np.pi/8):
            nrm = integrate(lambda u1, u2, q: JB_half(-u1, -u2, m), th)/(1j/m['d0'])
            out(f"    theta/pi={th/np.pi:.3f}: int J_B / Jcal_B = {nrm:.10f}")
        for Kr in (None, 1e4, 1e2, 10.0, 1.0, 0.1, 0.01, 0.001):
            K = None if Kr is None else Kr*a/lamB
            vals = []
            for th in ((np.pi/8, np.pi/4) if Kr in (None, 1.0, 0.01) else (np.pi/4,)):
                num = integrate(lambda u1, u2, q: W12(u1, u2, m['a1'], m['a2'], K, q)*JB_half(-u1, -u2, m), th)
                den = integrate(lambda u1, u2, q: JB_half(-u1, -u2, m), th)
                vals.append((th, num/den))
            lab = "no k^- regulator (race weights)" if Kr is None else f"K^- = {Kr:g} a/lambda_B"
            out(f"    {lab:34s}: " + ";  ".join(f"theta/pi={th/np.pi:.3f}: W12 = {v:.8f}" for th, v in vals))

# ----------------------------------------------------------------------------- (B) fully coincident
def jet_params(M, ma, ms, xs, sT, k1T, k2T):
    P = M**2/2
    sub = lambda u, v: (u[0] - v[0], u[1] - v[1])
    s0T = sub(sub(sT, k1T), k2T); s1T = sub(sT, k2T); s2T = sub(sT, k1T)
    aT = (-s0T[0], -s0T[1])
    Ea = E(aT, ma, 1 - xs); Es = E(sT, ms, xs)
    Es0 = E(s0T, ms, xs); Es1 = E(s1T, ms, xs); Es2 = E(s2T, ms, xs)
    return dict(d0=P - Ea - Es0, beta=Ea + Es - P, al0=Es - Es0, al1=Es - Es1, al2=Es - Es2)

def JB_full(p1, p2, pb, col):
    den3 = (pb['al1'] - p2) if col == '12' else (pb['al2'] - p1)
    return (1j)**3/((p1 + p2 - pb['beta'])*(pb['al0'] - p1 - p2)*den3)

def run_B(out):
    k1T, k2T = (0.8, 0.1), (-0.3, 0.9)
    pb = jet_params(0.8, 0.6, 0.5, 0.55, (-0.25, 0.4), (-0.8, -0.1), (0.3, -0.9))   # base set, jet B
    a1 = k1T[0]**2 + k1T[1]**2; a2 = k2T[0]**2 + k2T[1]**2; a = np.sqrt(a1*a2)
    lamB = abs(pb['d0']); Jcal = 1j/pb['d0']
    out(f"(B) fully coincident, jet B = base set: al0={pb['al0']:.4f} al1={pb['al1']:.4f} al2={pb['al2']:.4f} "
        f"beta={pb['beta']:.4f} d0={pb['d0']:.4f};  a1={a1:.3f} a2={a2:.3f}")
    def popp(Kp, Km, th=np.pi/4):
        I = {}
        for cA in ('12', '21'):
            for cB in ('12', '21'):
                def fun(u1, u2, q, cA=cA, cB=cB):
                    w = W12(u1, u2, a1, a2, Km, q)
                    if cA == '21': w = 1 - w
                    return w*lorentz(u1, Kp)*lorentz(u2, Kp)*JB_full(-u1, -u2, pb, cB)
                I[(cA, cB)] = integrate(fun, th)
        N = sum(I.values())
        return N/Jcal, (I[('12', '21')] + I[('21', '12')])/N
    for Kp_r in (1e2, 1e4):
        Kp = Kp_r*lamB
        for Km_r in (None, 1e3, 10.0, 1.0, 0.1, 1e-3):
            Km = None if Km_r is None else Km_r*(a/Kp)       # K^- in units of a/K^+:  Km_r = K^+ K^- / a
            t0 = time.time()
            res = [popp(Kp, Km, th) for th in ((np.pi/8, np.pi/4) if Km_r in (None, 1.0) else (np.pi/4,))]
            lab = "no k^- regulator" if Km_r is None else f"K^+ K^- / a = {Km_r:g}"
            out(f"    K^+ = {Kp_r:g} lambda_B, {lab:22s}: " +
                ";  ".join(f"N/Jcal={nn:.6f}  p_opp={pp:.6f}" for nn, pp in res) + f"   ({time.time()-t0:.0f}s)")

if __name__ == '__main__':
    def out(sline):
        print(sline, flush=True)
    which = sys.argv[1] if len(sys.argv) > 1 else 'AB'
    if 'A' in which: run_A(out)
    if 'B' in which: run_B(out)
