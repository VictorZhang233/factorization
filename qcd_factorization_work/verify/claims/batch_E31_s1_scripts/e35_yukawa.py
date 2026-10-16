"""
E35 independent check (verifier stage 1, batch E31): one-loop quark-in-"nucleon" PDF in the massive Yukawa model
L_int = -lambda Psibar_N psi_q phi + h.c.  (target fermion m_p, quark m_q, scalar m_s).
Derivation (by hand, see batch_E31_s1.md section E35):
  f(xi) = lambda^2 (1-xi)/(2 (2 pi)^(D-1)) * mu^(2 eps) Int d^(D-2)k_T [k_T^2 + (m_q + xi m_p)^2]/(k_T^2 + Delta)^2 ,
  Delta = xi m_s^2 + (1-xi) m_q^2 - xi(1-xi) m_p^2 .
Checks:
 (a) the spin trace (1/2) Tr[(Pslash+m_p)(kslash+m_q) g^+ (kslash+m_q)] = 2 P^+ [(m_q+xi m_p)^2 + k_T^2] with l=P-k on shell
     (sympy, explicit light-cone components);
 (b) dimensional regularisation of the k_T integral, MS-bar: bracket ln(mu^2/Delta) - 1 + (m_q+xi m_p)^2/Delta and
     pole a(1-xi) S_eps/eps (sympy series in eps);
 (c) cut-off version vs MS-bar: difference O(m^2/K^2);
 (d) sign structure for m_q=0.3, m_p=1.0, m_s=1.5 GeV: negative xi-interval at mu = 0.8, 1.2, 2.5 GeV; mu_* for xi->1;
     the scale mu_0(xi) below which f<0, and its maximum over xi; Delta>0 on [0,1].
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

# (a) trace with explicit components in light-cone coordinates (metric +,-,-,-; v.w = v+w- + v-w+ - vT.wT)
xi, Pp, kT, mq, mp_, ms = sp.symbols('xi P_plus k_T m_q m_p m_s', positive=True)
# Dirac matrices (Dirac rep)
I2 = sp.eye(2); Z2 = sp.zeros(2)
sx = sp.Matrix([[0,1],[1,0]]); sy = sp.Matrix([[0,-sp.I],[sp.I,0]]); sz = sp.Matrix([[1,0],[0,-1]])
def blk(a,b,c,d): return sp.Matrix(sp.BlockMatrix([[a,b],[c,d]]))
g0 = blk(I2,Z2,Z2,-I2); g1 = blk(Z2,sx,-sx,Z2); g2 = blk(Z2,sy,-sy,Z2); g3 = blk(Z2,sz,-sz,Z2)
gplus = (g0 + g3)/sp.sqrt(2)
def slash(v0,v1,v2,v3): return g0*v0 - g1*v1 - g2*v2 - g3*v3
def from_lc(vp, vm, v1, v2):  # v^0 = (v+ + v-)/sqrt2, v^3 = (v+ - v-)/sqrt2
    return ((vp+vm)/sp.sqrt(2), v1, v2, (vp-vm)/sp.sqrt(2))
Pm = mp_**2/(2*Pp)
P = from_lc(Pp, Pm, 0, 0)
lp = (1-xi)*Pp; lm = (kT**2 + ms**2)/(2*lp)
kp = xi*Pp; km = Pm - lm
k = from_lc(kp, km, kT, 0)
E4 = sp.eye(4)
tr = sp.simplify(sp.Rational(1,2)*((slash(*P) + mp_*E4)*(slash(*k) + mq*E4)*gplus*(slash(*k) + mq*E4)).trace())
target = 2*Pp*((mq + xi*mp_)**2 + kT**2)
print("(a) (1/2)Tr[...] - 2P+[(mq+xi mp)^2+kT^2] =", sp.simplify(tr - target))
k2 = sp.simplify(2*kp*km - kT**2)
Delta = xi*ms**2 + (1-xi)*mq**2 - xi*(1-xi)*mp_**2
print("    k^2 - m_q^2 + (kT^2+Delta)/(1-xi) =", sp.simplify(k2 - mq**2 + (kT**2 + Delta)/(1-xi)))

# (b) DR: d = 2 - 2 eps transverse dims; I1 = Int d^dk/(2pi)^d 1/(k^2+D), I2 = Int d^dk/(2pi)^d 1/(k^2+D)^2
eps, D_, M2, mu = sp.symbols('epsilon Delta M2 mu', positive=True)
d = 2 - 2*eps
I1 = sp.gamma(1 - d/2)*D_**(d/2 - 1)/(4*sp.pi)**(d/2)
I2_ = sp.gamma(2 - d/2)*D_**(d/2 - 2)/(4*sp.pi)**(d/2)
J = mu**(2*eps)*(I1 + (M2 - D_)*I2_)          # Int [k^2 + M2]/(k^2+D)^2
# f = lambda^2 (1-xi)/(2 (2pi)) * J  (the (2pi)^(D-2) of the measure is inside I1, I2); a = lambda^2/(16 pi^2)
lam = sp.symbols('lambda', positive=True)
f = lam**2*(1-xi)/(4*sp.pi)*J
ser = sp.series(f, eps, 0, 1).removeO()
a = lam**2/(16*sp.pi**2)
Seps_pole = a*(1-xi)*(1/eps - sp.EulerGamma + sp.log(4*sp.pi))   # S_eps/eps expanded
msbar = sp.simplify(sp.expand(ser - Seps_pole))
expected = a*(1-xi)*(sp.log(mu**2/D_) - 1 + M2/D_)
print("(b) MS-bar finite part - a(1-xi)[ln(mu^2/Delta) - 1 + M2/Delta] =", sp.simplify(sp.expand_log(msbar - expected, force=True)))
print("    pole coefficient of 1/eps:", sp.simplify(sp.limit(ser*eps, eps, 0)/(a*(1-xi))), "x a(1-xi)")

# (c),(d) numerics
mp.mp.dps = 30
MQ, MP, MS = mp.mpf('0.3'), mp.mpf('1.0'), mp.mpf('1.5')
def Dl(x): return x*MS**2 + (1-x)*MQ**2 - x*(1-x)*MP**2
def bracket(x, m): return mp.log(m**2/Dl(x)) - 1 + (MQ + x*MP)**2/Dl(x)
def cut(x, K):     # exact k_T < K integral, divided by a(1-xi) (pi * Int dt)
    D0 = Dl(x); M = (MQ + x*MP)**2
    return mp.log((K**2 + D0)/D0) + (M - D0)*(1/D0 - 1/(K**2 + D0))
print("(c) cut-off (K=mu) minus MS-bar bracket, max over xi in (0,1):")
for m in [mp.mpf(5), mp.mpf(30), mp.mpf(100)]:
    xs = [mp.mpf(i)/200 for i in range(1, 200)]
    print(f"    mu=K={mp.nstr(m,3)} GeV: max|diff| = {mp.nstr(max(abs(cut(x, m) - bracket(x, m)) for x in xs), 4)}")
print("    min Delta on [0,1]:", mp.nstr(min(Dl(mp.mpf(i)/1000) for i in range(0, 1001)), 6), "(>0: stable target, m_p < m_q + m_s)")
def sign_changes(m, n=4000):
    xs = [mp.mpf(i)/n for i in range(1, n)]
    sg = [bracket(x, m) < 0 for x in xs]
    out = []
    for i in range(1, len(xs)):
        if sg[i] != sg[i-1]:
            a_, b_ = xs[i-1], xs[i]
            for _ in range(120):
                c_ = (a_ + b_)/2
                if (bracket(c_, m) < 0) == (bracket(a_, m) < 0): a_ = c_
                else: b_ = c_
            out.append((a_ + b_)/2)
    return sg[0], out, sg[-1]
for m in ['0.8', '1.2', '2.5']:
    s0, roots, s1 = sign_changes(mp.mpf(m))
    print(f"(d) mu={m} GeV: sign near xi=0: {'-' if s0 else '+'}; sign changes at xi = {[mp.nstr(r, 6) for r in roots]}; sign near xi=1: {'-' if s1 else '+'}")
mustar = MS*mp.exp(mp.mpf(1)/2*(1 - (MQ + MP)**2/MS**2))
print("    mu_* (xi->1) =", mp.nstr(mustar, 6), "GeV; bracket(1-1e-9, mu_*) =", mp.nstr(bracket(1 - mp.mpf('1e-9'), mustar), 3))
# mu_0(xi): zero of bracket in mu:  ln mu0^2 = ln Delta + 1 - M2/Delta
def mu0(x): return mp.sqrt(Dl(x))*mp.exp(mp.mpf(1)/2*(1 - (MQ + x*MP)**2/Dl(x)))
xs = [mp.mpf(i)/2000 for i in range(1, 2000)]
vals = [(mu0(x), x) for x in xs]
mx = max(vals)
print("    mu_0(xi) [f(xi;mu)<0 iff mu<mu_0(xi)]: mu_0(0+) =", mp.nstr(mu0(mp.mpf('1e-9')), 5), " mu_0(1-) =", mp.nstr(mu0(1 - mp.mpf('1e-9')), 5),
      " max over xi =", mp.nstr(mx[0], 6), "at xi =", mp.nstr(mx[1], 4))
