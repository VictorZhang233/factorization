# E35 stage-2: CRS Yukawa-model counterexample, re-derived by a route different from stage 1
# (stage 1 used an explicit d-dimensional Dirac trace).  Here:
#  (a) light-front wave functions of a spin-1/2 target (mass M=m_p) -> quark (m=m_q, fraction x) + scalar
#      (lambda_s = m_s), Brodsky-Hwang-Ma-Schmidt form psi_{+1/2} = (M + m/x) phi, psi_{-1/2} = -(k1+i k2)/x phi,
#      phi = g/sqrt(1-x) / (M^2 - (k^2+m^2)/x - (k^2+lambda_s^2)/(1-x));  f(x) = Int d^2k/(16 pi^3) sum |psi|^2;
#  (b) MS-bar via the textbook d-dim Euclidean master integral (d = 2 - 2 eps);
#  (c) high-precision roots (mpmath) of the bracket, monotonicity of the threshold mu_0(xi), mu_*.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

x, k2, M, m, ls, g = sp.symbols('x k2 M m lambda_s g', positive=True)
den = M**2 - (k2 + m**2)/x - (k2 + ls**2)/(1 - x)
phi2 = g**2/(1 - x)/den**2
lfwf_sum = ((M + m/x)**2 + k2/x**2)*phi2          # |psi_+|^2 + |psi_-|^2 (k2 = |k_T|^2)
Delta = x*ls**2 + (1 - x)*m**2 - x*(1 - x)*M**2
target = g**2*(1 - x)*(k2 + (m + x*M)**2)/(k2 + Delta)**2
print("(a) LFWF integrand == g^2 (1-x) [k^2+(m+xM)^2]/(k^2+Delta)^2 :", sp.simplify(lfwf_sum - target) == 0)

# (b) MS-bar: Int d^dk/(2pi)^d (mu^2 e^gamma/4pi)^eps 1/(k^2+D)^n, d = 2-2eps
eps, mu2, D, A = sp.symbols('epsilon mu2 D A', positive=True)
def master(n):
    d = 2 - 2*eps
    return (mu2*sp.exp(sp.EulerGamma)/(4*sp.pi))**eps*sp.gamma(n - d/2)/((4*sp.pi)**(d/2)*sp.gamma(n))*D**(d/2 - n)
bare = master(1) + (A - D)*master(2)            # [k^2 + A]/(k^2+D)^2 = 1/(k^2+D) + (A-D)/(k^2+D)^2
ser = sp.series(sp.expand(4*sp.pi*bare), eps, 0, 1).removeO()
pole = sp.simplify(sp.limit(eps*ser, eps, 0)); fin = sp.simplify(sp.expand(ser - pole/eps))
print("(b) 4 pi x [d^2k/(2pi)^2 integral]: pole =", pole, "; MS-bar finite part =", fin)
print("    equals ln(mu^2/D) - 1 + A/D :", sp.simplify(fin - (sp.log(mu2/D) - 1 + A/D)) == 0)
# overall normalisation: f = g^2/(16 pi^3) * (2pi)^2 * (1/(4 pi)) * (1-x) [..] = g^2/(16 pi^2) (1-x)[..]
print("    a_lambda = g^2/(16 pi^2):", sp.simplify(g**2/(16*sp.pi**3)*(2*sp.pi)**2/(4*sp.pi) - g**2/(16*sp.pi**2)) == 0)

# (c) numerics for m_q, m_p, m_s = 0.3, 1.0, 1.5 GeV
mp.mp.dps = 30
mq, mP, ms = mp.mpf('0.3'), mp.mpf('1.0'), mp.mpf('1.5')
Dl = lambda xi: xi*ms**2 + (1 - xi)*mq**2 - xi*(1 - xi)*mP**2
Aq = lambda xi: (mq + xi*mP)**2
br = lambda xi, mu: mp.log(mu**2/Dl(xi)) - 1 + Aq(xi)/Dl(xi)
mu0 = lambda xi: mp.sqrt(Dl(xi)*mp.e**(1 - Aq(xi)/Dl(xi)))       # bracket = 0  <=>  mu = mu0(xi)
print("(c) min Delta on [0,1]:", mp.nstr(min(Dl(mp.mpf(i)/1000) for i in range(1001)), 8))
# monotonicity of mu0 on (0,1): sample derivative sign
vals = [mu0(mp.mpf(i)/2000) for i in range(1, 2000)]
print("    mu0 strictly increasing on the grid:", all(vals[i+1] > vals[i] for i in range(len(vals)-1)),
      "; mu0(0+) =", mp.nstr(mu0(mp.mpf('1e-12')), 10), "; mu0(1-) =", mp.nstr(mu0(1 - mp.mpf('1e-12')), 10))
mustar = ms*mp.e**((1 - (mq + mP)**2/ms**2)/2)
print("    mu_* = m_s exp[(1-(m_q+m_p)^2/m_s^2)/2] =", mp.nstr(mustar, 10), "GeV")
for mu in ['0.5', '0.8', '1.0', '1.2', '1.5', '1.69']:
    mu = mp.mpf(mu)
    xc = mp.findroot(lambda xi: mu0(xi) - mu, (mp.mpf('1e-9'), 1 - mp.mpf('1e-12')), solver='anderson')
    print(f"    mu = {mp.nstr(mu,3)} GeV: f < 0 exactly for xi in ({mp.nstr(xc, 6)}, 1)"
          f"   [check: bracket(xc-1e-6) = {mp.nstr(br(xc-mp.mpf('1e-6'), mu), 3)}, bracket(xc+1e-6) = {mp.nstr(br(xc+mp.mpf('1e-6'), mu), 3)}]")
print("    sign at mu = 1.70 GeV, xi = 0.999999:", mp.nstr(br(1 - mp.mpf('1e-6'), mp.mpf('1.70')), 5),
      "; at mu = 1.698 GeV:", mp.nstr(br(1 - mp.mpf('1e-6'), mp.mpf('1.698')), 5))
# cutoff form vs MS-bar: Int_0^{L^2} dk^2 [k^2+A]/(k^2+D)^2 = ln((L^2+D)/D) + (A-D)(1/D - 1/(L^2+D))
for L in ['3', '30', '100']:
    L = mp.mpf(L)
    dev = max(abs((mp.log((L**2 + Dl(xi))/Dl(xi)) + (Aq(xi) - Dl(xi))*(1/Dl(xi) - 1/(L**2 + Dl(xi)))) - br(xi, L))
              for xi in [mp.mpf(i)/50 for i in range(1, 50)])
    print(f"    cutoff(k_T < mu) bracket minus MS-bar bracket, max over xi, mu = {mp.nstr(L,3)} GeV: {mp.nstr(dev, 4)}")

# (d) the CFH step 'bare pdfs are positive' fails for eps < 0 (n > 4), the regime CFH need (eps -> 0^-):
#     bare bracket = 4 pi [master(1) + (A-D) master(2)] evaluated at finite eps (exact Gamma functions)
bare_num = sp.lambdify((eps, mu2, D, A), sp.expand(4*sp.pi*bare), 'mpmath')
for e in ['0.05', '0.01', '-0.01', '-0.05']:
    xi = mp.mpf('0.5'); mu = mp.mpf('0.8')
    val = bare_num(mp.mpf(e), mu**2, Dl(xi), Aq(xi))
    print(f"(d) bare one-loop pdf bracket (units a_lambda (1-xi)) at xi=0.5, mu=0.8 GeV, eps={e}: {mp.nstr(mp.re(val), 8)}")
