"""X2 final revision / r3_bubble_recert.py -- the log-weighted triangle family (Thm B.6; called 'bubble class' in rounds
0-2) re-certified exactly as in r2_bubble_recert.py, archived SELF-CONTAINED (LP data with every piece record) in
logs/r3_bubble_certificates_sc.json.gz.  Cells, pieces, alternatives, eps values: those of r2_bubble_recert.py
(imported; only the certificate call and the record are replaced)."""
import sys, os, json, time, gzip
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
_ARGS = sys.argv[1:]
import numpy as np, sympy as sp
from fractions import Fraction as Fr
import r2_bubble_recert as R2B
sys.argv = [sys.argv[0]] + _ARGS
from r3_lptools import certify_piece

def strict_rec(num, dens, region, cons, eps):
    u, v, kap, m2 = R2B.u, R2B.v, R2B.kap, R2B.m2
    if region == 'I':
        N = sp.expand(num.subs(v, 1 - u)); loc = [u, kap]; fz = {v: R2B.HALF}
    elif region == 'II':
        N = sp.expand(num.subs(u, 1 - v)); loc = [v, kap]; fz = {u: R2B.HALF}
    else:
        N = sp.expand(num); loc = [u, kap]; fz = {}
    if N == 0:
        return np.inf, None, dict(status='zero')
    wv = [1, 1 - Fr(eps)] if eps else [1, 1]
    o = certify_piece(N, dens, loc, m2, cons, w=wv, frozen=fz, keep=True)
    if o['status'] == 'zero':
        return np.inf, None, dict(status='zero')
    if o['status'] != 'ok':
        return -np.inf, o['status'], dict(status=o['status'])
    rec = dict(status='ok', region=region, exponent=str(o['exponent']), Lpow=o['Lpow'], slope=str(o['slope']),
               certs=o['certs'], lpdata=o['lpdata'])
    return float(o['exponent']), o['slope'], rec
R2B.strict_rec = strict_rec          # run_items / run_remainder_* look the name up in the module namespace

if __name__ == "__main__":
    t0 = time.time(); log = []
    for eps in [Fr(0), Fr(1, 10)]:
        R2B.run_items(eps, log)
        R2B.run_remainder_big_u(eps, log)
        R2B.run_remainder_small_u(eps, log)
        print(f"[{time.time()-t0:.0f}s]", flush=True)
    path = os.path.join(os.path.dirname(R2B.HERE), 'logs', 'r3_bubble_certificates_sc.json.gz')
    with gzip.open(path, 'wt') as fh:
        json.dump(R2B.ARCHIVE, fh, default=str)
    ncert = sum(len(e['record'].get('certs', [])) for e in R2B.ARCHIVE if e['record'])
    print(f"archived {len(R2B.ARCHIVE)} piece records, {ncert} monomial certificates -> {path}  [{time.time()-t0:.0f}s]")
    json.dump(log, open(os.path.join(os.path.dirname(R2B.HERE), 'logs', 'r3_bubble_recert_summary.json'), 'w'), indent=1, default=str)
