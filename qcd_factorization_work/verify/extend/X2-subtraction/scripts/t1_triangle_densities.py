"""X2 / T1: one-loop off-shell triangle -- fibered (k^- integrated) densities of Gamma and of the four
Collins subtraction terms, derived independently by symbolic residues (sympy), and checked against
(a) the hand-derived closed forms used in REPORT.md, (b) direct numerical k^- integration with finite i*eta.

Conventions (REPORT.md Sec. B.1):  k=(x, km, kT), k^2 = 2 x km - kap, kap = kT^2.
  Dg = -k^2,  D1 = m2 + 2P km - (m2/P) x - k^2,  D2 = m2 + 2P' x - (m2/P') km - k^2   (all  - i0)
  e1 = m2 + 2P km, h1 = 2P km, t1 = 2P km - k^2 ;  e2 = m2 + 2P' x, h2 = 2P' x, t2 = 2P' x - k^2
  C_S = 1/(Dg e1 e2); C_C1 = 1/(Dg h2) (1/D1 - 1/e1); C_C2 = 1/(Dg h1)(1/D2 - 1/e2); C_H = Dg/(t1 h1 t2 h2)
Fibered density: rho_F(x,kap) = (1/(i pi)) * int dkm F   (so that  int d^4k/(i pi^2) F = int dx dkap rho_F ).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

x, km, kap, m2, P, Pp = sp.symbols('x km kap m2 P Pp', real=True)
eta = sp.symbols('eta', positive=True)

k2 = 2*x*km - kap
Dg = -k2
D1 = m2 + 2*P*km - (m2/P)*x - k2
D2 = m2 + 2*Pp*x - (m2/Pp)*km - k2
e1 = m2 + 2*P*km; h1 = 2*P*km; t1 = 2*P*km - k2
e2 = m2 + 2*Pp*x; h2 = 2*Pp*x; t2 = 2*Pp*x - k2

terms = {
    'Gamma': [(1, [Dg, D1, D2], [])],
    'C_S':   [(1, [Dg, e1], [e2])],
    'C_C1':  [(1, [Dg, D1], [h2]), (-1, [Dg, e1], [h2])],
    'C_C2':  [(1, [Dg, h1, D2], []), (-1, [Dg, h1], [e2])],
    'C_H':   [(1, [t1, h1, t2], [h2], Dg)],
}

def fibered_symbolic(dens_kdep, dens_const, num, xval_sign_info):
    """Return rho for a product num/(prod dens_kdep * prod dens_const), each dens_kdep linear in km,
    with -i eta.  xval_sign_info: dict of numerical values to decide pole sides."""
    # each denominator D = a*km + b - i*eta ; pole km0 = (-b + i eta)/a  ->  Im km0 = eta/a
    poles = []
    for D in dens_kdep:
        a = sp.diff(D, km); b = sp.simplify(D - a*km)
        assert sp.diff(a, km) == 0
        aval = float(a.subs(xval_sign_info))
        poles.append((D, a, b, 'upper' if aval > 0 else 'lower'))
    ups = [p for p in poles if p[3] == 'upper']
    lows = [p for p in poles if p[3] == 'lower']
    if not ups or not lows:
        return sp.Integer(0)
    # close in upper half plane: int = 2 pi i sum Res_upper
    tot = 0
    F = num / sp.Mul(*[p[0] for p in poles]) / sp.Mul(*dens_const)
    for (D, a, b, side) in ups:
        km0 = -b/a
        res = sp.simplify((F*D/a).subs(km, km0)) if True else None
        # careful: F*D cancels D; need limit form
        Fd = num / sp.Mul(*[q[0] for q in poles if q[0] is not D]) / sp.Mul(*dens_const) / a
        tot += Fd.subs(km, km0)
    # rho = (1/(i pi)) * 2 pi i * sum Res = 2 * sum Res
    return sp.simplify(2*tot)

# hand-derived forms (REPORT.md (B.4)-(B.8))
A = x*m2*(1 - x/P) + P*kap
B = x*m2 + P*kap
a2 = m2/Pp
k1m = -(m2*(1 - x/P) + kap)/(2*(P - x))
k2m = (m2 + 2*Pp*x + kap)/(a2 + 2*x)
hand = {
 ('Gamma', 'mid'): 1/((P - x)*Dg*D2).subs(km, k1m),
 ('Gamma', 'neg'): (2/((a2 + 2*x)*Dg*D1)).subs(km, k2m),
 ('C_S', 'mid'): 1/(B*e2), ('C_S', 'big'): 1/(B*e2), ('C_S', 'neg'): 0,
 ('C_C1', 'mid'): x*m2/(2*P*Pp*A*B), ('C_C1', 'big'): -1/(2*Pp*x*B), ('C_C1', 'neg'): 0,
 ('C_C2', 'mid'): -(1/P)/((e2 + kap)*e2), ('C_C2', 'big'): -(1/P)/((e2 + kap)*e2),
 ('C_C2', 'neg'): (2/((a2 + 2*x)*Dg*h1)).subs(km, k2m),
 ('C_H', 'mid'): -x/(P*(h2 + kap)*(h2*(P - x) + P*kap)), ('C_H', 'big'): 1/(P*(h2 + kap)*h2), ('C_H', 'neg'): 0,
}
ranges = {'neg': {x: -0.3e-2, P: 0.8, Pp: 1.3, m2: 0.02, kap: 0.1},   # -m2/(2P') < x < 0
          'mid': {x: 0.37, P: 0.8, Pp: 1.3, m2: 0.02, kap: 0.1},
          'big': {x: 1.7, P: 0.8, Pp: 1.3, m2: 0.02, kap: 0.1}}

ok = True
results = {}
for name, lst in terms.items():
    for rg, vals in ranges.items():
        tot = 0
        for item in lst:
            if len(item) == 3:
                c, dk, dc = item; num = sp.Integer(c)
            else:
                c, dk, dc, nm = item; num = c*nm
            tot += fibered_symbolic(dk, dc, num, vals)
        tot = sp.simplify(tot)
        results[(name, rg)] = tot
        h = hand[(name, rg)] if (name, rg) in hand else None
        if h is None:
            continue
        diff = sp.simplify(sp.together(tot - h))
        # numerical spot check at random points in range
        import random
        random.seed(1)
        maxd = 0
        for _ in range(5):
            Pv = random.uniform(0.5, 1.5); Ppv = random.uniform(0.5, 1.5); m2v = random.uniform(0.001, 0.05)
            if rg == 'neg': xv = -random.uniform(0.05, 0.95)*m2v/(2*Ppv)
            elif rg == 'mid': xv = random.uniform(0.01, 0.99)*Pv
            else: xv = Pv*random.uniform(1.01, 3)
            kv = random.uniform(1e-4, 2)
            sub = {x: xv, P: Pv, Pp: Ppv, m2: m2v, kap: kv}
            d = abs(complex(tot.subs(sub)) - complex(sp.sympify(h).subs(sub)))
            s = abs(complex(sp.sympify(h).subs(sub))) + 1e-300
            maxd = max(maxd, d/s if s > 1e-200 else d)
        flag = (diff == 0) or maxd < 1e-10
        ok &= flag
        print(f"{name:6s} range={rg:4s}: symbolic diff == 0: {diff == 0}; max rel. numeric diff {maxd:.2e}  {'PASS' if flag else 'FAIL'}")

# direct numerical k^- integration with finite eta at a few points
mp.mp.dps = 30
def num_rho(F, xv, kv, Pv, Ppv, m2v, etav=mp.mpf('1e-7')):
    def f(kmv):
        k2v = 2*xv*kmv - kv
        Dgv = -k2v - 1j*etav
        D1v = m2v + 2*Pv*kmv - (m2v/Pv)*xv - k2v - 1j*etav
        D2v = m2v + 2*Ppv*xv - (m2v/Ppv)*kmv - k2v - 1j*etav
        e1v = m2v + 2*Pv*kmv - 1j*etav; h1v = 2*Pv*kmv - 1j*etav; t1v = 2*Pv*kmv - k2v - 1j*etav
        e2v = m2v + 2*Ppv*xv; h2v = 2*Ppv*xv; t2v = 2*Ppv*xv - k2v - 1j*etav
        return F(Dgv, D1v, D2v, e1v, h1v, t1v, e2v, h2v, t2v)
    # breakpoints at all real parts of the poles (k^- linear denominators)
    poles = [kv/(2*xv), -(m2v*(1-xv/Pv)+kv)/(2*(Pv-xv)), (m2v+2*Ppv*xv+kv)/(2*xv+m2v/Ppv),
             -m2v/(2*Pv), mp.mpf(0), -kv/(2*(Pv-xv)), (2*Ppv*xv+kv)/(2*xv)]
    poles = sorted(set(poles))
    pts = [-mp.inf]
    for p in poles:
        w = 1e-3*(1+abs(p))
        pts += [p - w, p - etav*100, p, p + etav*100, p + w]
    pts += [mp.inf]
    pts = sorted(set(pts))
    val = mp.quad(f, pts, maxdegree=12)
    return val/(1j*mp.pi)
Fs = {
 'Gamma': lambda Dg_,D1_,D2_,e1_,h1_,t1_,e2_,h2_,t2_: 1/(Dg_*D1_*D2_),
 'C_S':   lambda Dg_,D1_,D2_,e1_,h1_,t1_,e2_,h2_,t2_: 1/(Dg_*e1_*e2_),
 'C_C1':  lambda Dg_,D1_,D2_,e1_,h1_,t1_,e2_,h2_,t2_: (1/(Dg_*h2_))*(1/D1_ - 1/e1_),
 'C_C2':  lambda Dg_,D1_,D2_,e1_,h1_,t1_,e2_,h2_,t2_: (1/(Dg_*h1_))*(1/D2_ - 1/e2_),
 'C_H':   lambda Dg_,D1_,D2_,e1_,h1_,t1_,e2_,h2_,t2_: Dg_/(t1_*h1_*t2_*h2_),
}
print("\nDirect numerical k^- integration (eta=1e-12) vs closed forms:")
for name in Fs:
    for rg, xv in [('mid', mp.mpf('0.37')), ('big', mp.mpf('1.7'))]:
        Pv, Ppv, m2v, kv = mp.mpf('0.8'), mp.mpf('1.3'), mp.mpf('0.02'), mp.mpf('0.1')
        nv = num_rho(Fs[name], xv, kv, Pv, Ppv, m2v)
        hexpr = hand.get((name, rg), 0)
        hv = complex(sp.sympify(hexpr).subs({x: float(xv), P: 0.8, Pp: 1.3, m2: 0.02, kap: 0.1}))
        rel = abs(complex(nv) - hv)/max(abs(hv), 1e-3)
        ok &= rel < 1e-4
        print(f"  {name:6s} {rg}: numeric {complex(nv):.10e}  closed {hv:.10e}  rel {rel:.1e}")
print("ALL PASS" if ok else "SOME FAIL")
