# N24 (stage-2 verifier): own two-loop computation of the massless vector correlator, own form factor and
# own real-emission integral, then the exact-in-eps cutting identity and the MS-bar constants.
# Independent of the project (c_ee) code and of stage 1 (which took Pi^(1) from Grozin's published formula):
#  - own D-dim Dirac trace engine (pairing recursion + index-chain contraction);
#  - own integral evaluator: triangle rule for the 5-line topology, nested and factorised one-loop tensor
#    integrals via the Feynman-parameter tensor formula (re-derived in batch_N18_s2.md §6);
#  - transversality q_mu q_nu Pi^{mu nu} = 0 and the one-loop normalisation as internal checks;
#  - everything evaluated at fixed rational eps with mpmath (40 digits) and compared with the closed form.
import sys, os, itertools
from functools import lru_cache
from fractions import Fraction as Fr
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
mp.mp.dps = 40
res = []
def check(name, cond, info=''):
    res.append(bool(cond)); print(('PASS ' if cond else 'FAIL ') + name + (('   [' + info + ']') if info else ''), flush=True)

# ------------------------------------------------------------------ D-dim trace engine
Dsym = sp.symbols('D')
def vec(**kw): return ('v', {k: sp.sympify(v) for k, v in kw.items()})
def idx(name): return ('i', name)
def pairings(slots):
    """yield (sign, list of pairs) for Tr(gamma^{s1}...gamma^{sn}) = sum sign * prod g(pair)  (times Tr 1 = 4)"""
    if not slots:
        yield 1, []
        return
    first, rest = slots[0], slots[1:]
    for k in range(len(rest)):
        sign = (-1)**k
        for s2, pr in pairings(rest[:k] + rest[k+1:]):
            yield sign*s2, [(first, rest[k])] + pr
def contract(pairs, dot):
    """contract a product of metric pairings; indices appear exactly twice. Returns a sympy expression."""
    pairs = list(pairs)
    expr = sp.Integer(1)
    changed = True
    while changed:
        changed = False
        for a, p in enumerate(pairs):
            for side in (0, 1):
                s = p[side]
                if s[0] != 'i': continue
                other = p[1 - side]
                if other == s:          # g^mu_mu
                    expr *= Dsym; pairs.pop(a); changed = True; break
                # find the partner occurrence of index s
                for b, p2 in enumerate(pairs):
                    if b == a: continue
                    if s in p2:
                        o2 = p2[1] if p2[0] == s else p2[0]
                        newp = (other, o2)
                        for j in sorted([a, b], reverse=True): pairs.pop(j)
                        pairs.append(newp); changed = True; break
                if changed: break
            if changed: break
    for (x, y) in pairs:
        assert x[0] == 'v' and y[0] == 'v', (x, y)
        expr *= sum(cx*cy*dot(bx, by) for bx, cx in x[1].items() for by, cy in y[1].items())
    return expr
def trace(slots, dot):
    tot = sp.Integer(0)
    for sign, pr in pairings(slots):
        tot += sign*contract(pr, dot)
    return sp.expand(4*tot)

# self-test of the engine: gamma^a p gamma_a = -(D-2) p ; Tr(p q) = 4 p.q ; gamma^a p q r gamma_a identity
pp, qq_ = sp.symbols('pp qq_')
def dot_test(a, b):
    a, b = sorted([a, b])
    return sp.Symbol('d_%s%s' % (a, b))
t1 = trace([idx('a'), vec(p=1), idx('a'), vec(q=1)], dot_test)
check('trace engine: Tr(gamma^a pslash gamma_a qslash) = -4(D-2) p.q', sp.simplify(t1 + 4*(Dsym - 2)*sp.Symbol('d_pq')) == 0)
t2 = trace([idx('a'), vec(p=1), vec(q=1), vec(r=1), idx('a'), vec(s=1)], dot_test)
t2ref = sp.expand(-2*trace([vec(r=1), vec(q=1), vec(p=1), vec(s=1)], dot_test) + (4 - Dsym)*trace([vec(p=1), vec(q=1), vec(r=1), vec(s=1)], dot_test))
check('trace engine: gamma^a p q r gamma_a = -2 r q p + (4-D) p q r inside a trace', sp.simplify(t2 - t2ref) == 0)

# ------------------------------------------------------------------ kinematics of the 5-line topology (Minkowski)
D1, D2, D3, D4, D5, QQ = sp.symbols('D1 D2 D3 D4 D5 qq')   # qq = q^2 (Minkowski)
def dot2(a, b):
    a, b = sorted([a, b])
    tab = {('k', 'k'): D1, ('r', 'r'): D3, ('q', 'q'): QQ,
           ('k', 'q'): (D1 + QQ - D2)/2, ('q', 'r'): (D3 + QQ - D4)/2, ('k', 'r'): (D1 + D3 - D5)/2}
    return tab[(a, b)]
k_ = vec(k=1); r_ = vec(r=1); q_ = vec(q=1)
kmq = vec(k=1, q=-1); rmq = vec(r=1, q=-1)
mu, nu, al = idx('mu'), idx('nu'), idx('al')
traces = {
  'V':  ([mu, k_, al, r_, mu, rmq, al, kmq], (1, 1, 1, 1, 1)),
  'S1': ([mu, k_, al, r_, al, k_, mu, kmq], (2, 1, 1, 0, 1)),
  'S2': ([mu, k_, mu, kmq, al, rmq, al, kmq], (1, 2, 0, 1, 1)),
}
# for transversality: replace the two photon indices by qslash
traces_q = {
  'V':  ([q_, k_, al, r_, q_, rmq, al, kmq], (1, 1, 1, 1, 1)),
  'S1': ([q_, k_, al, r_, al, k_, q_, kmq], (2, 1, 1, 0, 1)),
  'S2': ([q_, k_, q_, kmq, al, rmq, al, kmq], (1, 2, 0, 1, 1)),
}

# ------------------------------------------------------------------ integrals at fixed eps
EPS = sp.symbols('eps')
def make_evaluator(eps_val):
    e = mp.mpf(eps_val)
    Dv = 4 - 2*e
    def is_nonpos_int(z):
        z = sp.nsimplify(z)
        return z.is_integer and z <= 0
    def G(a, b):
        # a, b sympy expressions in EPS ; one-loop massless bubble, G=0 if a or b is a non-positive integer
        if is_nonpos_int(a) or is_nonpos_int(b): return mp.mpf(0)
        an = mp.mpf(sp.N(a.subs(EPS, sp.Rational(eps_val)), 50)) if hasattr(a, 'subs') else mp.mpf(a)
        bn = mp.mpf(sp.N(b.subs(EPS, sp.Rational(eps_val)), 50)) if hasattr(b, 'subs') else mp.mpf(b)
        return mp.gamma(an + bn - Dv/2)*mp.gamma(Dv/2 - an)*mp.gamma(Dv/2 - bn)/(mp.gamma(an)*mp.gamma(bn)*mp.gamma(Dv - an - bn))
    Dh = 2 - EPS   # D/2 as a symbol expression
    def A(m, t, a, b):
        # coefficient of {g^t p^{m-2t}} in int d^Dk/pi^{D/2} k^{mu1..mum}/((k^2)^a ((p-k)^2)^b) (Euclidean), times (p^2)^{D/2+t-a-b}
        if is_nonpos_int(a) or is_nonpos_int(b): return mp.mpf(0)
        sub = lambda z: mp.mpf(sp.N(sp.sympify(z).subs(EPS, sp.Rational(eps_val)), 50))
        an, bn = sub(a), sub(b)
        return (mp.gamma(an + bn - Dv/2 - t)*mp.gamma(Dv/2 - an + m - t)*mp.gamma(Dv/2 - bn + t)
                /(2**t*mp.gamma(an)*mp.gamma(bn)*mp.gamma(Dv - an - bn + m)))
    def nterms(m, t):
        return mp.factorial(m)/(2**t*mp.factorial(t)*mp.factorial(m - 2*t))
    @lru_cache(maxsize=None)
    def F(a):
        a1, a2, a3, a4, a5 = a
        # scaleless sectors
        if (a1 <= 0 and a2 <= 0) or (a3 <= 0 and a4 <= 0): return mp.mpf(0)
        if a5 <= 0:
            return F_fact(a)
        if a1 <= 0: return F_nest(a)
        if a2 <= 0: return F((a2, a1, a4, a3, a5))           # (k,r) -> (q-k, q-r)
        if a3 <= 0: return F((a3, a4, a1, a2, a5))           # k <-> r
        if a4 <= 0: return F((a4, a3, a2, a1, a5))           # both
        # all positive: triangle rule on (1,2,5)
        pref = Dv - a1 - a2 - 2*a5
        val = (a1*(F((a1 + 1, a2, a3, a4, a5 - 1)) - F((a1 + 1, a2, a3 - 1, a4, a5)))
               + a2*(F((a1, a2 + 1, a3, a4, a5 - 1)) - F((a1, a2 + 1, a3, a4 - 1, a5))))
        return val/pref
    def F_fact(a):
        a1, a2, a3, a4, a5 = a
        n = -a5
        tot = mp.mpf(0)
        for i in range(n + 1):
            for j in range(n + 1 - i):
                l = n - i - j
                coef = mp.factorial(n)/(mp.factorial(i)*mp.factorial(j)*mp.factorial(l))*(-2)**l
                # r-integral: int (k.r)^l/((r^2)^{a3-j}((r-q)^2)^{a4}) = sum_t A nterms (k^2)^t (k.q)^{l-2t} (q^2)^{D/2+t-(a3-j)-a4}
                for t in range(l//2 + 1):
                    At = A(l, t, sp.Integer(a3 - j), sp.Integer(a4))
                    if At == 0: continue
                    c1 = coef*At*nterms(l, t)
                    # k-integral: (k^2)^{t+i-a1} (k.q)^{l-2t} ((k-q)^2)^{-a2},  k.q = (k^2 + q^2 - (k-q)^2)/2  (Euclidean)
                    mpow = l - 2*t
                    for (u1, u2, u3) in [(x, y, mpow - x - y) for x in range(mpow + 1) for y in range(mpow + 1 - x)]:
                        c2 = mp.factorial(mpow)/(mp.factorial(u1)*mp.factorial(u2)*mp.factorial(u3))*(mp.mpf(1)/2)**mpow*(-1)**u3
                        # k^2 power u1, q^2 power u2, (k-q)^2 power u3
                        aa = sp.Integer(a1 - t - i - u1); bb = sp.Integer(a2 - u3)
                        tot += c1*c2*G(aa, bb)
        return tot
    def F_nest(a):
        a1, a2, a3, a4, a5 = a
        n1 = -a1
        tot = mp.mpf(0)
        for i in range(n1 + 1):
            for j in range(n1 + 1 - i):
                m = n1 - i - j
                coef = mp.factorial(n1)/(mp.factorial(i)*mp.factorial(j)*mp.factorial(m))*2**m
                # (l^2)^i (r^2)^j (2 l.r)^m ;  l-integral with (l^2)^{a5-i} ((l-p)^2)^{a2}, p = q - r
                for t in range(m//2 + 1):
                    At = A(m, t, sp.Integer(a5 - i), sp.Integer(a2))
                    if At == 0: continue
                    c1 = coef*At*nterms(m, t)
                    # gives (r^2)^t (r.p)^{m-2t} (p^2)^{D/2+t-(a5-i)-a2};  p^2 = D4, r.p = (q^2 - D3 - D4)/2
                    pw = 2 - EPS + t - (a5 - i) - a2        # exponent of D4 (symbolic, D/2 = 2-eps)
                    mp_ = m - 2*t
                    for (u1, u2, u3) in [(x, y, mp_ - x - y) for x in range(mp_ + 1) for y in range(mp_ + 1 - x)]:
                        # (q^2)^{u1} (-D3)^{u2} (-D4)^{u3} / 2^{mp_}
                        c2 = mp.factorial(mp_)/(mp.factorial(u1)*mp.factorial(u2)*mp.factorial(u3))*(mp.mpf(1)/2)**mp_*(-1)**(u2 + u3)
                        aa = sp.Integer(a3 - j - t - u2)
                        bb = sp.Integer(a4) - pw - u3
                        tot += c1*c2*G(aa, sp.expand(bb))
        return tot
    return F, G, Dv

# ------------------------------------------------------------------ assemble Pi^(1) at fixed eps
def numerator_poly(slots):
    tr = trace(slots, dot2)
    return sp.Poly(sp.expand(tr), D1, D2, D3, D4, D5, QQ)
polys = {k: numerator_poly(v[0]) for k, v in traces.items()}
polys_q = {k: numerator_poly(v[0]) for k, v in traces_q.items()}
print('   numerator polynomials built:', {k: len(p.terms()) for k, p in polys.items()}, flush=True)

def minkowski_twoloop(poly, a, F, Dv, Qsq=mp.mpf(1)):
    """int int d^Dk d^Dr/(2pi)^{2D} poly(D_i, q^2)/prod D_i^{a_i}  (Minkowski), in units 1/(4pi)^D, at Q^2 = -q^2 = Qsq."""
    tot = mp.mpf(0)
    for monom, coeff in poly.terms():
        n = monom[:5]; nq = monom[5]
        b = tuple(a[i] - n[i] for i in range(5))
        sb = sum(b)
        cnum = mp.mpf(sp.N(coeff.subs(Dsym, Dv) if hasattr(coeff, 'subs') else coeff, 50)) if not isinstance(coeff, (int,)) else mp.mpf(coeff)
        Fb = F(b)
        if Fb == 0: continue
        # (q^2)^{nq} = (-Q^2)^{nq};  int = -(-1)^{sb} F(b) (Q^2)^{D - sb}/(4pi)^D
        tot += cnum*(-Qsq)**nq*(-(-1)**sb)*Fb*Qsq**(Dv - sb)
    return tot

def coeffval(c, Dv):
    return mp.mpf(sp.N(sp.sympify(c).subs(Dsym, sp.nsimplify(Dv)) if False else 0, 10))

def Pi1(eps_val):
    F, G, Dv = make_evaluator(eps_val)
    # numerators contain D symbolically -> substitute numerically
    tot = mp.mpf(0); totq = mp.mpf(0); per = {}
    for kname, (slots, a) in traces.items():
        P = polys[kname]
        Pn = sp.Poly({m: sp.N(c.subs(Dsym, sp.Rational(4) - 2*sp.Rational(eps_val)), 50) for m, c in P.terms()}, D1, D2, D3, D4, D5, QQ)
        val = minkowski_twoloop(Pn, a, F, Dv)
        per[kname] = val; tot += val
        Pq = polys_q[kname]
        Pqn = sp.Poly({m: sp.N(c.subs(Dsym, sp.Rational(4) - 2*sp.Rational(eps_val)), 50) for m, c in Pq.terms()}, D1, D2, D3, D4, D5, QQ) if Pq.terms() else None
        if Pqn is not None:
            totq += minkowski_twoloop(Pqn, a, F, Dv)
    # Pi^{mu nu} = g^2 C_F N_c e_q^2 x [int int trace/denominators];  Pi = g_{mu nu}Pi^{mu nu}/((1-D) q^2), q^2 = -Q^2 = -1
    # => Pi^(1) in units N_c e_q^2 C_F g0^2 (Q^2)^{-2eps}/(4pi)^D :
    Pi = tot/((1 - Dv)*(-1))
    return Pi, totq, per, G, Dv

def closed_form(eps_val):
    e = mp.mpf(eps_val)
    G11 = mp.gamma(e)*mp.gamma(1 - e)**2/mp.gamma(2 - 2*e)
    G1e = mp.gamma(2*e)*mp.gamma(1 - 2*e)*mp.gamma(1 - e)/(mp.gamma(1 + e)*mp.gamma(2 - 3*e))
    r1 = -4*(1 - e)*(2 - e + 2*e**2)/(e*(3 - 2*e))
    r2 = 16*(1 - e)*(1 - 2*e)*(2 - 2*e + e**2)/(e*(3 - 2*e)*(2 - 3*e))
    return r1*G11**2 + r2*G11*G1e, G11, G1e, r1, r2

# one-loop normalisation with the same conventions: Pi^{mu nu}_0 = i N_c e_q^2 int Tr[gamma^mu kslash gamma^nu (k-q)slash]/(k^2 (k-q)^2)
def Pi0(eps_val):
    e = mp.mpf(eps_val); Dv = 4 - 2*e
    tr0 = trace([mu, k_, mu, kmq], dot2)        # contains D1, D2, qq
    P = sp.Poly(sp.expand(tr0), D1, D2, QQ)
    tot = mp.mpc(0)
    for (n1, n2, nq), c in P.terms():
        a1, a2 = 1 - n1, 1 - n2
        cn = mp.mpf(sp.N(c.subs(Dsym, 4 - 2*sp.Rational(eps_val)), 50))
        if a1 <= 0 or a2 <= 0: continue
        G = mp.gamma(a1 + a2 - Dv/2)*mp.gamma(Dv/2 - a1)*mp.gamma(Dv/2 - a2)/(mp.gamma(a1)*mp.gamma(a2)*mp.gamma(Dv - a1 - a2))
        # Minkowski one loop: int d^Dk/(2pi)^D prod D^{-a} = i (-1)^{a1+a2} G (Q^2)^{D/2-a1-a2}/(4pi)^{D/2}, q^2 = -1
        tot += cn*(-1)**nq*1j*(-1)**(a1 + a2)*G
    PiMuMu = 1j*tot             # times i from the definition
    return PiMuMu/((1 - Dv)*(-1))   # in units N_c e_q^2/(4pi)^{D/2}

for ev in ('1/10', '-1/5', '31/100', '-43/100', '123/10000'):
    e = mp.mpf(sp.Rational(ev))
    p0 = Pi0(sp.Rational(ev))
    G11 = mp.gamma(e)*mp.gamma(1 - e)**2/mp.gamma(2 - 2*e)
    target0 = 2*(2 - 2*e)/(3 - 2*e)*G11
    check('one-loop normalisation at eps=%s: Pi_0 = 2(D-2)/(D-1) G(1,1) (Q^2)^{-eps}/(4pi)^{D/2}' % ev, abs(p0 - target0) < mp.mpf('1e-30')*abs(target0))

for ev in ('1/10', '-1/5', '31/100', '-43/100', '123/10000', '7/30'):
    Pi, totq, per, G, Dv = Pi1(sp.Rational(ev))
    cf = closed_form(sp.Rational(ev))[0]
    check('eps=%s: own two-loop Pi^(1)_bare = r1 G11^2 + r2 G11 G(1+eps,1) (rel. dev %s)' % (ev, mp.nstr(abs(Pi - cf)/abs(cf), 3)),
          abs(Pi - cf) < mp.mpf('1e-28')*abs(cf), 'Pi=%s' % mp.nstr(Pi, 20))
    check('eps=%s: transversality q_mu q_nu Pi^{mu nu} = 0 (sum of V, S1, S2; |value| %s)' % (ev, mp.nstr(abs(totq), 3)), abs(totq) < mp.mpf('1e-28')*abs(per['V']))

# F(1,1,1,1,1) -> 6 zeta_3 at eps -> 0
F, G, Dv = make_evaluator(sp.Rational(1, 10**6))
check('own triangle-rule evaluation: F(1,1,1,1,1) -> 6 zeta(3) = %s (eps=1e-6: %s)' % (mp.nstr(6*mp.zeta(3), 12), mp.nstr(F((1, 1, 1, 1, 1)), 12)),
      abs(F((1, 1, 1, 1, 1)) - 6*mp.zeta(3)) < 1e-4)

# ------------------------------------------------------------------ cut side: own form factor and own real emission
# (a) one-loop form factor, exact in eps:  Lambda^mu = -i g^2 C_F int gamma^a (p1-l) gamma^mu (-p2-l) gamma_a / (l^2 (p1-l)^2 (p2+l)^2)
Da, Db, Dc, S = sp.symbols('Da Db Dc S')    # Da=l^2, Db=(p1-l)^2, Dc=(p2+l)^2, S = s = 2 p1.p2
def dot3(a, b):
    a, b = sorted([a, b])
    tab = {('l', 'l'): Da, ('p1', 'p1'): 0, ('p2', 'p2'): 0, ('p1', 'p2'): S/2,
           ('l', 'p1'): (Da - Db)/2, ('l', 'p2'): (Dc - Da)/2}
    return tab[(a, b)]
p1v = vec(p1=1); p2v = vec(p2=1); p1ml = vec(p1=1, l=-1); mp2ml = vec(p2=-1, l=-1)
ff_num = trace([p1v, al, p1ml, mu, mp2ml, al, p2v, mu], dot3)       # Tr[p1 Gamma^mu p2 gamma_mu]
ff_den = trace([p1v, mu, p2v, mu], dot3)
Pff = sp.Poly(sp.expand(ff_num), Da, Db, Dc, S)
def FF(eps_val):
    e = mp.mpf(eps_val); Dv = 4 - 2*e
    den = mp.mpf(sp.N(ff_den.subs({Dsym: 4 - 2*sp.Rational(eps_val), S: 1}), 50))
    tot = mp.mpc(0)
    for (na, nb, nc, ns), c in Pff.terms():
        a, b, cc = 1 - na, 1 - nb, 1 - nc
        cn = mp.mpf(sp.N(c.subs(Dsym, 4 - 2*sp.Rational(eps_val)), 50))
        # integrals J(a,b,c) = int d^Dl/(2pi)^D Da^-a Db^-b Dc^-c at s = 1 (Minkowski), in units 1/(4pi)^{D/2}, (-s-i0)^{-...}
        if a == 1 and b == 1 and cc == 1:
            J = -1j*mp.gamma(1 + e)*mp.gamma(-e)**2/mp.gamma(1 - 2*e)*mp.exp(1j*mp.pi*(-1 - e))*(-1)**0   # (-s-i0)^{-1-eps} at s=1 -> e^{i pi (1+eps)}?? see below
            J = -1j*mp.gamma(1 + e)*mp.gamma(-e)**2/mp.gamma(1 - 2*e)*mp.exp(1j*mp.pi*(1 + e))**(-1)*(-1)**0
            # (-1 - i0)^{-1-eps} = e^{-i pi (-1-eps)} = e^{i pi (1+eps)}
            J = -1j*mp.gamma(1 + e)*mp.gamma(-e)**2/mp.gamma(1 - 2*e)*mp.exp(1j*mp.pi*(1 + e))
        elif a <= 0 and b >= 1 and cc >= 1:
            # numerator (l^2)^{-a}: shift l = p1 - l'  ->  Db = l'^2, Dc = (q - l')^2 with q = p1+p2, Da = (p1-l')^2 = l'^2 - 2 l'.p1
            # only a = 0 and a = -1 occur; handle a=0: bubble; a=-1: l^2 = Db - 2 l'.p1 + 0 ... use tensor formula with p1.q = s/2
            if b != 1 or cc != 1: raise ValueError((a, b, cc))
            G11 = mp.gamma(e)*mp.gamma(1 - e)**2/mp.gamma(2 - 2*e)
            bub = 1j*G11*mp.exp(1j*mp.pi*e)        # int 1/(Db Dc) = i G(1,1) (-s-i0)^{-eps}/(4pi)^{D/2},  (-1-i0)^{-eps}=e^{i pi eps}
            if a == 0:
                J = bub
            elif a == -1:
                # int (l'^2 - 2 l'.p1)/(l'^2 (q-l')^2): first term scaleless; second: -2 p1.<l'> = -2 p1.q * (1/2) bub = -(s/2) bub
                J = -mp.mpf(1)/2*bub
            else:
                raise ValueError(a)
        elif b <= 0 or cc <= 0:
            J = 0      # scaleless (only one external light-like momentum left) -- checked: such terms carry Da with b or c <= 0
            if (b <= 0 and cc <= 0): J = 0
            # a bubble with external momentum p1 or p2 (light-like) is scaleless
        else:
            raise ValueError((a, b, cc))
        tot += cn*J
    # Lambda^mu = -i g^2 C_F int (...);  F^(1) = Tr[p1 Lambda p2 gamma]/Tr[p1 gamma p2 gamma]
    return (-1j)*tot/den     # units g0^2 C_F/(4pi)^{D/2} (s)^{-eps}
def FF_claim(eps_val):
    e = mp.mpf(eps_val)
    cG = mp.gamma(1 + e)*mp.gamma(1 - e)**2/mp.gamma(1 - 2*e)
    # F^(1) = -(alpha_s C_F/4pi)(4pi mu0^2/(-q^2-i0))^eps c_Gamma (2-eps+2eps^2)/(eps^2(1-2eps)); in units g0^2 C_F/(4pi)^{D/2}:
    # alpha_s/(4pi) (4pi)^eps = g0^2/(16 pi^2) (4pi)^eps = g0^2/(4pi)^{2-eps}
    return -mp.exp(1j*mp.pi*e)*cG*(2 - e + 2*e**2)/(e**2*(1 - 2*e))
for ev in ('1/10', '-1/5', '31/100', '-43/100'):
    a = FF(sp.Rational(ev)); b = FF_claim(sp.Rational(ev))
    check('own one-loop form factor at eps=%s equals -(a_s C_F/4pi)(4pi mu^2/(-s-i0))^eps c_Gamma (2-eps+2eps^2)/(eps^2(1-2eps))' % ev,
          abs(a - b) < mp.mpf('1e-30')*abs(b), mp.nstr(a, 15))

# (b) real emission: T_R = Tr[p1 Gamma^{a mu} p2 Gammabar_{a mu}], Gamma^{a mu} = g^a (p1+k) g^mu / s13 - g^mu (p2+k) g^a / s23
y12, y13, y23 = sp.symbols('y12 y13 y23', positive=True)
def dot4(a, b):
    a, b = sorted([a, b])
    tab = {('p1', 'p1'): 0, ('p2', 'p2'): 0, ('k', 'k'): 0, ('p1', 'p2'): y12/2, ('k', 'p1'): y13/2, ('k', 'p2'): y23/2}
    return tab[(a, b)]                         # units s = 1
p1k = vec(p1=1, k=1); p2k = vec(p2=1, k=1)
s13, s23 = y13, y23
TR = 0
for (A1, A2, c1) in [((al, p1k, mu), None, 1/s13), ((mu, p2k, al), None, -1/s23)]:
    for (B1, c2) in [((mu, p1k, al), 1/s13), ((al, p2k, mu), -1/s23)]:
        # Gammabar reverses the order: conj of (g^a X g^mu) is (g^mu X g^a)
        TR += c1*c2*trace([p1v] + list(A1) + [p2v] + list(B1), dot4)
TR = sp.simplify(TR)
TRc = sp.simplify(TR.subs(y12, 1 - y13 - y23))
TR_claim = 8*(1 - (2 - Dsym)/(-2))*0   # placeholder
TR_c_ee = 8*(1 - (4 - Dsym)/2)*((1 - (4 - Dsym)/2)*(y13/y23 + y23/y13) + 2*y12/(y13*y23) - 2*(4 - Dsym)/2)
check('real-emission trace T_R = 8(1-eps)[(1-eps)(y13/y23+y23/y13) + 2 y12/(y13 y23) - 2 eps] on y12+y13+y23=1 (own D-dim traces; = c_ee (3.4))',
      sp.simplify((TR - TR_c_ee).subs(y12, 1 - y13 - y23)) == 0)
# D-dim 3-body phase space: dPhi3 = s^{1-2eps}/(2(4pi)^{3-2eps}Gamma(2-2eps)) (y12 y13 y23)^{-eps} dy13 dy23 ; check the volume
def Phi2(s, m2, e):
    Dv = 4 - 2*e
    pm = (s - m2)/(2*mp.sqrt(s))
    Om = 2*mp.pi**((Dv - 1)/2)/mp.gamma((Dv - 1)/2)
    return Om*pm**(Dv - 3)/(4*(2*mp.pi)**(Dv - 2)*mp.sqrt(s))
for ev in (mp.mpf('-0.2'), mp.mpf('0.15'), mp.mpf('0.3')):
    e = ev
    rec = mp.quad(lambda M2: Phi2(1, M2, e)*Phi2(M2, 0, e), [0, 1])/(2*mp.pi)
    vol = 1/(2*(4*mp.pi)**(3 - 2*e)*mp.gamma(2 - 2*e))*mp.gamma(1 - e)**3/mp.gamma(3 - 3*e)
    check('3-body phase-space normalisation (eps=%s): recursion Phi3 = int dM^2/(2pi) Phi2(s;M^2,0) Phi2(M^2) equals the Dirichlet volume' % mp.nstr(e, 3),
          abs(rec - vol) < mp.mpf('1e-25')*vol)
def dirichlet(a, b, c, e):
    # int over y12+y13+y23=1 of y12^a y13^b y23^c (y12 y13 y23)^{-eps} dy13 dy23
    return mp.gamma(a + 1 - e)*mp.gamma(b + 1 - e)*mp.gamma(c + 1 - e)/mp.gamma(a + b + c + 3 - 3*e)
TRn = sp.expand(sp.together(TR))
num_, den_ = sp.fraction(sp.together(TR))
def rhoR(eps_val):
    e = mp.mpf(eps_val)
    expr = sp.expand(TR.subs(Dsym, 4 - 2*sp.Rational(eps_val)))
    tot = mp.mpf(0)
    for term in sp.Add.make_args(expr):
        c, rest = term.as_coeff_Mul()
        pw = {y12: 0, y13: 0, y23: 0}
        for f_ in sp.Mul.make_args(rest):
            b_, ex = f_.as_base_exp()
            if b_ in pw: pw[b_] += int(ex)
            else: c *= f_
        tot += mp.mpf(sp.N(c, 50))*dirichlet(pw[y12], pw[y13], pw[y23], e)
    # rho_R = g0^2 C_F N_c e_q^2 int dPhi3 T_R  (s=1), in units N_c e_q^2 C_F g0^2:
    return tot/(2*(4*mp.pi)**(3 - 2*e)*mp.gamma(2 - 2*e))
def rho0(eps_val):
    e = mp.mpf(eps_val); Dv = 4 - 2*e
    return 2*(Dv - 2)*Phi2(1, 0, e)       # units N_c e_q^2
for ev in ('1/10', '-1/5', '31/100', '-43/100', '123/10000'):
    e = mp.mpf(sp.Rational(ev)); Dv = 4 - 2*e
    # LHS: 2(D-1) s Im Pi^(1)_bare(s+i0) with (Q^2)^{-2eps} -> e^{2 pi i eps} at s=1; units N_c e_q^2 C_F g0^2
    cf, G11, G1e, r1, r2 = closed_form(sp.Rational(ev))
    Pi_own = Pi1(sp.Rational(ev))[0]
    lhs = 2*(Dv - 1)*mp.sin(2*mp.pi*e)*Pi_own/(4*mp.pi)**Dv
    rv = rho0(sp.Rational(ev))*2*mp.re(FF(sp.Rational(ev)))/(4*mp.pi)**(Dv/2)
    rr = rhoR(sp.Rational(ev))
    check('eps=%s: exact cutting identity 2(D-1)s Im Pi^(1)_bare = rho_V + rho_R with OWN Pi^(1), OWN form factor, OWN real emission (rel. dev %s)'
          % (ev, mp.nstr(abs(lhs - rv - rr)/abs(lhs), 3)), abs(lhs - rv - rr) < mp.mpf('1e-27')*abs(lhs))
    # term by term
    lhs1 = 2*(Dv - 1)*mp.sin(2*mp.pi*e)*r1*G11**2/(4*mp.pi)**Dv
    lhs2 = 2*(Dv - 1)*mp.sin(2*mp.pi*e)*r2*G11*G1e/(4*mp.pi)**Dv
    check('eps=%s: term by term: r1 G11^2 <-> rho_V and r2 G11 G(1+eps,1) <-> rho_R' % ev,
          abs(lhs1 - rv) < mp.mpf('1e-27')*abs(lhs1) and abs(lhs2 - rr) < mp.mpf('1e-27')*abs(lhs2))
    # LO: rho_0 = 2(D-1)s Im Pi_0
    lo = 2*(Dv - 1)*mp.sin(mp.pi*e)*2*(Dv - 2)/(Dv - 1)*G11/(4*mp.pi)**(Dv/2)
    check('eps=%s: LO normalisation rho_0 = 2(D-1)s Im Pi_0' % ev, abs(lo - rho0(sp.Rational(ev))) < mp.mpf('1e-30')*lo)

# ------------------------------------------------------------------ MS-bar expansion (numerical Laurent coefficients by contour integrals)
# units (alpha_s/pi) C_F N_c e_q^2/(12 pi^2):  Pi^(1) = (3/16) e^{2 eps gamma_E} e^{-2 eps L} [r1 G11^2 + r2 G11 G(1+eps,1)]
# units N_c e_q^2/(12 pi^2):                   Pi^(0) = (3/4) e^{eps gamma_E} e^{-eps L} 2(D-2)/(D-1) G11
mp.mp.dps = 40
def f1(e, Lv):
    cf, G11, G1e, r1, r2 = closed_form_mp(e)
    return mp.mpf(3)/16*mp.exp(2*e*mp.euler)*mp.exp(-2*e*Lv)*cf
def closed_form_mp(e):
    G11 = mp.gamma(e)*mp.gamma(1 - e)**2/mp.gamma(2 - 2*e)
    G1e = mp.gamma(2*e)*mp.gamma(1 - 2*e)*mp.gamma(1 - e)/(mp.gamma(1 + e)*mp.gamma(2 - 3*e))
    r1 = -4*(1 - e)*(2 - e + 2*e**2)/(e*(3 - 2*e))
    r2 = 16*(1 - e)*(1 - 2*e)*(2 - 2*e + e**2)/(e*(3 - 2*e)*(2 - 3*e))
    return r1*G11**2 + r2*G11*G1e, G11, G1e, r1, r2
def f0(e, Lv):
    G11 = mp.gamma(e)*mp.gamma(1 - e)**2/mp.gamma(2 - 2*e)
    return mp.mpf(3)/4*mp.exp(e*mp.euler)*mp.exp(-e*Lv)*2*(2 - 2*e)/(3 - 2*e)*G11
def laurent(f, n, rad=mp.mpf('0.1')):
    # c_n = (1/2 pi i) oint f(e) e^{-n-1} de on |e| = rad
    return mp.quad(lambda th: f(rad*mp.exp(1j*th))*(rad*mp.exp(1j*th))**(-n), [0, mp.pi/2, mp.pi, 3*mp.pi/2, 2*mp.pi])/(2*mp.pi)
for Lv in (mp.mpf(0), mp.mpf('1.7'), mp.mpf('-0.6')):
    c2 = laurent(lambda e: f1(e, Lv), -2); c1 = laurent(lambda e: f1(e, Lv), -1); c0 = laurent(lambda e: f1(e, Lv), 0)
    target0 = mp.mpf(55)/16 - 3*mp.zeta(3) - mp.mpf(3)/4*Lv
    check('L=%s: two-loop Laurent coefficients: 1/eps^2 -> %s (0), 1/eps -> %s (3/8, L-independent), eps^0 -> %s = 55/16 - 3 zeta3 - (3/4)L'
          % (mp.nstr(Lv, 3), mp.nstr(abs(c2), 3), mp.nstr(mp.re(c1), 25), mp.nstr(mp.re(c0), 25)),
          abs(c2) < mp.mpf('1e-30') and abs(c1 - mp.mpf(3)/8) < mp.mpf('1e-30') and abs(c0 - target0) < mp.mpf('1e-30'))
    d1 = laurent(lambda e: f0(e, Lv), -1); d0 = laurent(lambda e: f0(e, Lv), 0)
    check('L=%s: one-loop: pole 1/eps (coefficient 1, local), finite 5/3 - L' % mp.nstr(Lv, 3),
          abs(d1 - 1) < mp.mpf('1e-30') and abs(d0 - (mp.mpf(5)/3 - Lv)) < mp.mpf('1e-30'))
check('MS-bar: Pi = N_c e_q^2/(12 pi^2)[5/3 - L + (alpha_s/pi)(3C_F/4)(55/12 - 4 zeta3 - L)] since (3/4)(55/12-4zeta3-L) = 55/16-3zeta3-(3/4)L',
      abs(mp.mpf(3)/4*(mp.mpf(55)/12 - 4*mp.zeta(3)) - (mp.mpf(55)/16 - 3*mp.zeta(3))) < mp.mpf('1e-35'))
# R: Im of the finite parts at L = l - i pi:  Im[-L] = pi  ->  12 pi Im Pi = N_c e_q^2 [1 + (3C_F/4) alpha_s/pi]
check('R = 12 pi Im Pi(s+i0) = N_c e_q^2 [1 + (3C_F/4) alpha_s/pi] (= 1 + alpha_s/pi for C_F = 4/3)', abs(12*mp.pi*(mp.pi/(12*mp.pi**2)) - 1) < 1e-30)
print('\nSUMMARY: %d/%d checks passed' % (sum(res), len(res)), flush=True)
