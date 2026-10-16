"""R1 check 3: kinematics (Fig.5 Breit frame, Fig.6 DY, |x|>1 region), normalisations ((2.8)-(2.10)),
power-counting algebra (Lemma 3.7, Cor. 3.8, Lemma 3.9, Lemma 3.10, Fig.10).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

def dot(a, b):  # light-cone (+,-,Tx,Ty)
    return a[0]*b[1] + a[1]*b[0] - a[2]*b[2] - a[3]*b[3]

Q, x, M = sp.symbols('Q x M', positive=True)
r2 = sp.sqrt(2)
print("== Fig.5(b) Breit frame ==")
P = (Q/(r2*x), 0, 0, 0); q = (-Q/r2, Q/r2, 0, 0); k = (Q/r2, 0, 0, 0)
kq = tuple(sp.simplify(k[i]+q[i]) for i in range(4))
print("q^2 =", sp.simplify(dot(q, q)), "; x_Bj = Q^2/(2P.q) =", sp.simplify(Q**2/(2*dot(P, q))),
      "; q^0 =", sp.simplify((q[0]+q[1])/r2), "; q^3 =", sp.simplify((q[0]-q[1])/r2))
print("k+q =", kq, "; (k+q)^2 =", sp.simplify(dot(kq, kq)), "; k^3 =", sp.simplify((k[0]-k[1])/r2), "; (k+q)^3 =", sp.simplify((kq[0]-kq[1])/r2), "; k^+/P^+ =", sp.simplify(k[0]/P[0]))
# W^2 with target mass: P = (P+, M^2/(2P+), 0,0)
Pp = sp.symbols('Pp', positive=True)
Pm_ = (Pp, M**2/(2*Pp), 0, 0)
qq = sp.symbols('qq')
# general: W^2 = M^2 + 2P.q - Q^2 with 2P.q = Q^2/x
W2 = M**2 + Q**2/x - Q**2
print("W^2 = M^2 + Q^2(1-x)/x :", sp.simplify(W2 - (M**2 + Q**2*(1-x)/x)) == 0)
print("crossed (P-q)^2 = M^2 - Q^2(1/x+1):", sp.simplify((M**2 - Q**2/x - Q**2) - (M**2 - Q**2*(1/x+1))) == 0)
for xv in [sp.Rational(3, 2), sp.Rational(-3, 2), sp.Rational(-11, 10)]:
    print(f"   x={xv}: W^2-M^2 = {sp.simplify(Q**2*(1/xv-1))},  (P-q)^2-M^2 = {sp.simplify(-Q**2*(1/xv+1))}")

print("\n== W = (1/2pi) Im T normalisation (single intermediate state, pole term) ==")
# W = (1/4pi) (2pi)^4 delta^4 |M|^2 ;  T-term = i * i(2pi)^3 delta^3 /(E + i0) ... Im[-1/(E+i0)] = pi delta(E)
E = sp.symbols('E', real=True); e0 = sp.symbols('e0', positive=True)
ImT_coeff = sp.limit(sp.im(-1/(E + sp.I*e0)).subs(E, 0)*e0, e0, 0)  # pi*delta(E) normalisation -> coefficient of delta is pi
# Im T = (2pi)^3 * pi * delta^4 |M|^2 = (1/2)(2pi)^4 delta^4 |M|^2 ; W = (1/4pi)(2pi)^4 delta^4 |M|^2
ratio = (sp.Rational(1, 2)) / (1/(4*sp.pi))
print("Im T / W =", sp.simplify(ratio), " -> W = Im T/(2 pi):", sp.simplify(ratio - 2*sp.pi) == 0)

print("\n== (2.10) DY LO normalisation ==")
alpha, s, Nc, eq = sp.symbols('alpha s N_c e_q', positive=True)
xa, xb, y = sp.symbols('x_a x_b y', positive=True)
sigma_hat0 = 4*sp.pi*alpha**2*eq**2/(3*Nc*Q**2)   # dsigma_hat/dQ^2 = sigma_hat0 * delta(Q^2 - x_a x_b s)  (sigma(qqbar->l+l-)=4pi a^2 e_q^2/(3 N_c shat))
# change variables (x_a,x_b) -> (Q^2, y): Q^2 = x_a x_b s, y = 1/2 ln(x_a/x_b)
J = sp.Matrix([[xb*s, xa*s], [1/(2*xa), -1/(2*xb)]]).det()
print("|d(Q^2,y)/d(x_a,x_b)| =", sp.simplify(abs(J)), " => dx_a dx_b = dQ^2 dy / s")
print("dsigma/dQ^2dy = sigma_hat0 / s * f f  =", sp.simplify(sigma_hat0/s), " ; doc: 4 pi alpha^2/(3 N_c Q^2 s) e_q^2  -> match:",
      sp.simplify(sigma_hat0/s - 4*sp.pi*alpha**2*eq**2/(3*Nc*Q**2*s)) == 0)
tau = sp.symbols('tau', positive=True)
print("x_A x_B = tau, y=1/2 ln(x_A/x_B) for x_A=sqrt(tau)e^y:", sp.simplify(sp.sqrt(tau)*sp.exp(y)*sp.sqrt(tau)*sp.exp(-y) - tau) == 0)

print("\n== Lemma 3.7 power counting algebra ==")
nF, nB, npl, nT, nmi, dext, ext = sp.symbols('n_F n_B n_+ n_T n_- d_ext ext')
DJ = 4 - 3*nB - sp.Rational(5, 2)*nF - dext
pJ = 4*(nF + nB - 1) + DJ - npl + nmi - sp.Rational(1, 2)*nF + ext
pJ = sp.expand(pJ.subs(nB, npl + nT + nmi))
print("p_J =", pJ, "  ( = n_F + n_T + 2 n_- - c_J with c_J = d_ext - ext )")
cJ = 2
print("DIS forward jet (c_J=2): p_J(n_F,n_T) for small configurations (n_-=0):")
for (a, b) in [(0, 0), (0, 1), (1, 1), (2, 0), (0, 2), (2, 1), (0, 3), (4, 0), (2, 2)]:
    print(f"   (n_F,n_T)=({a},{b}): p_J = {a + b - cJ}" + ("   <-- super-leading; n_F even, not excluded by fermion number" if a + b - cJ < 0 and a % 2 == 0 else ""))

print("\n== Lemma 3.9 soft power counting algebra ==")
Nb, Nf, V3, V4, Vqg, EJB, EJF, EHB, EHF = sp.symbols('N_b N_f V_3 V_4 V_qg E_J^B E_J^F E_H^B E_H^F')
VS = V3 + V4 + Vqg; LS = Nb + Nf - VS
pS = 8*LS - 4*Nb - 2*Nf - 2*(EJB + EJF) + 2*V3
pS = pS.subs({Nb: (3*V3 + 4*V4 + Vqg + EJB + EHB)/2, Nf: (2*Vqg + EJF + EHF)/2})
print("p_S =", sp.expand(pS), "  (doc (3.9): 2E_H^B + 3E_H^F + E_J^F)")

print("\n== Lemma 3.10 / Remark 3.11: Glauber and soft scalings for an A-collinear line l ~ (1,lam^2,lam) ==")
lam = sp.symbols('lambda', positive=True)
for name, (a, b, c) in [('soft (2,2,2)', (2, 2, 2)), ('Glauber (2,2,1)', (2, 2, 1)), ('TMD-soft (1,1,1)', (1, 1, 1))]:
    terms = {"l+ k-": 0 + b, "l- k+": 2 + a, "lT.kT": 1 + c, "k^2 (max of k+k-, kT^2)": min(a + b, 2*c)}
    kept = terms["l+ k-"]
    print(f"   {name}: exponents {terms}; dropped/kept: lT.kT -> lam^{terms['lT.kT']-kept}, k^2 -> lam^{terms['k^2 (max of k+k-, kT^2)']-kept}")
print("   Glauber single exchange: measure lam^6 * gluon lam^-2 * two jet props lam^-2 each = lam^", 6 - 2 - 2 - 2)

print("\n== Fig.10: parallelogram H,CA,CB,S with centre S_TMD ==")
H_, CA, CB, Ss, ST, Gl = (0, 0, 0), (0, 2, 1), (2, 0, 1), (2, 2, 2), (1, 1, 1), (2, 2, 1)
onplane = lambda p: sp.Rational(p[2]) == sp.Rational(p[0] + p[1], 2)
print("   on plane c=(a+b)/2:", [onplane(p) for p in (H_, CA, CB, Ss, ST)], " Glauber on plane:", onplane(Gl), "(c<(a+b)/2:", Gl[2] < (Gl[0] + Gl[1]) / 2, ")")
print("   H+S == CA+CB:", tuple(a + b for a, b in zip(H_, Ss)) == tuple(a + b for a, b in zip(CA, CB)), " centre:", tuple(sp.Rational(a + b, 2) for a, b in zip(H_, Ss)))
