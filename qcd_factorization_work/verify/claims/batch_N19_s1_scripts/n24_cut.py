"""
n24_cut.py -- independent check of the exact-in-eps O(alpha_s) cutting identity 2(D-1) s Im Pi^(1)_bare = rho_V + rho_R
and of Pi_MSbar at two loops (claim N24).  Own D-dimensional trace code (not the project's diracD.py).
 LHS: two-loop massless vector correlator exact in d from Grozin, hep-ph/0508242, eq. (Photon2:Pi) (QED photon self-energy;
      mapping Pi_here = -Pi_Grozin/e0^2, e0^4 -> e0^2 g0^2 C_F N_c e_q^2).
 RHS: rho_V from the exact one-loop form factor (derived here with Feynman parameters + own traces),
      rho_R from the D-dim matrix element (own traces) and the D-dim 3-body phase space (normalisation checked by recursion).
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
mp.mp.dps = 40
RES = []
def check(name, ok, info=''):
    RES.append(bool(ok)); print(('PASS ' if ok else 'FAIL ') + name + (('   [' + info + ']') if info else ''), flush=True)
D = sp.Symbol('D'); e = sp.Symbol('epsilon')

# ------------------------------------------------------------------ own D-dimensional trace engine
VECS = set()
def is_vec(a): return a in VECS
def pair(a, b):
    if is_vec(a) and is_vec(b): return ('d',) + tuple(sorted((a, b)))
    if is_vec(a): return ('c', a, b)
    if is_vec(b): return ('c', b, a)
    return ('g',) + tuple(sorted((a, b)))
def trace(seq):
    """Tr[seq] with Tr 1 = 4; returns list of (coeff, [factors])"""
    if len(seq) == 0: return [(4, [])]
    if len(seq) % 2: return []
    out = []
    a1 = seq[0]
    for k in range(1, len(seq)):
        sign = 1 if k % 2 == 1 else -1
        rest = seq[1:k] + seq[k + 1:]
        for c, fs in trace(rest):
            out.append((sign*c, fs + [pair(a1, seq[k])]))
    return out
def contract(fs):
    """contract repeated Lorentz indices; returns (coeff_sym, remaining factors)"""
    fs = list(fs); coeff = sp.Integer(1); changed = True
    while changed:
        changed = False
        idx_count = {}
        for f in fs:
            if f[0] == 'c': idx_count.setdefault(f[2], []).append(f)
            elif f[0] == 'g':
                idx_count.setdefault(f[1], []).append(f); idx_count.setdefault(f[2], []).append(f)
        for idx, lst in idx_count.items():
            if len(lst) == 1: continue
            # self-contraction g(i,i)
            f = lst[0]
            if f[0] == 'g' and f[1] == f[2]:
                fs.remove(f); coeff *= D; changed = True; break
            f1, f2 = lst[0], lst[1]
            if f1 is f2: continue
            fs.remove(f1); fs.remove(f2)
            def other(f, i):
                if f[0] == 'c': return ('v', f[1])
                return ('i', f[2] if f[1] == i else f[1])
            o1, o2 = other(f1, idx), other(f2, idx)
            if o1[0] == 'v' and o2[0] == 'v': fs.append(pair(o1[1], o2[1]))
            elif o1[0] == 'v': fs.append(pair(o1[1], o2[1]))
            elif o2[0] == 'v': fs.append(pair(o2[1], o1[1]))
            else: fs.append(pair(o1[1], o2[1]))
            changed = True; break
    return coeff, fs
def evaluate(terms, dots):
    tot = 0
    for c, fs in terms:
        cf, rem = contract(fs)
        val = sp.Integer(c)*cf
        for f in rem:
            assert f[0] == 'd', ('uncontracted', f)
            val *= dots[(f[1], f[2])]
        tot += val
    return sp.expand(tot)
def tr_lin(seq_with_lin, dots):
    """seq elements may be dicts {vector: coefficient} for linear combinations"""
    choices = []
    for el in seq_with_lin:
        if isinstance(el, dict): choices.append(list(el.items()))
        else: choices.append([(el, 1)])
    tot = 0
    for combo in itertools.product(*choices):
        seq = [c[0] for c in combo]; cf = sp.prod([c[1] for c in combo])
        tot += cf*evaluate(trace(seq), dots)
    return sp.expand(tot)
# self-test: Tr[a b c d] and gamma^mu a gamma_mu = -(D-2) a
VECS.update(['a', 'b', 'cc', 'dd'])
sa, sb, sc_, sd = sp.symbols('ab ac ad bc')
dots_t = {('a', 'b'): sa, ('a', 'cc'): sb, ('a', 'dd'): sc_, ('b', 'cc'): sd, ('b', 'dd'): sp.Symbol('bdd'), ('cc', 'dd'): sp.Symbol('cdd'),
          ('a', 'a'): sp.Symbol('aa'), ('b', 'b'): sp.Symbol('bb')}
t4 = evaluate(trace(['a', 'b', 'cc', 'dd']), dots_t)
check('trace engine: Tr[a b c d] = 4[(ab)(cd) - (ac)(bd) + (ad)(bc)]', sp.simplify(t4 - 4*(sa*sp.Symbol('cdd') - sb*sp.Symbol('bdd') + sc_*sd)) == 0)
t_mu = evaluate(trace(['mu', 'a', 'mu', 'b']), dots_t)
check('trace engine: Tr[g^mu a g_mu b] = -(D-2) Tr[a b]', sp.simplify(t_mu + (D - 2)*4*sa) == 0)

# ------------------------------------------------------------------ LO and real emission matrix elements
VECS.update(['p1', 'p2', 'k', 'l'])
s, y12, y13, y23 = sp.symbols('s y12 y13 y23', positive=True)
dots = {('p1', 'p1'): 0, ('p2', 'p2'): 0, ('k', 'k'): 0, ('p1', 'p2'): s*y12/2, ('k', 'p1'): s*y13/2, ('k', 'p2'): s*y23/2}
# LO: -g_{mu nu} sum u gamma^mu v vbar gamma^nu u = -Tr[p1 g^mu p2 g_mu]
lo = -evaluate(trace(['p1', 'mu', 'p2', 'mu']), {('p1', 'p2'): s/2, ('p1', 'p1'): 0, ('p2', 'p2'): 0})
check('LO: -g_{mu nu} Tr[p1 g^mu p2 g^nu] = 2(D-2) s', sp.simplify(lo - 2*(D - 2)*s) == 0)
# real: Gamma^{alpha mu} = g^al (p1+k) g^mu / s13 - g^mu (p2+k) g^al / s23 ; contract with -g_{mu nu} and polarisation sum -g_{al be}
P1K = {'p1': 1, 'k': 1}; P2K = {'p2': 1, 'k': 1}
s13, s23 = s*y13, s*y23
# M^mu Mbar_mu with both metric contractions: overall (+1) from (-g)(-g)
T11 = tr_lin(['p1', 'al', P1K, 'mu', 'p2', 'mu', P1K, 'al'], dots)/s13**2
T22 = tr_lin(['p1', 'mu', P2K, 'al', 'p2', 'al', P2K, 'mu'], dots)/s23**2
T12 = tr_lin(['p1', 'al', P1K, 'mu', 'p2', 'al', P2K, 'mu'], dots)/(s13*s23)   # Tr[p1 G1 p2 Gbar2], Gbar2 = reversed of G2 = g^al (p2+k) g^mu
T21 = tr_lin(['p1', 'mu', P2K, 'al', 'p2', 'mu', P1K, 'al'], dots)/(s13*s23)
real = sp.together(sp.expand((T11 + T22 - T12 - T21).subs(y12, 1 - y13 - y23)))
print('real-emission traces done', flush=True)
CF, Nc, eq2, g02 = sp.symbols('C_F N_c e_q2 g_0^2', positive=True)
claim34 = 8*(1 - e)*((1 - e)*(y13/y23 + y23/y13) + 2*y12/(y13*y23) - 2*e)
diff = sp.cancel(sp.together(real.subs(D, 4 - 2*e) - claim34.subs(y12, 1 - y13 - y23)))
check('real emission: -g_{mu nu} sum M^mu M^nu* = 8(1-eps) g0^2 C_F N_c e_q^2 [(1-eps)(y13/y23+y23/y13) + 2 y12/(y13 y23) - 2 eps]  (c_ee 3.4)', diff == 0)

# ------------------------------------------------------------------ 3-body phase space normalisation (recursion)
eps_v = mp.mpf('0.137'); Dv = 4 - 2*eps_v; sv = mp.mpf(1)
Om = lambda n: 2*mp.pi**(n/2)/mp.gamma(n/2)     # solid angle in n dimensions (sphere S^{n-1})
def Phi2(S, m2):    # two-body: one massive (m2), one massless; = Omega_{D-1} p^{D-3}/(4 (2pi)^{D-2} sqrt S)
    p = (S - m2)/(2*mp.sqrt(S))
    return Om(Dv - 1)*p**(Dv - 3)/(4*(2*mp.pi)**(Dv - 2)*mp.sqrt(S))
Phi3_rec = mp.quad(lambda M2: Phi2(sv, M2)*Phi2(M2, 0)/(2*mp.pi), [0, sv])
Phi3_formula = sv**(1 - 2*eps_v)*(4*mp.pi)**(2*eps_v - 3)/(2*mp.gamma(2 - 2*eps_v))*mp.gamma(1 - eps_v)**3/mp.gamma(3 - 3*eps_v)
check('3-body phase space: d Phi_3 = (4pi)^{2eps-3} s^{1-2eps}/(2 Gamma(2-2eps)) dy13 dy23 (y12 y13 y23)^{-eps}: total volume = recursion',
      abs(Phi3_rec/Phi3_formula - 1) < 1e-25, 'ratio %s' % mp.nstr(Phi3_rec/Phi3_formula, 20))
check('2-body massless: Phi_2 = (1/8pi)(4pi/s)^eps Gamma(1-eps)/Gamma(2-2eps)',
      abs(Phi2(sv, 0) - (1/(8*mp.pi))*(4*mp.pi/sv)**eps_v*mp.gamma(1 - eps_v)/mp.gamma(2 - 2*eps_v)) < 1e-30)

# ------------------------------------------------------------------ one-loop vertex, exact in eps (own derivation)
L2, lp1, lp2 = sp.symbols('L2 lp1 lp2')
dv = {('p1', 'p1'): 0, ('p2', 'p2'): 0, ('p1', 'p2'): s/2, ('l', 'l'): L2, ('l', 'p1'): lp1, ('l', 'p2'): lp2}
P1mL = {'p1': 1, 'l': -1}; mP2mL = {'p2': -1, 'l': -1}
num = tr_lin(['p1', 'al', P1mL, 'mu', mP2mL, 'al', 'p2', 'mu'], dv)
den = evaluate(trace(['p1', 'mu', 'p2', 'mu']), dv)
# express via denominators: Da = l^2, Db = (p1-l)^2 = l^2 - 2 l.p1, Dc = (p2+l)^2 = l^2 + 2 l.p2
Da, Db, Dc = sp.symbols('Da Db Dc')
numD = sp.expand(num.subs({L2: Da, lp1: (Da - Db)/2, lp2: (Dc - Da)/2}))
poly = sp.Poly(numD, Da, Db, Dc)
# integrals J(a,b,c) = int d^Dl/(2pi)^D Da^-a Db^-b Dc^-c ; with numerator monomials Da^i Db^j Dc^k -> J(1-i,1-j,1-k)
# non-vanishing (non-scaleless) ones: J(1,1,1), J(0,1,1), J(-1,1,1) = -(s/2) J(0,1,1); others with b<=0 or c<=0 are scaleless (p1^2=p2^2=0)
G = lambda a, b: sp.gamma(a + b - D/2)*sp.gamma(D/2 - a)*sp.gamma(D/2 - b)/(sp.gamma(a)*sp.gamma(b)*sp.gamma(D - a - b))
X = sp.Symbol('X')   # X = (-s - i0)
J111 = -sp.I/(4*sp.pi)**(D/2)*sp.gamma(1 + e)*sp.gamma(-e)**2/sp.gamma(1 - 2*e)*X**(-1 - e)     # Feynman parameters (derived in the report)
J011 = sp.I/(4*sp.pi)**(D/2)*G(1, 1)*X**(-e)
Jm111 = -s/2*J011
def Jint(a, b, c):
    if (a, b, c) == (1, 1, 1): return J111
    if (a, b, c) == (0, 1, 1): return J011
    if (a, b, c) == (-1, 1, 1): return Jm111
    if b <= 0 or c <= 0: return 0
    raise ValueError((a, b, c))
amp = 0
for (i, j, k), cf in poly.terms():
    amp += cf*Jint(1 - i, 1 - j, 1 - k)
# vertex Lambda^mu = -i g0^2 C_F int [...] / (Da Db Dc): Feynman rules (i g gamma t)(i S)(gamma^mu)(i S)(i g gamma t)(-i/l^2) -> -i g^2 C_F
F1expr = (-sp.I*g02*CF*amp/den)
alpha = g02/(4*sp.pi)
cG = sp.gamma(1 + e)*sp.gamma(1 - e)**2/sp.gamma(1 - 2*e)
F1_claim = -(alpha*CF/(4*sp.pi))*(4*sp.pi/(-s))**e*cG*(2 - e + 2*e**2)/(e**2*(1 - 2*e))   # (4 pi mu0^2/(-q^2))^eps, q^2 = s (spacelike s<0 here)
for ev in [sp.Rational(1, 7), sp.Rational(-2, 9), sp.Rational(3, 10)]:
    sub = {D: 4 - 2*ev, e: ev, X: 3, s: -3, g02: 1, CF: 1}
    r = sp.N(F1expr.subs(sub), 35)/sp.N(F1_claim.subs(sub), 35)
    check('one-loop form factor (own traces + Feynman-parameter integrals) = -(a_s C_F/4pi)(4pi mu0^2/(-q^2))^eps c_Gamma (2-e+2e^2)/(e^2(1-2e)), eps=%s' % ev,
          abs(r - 1) < 1e-25, 'ratio %s' % sp.N(r, 20))
# ------------------------------------------------------------------ assemble both sides, exact in eps
def rhs_lhs(ev, sval=mp.mpf(3), g2=mp.mpf(1)):
    E = mp.mpf(ev); Dd = 4 - 2*E
    Gm = lambda a, b: mp.gamma(a + b - Dd/2)*mp.gamma(Dd/2 - a)*mp.gamma(Dd/2 - b)/(mp.gamma(a)*mp.gamma(b)*mp.gamma(Dd - a - b))
    cGv = mp.gamma(1 + E)*mp.gamma(1 - E)**2/mp.gamma(1 - 2*E)
    # LO
    Phi2v = (1/(8*mp.pi))*(4*mp.pi/sval)**E*mp.gamma(1 - E)/mp.gamma(2 - 2*E)
    rho0 = 2*(Dd - 2)*sval*Phi2v                         # per N_c e_q^2
    # virtual: 2 Re F^(1)(s+i0) = 2 Re[(-s-i0)^(-eps)] ... = 2 cos(pi eps) x (spacelike form at |q^2| = s)
    F1s = -(g2/(4*mp.pi)/(4*mp.pi))*(4*mp.pi/sval)**E*cGv*(2 - E + 2*E**2)/(E**2*(1 - 2*E))
    rhoV = rho0*2*mp.cos(mp.pi*E)*F1s*CFv
    # real: integrate the D-dim matrix element over the 3-body phase space (Dirichlet integrals)
    def dirichlet(a, b, c): return mp.gamma(a)*mp.gamma(b)*mp.gamma(c)/mp.gamma(a + b + c)
    # integrand (y12 y13 y23)^{-eps} * [(1-eps)(y13/y23 + y23/y13) + 2 y12/(y13 y23) - 2 eps]
    Iy = (1 - E)*2*dirichlet(1 - E, 2 - E, -E) + 2*dirichlet(2 - E, -E, -E) - 2*E*dirichlet(1 - E, 1 - E, 1 - E)
    Phi3pref = (4*mp.pi)**(2*E - 3)*sval**(1 - 2*E)/(2*mp.gamma(2 - 2*E))
    rhoR = 8*(1 - E)*g2*CFv*Phi3pref*Iy
    # LHS from Grozin's d-dimensional two-loop result
    r1 = -4*(1 - E)*(2 - E + 2*E**2)/(E*(3 - 2*E))
    G11 = Gm(1, 1); G1e = Gm(1, E)
    # Grozin: Pi_G2 = e0^4 (-p^2)^{-2eps}/(4pi)^d * 2(d-2)/((d-1)(d-4)) [ -(d^2-7d+16) G1^2 + 4 (d-3)(d^2-4d+8)/(d-4) G2 ],  G2 = G(1,1) G(1,eps)
    bracketG = 2*(Dd - 2)/((Dd - 1)*(Dd - 4))*(-(Dd**2 - 7*Dd + 16)*G11**2 + 4*(Dd - 3)*(Dd**2 - 4*Dd + 8)/(Dd - 4)*G11*G1e)
    Pi_here_over = -bracketG*g2*CFv/(4*mp.pi)**Dd        # Pi_here = -Pi_G/e0^2 with e0^2 -> g0^2 C_F (per N_c e_q^2), times (Q^2)^{-2eps}
    ImPi = Pi_here_over*sval**(-2*E)*mp.sin(2*mp.pi*E)   # (Q^2)^{-2eps} = s^{-2eps} e^{2 i pi eps}
    lhs = 2*(Dd - 1)*sval*ImPi
    # also: LO consistency 2(D-1) s Im Pi^(0) = rho0 with Pi^(0) = (Q^2)^{-eps}/(4pi)^{D/2} 2(D-2)/(D-1) G(1,1)
    ImPi0 = sval**(-E)*mp.sin(mp.pi*E)/(4*mp.pi)**(Dd/2)*2*(Dd - 2)/(Dd - 1)*G11
    lo_ok = abs(2*(Dd - 1)*sval*ImPi0/rho0 - 1)
    # c_ee's r1, r2 representation for comparison
    r2 = 16*(1 - E)*(1 - 2*E)*(2 - 2*E + E**2)/(E*(3 - 2*E)*(2 - 3*E))
    Gpe = Gm(1 + E, 1)
    cee = (r1*G11**2 + r2*G11*Gpe)*g2*CFv/(4*mp.pi)**Dd
    return lhs, rhoV, rhoR, lo_ok, cee, Pi_here_over, r1*G11**2*g2*CFv/(4*mp.pi)**Dd, r2*G11*Gpe*g2*CFv/(4*mp.pi)**Dd
CFv = mp.mpf(4)/3
for ev in ['0.1', '-0.2', '0.31', '-0.43', '0.0123']:
    lhs, rV, rR, lo_ok, cee, piG, t1, t2 = rhs_lhs(ev)
    E = mp.mpf(ev)
    check('eps=%s: LO normalisation 2(D-1) s Im Pi^(0) = rho_0' % ev, lo_ok < 1e-30)
    check('eps=%s: Grozin d-dim two-loop result == c_ee (4.1) r1 G11^2 + r2 G11 G(1+eps,1)' % ev, abs(piG/cee - 1) < 1e-30)
    check('eps=%s: 2(D-1) s Im Pi^(1)_bare = rho_V + rho_R  (exact in eps, 30 digits)' % ev, abs(lhs/(rV + rR) - 1) < 1e-30, 'ratio %s' % mp.nstr(lhs/(rV + rR), 25))
    # termwise: G11^2 term <-> virtual, G11 G(1+eps,1) term <-> real
    sfac = 2*(4 - 2*E - 1)*3*mp.mpf(3)**(-2*E)*mp.sin(2*mp.pi*E)
    check('eps=%s: termwise: Im[r1 G11^2 term] <-> rho_V, Im[r2 G11 G(1+eps,1) term] <-> rho_R' % ev,
          abs(sfac*t1/rV - 1) < 1e-28 and abs(sfac*t2/rR - 1) < 1e-28)

# MSbar expansion: see n24_msbar.py (Laurent coefficients by contour integration; symbolic series was too slow)
print('\nSUMMARY n24: %d/%d PASS' % (sum(RES), len(RES)))
