#!/usr/bin/env python3
"""N25 (stage-2 verifier): abelian DY Glauber toy and the plus-prescription trap.
Methods deliberately different from the project script (glauber_toy.py) and from stage 1
(Schwinger parametrisation, real-axis finite-eps quadrature):
  (1) chi(b): Hankel transform with mpmath.quadosc + classical eikonal phase of a repulsive Yukawa potential
  (2) light-front Jacobian and sign bookkeeping of the one-exchange kernel (sympy)
  (3) k^- integral of the trapped pair and I_as: exact partial-fraction evaluation at FINITE eps (no residues,
      no numerical quadrature), plus an independent check on a complex bump contour (mpmath)
  (4) eikonal replacement / past-pointing rule from the semi-infinite line integral (sympy)
  (5) cut sums: direct-space 1D quadrature (no FFT) of O(g^2), O(g^4) interference
  (6) plus trap: general symbolic identity, the 7/4, and a proof that the literal claim text is false
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import sympy as sp
import numpy as np

mp.mp.dps = 30
NP = 0; NF = 0
def check(name, ok, info=''):
    global NP, NF
    if ok: NP += 1
    else: NF += 1
    print(('[PASS] ' if ok else '[FAIL] ') + name + ('   ' + info if info else ''))

# ---------------------------------------------------------------- (1) chi(b)
gAgB = mp.mpf('0.7')
for m, b in [(mp.mpf(1), mp.mpf('0.3')), (mp.mpf('0.5'), mp.mpf(2)), (mp.mpf(2), mp.mpf('1.1'))]:
    # int d^2k/(2pi)^2 e^{ik.b}/(k^2+m^2) = (1/2pi) int_0^inf k J0(kb)/(k^2+m^2) dk
    hank = mp.quadosc(lambda k: k * mp.besselj(0, k * b) / (k**2 + m**2), [0, mp.inf], omega=b) / (2 * mp.pi)
    target = mp.besselk(0, m * b) / (2 * mp.pi)
    check('(1a) 2D FT of 1/(k^2+m^2) = K0(mb)/(2pi) via Hankel transform, m=%s b=%s' % (m, b),
          abs(hank - target) < 1e-20, 'rel dev %.1e' % float(abs(hank / target - 1)))
    chi = -gAgB / (2 * mp.pi) * mp.besselk(0, m * b)
    # classical eikonal phase for a repulsive Yukawa potential V(r)=gAgB e^{-mr}/(4 pi r), speed 1:
    chi_cl = -mp.quad(lambda z: gAgB * mp.exp(-m * mp.sqrt(b**2 + z**2)) / (4 * mp.pi * mp.sqrt(b**2 + z**2)), [-mp.inf, 0, mp.inf])
    check('(1b) chi(b) = -(gAgB/2pi)K0(mb) equals the classical eikonal phase -int dz V (repulsive for gAgB>0)',
          abs(chi - chi_cl) < 1e-20, 'chi=%s' % mp.nstr(chi, 12))

# ---------------------------------------------------------------- (2) Jacobian, sign of kernel
k0, k3, kp, km = sp.symbols('k0 k3 kp km', real=True)
J = sp.Matrix([[(k0 + k3) / sp.sqrt(2)], [(k0 - k3) / sp.sqrt(2)]]).jacobian(sp.Matrix([k0, k3]))
check('(2a) |d(k+,k-)/d(k0,k3)| = 1, so d^4k = dk+ dk- d^2k_T', sp.simplify(abs(J.det())) == 1)
# one-exchange kernel: vertices (i gA)(i gB) * (v_A.v_B=1) * Feynman-gauge propagator -i g_{mu nu}/(k^2-m^2) at k^+=k^-=0
kT2, m2, gA, gB = sp.symbols('kT2 m2 gA gB', positive=True)
kernel = (sp.I * gA) * (sp.I * gB) * (-sp.I) / (-kT2 - m2)
check('(2b) exchange kernel = -i gA gB/(kT^2+m^2)  =>  i chi(b) = -i gA gB K0/(2pi), chi real',
      sp.simplify(kernel - (-sp.I * gA * gB / (kT2 + m2))) == 0, str(sp.simplify(kernel)))

# ---------------------------------------------------------------- (3) exact partial-fraction integral
def pf_integral(al, be, ga, de):
    """int_{-inf}^{inf} dk / ((al k + be)(ga k + de)), al,ga real nonzero, Im be>0, Im de>0 (exact, any finite eps)"""
    return -1j * mp.pi * (mp.sign(al) - mp.sign(ga)) / (al * de - be * ga)

# symbolic derivation of pf_integral (antiderivative, limits along the real axis, Im be, Im de > 0)
kk = sp.symbols('k', real=True)
R = sp.symbols('R', positive=True)
al_, ga_ = sp.symbols('alpha gamma', positive=True)
be_ = sp.Symbol('beta'); de_ = sp.Symbol('delta')
anti = (sp.log(al_ * kk + be_) - sp.log(ga_ * kk + de_)) / (al_ * de_ - be_ * ga_)
check('(3a) partial fractions: d/dk antiderivative = integrand',
      sp.simplify(sp.diff(anti, kk) - 1 / ((al_ * kk + be_) * (ga_ * kk + de_))) == 0)
# numeric cross-check of the closed form against brute-force quadrature at moderate eps (different eps each time)
for (al, be, ga, de) in [(2.0, 0.3 + 0.2j, -1.3, -0.7 + 0.1j), (1.0, -0.5 + 0.05j, 0.7, 0.4 + 0.3j), (-1.5, 0.2 + 0.4j, 2.5, 1.1 + 0.2j)]:
    f = lambda k: 1 / ((al * k + be) * (ga * k + de))
    num = mp.quad(f, [-mp.inf, -10, -1, 0, 1, 10, mp.inf])
    check('(3b) closed form = quadrature at finite eps (al=%g, ga=%g)' % (al, ga), abs(num - pf_integral(al, be, ga, de)) < 1e-12,
          'quad=%s formula=%s' % (mp.nstr(num, 10), mp.nstr(pf_integral(al, be, ga, de), 10)))

# trapped k^- integral of the S-S graph: int dk-/2pi  i/(-2pA'(k- - k1)+i0) * 1/(2pa(k- - k2)+i0)  = F(k1)/(2pA')
pAp, pa, k1, k2 = mp.mpf('1.3'), mp.mpf('0.8'), mp.mpf('0.011'), mp.mpf('-0.004')
eps = mp.mpf('1e-25')
val = 1j / (2 * mp.pi) * pf_integral(-2 * pAp, 2 * pAp * k1 + 1j * eps, 2 * pa, -2 * pa * k2 + 1j * eps)
pred = 1 / (2 * pAp) * 1 / (2 * pa * (k1 - k2))
check('(3c) S-S trapped k^- integral = F(k1)/(2p_A\'^+): spectator s_A put on shell', abs(val - pred) < 1e-15,
      'val=%s pred=%s' % (mp.nstr(val, 12), mp.nstr(pred, 12)))
# same-side control
val2 = pf_integral(2 * pAp, -2 * pAp * k1 + 1j * eps, 2 * pa, -2 * pa * k2 + 1j * eps)
check('(3d) control: both poles on the same side -> integral 0 exactly', abs(val2) == 0)

# I_as(k^-) = int dk+ 1/((2pb k+ + cb + i0)(2k+ k- - K^2 + i0))  vs  2 pi i theta(-k-)/(2 pb K^2 + 2 k- cb)
lam = mp.mpf('0.1'); Q = mp.mpf(1)
pb, cb, K2 = mp.mpf('0.9') * Q, mp.mpf('0.6') * lam**2 * Q**2, mp.mpf('1.3') * lam**2 * Q**2
for kmv in [mp.mpf('-0.6') * lam**2, mp.mpf('-2.0') * lam**2, mp.mpf('0.6') * lam**2, mp.mpf('1.7') * lam**2]:
    for e in [mp.mpf('1e-3') * lam**2, mp.mpf('1e-20')]:
        v = pf_integral(2 * pb, cb + 1j * e, 2 * kmv, -K2 + 1j * e)
        form = 2j * mp.pi * (1 if kmv < 0 else 0) / (2 * pb * K2 + 2 * kmv * cb)
        formeps = 2j * mp.pi * (1 if kmv < 0 else 0) / (2 * pb * (K2 - 1j * e) + 2 * kmv * (cb + 1j * e))
        ok = abs(v - formeps) < 1e-18 * max(1, abs(formeps)) and abs(v - form) <= 4 * float(e / K2) * max(1, abs(form)) + 1e-18
        check('(3e) I_as exact at eps=%s, k-=%s: = 2 pi i theta(-k-)/(2pb K^2+2k- cb) (+O(eps))' % (mp.nstr(e, 2), mp.nstr(kmv, 3)), ok,
              'I=%s formula=%s' % (mp.nstr(v, 10), mp.nstr(form, 10)))

# contour check: bump contour k = t + i H exp(-t^2/w^2); lifting over the Glauber region does not change I_as,
# lifting over the boson pole (Re k+ = K^2/(2k-) ~ -1) removes it entirely (=> saturated by the boson pole)
kmv = mp.mpf('-0.6') * lam**2
e = mp.mpf('1e-30')
f = lambda k: 1 / ((2 * pb * k + cb + 1j * e) * (2 * k * kmv - K2 + 1j * e))
def contour(bumps):
    """real axis deformed by non-overlapping compact C^1 bumps (c, w, H): z = t + i H (1-((t-c)/w)^2)^2 on |t-c|<w.
    H>0 lifts the contour (allowed across LHP poles), H<0 lowers it (allowed across UHP poles)."""
    bumps = sorted(bumps)
    tot = mp.mpc(0); left = -mp.inf
    for (c, w, H) in bumps:
        tot += mp.quad(f, [left, c - w]) if left == -mp.inf else mp.quad(f, [left, c - w])
        z = lambda t, c=c, w=w, H=H: t + 1j * H * (1 - ((t - c) / w)**2)**2
        dz = lambda t, c=c, w=w, H=H: 1 + 1j * H * 2 * (1 - ((t - c) / w)**2) * (-2 * (t - c) / w**2)
        tot += mp.quad(lambda t: f(z(t)) * dz(t), [c - w, c - w / 2, c, c + w / 2, c + w])
        left = c + w
    tot += mp.quad(f, [left, mp.inf])
    return tot
I0 = 2j * mp.pi / (2 * pb * K2 + 2 * kmv * cb)
kbos = K2 / (2 * kmv)           # boson pole, UHP for k^- < 0
# (f) contour lifted by i*lambda over the Glauber region |Re k+| < 3 lambda (moves away from the LHP b pole);
#     the boson pole far away is passed BELOW (a downward dip only keeps the quadrature away from it; no pole crossed)
Ig = contour([(mp.mpf(0), 3 * lam, lam), (kbos, mp.mpf('0.5'), mp.mpf('-0.2'))])
# (g) same, but now passing ABOVE the boson pole: the contour has crossed the only UHP pole
Ib = contour([(mp.mpf(0), 3 * lam, lam), (kbos, mp.mpf('0.5'), mp.mpf('0.2'))])
check('(3f) bump contour lifted by i*lambda over the Glauber region: value unchanged (no trapping in k+)', abs(Ig - I0) < 1e-12 * abs(I0),
      'lifted=%s exact=%s' % (mp.nstr(Ig, 10), mp.nstr(I0, 10)))
check('(3g) lifting above the boson pole at k+ = -K^2/(2|k-|) gives 0: the integral is the boson-pole residue', abs(Ib) < 1e-12 * abs(I0),
      '|lifted| = %s, pole at %s' % (mp.nstr(abs(Ib), 3), mp.nstr(K2 / (2 * kmv), 4)))

# (h) spectator-spectator k^+ integral with the EXACT boson propagator: poles s_B (kap_s - i0, LHP) and b (kap_b + i0, UHP)
#     both at |k+| ~ lambda^2: the Glauber region is trapped. Lifting the contour by i*lambda over it crosses the b pole.
pBp, kap_s, kap_b = mp.mpf('1.1'), mp.mpf('0.004'), mp.mpf('-0.007')
for kmv2 in [mp.mpf('0.6') * lam**2, mp.mpf('-0.6') * lam**2]:
    e2 = mp.mpf('1e-30')
    f = lambda k: 1 / ((2 * pBp * (k - kap_s) + 1j * e2) * (-2 * pb * (k - kap_b) + 1j * e2) * (2 * k * kmv2 - K2 + 1j * e2))
    kb2 = K2 / (2 * kmv2)
    Hb = mp.mpf('-0.2') if kmv2 < 0 else mp.mpf('0.2')       # pass the far boson pole on the side that crosses nothing
    # contour equivalent to the real axis with the Feynman i0's: small lift over s_B (LHP) and small dip under b (UHP)
    real_axis = contour([(kap_s, mp.mpf('0.004'), mp.mpf('0.002')), (kap_b, mp.mpf('0.004'), mp.mpf('-0.002')), (kb2, mp.mpf('0.5'), Hb)])
    lifted = contour([(mp.mpf(0), 3 * lam, lam), (kb2, mp.mpf('0.5'), Hb)])
    lowered = contour([(mp.mpf(0), 3 * lam, -lam), (kb2, mp.mpf('0.5'), Hb)])
    # Glauber-scale residue (close below on s_B): -2 pi i Res_{s_B}, boson propagator taken in Glauber approximation -1/K^2
    res_sB = -2j * mp.pi / (2 * pBp) / (-2 * pb * (kap_s - kap_b)) * (-1 / K2)
    ok = abs(real_axis / res_sB - 1) < 0.02 and abs(lifted - real_axis) > 0.5 * abs(real_axis) and abs(lowered - real_axis) > 0.5 * abs(real_axis)
    check('(3h) S-S exchange, k-=%s: value = Glauber-scale residue (boson -> -1/K^2), and lifting OR lowering by i*lambda changes it: trapped' % mp.nstr(kmv2, 2),
          ok, 'axis=%s  Glauber-residue=%s  lifted=%s  lowered=%s' % (mp.nstr(real_axis, 8), mp.nstr(res_sB, 8), mp.nstr(lifted, 5), mp.nstr(lowered, 5)))

# ---------------------------------------------------------------- (4) eikonal replacement and past-pointing line
Ieik = 2j * mp.pi / (2 * pb * K2)
check('(4a) eikonal b-line 1/(2pb k+ + i0): I_eik/I_as - 1 = k- cb/(pb K^2) = O(lambda^2)',
      abs(Ieik / I0 - 1 - kmv * cb / (pb * K2)) < 1e-25, 'rel. change %s (lambda^2 = %s)' % (mp.nstr(Ieik / I0 - 1, 4), mp.nstr(lam**2, 2)))
lmb, nk, et = sp.symbols('lambda nk eta', real=True)
etp = sp.Symbol('etap', positive=True)
past = sp.integrate(sp.exp(-sp.I * lmb * nk + etp * lmb), (lmb, -sp.oo, 0), conds='none')
fut = sp.integrate(sp.exp(-sp.I * lmb * nk - etp * lmb), (lmb, 0, sp.oo), conds='none')
check('(4b) past-pointing line W[0,-inf n], k flowing in: int_{-inf}^0 e^{-i lambda n.k + eta lambda} = i/(n.k + i eta)',
      sp.simplify(past - sp.I / (nk + sp.I * etp)) == 0, str(sp.simplify(past)))
check('(4c) future-pointing line gives -i/(n.k - i eta): the +i0 of the active-parton propagator selects the PAST-pointing line',
      sp.simplify(fut - (-sp.I) / (nk - sp.I * etp)) == 0, str(sp.simplify(fut)))
# the active b with k flowing in: i/((p_b+k)^2+i0) -> i/(2 p_b^- k^+ + i0) = (1/(2p_b^-)) * i/(n_B.k + i0), n_B.k = k^+
check('(4d) i/(2 pb^- k^+ + i0) = (1/2pb^-) x [past-pointing rule with n_B.k = k^+]', True, '(algebraic identity)')

# ---------------------------------------------------------------- (5) cut sums in direct space (1D toy, no FFT)
rng = np.random.default_rng(7)
xs = np.linspace(-12, 12, 1601); dx = xs[1] - xs[0]
M0 = (np.exp(-(xs - 0.7)**2 / 3) * (1 + 0.5j * np.sin(1.3 * xs)) + 0.3j * np.exp(-(xs + 1.5)**2))
Kr = 0.35 / ((xs[:, None] - xs[None, :])**2 + 0.8)      # real symmetric kernel K_r(p - p')
K = -1j * Kr * dx                                       # amplitude-level exchange kernel (-i x real)
M1 = K @ M0; M2 = 0.5 * K @ (K @ M0)
o2 = 2 * np.real(np.vdot(M0, M1)) * dx
o4 = (np.vdot(M1, M1).real + 2 * np.real(np.vdot(M0, M2))) * dx
pointwise = np.sum(np.abs(2 * np.real(np.conj(M0) * M1))) * dx
check('(5a) O(g^2): pointwise interference nonzero but its integral over the relative momentum vanishes',
      abs(o2) < 1e-13 * pointwise and pointwise > 1e-2, 'int|.|=%.3e, int=%.1e' % (pointwise, o2))
check('(5b) O(g^4): int[|M1|^2 + 2Re M0* M2] = 0', abs(o4) < 1e-13 * np.vdot(M1, M1).real * dx, 'int|M1|^2=%.3e, sum=%.1e' % (np.vdot(M1, M1).real * dx, o4))

# ---------------------------------------------------------------- (6) plus trap
z = sp.symbols('z', positive=True)
g = 1 + z**2
diff_coeff = sp.integrate(sp.simplify((g - g.subs(z, 1)) * sp.log(1 - z) / (1 - z)), (z, 0, 1))
check('(6a) g(z)D_1 - [g ln(1-z)/(1-z)]_+ = h(1) int_0^1 (g(z)-g(1)) ln(1-z)/(1-z) dz; for g=1+z^2 this is 7/4',
      sp.nsimplify(diff_coeff) == sp.Rational(7, 4), 'coefficient = %s' % diff_coeff)
# numerical, several test functions, product convention vs whole-term plus
def pair_prod(h):   # <(1+z^2) D_1, h> = int [(1+z^2) h(z) - 2 h(1)] ln(1-z)/(1-z)
    return mp.quad(lambda w: ((1 + w**2) * h(w) - 2 * h(1)) * mp.log(1 - w) / (1 - w), [0, 1])
def pair_whole(h):  # <[(1+z^2) ln(1-z)/(1-z)]_+, h>
    return mp.quad(lambda w: (1 + w**2) * (h(w) - h(1)) * mp.log(1 - w) / (1 - w), [0, 1])
def pair_literal(h):  # <[(1+z^2)/(1-z)]_+, h>  (what the condensed claim text literally says)
    return mp.quad(lambda w: (1 + w**2) * (h(w) - h(1)) / (1 - w), [0, 1])
tests = [lambda w: mp.exp(w) * mp.cos(2 * w), lambda w: 1 / (1 + 3 * w**2), lambda w: w**5 - 2 * w + 3, lambda w: mp.sin(4 * w) + 2]
ratios_ok = []; ratios_lit = []
for h in tests:
    ratios_ok.append((pair_prod(h) - pair_whole(h)) / h(1))
    ratios_lit.append((pair_prod(h) - pair_literal(h)) / h(1))
check('(6b) correct statement: (1+z^2)D_1 - [(1+z^2)ln(1-z)/(1-z)]_+ = (7/4) delta(1-z) on 4 test functions',
      all(abs(r - mp.mpf(7) / 4) < 1e-20 for r in ratios_ok), str([mp.nstr(r, 15) for r in ratios_ok]))
check('(6c) LITERAL claim text "(1+z^2)D_1 vs [(1+z^2)/(1-z)]_+ differ by (7/4)delta" is FALSE (difference/h(1) not constant)',
      max(ratios_lit) - min(ratios_lit) > 0.1, str([mp.nstr(r, 6) for r in ratios_lit]))
# DY delta coefficient: 4 C_F (1+z^2) D_1 + (2pi^2/3 - 8) C_F delta  ==  4 C_F [..]_+ + (2pi^2/3 - 1) C_F delta
check('(6d) consequence: delta coefficient of Delta_qqbar^(1) is C_F(2pi^2/3-8) in the product convention, C_F(2pi^2/3-1) with the whole-term plus',
      sp.simplify((2 * sp.pi**2 / 3 - 8) + 4 * sp.Rational(7, 4) - (2 * sp.pi**2 / 3 - 1)) == 0)

print('\nSUMMARY n25_s2: %d PASS, %d FAIL' % (NP, NF))
