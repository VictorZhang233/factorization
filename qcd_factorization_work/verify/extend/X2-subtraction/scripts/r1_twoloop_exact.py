"""X2 fix round 1 / r1_twoloop_exact.py -- two-loop planar vertex: exact integrated remainder and its asymptotics.

(1) Homogeneity of every zeroing pattern (exact, symbolic).  For each of the 50 patterns of r = prod_R (1-T_R) Gamma
    (twoloop_patterns.json, soft-first convention) we solve for scaling weights of (k1+,k1-,k1T,k2+,k2-,k2T) with
    weight(m2) = 1 (p1^- and p2^+ carry m2; P, P' carry weight 0) such that every line factor -V^2 = -2V+V- + |V_T|^2
    is homogeneous, and compute the total degree D0 = sum(measure weights) - sum(factor weights) at eps = 0 and the
    eps-dependence -2 eps (a1T + a2T).  Homogeneity with D0 = 0 for all patterns implies
        sum_R int C_R Gamma = sum_patterns c_p K_p(eps) (m2)^{-2 eps (a1T+a2T)_p}   (pure powers),
    hence, once the poles cancel (int Gamma and int r finite), a polynomial P(Lt) of degree <= 4 in Lt = ln(Qt^2/m2).
(2) Exact remainder:  int r = Phi2(t,t)/Q^4 - P(Lt).  If int r -> 0 (content of the subtraction theorem, numerically
    supported) then P = LP = Lt^4/4 + pi^2 Lt^2/2 + 7 pi^4/60, and
        int r = -m2 (Lt^4/2 + pi^2 Lt^2 + 12 + 7 pi^4/30) + O(m2^2 Lt^4)      (Qt = 1, p1^2 = p2^2 = -m2).
    Here Phi2(t,t) = -(6/lam)[Li4(-1/(rho t)) - Li4(-rho t)] and, for Qt = 1, rho t = m2 exactly, lam = (1-m2)/(1+m2),
    Q^2 = (1+m2)^2, so  int Gamma = (1+m2) [12 Li4(-m2) + Lt^4/4 + pi^2 Lt^2/2 + 7 pi^4/60] / ((1-m2)(1+m2)^4).
(3) Comparison with the QMC estimates of t12 (n16, n18 logs) and of r1_twoloop_qmc (if present)."""
import sys, os, json, re
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp, mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
mp.mp.dps = 40

# ---------------- (1) homogeneity ----------------
LINE_DEF = {'g1': (None, 1, 0), 'g2': (None, 0, 1), 'a1': ('p1', 0, -1), 'a2': ('p1', -1, -1),
            'b1': ('p2', 0, 1), 'b2': ('p2', 1, 1)}
A = sp.symbols('a1p a1m a1T a2p a2m a2T')
a1p, a1m, a1T, a2p, a2m, a2T = A
def factor_monomial_weights(line, Z):
    c0, c1, c2 = LINE_DEF[line]
    zM = 'M' in Z
    Vp, Vm, VT = [], [], []
    if c0 == 'p1':
        Vp.append(0)                       # P (weight 0)
        if not zM: Vm.append(1)            # p1^- = -m2/2P (weight 1)
    elif c0 == 'p2':
        if not zM: Vp.append(1)            # p2^+ = m2/2P'
        Vm.append(0)                       # -P'
    if c1 and 'k1+' not in Z: Vp.append(a1p)
    if c2 and 'k2+' not in Z: Vp.append(a2p)
    if c1 and 'k1-' not in Z: Vm.append(a1m)
    if c2 and 'k2-' not in Z: Vm.append(a2m)
    if c1 and 'k1T' not in Z: VT.append(a1T)
    if c2 and 'k2T' not in Z: VT.append(a2T)
    mons = [x + y for x in Vp for y in Vm] + [x + y for x in VT for y in VT]
    return mons

def homogeneity(pattern):
    """pattern: dict line -> set.  Returns (solution weights, D0, eps-coefficient) or None if not homogeneous."""
    W = {l: sp.Symbol('w_' + l) for l in LINE_DEF}
    eqs = []
    for l in LINE_DEF:
        for mexpr in factor_monomial_weights(l, pattern[l]):
            eqs.append(sp.Eq(mexpr, W[l]))
    unknowns = list(A) + list(W.values())
    sol = sp.solve(eqs, unknowns, dict=True)
    if not sol:
        return None
    s = sol[0]
    D0 = sum(s.get(x, x) for x in [a1p, a1m, a2p, a2m]) + 2*(s.get(a1T, a1T) + s.get(a2T, a2T)) - sum(s.get(W[l], W[l]) for l in LINE_DEF)
    epsc = -2*(s.get(a1T, a1T) + s.get(a2T, a2T))
    return s, sp.simplify(D0), sp.simplify(epsc)

pats = json.load(open(os.path.join(HERE, 'twoloop_patterns.json')))
LINES = ['g1', 'g2', 'a1', 'a2', 'b1', 'b2']
print("(1) homogeneity of the 50 zeroing patterns of r (soft-first):")
nonhom = 0; D0bad = 0; free_D0 = 0; exps = {}
for p, c in pats['r']:
    pat = {LINES[i]: set(p[i]) for i in range(6)}
    out = homogeneity(pat)
    if out is None:
        nonhom += 1; print("   NOT homogeneous:", p); continue
    s, D0, epsc = out
    if D0.free_symbols:
        # D0 depends on undetermined weights: check it is identically zero
        free_D0 += 1
    if sp.simplify(D0) != 0:
        D0bad += 1; print("   D0 != 0:", p, D0)
    exps[str(p)] = str(epsc)
print(f"   patterns: {len(pats['r'])}, non-homogeneous: {nonhom}, D0 != 0: {D0bad}, (D0 with free weights: {free_D0})")
from collections import Counter
print("   distribution of the eps-exponent of m2 (coefficient of eps):", Counter(exps.values()))
# Gamma itself (no zeroing) must NOT be homogeneous:
print("   Gamma (no zeroing) homogeneous?", homogeneity({l: set() for l in LINES}) is not None)

# ---------------- (2) exact remainder and its expansion ----------------
def int_gamma(m2):
    m2 = mp.mpf(m2); Lt = mp.log(1/m2)
    return (1 + m2)*(12*mp.polylog(4, -m2) + Lt**4/4 + mp.pi**2*Lt**2/2 + 7*mp.pi**4/60)/((1 - m2)*(1 + m2)**4)
def int_gamma_ud(m2):
    m2 = mp.mpf(m2); Q2 = (1 + m2)**2; t = m2/Q2; lam = mp.sqrt(1 - 4*t); rho = 2/(1 - 2*t + lam)
    return -(6/lam)*(mp.polylog(4, -1/(rho*t)) - mp.polylog(4, -rho*t))/Q2**2
def LP(m2):
    Lt = mp.log(1/mp.mpf(m2)); return Lt**4/4 + mp.pi**2*Lt**2/2 + 7*mp.pi**4/60
def NLP(m2):
    m2 = mp.mpf(m2); Lt = mp.log(1/m2); return -m2*(Lt**4/2 + mp.pi**2*Lt**2 + 12 + 7*mp.pi**4/30)
print("\n(2) int Gamma: closed form (rho t = m2) vs UD formula; exact int r = int Gamma - LP; NLP formula:")
for m2 in ['0.04', '0.01', '0.0025', '0.000625', '1e-4', '1e-6', '1e-8', '1e-10']:
    g = int_gamma(m2); g2 = int_gamma_ud(m2); r = g - LP(m2); nl = NLP(m2); Lt = mp.log(1/mp.mpf(m2))
    print(f"   m2={m2:>9}: int Gamma={mp.nstr(g,12):>16} (UD diff {mp.nstr(g-g2,3):>8})  int r={mp.nstr(r,10):>16}"
          f"  NLP={mp.nstr(nl,10):>16}  r/NLP={mp.nstr(r/nl,8):>11}  r/(m2 Lt^4)={mp.nstr(r/(mp.mpf(m2)*Lt**4),6):>9}")
# series check with sympy
m, L = sp.symbols('m2 Lt', positive=True)
expr = (1 + m)*(12*(-m) + L**4/4 + sp.pi**2*L**2/2 + 7*sp.pi**4/60)/((1 - m)*(1 + m)**4)
ser = sp.expand(sp.series(expr, m, 0, 2).removeO())
print("   O(m2) coefficient of int Gamma (Li4(-m2) = -m2 + O(m2^2)):", sp.factor(ser.coeff(m, 1)))

# ---------------- (3) comparison with QMC logs ----------------
print("\n(3) QMC estimates vs exact:")
pat_re = re.compile(r"m2=([0-9.e+-]+): int Gamma = ([0-9.e+-]+) \+- ([0-9.e+-]+).*int r = ([0-9.e+-]+) \+- ([0-9.e+-]+)")
for f in ['t12_twoloop_remainder_n16.log', 't12_twoloop_remainder_n18.log', 'r1_twoloop_qmc.log']:
    pth = os.path.join(os.path.dirname(HERE), 'logs', f)
    if not os.path.exists(pth):
        continue
    print("  ", f)
    for line in open(pth):
        mt = pat_re.search(line)
        if not mt: continue
        m2v = mt.group(1); g, ge, r, re_ = map(float, mt.groups()[1:])
        gx = float(int_gamma(m2v)); rx = float(int_gamma(m2v) - LP(m2v))
        print(f"      m2={float(m2v):.3e}: Gamma {g:.4e}+-{ge:.1e} (exact {gx:.4e}, pull {(g-gx)/ge:+.2f});"
              f"  r {r:+.4f}+-{re_:.3f} (exact {rx:+.4f}, pull {(r-rx)/re_:+.2f})")
