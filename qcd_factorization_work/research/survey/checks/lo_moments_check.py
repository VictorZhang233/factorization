# Check LO splitting-function Mellin moments and sum rules in the CONTEXT normalization:
#   d f_i/d ln mu^2 = (alpha_s/2pi) sum_j P_ij (x) f_j ,  gamma_ij(N) = int_0^1 z^(N-1) P_ij(z) dz
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
z = sp.symbols('z', positive=True)
CF, CA, TF, nf = sp.Rational(4, 3), 3, sp.Rational(1, 2), sp.symbols('n_f')

def mellin_plus(f_sing, N):
    # int_0^1 (z^(N-1)-1) f_sing(z) dz   for [f_sing]_+
    return sp.simplify(sp.integrate(sp.expand((z**(N-1) - 1) * f_sing), (z, 0, 1)))

def gamma_qq(N):
    return CF * mellin_plus((1 + z**2) / (1 - z), N)          # C_F [(1+z^2)/(1-z)]_+
def gamma_qg(N):
    return TF * sp.integrate(z**(N-1) * (z**2 + (1 - z)**2), (z, 0, 1))
def gamma_gq(N):
    return CF * sp.integrate(z**(N-1) * (1 + (1 - z)**2) / z, (z, 0, 1))
def gamma_gg(N):
    reg = 2 * CA * sp.integrate(z**(N-1) * ((1 - z) / z + z * (1 - z)), (z, 0, 1))
    # z/(1-z)_+ means z*[1/(1-z)]_+ :  int dz [1/(1-z)]_+ g(z) = int (g(z)-g(1))/(1-z), g = z^N
    plus = 2 * CA * sp.integrate(sp.cancel((z**N - 1) / (1 - z)), (z, 0, 1))
    delta = (11 * CA - 4 * nf * TF) / 6
    return sp.simplify(reg + plus + delta)

def closed_qq(N):
    H = sum(sp.Rational(1, k) for k in range(1, N + 1))
    return CF * (sp.Rational(3, 2) + sp.Rational(1, N * (N + 1)) - 2 * H)

ok = True
for N in range(1, 9):
    a, b = sp.nsimplify(gamma_qq(N)), closed_qq(N)
    if sp.simplify(a - b) != 0:
        ok = False; print("MISMATCH qq", N, a, b)
print("gamma_qq(N) closed form C_F[3/2 + 1/(N(N+1)) - 2 S_1(N)] verified N=1..8:", ok)
print("quark number (N=1): gamma_qq(1) =", gamma_qq(1))
mom_q = sp.simplify(gamma_qq(2) + gamma_gq(2))
mom_g = sp.simplify(gamma_gg(2) + 2 * nf * gamma_qg(2))
print("momentum sum rule, quark column  gamma_qq(2)+gamma_gq(2) =", mom_q)
print("momentum sum rule, gluon column  gamma_gg(2)+2 n_f gamma_qg(2) =", mom_g)
print("closed form gamma_gg(N) = 2C_A[1/(N(N-1)) + 1/((N+1)(N+2)) - S_1(N)] + (11C_A-4n_f T_F)/6 check N=2..6:", all(sp.simplify(gamma_gg(N) - (2*CA*(sp.Rational(1,N*(N-1)) + sp.Rational(1,(N+1)*(N+2)) - sum(sp.Rational(1,k) for k in range(1,N+1))) + (11*CA-4*nf*TF)/6))==0 for N in range(2,7)))
print("gamma_qq(2) =", gamma_qq(2), "; gamma_gq(2) =", gamma_gq(2), "; gamma_qg(2) =", gamma_qg(2), "; gamma_gg(2) =", gamma_gg(2))
