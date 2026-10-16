"""
glauber_poles.py  --  Part (1) of research/c_glauber: Glauber pinch analysis at one-gluon level.

Conventions (binding, CONTEXT.md): metric (+,-,-,-); v^pm=(v^0 pm v^3)/sqrt2; v.w = v^+w^- + v^-w^+ - vT.wT.
Hadron A moves along +z (large plus momentum), hadron B along -z (large minus momentum).
n_A=(1^+,0^-,0_T) so n_A.k = k^- ;  n_B=(0^+,1^-,0_T) so n_B.k = k^+ .

Checks:
 P1  pole classification (half-planes) for every one-gluon attachment class in DY, DIS, e+e-,
     computed from the exact propagators with numerical collinear/Glauber kinematics;
     compared with CSS review (arXiv:hep-ph/0409313v1) eq.(166) [text verified] and with the
     contour arguments of Collins 1998 (hep-ph/9709499v2, Sec. III) [text verified].  (Collins 2011,
     Chs. 5 and 14, treats the same material; exact equation/section numbers there NOT verified here.)
 P2  two-pole residue formula used for the spectator-spectator exchange (exact, sympy).
 P3  blueprint E7.24 integral (past-past eikonal lines) and past-minus-future eikonal difference.
 P4  DIS final-state interaction: the k^+ (jet-side) contour can be deformed; eikonal approx. valid
     on the deformed contour (numerical, exact propagators).  Contrast: DY spectator-spectator trapped.
 P5  power counting of the DY spectator-spectator Glauber exchange (Collins 2011 Sec.5.6.2): Q^0.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
from scipy import integrate

RESULTS = []
def check(name, ok, detail=''):
    RESULTS.append((name, bool(ok)))
    print(('PASS' if ok else 'FAIL') + '  ' + name + ('   [' + detail + ']' if detail else ''))

# ----------------------------------------------------------------------------------------------
# light-front helpers
def dot(a, b):
    """a=(plus, minus, T1, T2)"""
    return a[0]*b[1] + a[1]*b[0] - a[2]*b[2] - a[3]*b[3]

def vec(p, m, pT):
    """on-shell momentum with given plus component p, mass m, transverse pT (2-vector)"""
    pT = np.asarray(pT, float)
    return np.array([p, (m**2 + pT @ pT)/(2*p), pT[0], pT[1]])

# ----------------------------------------------------------------------------------------------
# P1: pole classification.
# A propagator 1/((l + s k)^2 - M^2 + i0) is linear in k^- for an A-collinear line (coefficient
# 2 s (l^+ + s k^+)) and linear in k^+ for a B-collinear line (coefficient 2 s (l^- + s k^-)).
# We compute the location of the pole numerically, including the +i eps, and read off Im(pole).
def pole_im_kminus(l, s, k, M, eps=1e-9):
    # D(k^-) = 2 (l^+ + s k^+)(l^- + s k^-) - (lT + s kT)^2 - M^2 + i eps = 0, solve for k^-
    lp = l[0] + s*k[0]
    lT = l[2:] + s*k[2:]
    # 2 lp l^- + 2 lp s k^- - lT^2 - M^2 + i eps = 0
    kminus = (lT @ lT + M**2 - 2*lp*l[1] - 1j*eps)/(2*lp*s)
    return kminus

def pole_im_kplus(l, s, k, M, eps=1e-9):
    lm = l[1] + s*k[1]
    lT = l[2:] + s*k[2:]
    kplus = (lT @ lT + M**2 - 2*lm*l[0] - 1j*eps)/(2*lm*s)
    return kplus

def half(z):
    return 'UHP' if z.imag > 0 else 'LHP'

Q = 100.0
lam = 0.05            # lambda = m/Q
m = lam*Q             # hadronic scale
# hadron momenta
PA = vec(Q, m, [0, 0]); PB = np.array([m**2/(2*Q), Q, 0, 0])
# final-state spectators (A-collinear, B-collinear) with transverse momenta ~ m
pAp = vec(0.6*Q, m, [0.7*m, 0.2*m])                       # s_A final momentum
pBp_T = np.array([-0.3*m, 0.5*m])
pBp = np.array([(m**2 + pBp_T@pBp_T)/(2*0.55*Q), 0.55*Q, pBp_T[0], pBp_T[1]])   # s_B final momentum
la = PA - pAp      # active parton a (k = 0)
lb = PB - pBp      # active parton b (k = 0)
# Glauber gluon momentum k ~ (m^2/Q, m^2/Q, m)
kG = np.array([0.4*m**2/Q, -0.3*m**2/Q, 0.8*m, -0.5*m])

print('\n=== P1: pole half-planes, one-gluon exchange, k flows from the B-side line Y into the A-side line X ===')
print('kinematics: Q=%.0f, m=%.1f; Glauber k=(%.3g,%.3g,%.3g,%.3g)' % (Q, m, *kG))
# Routing rule (amplitude): k enters X, flows back along A-lines to the hard vertex H, then from H
# back along B-lines to Y.  Sign s = +1 if k flows along the line's own momentum direction.
#   X = s_A : segment (A-blob -> X) carries p_A' - k  (s=-1);  line a carries l_a + k (s=+1)
#   X = a   : segment (X -> H) carries l_a + k (s=+1)
#   Y = s_B : segment (B-blob -> Y) carries p_B' + k (s=+1);   line b carries l_b - k (s=-1)
#   Y = b   : segment (Y -> H) carries l_b - k (s=-1)
Mq = m
A_lines = {'sA': [('s_A seg', pAp, -1), ('a', la, +1)], 'a': [('a seg', la, +1)]}
B_lines = {'sB': [('s_B seg', pBp, +1), ('b', lb, -1)], 'b': [('b seg', lb, -1)]}
table = {}
for X in ['sA', 'a']:
    for Y in ['sB', 'b']:
        km = [(nm, half(pole_im_kminus(l, s, kG, Mq))) for nm, l, s in A_lines[X]]
        kp = [(nm, half(pole_im_kplus(l, s, kG, Mq))) for nm, l, s in B_lines[Y]]
        trap_m = len(set(h for _, h in km)) == 2
        trap_p = len(set(h for _, h in kp)) == 2
        table[(X, Y)] = (km, kp, trap_m, trap_p)
        print('  X=%-3s Y=%-3s | k^- poles: %-34s trapped=%-5s | k^+ poles: %-34s trapped=%-5s | Glauber pinch=%s'
              % (X, Y, km, trap_m, kp, trap_p, trap_m and trap_p))

check('P1a DY spectator-spectator: k^- AND k^+ trapped (Glauber pinch)',
      table[('sA', 'sB')][2] and table[('sA', 'sB')][3])
check('P1b DY s_A-spectator / B-active: k^- trapped, k^+ NOT trapped (deform k^+ -> A-collinear, past-pointing W in f_A)',
      table[('sA', 'b')][2] and not table[('sA', 'b')][3])
check('P1c DY A-active / s_B-spectator: k^+ trapped, k^- NOT trapped (mirror)',
      (not table[('a', 'sB')][2]) and table[('a', 'sB')][3])
check('P1d DY active-active (vertex): neither variable trapped by collinear lines',
      (not table[('a', 'b')][2]) and (not table[('a', 'b')][3]))
# CSS review eq.(166): spectator pole UHP, active pole LHP, both at distance ~ 2 l_T.q_T/p^+
zs = pole_im_kminus(pAp, -1, kG, Mq); za = pole_im_kminus(la, +1, kG, Mq)
check('P1e CSS(166): A-spectator pole in UHP, A-active pole in LHP, |Re k^-| ~ m^2/Q (Glauber scale)',
      zs.imag > 0 and za.imag < 0 and max(abs(zs.real), abs(za.real)) < 10*m**2/Q,
      'Re poles = %.3g, %.3g ; m^2/Q=%.3g' % (zs.real, za.real, m**2/Q))

# DIS: target A (active a, spectator s_A), current jet c outgoing with large minus momentum.
# FSI gluon between s_A (X) and jet c (Y): from H along c to Y, segment carries p_c + k (s=+1).
pc = np.array([m**2/(2*Q), Q, 0.0, 0.0]) + np.array([0, 0, 0.6*m, 0.1*m])
pc[0] = (m**2 + pc[2]**2 + pc[3]**2)/(2*pc[1])
kp_jet = half(pole_im_kplus(pc, +1, kG, Mq))
km_DIS = [half(pole_im_kminus(pAp, -1, kG, Mq)), half(pole_im_kminus(la, +1, kG, Mq))]
check('P1f DIS FSI (target spectator - current jet): k^- trapped by target lines, k^+ has only the jet (final-state) pole -> deformable; cf. Collins 1998 Sec. III B',
      len(set(km_DIS)) == 2 and kp_jet == 'LHP', 'k^- poles %s, jet k^+ pole %s' % (km_DIS, kp_jet))
# e+e-: two outgoing jets J1 (+z) and J2 (-z).  Make the route non-trivial: inside J1 the parton p1 splits
# (final state) into q1 + q2 and the gluon attaches to q1; inside J2 the parton p2 splits into r1 + r2 and the
# gluon attaches to r1.  Route: k enters q1 at X, flows back along q1 and p1 to H (against their momenta,
# s=-1), then from H along p2 and r1 to Y (with their momenta, s=+1).  ALL lines are final-state lines.
q1 = vec(0.6*Q, m, [0.5*m, 0.1*m]); q2 = vec(0.4*Q, m, [-0.2*m, 0.3*m]); p1 = q1 + q2      # p1 internal, off shell ~m^2
r1_T = np.array([-0.4*m, 0.2*m]); r2_T = np.array([0.1*m, -0.6*m])
r1 = np.array([(m**2 + r1_T @ r1_T)/(2*0.55*Q), 0.55*Q, *r1_T]); r2 = np.array([(m**2 + r2_T @ r2_T)/(2*0.45*Q), 0.45*Q, *r2_T])
p2 = r1 + r2
J1 = [half(pole_im_kminus(q1, -1, kG, Mq)), half(pole_im_kminus(p1, -1, kG, Mq))]   # internal p1: off shell by O(m^2)
J2 = [half(pole_im_kplus(r1, +1, kG, Mq)), half(pole_im_kplus(p2, +1, kG, Mq))]
check('P1g e+e- (all collinear lines are final-state lines): all J1 poles in k^- on one side, all J2 poles in k^+ on the other -> no trapping',
      len(set(J1)) == 1 and len(set(J2)) == 1, 'J1 k^- poles %s ; J2 k^+ poles %s' % (J1, J2))

# ----------------------------------------------------------------------------------------------
print('\n=== P2: two-pole residue formula (exact) ===')
x = sp.symbols('x', real=True)
a, b, c1, c2 = sp.symbols('a b c1 c2', positive=True)
e = sp.symbols('epsilon', positive=True)
# I = int dx/(2pi) 1/((-a x + c1 + i e)(b x + c2 + i e)), poles: x1=(c1+ie)/a in UHP, x2=-(c2+ie)/b in LHP
x1 = (c1 + sp.I*e)/a
res = sp.residue(1/((-a*x + c1 + sp.I*e)*(b*x + c2 + sp.I*e)), x, x1)
I_closed = sp.simplify(sp.I*res)      # 2 pi i * res / (2 pi)
pred = -sp.I/(b*c1 + a*c2 + sp.I*e*(a + b))
check('P2 int dx/2pi [(-a x+c1+i0)(b x+c2+i0)]^-1 = -i/(b c1 + a c2): sets the final-state line on shell',
      sp.simplify(I_closed - pred) == 0, str(sp.simplify(I_closed.subs(e, 0))))
# numerical confirmation with finite epsilon
an, bn, c1n, c2n, en = 1.3, 0.7, 0.4, -0.9, 1e-3
f = lambda t: 1/((-an*t + c1n + 1j*en)*(bn*t + c2n + 1j*en))
L = 2e4
re = integrate.quad(lambda t: f(t).real, -L, L, points=[c1n/an, -c2n/bn], limit=4000)[0]
im = integrate.quad(lambda t: f(t).imag, -L, L, points=[c1n/an, -c2n/bn], limit=4000)[0]
num = (re + 1j*im)/(2*np.pi)
exact = -1j/(bn*c1n + an*c2n + 1j*en*(an + bn))
check('P2n numerical (eps=1e-3)', abs(num - exact) < 2e-3*abs(exact), 'num=%s exact=%s' % (num, exact))

# ----------------------------------------------------------------------------------------------
print('\n=== P3: blueprint E7.24 and past-vs-future eikonal lines ===')
km_, kp_, kT2 = sp.symbols('k_m k_p kT2', real=True)
# integrand 1/((k^- + i e)(-k^+ + i e)(2 k^+ k^- - kT2 + i e)); decays like 1/(k^-)^2 -> close in UHP.
def E724(kpval):
    expr = 1/((km_ + sp.I*e)*(-kpval + sp.I*e)*(2*kpval*km_ - kT2 + sp.I*e))
    poles = [-sp.I*e, (kT2 - sp.I*e)/(2*kpval)]
    tot = 0
    for p_ in poles:
        if sp.im(p_.subs({e: sp.Rational(1, 10**6), kT2: 1})) > 0:
            tot += 2*sp.pi*sp.I*sp.residue(expr, km_, p_)
    return sp.simplify(sp.limit(tot, e, 0))
r_pos = E724(sp.Rational(3, 2)); r_neg = E724(-sp.Rational(3, 2))
check('P3a E7.24: k^- integral vanishes for k^+>0', r_pos == 0, str(r_pos))
check('P3b E7.24: k^- integral = -2 pi i/(kT^2 k^+) for k^+<0',
      sp.simplify(r_neg - (-2*sp.pi*sp.I/(kT2*(-sp.Rational(3, 2))))) == 0, str(r_neg))
# numerical version of P3b with finite eps, compared with the exact finite-eps residue value
kTn2, kpn, en = 1.0, -1.5, 2e-3
g = lambda t: 1/((t + 1j*en)*(-kpn + 1j*en)*(2*kpn*t - kTn2 + 1j*en))
def piecewise_real(fun, a_, b_, centres, widths):
    pts = [a_, b_]
    for c_, w_ in zip(centres, widths):
        # geometric breakpoints c +- w*10^k resolve the peak and the 1/|z| tails accurately
        for kk in range(0, 16):
            for d_ in ([0.0] if kk == 0 else []) + [-w_*10.0**kk, w_*10.0**kk]:
                if a_ < c_ + d_ < b_:
                    pts.append(c_ + d_)
    pts = sorted(set(pts))
    tot = 0j
    for x0, x1 in zip(pts[:-1], pts[1:]):
        tot += integrate.quad(lambda t: fun(t).real, x0, x1, limit=4000)[0] + 1j*integrate.quad(lambda t: fun(t).imag, x0, x1, limit=4000)[0]
    return tot
val = piecewise_real(g, -3e4, 3e4, [0.0, kTn2/(2*kpn)], [en, en/abs(2*kpn)])
re, im = val.real, val.imag
zp = (kTn2 - 1j*en)/(2*kpn)                      # UHP pole for k^+<0
exact_eps = 2j*np.pi/((zp + 1j*en)*(-kpn + 1j*en)*(2*kpn))
check('P3c E7.24 numerical (k^+=-1.5, kT^2=1, eps=2e-3) vs exact finite-eps residue; eps->0 limit -2 pi i/(kT^2 k^+)',
      abs((re + 1j*im) - exact_eps) < 2e-4 and abs(exact_eps - (-2j*np.pi/(kTn2*kpn))) < 0.05,
      'num=%.5f%+.5fi  exact(eps)=%.5f%+.5fi  limit=%+.5fi' % (re, im, exact_eps.real, exact_eps.imag, (-2*np.pi/(kTn2*kpn))))
# past-pointing  1/(k+i0)  minus future-pointing 1/(k-i0) = -2 pi i delta(k): test function
phi = lambda t: np.exp(-(t - 0.3)**2)*(1 + 0.2*t)
for en in [1e-2, 1e-3]:
    vals = []
    for sgn in [+1, -1]:
        re = integrate.quad(lambda t: (phi(t)/(t + 1j*sgn*en)).real, -40, 40, points=[0], limit=4000)[0]
        im = integrate.quad(lambda t: (phi(t)/(t + 1j*sgn*en)).imag, -40, 40, points=[0], limit=4000)[0]
        vals.append(re + 1j*im)
    diff = vals[0] - vals[1]
print('   past - future on test fn: %s ; -2 pi i phi(0) = %s' % (diff, -2j*np.pi*phi(0)))
check('P3d 1/(k+i0) - 1/(k-i0) = -2 pi i delta(k)  (Glauber/Coulomb term)', abs(diff + 2j*np.pi*phi(0)) < 1e-2)

# ----------------------------------------------------------------------------------------------
print('\n=== P4: DIS final-state interaction can be deformed (numerical, exact propagators) ===')
# One-gluon FSI in SIDIS-like kinematics (cf. Collins-Qiu 2007 eq.(3.8)): after the l^- integral is done
# (target side), the l^+ dependence near the Glauber region is the jet propagator
#   1/((p_c - l)^2 - mc^2 + i0) ~ 1/(-2 p_c^- l^+ + c_J + i0)   [pole in the UHP]
# times the gluon propagator 1/(2 l^+ l^- - K^2 + i0), K^2 = lT^2 + mg^2, whose pole is at |l^+| ~ K^2/|l^-| ~ Q.
# Small finite widths eps are used so that the real-axis integral can be done numerically.
pcm = Q; K2 = (0.9*m)**2 + (0.7*m)**2; cJ = 0.6*m**2
epsJ = 1e-3*m**2; epsg = 1e-3*m**2
W = 3*lam*Q; Lmax = 2e4*Q

def path_integral(f, segs):
    tot = 0j
    for z0, z1 in segs:
        if abs(z1 - z0) == 0:
            continue
        fr = lambda t: (f(z0 + (z1 - z0)*t)*(z1 - z0)).real
        fi = lambda t: (f(z0 + (z1 - z0)*t)*(z1 - z0)).imag
        tot += integrate.quad(fr, 0, 1, limit=4000)[0] + 1j*integrate.quad(fi, 0, 1, limit=4000)[0]
    return tot

def contour_value(f, poles, depth):
    """Integral along a path equal to the real axis for |Re z|>W and displaced by i*depth for |Re z|<W
    (depth=0: real axis).  Real stretches are split at every pole so that narrow peaks are resolved."""
    cen = [p.real for p in poles]; wid = [max(abs(p.imag), 1e-9) for p in poles]
    if depth == 0:
        return piecewise_real(f, -Lmax, Lmax, cen, wid)
    tot = piecewise_real(f, -Lmax, -W, cen, wid) + piecewise_real(f, W, Lmax, cen, wid)
    tot += path_integral(f, [(-W + 0j, -W + 1j*depth), (-W + 1j*depth, W + 1j*depth), (W + 1j*depth, W + 0j)])
    return tot

for lm in [+0.5*m**2/Q, -0.5*m**2/Q]:
    fJ = lambda z, eik=False: 1.0/(-2*pcm*z + (0.0 if eik else cJ) + 1j*epsJ)
    fg = lambda z: 1.0/(2*z*lm - K2 + 1j*epsg)
    f = lambda z: fJ(z)*fg(z)
    feik = lambda z: fJ(z, True)*fg(z)
    zJ = (cJ + 1j*epsJ)/(2*pcm); zg = (K2 - 1j*epsg)/(2*lm)
    I_real = contour_value(f, [zJ, zg], 0)
    I_down = contour_value(f, [zJ, zg], -lam*Q)
    I_down2 = contour_value(f, [zJ, zg], -0.3*lam*Q)
    I_up = contour_value(f, [zJ, zg], +lam*Q)
    I_eik = contour_value(feik, [1j*epsJ/(2*pcm), zg], -lam*Q)
    resJ = (1.0/(-2*pcm))*fg(zJ)
    print('   l^-=%+.4g: real axis=%s  down-dip=%s  up-dip=%s  (up-down)/(2 pi i ResJ)=%s'
          % (lm, I_real, I_down, I_up, (I_up - I_down)/(2j*np.pi*resJ)))
    check('P4a l^-=%+.3g: contour pushed into the LHP (two depths) reproduces the real-axis value' % lm,
          abs(I_down - I_real) < 1e-4*2*np.pi*abs(resJ) and abs(I_down2 - I_down) < 1e-6*2*np.pi*abs(resJ),
          '|diff|/|2 pi Res_J| = %.1e' % (abs(I_down - I_real)/(2*np.pi*abs(resJ))))
    check('P4b l^-=%+.3g: the only nearby singularity is the final-state jet pole, in the UHP (up-dip differs by -2 pi i Res)' % lm,
          abs((I_up - I_down) + 2j*np.pi*resJ) < 1e-6*abs(resJ)*2*np.pi)
    check('P4e l^-=%+.3g: on the deformed contour the eikonal jet line 1/(-2p_c^- l^+ + i0) [future-pointing] is accurate (rel.err < lam)' % lm,
          abs(I_eik - I_down) <= lam*abs(I_down) + 1e-14, 'rel err=%.2e' % (abs(I_eik - I_down)/max(abs(I_down), 1e-30)))

# Contrast: DY spectator-spectator. k^+ dependence: s_B segment (pole LHP) and b (pole UHP), both within ~m^2/Q.
cs, cb = 0.5*m**2, -0.8*m**2; es = 1e-3*m**2
km_G = 0.3*m**2/Q
fss = lambda z: 1.0/((2*pBp[1]*z + cs + 1j*es)*(-2*lb[1]*z + cb + 1j*es)*(2*z*km_G - K2 + 1j*es))
zs_ = (-cs - 1j*es)/(2*pBp[1]); zb_ = (cb + 1j*es)/(2*lb[1]); zg_ = (K2 - 1j*es)/(2*km_G)
I_real = contour_value(fss, [zs_, zb_, zg_], 0)
I_dn = contour_value(fss, [zs_, zb_, zg_], -lam*Q); I_up = contour_value(fss, [zs_, zb_, zg_], +lam*Q)
# exact real-axis value by residues (integrand ~ 1/z^3 -> close in the UHP: only the b pole, since zg_ is in the LHP)
res_b = (1.0/(2*pBp[1]*zb_ + cs + 1j*es))*(1.0/(-2*lb[1]))*(1.0/(2*zb_*km_G - K2 + 1j*es))
I_res = 2j*np.pi*res_b
check('P4d DY spectator-spectator: numerical real-axis k^+ integral equals residue of the b (initial-state) pole',
      abs(I_real - I_res) < 1e-4*abs(I_res), 'num=%s res=%s' % (I_real, I_res))
print('   DY s-s: real axis=%s  down-dip=%s  up-dip=%s' % (I_real, I_dn, I_up))
check('P4c DY spectator-spectator k^+: neither deformation reproduces the real-axis value (contour trapped at k^+ ~ m^2/Q)',
      abs(I_dn - I_real) > 0.5*abs(I_real) and abs(I_up - I_real) > 0.5*abs(I_real))

# ----------------------------------------------------------------------------------------------
print('\n=== P5: power counting of the spectator-spectator Glauber exchange (Collins 2011 Sec.5.6.2) ===')
lamS = sp.symbols('lambda', positive=True)
QQ = sp.symbols('Q', positive=True)
# scale: k^pm ~ lam^2 Q, kT ~ lam Q  (so m ~ lam Q).  Extra factors relative to the tree graph:
measure = (lamS**2*QQ)**2*(lamS*QQ)**2       # dk^+ dk^- d^2kT
gluon = 1/(lamS*QQ)**2                       # -1/(kT^2+mg^2)
spect_props = 1/((lamS*QQ)**2)**2            # two spectator lines now off shell by O(m^2)
numer = QQ**2                                # couplings to large components: 2p_A^+ x 2p_B^-
active_change = 1                            # active lines keep virtuality O(m^2): unchanged
power = sp.simplify(measure*gluon*spect_props*numer*active_change)
check('P5 extra Glauber gluon is leading power: measure x denominators x numerator ~ Q^0 lambda^0',
      sp.simplify(power) == 1, 'scaling factor = %s' % power)

print('\nSUMMARY: %d/%d PASS' % (sum(ok for _, ok in RESULTS), len(RESULTS)))
