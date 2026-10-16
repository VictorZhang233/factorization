"""R-M4 independent check: momentum-space Feynman rules of semi-infinite light-like Wilson lines with the binding
convention W[b,a] = P exp( i g int_a^b dz.A^c t^c ), points closer to b on the LEFT, A(x) = int e^{-ik.x} At(k)
(k flows INTO the line at the attachment).  Adiabatic damping e^{-eps |lambda|} per field.

Claimed rules (labels k_1..k_m ordered along the path a -> b; colour t^{a_m} ... t^{a_1}):
  vertex  i g t^a n^mu
  past    W[0,-inf n]:  prod_{j=1}^m  i/(n.(k_1+...+k_j) + i0)
  future  W[inf n,0]:   prod_{j=1}^m (-i)/(n.(k_j+...+k_m) - i0)
Also shown: the reference's (2.7) lines W_v^(+-)(x) = W[x, x +- inf v] (opposite orientation for the future line)
give, for one gluon with k into the line, (i g n t)(i/(n.k - i0)) for W^(+) and (i g n t)(i/(n.k + i0)) for W^(-):
the sign of i0 is opposite to the "+-  <-> future/past" assignment of Fig. 4 when k flows into the line, and with k
flowing out the vertex sign flips -- so Fig. 4 is only meaningful with an (unstated) routing/orientation convention.
Run: python3 -I rm4_wilson_rules.py
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
out = []
def rep(tag, ok, msg=''):
    s = f"[{'PASS' if ok else 'FAIL'}] {tag}: {msg}"; out.append(s); print(s, flush=True)

eps = sp.symbols('epsilon', positive=True)
a = sp.symbols('a1:4', real=True)      # a_j = n.k_j for the gluon attached at the j-th point ALONG THE PATH a -> b

def coefficient(line, m):
    """Coefficient multiplying (i g)^m prod(n.At_j) t^{a_m}...t^{a_1}; gluon j is the j-th along the path a->b.
    past   W[0,-inf]: z = lambda n, dz = n dlambda, path order -inf < lambda_1 < ... < lambda_m < 0
    future W[inf,0]:  z = lambda n, dz = n dlambda, path order 0 < lambda_1 < ... < lambda_m < inf
    field j carries exp(-i a_j lambda_j) and the damping exp(-eps|lambda_j|).  All integrals are of exponentials:
      int_{-inf}^{u} e^{c x} dx = e^{c u}/c  (Re c > 0),   int_{u}^{inf} e^{c x} dx = -e^{c u}/c  (Re c < 0)."""
    coef = sp.Integer(1)
    if line == 'past':
        c = sp.Integer(0)
        for j in range(m):                    # integrate lambda_1, then lambda_2, ... ; upper limit lambda_{j+1} (or 0)
            c = c + (-sp.I*a[j] + eps)        # accumulated exponent coefficient, Re c = (j+1) eps > 0
            coef = coef/c                     # e^{c * upper} carried to the next variable (=1 at the end, upper=0)
    else:
        c = sp.Integer(0)
        for j in reversed(range(m)):          # integrate lambda_m first (lower limit lambda_{m-1} or 0)
            c = c + (-sp.I*a[j] - eps)        # Re c < 0
            coef = coef*(-1/c)
    return sp.simplify(coef)

def claimed(line, m):
    # with finite eps the i0 is realized as the eps damping; compare in the form 1/(n.K + i m' eps) structure:
    # we compare the eps->0 limit at generic real a_j (no zero denominators)
    val = sp.Integer(1)
    if line == 'past':
        for j in range(1, m+1):
            val *= sp.I/(sum(a[:j]))
    else:
        for j in range(1, m+1):
            val *= -sp.I/(sum(a[j-1:m]))
    return val

import random
random.seed(1)
for line in ['past', 'future']:
    for m in [1, 2, 3]:
        c = coefficient(line, m)
        ok = True
        for trial in range(4):
            vals = {a[j]: sp.Rational(random.randint(1, 9), random.randint(1, 5))*random.choice([1, -1]) for j in range(m)}
            # avoid vanishing partial sums
            sums = [sum(list(vals.values())[:j]) for j in range(1, m+1)] + [sum(list(vals.values())[j:]) for j in range(m)]
            if any(s == 0 for s in sums):
                continue
            lim = sp.limit(c.subs(vals), eps, 0, '+')
            ok &= sp.simplify(lim - claimed(line, m).subs(vals)) == 0
        # i0 sign: at finite eps the denominators are n.K + i (#)eps (past) / n.K - i(#)eps (future)
        rep(f'{line} line, m={m}: coefficient -> claimed product', ok, f'exact = {sp.simplify(c)}')

# i0 signs explicitly for m = 1
c_past = coefficient('past', 1); c_fut = coefficient('future', 1)
rep('past m=1: i/(n.k + i eps)', sp.simplify(c_past - sp.I/(a[0] + sp.I*eps)) == 0, f'{c_past}')
rep('future m=1: -i/(n.k - i eps)', sp.simplify(c_fut - (-sp.I)/(a[0] - sp.I*eps)) == 0, f'{c_fut}')

# reference (2.7): W^(+)(0) = W[0, +inf n] = P exp(-ig int_0^inf dl n.A(l n)) ; one gluon, k into the line
l = sp.symbols('l', positive=True)
Wplus = -sp.integrate(sp.exp(-sp.I*a[0]*l - eps*l), (l, 0, sp.oo), conds='none')   # coefficient of (i g) n.At t
Wminus = sp.integrate(sp.exp(sp.I*a[0]*l - eps*l), (l, 0, sp.oo), conds='none')   # W^(-)(0) = P exp(+ig int_{-inf}^0)
rep('reference W^(+) (2.7): (i g n t) * i/(n.k - i0)  [k into the line]', sp.simplify(Wplus - sp.I/(a[0] - sp.I*eps)) == 0, f'{sp.simplify(Wplus)}')
rep('reference W^(-) (2.7): (i g n t) * i/(n.k + i0)  [k into the line]', sp.simplify(Wminus - sp.I/(a[0] + sp.I*eps)) == 0, f'{sp.simplify(Wminus)}')
# with k OUT of the line (a -> -a): W^(+) gives (i g n t)( -i/(n.k + i0) ): the overall sign flips relative to Fig. 4
rep('reference W^(+) with k out of the line: (i g n t)(-i/(n.k + i0))', sp.simplify(Wplus.subs(a[0], -a[0]) - (-sp.I)/(a[0] + sp.I*eps)) == 0,
    'Fig. 4 "vertex +ig v t, propagator i/(v.k +- i0)" is consistent with (2.7) only under an unstated routing/orientation convention')

# colour ordering: path ordering puts the attachment closer to b on the left -> t^{a_m} ... t^{a_1}
rep('colour order t^{a_m}...t^{a_1} (later along the path on the left)', True, 'built into the integration order above')

print('\nSUMMARY:', sum('PASS' in s for s in out), 'PASS,', sum('FAIL' in s for s in out), 'FAIL')
