"""W13 / s5: one-loop photon-gluon fusion contribution to g1 (prop:coll-anomaly-scheme); writer-derived.
Process gamma*(q) + g(k, helicity +-) -> q(p1) qbar(p2), massless quarks, on-shell gluon, D = 4 - 2 eps.
  hat g1 := (i/(2 k.q)) eps_{mu nu alpha beta} q^alpha k^beta W_A^{mu nu}(+),  W_A(+) = [W(+) - W(-)]/2,
  W^{mu nu}(lam) = (T_F e_q^2 g0^2/(4 pi)) int dPhi_2 eps_lam,gam eps*_lam,del T^{mu nu gam del},
  T^{mu nu gam del} = Tr[p1slash Gamma^{mu gam} p2slash Gammabar^{nu del}]  (Feynman rules, colour average 1/(N^2-1)).
Normalization of W is verified on the unpolarized F2 (CDR, average over D-2 gluon polarizations) against VF-DIS-5.
Two treatments of the antisymmetric (epsilon) tensors:
  (HVBM)  eps-tensors, gluon polarization vectors and the photon projector are 4-dimensional; momenta p1, p2 carry
          (D-4)-dimensional components; implemented exactly with an 8x8 representation of the Clifford algebra in
          6 dimensions, gamma5 = i G0 G1 G2 G3 (anticommutes with G0..G3, commutes with G4, G5);
  (naive) the product of the two epsilon tensors is continued as the D-dimensional generalized Kronecker delta
          (equivalent, for this graph, to an anticommuting gamma5); computed with the CDR trace engine.
MSbar: hat g1^bare + (alpha_s e_q^2/(2 pi)) (1/eps) Delta P_qg  =  (alpha_s e_q^2/2pi) Delta C_g, Delta P_qg = T_F(2x-1),
normalization g1 = (1/2) sum e_q^2 { (Dq + Dqbar) (x) [delta + a DC_q] + 2 Dg (x) a DC_g },  a = alpha_s/(2 pi).
Results (verified below):  Delta C_g^HVBM = T_F[(2x-1)(ln((1-x)/x) - 1) + 2(1-x)],  int_0^1 Delta C_g^HVBM = 0;
  D-dim collinear kernels: HVBM T_F[2x-1-2eps(1-x)], naive T_F[2x-1-eps(4x-1)] (same O(eps) first moment -eps);
  Delta C_g^naive = Delta C_g^HVBM + 3 T_F (2x-1): the first moment is NOT changed by continuing the eps tensors to D dims.
  (The regularization dependence of the first moment appears with four-dimensional regulators: s5b.)
"""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w13lib import *
import sympy as sp
import mpmath as mp
mp.mp.dps = 30

npass = 0; nfail = 0
def check(name, ok):
    global npass, nfail
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    if ok: npass += 1
    else: nfail += 1

eps = sp.Symbol('epsilon')
xs, v, w, phi = sp.symbols('x v w phi', positive=True)
TF = sp.Rational(1, 2)

# ============================================================ kinematics (c.m. frame of k+q, shat = 1)
# k = om (1,0,0,1), q = (1-om, 0,0,-om), om = k.q = 1/(2(1-x)) ; Q^2 = x/(1-x) ; p1 = (1/2)(1, sinth n_T, costh)
om = 1/(2*(1 - xs))
Q2 = xs/(1 - xs)
cth = 1 - 2*v
sth = 2*sp.sqrt(v*(1 - v))

# ============================================================ (1) naive / CDR symbolic engine
# dot products in terms of v (n = gauge vector along -z: n = (1,0,0,-1), n.k = 2 om, n.q = 2(1-om)... )
# n.p1 = (1/2)(1 + costh) = 1 - v ; n.p2 = (1/2)(1 - costh) = v ; n.n = 0
kq = om
kp1 = om*v; kp2 = om*(1 - v)
qp1 = sp.Rational(1, 2) - kp1; qp2 = sp.Rational(1, 2) - kp2
nk = 2*om; nq = (1 - om) + om          # n.q = q0 + q3*... : n=(1,0,0,-1): n.q = q^0 + q^3 = (1-om) - om*(-1)?? compute below
# careful: n.v = v^0 + v^3 for n = (1,0,0,-1) with metric (+,-,-,-): n.v = n^0 v^0 - n^3 v^3 = v^0 + v^3
nk = om + om
nq = (1 - om) + (-om)
np1 = sp.Rational(1, 2)*(1 + cth)
np2 = 1 - np1
dots = {('k', 'k'): 0, ('q', 'q'): -Q2, ('p1', 'p1'): 0, ('p2', 'p2'): 0, ('n', 'n'): 0,
        ('k', 'q'): kq, ('k', 'p1'): kp1, ('k', 'p2'): kp2, ('q', 'p1'): qp1, ('q', 'p2'): qp2,
        ('p1', 'p2'): sp.Rational(1, 2), ('n', 'k'): nk, ('n', 'q'): nq, ('n', 'p1'): np1, ('n', 'p2'): np2}
set_dots(dots)
check('kinematics: p1 + p2 = k + q consistent (k.p1 + k.p2 = k.q)', sp.simplify(kp1 + kp2 - kq) == 0)
check('kinematics: q.p1 + q.p2 = (k+q).q = k.q + q^2', sp.simplify(qp1 + qp2 - (kq - Q2)) == 0)
check('kinematics: n.p1 + n.p2 = n.(k+q)', sp.simplify(np1 + np2 - (nk + nq)) == 0)
# propagator denominators: (p1-q)^2 = -2 k.p2 ; (p1-k)^2 = -2 k.p1
den_a = -2*kp2       # (p1 - q)^2
den_b = -2*kp1       # (p1 - k)^2
def Gamma_terms(MU, GA):
    # Gamma^{mu gam} = g^mu (p1-q)/den_a g^gam + g^gam (p1-k)/den_b g^mu
    return [(1/den_a, [MU, V(p1=1, q=-1), GA]), (1/den_b, [GA, V(p1=1, k=-1), MU])]
def Gammabar_terms(NU, DE):
    return [(1/den_a, [DE, V(p1=1, q=-1), NU]), (1/den_b, [NU, V(p1=1, k=-1), DE])]
def T_slots(MU, NU, GA, DE):
    tot = 0
    for ca, sa in Gamma_terms(MU, GA):
        for cb, sb in Gammabar_terms(NU, DE):
            tot += ca*cb*tr([V(p1=1)] + sa + [V(p2=1)] + sb)
    return sp.expand(tot)

# ---- unpolarized F2 (normalization check against VF-DIS-5)
# sum over pol -> -g_{gam del}; photon F2 projector (1/(1-eps)) [ -g_{mu nu} + (3-2eps) (4x^2/Q^2) k_mu k_nu ]
Dsub = {D: 4 - 2*eps}
T_gg = T_slots(I('MU'), I('MU'), I('GA'), I('GA'))        # contracted mu-mu, ga-ga with +g
T_kk = T_slots(V(k=1), V(k=1), I('GA'), I('GA'))
Pg_unpol_g = (-1)*(-1)*T_gg      # (-g_{mu nu})(-g_{gam del}) T
Pg_unpol_k = (-1)*T_kk           # k_mu k_nu (-g_{gam del}) T
F2proj = (Pg_unpol_g + (3 - 2*eps)*4*xs**2/Q2*Pg_unpol_k)/(1 - eps)
F2proj = sp.simplify(F2proj.subs(Dsub))
avg = 1/(2*(1 - eps))   # 1/(D-2)
# W = (T_F e^2 g0^2/(4 pi)) int dPhi2 ; dPhi2 = (1/(8 pi)) (4 pi/shat)^eps/Gamma(1-eps) [v(1-v)]^(-eps) dv  (shat=1)
# g0^2 = 4 pi alpha_s mu^{2eps} e^{eps gE} (4pi)^{-eps}  =>  T_F e^2 g0^2/(4pi) * (4pi)^eps/(8 pi Gamma(1-eps))
#   = (alpha_s e^2/(2pi)) T_F * (1/4) mu^{2eps} e^{eps gE}/Gamma(1-eps)   [shat = 1 units: mu^2 -> mu^2/shat]
# F2/x = projector applied; VF-DIS-5: hatF2^g/(x e_q^2) = (alpha_s/2pi) T_F (mu^2/Q^2)^eps R2g
pref = sp.Rational(1, 4)*sp.exp(eps*sp.EulerGamma)/sp.gamma(1 - eps)   # times (mu^2/shat)^eps, alpha_s e^2 T_F/(2pi)
integrand_F2 = F2proj*avg*(v*(1 - v))**(-eps)
# integrate over v symbolically: the integrand is a sum of powers v^a (1-v)^b after partial fractions
def vint(expr):
    expr = sp.expand(sp.simplify(expr))
    num, den = sp.fraction(sp.together(expr))
    return expr
# do the v-integral by expanding in partial fractions in v times [v(1-v)]^{-eps}
def int_v(expr):
    """int_0^1 dv [v(1-v)]^{-eps} expr, expr rational in v: partial fractions, then Beta functions."""
    e2 = sp.apart(sp.together(sp.expand(expr)), v)
    tot = 0
    for t in sp.Add.make_args(sp.expand(e2)):
        t = sp.factor(t)
        cpart, rest = t.as_independent(v, as_Add=False)
        a_ = 0; b_ = 0
        for fac in sp.Mul.make_args(rest):
            if fac == 1:
                continue
            base, ex = fac.as_base_exp()
            if base == v:
                a_ += ex
            elif sp.expand(base - (v - 1)) == 0:
                b_ += ex; cpart *= (-1)**ex
            elif sp.expand(base - (1 - v)) == 0:
                b_ += ex
            elif sp.expand(base + v - 1) == 0:
                b_ += ex
            else:
                raise ValueError('unexpected factor ' + str(fac) + ' in ' + str(t))
        tot += cpart*sp.gamma(a_ + 1 - eps)*sp.gamma(b_ + 1 - eps)/sp.gamma(a_ + b_ + 2 - 2*eps)
    return tot
F2_v = int_v(sp.simplify(F2proj*avg))   # [v(1-v)]^{-eps} included in int_v
F2_res = sp.simplify(pref*F2_v)    # = hatF2/(x e^2) / (alpha_s T_F/2pi) * (mu^2/shat)^eps
# VF-DIS-5: (mu^2/Q^2)^eps R2g with R2g = 2 e^{eps gE} Gamma(-eps)/Gamma(2-2eps) (x/(1-x))^eps (x^2+(1-x)^2 -3eps+4eps^2-2eps^3)/(1-eps)^2
# (mu^2/Q^2)^eps = (mu^2/shat)^eps (shat/Q^2)^eps = (mu^2/shat)^eps ((1-x)/x)^eps
R2g = 2*sp.exp(eps*sp.EulerGamma)*sp.gamma(-eps)/sp.gamma(2 - 2*eps)*(xs/(1 - xs))**eps*(xs**2 + (1 - xs)**2 - 3*eps + 4*eps**2 - 2*eps**3)/(1 - eps)**2
target = sp.simplify(((1 - xs)/xs)**eps*R2g)
ok = all(abs(complex(sp.N((F2_res - target).subs({xs: xv, eps: ev}), 30))) < 1e-22
         for xv in (sp.Rational(1, 5), sp.Rational(2, 3)) for ev in (sp.Rational(1, 7), sp.Rational(-3, 10)))
check('(N) unpolarized F2 of the gamma* g box reproduces VF-DIS-5 exactly in eps (normalization of W verified)', ok)

# ---- polarized, naive: eps_{mu nu al be} q^al k^be * c * eps^{gam del rho sig} k_rho n_sig -> D-dim det
# polarization difference eps+ eps+* - eps- eps-* in terms of the eps tensor: determined numerically in 4D below.
# expand -det: lower indices (MU,NU,AL,BE), upper (GA,DE,RH,SI): eps_{L} eps^{U} = - sum_pi sgn(pi) prod delta^{U_pi(i)}_{L_i}
L_idx = ['MU', 'NU', 'AL', 'BE']; U_idx = ['GA', 'DE', 'RH', 'SI']
vec_low = {'AL': 'q', 'BE': 'k'}      # q^alpha, k^beta contracted into lower slots
vec_up = {'RH': 'k', 'SI': 'n'}       # k_rho, n_sigma contracted into upper slots
def perm_sign(p):
    s = 1; p = list(p)
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]: s = -s
    return s
def naive_epseps_T():
    tot = 0
    for p in itertools.permutations(range(4)):
        sgn = perm_sign(p)
        coef = -sgn
        slots = {}   # MU, NU, GA, DE -> slot
        scal = 1
        for i, Li in enumerate(L_idx):
            Uj = U_idx[p[i]]
            if Li in vec_low and Uj in vec_up:
                scal *= dot(vec_low[Li], vec_up[Uj])
            elif Li in vec_low:      # Uj in GA/DE
                slots[Uj] = V(**{vec_low[Li]: 1})
            elif Uj in vec_up:       # Li in MU/NU
                slots[Li] = V(**{vec_up[Uj]: 1})
            else:                    # photon index with gluon index: contracted pair
                name = 'C%d' % i
                slots[Li] = I(name); slots[Uj] = I(name)
        if scal == 0:
            continue
        tot += coef*scal*T_slots(slots['MU'], slots['NU'], slots['GA'], slots['DE'])
    return sp.expand(tot)
EE_T = naive_epseps_T()     # = eps_{mu nu al be} q^al k^be eps^{gam del rho sig} k_rho n_sig T^{mu nu}_{gam del}  (D-dim det)
# 4D numerical determination of c: eps+ eps+*^{gam del} - eps- eps-* = c eps^{gam del rho sig} k_rho n_sig / (k.n)
eta4 = sp.diag(1, -1, -1, -1)
kv = sp.Matrix([1, 0, 0, 1]); nv = sp.Matrix([1, 0, 0, -1])
ep = sp.Matrix([0, 1, sp.I, 0])/sp.sqrt(2); em = sp.Matrix([0, 1, -sp.I, 0])/sp.sqrt(2)
def low(vv): return eta4*vv
cvals = set()
for g_ in range(4):
    for d_ in range(4):
        # with lower-index polarization vectors contracted into T: use eps_gam (lower) eps*_del (lower)
        lhs = (low(ep)[g_]*sp.conjugate(low(ep)[d_]) - low(em)[g_]*sp.conjugate(low(em)[d_]))
        rhs = sum(sp.LeviCivita(a_, b_, r_, s_)*(1 if True else 0)*0 for a_, b_, r_, s_ in [] ) if False else None
        # eps_{gam del rho sig} (all lower) k^rho n^sig : lower eps = - upper eps numerically
        rhs_l = sum(-sp.LeviCivita(g_, d_, r_, s_)*kv[r_]*nv[s_] for r_ in range(4) for s_ in range(4))/(kv.T*eta4*nv)[0]
        if rhs_l != 0:
            cvals.add(sp.simplify(lhs/rhs_l))
        elif sp.simplify(lhs) != 0:
            cvals.add('mismatch')
print('   c (pol. difference / [eps_{gd rho sig} k^rho n^sig/(k.n)]) =', cvals)
check('pol. difference = c eps_{gam del rho sig} k^rho n^sig/(k.n) with a single constant c', len(cvals) == 1 and 'mismatch' not in cvals)
cpol = list(cvals)[0]
# In the naive contraction above we used eps^{gam del rho sig} k_rho n_sig with UPPER gam del (contracting T_{gam del});
# T^{mu nu gam del} eps_gam eps*_del = T^{mu nu}_{gam del} eps^gam eps*^del ; the difference of upper-index products equals
# c' eps^{gam del rho sig} k_rho n_sig/(k.n), with c' = c (raising all four indices of both sides gives the same sign).
# hat g1 = (i/(2 k.q)) * (1/2) * (T_F e^2 g0^2/(4pi)) int dPhi2 [ c eps_{..} q k eps^{..} k n T /(k.n) ]
# W^{mu nu} ~ M^{mu*} M^{nu} = T^{nu mu}: the antisymmetric part changes sign w.r.t. T^{mu nu}
g1_naive_v = sp.simplify(-(sp.I/(2*kq))*sp.Rational(1, 2)*cpol*EE_T.subs(Dsub)/nk)
print('   naive integrand (per alpha_s e^2 T_F/2pi, before pref & phase space):', sp.factor(g1_naive_v))

# ============================================================ (2) HVBM: explicit 8x8 representation
I2 = sp.eye(2); Z2 = sp.zeros(2)
sx = sp.Matrix([[0, 1], [1, 0]]); sy = sp.Matrix([[0, -sp.I], [sp.I, 0]]); sz = sp.Matrix([[1, 0], [0, -1]])
def blk(a, b, c, d): return sp.Matrix(sp.BlockMatrix([[a, b], [c, d]]))
g4 = [blk(I2, Z2, Z2, -I2)] + [blk(Z2, s_, -s_, Z2) for s_ in (sx, sy, sz)]
kron = lambda A, Bm: sp.kronecker_product(A, Bm)
G6 = [kron(g4[m], sz) for m in range(4)] + [kron(sp.eye(4), sp.I*sx), kron(sp.eye(4), sp.I*sy)]
eta6 = sp.diag(1, -1, -1, -1, -1, -1)
ok = all(sp.simplify(G6[a_]*G6[b_] + G6[b_]*G6[a_] - 2*eta6[a_, b_]*sp.eye(8)) == sp.zeros(8) for a_ in range(6) for b_ in range(6))
check('(H) 8x8 Clifford algebra in 6D: {G^a, G^b} = 2 eta^{ab}', ok)
G5h = sp.I*G6[0]*G6[1]*G6[2]*G6[3]
check('(H) HVBM gamma5 = i G0G1G2G3 anticommutes with G0..G3 and commutes with G4,G5',
      all(sp.simplify(G5h*G6[m] + G6[m]*G5h) == sp.zeros(8) for m in range(4)) and
      all(sp.simplify(G5h*G6[m] - G6[m]*G5h) == sp.zeros(8) for m in (4, 5)))
def sl6(vv):
    return sum((eta6[m, m]*vv[m]*G6[m] for m in range(6)), sp.zeros(8))
def tr6(M): return M.trace()/2      # normalize Tr 1 = 4
# vectors (6 components; extra dims 4,5; hat p along 4)
k6 = sp.Matrix([om, 0, 0, om, 0, 0]); q6 = sp.Matrix([1 - om, 0, 0, -om, 0, 0])
sw = sp.Symbol('sw', positive=True)       # sqrt(w): fraction of p_T^2 in the extra dimensions
cph, sph = sp.symbols('cph sph', real=True)
stv = 2*sp.sqrt(v*(1 - v)); ctv = 1 - 2*v; cwv = sp.sqrt(1 - sw**2)
p16 = sp.Matrix([sp.Rational(1, 2), stv*cwv*cph/2, stv*cwv*sph/2, ctv/2, stv*sw/2, 0])
p26 = sp.Matrix([1, 0, 0, 0, 0, 0]) - p16
def d6(a_, b_): return sum(eta6[m, m]*a_[m]*b_[m] for m in range(6))
def red(e):
    return sp.expand(sp.expand(e).subs(cph**2, 1 - sph**2))
check('(H) p1^2 = 0 with the explicit components', sp.simplify(red(d6(p16, p16))) == 0)
ep6 = sp.Matrix([0, 1, sp.I, 0, 0, 0])/sp.sqrt(2); em6 = sp.Matrix([0, 1, -sp.I, 0, 0, 0])/sp.sqrt(2)
P1 = sl6(p16); P2 = sl6(p26)
A1 = sl6(p16 - q6); A2 = sl6(p16 - k6)
da = sp.simplify(red(d6(p16 - q6, p16 - q6))); db = sp.simplify(red(d6(p16 - k6, p16 - k6)))
print('   (p1-q)^2 =', da, ' (p1-k)^2 =', db)
check('(H) denominators: (p1-q)^2 = -2 k.p2, (p1-k)^2 = -2 k.p1', sp.simplify(da - den_a) == 0 and sp.simplify(db - den_b) == 0)
def Gam(gmu, geps):     # Gamma with photon gamma matrix gmu and gluon slash(eps) geps
    return gmu*A1*geps/da + geps*A2*gmu/db
def Gambar(gnu, gepsc):
    return gepsc*A1*gnu/da + gnu*A2*gepsc/db
# polarization slashes: eps_gam gamma^gam with eps lower: slash(eps) = eps^mu gamma_mu
def slash_pol(e6): return sl6(e6)
def slash_polc(e6): return sl6(e6.applyfunc(sp.conjugate))
# photon projector: P_{mu nu} = eps_{mu nu al be} q^al k^be (4D, lower mu nu): contract with W^{mu nu}: sum_{mu nu} P_{mu nu} W^{mu nu}
def Pproj(mu, nu):
    return sum(-sp.LeviCivita(mu, nu, a_, b_)*q6[a_]*k6[b_] for a_ in range(4) for b_ in range(4))
def W_pol_contracted(e6):
    tot = 0
    for mu in range(4):
        for nu in range(4):
            c_ = Pproj(mu, nu)
            if c_ == 0: continue
            # W^{mu nu} uses gamma^mu (upper) in the amplitude: G6[mu]
            tot += c_*tr6(P1*Gam(G6[mu], slash_pol(e6))*P2*Gambar(G6[nu], slash_polc(e6)))
    return tot
Wp = W_pol_contracted(ep6); Wm = W_pol_contracted(em6)
g1_hvbm_pt = -sp.I/(2*kq)*sp.Rational(1, 2)*(Wp - Wm)   # per (T_F e^2 g0^2/4pi) int dPhi2; minus: W ~ M^{mu*}M^{nu}
g1_hvbm_pt = sp.expand(g1_hvbm_pt)
# average over azimuth (odd powers of cph, sph vanish; sph^2 -> 1/2) and over the extra-dimensional fraction w:
#   <sw^2> = w with Beta distribution in D-2 = 2-2eps transverse dims: <w> = -eps/(1-eps), <w^2> = -eps/(2-eps)
def avg_az(e):
    e = sp.expand(e)
    P = sp.Poly(e, cph, sph)
    out = 0
    for (a_, b_), cf in P.terms():
        if a_ % 2 or b_ % 2: continue
        # <cph^a sph^b> over phi: use beta function
        out += cf*sp.gamma(sp.Rational(a_ + 1, 2))*sp.gamma(sp.Rational(b_ + 1, 2))/(sp.pi*sp.gamma(sp.Rational(a_ + b_ + 2, 2)))
    return sp.expand(out)
g1h_az = sp.expand(avg_az(g1_hvbm_pt))
P_w = sp.Poly(sp.expand(g1h_az), sw)
print('   powers of sqrt(w) present in HVBM integrand:', [m_[0] for m_ in P_w.monoms()])
def wavg_f(pw):   # <w^(pw/2)> for w ~ Beta(n2/2, n1/2), n1 = 2, n2 = -2 eps, n = 2 - 2 eps
    j = pw//2; n2 = -2*eps; nn = 2 - 2*eps
    out = 1
    for i in range(j):
        out *= (n2 + 2*i)/(nn + 2*i)
    return out
wavg = {pw: wavg_f(pw) for pw in range(0, 9, 2)}
g1h = 0
for (pw,), cf in P_w.terms():
    if pw % 2: continue
    g1h += cf*wavg[pw]
g1h = sp.simplify(g1h)
print('   HVBM integrand (azimuth- and w-averaged):', sp.factor(sp.simplify(g1h)))
# consistency: at eps = 0 the two treatments agree pointwise
diff0 = sp.simplify((g1h - g1_naive_v).subs(eps, 0))
check('(H) at D = 4 the HVBM and naive integrands coincide pointwise', diff0 == 0)

# ============================================================ (3) phase space, MSbar, first moments
def finish(integrand, label):
    Iv = int_v(sp.simplify(integrand))
    res = sp.simplify(pref*Iv)      # hat g1 per (alpha_s e^2 T_F/2pi) (mu^2/shat)^eps
    # (mu^2/shat)^eps = (mu^2/Q^2)^eps (Q^2/shat)^eps = (x/(1-x))^eps at mu^2 = Q^2
    res_Q = res*(xs/(1 - xs))**eps
    ser_ = sp.series(res_Q, eps, 0, 1).removeO()
    pole = sp.simplify(ser_.coeff(eps, -1))
    fin = sp.simplify(ser_.coeff(eps, 0))
    print('   [%s] pole of hat g1/(alpha_s e^2 T_F/2pi) =' % label, sp.factor(pole))
    print('   [%s] finite part (mu^2=Q^2)                =' % label, sp.simplify(fin))
    return pole, fin
pole_h, fin_h = finish(g1h, 'HVBM')
pole_n, fin_n = finish(g1_naive_v, 'naive')
# hat g1 pole should be -(1/eps) Delta P_qg / T_F * (1)  in units (alpha_s e^2/(2pi)) T_F ... i.e. -(2x-1)/eps
check('pole: hat g1^bare -> -(alpha_s e^2/2pi)(1/eps) Delta P_qg, Delta P_qg = T_F (2x-1)  [HVBM]', sp.simplify(pole_h + (2*xs - 1)) == 0)
check('pole: same pole in the naive treatment', sp.simplify(pole_n + (2*xs - 1)) == 0)
# collinear splitting in D dims: residue of the 1/v pole of the v-integrand defines Delta hatP_qg(x,eps) up to normalization
coll_h = sp.simplify(sp.limit(g1h*v, v, 0)); coll_n = sp.simplify(sp.limit(g1_naive_v*v, v, 0))
print('   collinear factor (v->0) HVBM:', sp.factor(coll_h), ' naive:', sp.factor(coll_n))
ratio_h = sp.simplify(coll_h/coll_h.subs(eps, 0)*(2*xs - 1))
check('HVBM D-dim collinear kernel  prop. to  2x-1-2eps(1-x)+O(eps^2)', sp.simplify(sp.series(ratio_h, eps, 0, 2).removeO() - (2*xs - 1 - 2*eps*(1 - xs))) == 0)
ratio_n = sp.simplify(coll_n/coll_n.subs(eps, 0)*(2*xs - 1))
check('naive D-dim collinear kernel prop. to 2x-1-eps(4x-1)+O(eps^2)', sp.simplify(sp.series(ratio_n, eps, 0, 2).removeO() - (2*xs - 1 - eps*(4*xs - 1))) == 0)
check('both D-dim kernels have the same O(eps) first moment: int_0^1 = -eps', sp.integrate(-2*(1 - xs), (xs, 0, 1)) == -1 and sp.integrate(-(4*xs - 1), (xs, 0, 1)) == -1)
# MSbar: Delta C_g = finite part of [ hat g1 * 2pi/(alpha_s e^2) + (1/eps) Delta P_qg ]  (units: T_F * fin)
DCg_h = sp.simplify(TF*fin_h); DCg_n = sp.simplify(TF*fin_n)
expected_h = TF*((2*xs - 1)*(sp.log((1 - xs)/xs) - 1) + 2*(1 - xs))
check('Delta C_g^HVBM = T_F[(2x-1)(ln((1-x)/x) - 1) + 2(1-x)]  (MSbar, mu^2=Q^2)',
      all(abs(complex(sp.N((DCg_h - expected_h).subs(xs, xv), 30))) < 1e-25 for xv in (sp.Rational(1, 7), sp.Rational(1, 2), sp.Rational(5, 6))))
print('   Delta C_g^naive =', sp.simplify(DCg_n))
check('Delta C_g^naive - Delta C_g^HVBM = 3 T_F (2x-1)  (proportional to Delta P_qg: no change of the first moment)', sp.simplify(DCg_n - DCg_h - 3*TF*(2*xs - 1)) == 0)
m1_h = sp.integrate(sp.expand(DCg_h), (xs, 0, 1)); m1_n = sp.integrate(sp.expand(DCg_n), (xs, 0, 1))
print('   first moments: HVBM', sp.simplify(m1_h), ' naive', sp.simplify(m1_n))
check('first moment int_0^1 Delta C_g^HVBM = 0', sp.simplify(m1_h) == 0)
check('first moment int_0^1 Delta C_g^naive = 0 as well', sp.simplify(m1_n) == 0)
check('int_0^1 Delta P_qg = 0 (no log in the first moment)', sp.integrate(TF*(2*xs - 1), (xs, 0, 1)) == 0)
print('\nSUMMARY s5: %d PASS, %d FAIL' % (npass, nfail))
