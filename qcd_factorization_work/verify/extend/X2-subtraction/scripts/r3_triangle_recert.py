"""X2 final revision / r3_triangle_recert.py -- the triangle certificates of r1_triangle_recert.py (Thm B.4, Prop B.3),
re-run with the S+-repaired tool (r2_lptools, via r3_lptools) and archived SELF-CONTAINED (LP data stored with every
piece) in logs/r3_triangle_certificates_sc.json.gz.  Items, cells, covers, eps values and sliver sub-domains are those
of r1_triangle_recert.py (imported, unchanged)."""
import sys, os, json, time, gzip
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
from fractions import Fraction as Fr
import r1_triangle_recert as R1
from r3_lptools import certify_piece

def run(label, N, D, cell, cons, eps, archive, theta=None, kind='item'):
    if cell == 'BIG':
        Nl, Dl, loc, fz = sp.expand(N), D, [R1.u, R1.kap], {}
    else:
        Nl, Dl, loc, fz = R1.cell_args(N, D, cell)
    wv = [1]*len(loc)
    if eps:
        wv[loc.index(R1.kap)] = 1 - Fr(eps)
    out = certify_piece(Nl, Dl, loc, R1.m2, cons, w=wv, frozen=fz, label=label, keep=True)
    archive.append(dict(label=label, kind=kind, theta=theta, cell=cell, eps=str(eps), status=out['status'],
                        exponent=(str(out.get('exponent')) if out.get('phi') is not None else None),
                        Lpow=out.get('Lpow'), slope=(str(out['slope']) if out.get('slope') is not None else None),
                        certs=out.get('certs', []), lpdata=out['lpdata']))
    return out

if __name__ == "__main__":
    t0 = time.time(); archive = []
    for eps in [0, Fr(1, 10)]:
        for theta in [2, 1]:
            if theta == 1 and eps:
                continue
            worst = None
            for (lab, N, D, cell, cons) in R1.items_for(theta):
                o = run(f'theta={theta} {lab}', N, D, cell, cons, eps, archive, theta=theta)
                if o['status'] == 'ok':
                    e_ = o['exponent']; worst = e_ if (worst is None or e_ < worst) else worst
                elif o['status'] != 'zero':
                    print(f"   FAILED {lab}: {o['status']}", flush=True); worst = -99
            print(f"theta={theta} eps={eps}: worst item exponent {worst}", flush=True)
        for (lab, N, D, cell, cons) in R1.remainder_items():
            o = run(lab, N, D, cell, cons, eps, archive, kind='remainder')
            print(f"eps={eps} {lab:22s}: {o['status']} lambda^{o.get('exponent')} L^(<={o.get('Lpow')}) slope {o.get('slope')}", flush=True)
        for (lab, (Nl, Dl, loc, fz), cons) in R1.sliver_items():
            wv = [1]*len(loc)
            if eps:
                wv[loc.index(R1.kap)] = 1 - Fr(eps)
            o = certify_piece(Nl, Dl, loc, R1.m2, cons, w=wv, frozen=fz, label=lab, keep=True)
            archive.append(dict(label=lab, kind='sliver', theta=None, cell='sliver', eps=str(eps), status=o['status'],
                                exponent=str(o.get('exponent')), Lpow=o.get('Lpow'), slope=str(o.get('slope')),
                                certs=o.get('certs', []), lpdata=o['lpdata']))
            print(f"eps={eps} {lab:22s}: {o['status']} lambda^{o.get('exponent')} L^(<={o.get('Lpow')}) slope {o.get('slope')}", flush=True)
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs', 'r3_triangle_certificates_sc.json.gz')
    with gzip.open(path, 'wt') as fh:
        json.dump(archive, fh, default=str)
    ncert = sum(len(a['certs']) for a in archive)
    print(f"archived {len(archive)} piece records, {ncert} monomial certificates -> {path}  [{time.time()-t0:.0f}s]")
