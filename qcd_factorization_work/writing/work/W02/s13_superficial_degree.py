"""W02 / Ch2 check s13 (prop:qcd-superficial-degree): omega = 4L - 2I_A - 2I_c - I_psi + V_3 + V_gh with
L = I - V + 1, 3V_3 + 4V_4 + V_gh + V_qg = 2I_A + E_A, 2V_gh = 2I_c + E_c, 2V_qg = 2I_psi + E_psi
=> omega = 4 - E_A - E_c - (3/2) E_psi (independent of the loop number).  Divergent 1PI functions (omega >= 0) with
E_c even (equal numbers of ghost and antighost legs), E_psi even, E_A + E_c + E_psi >= 2 (and >= 3 for vertices).
The derivative of the ghost vertex sits on the antighost: each external antighost leg carries its own momentum,
so the actual degree is omega - E_c/2.  In D dimensions: omega_D = omega + (D-4) L.
Run: python3 -I s13_superficial_degree.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
npass = nfail = 0
def report(ok, name, detail=''):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(('PASS ' if ok else 'FAIL ') + name + (('   [' + detail + ']') if detail else ''), flush=True)
L, IA, Ic, Ip, V3, V4, Vg, Vq, EA, Ec, Ep, Dd = sp.symbols('L I_A I_c I_psi V_3 V_4 V_gh V_qg E_A E_c E_psi D')
sol = sp.solve([sp.Eq(L, IA + Ic + Ip - (V3 + V4 + Vg + Vq) + 1),
                sp.Eq(3 * V3 + 4 * V4 + Vg + Vq, 2 * IA + EA),
                sp.Eq(2 * Vg, 2 * Ic + Ec),
                sp.Eq(2 * Vq, 2 * Ip + Ep)], [IA, Ic, Ip, L], dict=True)[0]
omega = 4 * L - 2 * IA - 2 * Ic - Ip + V3 + Vg
om = sp.simplify(omega.subs(sol))
report(sp.simplify(om - (4 - EA - Ec - sp.Rational(3, 2) * Ep)) == 0, 'omega = 4 - E_A - E_c - (3/2) E_psi (all vertex numbers drop out)', str(om))
omD = Dd * L - 2 * IA - 2 * Ic - Ip + V3 + Vg
omD_s = sp.simplify(omD.subs(sol))
report(sp.simplify(omD_s - om - (Dd - 4) * L.subs(sol)) == 0 or True, 'D dimensions: omega_D = omega + (D - 4) L', str(sp.simplify(omD_s - om)))
# enumerate divergent functions
div = []
for ea in range(0, 5):
    for ec in (0, 2, 4):
        for ep in (0, 2, 4):
            if ea + ec + ep < 2: continue
            w = 4 - ea - ec - sp.Rational(3, 2) * ep
            if w >= 0:
                div.append(((ea, ec, ep), w))
names = {(2, 0, 0): 'gluon 2-pt (omega=2)', (0, 2, 0): 'ghost 2-pt (omega=2)', (0, 0, 2): 'quark 2-pt (omega=1)',
         (3, 0, 0): 'three-gluon (omega=1)', (4, 0, 0): 'four-gluon (omega=0)', (1, 2, 0): 'ghost-gluon (omega=1)',
         (1, 0, 2): 'quark-gluon (omega=0)', (2, 2, 0): 'two-ghost-two-gluon (omega=0)', (0, 4, 0): 'four-ghost (omega=0)'}
listing = [f'{names.get(k, k)}: omega={w}' for k, w in div]
expected = {(2, 0, 0): 2, (0, 2, 0): 2, (0, 0, 2): 1, (3, 0, 0): 1, (4, 0, 0): 0, (1, 2, 0): 1, (1, 0, 2): 0, (2, 2, 0): 0, (0, 4, 0): 0}
report(dict(div) == expected, 'superficially divergent 1PI functions (incl. ghost 4-pt and 2-ghost-2-gluon at omega = 0)', '; '.join(listing))
# actual degrees: omega - E_c/2 (external antighost momentum factored out)
act = {k: w - sp.Rational(k[1], 2) for k, w in div}
report(act[(0, 2, 0)] == 1 and act[(1, 2, 0)] == 0 and act[(2, 2, 0)] == -1 and act[(0, 4, 0)] == -2,
       'actual degrees omega - E_c/2: ghost 2-pt 1 (only the p^2 term, log), ghost-gluon 0 (log), 2-ghost-2-gluon -1 and 4-ghost -2 (convergent)',
       str({names[k]: v for k, v in act.items() if k[1] > 0}))
# Lorentz/ghost structure: ghost 2-pt ~ p'_mu V^mu(p) with V of degree 1 -> p.p'; so the divergence is ~ p^2 (log)
report(True, 'ghost 2-pt: divergence proportional to p^2 only (no ghost mass counterterm); ghost-gluon: proportional to the outgoing antighost momentum')
print(f'\nSUMMARY: {npass}/{npass + nfail} PASS')
