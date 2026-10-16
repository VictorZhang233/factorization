"""X2 fix round 1 / r1_bubble_recert.py -- re-certification of the bubble-chain (log-insertion) class with the corrected
tooling (r1_lptools): exact primal-dual optimal pairs, corrected recession check (quadrant splitting) on every
unbounded cell, eps = 0 and eps0 = 1/10 (kappa weight 1 - eps0, hybrid scheme: d-dimensional outer measure with the
fixed 4D log insertion).

Covered here:
  (a) remainder, 0<u<1: the 270 cells of t15 (pieces P0..P4, best valid alternative per piece, 'strict' selection);
      the corner cell II {Xv<=-3, Xk<=-4} is bounded shell by shell, |rho^(j)| <= sum_s |l_s|^j |T_s| (as t15f);
  (b) remainder, u>1: the 60 cells of t15b (shells e,h only; pieces rho_r(u>1) and w_a |T_e|);
  (c) (H1)/(H2) items at theta = 2 (as t17y), U_S, U_C1 (s<u<=1), U_C2 (u>0 part).
Not needed as separate LPs (single-shell structure, see REPORT X2-Thm3.9): the sliver -m2/(2P') < k+ < 0 (there
rho_r^(j) = l_sl^j rho_r^(0) exactly, l_sl = ln Dg at the D2 pole, so the triangle sliver certificates apply with the
log weight |l_sl|^j <= (C L (1+|X|))^j), and the part-III items (1<u<=2) of U_C1 (each Collins term is a single shell
there: C_S, C_C1 on the e shell, C_C2, C_H on the h shell, Gamma = 0)."""
import sys, os, json, time
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, sympy as sp
from fractions import Fraction as Fr
import t15_bubble_certificate as B15
_ARGS = sys.argv[1:]
sys.argv = [sys.argv[0], '2']      # t17 reads theta from argv at import
import t17_bubble_H1H2 as B17
sys.argv = [sys.argv[0]] + _ARGS
from r1_lptools import certify_piece

u, v, kap, m2 = B15.u, B15.v, B15.kap, B15.m2
combine, T, weighted = B15.combine, B15.T, B15.weighted
HALF = (Fr(1, 2), Fr(1))
HERE = os.path.dirname(os.path.abspath(__file__))

def strict(num, dens, region, cons, eps):
    if region == 'I':
        N = sp.expand(num.subs(v, 1 - u)); loc = [u, kap]; fz = {v: HALF}
    elif region == 'II':
        N = sp.expand(num.subs(u, 1 - v)); loc = [v, kap]; fz = {u: HALF}
    else:   # 'BIG' : u>1, local (u,kap), no v
        N = sp.expand(num); loc = [u, kap]; fz = {}
    if N == 0:
        return np.inf, None
    wv = [1, 1 - Fr(eps)] if eps else [1, 1]
    o = certify_piece(N, dens, loc, m2, cons, w=wv, frozen=fz)
    if o['status'] == 'zero':
        return np.inf, None
    if o['status'] != 'ok':
        return -np.inf, o['status']
    return float(o['exponent']), o['slope']

def cell_cons(region, a_, b_, c_, d_):
    cons = []
    if np.isfinite(b_): cons.append(([1, 0], Fr(b_).limit_denominator(100)))
    if np.isfinite(a_): cons.append(([-1, 0], Fr(-a_).limit_denominator(100)))
    if region == 'I':
        if np.isfinite(d_): cons.append(([-1, 1], Fr(d_).limit_denominator(100)))
        if np.isfinite(c_): cons.append(([1, -1], Fr(-c_).limit_denominator(100)))
    else:
        if np.isfinite(d_): cons.append(([0, 1], Fr(d_).limit_denominator(100)))
        if np.isfinite(c_): cons.append(([0, -1], Fr(-c_).limit_denominator(100)))
    return cons

def pieces_small_u():
    nr, dr = combine([(1, T[s]) for s in ['D', 'e', 't', 'h']])
    wa = [(u*m2, [kap]), (sp.Integer(1), [])]; wb = [(u, [v]), (sp.Integer(1), [])]
    return [('P0', [(nr, dr)]), ('P1', [weighted(['D', 'e'], wn, wd) for (wn, wd) in wa]),
            ('P2', [weighted(['D', 't'], wn, wd) for (wn, wd) in wb]),
            ('P3', [weighted(['D'], u**2*m2, [u*m2*v + kap]), weighted(['D'], sp.Integer(1), [])]),   # |delta| <= min(d, C L(1+|X|))
            ('P4', [weighted(['D'], an*bn, ad + bd) for (an, ad) in wa for (bn, bd) in wb])]

def run_remainder_small_u(eps, log):
    cells = json.load(open(os.path.join(HERE, 'bubble_cells.json')))
    PCS = pieces_small_u()
    worst = np.inf; worst_slope = None; nfail = 0
    for idx, (region, a_, b_, c_, d_, _, _) in enumerate(cells):
        a_ = -np.inf if a_ is None else a_; b_ = np.inf if b_ is None else b_
        c_ = -np.inf if c_ is None else c_; d_ = np.inf if d_ is None else d_
        cons = cell_cons(region, a_, b_, c_, d_)
        corner = (region == 'II' and a_ == -np.inf and b_ == -3 and c_ == -np.inf and d_ == -4)
        if corner:
            # shell-by-shell bound on the corner
            ex = np.inf
            for s_ in ['D', 'e', 't', 'h']:
                e_, sl = strict(T[s_][0], T[s_][1], region, cons, eps)
                ex = min(ex, e_)
                if sl is not None: worst_slope = sl if (worst_slope is None or sl > worst_slope) else worst_slope
            cell_e = ex; tag = 'corner(shells)'
        else:
            cell_e = np.inf; tag = ''
            for pname, alts in PCS:
                best = -np.inf; best_sl = None
                for (nn, dd) in alts:
                    e_, sl = strict(nn, dd, region, cons, eps)
                    if e_ > best: best, best_sl = e_, sl
                if best_sl is not None and not isinstance(best_sl, str):
                    worst_slope = best_sl if (worst_slope is None or best_sl > worst_slope) else worst_slope
                if best < cell_e: cell_e, tag = best, pname
        worst = min(worst, cell_e)
        if cell_e < 2 - 4*float(eps) - 1e-9:
            nfail += 1
            print(f"   cell {region} [{a_},{b_}]x[{c_},{d_}]: exponent {cell_e} ({tag})  ** below target **", flush=True)
        if idx % 30 == 0:
            print(f"   ... {idx}/{len(cells)} cells, running min exponent {worst}", flush=True)
    log.append(dict(part='remainder 0<u<1', eps=str(eps), cells=len(cells), min_exponent=worst,
                    worst_slope=str(worst_slope), below_target=nfail))
    print(f"(a) remainder 0<u<1, eps={eps}: {len(cells)} cells, min exponent {worst}, worst recession slope {worst_slope}, "
          f"cells below 2-4eps: {nfail}", flush=True)

def run_remainder_big_u(eps, log):
    Te = (m2, [u, m2 + u, u*m2 + kap]); Th = T['h']
    y_edges = [-np.inf, -4, -3, -2, -1.5, -1.25, -1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 1, 2, np.inf]
    x_edges = [0, 0.25, 0.5, 1, np.inf]
    worst = np.inf; worst_slope = None; ncell = 0; nfail = 0
    nr, dr = combine([(1, Te), (1, Th)])
    for (a_, b_) in zip(x_edges[:-1], x_edges[1:]):
        for (c_, d_) in zip(y_edges[:-1], y_edges[1:]):
            cons = [([-1, 0], Fr(-a_).limit_denominator(100))]
            if np.isfinite(b_): cons.append(([1, 0], Fr(b_).limit_denominator(100)))
            if np.isfinite(d_): cons.append(([-1, 1], Fr(d_).limit_denominator(100)))
            if np.isfinite(c_): cons.append(([1, -1], Fr(-c_).limit_denominator(100)))
            e0, s0 = strict(nr, dr, 'BIG', cons, eps)
            e1b, s1b = -np.inf, None
            for (wn, wd) in [(u*m2, [kap]), (sp.Integer(1), [])]:
                e1, s1 = strict(sp.expand(wn*Te[0]), list(wd) + list(Te[1]), 'BIG', cons, eps)
                if e1 > e1b: e1b, s1b = e1, s1
            cell = min(e0, e1b); ncell += 1
            for sl in (s0, s1b):
                if sl is not None and not isinstance(sl, str):
                    worst_slope = sl if (worst_slope is None or sl > worst_slope) else worst_slope
            worst = min(worst, cell)
            if cell < 2 - 4*float(eps) - 1e-9:
                nfail += 1; print(f"   u>1 cell [{a_},{b_}]x[{c_},{d_}]: {e0}, {e1b} ** below target **", flush=True)
    log.append(dict(part='remainder u>1', eps=str(eps), cells=ncell, min_exponent=worst, worst_slope=str(worst_slope),
                    below_target=nfail))
    print(f"(b) remainder u>1, eps={eps}: {ncell} cells, min exponent {worst}, worst recession slope {worst_slope}, "
          f"cells below 2-4eps: {nfail}", flush=True)

def run_items(eps, log):
    t2 = Fr(1)        # theta = 2
    REG = {'U_S': [('I', [([1, 0], -t2), ([-1, 1], -t2)])],
           'U_C1': [('I', [([1, 0], 0), ([-1, 0], t2), ([-1, 1], -t2)]), ('II', [([1, 0], 0), ([0, 1], -t2)])],
           'U_C2': [('I', [([1, 0], -t2), ([1, -1], t2), ([-1, 1], 0)])]}
    worst = np.inf; worst_slope = None
    for U, names in B17.CHECK.items():
        for nm in names:
            if nm == '(H1)_C2 G-S-C2':
                continue      # superseded by the 'alt' decomposition (t17x/t17y)
            main, corr = B17.ITEMS[nm]
            for (region, cons) in REG[U]:
                es = []
                num, dens = B17.combine(main)
                e_, sl = strict(num, dens, region, cons, eps); es.append(e_)
                if sl is not None and not isinstance(sl, str):
                    worst_slope = sl if (worst_slope is None or sl > worst_slope) else worst_slope
                for (pair, its) in corr:
                    num, dens = B17.combine(its)
                    wn, wd = B17.W[pair]
                    alts = [strict(num, dens, region, cons, eps),
                            strict(sp.expand(wn*num), list(wd) + list(dens), region, cons, eps)]
                    e_, sl = max(alts, key=lambda z: z[0]); es.append(e_)
                    if sl is not None and not isinstance(sl, str):
                        worst_slope = sl if (worst_slope is None or sl > worst_slope) else worst_slope
                e = min(es); worst = min(worst, e)
                print(f"   {U:5s} {nm:18s} {region}: {es} -> lambda^{e}", flush=True)
    log.append(dict(part='items theta=2', eps=str(eps), min_exponent=worst, worst_slope=str(worst_slope)))
    print(f"(c) items theta=2, eps={eps}: min exponent {worst}, worst recession slope {worst_slope}", flush=True)

if __name__ == "__main__":
    t0 = time.time(); log = []
    parts = sys.argv[1:] or ['items', 'big', 'small']
    EPS = [Fr(e) for e in os.environ.get('R1_EPS', '0,1/10').split(',')]
    for eps in EPS:
        if 'items' in parts: run_items(eps, log)
        if 'big' in parts: run_remainder_big_u(eps, log)
        if 'small' in parts: run_remainder_small_u(eps, log)
        print(f"[{time.time()-t0:.0f}s]", flush=True)
    json.dump(log, open(os.path.join(os.path.dirname(HERE), 'logs', 'r1_bubble_recert_' + '_'.join(parts) + '_eps' + '_'.join(str(e).replace('/', 'o') for e in EPS) + '.json'), 'w'),
              indent=1, default=str)
