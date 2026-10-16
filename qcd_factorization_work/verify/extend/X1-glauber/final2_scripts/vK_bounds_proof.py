# X1 final2 (Fix 5): PROOF (computer-algebra certificate) of the two inequalities used in T3(e), step (3),
#   |v_K| <= 1/2   and   |v_K| <= (|x_1|+|x_2|)/4,
# for the regulated localized weight v_K = w_K^[12] - 1/2 on the theta = pi/4 contour, and of the remainder bound
#   |v_K - (x_1-x_2)/4| <= s^3 (1+s/4)(3/2+s/4) / (4(1+sqrt2 s)),   s = |x_1|+|x_2|.
# Setting (L1' with the even Lorentzian regulator chi_K(k) = K^2/(k^2+K^2) on both lines):
#   line e has poles z_e (final iff Im z_e < 0), +iK (initial), -iK (final), normalized weights
#   u_z = K^2/(z^2+K^2), u_+ = z/(2(z-iK)), u_- = z/(2(z+iK));  x_e := iK/z_e  =>  u_z = x^2/(x^2-1),
#   u_+ = 1/(2(1-x)), u_- = 1/(2(1+x));  a pole p = iK/y enters the race weight through y (y = x, 1, -1).
#   Race weights of colour order [12]: both final y2/(y1+y2); both initial y1/(y1+y2); (1 init, 2 fin) 1; (1 fin, 2 init) 0.
# On the pi/4 contour k_e^+ = e^{i pi/4} s_e: z_e initial (s_e<0) <=> x_e = t_e w, final (s_e>0) <=> x_e = -t_e w,
#   w = e^{-i pi/4}, t_e = |x_e| = 2K|s_e|/a_e.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp

out = []
def log(s=''):
    print(s, flush=True); out.append(s)

x1, x2 = sp.symbols('x1 x2')
t1, t2 = sp.symbols('t1 t2', nonnegative=True)
one = sp.Integer(1)
def u(y, x):
    return {'z': x**2/(x**2 - 1), 1: one/(2*(1 - x)), -1: one/(2*(1 + x))}[y]
def W(y1, f1, y2, f2):
    if f1 and f2: return y2/(y1 + y2)
    if (not f1) and (not f2): return y1/(y1 + y2)
    if (not f1) and f2: return one
    return sp.Integer(0)
v = {}
for c1 in ('I', 'F'):
    for c2 in ('I', 'F'):
        tot = 0
        for y1 in ('z', 1, -1):
            for y2 in ('z', 1, -1):
                Y1 = x1 if y1 == 'z' else sp.Integer(y1); Y2 = x2 if y2 == 'z' else sp.Integer(y2)
                f1 = (c1 == 'F') if y1 == 'z' else (y1 == -1)
                f2 = (c2 == 'F') if y2 == 'z' else (y2 == -1)
                tot += u(y1, x1)*u(y2, x2)*W(Y1, f1, Y2, f2)
        v[(c1, c2)] = sp.simplify(tot - sp.Rational(1, 2))
ok = True
# sum of all pole weights equals 1 (normalization of the pole sum) -- check for one pattern
tot1 = sum(u(y1, x1)*u(y2, x2) for y1 in ('z', 1, -1) for y2 in ('z', 1, -1))
ok &= sp.simplify(tot1 - 1) == 0
D = x1 - x2 - x1*x2; S = x1 + x2 + x1*x2
cIF = (2*D**2 + (x1 - x2))/(4*(1 + D)**2)
cII = (x1 - x2)*(2*S**2 + (x1 + x2))/(4*(1 + S)**2*(x1 + x2))
c1_ = sp.simplify(v[('I', 'F')] - cIF) == 0; c2_ = sp.simplify(v[('I', 'I')] - cII) == 0
c3_ = sp.simplify(v[('F', 'I')] + v[('I', 'F')].subs({x1: -x1, x2: -x2}, simultaneous=True)) == 0
c4_ = sp.simplify(v[('F', 'F')] + v[('I', 'I')].subs({x1: -x1, x2: -x2}, simultaneous=True)) == 0
ok &= c1_ and c2_ and c3_ and c4_
log("(1) closed forms from the L1' pole sum:")
log("    v_IF = [2D^2 + (x1-x2)] / [4(1+D)^2],  D = x1 - x2 - x1 x2 = (1+x1)(1-x2) - 1 :  " + str(c1_))
log("    v_II = (x1-x2)[2S^2 + (x1+x2)] / [4(1+S)^2 (x1+x2)],  S = x1 + x2 + x1 x2 = (1+x1)(1+x2) - 1 :  " + str(c2_))
log("    v_FI(x1,x2) = -v_IF(-x1,-x2): " + str(c3_) + ";   v_FF(x1,x2) = -v_II(-x1,-x2): " + str(c4_))
w = sp.exp(-sp.I*sp.pi/4)
vIF = sp.simplify(cIF.subs({x1: t1*w, x2: -t2*w}, simultaneous=True))
vII = sp.simplify(cII.subs({x1: t1*w, x2: t2*w}, simultaneous=True))
c5_ = sp.simplify(vII - (t1 - t2)/(t1 + t2)*vIF) == 0
ok &= c5_
log("(2) on the rays: v_II(t1 w, t2 w) = [(t1-t2)/(t1+t2)] v_IF(t1 w, -t2 w): " + str(c5_))
# (3) |v_IF| <= 1/2 : |2D^2 + xi| <= 2|D|^2 + s and 2|1+D|^2 - (2|D|^2 + s) = 2 + 4 Re D - s, Re D = s/sqrt2
s_, p_ = sp.symbols('s p', nonnegative=True)
Dr = sp.expand(((t1 + t2)*w - sp.I*t1*t2))
DIF = sp.expand(D.subs({x1: t1*w, x2: -t2*w}, simultaneous=True))
c6_ = sp.simplify(sp.expand_complex(DIF - Dr)) == 0
ReD = sp.simplify(sp.re(sp.expand_complex(Dr)))
c7_ = sp.simplify(ReD - (t1 + t2)/sp.sqrt(2)) == 0
ok &= c6_ and c7_
log("(3) D = (t1+t2) w - i t1 t2 on the (I,F) rays: " + str(c6_) + ";  Re D = (t1+t2)/sqrt2: " + str(c7_))
log("    hence 2|1+D|^2 - (2|D|^2 + s) = 2 + (2 sqrt2 - 1) s > 0, so |v_IF| < 1/2; |v_II| <= |v_IF|; FI, FF by x -> -x.")
# (4) polynomial certificate for |v_IF| <= s/4
P = sp.expand((1 + t1*w)*(1 + t2*w))
N = sp.expand(sp.simplify(vIF*4*P**2/((t1 + t2)*w)))
P2 = sp.simplify(sp.expand_complex(sp.expand(P*sp.conjugate(P))))
N2 = sp.simplify(sp.expand_complex(sp.expand(N*sp.conjugate(N))))
F = sp.expand(sp.simplify((P2**2 - N2)*(t1 + t2)**2))
poly = sp.Poly(F, t1, t2)
coeffs = poly.coeffs()
nonneg = all(sp.N(c) >= 0 for c in coeffs)
ok &= nonneg
log("(4) v_IF = (s w/4) N/P^2 with P = (1 + t1 w)(1 + t2 w) = 1 + D; the certificate")
log("    F(t1,t2) := (t1+t2)^2 (|P|^4 - |N|^2) =")
log("      " + str(sp.factor(F)))
log(f"    has {len(coeffs)} monomials, all coefficients >= 0: {nonneg}  (lowest total degree "
    f"{min(sum(m) for m in poly.monoms())}).  Hence |N| <= |P|^2, i.e. |v_IF| <= (t1+t2)/4, for ALL t1, t2 >= 0;")
log("    then |v_II| = |t1-t2|/(t1+t2) |v_IF| <= |t1-t2|/4, and the (F,I), (F,F) patterns follow by x -> -x.")
log("    |P|^2 = (1 + sqrt2 t1 + t1^2)(1 + sqrt2 t2 + t2^2) = " + str(sp.factor(P2)))
# (5) remainder: v_IF - xi/4 = -D (2 x1 x2 + xi D) / (4 (1+D)^2)
xi = x1 - x2
rem_id = sp.simplify(cIF - xi/4 + D*(2*x1*x2 + xi*D)/(4*(1 + D)**2)) == 0
ok &= rem_id
log("(5) identity v_IF - (x1-x2)/4 = -D (2 x1 x2 + (x1-x2) D) / (4 (1+D)^2): " + str(rem_id))
log("    with |D| <= s + p, |2 x1 x2 + xi D| <= 2p + s(s+p), p = t1 t2 <= s^2/4, |1+D|^2 = |P|^2 >= 1 + sqrt2 s:")
log("    |v_K - (x1-x2)/4| <= s^3 (1+s/4)(3/2+s/4) / (4 (1 + sqrt2 s))   (all four patterns; (I,I) via the factor |t1-t2|/s)")
# (6) numerical confirmation, independent pole-sum implementation and 1-D PV representation
rng = np.random.default_rng(20261014)
def wK_num(z1, z2, K=1.0):
    poles = lambda z: [(z, K**2/(z**2 + K**2)), (1j*K, z/(2*(z - 1j*K))), (-1j*K, z/(2*(z + 1j*K)))]
    tot = 0
    for p1, u1 in poles(z1):
        for p2, u2 in poles(z2):
            f1, f2 = p1.imag < 0, p2.imag < 0
            Wt = p1/(p1 + p2) if (f1 and f2) else (p2/(p1 + p2) if (not f1 and not f2) else (1.0 if (not f1 and f2) else 0.0))
            tot += u1*u2*Wt
    return tot
sup_half = 0; sup_lin = 0; sup_rem = 0
th = np.pi/4
for n in range(300000):
    tt = 10**rng.uniform(-5, 5, size=2); sg = rng.choice([-1, 1], size=2)
    z = 1j/(sg*tt*np.exp(1j*(th + np.pi/2)))           # K = 1; x_e = i/z_e = sg t e^{i 3pi/4}
    xK = 1j/z
    vv = wK_num(z[0], z[1]) - 0.5
    s = tt.sum()
    sup_half = max(sup_half, abs(vv))
    sup_lin = max(sup_lin, abs(vv)/(s/4))
    remb = s**3*(1 + s/4)*(1.5 + s/4)/(4*(1 + np.sqrt(2)*s))
    sup_rem = max(sup_rem, abs(vv - (xK[0] - xK[1])/4)/remb)
okn = sup_half < 0.5 + 1e-12 and sup_lin <= 1 + 1e-9 and sup_rem <= 1 + 1e-9
ok &= okn
log(f"(6) 3e5 random points, |x_e| in [1e-5, 1e5], all sign patterns: sup|v_K| = {sup_half:.6f} (< 1/2);"
    f"  sup |v_K|/((|x1|+|x2|)/4) = {sup_lin:.6f} (<= 1);  sup |v_K-(x1-x2)/4| / remainder bound = {sup_rem:.4f} (<= 1)")
# (7) c_U on the pi/4 rays: exact function of t = |x|, analytic bound (3+sqrt2)/2
tgrid = np.exp(np.linspace(np.log(1e-6), np.log(1e6), 2000001))
cU_t = tgrid**2/np.sqrt(1 + tgrid**4) + 0.5/np.sqrt(1 - np.sqrt(2)*tgrid + tgrid**2) + 0.5/np.sqrt(1 + np.sqrt(2)*tgrid + tgrid**2)
imax = np.argmax(cU_t)
log(f"(7) c_U(t) = t^2/sqrt(1+t^4) + 1/(2 sqrt(1 - sqrt2 t + t^2)) + 1/(2 sqrt(1 + sqrt2 t + t^2)) on the pi/4 rays;")
log(f"    numerical maximum {cU_t[imax]:.5f} at t = {tgrid[imax]:.4f};  analytic bound: t^2/sqrt(1+t^4) <= 1,"
    f" 1 - sqrt2 t + t^2 >= 1/2, 1 + sqrt2 t + t^2 >= 1  =>  c_U <= 1 + 1/sqrt2 + 1/2 = (3+sqrt2)/2 = {(3 + np.sqrt(2))/2:.5f}")
ok &= cU_t[imax] <= (3 + np.sqrt(2))/2
# direct check of c_U against the pole weights on both rays
cmax = 0
for t in tgrid[::1000]:
    for sg in (1, -1):
        z = 1j/(sg*t*np.exp(1j*3*np.pi/4))
        cmax = max(cmax, abs(1/(z**2 + 1)) + abs(z/(2*(z - 1j))) + abs(z/(2*(z + 1j))))
log(f"    direct pole-weight evaluation on both rays: max sum|u| = {cmax:.5f}")
log("ALL PASS" if ok else "SOME CHECK FAILED")
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'final2_logs', 'vK_bounds_proof.log'), 'w') as f:
    f.write('\n'.join(out) + '\n')
