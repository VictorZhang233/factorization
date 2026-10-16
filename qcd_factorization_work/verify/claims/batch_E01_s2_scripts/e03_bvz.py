# Stage-2 check of E03 (BVZ eqs. (61)-(64), PRD 99 (2019) 014013).
# (i) exact symbolic check for polynomial-type q (sympy, rational arithmetic):  x^2 F''(x) vs braces
# (ii) numerical check for BVZ model (60) q = x^{-1/2}(1-x)^3 by direct numerical differentiation (mpmath)
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
x, y, t = sp.symbols('x y t', positive=True)

def check_exact(q, label):
    # F_par(x) = int_x^1 dy/y (y + (1-y)ln(1-y)) q(x/y);   F_perp adds y(1-y)
    out = {}
    for name, k in (('par', y + (1-y)*sp.log(1-y)), ('perp', y + (1-y)*sp.log(1-y) + y*(1-y))):
        F = sp.integrate(sp.expand(k*q.subs(x, x/y)/y), (y, x, 1))
        lhs = sp.simplify(x**2*sp.diff(F, x, 2))
        qx, qp = q, sp.diff(q, x)
        # braces with the [0,1] plus distribution, rewritten over [x,1]: int_x^1 [y q(x/y) - q(x)]/(1-y) + q ln(1-x)
        if name == 'par':
            core = sp.integrate(sp.simplify((y*q.subs(x, x/y) - qx)/(1-y)), (y, x, 1))
            correct = core + qx*sp.log(1-x) + qx - x*qp
            printed = core + qx - x*qp                       # eq. (64), R_par * q / xbar
        else:
            core = sp.integrate(sp.simplify((y*(2*y-1)*q.subs(x, x/y) - qx)/(1-y)), (y, x, 1))
            correct = core + qx*sp.log(1-x) + 2*qx - x*qp
            printed = core + 2*qx - x*qp
        d1 = sp.simplify(lhs - correct)
        d2 = sp.simplify(lhs - printed)
        out[name] = (d1, d2)
        print("  %s %s: x^2F'' - braces([0,1]-plus) = %s ;  x^2F'' - braces(eq.64) = %s" % (label, name, d1, sp.factor(d2)))
    return out

print("(i) exact symbolic checks")
for q in [x*(1-x)**3, x**2*(1-x)**2, (1-x)**4, x**3*(1-x)]:
    check_exact(q, str(q))

print("(ii) BVZ model (60) q = x^{-1/2}(1-x)^3: direct numerical second derivative")
mp.mp.dps = 30
qf = lambda u: u**mp.mpf(-0.5)*(1-u)**3
def F(xx, perp=False):
    k = (lambda yy: yy + (1-yy)*mp.log(1-yy) + (yy*(1-yy) if perp else 0))
    return mp.quad(lambda yy: k(yy)*qf(xx/yy)/yy, [xx, 1])
def braces(xx, perp=False, printed=False):
    q0 = qf(xx); qp = mp.diff(qf, xx)
    if not perp:
        core = mp.quad(lambda yy: (yy*qf(xx/yy) - q0)/(1-yy), [xx, 1]); extra = q0 - xx*qp
    else:
        core = mp.quad(lambda yy: (yy*(2*yy-1)*qf(xx/yy) - q0)/(1-yy), [xx, 1]); extra = 2*q0 - xx*qp
    return core + extra + (0 if printed else q0*mp.log(1-xx))
for xx in [mp.mpf('0.2'), mp.mpf('0.5'), mp.mpf('0.8')]:
    for perp in (False, True):
        d2 = mp.diff(lambda u: F(u, perp), xx, 2)
        lhs = xx**2*d2
        bc = braces(xx, perp); bp = braces(xx, perp, printed=True)
        Rc = (1-xx)/qf(xx)*bc; Rp = (1-xx)/qf(xx)*bp
        print("  x=%s %s: x^2F''=%s  [0,1]-plus braces=%s  eq.(64) braces=%s | R_correct=%s R_printed=%s (+%s%%)  R_p-R_c=%s  -xbar ln xbar=%s" % (
            mp.nstr(xx,2), 'perp' if perp else 'par ', mp.nstr(lhs, 12), mp.nstr(bc, 12), mp.nstr(bp, 12),
            mp.nstr(Rc, 6), mp.nstr(Rp, 6), mp.nstr(100*(Rp-Rc)/Rc, 4), mp.nstr(Rp-Rc, 8), mp.nstr(-(1-xx)*mp.log(1-xx), 8)))
