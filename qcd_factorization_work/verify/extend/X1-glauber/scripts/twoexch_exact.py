# Robust eta->0 evaluation of the joint ordering weights W(piA,piB) for two SS Glauber exchanges
# between one spectator of jet A and one spectator of jet B (scalar model, Lemma-E.19-approximated jets,
# EXACT connecting propagators).  Same model as twoexch_model.py, but:
#   * inner k2^+ integral: exact log-residue formula, eta -> 0 implemented by a tiny imaginary part
#     (dps 50) -- exact in the limit;
#   * outer k1^+ integral: breakpoints at every special point; real-axis simple poles of the
#     y-dependent prefactors are treated by PV + (-/+ i pi) residue subtraction.
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 50
I = mp.mpc(0, 1)
TINY = mp.mpf('1e-35')

def E(pT, m, pplus):
    return (pT[0]**2 + pT[1]**2 + m**2) / (2*pplus)

def jet_params(M, ma, ms, xs, sT, k1T, k2T):
    P = mp.mpf(M)**2/2
    sub = lambda u, v: (u[0]-v[0], u[1]-v[1])
    s0T = sub(sub(sT, k1T), k2T); s1T = sub(sT, k2T); s2T = sub(sT, k1T)
    aT = (-s0T[0], -s0T[1])
    Ea = E(aT, ma, 1-xs); Es = E(sT, ms, xs)
    Es0 = E(s0T, ms, xs); Es1 = E(s1T, ms, xs); Es2 = E(s2T, ms, xs)
    return dict(d0=P-Ea-Es0, d10=P-Ea-Es1, d20=P-Ea-Es2, beta=Ea+Es-P,
                al0=Es-Es0, al1=Es-Es1, al2=Es-Es2)

def int_halfline(C, m, facs, sign):
    if sign < 0:
        facs = [(-g, h) for (g, h) in facs]; C = C*((-1)**m)
    tot = mp.mpc(0)
    for j, (gj, hj) in enumerate(facs):
        c = hj/gj
        res = C*c**m/gj
        for i2, (g, h) in enumerate(facs):
            if i2 != j: res = res/(g*c - h)
        tot += -res*mp.log(-c)
    return tot

# ---- integrand bookkeeping:  term = (prefactor_without_poles(y), polelist, m, facs(y))
# polelist: list of (y0, s) meaning a factor 1/(y - y0 + s*i0) (s = +1 or -1) times its residue-free part.
def A_terms(y, pa, a1, a2, colour):
    d0, d10, d20, beta, al0, al1, al2 = (pa[k] for k in ('d0','d10','d20','beta','al0','al1','al2'))
    e = TINY; ie = I*e; i3 = I**3
    z1 = (a1 - ie)/(2*y)
    out = {+1: [], -1: []}
    if y > 0:
        if colour == '12':
            out[+1].append((-i3/(y*d0), [], 1, [(2*(al0 - z1 + ie), a2 - ie), (2*(al1 + ie), a2 - ie)]))
        else:
            # factor 1/(al2 - z1 + i0) = (2y/(2 al2)) / (y - y0 + i0 sgn(al2)),  y0 = a1/(2 al2) if al2 > 0
            pref = -i3/(4*y*d0)*2
            if al2 > 0:
                y0 = a1/(2*al2)
                pref2 = pref*(2*y)/(2*al2)
                out[+1].append((pref2, [(y0, +1)], 0, [(2*(al0 - z1 + ie), a2 - ie)]))
                out[-1].append((-pref2, [(y0, +1)], 0, [(2*(d20 + ie), -(a2 - ie))]))
            else:
                pref2 = pref/(al2 - z1 + ie)
                out[+1].append((pref2, [], 0, [(2*(al0 - z1 + ie), a2 - ie)]))
                out[-1].append((-pref2, [], 0, [(2*(d20 + ie), -(a2 - ie))]))
    else:
        if colour == '12':
            pref = i3/(4*y*d0*(d10 + z1 + ie))*2       # d10 + z1 < 0 always (bound state, y<0): no pole
            out[+1].append((pref, [], 0, [(2*(al1 + ie), a2 - ie)]))
            out[-1].append((-pref, [], 0, [(2*(z1 - beta + ie), -(a2 - ie))]))
        else:
            out[-1].append((-i3/(4*y*d0)*4, [], 1, [(2*(d20 + ie), -(a2 - ie)), (2*(z1 - beta + ie), -(a2 - ie))]))
    return out

def B_terms(y, pb, colour):
    d0, d10, d20, beta, al0, al1, al2 = (pb[k] for k in ('d0','d10','d20','beta','al0','al1','al2'))
    e = TINY; ie = I*e; i3 = I**3
    f1 = (-1, (y + beta - ie)); f2 = (1, -(y + al0 + ie))
    if colour == '12':
        return [(i3, [], 0, [f1, f2, (1, -(al1 + ie))])]
    else:
        # 1/(al2 + y + i0) = 1/(y - y0 + i0), y0 = -al2
        return [(i3, [(-al2, +1)], 0, [f1, f2])]

def integrand_parts(y, pa, pb, a1, a2, cA, cB):
    """returns list of (value_without_pole_factors, polelist) for this y (sum over x half-lines)."""
    FA = A_terms(y, pa, a1, a2, cA); JB = B_terms(y, pb, cB)
    parts = []
    for sx in (+1, -1):
        for (C1, p1, m1, f1) in FA[sx]:
            for (C2, p2, m2, f2) in JB:
                parts.append((int_halfline(C1*C2, m1 + m2, f1 + f2, sx), p1 + p2))
    return parts

def special_points(pa, pb, a1, a2, sgn):
    pts = set()
    cand = [-pb['al0'], -pb['beta'], -pb['al1'] - pb['al0'], -pb['al2'], pb['al1'] - pb['beta'], pb['al1'] - pb['al0']]
    for key in ('al0', 'al1', 'al2'):
        if pa[key] != 0: cand.append(a1/(2*pa[key]))
    for key in ('d10', 'd20', 'beta'):
        cand.append(-a1/(2*pa[key]))
    if pa['al0'] - pa['al1'] != 0: cand.append(a1/(2*(pa['al0'] - pa['al1'])))
    for c in cand:
        c = mp.mpf(c)
        if c*sgn > 0: pts.add(abs(c))
    return sorted(pts)

def outer(pa, pb, a1, a2, cA, cB, sgn, ymin=mp.mpf('1e-14'), ymax=mp.mpf('1e8'), dense=40):
    """integral over y in sgn*(0,inf) of the full integrand / (2pi)^2 ."""
    sp = special_points(pa, pb, a1, a2, sgn)
    # gather all pole locations with prescriptions (they do not depend on y)
    probe = integrand_parts(sgn*mp.mpf('0.37')*(sp[0] if sp else 1), pa, pb, a1, a2, cA, cB)
    poles = {}
    # poles are attached per part; re-identify at evaluation time
    def f(t):
        y = sgn*mp.e**t
        tot = mp.mpc(0)
        for (v, pl) in integrand_parts(y, pa, pb, a1, a2, cA, cB):
            for (y0, s) in pl:
                v = v/(y - y0 + s*I*TINY)
            tot += v
        return tot*mp.e**t
    # breakpoints in t = log|y|
    bks = [mp.log(ymin)] + [mp.log(p) for p in sp if ymin < p < ymax] + [mp.log(ymax)]
    fine = sorted(set(list(mp.linspace(mp.log(ymin), mp.log(ymax), dense)) + bks))
    # identify real poles inside the range: from A al2>0 and B -al2
    rpoles = []
    if cB == '21' and (-pb['al2'])*sgn > 0: rpoles.append((mp.mpf(-pb['al2']), +1))
    if cA == '21' and sgn > 0 and pa['al2'] > 0: rpoles.append((a1/(2*pa['al2']), +1))
    val = mp.mpc(0)
    if not rpoles:
        val = mp.quad(f, fine)
    else:
        # subtract poles: around each pole y0 use symmetric window in y of half-width w
        segs = []
        lo = mp.log(ymin)
        windows = []
        for (y0, s) in rpoles:
            w = abs(y0)*mp.mpf('0.2')
            windows.append((abs(y0) - w, abs(y0) + w, y0, s))
        windows.sort(key=lambda z: z[0])
        # regular parts
        edges = [mp.log(ymin)]
        for (a, b, y0, s) in windows:
            edges += [mp.log(a), mp.log(b)]
        edges.append(mp.log(ymax))
        for k in range(0, len(edges), 2):
            a, b = edges[k], edges[k+1]
            pts = sorted(set([a, b] + [t for t in fine if a < t < b]))
            val += mp.quad(f, pts)
        # pole windows (in y directly): G(y) = integrand*(y - y0 + s i0)
        for (a, b, y0, s) in windows:
            def G(yy):
                tot = mp.mpc(0)
                yv = sgn*yy
                for (v, pl) in integrand_parts(yv, pa, pb, a1, a2, cA, cB):
                    for (yp, sp_) in pl:
                        if abs(yp - y0) > mp.mpf('1e-30'):
                            v = v/(yv - yp + sp_*I*TINY)
                    tot += v
                return tot
            # integral over |y| in (a,b) of G(y)/(y - y0 + s i0) dy with y = sgn*|y|; dy = sgn d|y|
            Y0 = abs(y0); G0 = G(Y0)
            inner_pts = sorted(set([a, Y0, b] + [p for p in sp if a < p < b]))
            reg = mp.quad(lambda yy: (G(yy) - G0)/(sgn*yy - y0), inner_pts)
            # PV of int_a^b d|y| / (sgn|y| - y0) = sgn*log((b-Y0)/(Y0-a)) ; delta part: sgn*(-s i pi) ... careful:
            # int dy/(y-y0+s i0) over the y-interval = PV - s i pi ; in |y| variable dy = sgn d|y|
            pv = mp.log((b - Y0)/(Y0 - a))   # = PV int_{y-interval} dy/(y-y0) (orientation increasing y)
            if sgn > 0:
                val += reg + G0*(pv - s*I*mp.pi)
            else:
                # y in (-b,-a):  int_a^b d|y| G/(-(|y|-Y0) + s i0) = reg - G0*(pv + s i pi)
                val += reg - G0*(pv + s*I*mp.pi)
    return val/(2*mp.pi)**2

def weights(pa, pb, a1, a2):
    res = {}
    for cA, cB in itertools.product(('12','21'), repeat=2):
        res[(cA, cB)] = outer(pa, pb, a1, a2, cA, cB, +1) + outer(pa, pb, a1, a2, cA, cB, -1)
    return res

if __name__ == '__main__':
    lam = mp.mpf(sys.argv[1]) if len(sys.argv) > 1 else mp.mpf('0.1')
    setB = sys.argv[2] if len(sys.argv) > 2 else 'base'
    sc = lambda v: (lam*mp.mpf(v[0]), lam*mp.mpf(v[1]))
    k1T = sc(('0.8', '0.1')); k2T = sc(('-0.3', '0.9'))
    k1Tm = (-k1T[0], -k1T[1]); k2Tm = (-k2T[0], -k2T[1])
    sets = {
      # name: (A: M, ma, ms, xs, sT) , (B: M, ma, ms, xs, sT)
      'base': (('0.9','0.5','0.7','0.4',('0.3','0.2')),  ('0.8','0.6','0.5','0.55',('-0.25','0.4'))),
      'alt':  (('0.9','0.5','0.7','0.4',('0.3','0.2')),  ('0.8','0.6','0.5','0.55',('-0.9','1.1'))),
      'apole':(('0.9','0.5','0.7','0.4',('-0.3','1.0')), ('0.8','0.6','0.5','0.55',('-0.25','0.4'))),
      'both': (('0.9','0.5','0.7','0.4',('-0.3','1.0')), ('0.8','0.6','0.5','0.55',('-0.9','1.1'))),
      'altswap': (('0.8','0.6','0.5','0.55',('0.9','-1.1')), ('0.9','0.5','0.7','0.4',('-0.3','-0.2'))),
      'baseswap': (('0.8','0.6','0.5','0.55',('0.25','-0.4')), ('0.9','0.5','0.7','0.4',('-0.3','-0.2'))),
    }
    (MA, maA, msA, xA, sTA), (MB, maB, msB, xB, sTB) = sets[setB]
    pa = jet_params(mp.mpf(MA)*lam, mp.mpf(maA)*lam, mp.mpf(msA)*lam, mp.mpf(xA), sc(sTA), k1T, k2T)
    pb = jet_params(mp.mpf(MB)*lam, mp.mpf(maB)*lam, mp.mpf(msB)*lam, mp.mpf(xB), sc(sTB), k1Tm, k2Tm)
    a1 = k1T[0]**2 + k1T[1]**2; a2 = k2T[0]**2 + k2T[1]**2
    res = weights(pa, pb, a1, a2)
    N = sum(res.values()); N0 = (I/pa['d0'])*(I/pb['d0'])/(a1*a2)
    popp = (res[('12','21')] + res[('21','12')])/N
    print(f"lam={mp.nstr(lam,4)} set={setB}: alphas A=({mp.nstr(pa['al1']/lam**2,4)},{mp.nstr(pa['al2']/lam**2,4)}) B=({mp.nstr(pb['al1']/lam**2,4)},{mp.nstr(pb['al2']/lam**2,4)})")
    print(f"   N/N0 = {mp.nstr(N/N0, 12)}")
    for k, v in res.items(): print(f"   W{k} = {mp.nstr(v/N, 12)}")
    print(f"   p_opp = {mp.nstr(popp, 12)}", flush=True)
    pred = 0
    if pa['al1'] > 0: pred += a1*pa['al1']/(a1*pa['al1'] + a2*abs(pa['d10']))/2
    if pa['al2'] > 0: pred += a2*pa['al2']/(a2*pa['al2'] + a1*abs(pa['d20']))/2
    if pb['al1'] > 0: pred += a1*pb['al1']/(a1*pb['al1'] + a2*abs(pb['d10']))/2
    if pb['al2'] > 0: pred += a2*pb['al2']/(a2*pb['al2'] + a1*abs(pb['d20']))/2
    print(f"   naive pole-formula prediction for Re p_opp (region-II analysis): {mp.nstr(pred, 8)}", flush=True)
