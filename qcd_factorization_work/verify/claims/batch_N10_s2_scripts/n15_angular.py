# N15 (stage 2): reference Ex C.27 combination  kappa * int d^4k [Delta(q-k) - Delta(q)] Delta(k)^3, Euclidean
# Delta(k) = 1/(k^2+m^2).  METHOD (different from stage 1's Feynman parameters): exact 4D angular average
#   <1/((q-k)^2+m^2)>_{S^3} = 2/(A + sqrt(A^2 - 4 q^2 k^2)),  A = q^2 + k^2 + m^2,
# then a 1D radial integral at high precision; plus the m-independent leading term from the 4D mean-value
# property (harmonicity of 1/x^2 in R^4).  Also: region poset of the two-loop planar vertex -> 1/243.
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
npass = 0; nfail = 0
def check(name, ok, info=""):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(("PASS " if ok else "FAIL ") + name + ("  " + info if info else ""), flush=True)
mp.mp.dps = 40
# angular average formula: check against direct S^3 average (measure (2/pi) sin^2 th dth)
def ang_exact(q, k, m):
    A = q*q + k*k + m*m
    return 2/(A + mp.sqrt(A*A - 4*q*q*k*k))
def ang_direct(q, k, m):
    return (2/mp.pi)*mp.quad(lambda th: mp.sin(th)**2/(q*q + k*k + m*m - 2*q*k*mp.cos(th)), [0, mp.pi])
for (q, k, m) in [(3, 1, 1), (2, 5, mp.mpf('0.3')), (1, 1, mp.mpf('0.01'))]:
    q, k, m = mp.mpf(q), mp.mpf(k), mp.mpf(m)
    check("4D angular average formula (q=%s,k=%s,m=%s)" % (q, k, m), abs(ang_exact(q, k, m) - ang_direct(q, k, m)) < mp.mpf(10)**-30)
# mean-value property (m=0): <1/(q-k)^2> = 1/max(q^2,k^2)
for (q, k) in [(3, 1), (1, 3), (2, 2.5)]:
    q, k = mp.mpf(q), mp.mpf(k)
    check("mean-value property <1/(q-k)^2> = 1/max(q^2,k^2) (q=%s,k=%s)" % (q, k), abs(ang_direct(q, k, mp.mpf('1e-30')) - 1/max(q*q, k*k)) < mp.mpf(10)**-25)
check("int d^4k Delta^3 = pi^2/(2 m^2)  (m=1)", abs(mp.pi**2*mp.quad(lambda u: u/(u+1)**3, [0, mp.inf]) - mp.pi**2/2) < mp.mpf(10)**-30)
# I(q) with m = 1 (I(q,m) = m^-4 I(q/m,1)):  d^4k = pi^2 u du, u = k^2
def I_ang(q, m=mp.mpf(1)):
    a = q*q + m*m
    def f(u):
        A = q*q + u + m*m
        # write <Delta(q-k)> - Delta(q) without cancellation:  2/(A+s) - 1/a = (2a - A - s)/(a(A+s))
        s = mp.sqrt(A*A - 4*q*q*u)
        num = (2*a - A - s)
        return mp.pi**2*u*num/(a*(A + s))/(u + m*m)**3
    pts = [0, m*m/100, m*m, 10*m*m, q*q/10, q*q, 10*q*q, mp.inf]
    pts = sorted(set(pts), key=lambda x: (x == mp.inf, x))
    return mp.quad(f, pts)
# Feynman-parameter cross check at moderate q (stage-1 form, only as a sanity check of normalization)
def I_feyn(q, m=mp.mpf(1)):
    return (mp.pi**2/2)*(mp.quad(lambda x: x*x/(x*(1-x)*q*q + m*m)**2, [0, 1]) - 1/(m*m*(q*q + m*m)))
for q in [mp.mpf('0.7'), mp.mpf(3), mp.mpf(10)]:
    check("angular-average I(q) = Feynman-parameter I(q) at q=%s" % q, abs(I_ang(q)/I_feyn(q) - 1) < mp.mpf(10)**-25, mp.nstr(I_ang(q), 15))
print("   q      q^4 I(q)                      q^6[I + pi^2/(2q^4)] / m^2      model -2 pi^2 ln(q^2/m^2) + 7 pi^2/2")
prev = None
for q in [mp.mpf(10), mp.mpf(30), mp.mpf(100), mp.mpf(1000), mp.mpf(10)**4, mp.mpf(10)**6]:
    Iq = I_ang(q)
    r = q**6*(Iq + mp.pi**2/(2*q**4))
    model = -2*mp.pi**2*mp.log(q*q) + 7*mp.pi**2/2
    print("   %-6s %-28s %-30s %s" % (mp.nstr(q, 3), mp.nstr(q**4*Iq, 20), mp.nstr(r, 15), mp.nstr(model, 15)))
mp.mp.dps = 70
q = mp.mpf(10)**6
check("leading term: q^4 I(q) -> -pi^2/2 (m-independent, no log)", abs(q**4*I_ang(q) + mp.pi**2/2) < mp.mpf(10)**-9)
# remainder is O(m^2 q^-6 ln q): ratio to ln q bounded and approaching -4 pi^2 per unit ln q ... check NLP coefficient numerically
r1 = (q**6*(I_ang(q) + mp.pi**2/(2*q**4))); q2 = mp.mpf(10)**5; r2 = q2**6*(I_ang(q2) + mp.pi**2/(2*q2**4))
slope = (r1 - r2)/(mp.log(q*q) - mp.log(q2*q2))
check("NLP: q^6 [I + pi^2/(2q^4)] grows like ln(q^2/m^2) (O(m^2 q^-6 ln q)); slope -> -2 pi^2", abs(slope + 2*mp.pi**2) < 1e-7, "slope %s vs %s" % (mp.nstr(slope, 12), mp.nstr(-2*mp.pi**2, 12)))
check("NLP constant 7 pi^2/2 (stage-1 value) reproduced", abs(r1 - (-2*mp.pi**2*mp.log(q*q) + 7*mp.pi**2/2)) < 1e-7, mp.nstr(r1 - (-2*mp.pi**2*mp.log(q*q)), 12))
mp.mp.dps = 40
# m-independence of the leading term at fixed large q: vary m
for m in [mp.mpf('0.5'), mp.mpf(2)]:
    q = mp.mpf(10)**5
    check("q^4 I(q;m) -> -pi^2/2 for m=%s" % m, abs(q**4*I_ang(q, m) + mp.pi**2/2) < 1e-6, mp.nstr(q**4*I_ang(q, m), 12))
# the reference's statement O(q^-4 ln q^2) is a (non-sharp) upper bound: show |q^4 I| does not grow like ln q
vals = [abs(mp.mpf(10)**(4*j)*I_ang(mp.mpf(10)**j)) for j in (2, 4, 6)]
check("no ln q^2 at leading power: |q^4 I| at q=1e2,1e4,1e6 decreasing to pi^2/2", vals[0] > vals[1] > vals[2] > mp.pi**2/2 - 1e-6, str([mp.nstr(v, 10) for v in vals]))

# ---------------- F3: region exponents ----------------
modes = ['S', 'C1', 'C2', 'H']
def le(a, b):  # mode order S < C1, C2 < H
    return a == b or a == 'S' or b == 'H'
def add(a, b):
    if a == 'H' or b == 'H': return 'H'
    if a == 'S': return b
    if b == 'S': return a
    return a if a == b else 'H'
def lines(r):  # r = (mode k1 inner, mode k2 outer); lines: k1, k2, p1-k2, p1-k2-k1, p2+k2, p2+k2+k1
    k1, k2 = r
    return (k1, k2, add('C1', k2), add('C1', add(k1, k2)), add('C2', k2), add('C2', add(k1, k2)))
regions2 = [('H','H'), ('H','C1'), ('H','C2'), ('H','S'), ('C1','C1'), ('C2','C2'), ('C1','S'), ('C2','S'), ('S','S')]
def leq(r, s): return all(le(a, b) for a, b in zip(lines(r), lines(s)))
def lt(r, s): return leq(r, s) and lines(r) != lines(s)
def height(r, regs):
    below = [s for s in regs if lt(s, r)]
    return 0 if not below else 1 + max(height(s, regs) for s in below)
H = {r: height(r, regions2) for r in regions2}
hstar = 1 + max(H[r] for r in regions2 if r != ('H','H'))
beta = {r: mp.mpf(3)**(H[r] - hstar) for r in regions2 if r != ('H','H')}
cover = [(s, r) for r in regions2 for s in regions2 if lt(s, r) and not any(lt(s, t) and lt(t, r) for t in regions2)]
print("   two-loop heights:", H, " h* =", hstar)
print("   covering relations (%d):" % len(cover), cover)
def meet(r, s):
    cands = [t for t in regions2 if leq(t, r) and leq(t, s)]
    mx = [t for t in cands if all(leq(u, t) for u in cands)]
    return mx[0] if mx else None
check("Fig.63 meets: (C1,C1)^(H,S)=(C1,S), (H,C1)^(H,C2)=(H,S), (C1,C1)^(C2,C2)=(S,S)",
      meet(('C1','C1'), ('H','S')) == ('C1','S') and meet(('H','C1'), ('H','C2')) == ('H','S') and meet(('C1','C1'), ('C2','C2')) == ('S','S'))
check("two-loop (S,S): beta = 3^-4 = 1/81, a = beta/3 = 1/243", abs(beta[('S','S')] - mp.mpf(1)/81) < mp.mpf(10)**-35 and abs(beta[('S','S')]/3 - mp.mpf(1)/243) < mp.mpf(10)**-35, "beta=%s" % mp.nstr(beta[('S','S')], 12))
check("feasibility: R' < R != Rmax  =>  beta_R >= 3 beta_R'", all(beta[r] >= 3*beta[s] for (s, r) in cover if r != ('H','H')))
# one loop: S < C1, C2 < H
def lines1(r): return (r, add('C1', r), add('C2', r))
reg1 = ['H', 'C1', 'C2', 'S']
def lt1(r, s): return all(le(a, b) for a, b in zip(lines1(r), lines1(s))) and lines1(r) != lines1(s)
def h1(r): 
    below = [s for s in reg1 if lt1(s, r)]
    return 0 if not below else 1 + max(h1(s) for s in below)
hs1 = 1 + max(h1(r) for r in reg1 if r != 'H')
b1 = {r: mp.mpf(3)**(h1(r) - hs1) for r in reg1 if r != 'H'}
check("one-loop triangle: beta_S = 1/9, beta_C = 1/3, a_S = 1/27 (reference: beta_S=1/9, beta_C=1/3)", abs(b1['S'] - mp.mpf(1)/9) < mp.mpf(10)**-35 and abs(b1['C1'] - mp.mpf(1)/3) < mp.mpf(10)**-35)
print("\nTOTAL: %d PASS, %d FAIL" % (npass, nfail))
