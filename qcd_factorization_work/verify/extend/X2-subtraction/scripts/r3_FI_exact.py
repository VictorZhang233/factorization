"""X2 final revision / r3_FI_exact.py -- exact proofs (symbolic steps + numerical confirmation) of the identification
(FI) of fibered and covariant values for Gamma of the one-loop triangle (M1) and of the one-rung DIS ladder (M2)
(closes open item O15 of round 2; removes the premise (FI)_Gamma from the integrated corollary of Thm B.4).

TRIANGLE (units Qt = 1, tau = m2/Qt^2 = m2, Q^2 = (1+tau)^2; covariant value I = Gamma(1+eps) int_simplex F^{-1-eps},
F = x_g m2 (x1 + x2) + x1 x2 Q^2; light-cone variable u = k+/P = x1 - tau x2 (alpha-representation)):
  main part 0 < k+ < P:  kappa-integral with a Feynman parameter y gives
      fib_main = Gamma(1+eps)/(1+tau) int_0^1 du int_0^1 dy (1-u)^{-eps} [m2(1-y+yu) + (1-y) u]^{-1-eps};
      on {x1 > tau x2}: x2 = (1-u) z/(1+tau), x1 = u + tau x2, Jacobian (1-u)/(1+tau), and
      F = (1-u)[m2 (u + (1-u) z) + z u]   =>  with z = 1 - y the two integrands coincide.
  sliver -tau P < k+ < 0 (s = 1 + u/tau in (0,1)):  rho_Gamma = (2s/(2P(1+tau))) / ((kappa + m2 s(1-s))(kappa + m2 s(1+tau(1-s)))),
      fib_sliver = Gamma(1+eps) tau/(1+tau) m2^{-1-eps} int ds dy s^{-eps} [1 - y s + tau (1-y)(1-s)]^{-1-eps};
      on {x1 < tau x2}: x1 = tau s v/(1+tau), x2 = 1 - s + s v/(1+tau), Jacobian tau s/(1+tau), and
      F = tau s [1 - s(1-v) + tau v (1-s)]   =>  with y = 1 - v the two integrands coincide.
  Hence fibered value of Gamma = covariant value, for every eps in (-1, 1), exactly.
ONE-RUNG LADDER (d = 6 - 2eps, Q = 1, c = 1 - 1/x): transverse Euclidean integral (D = 4 - 2eps) + Feynman parameter y:
      fib = Gamma(1+eps) int_0^1 dxi (1-xi)^{1-eps} int_0^1 dy y [y xi m2 + (1-y) xi (c + m2) + y(1-y)(1-xi)]^{-1-eps};
      covariant: Gamma(1+eps) int_simplex x1 [x2 (x1 + x3) m2 + x3 (x1 + x2 c)]^{-1-eps}; x2 = xi, x1 = (1-xi) y,
      x3 = (1-xi)(1-y) (Jacobian 1-xi) maps one onto the other exactly."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

print("(1) symbolic identities")
u, z, s, v, t, m2, y, xi, c = sp.symbols('u z s v tau m2 y xi c', positive=True)
Q2 = (1 + t)**2
def F(xg, x1, x2, mm=t): return xg*mm*(x1 + x2) + x1*x2*Q2
x2m = (1 - u)*z/(1 + t); x1m = u + t*x2m
Fm = sp.factor(sp.expand(F(1 - x1m - x2m, x1m, x2m)))
Jm = sp.simplify(sp.Matrix([[sp.diff(x1m, u), sp.diff(x1m, z)], [sp.diff(x2m, u), sp.diff(x2m, z)]]).det())
print("   main:   F =", Fm, "   target (1-u)[m2(u+(1-u)z)+z u] (m2=tau):",
      sp.simplify(Fm - (1 - u)*(t*(u + (1 - u)*z) + z*u)) == 0, "   Jacobian =", Jm)
x1s = t*s*v/(1 + t); x2s = 1 - s + s*v/(1 + t)
Fs = sp.factor(sp.expand(F(1 - x1s - x2s, x1s, x2s)))
Js = sp.simplify(sp.Matrix([[sp.diff(x1s, s), sp.diff(x1s, v)], [sp.diff(x2s, s), sp.diff(x2s, v)]]).det())
print("   sliver: F =", Fs, "   target tau s[1-s(1-v)+tau v(1-s)]:",
      sp.simplify(Fs - t*s*(1 - s*(1 - v) + t*v*(1 - s))) == 0, "   Jacobian =", Js)
print("   region checks: u = x1 - tau x2 on the main map:", sp.simplify(x1m - t*x2m - u) == 0,
      ";  s = 1 - x2 + x1/tau on the sliver map:", sp.simplify(1 - x2s + x1s/t - s) == 0,
      ";  x_g = (1-u)(1-z) and s(1-v):", sp.simplify(1 - x1m - x2m - (1 - u)*(1 - z)) == 0, sp.simplify(1 - x1s - x2s - s*(1 - v)) == 0)
# sliver density in (s, kappa) from the round-2 closed form (P = P' general, a = m2/P', w = a s, c' = a - w)
P, Pp, kap = sp.symbols('P Pp kappa', positive=True)
a = m2/Pp; w = a*s; cc = a - w
Dg_w = cc*Pp*w + a*kap
D1_num = (m2*(1 + cc/(2*P)) + kap)*w + 2*(Pp*w + kap)*(P + cc/2)
rho_sl = 2*w/(Dg_w*D1_num)
tau_ = m2/(2*P*Pp)
target = (2*s/(2*P*(1 + tau_)))/((kap + m2*s*(1 - s))*(kap + m2*s*(1 + tau_*(1 - s))))
print("   sliver density = (2s/(2P(1+tau)))/((kappa+m2 s(1-s))(kappa+m2 s(1+tau(1-s)))):", sp.simplify(rho_sl - target) == 0)
# main density (Prop B.1) in (u, kappa), Qt = 2 P P' general
uu = sp.Symbol('u', positive=True); Qt2 = 2*P*Pp; x = P*uu
A = x*m2*(1 - uu) + P*kap; e2 = m2 + 2*Pp*x
rho_m = 1/(A*(e2*(1 + m2/Qt2 + kap/(Qt2*(1 - uu))) + kap))
tg = (1 - uu)/(P*(1 + tau_)*(kap + uu*(1 - uu)*m2)*(kap + (1 - uu)*(m2 + Qt2*uu)))
print("   main density = (1-u)/(P(1+tau)(kappa+u(1-u)m2)(kappa+(1-u)(m2+Qt^2 u))):", sp.simplify(rho_m - tg) == 0)
# ladder
Fl = lambda x1, x2, x3: x2*(x1 + x3)*m2 + x3*(x1 + x2*c)
X1 = (1 - xi)*y; X2 = xi; X3 = (1 - xi)*(1 - y)
br = y*xi*m2 + (1 - y)*xi*(c + m2) + y*(1 - y)*(1 - xi)
print("   ladder: F(x(xi,y)) = (1-xi) * bracket:", sp.simplify(Fl(X1, X2, X3) - (1 - xi)*br) == 0)

print("\n(2) numerical confirmation (direct 2D quadratures of the fibered densities and of the simplex sub-regions)")
mp.mp.dps = 25
def tri_check(m2v, eps, P_=mp.mpf('0.8'), Pp_=mp.mpf('1.3')):
    """covariant integral over the simplex sub-regions {x1 > tau x2}, {x1 < tau x2} (breakpoints at both soft corners,
    x2 -> 0 and x2 -> 1, are needed: the integrand is singular there) versus the fibered main part in (u,z)-form and the
    fibered sliver in (s,y)-form (each obtained from Prop B.1 by the exact kappa-integration of step 1/3)."""
    Qt2v = 2*P_*Pp_; tv = m2v/Qt2v; Q2v = (Qt2v + m2v)**2/Qt2v; g = mp.gamma(1 + eps)
    Fv = lambda xg, a1, a2: xg*m2v*(a1 + a2) + a1*a2*Q2v
    ks = [mp.mpf(10)**k for k in range(-12, 0)]
    outer = sorted(set([mp.mpf(0)] + ks + [mp.mpf('0.5')] + [1 - k for k in ks] + [mp.mpf(1)]))
    def inner(a2, lo, hi):
        if hi <= lo: return mp.mpf(0)
        pts = sorted(set([lo, hi] + [lo + k*(hi - lo) for k in ks] + [hi - k*(hi - lo) for k in ks]))
        return mp.quad(lambda a1: Fv(1 - a1 - a2, a1, a2)**(-1 - eps), pts)
    cm = g*mp.quad(lambda a2: inner(a2, min(tv*a2, 1 - a2), 1 - a2), outer)
    cs = g*mp.quad(lambda a2: inner(a2, mp.mpf(0), min(tv*a2, 1 - a2)), outer)
    fm = g/(1 + tv)*mp.quad(lambda uu: (1 - uu)**(-eps)*mp.quad(lambda zz: (m2v*(uu + (1 - uu)*zz) + zz*uu*Qt2v)**(-1 - eps), [0, 1]),
                            [0] + ks + [mp.mpf('0.5')] + [1 - k for k in ks] + [1])
    fs = g*tv/(1 + tv)*m2v**(-1 - eps)*mp.quad(lambda ss: ss**(-eps)*mp.quad(lambda yy: (1 - yy*ss + tv*(1 - yy)*(1 - ss))**(-1 - eps), [0, 1]),
                                               [0] + ks + [1])
    return fm, cm, fs, cs
for (m2v, ev) in [(mp.mpf('0.1'), mp.mpf('0.3')), (mp.mpf('0.02'), mp.mpf('0.05'))]:
    fm, cm, fs, cs = tri_check(m2v, ev)
    print(f"   triangle P=0.8 P'=1.3 m2={m2v}, eps={ev}: main fib {mp.nstr(fm, 16)} cov {mp.nstr(cm, 16)} rel {mp.nstr(abs(fm/cm - 1), 3)};"
          f" sliver fib {mp.nstr(fs, 16)} cov {mp.nstr(cs, 16)} rel {mp.nstr(abs(fs/cs - 1), 3)}; total fib {mp.nstr(fm + fs, 16)} cov {mp.nstr(cm + cs, 16)}", flush=True)
def lad_check(m2v, eps, xB=mp.mpf(2)):
    cv = 1 - 1/xB; g = mp.gamma(1 + eps)
    cov = g*mp.quad(lambda a2: mp.quad(lambda a1: a1*(a2*(1 - a2)*m2v + (1 - a1 - a2)*(a1 + a2*cv))**(-1 - eps), [0, 1 - a2]), [0, mp.mpf(1)/2, 1])
    # fibered: (1/Gamma(2-eps)) int dxi/(1-xi) int dt t^{1-eps} <h1>/v^2, rung on shell, S^{3-2eps} average
    def inner(x_):
        A = 1 - x_/xB
        def f(lt):
            tt = mp.e**lt; vv = x_*m2v + tt/(1 - x_)
            aa = A + vv; b2 = 4*tt; r = mp.sqrt(aa**2 - b2)
            hav = 2/(aa + r)*mp.hyp2f1(1, eps, 2 - eps, (aa - r)/(aa + r))
            return tt**(2 - eps)*hav/vv**2
        return mp.quad(f, [-mp.inf, mp.log(x_*m2v*(1 - x_)) - 4, mp.log(x_*m2v*(1 - x_)) + 4, 4, mp.inf])/(1 - x_)
    fib = mp.quad(inner, [0, mp.mpf(1)/2, 1])/mp.gamma(2 - eps)
    return fib, cov
for (m2v, ev) in [(mp.mpf('0.01'), mp.mpf('0.1')), (mp.mpf('0.05'), mp.mpf('0.25'))]:
    fb, cv_ = lad_check(m2v, ev)
    print(f"   ladder m2={m2v}, eps={ev}: fibered {mp.nstr(fb, 18)}  covariant {mp.nstr(cv_, 18)}  rel.dev {mp.nstr(abs(fb/cv_ - 1), 3)}", flush=True)
