# evaluate the exact sympy differences at sample points (branch artifacts of sympy removed by numerics)
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
x, y = sp.symbols('x y', positive=True)
for q in [x*(1-x)**3, x**2*(1-x)**2, (1-x)**4, x**3*(1-x)]:
    for name, k, mult in (('par', y + (1-y)*sp.log(1-y), 1), ('perp', y + (1-y)*sp.log(1-y) + y*(1-y), 2)):
        F = sp.integrate(sp.expand(k*q.subs(x, x/y)/y), (y, x, 1))
        lhs = x**2*sp.diff(F, x, 2)
        lhs = lhs.replace(sp.exp_polar, sp.exp)
        lhs = lhs.replace(lambda e: isinstance(e, sp.polylog) and e.args[0] == 1, lambda e: -sp.log(1 - e.args[1]))
        qp = sp.diff(q, x)
        if name == 'par':
            core_int = (y*q.subs(x, x/y) - q)/(1-y)
        else:
            core_int = (y*(2*y-1)*q.subs(x, x/y) - q)/(1-y)
        vals = []
        for xv in [sp.Rational(3,10), sp.Rational(6,10)]:
            L = complex(sp.N(lhs.subs(x, xv), 25))
            core = sp.Integral(core_int.subs(x, xv), (y, xv, 1)).evalf(25)
            qv, qpv = q.subs(x, xv), qp.subs(x, xv)
            corr = float(core + qv*sp.log(1-xv) + mult*qv - xv*qpv)
            prin = float(core + mult*qv - xv*qpv)
            vals.append((float(xv), L, corr, prin, float(qv*sp.log(1-xv))))
        for (xv, L, corr, prin, qlog) in vals:
            print("q=%-18s %-4s x=%.1f  x^2F''=%.15g%+.1ei  [0,1]-plus=%.15g  eq64=%.15g  (x^2F''-eq64)=%.15g  q ln(1-x)=%.15g" % (
                str(q), name, xv, L.real, L.imag, corr, prin, L.real - prin, qlog))
