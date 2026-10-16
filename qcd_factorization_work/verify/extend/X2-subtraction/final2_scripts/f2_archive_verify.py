"""X2 final2 / f2_archive_verify.py -- final-review Fix 8: independent EXACT re-verification of the certificate archives
logs/r3_triangle_certificates_sc.json.gz (Thm B.5) and logs/r3_bubble_certificates_sc.json.gz (Thm B.8), removing the
two limitations of r3_archive_verify.py:
 (C') closed forms: every archived rational function f_arch is proven equal to c * f_exp for a non-zero constant c by an
      exact POLYNOMIAL IDENTITY over Q(sqrt2) (sqrt2 kept as a symbol s2 and reduced modulo s2^2 - 2), where f_exp is the
      density coded independently from Prop B.1 (triangle items, remainder, sliver), from the four-shell representation
      (bubble pieces P0..P4, corner shells, u > 1 pieces) and -- new -- from the shell forms of the log-weighted ITEMS
      (main parts and log-difference corrections, 48 records); the shell forms are themselves checked exactly against
      Prop B.1.  The constant c is obtained at one exact rational point; no random points are used.
 (V)  coverage: for every region the union of the archived LP cells is proven to contain the (relaxed) target region,
      by exact rational polygon subtraction in normalized log coordinates (target ∩ box minus cells has zero area; the
      box contains every vertex of the line arrangement of the target, the cells and the coordinate axes, so every
      face of that arrangement meets the box in positive area); 1D cells by interval inclusion.
 (Pc) piece completeness: every remainder cell carries P0..P4 (each with one certified alternative), every u > 1 cell
      carries rho_r and w_a|T_e|, the corner carries the four shells, every item cell carries the main part and the
      corrections that connect all shells of the item's terms.
The LP checks (S), (L), (F), (E), (R) of r3_archive_verify.py are repeated verbatim (no certificate-producing code is
imported; only the archived data, sympy and exact rationals).
Run: python3 -I f2_archive_verify.py [triangle] [bubble] [--no-lp]   (log: ../final2_logs/f2_archive_verify.log)"""
import sys, os, json, gzip, itertools
from fractions import Fraction as Fr
from collections import defaultdict
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import functools
print = functools.partial(print, flush=True)
HERE = os.path.dirname(os.path.abspath(__file__)); LOGS = os.path.join(os.path.dirname(HERE), 'logs')

# ================================================================== LP checks (verbatim from r3_archive_verify.py)
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
            lo, hi = Fr(0), Fr(1)
            for g in G:
                A = g[0]*s1 - g[1]*s2; B = g[1]*s2
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
                v = psi_inf(a, w, forms, r)
                best = v if (best is None or v > best) else best
    return best

STATS = defaultdict(int); FAIL = []; MINEXP = {}; MAXL = 0
def verify_record(tag, lp, certs, exponent, Lpow, slope):
    global MAXL
    loc = lp['local']; n = len(loc); fz = lp['frozen']
    syms = {s: sp.Symbol(s, positive=True) for s in loc + [lp['m2']] + list(fz.keys())}
    gens = [syms[s] for s in loc] + [syms[lp['m2']]]
    w = [Fr(x) for x in lp['weights']]; cons = [([Fr(x) for x in g], Fr(h)) for g, h in lp['cons']]
    forms = [[tuple(b) for b in fl] for fl in lp['forms']]
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

# ================================================================== independent closed forms (exact, sqrt2 -> s2)
u, v, kap, m2, w_, c_, gam = sp.symbols('u v kap m2 w c gamma', positive=True)
s2 = sp.Symbol('s2', positive=True)                 # s2 = sqrt(2), reduced modulo s2^2 - 2
P = Pp = 1/s2                                       # P = P' = 1/sqrt2
def tri_rho(name, x, k, big):
    """Prop B.1 densities (general-P formulas at P = P' = 1/sqrt2), x = k+, k = kappa"""
    uu = x/P; e2 = m2 + 2*Pp*x; h2 = 2*Pp*x; Qt2 = 2*P*Pp
    A = x*m2*(1 - uu) + P*k; Bq = x*m2 + P*k
    if name == 'G': return 0 if big else 1/(A*(e2*(1 + m2/Qt2 + k/(Qt2*(1 - uu))) + k))
    if name == 'S': return 1/(Bq*e2)
    if name == 'C1': return -1/(h2*Bq) if big else x*m2/(Qt2*A*Bq)
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
# shell forms of the log-weighted items (0 < u < 1, v = 1 - u, du dkappa normalization), verified against Prop B.1 below:
# Gamma = l_D^j rG; C_S = l_e^j rS; C_C1 = l_D^j a1 - l_e^j a2; C_C2 = l_h^j rC2; C_H = -l_t^j b1 + l_h^j b2
SH = {'rG': v/((u*m2*v + kap)*DG), 'rS': 1/((u*m2 + kap)*(m2 + u)), 'a1': 1/(u*(u*m2*v + kap)), 'a2': 1/(u*(u*m2 + kap)),
      'rC2': -1/((m2 + u + kap)*(m2 + u)), 'b1': 1/(u*(u*v + kap)), 'b2': 1/(u*(u + kap))}
SHELL_OF = {'rG': 'D', 'rS': 'e', 'a1': 'D', 'a2': 'e', 'rC2': 'h', 'b1': 't', 'b2': 'h'}
WPAIR = {('D', 'e'): u/v, ('t', 'h'): u/v, ('D', 'h'): u*(m2*v + kap)/(v*kap), ('e', 'h'): u*m2/kap, ('D', 't'): u*m2*v/kap}
TERMS = {'Gamma': [('rG', 1)], 'C_S': [('rS', 1)], 'C_C1': [('a1', 1), ('a2', -1)], 'C_C2': [('rC2', 1)],
         'C_H': [('b1', -1), ('b2', 1)]}
ITEM_TERMS = {   # item label -> signed list of Collins objects whose densities form the item
 '(H1)_S  G-S': [('Gamma', 1), ('C_S', -1)], '(H2)_S  C_C1': [('C_C1', 1)], '(H2)_S  C_C2': [('C_C2', 1)],
 '(H2)_S  C_H': [('C_H', 1)], '(H1)_C1 G-S-C1': [('Gamma', 1), ('C_S', -1), ('C_C1', -1)],
 '(H1)_C2 alt': [('Gamma', 1), ('C_S', -1), ('C_C2', -1)]}
def item_rational_terms(label):
    out = []
    for obj, s in ITEM_TERMS[label]:
        for nm, s2_ in TERMS[obj]: out.append((nm, s*s2_))
    return out
def item_expected(label, piece, alt):
    """main = the j = 0 item (sum of all its rational terms); corr (a, b) = [weight] x (sum of the item's terms whose
       shell is the first member a of the pair, after the reference has been moved to b along the chain)"""
    terms = item_rational_terms(label)
    if piece == 'main':
        return sum(s*SH[nm] for nm, s in terms)
    pair = tuple(piece[len('corr '):].strip("()").replace("'", "").replace(' ', '').split(','))
    # terms carried by a correction (a,b): those on shell a; for the chain D -> e -> h of '(H1)_C2 alt' the archive's
    # (e,h) correction carries rC2 (moved from h to e: sign flipped relative to the l_h^j term) -- see LOGIC below
    return pair, terms

def reduce_s2(expr):
    """exact reduction of a polynomial in s2 modulo s2^2 - 2"""
    p = sp.Poly(sp.expand(expr), s2)
    q = sp.rem(p, sp.Poly(s2**2 - 2, s2))
    return q.as_expr()

def exact_identity(arch, expct, gens, pt):
    """prove arch = c * expct exactly, c a non-zero constant in Q(sqrt2): c is computed at the rational point pt with s2
       kept symbolic (c = cn(s2)/cd(s2)); the identity a_n e_d cd - cn e_n a_d = 0 is then checked as a polynomial
       identity in Q[variables][s2] modulo the minimal polynomial s2^2 - 2.  Returns (ok, c at s2 = sqrt2)."""
    a_n, a_d = sp.fraction(sp.together(arch)); e_n, e_d = sp.fraction(sp.together(expct))
    av = sp.together(arch.subs(pt)); ev = sp.together(expct.subs(pt))
    if reduce_s2(sp.fraction(ev)[0]) == 0 or reduce_s2(sp.fraction(av)[0]) == 0:
        return False, 'vanishes at the test point'
    c = sp.together(av/ev)
    cn, cd = sp.fraction(c)
    poly = sp.expand(a_n*e_d*cd - cn*e_n*a_d)
    red = sp.expand(reduce_s2(poly)) if poly.has(s2) else poly
    ok = (red == 0)
    cval = sp.nsimplify(sp.radsimp(c.subs(s2, sp.sqrt(2))))
    return ok, cval

# ================================================================== exact 2D coverage by polygon subtraction
def clip(poly, g, h, sense):
    """Sutherland-Hodgman: keep {X : g.X <= h} (sense = 'le') or {g.X >= h} ('ge'); exact Fractions"""
    def val(p): return g[0]*p[0] + g[1]*p[1] - h
    inside = (lambda t: t <= 0) if sense == 'le' else (lambda t: t >= 0)
    out = []
    n = len(poly)
    for i in range(n):
        P1, P2 = poly[i], poly[(i + 1) % n]
        v1, v2 = val(P1), val(P2)
        if inside(v1): out.append(P1)
        if (v1 < 0 < v2) or (v2 < 0 < v1):
            t = v1/(v1 - v2)
            out.append((P1[0] + t*(P2[0] - P1[0]), P1[1] + t*(P2[1] - P1[1])))
    # remove consecutive duplicates
    res = []
    for p in out:
        if not res or res[-1] != p: res.append(p)
    if len(res) > 1 and res[0] == res[-1]: res.pop()
    return res
def area(poly):
    if len(poly) < 3: return Fr(0)
    s = Fr(0)
    for i in range(len(poly)):
        x1, y1 = poly[i]; x2, y2 = poly[(i + 1) % len(poly)]
        s += x1*y2 - x2*y1
    return abs(s)/2
def subtract(poly, cell):
    pieces = []; cur = poly
    for g, h in cell:
        out = clip(cur, g, h, 'ge')
        if area(out) > 0: pieces.append(out)
        cur = clip(cur, g, h, 'le')
        if area(cur) == 0: break
    return pieces
def line_set(conslists):
    L = set()
    for cl in conslists:
        for g, h in cl: L.add((Fr(g[0]), Fr(g[1]), Fr(h)))
    L.add((Fr(1), Fr(0), Fr(0))); L.add((Fr(0), Fr(1), Fr(0)))          # coordinate axes
    return list(L)
def box_size(lines):
    M = Fr(1)
    for (a1, b1, c1), (a2, b2, c2) in itertools.combinations(lines, 2):
        det = a1*b2 - a2*b1
        if det != 0:
            x = (c1*b2 - c2*b1)/det; y = (a1*c2 - a2*c1)/det
            M = max(M, abs(x), abs(y))
    return 2*M + 10
def covers_2d(target, cells):
    """exact: target (list of (g,h), g.X <= h) contained in the union of cells (each a list of (g,h)), up to measure 0"""
    cl = [[([Fr(x) for x in g], Fr(h)) for g, h in c] for c in cells]
    tg = [([Fr(x) for x in g], Fr(h)) for g, h in target]
    M = box_size(line_set(cl + [tg]))
    poly = [(-M, -M), (M, -M), (M, M), (-M, M)]
    for g, h in tg: poly = clip(poly, g, h, 'le')
    remaining = [poly] if area(poly) > 0 else []
    for c in cl:
        new = []
        for p in remaining: new.extend(subtract(p, c))
        remaining = new
        if not remaining: break
    return (len(remaining) == 0), sum((area(p) for p in remaining), Fr(0)), M
def covers_1d(target_iv, cells):
    """target interval (lo, hi) (None = infinite) contained in the union of 1D cells given as lists of (g,h), g = [+-1]"""
    ivs = []
    for c in cells:
        lo, hi = None, None
        for g, h in c:
            g0 = Fr(g[0]); h0 = Fr(h)
            if g0 > 0: hi = h0/g0 if hi is None else min(hi, h0/g0)
            else: lo = h0/g0 if lo is None else max(lo, h0/g0)
        ivs.append((lo, hi))
    lo_t, hi_t = target_iv
    # sweep: does the union of closed intervals contain [lo_t, hi_t]?
    pts = sorted({x for iv in ivs for x in iv if x is not None} | {x for x in target_iv if x is not None})
    probes = []
    if pts:
        probes.append(pts[0] - 1); probes.append(pts[-1] + 1)
        probes += [(p + q)/2 for p, q in zip(pts, pts[1:])]
    else:
        probes = [Fr(0)]
    def inside(x, iv): return (iv[0] is None or x >= iv[0]) and (iv[1] is None or x <= iv[1])
    for x in probes:
        if inside(x, target_iv) and not any(inside(x, iv) for iv in ivs): return False
    return True

# ================================================================== drivers
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

def arch_expr(lp):
    syms = {s: sp.Symbol(s, positive=True) for s in lp['local'] + [lp['m2']] + list(lp['frozen'].keys())}
    num = sp.sympify(lp['num'], locals=syms); den = sp.Mul(*[sp.sympify(d, locals=syms) for d in lp['dens']])
    return num/den, syms

CF_OK = defaultdict(int)
def check_closed_form(tag, lp, expected, mode):
    """mode: 'u' (local u or v with v = 1 - u), 'sliverA', 'sliverB'"""
    f, syms = arch_expr(lp)
    f = f.subs(sp.sqrt(2), s2)                       # archived sliver functions carry sqrt(2) explicitly
    S = lambda n: sp.Symbol(n, positive=True)
    if mode == 'u':
        f = f.subs({S('v'): 1 - u}) if 'v' in syms else f
        e = expected.subs(v, 1 - u)
        pt = {u: sp.Rational(3, 7), kap: sp.Rational(5, 11), m2: sp.Rational(2, 13)}
        gens = [u, kap, m2]
        if 'u' not in syms and 'v' in syms: pass
    elif mode == 'sliverA':
        f = f.subs({S('gamma'): (s2*m2 - w_)/m2})
        e = expected; pt = {w_: sp.Rational(1, 50), kap: sp.Rational(5, 11), m2: sp.Rational(2, 13)}
    else:
        f = f.subs({S('c'): s2*m2 - w_, S('gamma'): w_/m2})
        e = expected; pt = {w_: sp.Rational(1, 5), kap: sp.Rational(5, 11), m2: sp.Rational(2, 13)}
    ok, cval = exact_identity(f, e, None, pt)
    CF_OK['ok' if ok else 'FAIL'] += 1
    if not ok: FAIL.append((tag, f'closed form not identical (c = {cval})'))
    return ok, cval

def run_triangle(do_lp):
    arc = json.load(gzip.open(os.path.join(LOGS, 'r3_triangle_certificates_sc.json.gz')))
    consts = defaultdict(set)
    for rec in arc:
        if rec['status'] != 'ok': continue
        tag = f"triangle | {rec['label']} | eps={rec['eps']}"
        if do_lp: verify_record(tag, rec['lpdata'], rec['certs'], rec['exponent'], rec['Lpow'], rec['slope'])
        key = ('triangle ' + rec['kind'] + (f" theta={rec['theta']}" if rec['theta'] else ''), rec['eps'])
        MINEXP[key] = min(MINEXP.get(key, Fr(99)), Fr(rec['exponent']))
        lp = rec['lpdata']
        if rec['kind'] == 'sliver':
            ok, cval = check_closed_form(tag, lp, sliver_expected(), 'sliverA' if 'w' in lp['local'] else 'sliverB')
        else:
            big = rec['cell'] in ('III', 'BIG')
            ok, cval = check_closed_form(tag, lp, tri_expected(tri_combo(rec['label']), big), 'u')
        consts[str(cval)].add(rec['kind'])
    print(f"   triangle archive: {len(arc)} piece records; closed-form constants c (archived = c x Prop B.1): "
          f"{ {k: sorted(v_) for k, v_ in consts.items()} }")
    return arc

def run_bubble(do_lp):
    arc = json.load(gzip.open(os.path.join(LOGS, 'r3_bubble_certificates_sc.json.gz')))
    consts = defaultdict(int)
    for ent in arc:
        rec = ent['record']
        if not rec or rec.get('status') != 'ok': continue
        tag = f"bubble | {ent['part']} | {ent['cell']} | {ent['piece']} | alt {ent['alternative']} | eps={ent['eps']}"
        if do_lp: verify_record(tag, rec['lpdata'], rec['certs'], rec['exponent'], rec['Lpow'], rec['slope'])
        key = ('bubble ' + ent['part'], ent['eps'])
        MINEXP[key] = min(MINEXP.get(key, Fr(99)), Fr(rec['exponent']))
        if ent['part'].startswith('items'):
            label = ent['cell'][1]; piece = ent['piece']
            if piece == 'main':
                ex = sum(s*SH[nm] for nm, s in item_rational_terms(label))
            else:
                pair = tuple(piece[len('corr '):].strip("()").replace("'", "").replace(' ', '').split(','))
                ex = CORR_EXPECTED[(label, pair)]
                if ent['alternative'] == 1: ex = WPAIR[pair]*ex
            ok, cval = check_closed_form(tag, rec['lpdata'], ex, 'u')
        else:
            ex = bubble_expected(ent['part'], ent['piece'], ent['alternative'])
            ok, cval = check_closed_form(tag, rec['lpdata'], ex, 'u')
        consts[str(cval)] += 1
    print(f"   bubble archive: {len(arc)} piece records; closed-form constants c: {dict(consts)}")
    return arc

# The log-difference corrections of the items: writing each item as l_ref^j (sum of terms) + sum over shells s != ref of
# (l_s^j - l_ref^j) (terms on shell s), the archive uses a chain of pairs; the rational factor certified for a pair (a, b)
# is the sum of the item's terms that sit on shell a when the reference is b, for the items below:
CORR_EXPECTED = {
 ('(H1)_S  G-S', ('D', 'e')): SH['rG'],                       # l_e^j (G - S) + (l_D^j - l_e^j) G
 ('(H2)_S  C_C1', ('D', 'e')): SH['a1'],                      # l_e^j (a1 - a2) + (l_D^j - l_e^j) a1
 ('(H2)_S  C_H', ('t', 'h')): SH['b1'],                       # l_h^j (b2 - b1) - (l_t^j - l_h^j) b1   (|.| certified)
 ('(H1)_C1 G-S-C1', ('D', 'e')): SH['rG'] - SH['a1'],          # l_e^j (G - S - a1 + a2) + (l_D^j - l_e^j)(G - a1)
 ('(H1)_C2 alt', ('e', 'h')): SH['rC2'],                      # l_e^j (G - S - C2) + (l_e^j - l_h^j) C2
 ('(H1)_C2 alt', ('D', 'e')): SH['rG'],                       #                    + (l_D^j - l_e^j) G
}
def check_item_algebra():
    """exact: (i) shell forms = Prop B.1 densities; (ii) each item decomposition reproduces the item for every shell
       assignment of logarithms (identity in independent symbols l_D, l_e, l_t, l_h, any j = 1, 2, 3); (iii) the
       corrections present connect all shells of the item's terms"""
    ok = True
    x = P*u
    chk = {'rG': tri_expected([('G', 1)], False), 'rS': tri_expected([('S', 1)], False),
           'a1-a2': tri_expected([('C1', 1)], False), 'rC2': tri_expected([('C2', 1)], False),
           'b2-b1': tri_expected([('H', 1)], False)}
    mine = {'rG': SH['rG'], 'rS': SH['rS'], 'a1-a2': SH['a1'] - SH['a2'], 'rC2': SH['rC2'], 'b2-b1': SH['b2'] - SH['b1']}
    for k in chk:
        d = sp.together((mine[k] - chk[k]).subs(v, 1 - u))
        nm_, _ = sp.fraction(d)
        r = reduce_s2(sp.expand(nm_))
        good = sp.expand(r) == 0
        print(f"   shell form {k:6s} = Prop B.1 density (du dkappa normalization): {good}")
        ok &= good
    # T_C1 Gamma on the D shell and T_C1 T_S Gamma on the e shell: residue poles (check the separate pieces)
    ls = {s: sp.Symbol('l_' + s) for s in 'Deth'}
    for label, terms in ITEM_TERMS.items():
        rterms = item_rational_terms(label)
        shells = sorted({SHELL_OF[nm] for nm, _ in rterms})
        corrs = [p for (lab, p) in CORR_EXPECTED if lab == label]
        # connectivity of the shells through the correction pairs
        comp = {shells[0]} if shells else set()
        changed = True
        while changed:
            changed = False
            for a_, b_ in corrs:
                if (a_ in comp) != (b_ in comp): comp |= {a_, b_}; changed = True
        conn = comp == set(shells) or len(shells) <= 1
        # algebraic identity for j = 1, 2, 3 with the reference = the second member of the last pair (or the only shell)
        ident = True
        for j in (1, 2, 3):
            lhs = sum(s*ls[SHELL_OF[nm]]**j*SH[nm] for nm, s in rterms)
            if not corrs:
                ref = shells[0]
                rhs = ls[ref]**j*sum(s*SH[nm] for nm, s in rterms)
            elif label == '(H1)_C2 alt':
                rhs = (ls['e']**j*sum(s*SH[nm] for nm, s in rterms) + (ls['e']**j - ls['h']**j)*SH['rC2']
                       + (ls['D']**j - ls['e']**j)*SH['rG'])
            elif label == '(H2)_S  C_H':
                rhs = ls['h']**j*(SH['b2'] - SH['b1']) - (ls['t']**j - ls['h']**j)*SH['b1']
            else:
                (a_, b_), = corrs
                rhs = ls[b_]**j*sum(s*SH[nm] for nm, s in rterms) + (ls[a_]**j - ls[b_]**j)*CORR_EXPECTED[(label, (a_, b_))]
            ident &= sp.simplify(sp.expand(lhs - rhs)) == 0
        print(f"   item {label:18s}: shells {shells}, corrections {corrs}; decomposition identity (j=1,2,3): {ident};"
              f" corrections connect all shells: {conn}")
        ok &= ident and conn
    return ok

def run_coverage(tri, bub):
    ok_all = True
    print("\n(V) coverage (exact)")
    # ---- triangle: items theta = 1, 2 (relaxed targets in each strip), remainder, sliver
    def tcells(label, eps):
        return [r for r in tri if r['label'] == label and r['eps'] == eps and r['status'] == 'ok']
    for eps in ['0', '1/10']:
        for th in ([Fr(2), Fr(1)] if eps == '0' else [Fr(2)]):
            t2 = th/2
            targets = {   # (item label stem, strip) -> relaxed target in that strip's log coordinates
             'U_S': [('I', [([1, 0], -t2), ([-1, 1], -t2)])],
             'U_C1': [('I', [([1, 0], 0), ([-1, 0], t2), ([-1, 1], -t2)]), ('II', [([1, 0], 0), ([0, 1], -t2)]),
                      ('III', [([1], -t2)])],
             'U_C2': [('I', [([1, 0], -t2), ([1, -1], t2), ([-1, 1], 0)])]}
            items = {'U_S': ['(H1)_S  G-S', '(H2)_S  C1', '(H2)_S  C2', '(H2)_S  H'],
                     'U_C1': ['(H1)_C1', '(H2)_C1 C2', '(H2)_C1 H'],
                     'U_C2': ['(H1)_C2 (u>0)', '(H2)_C2 C1', '(H2)_C2 H']}
            for U, labs in items.items():
                for lab in labs:
                    for strip, tg in targets[U]:
                        full = f"theta={th} {lab}" + ('' if U in ('U_S', 'U_C2') else f" {strip}")
                        cs = [r for r in tri if r['label'] == full and r['eps'] == eps and r['status'] == 'ok']
                        if not cs:
                            print(f"   [FAIL] triangle eps={eps} {full}: no record"); ok_all = False; continue
                        cells = [r['lpdata']['cons'] for r in cs]
                        if strip == 'III':
                            good = covers_1d((None, Fr(-t2)), cells)
                        else:
                            good, ar, M = covers_2d(tg, cells)
                        ok_all &= good
                        if not good: print(f"   [FAIL] triangle eps={eps} {full} strip {strip}")
            print(f"   triangle eps={eps} theta={th}: every item cell contains its relaxed target U_R ∩ strip: "
                  f"{'PASS' if ok_all else 'FAIL'}")
        # remainder: r cell I (X_u <= 0), r cell II (X_v <= 0), r u>1 (X_u >= 0), sliver A (X_w <= -1), B (X_c <= -1)
        tests = [('r cell I (0<u<=1/2)', [([1, 0], 0)]), ('r cell II (1/2<u<1)', [([1, 0], 0)]),
                 ('r u>1 (local u,kap)', [([-1, 0], 0)]), ('sliver A (w<=a/2)', [([1, 0], -1)]),
                 ('sliver B (w>=a/2)', [([1, 0], -1)])]
        good_r = True
        for lab, tg in tests:
            cs = tcells(lab, eps)
            g_, ar, M = covers_2d(tg, [r['lpdata']['cons'] for r in cs]) if cs else (False, None, None)
            good_r &= g_
            fz = cs[0]['lpdata']['frozen'] if cs else None
            print(f"   triangle eps={eps} remainder record '{lab}': cell ⊇ relaxed strip {tg} with kappa free: {g_};"
                  f" frozen ranges {fz}")
        # frozen-range adequacy (exact): strips u in (0,1/2], [1/2,1), [1,2] and the sliver gamma range [1/sqrt2, sqrt2]
        good_fz = (Fr(7, 10)**2 <= Fr(1, 2)) and (Fr(3, 2)**2 >= 2)
        print(f"   sliver frozen range [7/10, 3/2] contains [1/sqrt2, sqrt2] (exact: (7/10)^2 <= 1/2, (3/2)^2 >= 2): {good_fz}")
        ok_all &= good_r and good_fz
    # ---- bubble: remainder regions I, II (+ corner), u > 1; items theta = 2
    for eps in ['0', '1/10']:
        cells = defaultdict(list); pieces = defaultdict(lambda: defaultdict(set))
        for ent in bub:
            rec = ent['record']
            if not rec or rec.get('status') != 'ok' or ent['eps'] != eps: continue
            k = (ent['part'], rec['region'])
            cons = json.dumps(rec['lpdata']['cons'])
            if cons not in [json.dumps(c) for c in cells[k]]: cells[k].append(rec['lpdata']['cons'])
            pieces[k][cons].add((ent['piece'], ent['alternative']))
        reg_I = cells[('remainder 0<u<1', 'I')]; reg_II = cells[('remainder 0<u<1', 'II')]
        corner = cells[('remainder 0<u<1 corner', 'II')]; big = cells[('remainder u>1', 'BIG')]
        gI, aI, MI = covers_2d([([1, 0], 0)], reg_I)
        gII, aII, MII = covers_2d([([1, 0], 0)], reg_II + corner)
        gB, aB, MB = covers_2d([([-1, 0], 0)], big)
        print(f"   bubble eps={eps}: region I (X_u <= 0, kappa free) covered by its {len(reg_I)} cells: {gI} (box {float(MI):.0f});"
              f" region II (X_v <= 0) by {len(reg_II)} cells + corner: {gII}; u > 1 (X_u >= 0) by {len(big)} cells: {gB}")
        ok_all &= gI and gII and gB
        # piece completeness
        need_small = {'P0', 'P1', 'P2', 'P3', 'P4'}
        comp_ok = True
        for k in [('remainder 0<u<1', 'I'), ('remainder 0<u<1', 'II')]:
            for cons, ps in pieces[k].items():
                if {p for p, _ in ps} != need_small: comp_ok = False
        for cons, ps in pieces[('remainder u>1', 'BIG')].items():
            if {p for p, _ in ps} != {'rho_r', 'w_a|T_e|'}: comp_ok = False
        for cons, ps in pieces[('remainder 0<u<1 corner', 'II')].items():
            if {p for p, _ in ps} != {'shell D', 'shell e', 'shell t', 'shell h'}: comp_ok = False
        print(f"   bubble eps={eps}: every remainder cell carries P0..P4, every u>1 cell rho_r and w_a|T_e|, the corner its"
              f" four shells: {comp_ok}")
        ok_all &= comp_ok
        # items: coverage of U_S, U_C1 (I, II), U_C2 by the item cells, and main + corrections present
        it_cells = defaultdict(list); it_pieces = defaultdict(set)
        for ent in bub:
            rec = ent['record']
            if not rec or rec.get('status') != 'ok' or ent['eps'] != eps or not ent['part'].startswith('items'): continue
            U, lab, region = ent['cell']
            it_cells[(U, lab, region)].append(rec['lpdata']['cons']); it_pieces[(U, lab, region)].add(ent['piece'])
        t2 = Fr(1)
        targ = {('U_S', 'I'): [([1, 0], -t2), ([-1, 1], -t2)],
                ('U_C1', 'I'): [([1, 0], 0), ([-1, 0], t2), ([-1, 1], -t2)], ('U_C1', 'II'): [([1, 0], 0), ([0, 1], -t2)],
                ('U_C2', 'I'): [([1, 0], -t2), ([1, -1], t2), ([-1, 1], 0)]}
        good_it = True
        for (U, lab, region), cl in it_cells.items():
            g_, ar, M = covers_2d(targ[(U, region)], cl)
            need = {'main'} | {'corr ' + str(p) for (l2, p) in CORR_EXPECTED if l2 == lab}
            good_it &= g_ and (it_pieces[(U, lab, region)] == need)
            if not (g_ and it_pieces[(U, lab, region)] == need):
                print(f"   [FAIL] bubble item {U} {lab} {region}: coverage {g_}, pieces {sorted(it_pieces[(U, lab, region)])} vs {sorted(need)}")
        expected_items = {('U_S', l) for l in ['(H1)_S  G-S', '(H2)_S  C_C1', '(H2)_S  C_C2', '(H2)_S  C_H']} | \
                         {('U_C1', l) for l in ['(H1)_C1 G-S-C1', '(H2)_S  C_C2', '(H2)_S  C_H']} | \
                         {('U_C2', l) for l in ['(H1)_C2 alt', '(H2)_S  C_C1', '(H2)_S  C_H']}
        present = {(U, l) for (U, l, r) in it_cells}
        regions_ok = all(((U, l, 'I') in it_cells) and (U != 'U_C1' or (U, l, 'II') in it_cells) for (U, l) in expected_items)
        print(f"   bubble eps={eps}: items -- all {len(expected_items)} (U_R, item) pairs present with their strips: "
              f"{present == expected_items and regions_ok}; each item cell contains its relaxed target and carries main + "
              f"the connecting corrections: {good_it}  (u in (1,2] and the sliver: triangle cells x |l|^j, checked above)")
        ok_all &= good_it and present == expected_items and regions_ok
    return ok_all

if __name__ == "__main__":
    args = sys.argv[1:]
    do_lp = '--no-lp' not in args
    parts = [a for a in args if not a.startswith('--')] or ['triangle', 'bubble']
    print("(0) four-shell representation and item shell forms vs Prop B.1 (exact)")
    r_small = sp.together((tri_expected([('G', 1), ('S', -1), ('C1', -1), ('C2', -1), ('H', -1)], False)
                           - sum(TS.values())).subs(v, 1 - u))
    r_big = sp.together(tri_expected([('S', -1), ('C1', -1), ('C2', -1), ('H', -1)], True) - (TS['e'] + TS['h']))
    ok0 = (sp.expand(reduce_s2(sp.expand(sp.fraction(r_small)[0]))) == 0 and
           sp.expand(reduce_s2(sp.expand(sp.fraction(r_big)[0]))) == 0)
    print(f"   sum_s T_s = r^(0) (0<u<1) and T_e + T_h = r^(0) (u>1): {ok0}")
    ok_items = check_item_algebra()
    tri = bub = None
    print("\n(S)(L)(F)(E)(R) LP checks" + (" and (C') exact closed forms" if do_lp else " skipped; (C') exact closed forms"))
    if 'triangle' in parts: tri = run_triangle(do_lp)
    if 'bubble' in parts: bub = run_bubble(do_lp)
    print("   checks passed:", dict(STATS), "  closed-form identities:", dict(CF_OK))
    print("   failures:", len(FAIL))
    for f in FAIL[:20]: print("      ", f)
    if tri is None: tri = json.load(gzip.open(os.path.join(LOGS, 'r3_triangle_certificates_sc.json.gz')))
    if bub is None: bub = json.load(gzip.open(os.path.join(LOGS, 'r3_bubble_certificates_sc.json.gz')))
    okV = run_coverage(tri, bub)
    print("\n   max L-power bound used:", MAXL)
    for k in sorted(MINEXP): print(f"   min exponent {k[0]:40s} eps={k[1]:>5s}: {MINEXP[k]}")
    print("\nALL CHECKS PASS" if (not FAIL and ok0 and ok_items and okV) else "\nSOME CHECKS FAIL")
