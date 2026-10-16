# Reviewer-2 independent derivation (X1 review).
# Localized A-side ordering weight for two insertions on ONE spectator, from the time-space form
#   J^[12](tau1,tau2) = Jcal * theta(tau2 - tau1)   (|tau| << 1/lambda_A)
#   => J^[12](k1,k2) = Jcal * 2 pi delta(k1+k2) * (-i)/(k2 - i0)
# with external factors f_e(k) = R_e(k) chi(k),  R_e = r_e/(k - z_e),  chi(k) = K^2/(k^2+K^2) (or chi = 1).
#   W12 = [ int dk/(2pi) (-i)/(k - i0) f_1(-k) f_2(k) ] / ( f_1(0) f_2(0) )
# Cases by half plane of z_e (F = final: Im z<0 ; B = initial: Im z>0).  Close in the LHP.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

k, z1, z2, K = sp.symbols('k z1 z2 K')
I = sp.I

def W12_expr(case, reg=True):
    chi = (lambda q: K**2/((q - I*K)*(q + I*K))) if reg else (lambda q: 1)
    f1 = lambda q: 1/(q - z1)*chi(q)
    f2 = lambda q: 1/(q - z2)*chi(q)
    g = (-I)/k * f1(-k) * f2(k)          # the pole k = +i0 is in the UHP: never picked when closing below
    lhp = []
    if case[0] == 'B': lhp.append(-z1)    # pole of f1(-k) at k = -z1 is in the LHP iff Im z1 > 0
    if case[1] == 'F': lhp.append(z2)     # pole of f2 at k = z2 in the LHP iff Im z2 < 0
    if reg: lhp.append(-I*K)              # double pole at k = -iK
    tot = 0
    for p in lhp:
        tot += sp.residue(g, k, p)
    num = -I*tot
    den = f1(0)*f2(0)
    return sp.simplify(sp.together(num/den))

if __name__ == '__main__':
    out = {}
    for case in ('FF', 'BB', 'BF', 'FB'):
        race = W12_expr(case, reg=False)
        regd = W12_expr(case, reg=True)
        out[case] = regd
        lim = sp.simplify(sp.limit(regd, K, sp.oo))
        print(case, ' race:', race, '   reg(K->oo) - race =', sp.simplify(lim - race))
        print('    reg:', regd)
        # |z| >> K limit: z -> t*z with t -> oo
        t = sp.symbols('t', positive=True)
        big = sp.simplify(sp.limit(regd.subs({z1: t*z1, z2: t*z2}), t, sp.oo))
        print('    |z|>>K limit:', big)
    # symmetry check: W12^BB(z) = 1 - W12^FF(-z)  (time reversal)
    print('time-reversal FF/BB:', sp.simplify(out['BB'] - (1 - out['FF'].subs({z1: -z1, z2: -z2}, simultaneous=True))))
    import pickle
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'regweights.pkl'), 'wb') as fh:
        pickle.dump({c: sp.srepr(e) for c, e in out.items()}, fh)
