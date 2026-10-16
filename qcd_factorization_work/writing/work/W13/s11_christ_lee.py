"""W13 / s11: Christ-Lee: no single-target-spin asymmetry in inclusive DIS at one-photon exchange (rem:coll-christ-lee).
Hadronic tensor W^{mu nu}(P,q,S) = (1/4pi) int d^4z e^{iqz} <P,S|[j^mu(z), j^nu(0)]|P,S>, linear in S (S.P = 0).
 (i)  Hermiticity: W^{mu nu *} = W^{nu mu}  (real symmetric part, imaginary antisymmetric part).
 (ii) Time reversal (antiunitary; T j^mu(x) T^-1 = j_mu(xt) with xt = (x0,-x)... standard): W^{mu nu}(P,q,S)^* =
      W_{mu nu}(Pt, qt, St), where vt = (v^0, -v) for momenta AND for the spin vector, and lowering = applying
      g = diag(1,-1,-1,-1) to each index.  Combined with (i):  W^{mu nu}(P,q,S) = [g W(Pt,qt,St) g]^{nu mu}.
 We check, with explicit components, that among the S-linear, parity-allowed, current-conserving tensors
   A^{mu nu} = i eps^{mu nu rho sigma} q_rho S_sigma                      (antisymmetric, the g1 structure),
   B^{mu nu} = i eps^{mu nu rho sigma} q_rho P_sigma (S.q)                 (antisymmetric, g2-type),
   C^{mu nu} = Pt^mu E^nu + Pt^nu E^mu,  E^nu = eps^{nu alpha beta gamma} q_alpha P_beta S_gamma   (symmetric, real coefficient),
 the T-relation is satisfied by A, B (allowed) and violated by C (C -> -C), so the coefficient of C vanishes:
 the spin-dependent part of W is purely antisymmetric and drops out against the symmetric unpolarized lepton tensor.
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

npass = 0; nfail = 0
def check(name, ok):
    global npass, nfail
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    if ok: npass += 1
    else: nfail += 1

g = sp.diag(1, -1, -1, -1)
def low(v): return g*v
def dot(a, b): return (a.T*g*b)[0]
def eps(a, b, c_, d): return sp.LeviCivita(a, b, c_, d)   # eps^{0123} = +1, upper indices
P = sp.Matrix(sp.symbols('P0:4', real=True)); q = sp.Matrix(sp.symbols('q0:4', real=True))
S = sp.Matrix(sp.symbols('S0:4', real=True))
def tilde(v): return sp.Matrix([v[0], -v[1], -v[2], -v[3]])
def Avec(P, q, S):
    ql, Sl = low(q), low(S)
    return sp.Matrix(4, 4, lambda m, n: sp.I*sum(eps(m, n, r, s_)*ql[r]*Sl[s_] for r in range(4) for s_ in range(4)))
def Bvec(P, q, S):
    ql, Pl = low(q), low(P)
    return sp.Matrix(4, 4, lambda m, n: sp.I*dot(S, q)*sum(eps(m, n, r, s_)*ql[r]*Pl[s_] for r in range(4) for s_ in range(4)))
def Cvec(P, q, S):
    ql, Pl, Sl = low(q), low(P), low(S)
    E = [sum(eps(n, a, b, c_)*ql[a]*Pl[b]*Sl[c_] for a in range(4) for b in range(4) for c_ in range(4)) for n in range(4)]
    Pt = P - dot(P, q)/dot(q, q)*q
    return sp.Matrix(4, 4, lambda m, n: Pt[m]*E[n] + Pt[n]*E[m])
def Trel(Tfun):
    """residual of W^{mu nu}(P,q,S) = [g W(Pt,qt,St) g]^{nu mu} (hermiticity + T)."""
    Wt = Tfun(tilde(P), tilde(q), tilde(S))
    rhs = (g*Wt*g).T
    return sp.simplify(Tfun(P, q, S) - rhs)
def herm(Tfun):
    W = Tfun(P, q, S)
    return sp.simplify(W.applyfunc(sp.conjugate) - W.T)
for nm, f in (('A (g1 structure)', Avec), ('B (g2 structure)', Bvec), ('C (symmetric S-odd)', Cvec)):
    print('   %s: hermitian residual zero: %s' % (nm, herm(f) == sp.zeros(4)))
check('(i) A and B are hermitian (i x real antisymmetric); C is hermitian (real symmetric)',
      herm(Avec) == sp.zeros(4) and herm(Bvec) == sp.zeros(4) and herm(Cvec) == sp.zeros(4))
check('(ii) A satisfies the hermiticity+T relation (allowed: g1)', Trel(Avec) == sp.zeros(4))
check('(ii) B satisfies the hermiticity+T relation (allowed: g2)', Trel(Bvec) == sp.zeros(4))
resC = Trel(Cvec)
check('(ii) C violates it: C(P,q,S) = -[g C(Pt,qt,St) g]^T, so its coefficient must vanish',
      sp.simplify(resC - 2*Cvec(P, q, S)) == sp.zeros(4))
# current conservation of C and parity: C is built with one eps and one axial vector S -> true tensor
Cm = Cvec(P, q, S)
check('(iii) q_mu C^{mu nu} = 0 (C is current conserving; only T excludes it)',
      all(sp.simplify(sum(low(q)[m]*Cm[m, n] for m in range(4))) == 0 for n in range(4)))
# contraction of the antisymmetric parts with a symmetric lepton tensor vanishes
l, lp = sp.Matrix(sp.symbols('l0:4', real=True)), sp.Matrix(sp.symbols('m0:4', real=True))
Lsym = sp.Matrix(4, 4, lambda m, n: low(l)[m]*low(lp)[n] + low(lp)[m]*low(l)[n] - g[m, n]*dot(l, lp))
cA = sp.simplify(sum(Lsym[m, n]*Avec(P, q, S)[m, n] for m in range(4) for n in range(4)))
check('(iv) unpolarized (symmetric) lepton tensor contracted with the g1 structure = 0', cA == 0)
print('\nSUMMARY s11: %d PASS, %d FAIL' % (npass, nfail))
