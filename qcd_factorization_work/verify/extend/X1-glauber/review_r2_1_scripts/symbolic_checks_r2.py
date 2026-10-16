# Round-2 reviewer #1: symbolic checks (sympy) of
#  (1) T2'(b): end-pole residue Res(rho_12)/k_p = -a1 al1/(a1 al1 + a2 |d10|) in the scalar model,
#      rho_12(k) = (a1 a2/Jcal_A) F_A^[12](-k,k) built from L3 (F = prod(-i sgn r) J^(1V2)(z)) and the model's
#      mixed-sector function J^(1V2) = i^3/(d0 (d10 + z1)(al1 - z2)), Jcal_A = i/d0;
#  (2) L1' example: pole weights of R(k) chi(k), chi = K^2/(k^2+K^2), and their sum rule;
#  (3) P4: closed forms of int_0^inf dk/k rho2(k) for the three parameter sets of p4_perturbation.py,
#      and the sign-definiteness of rho2 on (0,inf) (so the shift is non-zero for EVERY admissible set);
#  (4) L1(b) constant: telescoping bound for one gap, and the multi-state bound 2^{N+d}(lJ/kappa)^d <= 2^{N+1} lJ/kappa;
#  (5) NF formula alpha_1 = (2 s_T.k_2T - k_2T^2)/(2 x_s P^+);
#  (6) L4(a): M2 + M2^dag + M1^dag M1 = -1/2 C_A chi^2 Re(p_opp) X (operator algebra with commuting X).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

k, a1, a2, d0, d10, al1, al2, d20 = sp.symbols('k a1 a2 d0 d10 alpha1 alpha2 d20', real=True)
I = sp.I
# (1)
k1p, k2p = -k, k
z1, z2 = a1/(2*k1p), a2/(2*k2p)
r1, r2 = 1/(2*k1p), 1/(2*k2p)
pref = (-I*sp.sign(k1p)*r1)*(-I*sp.sign(k2p)*r2)
pref = pref.subs(sp.sign(-k), -1).subs(sp.sign(k), 1)
J1V2 = I**3/(d0*(d10 + z1)*(al1 - z2))
JcalA = I/d0
rho12 = sp.simplify(a1*a2/JcalA*pref*J1V2)
print("(1) rho_12(k) =", sp.factor(rho12))
print("    rho_12(0) =", sp.limit(rho12, k, 0))
kp = a2/(2*al1)
res = sp.simplify(sp.limit((k - kp)*rho12, k, kp))
print("    Res at k_p = a2/(2 al1):", sp.factor(res), ";  Res/k_p =", sp.factor(sp.simplify(res/kp)))
D10 = sp.symbols('D10', positive=True)   # |d10|, d10 = -|d10|
print("    with d10 = -|d10|: Res/k_p =", sp.factor(sp.simplify((res/kp).subs(d10, -D10))),
      "  (report: -a1 al1/(a1 al1 + a2 |d10|))")
# (2)
z, Kr, r = sp.symbols('z K r')
kk = sp.symbols('kk')
Rchi = r/(kk - z)*Kr**2/(kk**2 + Kr**2)
R0 = Rchi.subs(kk, 0)
poles = [z, I*Kr, -I*Kr]
u = []
for p in poles:
    rho_p = sp.simplify(sp.limit((kk - p)*Rchi, kk, p))
    u.append(sp.simplify((-rho_p/p)/R0))
print("(2) u_z, u_+, u_- =", [sp.factor(x) for x in u], "; sum =", sp.simplify(sum(u)))
print("    report: u_z = K^2/(z^2+K^2), u_+ = z/(2(z-iK)), u_- = z/(2(z+iK)):",
      [sp.simplify(u[0] - Kr**2/(z**2 + Kr**2)), sp.simplify(u[1] - z/(2*(z - I*Kr))), sp.simplify(u[2] - z/(2*(z + I*Kr)))])
# (3)
A1, A2, Ap, rr = sp.symbols('A1 A2 Ap rr', real=True)
rho2 = a1*a2*rr*2*k/((2*k*A1 - a1)*(2*k*A2 - a1)*(2*k*Ap - a2))
for (va1, va2, vA1, vA2, vAp, vr) in ((1, 1, -1, -2, -1, 1), (sp.Rational(65, 100), sp.Rational(9, 10), sp.Rational(-16, 10),
                                      sp.Rational(-3, 10), sp.Rational(-16, 10), sp.Rational(7, 10)),
                                     (1, 2, sp.Rational(-1, 2), -3, -2, sp.Rational(-13, 10))):
    f = (rho2/k).subs({a1: va1, a2: va2, A1: vA1, A2: vA2, Ap: vAp, rr: vr})
    val = sp.integrate(sp.apart(sp.simplify(f), k), (k, 0, sp.oo))
    print(f"(3) set a=({va1},{va2}) A1={vA1} A2={vA2} A'={vAp} ct2/c1={vr}: int_0^inf dk/k rho2 = {sp.nsimplify(sp.simplify(val))}"
          f" = {sp.N(val, 12)};  dW/s = -(i/2pi) int = {sp.N(-I*val/(2*sp.pi), 10)}")
print("    sign of rho2 on (0,inf): each factor (2k A - a) < 0 for A<0, so rho2 = -(sign) * 2k a1 a2 ct2/c1/|...|:"
      " fixed sign -> integral never zero for ct2 != 0")
# (4)
lJ, kap, N, d = sp.symbols('lambda_J kappa N d', positive=True)
print("(4) single gap: |1/(A+K) - 1/K| = |A|/(|K||A+K|) <= lJ/(|K| |K|/2) = 2 lJ/|K|^2  (|A|<=lJ<=|K|/2)")
for Nv in range(1, 6):
    for dv in range(1, 6):
        for x in (sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 10)):   # x = lJ/kappa <= 1/2
            assert 2**(Nv + dv)*x**dv <= 2**(Nv + 1)*x
print("    2^{N+d} (lJ/kappa)^d <= 2^{N+1} (lJ/kappa) for lJ/kappa <= 1/2, N,d <= 5: OK")
# (5)
sx, sy, kx, ky, m, xs, Pp = sp.symbols('s_x s_y k_x k_y m x_s P', real=True)
E = lambda px, py: (px**2 + py**2 + m**2)/(2*xs*Pp)
alpha1 = sp.simplify(E(sx, sy) - E(sx - kx, sy - ky))
print("(5) alpha_1 =", sp.factor(alpha1), " vs report (2 s.k - k^2)/(2 x_s P):",
      sp.simplify(alpha1 - (2*(sx*kx + sy*ky) - kx**2 - ky**2)/(2*xs*Pp)))
# (6) noncommutative check with symbols: X commuting with itself, p_opp complex
chi, CA = sp.symbols('chi C_A', positive=True)
pr, pi_ = sp.symbols('p_r p_i', real=True)
X = sp.symbols('X')   # Hermitian, commuting with itself -> treat as real commuting symbol
popp = pr + I*pi_
M1 = -I*chi*X
M2 = (-I*chi)**2/2*(X**2 + popp*CA/2*X)
tot = sp.expand(M2 + sp.conjugate(M2).subs(sp.conjugate(X), X) + sp.conjugate(M1).subs(sp.conjugate(X), X)*M1)
print("(6) M2 + M2^dag + M1^dag M1 =", sp.factor(tot), " (report: -1/2 C_A chi^2 Re(p_opp) X)")
