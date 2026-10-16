# Generic exact iterated-residue engine for  Int dk1 dk2/(2pi)^2  coef / prod_j (a_j k1 + b_j k2 + c_j)
# over the real k1,k2 axes (each factor has its own complex constant; generic positions assumed).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp

def int1d(coef, facs):
    """Int dk/(2pi) coef/prod (a_j k + c_j) over real k; facs: list of (a, c). Close upward."""
    var = [(a, c) for (a, c) in facs if a != 0]
    const = mp.mpc(1)
    for (a, c) in facs:
        if a == 0: const *= c
    if len(var) < 2: raise ValueError('not convergent: %d k-dependent factors' % len(var))
    tot = mp.mpc(0)
    for j, (aj, cj) in enumerate(var):
        p = -cj/aj
        if mp.im(p) > 0:
            r = coef/aj
            for l, (al, cl) in enumerate(var):
                if l != j: r /= (al*p + cl)
            tot += r
    return 1j*tot/const      # 2 pi i /(2pi) * sum res

def int2d(coef, facs):
    """facs: list of (a, b, c) for a*k1 + b*k2 + c. inner k2 then outer k1."""
    var2 = [f for f in facs if f[1] != 0]
    if len(var2) < 2: raise ValueError('inner not convergent')
    terms = []
    for j, (aj, bj, cj) in enumerate(var2):
        # pole k2 = -(aj k1 + cj)/bj ; side must be k1-independent: need Im(aj/bj) == 0
        if abs(mp.im(aj/bj)) > 1e-40: raise ValueError('pole side depends on k1')
        if mp.im(-cj/bj) > 0:
            newfacs = []
            for l, (al, bl, cl) in enumerate(facs):
                if (al, bl, cl) == (aj, bj, cj) and l == facs.index((aj, bj, cj)):
                    continue
                newfacs.append((al - bl*aj/bj, cl - bl*cj/bj))
            terms.append((coef/bj*1j, newfacs))
    return sum(int1d(c, f) for (c, f) in terms)
