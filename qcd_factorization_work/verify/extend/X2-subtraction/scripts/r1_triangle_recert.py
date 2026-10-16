"""X2 fix round 1 / r1_triangle_recert.py -- re-certification of every LP certificate of the one-loop triangle with the
corrected tooling (r1_lptools): exact primal-dual optimal pairs (strong duality asserted), corrected recession check on
every unbounded cell (quadrant splitting), frozen O(1) variables treated as coefficients (never substituted into
numerators), at eps = 0 and eps0 = 1/10 (kappa weight 1-eps0), on the natural cover theta = 2 (main theorem), on the
fat cover theta = 1 (family statement), the global remainder cells and the negative-k+ sliver.  The certificates
(cells, dual vectors, primal points) are archived in logs/r1_triangle_certificates.json.

Cover (units Qt = 1, P = P' = 1/sqrt2, u = k+/P, kap = kT^2, s = lambda^theta):
  U_S  = {0 < u <= s, kap <= u s}
  U_C1 = {s < u <= 1, kap <= u s}  U  {1 < u <= 2, kap <= s}
  U_C2 = {0 < u <= s, u s < kap <= u}  U  sliver {-m2/(2P') < k+ < 0}
  U_H  = complement (all UV directions).
Cells: I = {u <= 1/2} (local u, kap; v = 1-u in [1/2,1] is a frozen coefficient in denominators, the numerator is exact),
       II = {1/2 < u < 1} (local v, kap; u in [1/2,1] frozen in denominators, numerator exact),
       III = {1 < u <= 2} (local kap; u in [1,2] frozen everywhere, numerator support with u as coefficient).
The LP is solved on the log-coordinate superset of each cell (u <= 1 instead of u <= 1/2 etc.); the frozen-variable
comparability holds on the actual cell; constants never change exponents.
"""
import sys, os, json, time
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
from fractions import Fraction as Fr
import t4_triangle_certificates as T4
from r1_lptools import certify_piece

u, v, kap, m2 = T4.u, T4.v, T4.kap, T4.m2
F, Fbig, combo = T4.F, T4.Fbig, T4.combo
HALF = (Fr(1, 2), Fr(1))

def cell_args(N, D, cell):
    if cell == 'I':
        return sp.expand(N.subs(v, 1 - u)), D, [u, kap], {v: HALF}
    if cell == 'II':
        return sp.expand(N.subs(u, 1 - v)), D, [v, kap], {u: HALF}
    if cell == 'III':
        return sp.expand(N), D, [kap], {u: (Fr(1), Fr(2))}
    raise ValueError

def items_for(theta):
    t2 = Fr(theta)/2
    it = []
    def add(lab, table, combo_spec, cell, cons):
        N, D = combo(table, combo_spec)
        it.append((lab, N, D, cell, cons))
    S_cons = [([1, 0], -t2), ([-1, 1], -t2)]
    C1_I = [([1, 0], 0), ([-1, 0], t2), ([-1, 1], -t2)]
    C1_II = [([1, 0], 0), ([0, 1], -t2)]
    C1_III = [([1], -t2)]
    C2_cons = [([1, 0], -t2), ([1, -1], t2), ([-1, 1], 0)]
    add('(H1)_S  G-S', F, [('G', 1), ('S', -1)], 'I', S_cons)
    for nm in ['C1', 'C2', 'H']:
        add(f'(H2)_S  {nm}', F, [(nm, 1)], 'I', S_cons)
    add('(H1)_C1 I', F, [('G', 1), ('S', -1), ('C1', -1)], 'I', C1_I)
    add('(H1)_C1 II', F, [('G', 1), ('S', -1), ('C1', -1)], 'II', C1_II)
    add('(H1)_C1 III', Fbig, [('S', -1), ('C1', -1)], 'III', C1_III)
    for nm in ['C2', 'H']:
        add(f'(H2)_C1 {nm} I', F, [(nm, 1)], 'I', C1_I)
        add(f'(H2)_C1 {nm} II', F, [(nm, 1)], 'II', C1_II)
        add(f'(H2)_C1 {nm} III', Fbig, [(nm, 1)], 'III', C1_III)
    add('(H1)_C2 (u>0)', F, [('G', 1), ('S', -1), ('C2', -1)], 'I', C2_cons)
    for nm in ['C1', 'H']:
        add(f'(H2)_C2 {nm}', F, [(nm, 1)], 'I', C2_cons)
    return it

def remainder_items():
    N, D = combo(F, [('G', 1), ('S', -1), ('C1', -1), ('C2', -1), ('H', -1)])
    Nb, Db = combo(Fbig, [('S', -1), ('C1', -1), ('C2', -1), ('H', -1)])
    return [('r cell I (0<u<=1/2)', N, D, 'I', [([1, 0], 0)]),
            ('r cell II (1/2<u<1)', N, D, 'II', [([1, 0], 0)]),
            ('r u>1 (local u,kap)', Nb, Db, 'BIG', [([-1, 0], 0)])]

def sliver_items():
    """negative-k+ sliver (t4z): w = 2k+ + a, c = a - w, a = sqrt2 m2;  r = num/prod(dens).  Sub-domain A: w <= a/2
    (local w, kap; c = gamma*m2 with gamma in [1/sqrt2, sqrt2] frozen), B: w >= a/2 (local c, kap; w = gamma*m2)."""
    w, c, g = sp.symbols('w c gamma', positive=True)
    s2 = sp.sqrt(2); P = Pp = 1/s2; a = s2*m2
    Dg_num = c*Pp*w + a*kap
    D1_num = (m2*(1 + c/(2*P)) + kap)*w + 2*(Pp*w + kap)*(P + c/2)
    h1_num = 2*P*(Pp*w + kap)
    num = sp.expand(-2*(m2*(1 + c/(2*P))*w + Dg_num)*w)
    dens = [sp.expand(Dg_num), sp.expand(D1_num), sp.expand(h1_num)]
    # sympy positivity test needs rational coefficients: multiply sqrt2 factors out by substituting exact values is fine,
    # positive_form only checks signs.
    A = (sp.expand(num.subs(c, g*m2)), [sp.expand(d.subs(c, g*m2)) for d in dens], [w, kap], {g: (Fr(7, 10), Fr(15, 10))})
    B = (sp.expand(num.subs(w, g*m2)), [sp.expand(d.subs(w, g*m2)) for d in dens], [c, kap], {g: (Fr(7, 10), Fr(15, 10))})
    return [('sliver A (w<=a/2)', A, [([1, 0], -1)]), ('sliver B (w>=a/2)', B, [([1, 0], -1)])]

def run(label, N, D, cell, cons, eps, archive):
    if cell == 'BIG':
        Nl, Dl, loc, fz = sp.expand(N), D, [u, kap], {}
    else:
        Nl, Dl, loc, fz = cell_args(N, D, cell)
    wv = [1]*len(loc)
    if eps:
        wv[loc.index(kap)] = 1 - Fr(eps)
    out = certify_piece(Nl, Dl, loc, m2, cons, w=wv, frozen=fz, label=label, keep=True)
    archive.append(dict(label=label, cell=cell, eps=str(eps), cons=[[list(map(str, g)), str(h)] for g, h in cons],
                        status=out['status'], exponent=(str(out.get('exponent')) if out.get('phi') is not None else None),
                        Lpow=out.get('Lpow'), slope=(str(out['slope']) if out.get('slope') is not None else None),
                        certs=out.get('certs', [])))
    return out

if __name__ == "__main__":
    t0 = time.time()
    archive = []
    summary = {}
    for eps in [0, Fr(1, 10)]:
        for theta in [2, 1]:
            if theta == 1 and eps:
                continue
            print(f"===== theta = {theta}, eps = {eps}", flush=True)
            worst = None
            for (lab, N, D, cell, cons) in items_for(theta):
                o = run(f'theta={theta} {lab}', N, D, cell, cons, eps, archive)
                if o['status'] not in ('ok', 'zero'):
                    print(f"  {lab:20s}: FAILED {o['status']} {o.get('monomial')}", flush=True); worst = -99; continue
                if o['status'] == 'zero':
                    print(f"  {lab:20s}: identically zero"); continue
                e = o['exponent']; worst = e if (worst is None or e < worst) else worst
                print(f"  {lab:20s}: lambda^{e} L^(<={o['Lpow']})  max rec. slope {o['slope']}  (#mon {o['nmon']})", flush=True)
            summary[(theta, str(eps))] = worst
            print(f"  worst item exponent: {worst}", flush=True)
        print(f"===== global remainder cells, eps = {eps}", flush=True)
        for (lab, N, D, cell, cons) in remainder_items():
            o = run(lab, N, D, cell, cons, eps, archive)
            print(f"  {lab:22s}: {o['status']}  lambda^{o.get('exponent')} L^(<={o.get('Lpow')})  max rec. slope {o.get('slope')}", flush=True)
        print(f"===== sliver, eps = {eps}", flush=True)
        for (lab, (Nl, Dl, loc, fz), cons) in sliver_items():
            wv = [1]*len(loc)
            if eps:
                wv[loc.index(kap)] = 1 - Fr(eps)
            o = certify_piece(Nl, Dl, loc, m2, cons, w=wv, frozen=fz, label=lab, keep=True)
            archive.append(dict(label=lab, eps=str(eps), status=o['status'], exponent=str(o.get('exponent')),
                                Lpow=o.get('Lpow'), slope=str(o.get('slope')), certs=o.get('certs', [])))
            print(f"  {lab:22s}: {o['status']}  lambda^{o.get('exponent')} L^(<={o.get('Lpow')})  max rec. slope {o.get('slope')}", flush=True)
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs', 'r1_triangle_certificates.json')
    json.dump(archive, open(out, 'w'), indent=0)
    print("archived", len(archive), "certificates ->", out)
    print("summary (theta, eps) -> worst item exponent:", {str(k): str(v_) for k, v_ in summary.items()})
    print(f"[{time.time()-t0:.0f}s]")
