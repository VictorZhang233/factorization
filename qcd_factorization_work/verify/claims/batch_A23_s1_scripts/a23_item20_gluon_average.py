#!/usr/bin/env python3
"""A23 item 20 (REVIEW D5): which D-dimensional gluon-polarisation average underlies the standard
MS-bar gluon coefficient function C_2^g of DIS?

Independent re-derivation (own D-dimensional Dirac-trace routine, own phase-space integration), not
using any project script:
  * gamma* g -> q qbar at O(alpha_s) in D = 4 - 2 eps, massless quarks, polarisation sum -g_{rho sigma}
    (legitimate: one external gluon, k_rho M^rho = 0 is checked symbolically below);
  * hadronic-tensor normalisation fixed by the LO quark result  F2/x = e_q^2 delta(1-z);
  * projections  F2/x = 2/(D-2) [ -g.W + (D-1)(4 x^2/Q^2) p.W.p ],  F_L/x = (8x^2/Q^2) p.W.p ;
  * MS-bar collinear counterterm  -(alpha_s/2pi)(1/eps) 2 P_qg(z) (pure pole, S_eps = (4pi)^eps e^{-eps gamma_E});
  * the bare result is computed with BOTH averages 1/(D-2) and 1/2; the finite remainders are compared with
    the standard textbook form  C_g = T_F[(z^2+(1-z)^2) ln((1-z)/z) - 1 + 8 z (1-z)]  (per flavour, q or qbar).

Run:  python3 -I a23_item20_gluon_average.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import itertools
from functools import lru_cache
import sympy as sp

eps, z, y, Q2 = sp.symbols('epsilon z y Q2', positive=True)
D = 4 - 2*eps

# ---------------------------------------------------------------- D-dimensional traces
# token = ('p', name) slashed momentum, ('i', label) gamma^label (all labels contracted in pairs)

def pair_value_terms(tokens):
    """All perfect matchings of the token list with the sign of the trace recursion."""
    if not tokens:
        yield 1, []
        return
    a = tokens[0]
    rest = tokens[1:]
    for k in range(len(rest)):
        sign = (-1)**k  # Tr(a1 a2 ... an) = sum_{k>=2} (-1)^k <a1 ak> Tr(...): k index shift
        b = rest[k]
        remaining = rest[:k] + rest[k+1:]
        for s2, pairs in pair_value_terms(remaining):
            yield sign*s2, [(a, b)] + pairs


def contract(pairs, dot):
    """Evaluate a product of pairings with every index label appearing exactly twice."""
    # occurrences: map each token occurrence (by id in pairs) to its partner in the pairing
    occ = []  # list of tokens with unique ids
    partner = {}
    for (a, b) in pairs:
        ia, ib = len(occ), len(occ)+1
        occ.append(a); occ.append(b)
        partner[ia] = ib; partner[ib] = ia
    # index identification: same label -> linked occurrences
    label_pos = {}
    for n, t in enumerate(occ):
        if t[0] == 'i':
            label_pos.setdefault(t[1], []).append(n)
    other = {}
    for lab, pos in label_pos.items():
        assert len(pos) == 2, (lab, pos)
        other[pos[0]] = pos[1]; other[pos[1]] = pos[0]
    visited = set()
    val = 1
    # paths starting at momenta
    for n, t in enumerate(occ):
        if t[0] == 'p' and n not in visited:
            cur = n
            visited.add(cur)
            while True:
                m = partner[cur]
                visited.add(m)
                if occ[m][0] == 'p':
                    val *= dot(t[1], occ[m][1])
                    break
                cur = other[m]
                visited.add(cur)
    # closed index loops
    for n, t in enumerate(occ):
        if n not in visited:
            cur = n
            visited.add(cur)
            while True:
                m = partner[cur]; visited.add(m)
                cur = other[m]
                if cur in visited:
                    break
                visited.add(cur)
            val *= D
    return val


def trace(tokens, dot):
    tot = 0
    for s, pairs in pair_value_terms(list(tokens)):
        tot += s*contract(pairs, dot)
    return 4*tot

# ---------------------------------------------------------------- kinematics
# momenta: p (gluon/quark in), q (photon), k1 (quark out), k2 (antiquark out), all massless except q^2=-Q2
# express everything through s_hat, t_hat, u_hat:  s+t+u = -Q2 ; z = Q2/(2 p.q)
s, t, u = sp.symbols('s t u')
def make_dot(sv, tv, uv):
    # p.p=0, k1.k1=0, k2.k2=0, q.q=-Q2 ; p.q = (s+Q2)/2 ; p.k1 = -t/2 ; p.k2 = -u/2 ;
    # k1.k2 = s/2 ; q.k1 = p.k2 + k1.k2 - ... use q = k1 + k2 - p
    base = {('p','p'):0, ('k1','k1'):0, ('k2','k2'):0,
            ('p','k1'):-tv/2, ('p','k2'):-uv/2, ('k1','k2'):sv/2}
    def d0(a, b):
        if (a, b) in base: return base[(a, b)]
        if (b, a) in base: return base[(b, a)]
        raise KeyError((a, b))
    # composite momenta as linear combinations
    comp = {'p': {'p':1}, 'k1': {'k1':1}, 'k2': {'k2':1},
            'q': {'k1':1, 'k2':1, 'p':-1},
            'KA': {'p':1, 'k2':-1},   # k1 - q = p - k2
            'KB': {'k1':1, 'p':-1}}   # k1 - p
    def dot(a, b):
        ca, cb = comp[a], comp[b]
        return sp.expand(sum(x*yv*d0(i, j) for i, x in ca.items() for j, yv in cb.items()))
    return dot

dot = make_dot(s, t, u)
assert sp.simplify(dot('q','q').subs(u, -Q2 - s - t) + Q2) == 0

P = lambda n: ('p', n)
I = lambda l: ('i', l)

def gam_amp(mu, rho, which):
    # Gamma^{mu rho} pieces: A = gamma^mu KA gamma^rho / u ; B = gamma^rho KB gamma^mu / t
    return {'A': ([I(mu), P('KA'), I(rho)], u), 'B': ([I(rho), P('KB'), I(mu)], t)}[which]

def gam_conj(nu, sig, which):
    return {'A': ([I(sig), P('KA'), I(nu)], u), 'B': ([I(nu), P('KB'), I(sig)], t)}[which]

def tensor_contract(proj):
    """sum_spins M^mu M^nu* (-g_{rho sigma}) contracted with the projector:
       proj='g'  -> -g_{mu nu};  proj='pp' -> p_mu p_nu.  Returns Dirac part (no couplings)."""
    tot = 0
    for wa in 'AB':
        for wb in 'AB':
            ga, da = gam_amp('mu', 'rho', wa)
            gb, db = gam_conj('nu', 'sig', wb)
            # polarisation sum -g_{rho sigma}: identify sig with rho, overall minus
            gb = [I('rho') if tk == I('sig') else tk for tk in gb]
            if proj == 'g':   # -g_{mu nu}: identify nu with mu, overall minus
                gb2 = [I('mu') if tk == I('nu') else tk for tk in gb]
                toks = [P('k1')] + ga + [P('k2')] + gb2
                val = -(-trace(toks, dot))
            else:             # p_mu p_nu: replace gamma^mu, gamma^nu by pslash
                ga2 = [P('p') if tk == I('mu') else tk for tk in ga]
                gb2 = [P('p') if tk == I('nu') else tk for tk in gb]
                toks = [P('k1')] + ga2 + [P('k2')] + gb2
                val = -trace(toks, dot)
            tot += val/(da*db)
    return sp.simplify(sp.expand(tot).subs(u, -Q2 - s - t))

print("computing D-dimensional traces ...")
Tg = tensor_contract('g')
Tpp = tensor_contract('pp')
print("  (-g_{mu nu}) sum M M*  =", sp.factor(Tg))
print("  (p_mu p_nu)  sum M M*  =", sp.factor(Tpp))

# Compare with the closed forms quoted in research/c_dis §6 (as an independent cross-check of that file):
cdis_g = 8*(1-eps)*((1-eps)*(u/t + t/u) - 2*s*Q2/(t*u) - 2*eps)
cdis_pp = 8*s
chk_g = sp.simplify((Tg - cdis_g.subs(u, -Q2 - s - t)))
chk_pp = sp.simplify((Tpp - cdis_pp))
print("  difference to c_dis closed form (-g):", chk_g, "; (pp):", chk_pp)

# gauge-invariance check: replace eps_rho by k_rho = p_rho -> amplitude contracted must vanish.
# Check via trace: sum_spins (p_rho M^{mu rho}) (p_sigma M^{nu sigma})* contracted with -g_{mu nu} = 0
def ward_check():
    tot = 0
    for wa in 'AB':
        for wb in 'AB':
            ga, da = gam_amp('mu', 'rho', wa)
            gb, db = gam_conj('nu', 'sig', wb)
            ga2 = [P('p') if tk == I('rho') else tk for tk in ga]
            gb2 = [P('p') if tk == I('sig') else tk for tk in gb]
            gb2 = [I('mu') if tk == I('nu') else tk for tk in gb2]
            toks = [P('k1')] + ga2 + [P('k2')] + gb2
            tot += -trace(toks, dot)/(da*db)
    return sp.simplify(sp.expand(tot).subs(u, -Q2 - s - t))
print("  Ward check  sum |p_rho M^{mu rho}|^2 (-g_mu nu)  =", ward_check())

# ---------------------------------------------------------------- phase space and projections
# s_hat = Q2 (1-z)/z ; t = -(s+Q2) y ; u = -(s+Q2)(1-y) ; x -> z (partonic)
sub = {s: Q2*(1-z)/z}
sub_t = {t: -(Q2/z)*y}
Tg_y = sp.simplify(Tg.subs(sub).subs(sub_t))
Tpp_y = sp.simplify(Tpp.subs(sub).subs(sub_t))

# W^{mu nu} = (1/4pi) * avg * colour * g0^2 e_q^2 * Int dPS2 [ ... ]
# dPS2 = (1/8pi) (4pi/s)^eps / Gamma(1-eps) * dy [y(1-y)]^(-eps)
# g0^2 = 4 pi alpha_s mu^(2eps) e^(eps gammaE) (4pi)^(-eps)  ->  combine (4pi/s)^eps (4pi)^-eps mu^2eps = (mu^2/s)^eps
#  => W = alpha_s * e^(eps gE) (mu^2/s)^eps * avg * T_F * (1/(8 pi Gamma(1-eps))) Int dy [y(1-y)]^-eps [ ... ]
# We factor out  (alpha_s/2pi) T_F (mu^2/Q2)^eps e_q^2 and return R such that F2/(z e_q^2) = that * R.
gE = sp.EulerGamma
def proj_integral(expr):
    integrand = sp.simplify(expr*(y*(1-y))**(-eps))
    return integrand

def R2(avg):
    # F2/x = 2/(D-2) [ -g.W + (D-1)(4 z^2/Q2) p.W.p ]
    comb = 2/(D-2)*(Tg_y + (D-1)*(4*z**2/Q2)*Tpp_y)
    comb = sp.simplify(comb)
    # integrate over y with weight [y(1-y)]^-eps: expand comb in powers of y and 1/y, 1/(1-y)
    comb_ap = sp.apart(sp.together(comb), y)
    terms = sp.Add.make_args(sp.expand(comb_ap))
    tot = 0
    for term in terms:
        c, rest = term.as_independent(y)
        # rest is y^a (1-y)^b with integer a,b (possibly negative)
        rest = sp.powsimp(rest)
        a = sp.degree(rest, y) if rest.is_polynomial(y) else None
        # generic: write rest = y^a * (1-y)^b
        a_exp = 0; b_exp = 0
        for f in sp.Mul.make_args(rest):
            base, ex = f.as_base_exp()
            if base == y: a_exp += ex
            elif sp.simplify(base - (1-y)) == 0: b_exp += ex
            elif sp.simplify(base - (y-1)) == 0:
                b_exp += ex; c *= (-1)**ex
            elif base == 1: pass
            else: raise ValueError(("unexpected factor", f))
        tot += c*sp.gamma(1 - eps + a_exp)*sp.gamma(1 - eps + b_exp)/sp.gamma(2 - 2*eps + a_exp + b_exp)
    # prefactor: alpha_s e^{eps gE} (mu^2/s)^eps avg T_F /(8 pi Gamma(1-eps)) ; W normalisation 1/(4 pi) included?
    # F2/x itself is built from W; W includes 1/(4pi). So F2/x = (1/4pi)*avg*T_F*g0^2*(1/(8 pi Gamma(1-eps)))(4pi/s)^eps * tot
    # with g0^2 (4pi/s)^eps = 4 pi alpha_s e^{eps gE} (mu^2/s)^eps:
    # F2/x = alpha_s e^{eps gE} (mu^2/s)^eps avg T_F tot /(8 pi Gamma(1-eps))
    # = (alpha_s/2pi) T_F (mu^2/Q2)^eps * [ e^{eps gE} (z/(1-z))^eps avg tot / (4 Gamma(1-eps)) ]
    return sp.exp(eps*gE)*(z/(1-z))**eps*avg*tot/(4*sp.gamma(1-eps))

R_D2 = sp.simplify(R2(1/(D-2)))
R_2 = sp.simplify(R2(sp.Rational(1, 2)))

# c_dis closed form for comparison
R_cdis = 2*sp.exp(eps*gE)*sp.gamma(-eps)/sp.gamma(2-2*eps)*(z/(1-z))**eps*(z**2+(1-z)**2-3*eps+4*eps**2-2*eps**3)/(1-eps)**2
zt = sp.Rational(3, 10)
for e_ in [sp.Rational(-1, 7), sp.Rational(1, 9)]:
    v1 = sp.N(R_D2.subs({z: zt, eps: e_}), 25); v2 = sp.N(R_cdis.subs({z: zt, eps: e_}), 25)
    print(f"  R_2^g(avg 1/(D-2)) at z=0.3, eps={e_}: mine {v1}  c_dis {v2}  diff {sp.N(v1-v2, 5)}")

Pqg = z**2 + (1-z)**2
def finite_part(R):
    ser = sp.series(R, eps, 0, 1).removeO()
    pole = sp.simplify(ser.coeff(eps, -1))
    fin = sp.simplify(ser.coeff(eps, 0))
    return pole, fin

pole_D2, fin_D2 = finite_part(R_D2)
pole_2, fin_2 = finite_part(R_2)
print("avg 1/(D-2):  pole coeff =", sp.factor(pole_D2), " ; finite =", sp.simplify(fin_D2))
print("avg 1/2    :  pole coeff =", sp.factor(pole_2), " ; finite =", sp.simplify(fin_2))
# MS-bar: R = -(2/eps) Pqg + 2 C_2^g  (counterterm f_{q/g}+f_{qbar/g} = -(alpha_s/2pi)(2/eps)Pqg)
C_D2 = sp.simplify(fin_D2/2)
C_2 = sp.simplify(fin_2/2)
C_std = Pqg*sp.log((1-z)/z) - 1 + 8*z*(1-z)
print("pole = -2 Pqg (both)?", sp.simplify(pole_D2 + 2*Pqg) == 0, sp.simplify(pole_2 + 2*Pqg) == 0)
def fixlog(e):
    # 0<z<1: log(-1/(z-1)) = -log(1-z); compare symbolically after the replacement and numerically
    return sp.simplify(sp.expand_log(e.replace(sp.log(-1/(z-1)), -sp.log(1-z)), force=True))
d1 = fixlog(C_D2 - C_std); d2 = fixlog(C_2 - C_std - Pqg)
num1 = max(abs(sp.N((C_D2 - C_std).subs(z, zz), 30)) for zz in [sp.Rational(1,10), sp.Rational(3,10), sp.Rational(7,10), sp.Rational(9,10)])
num2 = max(abs(sp.N((C_2 - C_std - Pqg).subs(z, zz), 30)) for zz in [sp.Rational(1,10), sp.Rational(3,10), sp.Rational(7,10), sp.Rational(9,10)])
print("C_2^g [1/(D-2)] - standard =", d1, "; numerical max |diff| on z=0.1,0.3,0.7,0.9:", num1)
print("C_2^g [1/2] - standard - Pqg =", d2, "; numerical max |diff|:", num2)
# F_L (finite, convention independent at O(eps^0))
FL = lambda avg: sp.simplify(sp.series(sp.exp(eps*gE)*(z/(1-z))**eps*avg/(4*sp.gamma(1-eps)) *
                    sp.integrate(sp.expand((8*z**2/Q2)*Tpp_y), (y, 0, 1)), eps, 0, 1).removeO().coeff(eps, 0))
print("F_L^g/(z e_q^2) finite part (avg 1/(D-2)) =", sp.factor(FL(1/(D-2))), " ; (avg 1/2) =", sp.factor(FL(sp.Rational(1, 2))))
ok = (d1 == 0) and (d2 == 0) and num1 < 1e-25 and num2 < 1e-25
print("RESULT:", "PASS" if ok else "FAIL",
      "- standard MS-bar C_g corresponds to the 1/(D-2)=1/[2(1-eps)] gluon average; the 1/2 average adds +P_qg")
