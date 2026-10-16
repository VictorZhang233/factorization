# W17 / Ch14 -- s02: one-gluon real emission in the unsubtracted TMD of a quark in a quark, Feynman gauge,
# non-light-like Wilson line n = n_B(y_B) = (s e^{2y_B}, 1^-, 0_T)  (s=-1 space-like (Collins), s=+1 time-like),
# book conventions (D = d - i g A t, vertex i g gamma t, future-pointing W[inf n,0]: g t n^mu/(n.k - i0), k INTO line).
# Amplitude (SIDIS, outgoing gluon l = p - k):  M^mu = -g t^a [ kslash gamma^mu / k^2 + n^mu/(n.l + i0) ] u(p)
# (DY: n.l - i0).  f_real = c_S N/(4 (1-x) p^+),  N = 1/2 Tr[pslash Gbar_nu gamma^+ G_mu](-g^{mu nu}),  F = kT^2 N/(4(1-x)p^+).
# Independent D-dimensional trace routine written for this check.
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

D = sp.Symbol('D')
ok = True
def check(name, cond):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name); ok &= bool(cond)

# ---------- minimal D-dim trace: slots are ('v',name) or ('i',name); g(a,b) symbolic pair
def pair(a, b):
    x, y = sorted([a, b])
    return sp.Symbol('g[%s,%s]' % (x, y))
def tr(slots):
    n = len(slots)
    if n == 0:
        return sp.Integer(4)
    if n % 2 == 1:
        return sp.Integer(0)
    a = slots[0]; res = 0
    for j in range(1, n):
        sign = (-1)**(j - 1)
        rest = slots[1:j] + slots[j + 1:]
        res += sign*pair(a[1], slots[j][1])*tr(rest)
    return sp.expand(res)

def contract(expr, idx, vecs):
    """contract repeated Lorentz index idx (appearing in pair symbols) ; vecs: names of vectors/other indices"""
    expr = sp.expand(expr)
    out = 0
    for term in sp.Add.make_args(expr):
        c, facs = term.as_coeff_mul()
        others = []; partners = []
        for f in facs:
            base, ex = f.as_base_exp()
            nm = str(base)
            if nm.startswith('g[') and idx in nm[2:-1].split(','):
                a, b = nm[2:-1].split(',')
                if a == idx and b == idx:
                    others.append(D**ex)
                    continue
                partner = b if a == idx else a
                partners += [partner]*int(ex)
            else:
                others.append(f)
        val = c*sp.Mul(*others)
        if len(partners) == 2:
            val *= pair(partners[0], partners[1])
        elif len(partners) == 0:
            pass
        else:
            raise ValueError('bad contraction %s' % term)
        out += val
    return sp.expand(out)

# ---------- kinematics
x, kT, pp, yB, eps = sp.symbols('x k_T p_p y_B epsilon', positive=True)
s = sp.Symbol('s')   # +-1
E2 = sp.exp(2*yB)
vec = {   # light-cone components (plus, minus), transverse 2-vector
    'p': (pp, 0, (0, 0)),
    'l': ((1 - x)*pp, kT**2/(2*(1 - x)*pp), (-kT, 0)),
    'k': (x*pp, -kT**2/(2*(1 - x)*pp), (kT, 0)),
    'nB': (0, 1, (0, 0)),          # gamma^+ = nB-slash
    'n': (s*E2, 1, (0, 0)),        # regulator line
}
def dot4(a, b):
    A, B = vec[a], vec[b]
    return sp.simplify(A[0]*B[1] + A[1]*B[0] - (A[2][0]*B[2][0] + A[2][1]*B[2][1]))
subs = {}
names = list(vec)
for a, b in itertools.combinations_with_replacement(names, 2):
    subs[pair(a, b)] = dot4(a, b)
k2 = dot4('k', 'k'); nl = dot4('n', 'l')
check('k^2 = -kT^2/(1-x)', sp.simplify(k2 + kT**2/(1 - x)) == 0)
check('l^2 = 0 and p^2 = 0', dot4('l', 'l') == 0 and dot4('p', 'p') == 0)

V = lambda nm: ('v', nm)
I = lambda nm: ('i', nm)
# N = 1/2 * (-g^{mu nu}) Tr[ p Gbar_nu nB G_mu ],  G_mu = k gamma_mu / k^2 + n_mu / nl ;  Gbar_nu = gamma_nu k / k^2 + n_nu/nl
t1 = tr([V('p'), I('nu'), V('k'), V('nB'), V('k'), I('mu')])/k2**2         # (gamma_nu k)(k gamma_mu)
t2 = tr([V('p'), I('nu'), V('k'), V('nB')])*pair('n', 'mu')/(k2*nl)        # (gamma_nu k) ... n_mu
t3 = tr([V('p'), V('nB'), V('k'), I('mu')])*pair('n', 'nu')/(k2*nl)        # n_nu ... (k gamma_mu)
t4 = tr([V('p'), V('nB')])*pair('n', 'mu')*pair('n', 'nu')/nl**2
Ns = {}
for lab, t in [('a', t1), ('b', t2 + t3), ('c', t4)]:
    e = sp.expand(-t*pair('mu', 'nu'))     # -g^{mu nu}
    e = contract(e, 'mu', names)
    e = contract(e, 'nu', names)
    e = sp.Rational(1, 2)*e.subs(subs)
    Ns[lab] = sp.simplify(e)
F = {lab: sp.simplify(kT**2*Ns[lab]/(4*(1 - x)*pp)) for lab in Ns}
delta2 = E2*kT**2/(2*pp**2)
Fa_exp = (1 - eps)*(1 - x)
Fb_exp = 2*x*(1 - x)/((1 - x)**2 + s*delta2)
Fc_exp = -2*s*delta2*(1 - x)/((1 - x)**2 + s*delta2)**2
check('F_a = (1-eps)(1-x)', sp.simplify(F['a'].subs(D, 4 - 2*eps) - Fa_exp) == 0)
check('F_b = 2x(1-x)/((1-x)^2 + s delta^2)', sp.simplify(F['b'] - Fb_exp) == 0)
check('F_c = -2 s delta^2 (1-x)/((1-x)^2+s delta^2)^2', sp.simplify(F['c'] - Fc_exp) == 0)
print('   F_a =', sp.factor(F['a'].subs(D, 4 - 2*eps)))
print('   F_b =', sp.factor(F['b']))
print('   F_c =', sp.factor(F['c']))
# Ward identity l_mu M^mu = 0  =>  polarization sum -g allowed (checked algebraically: kslash lslash u = -k^2 u)
# light-like limit (delta -> 0 at fixed x<1): F_b -> 2x/(1-x); T21 coefficient at eps=0:  c_S = alpha_s C_F/(2 pi^2)
check('light-like limit: F_b -> 2x/(1-x)', sp.simplify(sp.limit(F['b'], yB, -sp.oo) - 2*x/(1 - x)) == 0)
als, CF = sp.symbols('alpha_s C_F', positive=True)
cS0 = 4*sp.pi*als*CF/(2*sp.pi)**3
check('T21: c_S/kT^2 * 2x/(1-x) = alpha_s C_F x/(pi^2 (1-x) kT^2)', sp.simplify(cS0/kT**2*2*x/(1 - x) - als*CF*x/(sp.pi**2*(1 - x)*kT**2)) == 0)
# ladder+light-like Wilson graphs sum at eps=0: (1-x) + 2x/(1-x) = (1+x^2)/(1-x)
check('(1-x) + 2x/(1-x) = (1+x^2)/(1-x)', sp.simplify((1 - x) + 2*x/(1 - x) - (1 + x**2)/(1 - x)) == 0)
# n.l in terms of delta: n.l = p+/(1-x) [ (1-x)^2 + s delta^2 ]
check('n.l = p^+/(1-x) [(1-x)^2 + s delta^2]', sp.simplify(nl - pp/(1 - x)*((1 - x)**2 + s*delta2)) == 0)
print('ALL PASS' if ok else 'SOME FAIL')
