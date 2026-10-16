"""X2 final revision / r3_archive_verify.py -- INDEPENDENT exact re-verification of the self-contained certificate
archives logs/r3_triangle_certificates_sc.json.gz (Thm B.4, Prop B.3) and logs/r3_bubble_certificates_sc.json.gz
(Thm B.6).  This script does NOT import r1/r2/r3_lptools or any certificate-producing code; it uses only the archived
data, sympy and exact rationals.  For every piece record with status 'ok' it checks:

 (S) supports: the numerator support (exponents over (local..., m2), frozen variables as coefficients) recomputed from
     the archived numerator string equals the set of certified monomials (one certificate per monomial); every
     denominator factor has coefficients of one sign as a polynomial in (local, m2, frozen) and its support equals the
     archived 'forms'; the comparability constants prod_u (max(hi,1)/min(lo,1))^{deg_u} are recomputed;
 (L) each LP is rebuilt from (forms, cons, weights, monomial):  max <a+w,X> - a_m - sum_k t_k  s.t.
     <b,X> - t_k <= b_m (b in forms[k]),  G X <= h;  the archived dual y satisfies y >= 0, A^T y = c exactly and
     b.y + const = value; the archived primal x satisfies A x <= b and c.x + const = value (exact optimality);
 (F) S+ = {i : y_i > 0}, dim(argmax face) <= nv - rank(A_{S+}) (own exact Gaussian elimination) equals the archived bound;
 (E) record exponent = -2 max_a value_a, L-power = max face bound among maximizing monomials;
 (R) recession: on unbounded cells the exact maximum of psi_inf(r)/|r|_1 over the recession cone (own algorithm:
     quadrant segments |r|_1 = 1, endpoints and tie points) equals the archived slope and is < 0;
 (C) closed forms: the archived rational function equals the density it is claimed to bound, coded independently:
     triangle items/remainder from the closed forms of Prop B.1 (P = P' = 1/sqrt2, du dkappa normalization; sliver in
     (w, kappa) with c = a - w), bubble pieces P0..P4, the corner shells and the u > 1 pieces from the four-shell
     representation T_D, T_e, T_t, T_h (Thm B.6); the identity sum_s T_s = r^(0) (0<u<1) and T_e + T_h = r^(0) (u>1)
     against Prop B.1 is checked symbolically.  Evaluation at random rational points of the cell, ratio constant."""
import sys, os, json, gzip, random
from fractions import Fraction as Fr
from collections import defaultdict
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
HERE = os.path.dirname(os.path.abspath(__file__)); LOGS = os.path.join(os.path.dirname(HERE), 'logs')
random.seed(20261011)

# ------------------------------------------------------------------ exact linear algebra
def rank(rows):
    M = [list(r) for r in rows]; rk = 0; ncol = len(M[0]) if M else 0
    for col in range(ncol):
        piv = next((i for i in range(rk, len(M)) if M[i][col] != 0), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]
        for i in range(len(M)):
            if i != rk and M[i][col] != 0:
                f = M[i][col]/M[rk][col]
                M[i] = [a - f*b for a, b in zip(M[i], M[rk])]
        rk += 1
    return rk

def build(forms, cons, w, a, n):
    K = len(forms); rows, rhs = [], []
    for k, fl in enumerate(forms):
        for b in fl:
            r = [Fr(b[i]) for i in range(n)] + [Fr(0)]*K; r[n + k] = Fr(-1)
            rows.append(r); rhs.append(Fr(b[n]))
    for g, h in cons:
        rows.append([Fr(x) for x in g] + [Fr(0)]*K); rhs.append(Fr(h))
    c = [Fr(a[i]) + w[i] for i in range(n)] + [Fr(-1)]*K
    return rows, rhs, c, Fr(-a[n])

def psi_inf(a, w, forms, r):
    n = len(r)
    return sum((Fr(a[i]) + w[i])*r[i] for i in range(n)) - sum(max(sum(Fr(b[i])*r[i] for i in range(n)) for b in fl) for fl in forms)

def max_slope(a, w, forms, cons, n):
    G = [[Fr(x) for x in g] for g, _ in cons]
    if n == 1:
        vals = [psi_inf(a, w, forms, [Fr(s)]) for s in (1, -1) if all(g[0]*s <= 0 for g in G)]
        return max(vals) if vals else None
    best = None
    for s1 in (1, -1):
        for s2 in (1, -1):
            # r(t) = (s1 t, s2 (1-t)), t in [0,1]; constraints g.r <= 0 linear in t
            lo, hi = Fr(0), Fr(1)
            for g in G:
                A = g[0]*s1 - g[1]*s2; B = g[1]*s2            # A t + B <= 0
                if A == 0:
                    if B > 0: lo, hi = Fr(1), Fr(0)
                elif A > 0: hi = min(hi, -B/A)
                else: lo = max(lo, -B/A)
            if lo > hi: continue
            ts = {lo, hi}
            for fl in forms:
                for i in range(len(fl)):
                    for j in range(i + 1, len(fl)):
                        d0 = Fr(fl[i][0] - fl[j][0]); d1 = Fr(fl[i][1] - fl[j][1])
                        A = d0*s1 - d1*s2; B = d1*s2
                        if A != 0:
                            t = -B/A
                            if lo <= t <= hi: ts.add(t)
            for t in ts:
                r = [s1*t, s2*(1 - t)]
                if r == [0, 0]: continue
                v = psi_inf(a, w, forms, r)                    # |r|_1 = 1 on the segment
                best = v if (best is None or v > best) else best
    return best

# ------------------------------------------------------------------ closed forms (independent)
u, v, kap, m2, w_, c_, gam = sp.symbols('u v kap m2 w c gamma', positive=True)
P = Pp = 1/sp.sqrt(2)
def tri_rho(name, x, k, big):
    """Prop B.1 densities (general-P formulas at P = P' = 1/sqrt2), x = k+, k = kappa"""
    uu = x/P; e2 = m2 + 2*Pp*x; h2 = 2*Pp*x; Qt2 = 2*P*Pp
    A = x*m2*(1 - uu) + P*k; B = x*m2 + P*k
    if name == 'G':
        return 0 if big else 1/(A*(e2*(1 + m2/Qt2 + k/(Qt2*(1 - uu))) + k))
    if name == 'S': return 1/(B*e2)
    if name == 'C1': return -1/(h2*B) if big else x*m2/(Qt2*A*B)
    if name == 'C2': return -1/(P*e2*(e2 + k))
    if name == 'H': return 1/(P*(h2 + k)*h2) if big else -x/(P*(h2 + k)*(h2*(P - x) + P*k))
def tri_expected(combo, big):
    x = P*u
    return P*sum(s*tri_rho(nm, x, kap, big) for nm, s in combo)   # du dkappa normalization: dx = P du
def sliver_expected():
    a = m2/Pp; x = (w_ - a)/2; km = Pp + kap/w_
    Dg = -2*x*km + kap; D1 = -2*(P - x)*(-m2/(2*P) - km) + kap
    rG = 2/(w_*Dg*D1); rC2 = w_/(P*((a - w_)*Pp*w_ + a*kap)*(Pp*w_ + kap))
    return rG - rC2
DG = (m2 + u)*(v*(1 + m2) + kap) + kap*v
TS = {'D': (v/DG - 1/u)/(u*m2*v + kap), 'e': m2/(u*(m2 + u)*(u*m2 + kap)), 't': 1/(u*(u*v + kap)),
      'h': 1/((m2 + u)*(m2 + u + kap)) - 1/(u*(u + kap))}
WA = [u*m2/kap, sp.Integer(1)]; WB = [u/v, sp.Integer(1)]; WD = [u**2*m2/(u*m2*v + kap), sp.Integer(1)]
def bubble_expected(part, piece, alt):
    S = lambda *ss: sum(TS[s] for s in ss)
    if part.startswith('remainder 0<u<1'):
        if piece.startswith('shell '): return TS[piece.split()[1]]
        if piece == 'P0': return S('D', 'e', 't', 'h')
        if piece == 'P1': return WA[alt]*S('D', 'e')
        if piece == 'P2': return WB[alt]*S('D', 't')
        if piece == 'P3': return WD[alt]*TS['D']
        if piece == 'P4': return [WA[0]*WB[0], WA[0]*WB[1], WA[1]*WB[0], WA[1]*WB[1]][alt]*TS['D']
    if part == 'remainder u>1':
        if piece == 'rho_r': return S('e', 'h')
        if piece == 'w_a|T_e|': return WA[alt]*TS['e']
    return None
def tri_combo(label):
    if '(H1)_S' in label: return [('G', 1), ('S', -1)]
    if '(H1)_C1' in label: return [('S', -1), ('C1', -1)] if label.endswith('III') else [('G', 1), ('S', -1), ('C1', -1)]
    if '(H1)_C2' in label: return [('G', 1), ('S', -1), ('C2', -1)]
    if label.startswith('r cell'): return [('G', 1), ('S', -1), ('C1', -1), ('C2', -1), ('H', -1)]
    if label.startswith('r u>1'): return [('S', -1), ('C1', -1), ('C2', -1), ('H', -1)]
    if '(H2)' in label:
        toks = label.split()
        i = next(i for i, t in enumerate(toks) if t.startswith('(H2)'))
        return [(toks[i + 1], 1)]
    raise ValueError(label)

def rnd(lo, hi):
    return Fr(random.randint(1, 10**6), 10**6)*(hi - lo) + lo

def same(r, r0):
    """exact equality of two algebraic numbers (radical simplification), with a 60-digit numerical fallback"""
    d = sp.radsimp(sp.nsimplify(r) - sp.nsimplify(r0))
    if sp.simplify(d) == 0:
        return True
    return abs(sp.N(r - r0, 80)) < sp.Float('1e-60')*max(1, abs(sp.N(r0, 80)))

def closed_form_check(lp, expected, sampler):
    syms = {s: sp.Symbol(s, positive=True) for s in lp['local'] + [lp['m2']] + list(lp['frozen'].keys())}
    num = sp.sympify(lp['num'], locals=syms); den = sp.Mul(*[sp.sympify(d, locals=syms) for d in lp['dens']])
    ratios = []
    for _ in range(3):
        pt = sampler()
        an = (num/den).subs({syms[k]: sp.Rational(val.numerator, val.denominator) for k, val in pt.items() if k in syms})
        ex = expected.subs({sp.Symbol(k, positive=True): sp.Rational(val.numerator, val.denominator) for k, val in pt.items()})
        an = sp.nsimplify(sp.simplify(an)); ex = sp.simplify(ex)
        if ex == 0:
            return False, 'expected vanishes'
        ratios.append(sp.simplify(an/ex))
    ok = all(same(r, ratios[0]) for r in ratios) and ratios[0] != 0
    return ok, ratios[0]

# ------------------------------------------------------------------ record verification
STATS = defaultdict(int); FAIL = []; MINEXP = {}; MAXSLOPE = {}; MAXL = 0
def verify_record(tag, lp, certs, exponent, Lpow, slope):
    global MAXL
    loc = lp['local']; n = len(loc); fz = lp['frozen']
    syms = {s: sp.Symbol(s, positive=True) for s in loc + [lp['m2']] + list(fz.keys())}
    gens = [syms[s] for s in loc] + [syms[lp['m2']]]
    w = [Fr(x) for x in lp['weights']]; cons = [([Fr(x) for x in g], Fr(h)) for g, h in lp['cons']]
    forms = [[tuple(b) for b in fl] for fl in lp['forms']]
    # (S) supports
    num = sp.expand(sp.sympify(lp['num'], locals=syms))
    sup = {tuple(int(e) for e in m) for m in sp.Poly(num, *gens).monoms()}
    cm = [tuple(c['monomial']) for c in certs]
    if sup != set(cm) or len(cm) != len(set(cm)):
        FAIL.append((tag, 'numerator support')); return
    for k, d in enumerate(lp['dens']):
        f = sp.expand(sp.sympify(d, locals=syms))
        co = sp.Poly(f, *(gens + [syms[z] for z in fz])).coeffs()
        if not (all(x > 0 for x in co) or all(x < 0 for x in co)):
            FAIL.append((tag, f'denominator {k} not sign-definite')); return
        if {tuple(int(e) for e in m) for m in sp.Poly(f, *gens).monoms()} != set(forms[k]):
            FAIL.append((tag, f'denominator {k} support')); return
        if fz:
            const = Fr(1)
            for z, (lo, hi) in fz.items():
                dg = sp.Poly(f, syms[z]).degree()
                const *= (max(Fr(hi), Fr(1))/min(Fr(lo), Fr(1)))**dg
            if lp['comparability'] and Fr(lp['comparability'][k]) != const:
                FAIL.append((tag, 'comparability constant')); return
    STATS['supports ok'] += 1
    # (L), (F), (R)
    vals = []; slopes = []
    for c in certs:
        a = [int(x) for x in c['monomial']]
        rows, rhs, cvec, const = build(forms, cons, w, a, n)
        y = {int(i): Fr(val) for i, val in c['dual'].items()}
        if any(val < 0 for val in y.values()):
            FAIL.append((tag, 'negative dual')); return
        if any(sum(y[i]*rows[i][j] for i in y) != cvec[j] for j in range(len(cvec))):
            FAIL.append((tag, 'A^T y != c')); return
        value = Fr(c['value'])
        if sum(y[i]*rhs[i] for i in y) + const != value:
            FAIL.append((tag, 'dual value')); return
        x = [Fr(val) for val in c['primal']]
        if any(sum(r[j]*x[j] for j in range(len(x))) > b for r, b in zip(rows, rhs)):
            FAIL.append((tag, 'primal infeasible')); return
        if sum(cvec[j]*x[j] for j in range(len(x))) + const != value:
            FAIL.append((tag, 'primal value')); return
        Sp = sorted(i for i, val in y.items() if val > 0)
        if Sp != sorted(int(i) for i in c['Splus']):
            FAIL.append((tag, 'S+')); return
        db = len(cvec) - (rank([rows[i] for i in Sp]) if Sp else 0)
        if db != c['dim_bound']:
            FAIL.append((tag, f'face bound {db} != {c["dim_bound"]}')); return
        vals.append((value, db))
        s = max_slope(a, w, forms, cons, n)
        if s is not None:
            if s >= 0:
                FAIL.append((tag, f'recession slope {s} >= 0')); return
            slopes.append(s)
        STATS['certificates ok'] += 1
    mx = max(v_ for v_, _ in vals)
    if Fr(exponent) != -2*mx:
        FAIL.append((tag, 'exponent')); return
    if Lpow != max(d for v_, d in vals if v_ == mx):
        FAIL.append((tag, 'L-power')); return
    arch_slope = None if slope in (None, 'None') else Fr(slope)
    my_slope = max(slopes) if slopes else None
    if arch_slope != my_slope:
        FAIL.append((tag, f'slope {my_slope} != archived {arch_slope}')); return
    MAXL = max(MAXL, Lpow)
    STATS['records ok'] += 1

def sampler_tri(cell, lp):
    def f():
        m = rnd(Fr(1, 1000), Fr(1, 3)); k = rnd(Fr(1, 100), Fr(3))
        if cell == 'I':
            uu = rnd(Fr(1, 100), Fr(1, 2)); return {'u': uu, 'kap': k, 'm2': m, 'v': 1 - uu}
        if cell == 'II':
            vv = rnd(Fr(1, 100), Fr(1, 2)); return {'v': vv, 'kap': k, 'm2': m, 'u': 1 - vv}
        if cell == 'III':
            return {'u': rnd(Fr(1), Fr(2)), 'kap': k, 'm2': m}
        return {'u': rnd(Fr(1), Fr(5)), 'kap': k, 'm2': m}
    return f

def run_triangle(path):
    arc = json.load(gzip.open(path))
    ncf = 0
    for rec in arc:
        if rec['status'] != 'ok': continue
        tag = f"triangle | {rec['label']} | eps={rec['eps']}"
        verify_record(tag, rec['lpdata'], rec['certs'], rec['exponent'], rec['Lpow'], rec['slope'])
        key = ('triangle ' + rec['kind'] + (f" theta={rec['theta']}" if rec['theta'] else ''), rec['eps'])
        MINEXP[key] = min(MINEXP.get(key, Fr(99)), Fr(rec['exponent']))
        lp = rec['lpdata']
        if rec['kind'] == 'sliver':
            # exact sampling on the manifold c = a - w with irrational a: evaluate symbolically
            syms = {s: sp.Symbol(s, positive=True) for s in lp['local'] + [lp['m2']] + list(lp['frozen'].keys())}
            num = sp.sympify(lp['num'], locals=syms); den = sp.Mul(*[sp.sympify(d, locals=syms) for d in lp['dens']])
            ratios = []
            for _ in range(3):
                mm = sp.Rational(random.randint(1, 999), 3000); kk = sp.Rational(random.randint(1, 3000), 1000)
                aa = sp.sqrt(2)*mm
                if 'w' in lp['local']:
                    ww = aa*sp.Rational(random.randint(1, 499), 1000)       # w <= a/2
                    cc = aa - ww; sub = {syms['w']: ww, syms['kap']: kk, syms['m2']: mm, syms['gamma']: cc/mm}
                else:
                    ww = aa*sp.Rational(random.randint(501, 999), 1000)     # w >= a/2
                    cc = aa - ww; sub = {syms['c']: cc, syms['kap']: kk, syms['m2']: mm, syms['gamma']: ww/mm}
                an = sp.simplify((num/den).subs(sub))
                ex = sp.simplify(sliver_expected().subs({w_: ww, kap: kk, m2: mm}))
                ratios.append(sp.nsimplify(sp.simplify(an/ex)))
            ok = all(same(r_, ratios[0]) for r_ in ratios)
            STATS['triangle closed-form ok' if ok else 'triangle closed-form FAIL'] += 1
            if not ok: FAIL.append((tag, f'closed form ratios {ratios}'))
            continue
        combo = tri_combo(rec['label'])
        big = rec['cell'] in ('III', 'BIG')
        ok, ratio = closed_form_check(lp, tri_expected(combo, big), sampler_tri(rec['cell'], lp))
        STATS['triangle closed-form ok' if ok else 'triangle closed-form FAIL'] += 1
        if not ok: FAIL.append((tag, f'closed form {ratio}'))
        ncf += 1
    print(f"triangle archive: {len(arc)} piece records")

def run_bubble(path):
    arc = json.load(gzip.open(path))
    for ent in arc:
        rec = ent['record']
        if not rec or rec.get('status') != 'ok': continue
        tag = f"bubble | {ent['part']} | {ent['cell']} | {ent['piece']} | alt {ent['alternative']} | eps={ent['eps']}"
        verify_record(tag, rec['lpdata'], rec['certs'], rec['exponent'], rec['Lpow'], rec['slope'])
        key = ('bubble ' + ent['part'], ent['eps'])
        MINEXP[key] = min(MINEXP.get(key, Fr(99)), Fr(rec['exponent']))
        ex = bubble_expected(ent['part'], ent['piece'], ent['alternative'])
        if ex is None:
            STATS['bubble closed-form not applicable (items)'] += 1; continue
        region = rec['region']
        cell = {'I': 'I', 'II': 'II', 'BIG': 'BIG'}[region]
        ok, ratio = closed_form_check(rec['lpdata'], ex.subs(v, 1 - u) if region != 'II' else ex.subs(v, 1 - u),
                                      sampler_tri(cell, rec['lpdata']))
        STATS['bubble closed-form ok' if ok else 'bubble closed-form FAIL'] += 1
        if not ok: FAIL.append((tag, f'closed form {ratio}'))
    print(f"bubble archive: {len(arc)} piece records")

if __name__ == "__main__":
    # symbolic consistency of the four-shell representation with Prop B.1 (j = 0 remainder)
    r_small = sp.simplify((tri_expected([('G', 1), ('S', -1), ('C1', -1), ('C2', -1), ('H', -1)], False)
                           - sum(TS.values()).subs(v, 1 - u)))
    r_big = sp.simplify((tri_expected([('S', -1), ('C1', -1), ('C2', -1), ('H', -1)], True) - (TS['e'] + TS['h'])))
    print("four-shell representation vs Prop B.1:  0<u<1:", r_small == 0, "  u>1:", r_big == 0)
    parts = sys.argv[1:] or ['triangle', 'bubble']
    if 'triangle' in parts: run_triangle(os.path.join(LOGS, 'r3_triangle_certificates_sc.json.gz'))
    if 'bubble' in parts: run_bubble(os.path.join(LOGS, 'r3_bubble_certificates_sc.json.gz'))
    print("checks passed:", dict(STATS))
    print("failures:", len(FAIL))
    for f in FAIL[:20]: print("   ", f)
    print("max L-power bound used:", MAXL)
    for k in sorted(MINEXP): print(f"   min exponent {k[0]:40s} eps={k[1]:>5s}: {MINEXP[k]}")
    print("ALL CHECKS PASS" if not FAIL else "SOME CHECKS FAIL")
