# X1 final revision -- P2(b): orientation convention of delta_B (round-3 fix F7).
#
# Strict-Glauber limit (connecting propagators independent of k^+-), jets eikonal-localized, independent
# rational regulators.  For a jet X with two insertions of injected light-cone energies q1, q2 (q = k^- for
# jet A; q = p = -k^+ for jet B) the three LCOPT sectors of colour order [12] in the eikonal limit are
#   (12|) : i/(q1+i eta) * i/(q1+q2+i eta)        (both insertions before V_H)
#   (1|2) : i/(q1+i eta) * i/(-q2+i eta)
#   (|12) : i/(-(q1+q2)+i eta) * i/(-q2+i eta)    (both after V_H)
# and [21] is obtained by exchanging the labels.  We compute EXACTLY, by iterated residues with symbolic eta and
# eta -> 0+, the weights w_12 = I_12/(I_12+I_21) with regulators chi_1(q1) chi_2(q2), WITHOUT using the
# principal-value formula, and compare with
#   w_12 = 1/2 + i delta,   delta = (1/2pi) PV int chi_1(q) chi_2(-q) dq/q / (chi_1(0) chi_2(0))   (q = jet's OWN energy).
# For jet B with regulators given as functions of k^+ (chi'_e(k^+), q_e = p_e = -k_e^+) we check
#   delta_B(own energy p) = - delta_B(k^+ orientation),
# hence p_opp = 1/2 + 2 delta_A delta_B(p) = 1/2 - 2 delta_A delta_B(k^+).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

q1, q2 = sp.symbols('q1 q2', real=True)
eta = sp.symbols('eta', positive=True)
I = sp.I

def rat(K1, K2):
    """rational non-even regulator with poles at +i K1 (UHP) and -i K2 (LHP), value 1 at 0"""
    K1 = sp.Rational(K1); K2 = sp.Rational(K2)
    return lambda q: K1*K2/((K1 + I*q)*(K2 - I*q))

def uhp_poles(expr, var):
    num, den = sp.fraction(sp.together(expr))
    roots = sp.roots(sp.Poly(den, var))
    out = []
    for r in roots:
        im = sp.im(r)
        # imaginary parts are combinations of eta (>0) and positive rationals; decide sign at small eta
        val = complex(sp.N(im.subs(eta, sp.Rational(1, 10**6))))
        if val.real > 0:
            out.append(r)
    return out

def integrate_line(expr, var):
    """int_R dvar/(2pi) expr  =  i * sum of UHP residues (expr decays at least like 1/var^2)"""
    tot = 0
    for r in uhp_poles(expr, var):
        tot += sp.residue(expr, var, r)
    return sp.simplify(I*tot)

def sectors(order):
    a, b = (q1, q2) if order == '12' else (q2, q1)
    return (I/(a + I*eta))*(I/(a + b + I*eta)) + (I/(a + I*eta))*(I/(-b + I*eta)) \
        + (I/(-(a + b) + I*eta))*(I/(-b + I*eta))

def exact_weight(chi1, chi2):
    res = {}
    for order in ('12', '21'):
        e = sectors(order)*chi1(q1)*chi2(q2)
        e2 = integrate_line(e, q2)
        e1 = integrate_line(e2, q1)
        res[order] = sp.nsimplify(sp.limit(e1, eta, 0, '+'))
    tot = sp.simplify(res['12'] + res['21'])
    return sp.simplify(res['12']/tot), tot

def pv_delta(chi1, chi2):
    f1 = sp.lambdify(q1, chi1(q1), 'mpmath'); f2 = sp.lambdify(q1, chi2(q1), 'mpmath')
    g = lambda q: (f1(q)*f2(-q) - f1(-q)*f2(q))/(2*q)       # odd part / q
    val = mp.quad(g, [-mp.inf, -100, -10, -1, 0, 1, 10, 100, mp.inf])
    return val/(2*mp.pi*f1(0)*f2(0))

mp.mp.dps = 30
allok = True
print("(1) exact sector-sum weights vs PV formula (jet's own energy variable)")
for (K1a, K2a, K1b, K2b) in [(1, 3, 4, sp.Rational(1, 2)), (2, 1, sp.Rational(1, 2), 6), (1, 1, 3, 3), (5, 2, 1, 7)]:
    c1 = rat(K1a, K2a); c2 = rat(K1b, K2b)
    w12, tot = exact_weight(c1, c2)
    d = pv_delta(c1, c2)
    ok = abs(complex(sp.N(w12, 25)) - (0.5 + 1j*complex(d))) < 1e-12 and abs(complex(sp.N(tot)) - 1) < 1e-12
    allok &= ok
    print(f"    regs ({K1a},{K2a};{K1b},{K2b}): exact w12 = {w12} = {complex(sp.N(w12, 15)):.12f};"
          f"  1/2 + i delta = {complex(0.5 + 1j*complex(d)):.12f};  I12+I21 = {sp.N(tot, 12)};  ok={ok}")

print("(2) jet B with regulators specified as functions of k^+ (p = -k^+): delta(p) = -delta(k^+)")
for (K1a, K2a, K1b, K2b) in [(1, 3, 4, sp.Rational(1, 2)), (2, 1, sp.Rational(1, 2), 6)]:
    chik1 = rat(K1a, K2a); chik2 = rat(K1b, K2b)               # chi'_e(k^+)
    chip1 = lambda p, f=chik1: f(-p); chip2 = lambda p, f=chik2: f(-p)   # as functions of B's own energy p
    d_p = pv_delta(chip1, chip2); d_k = pv_delta(chik1, chik2)
    wB12, _ = exact_weight(chip1, chip2)
    okB = abs(complex(sp.N(wB12, 25)) - (0.5 + 1j*complex(d_p))) < 1e-12 and abs(d_p + d_k) < 1e-20
    allok &= okB
    print(f"    chi'(k^+) regs ({K1a},{K2a};{K1b},{K2b}): delta_B(p) = {mp.nstr(d_p, 12)}, delta_B(k^+) = {mp.nstr(d_k, 12)};"
          f"  exact w^B_12 = {complex(sp.N(wB12, 15)):.12f};  ok={okB}")

print("(3) p_opp from the exact factorized weights W(pi_A,pi_B) = w^A w^B (strict-Glauber limit)")
chiA = (rat(1, 3), rat(4, sp.Rational(1, 2)))
chiKB = (rat(2, 1), rat(sp.Rational(1, 2), 6))
wA12, _ = exact_weight(*chiA)
chiPB = (lambda p: chiKB[0](-p), lambda p: chiKB[1](-p))
wB12, _ = exact_weight(*chiPB)
wA12 = complex(sp.N(wA12, 25)); wB12 = complex(sp.N(wB12, 25))
popp = wA12*(1 - wB12) + (1 - wA12)*wB12
dA = complex(pv_delta(*chiA)); dBp = complex(pv_delta(*chiPB)); dBk = complex(pv_delta(*chiKB))
okp = abs(popp - (0.5 + 2*dA*dBp)) < 1e-12 and abs(popp - (0.5 - 2*dA*dBk)) < 1e-12
allok &= okp
print(f"    p_opp = {popp:.12f};  1/2 + 2 dA dB(p) = {0.5 + 2*dA*dBp:.12f};  1/2 - 2 dA dB(k^+) = {0.5 - 2*dA*dBk:.12f};  ok={okp}")
print("ALL PASS" if allok else "SOME CHECK FAILED")
