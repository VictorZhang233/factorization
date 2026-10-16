# N16 (stage 2), supplement: structure of Collins 2007 eq. (11) (same side of the cut) from the common factor.
# After l1^+ = l2^+ = 0, with v = l1 + l2 and u = l1^-:
#  (i) sum over the two spectator orderings: int du [1/(P u + c1 + i0) + 1/(P (v^- - u) + c2 + i0)] = -2 pi i / P
#      (independent of c1, c2, v^-);
#  (ii) the remaining v^- integral of 1/(D_s(v) D_q(v)) is the opposite-side integral: 2 pi i/(2 p+ A_v),
#      A_v = (kT - vT)^2 + mq^2;
#  (iii) conjugate tree propagator k^2 - mq^2 = -(kT^2 + mq^2)/(1-x) on the spectator cut;
#  => |same-side common factor| = (2pi)^2 (1-x)^2 /(A_v (kT^2+mq^2)), the opposite-side one = (2pi)^2 (1-x)^2/(A_1 A_2):
#     same prefactor N, structure G(kT)/(kT^2+mq^2) of eq. (11).  (The overall sign, minus in (11), is then fixed by
#     C07's stated cancellation int d^2kT (I1+I2) = 0, verified in n16_collins.py with this normalisation.)
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import sympy as sp
npass = 0; nfail = 0
def check(name, ok, info=""):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(("PASS " if ok else "FAIL ") + name + ("  " + info if info else ""), flush=True)
mp.mp.dps = 30
P = mp.mpf('1.4')
for (c1, c2, v) in [(mp.mpf('0.3'), mp.mpf('-0.7'), mp.mpf('0.25')), (mp.mpf('-1.1'), mp.mpf('2.0'), mp.mpf('-0.6'))]:
    for eps in [mp.mpf('1e-3'), mp.mpf('1e-5')]:
        # analytic antiderivative with finite eps and symmetric cutoff Lam -> the Lam -> inf limit
        def S(Lam):
            t1 = (mp.log(P*Lam + c1 + 1j*eps) - mp.log(-P*Lam + c1 + 1j*eps))/P
            t2 = (-mp.log(P*(v - Lam) + c2 + 1j*eps) + mp.log(P*(v + Lam) + c2 + 1j*eps))/P
            return t1 + t2
        val = S(mp.mpf(10)**12)
        # direct numerical quadrature on a large interval as a cross-check
        f = lambda u: 1/(P*u + c1 + 1j*eps) + 1/(P*(v - u) + c2 + 1j*eps)
        pts = sorted([-mp.mpf(10)**6, -c1/P, v + c2/P, mp.mpf(10)**6])
        num = mp.quad(f, [pts[0], -100, pts[1], pts[2], 100, pts[3]])
        check("ordering sum = -2 pi i/P (c1=%s, c2=%s, v=%s, eps=%s)" % (mp.nstr(c1,2), mp.nstr(c2,2), mp.nstr(v,2), mp.nstr(eps,1)),
              abs(val + 2j*mp.pi/P) < 1e-9 and abs(num + 2j*mp.pi/P) < 1e-5, "analytic %s, numeric %s" % (mp.nstr(val, 10), mp.nstr(num, 10)))
# magnitude bookkeeping (symbolic)
x, pp, Av, A1, A2, K = sp.symbols('x p_plus A_v A_1 A_2 K', positive=True)   # K = kT^2+mq^2
Pv = 2*(1-x)*pp
same = (2*sp.pi/Pv)*(2*sp.pi/(2*pp*Av))*Pv**2*(1-x)/K
opp = (2*sp.pi/(2*pp*A1))*(2*sp.pi/(2*pp*A2))*Pv**2
check("|same-side| = (2pi)^2 (1-x)^2/(A_v K) and |opposite| = (2pi)^2 (1-x)^2/(A_1 A_2): equal prefactors",
      sp.simplify(same - (2*sp.pi)**2*(1-x)**2/(Av*K)) == 0 and sp.simplify(opp - (2*sp.pi)**2*(1-x)**2/(A1*A2)) == 0)
# on-shell spectator: k^- = -(kT^2+mq^2)/(2(1-x)p+)  =>  k^2 - mq^2 = 2 x p+ k^- - kT^2 - mq^2 = -(kT^2+mq^2)/(1-x)
km = -K/(2*(1-x)*pp)
check("conjugate tree propagator: k^2 - mq^2 = -(kT^2+mq^2)/(1-x)", sp.simplify(2*x*pp*km - K + K/(1-x)) == 0)
print("\nTOTAL: %d PASS, %d FAIL" % (npass, nfail))
