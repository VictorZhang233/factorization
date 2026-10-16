"""R-m23 checks (minor corrections m23, m25; independent code).

(A) Off-shell triangle (reference Ex. D.47, Table 5, (D.32)):
    Q^2 I = int_0^1 dt int_0^1 du [lam2 (1-t) + t u(1-u)]^{-1},  lam2 = t_ = m^2/Q^2, L = ln(Q^2/m^2)
    (Feynman parameters x1 = 1-t, x2 = t u, x3 = t(1-u); F = m^2 x1(x2+x3) + Q^2 x2 x3, U = 1, d = 4)
    claims: NLP of Q^2 I is t_(2L^2 - 4L - 4 + 2 pi^2/3); Table 5 compares with L^2 + pi^2/3 in Q^2, not with
    (D.32) = [ln^2(Qt^2/m^2) + pi^2/3]/Qt^2, Q^2 = (Qt^2 + m^2)^2/Qt^2; the Collins remainder
    r = I - (D.32) = -4 m^2/Q^4 + O(m^4 Q^-6 L^2)  (no log at NLP).
(B) Ex. C.27: I(q) = int d^4k [Delta(q-k) - Delta(q)] Delta(k)^3, Delta = 1/(k^2+m^2) (Euclidean):
    q^4 I -> -pi^2/2 (m independent, no log), corrections O(m^2 q^-2 ln q).
(C) C_S k^+ integral: int_0^inf dk (k)^{-eps}/(m^2 + 2P' k) = (m^2)^{-eps} (2P')^{eps-1} Gamma(eps)Gamma(1-eps)  (Beta fn),
    not J(eps) = Gamma(-eps)Gamma(1-eps)/Gamma(1-2eps); and it reproduces B(eps) = Gamma(1+eps)^2 Gamma(1-eps)/eps^2 of (D.31).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 40

def Q2I(lam2):
    """u-integral done analytically: int_0^1 du/(a + t u(1-u)) = (2/(t s)) ln((s+1)/(s-1)), s = sqrt(1+4a/t), a = lam2 (1-t).
    Integrate in v = 1-t (log singularity at v -> 0 is integrable); s-1 computed as x/(1+s) to avoid cancellation."""
    lam2 = mp.mpf(lam2)
    def f(v):
        t = 1 - v
        if t <= 0 or v <= 0: return mp.mpf(0)
        x = 4*lam2*v/t
        s = mp.sqrt(1 + x)
        return 2/(t*s)*mp.log((s+1)*(1+s)/x)
    pts = [0, mp.mpf(10)**-30, mp.mpf(10)**-15, mp.mpf(10)**-8, mp.mpf(10)**-4, mp.mpf('0.1'), mp.mpf('0.5'),
           1 - 100*lam2, 1 - 10*lam2, 1 - lam2, 1 - lam2/10, 1]
    pts = sorted(set([p for p in pts if 0 <= p <= 1]))
    return mp.quad(f, pts)

print("(A) Table 5 reproduction and NLP fit")
print("   m^2/Q^2      Q^2 I (exact)           L^2+pi^2/3        diff            t(2L^2-4L-4+2pi^2/3)    diff - NLP")
for e in [1, 2, 3, 4, 6, 8, 10]:
    t_ = mp.mpf(10)**(-e)
    L = mp.log(1/t_)
    ex = Q2I(t_)
    lp = L**2 + mp.pi**2/3
    nlp = t_*(2*L**2 - 4*L - 4 + 2*mp.pi**2/3)
    print(f"   1e-{e:<2d}  {mp.nstr(ex,16):>22}  {mp.nstr(lp,16):>20}  {mp.nstr(ex-lp,6):>12}   {mp.nstr(nlp,6):>12}   {mp.nstr(ex-lp-nlp,4):>10}")
# fit of the reference's "2 lam^2 L^2 - 3.9 lam^2 L" vs exact NLP at t = 1e-10
t_ = mp.mpf('1e-10'); L = mp.log(1/t_)
print("   at 1e-10: ref fit 2L^2-3.9L =", mp.nstr(t_*(2*L**2-3.9*L), 6), "; exact NLP =", mp.nstr(t_*(2*L**2-4*L-4+2*mp.pi**2/3), 6),
      "; Table 5 diff 9.71e-8")

print("\n(A') Collins remainder r = I - (D.32), with Q^2 = (Qt^2+m^2)^2/Qt^2")
for e in [2, 3, 4, 5, 6, 8]:
    m2 = mp.mpf(1); Q2 = m2*mp.mpf(10)**e
    # solve Qt^2 from Q^2 = (Qt^2 + m^2)^2 / Qt^2  -> Qt^2 = [ (Q^2 - 2 m^2) + sqrt(Q^2 (Q^2 - 4 m^2)) ]/2
    Qt2 = ((Q2 - 2*m2) + mp.sqrt(Q2*(Q2 - 4*m2)))/2
    assert abs((Qt2+m2)**2/Qt2 - Q2) < mp.mpf(10)**(-25)*Q2
    I = Q2I(m2/Q2)/Q2
    sumR = (mp.log(Qt2/m2)**2 + mp.pi**2/3)/Qt2
    r = I - sumR
    L = mp.log(Q2/m2)
    print(f"   Q^2/m^2=1e{e}:  Q^4 r/m^2 = {mp.nstr(r*Q2**2/m2, 12)}   (claim -4 + O(t L^2));  "
          f"[Q^4 r/m^2 + 4]/(t(L^2-15+pi^2/3)) = {mp.nstr((r*Q2**2/m2 + 4)/((m2/Q2)*(L**2 - 15 + mp.pi**2/3)), 8)}")
# N12 numeric point
m2 = mp.mpf('0.02'); P = mp.mpf('0.8'); Pp = mp.mpf('1.3')
Qt2 = 2*P*Pp; Q2 = (Qt2 + m2)**2/Qt2
r = Q2I(m2/Q2)/Q2 - (mp.log(Qt2/m2)**2 + mp.pi**2/3)/Qt2
print("   N12 point m^2=0.02, P=0.8, P'=1.3:  int r =", mp.nstr(r, 13), "  (N12 states -0.0173434339581)")

print("\n(B) Ex. C.27")
def Iq(q, m=1):
    q = mp.mpf(q); m = mp.mpf(m)
    def f(k):
        A = q**2 + k**2 + m**2; B = 2*q*k
        avg = 2/(A + mp.sqrt(A**2 - B**2))          # 4D angular average of 1/((q-k)^2+m^2)
        return k**3*(avg - 1/(q**2 + m**2))/(k**2 + m**2)**3
    return 2*mp.pi**2*mp.quad(f, [0, m, 10*m, q/10, q, 10*q, mp.inf])
for q in [10, 30, 100, 300, 1000, 3000]:
    v = Iq(q)
    print(f"   q={q:5d}: q^4 I = {mp.nstr(v*q**4, 12)}   (-pi^2/2 = {mp.nstr(-mp.pi**2/2, 12)});  (q^4 I + pi^2/2) q^2/ln q = {mp.nstr((v*q**4 + mp.pi**2/2)*q**2/mp.log(q), 6)}")
# the unreduced piece kappa int d^4k Delta(q-k) Delta(k)^3 ~ pi^2/(2 m^2 q^2)
q = mp.mpf(1000)
def g(k):
    A = q**2 + k**2 + 1; B = 2*q*k
    return k**3*(2/(A + mp.sqrt(A**2 - B**2)))/(k**2 + 1)**3
unred = 2*mp.pi**2*mp.quad(g, [0, 1, 10, 100, q, 10*q, mp.inf])
print("   unreduced c0(q) m^2 q^2 at q=1000 (m=1):", mp.nstr(unred*q**2, 10), " vs pi^2/2 =", mp.nstr(mp.pi**2/2, 10))

print("\n(C) C_S k^+ integral")
eps = mp.mpf('0.3'); m2 = mp.mpf('0.02'); Pp = mp.mpf('1.3'); P = mp.mpf('0.8')
num = mp.quad(lambda k: k**(-eps)/(m2 + 2*Pp*k), [0, m2, 1, mp.inf])
beta_form = m2**(-eps)*(2*Pp)**(eps-1)*mp.gamma(eps)*mp.gamma(1-eps)
J = mp.gamma(-eps)*mp.gamma(1-eps)/mp.gamma(1-2*eps)
print("   numeric =", mp.nstr(num, 15), "; (m^2)^-eps (2P')^(eps-1) Gamma(eps)Gamma(1-eps) =", mp.nstr(beta_form, 15), "; J(eps) =", mp.nstr(J, 10))
mu2 = mp.mpf('1.7')
CS = mp.gamma(eps)*P**(eps-1)*(mu2/m2)**eps*num
Qt2 = 2*P*Pp
Bform = (mu2*Qt2/m2**2)**eps*mp.gamma(1+eps)**2*mp.gamma(1-eps)/eps**2/Qt2
print("   int C_S Gamma (from the printed intermediate form) =", mp.nstr(CS, 15), "; (D.31) Qt^-2 (mu^2 Qt^2/m^4)^eps B(eps) =", mp.nstr(Bform, 15))
