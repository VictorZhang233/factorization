# Independent real-contour check of the half-coincident weight W12 (cf. halfcoinc.py, rotated contour).
# A: one spectator, two insertions (colour orders); B: two spectators (commuting insertions),
#   J_B = i^3/((p1+p2-beta+i0)(al1-p1+i0)(al2-p2+i0)),  p = -k^+.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
import twoexch_exact as T
mp.mp.dps = 40
I = mp.mpc(0, 1)
def E(pT, m, pp): return (pT[0]**2 + pT[1]**2 + m**2)/(2*pp)

def B2_terms(y, pb2):
    beta, al1, al2 = pb2
    e = T.TINY; ie = I*e; i3 = I**3
    f1 = (-1, (y + beta - ie))          # p1+p2-beta+i0 = -x-y-beta+i0
    f3 = (1, -(al2 + ie))               # al2 - p2 + i0 = al2 + x + i0
    # al1 - p1 + i0 = al1 + y + i0 = (y - y0 + i0), y0 = -al1  (outer pole)
    return [(i3, [(-al1, +1)], 0, [f1, f3])]

def parts(y, pa, pb2, a1, a2, cA):
    FA = T.A_terms(y, pa, a1, a2, cA); JB = B2_terms(y, pb2)
    out = []
    for sx in (+1, -1):
        for (C1, p1, m1, f1) in FA[sx]:
            for (C2, p2, m2, f2) in JB:
                out.append((T.int_halfline(C1*C2, m1 + m2, f1 + f2, sx), p1 + p2))
    return out

def outer(pa, pb2, a1, a2, cA, sgn, ymin=mp.mpf('1e-14'), ymax=mp.mpf('1e8')):
    beta, al1, al2 = pb2
    sp = sorted(set([abs(c) for c in [-al1, -beta, al2 - beta, -al1 - al2, a1/(2*pa['al1']), a1/(2*pa['al2']), a1/(2*pa['al0']), -a1/(2*pa['d10']), -a1/(2*pa['d20']), a1/(2*(pa['al0'] - pa['al1']))] if c*sgn > 0]))
    def f(t):
        y = sgn*mp.e**t; tot = mp.mpc(0)
        for (v, pl) in parts(y, pa, pb2, a1, a2, cA):
            for (y0, s) in pl: v = v/(y - y0 + s*I*T.TINY)
            tot += v
        return tot*mp.e**t
    fine = sorted(set(list(mp.linspace(mp.log(ymin), mp.log(ymax), 50)) + [mp.log(p) for p in sp if ymin < p < ymax]))
    rpoles = []
    if (-al1)*sgn > 0: rpoles.append((mp.mpf(-al1), +1))
    if cA == '21' and sgn > 0 and pa['al2'] > 0: rpoles.append((a1/(2*pa['al2']), +1))
    if not rpoles: return mp.quad(f, fine)/(2*mp.pi)**2
    val = mp.mpc(0)
    windows = sorted([(abs(y0)*mp.mpf('0.8'), abs(y0)*mp.mpf('1.2'), y0, s) for (y0, s) in rpoles], key=lambda z: z[0])
    edges = [mp.log(ymin)]
    for (a, b, y0, s) in windows: edges += [mp.log(a), mp.log(b)]
    edges.append(mp.log(ymax))
    for kk in range(0, len(edges), 2):
        a, b = edges[kk], edges[kk+1]
        val += mp.quad(f, sorted(set([a, b] + [t for t in fine if a < t < b])))
    for (a, b, y0, s) in windows:
        def G(yy):
            tot = mp.mpc(0); yv = sgn*yy
            for (v, pl) in parts(yv, pa, pb2, a1, a2, cA):
                for (yp, sp_) in pl:
                    if abs(yp - y0) > mp.mpf('1e-30'): v = v/(yv - yp + sp_*I*T.TINY)
                tot += v
            return tot
        Y0 = abs(y0); G0 = G(Y0)
        reg = mp.quad(lambda yy: (G(yy) - G0)/(sgn*yy - y0), sorted(set([a, Y0, b] + [p for p in sp if a < p < b])))
        pv = mp.log((b - Y0)/(Y0 - a))
        val += (reg + G0*(pv - s*I*mp.pi)) if sgn > 0 else (reg - G0*(pv + s*I*mp.pi))
    return val/(2*mp.pi)**2

for lam in (mp.mpf('0.03'), mp.mpf('0.01'), mp.mpf('0.003')):
    sc = lambda v: (lam*mp.mpf(v[0]), lam*mp.mpf(v[1]))
    k1T = sc(('0.8', '0.1')); k2T = sc(('-0.3', '0.9'))
    pa = T.jet_params(mp.mpf('0.9')*lam, mp.mpf('0.5')*lam, mp.mpf('0.7')*lam, mp.mpf('0.4'), sc(('0.3', '0.2')), k1T, k2T)
    MB, mb, m1, m2 = mp.mpf('1.1')*lam, mp.mpf('0.5')*lam, mp.mpf('0.4')*lam, mp.mpf('0.6')*lam
    x1, x2 = mp.mpf('0.3'), mp.mpf('0.35'); xb = 1 - x1 - x2
    s1T, s2T = sc(('-0.2', '0.3')), sc(('0.25', '-0.15'))
    s1b = (s1T[0] + k1T[0], s1T[1] + k1T[1]); s2b = (s2T[0] + k2T[0], s2T[1] + k2T[1])
    bT = (-(s1b[0] + s2b[0]), -(s1b[1] + s2b[1]))
    al1 = E(s1T, m1, x1) - E(s1b, m1, x1); al2 = E(s2T, m2, x2) - E(s2b, m2, x2)
    beta = E(bT, mb, xb) + E(s1T, m1, x1) + E(s2T, m2, x2) - MB**2/2
    d0B = al1 + al2 - beta
    a1 = k1T[0]**2 + k1T[1]**2; a2 = k2T[0]**2 + k2T[1]**2
    Ival = {c: outer(pa, (beta, al1, al2), a1, a2, c, +1) + outer(pa, (beta, al1, al2), a1, a2, c, -1) for c in ('12', '21')}
    N = Ival['12'] + Ival['21']; N0 = (I/pa['d0'])*(I/d0B)/(a1*a2)
    print(f"lam={mp.nstr(lam,3)} REAL contour: N/N0={mp.nstr(N/N0,10)}  W12={mp.nstr(Ival['12']/N,10)}  W21={mp.nstr(Ival['21']/N,10)}", flush=True)
