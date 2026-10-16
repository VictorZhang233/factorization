"""X2 final2 -- f2v_dump_UF.py: print U, F (normalization U = det M = det A_T, F = U * stationary value; P' = Qt2/(2P))
of the nine singles and of the full planar/crossed vertex, and the line factors, for transcription into Prop E.4/E.5.
Run: python3 -I f2v_dump_UF.py (log: ../final2_logs/f2v_dump_UF.log)"""
import sys, os, io, contextlib
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import sympy as sp
with contextlib.redirect_stdout(io.StringIO()):
    import f2v_UF_polytopes as V
ren = dict(zip(V.XS, sp.symbols('x_g1 x_g2 x_a1 x_a2 x_b1 x_b2', positive=True)))
def show(E):
    E2 = sp.expand(sp.cancel(E.subs(V.Pp, V.Qt2/(2*V.P))))
    return sp.factor(E2.xreplace(ren))
for R in V.SINGLES:
    print(f"--- {R}")
    for ln in V.LINES:
        print(f"    {ln}: {sp.factor(V.zeroed_factor(ln, V.Z[R][ln]).subs(V.Pp, V.Qt2/(2*V.P)))}")
    print(f"    U = {show(V.SDATA[R]['U'])}")
    print(f"    F = {show(V.SDATA[R]['F'])}")
    fct = V.SDATA[R]['facets']
    print(f"    facets ({len(fct)}): " + "; ".join(f"{mu}:{nu}" for mu, nu in sorted(fct.items(), key=lambda kv: (kv[1], kv[0]))))
for kind in ['planar', 'crossed']:
    print(f"--- full {kind}: U = {show(V.FULL[kind]['U'])}")
    print(f"    F = {show(V.FULL[kind]['F'])}")
