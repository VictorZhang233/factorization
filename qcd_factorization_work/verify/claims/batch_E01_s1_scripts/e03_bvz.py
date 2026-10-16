import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import sympy as sp

mp.mp.dps = 40

# ---------- Mellin-space proof (exact) ----------
N = sp.symbols('N', positive=True, integer=True)
y = sp.symbols('y', positive=True)
def H(n):  # harmonic number
    return sp.harmonic(n)
# K_par(N) = int_0^1 y^{N-1} (y + (1-y) ln(1-y)) dy = 1/(N+1) - H_N/N + H_{N+1}/(N+1)
Kpar = 1/(N+1) - H(N)/N + H(N+1)/(N+1)
lhs = sp.simplify(sp.expand_func(N*(N+1)*Kpar))
# RHS Mellin of {int_x^1 dy/y y^2/[1-y]_+^{[0,1]} q(x/y) + q - x q'}  =  -H_{N+1} + 1 + N
rhs = -H(N+1) + 1 + N
print("Mellin check (parallel), N=1..8:", [sp.nsimplify(sp.simplify((lhs - rhs).subs(N, n))) for n in range(1, 9)])
Kperp = Kpar + 1/(N+1) - 1/(N+2)
rhs_perp = -H(N+1) - 2/(N+2) + 2 + N
print("Mellin check (perp), N=1..8:", [sp.nsimplify(sp.simplify((N*(N+1)*Kperp - rhs_perp).subs(N, n))) for n in range(1, 9)])
# the printed (64) braces correspond to G(N) without the q ln(1-x) term; Mellin of q(x) ln(1-x) is not of
# convolution form, so (64) cannot equal x^2 F'' for all q.

# ---------- direct x-space check ----------
def make_q(a, b):
    q = lambda x: x**a * (1 - x)**b
    dq = lambda x: a*x**(a-1)*(1-x)**b - b*x**a*(1-x)**(b-1)
    return q, dq

def F(x, q, kern):
    # F(x) = int_x^1 dy/y k(y) q(x/y)
    return mp.quad(lambda yy: kern(yy)/yy*q(x/yy), [x, (1+x)/2, 1])

kpar = lambda yy: yy + (1-yy)*mp.log(1-yy) if yy < 1 else mp.mpf(1)
kperp = lambda yy: kpar(yy) + yy*(1-yy)

def braces(x, q, dq, perp=False, with_log=True):
    if not perp:
        I = mp.quad(lambda yy: (yy*q(x/yy) - q(x))/(1-yy), [x, (1+x)/2, 1])
        extra = q(x) - x*dq(x)
    else:
        I = mp.quad(lambda yy: (yy*(2*yy-1)*q(x/yy) - q(x))/(1-yy), [x, (1+x)/2, 1])
        extra = 2*q(x) - x*dq(x)
    return I + extra + (q(x)*mp.log(1-x) if with_log else 0)

print()
print("x^2 F''(x) (numerical) vs braces with [0,1]-plus (incl. q ln(1-x)) vs printed eq.(64) braces (no log)")
for (a, b) in [(-0.5, 3), (-0.3, 3.5), (0.5, 3), (-0.5, 2)]:
    q, dq = make_q(mp.mpf(a), mp.mpf(b))
    for x in [mp.mpf('0.2'), mp.mpf('0.5'), mp.mpf('0.8')]:
        for perp in (False, True):
            kern = kperp if perp else kpar
            x2F2 = x**2*mp.diff(lambda t: F(t, q, kern), x, 2)
            A = braces(x, q, dq, perp, True)
            B = braces(x, q, dq, perp, False)
            Rc = (1-x)*A/q(x); Rp = (1-x)*B/q(x)
            print(f"a={a:5}, b={b:4}, x={float(x):.1f}, {'perp' if perp else 'par '}: x2F''={mp.nstr(x2F2,12)}  A={mp.nstr(A,12)}  B={mp.nstr(B,12)}"
                  f"  |x2F''-A|={mp.nstr(abs(x2F2-A),3)}  R_correct={mp.nstr(Rc,6)} R_printed={mp.nstr(Rp,6)} rel.err={mp.nstr((Rp-Rc)/Rc*100,4)}%")

print()
print("endpoint behaviour: R_printed - R_correct = -(1-x) ln(1-x):")
for x in [0.9, 0.99, 0.999, 0.01, 0.001]:
    print(f"  x={x}: {-(1-x)*mp.log(1-x)}")
