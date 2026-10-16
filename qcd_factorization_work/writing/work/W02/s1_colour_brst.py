"""W02 / Ch2 check s1: SU(N) colour identities (lem:qcd-colour-identities, ex:qcd-colour-algebra)
and the tensor identities behind s^2 = 0 (lem:prelim-brst-nilpotent, App J).
Conventions: [t^a,t^b] = i f^{abc} t^c, Tr(t^a t^b) = delta^{ab}/2, (F^a)_{bc} = -i f^{abc}.
Run: python3 -I s1_colour_brst.py
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np

npass = nfail = 0
def report(ok, name):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)

def generators(N):
    """Hermitian traceless generators normalised Tr(t^a t^b) = delta/2 (generalised Gell-Mann)."""
    gens = []
    for i in range(N):
        for j in range(i + 1, N):
            m = np.zeros((N, N), complex); m[i, j] = m[j, i] = 1; gens.append(m / 2)
            m = np.zeros((N, N), complex); m[i, j] = -1j; m[j, i] = 1j; gens.append(m / 2)
    for k in range(1, N):
        m = np.zeros((N, N), complex)
        for i in range(k): m[i, i] = 1
        m[k, k] = -k
        gens.append(m / np.sqrt(2 * k * (k + 1)))
    return np.array(gens)

for N in (2, 3, 4):
    t = generators(N); n = len(t)
    CF, CA = (N * N - 1) / (2 * N), N
    tr2 = np.einsum('aij,bji->ab', t, t)
    report(np.allclose(tr2, np.eye(n) / 2), f'SU({N}): Tr(t^a t^b) = delta^ab/2, hermitian traceless')
    f = np.zeros((n, n, n)); d = np.zeros((n, n, n))
    for a, b, c in itertools.product(range(n), repeat=3):
        comm = t[a] @ t[b] - t[b] @ t[a]; acomm = t[a] @ t[b] + t[b] @ t[a]
        f[a, b, c] = np.real(-2j * np.trace(comm @ t[c]))
        d[a, b, c] = np.real(2 * np.trace(acomm @ t[c]))
    ok = all(np.allclose(t[a] @ t[b] - t[b] @ t[a], 1j * np.einsum('c,cij->ij', f[a, b], t)) for a in range(n) for b in range(n))
    report(ok and np.allclose(f, -np.swapaxes(f, 0, 1)) and np.allclose(f, np.einsum('abc->bca', f)), f'SU({N}): [t^a,t^b]=i f t, f real and totally antisymmetric')
    # (i) Fierz
    lhs = np.einsum('aij,akl->ijkl', t, t)
    I = np.eye(N)
    rhs = 0.5 * (np.einsum('il,kj->ijkl', I, I) - np.einsum('ij,kl->ijkl', I, I) / N)
    report(np.allclose(lhs, rhs), f'SU({N}) (i): Fierz t^a_ij t^a_kl = 1/2(d_il d_kj - d_ij d_kl/N)')
    # (ii) Casimirs
    report(np.allclose(np.einsum('aij,ajk->ik', t, t), CF * I), f'SU({N}) (ii): t^a t^a = C_F 1, C_F = {CF}')
    report(np.allclose(np.einsum('acd,bcd->ab', f, f), CA * np.eye(n)), f'SU({N}) (ii): f^acd f^bcd = C_A delta, C_A = {N}')
    # (iii) t^b t^a t^b = (C_F - C_A/2) t^a = -1/(2N) t^a
    ok = all(np.allclose(np.einsum('bij,jk,bkl->il', t, t[a], t), (CF - CA / 2) * t[a]) for a in range(n))
    report(ok and np.isclose(CF - CA / 2, -1 / (2 * N)), f'SU({N}) (iii): t^b t^a t^b = (C_F - C_A/2) t^a = -t^a/(2N)')
    # (iv) Tr(t^a t^b t^c) = (d + i f)/4
    tr3 = np.einsum('aij,bjk,cki->abc', t, t, t)
    report(np.allclose(tr3, (d + 1j * f) / 4), f'SU({N}) (iv): Tr(t^a t^b t^c) = (d^abc + i f^abc)/4')
    # (v) Jacobi and adjoint representation
    jac = np.einsum('abe,ecd->abcd', f, f) + np.einsum('bce,ead->abcd', f, f) + np.einsum('cae,ebd->abcd', f, f)
    F = -1j * f   # (F^a)_{bc} = -i f^{abc}
    comm = np.einsum('abc,acd->abd', F, F)  # placeholder (not used)
    ok = all(np.allclose(F[a] @ F[b] - F[b] @ F[a], 1j * np.einsum('c,cij->ij', f[a, b], F)) for a in range(n) for b in range(n))
    report(np.allclose(jac, 0) and ok, f'SU({N}) (v): Jacobi identity, [F^a,F^b] = i f^abc F^c')
    report(np.allclose(np.einsum('aij,bji->ab', F, F), CA * np.eye(n)), f'SU({N}): Tr(F^a F^b) = C_A delta^ab')
    # (vi) i f^abc t^b t^c = -(C_A/2) t^a
    lhs = 1j * np.einsum('abc,bij,cjk->aik', f, t, t)
    report(np.allclose(lhs, -CA / 2 * t), f'SU({N}) (vi): i f^abc t^b t^c = -(C_A/2) t^a')
    # one-loop colour factors (ex:qcd-colour-algebra)
    # quark self-energy: t^b t^b = C_F; quark loop in gluon self-energy: Tr(t^a t^b) n_f = T_F n_f delta
    # gluon/ghost loop: f^acd f^bcd = C_A delta;
    # vertex, abelian-like graph: t^b t^a t^b = (C_F - C_A/2) t^a; non-abelian graph: f^{abc} t^b t^c (x i) -> C_A/2
    lhs = np.einsum('abc,bij,cjk->aik', f, t, t)   # f^{abc} t^b t^c = (i C_A/2) t^a
    report(np.allclose(lhs, 1j * CA / 2 * t), f'SU({N}): f^abc t^b t^c = (i C_A/2) t^a  [non-abelian vertex graph]')
    # ghost-loop colour of three-gluon function: Tr(F^a F^b F^c) = i (N/2) f^abc
    tr3F = np.einsum('aij,bjk,cki->abc', F, F, F)
    report(np.allclose(tr3F, 1j * N / 2 * f), f'SU({N}): Tr(F^a F^b F^c) = i (C_A/2) f^abc')
    # ---- BRST tensor identities ----
    # s^2 A = 0 needs: sum over antisymmetrised (d,e) of [-1/2 f^{abx} f^{xde} + f^{axe} f^{xbd}] = 0
    T = -0.5 * np.einsum('abx,xde->abde', f, f) + np.einsum('axe,xbd->abde', f, f)
    report(np.allclose(T - np.swapaxes(T, 2, 3), 0), f'SU({N}) BRST: coefficient of g^2 A^b c^d c^e in s^2 A^a vanishes (Jacobi)')
    # s^2 c = 0 needs: f^{ade} f^{dxy} totally antisymmetrised in (x,y,e) = 0
    U = np.einsum('ade,dxy->axye', f, f)
    Ua = sum(np.sign(np.linalg.det(np.eye(3)[list(p)])) * np.transpose(U, (0,) + tuple(1 + q for q in p)) for p in itertools.permutations(range(3)))
    report(np.allclose(Ua, 0), f'SU({N}) BRST: f^ade f^dxy antisymmetrised in (x,y,e) = 0, i.e. s^2 c = 0')
    # s^2 psi = 0 needs: -(i/2) f^{abc} c^b c^c t^a + c^a c^b t^a t^b = 0 as a coefficient of the antisymmetric c^b c^c
    V1 = -0.5j * np.einsum('abc,aij->bcij', f, t)          # coefficient of c^b c^c
    V2 = np.einsum('bij,cjk->bcik', t, t)                  # coefficient of c^b c^c from c^b c^c t^b t^c
    W = V1 + V2
    report(np.allclose(W - np.swapaxes(W, 0, 1), 0), f'SU({N}) BRST: s^2 psi = 0 (antisymmetric part of the c^b c^c coefficient vanishes)')

print(f'\nSUMMARY: {npass}/{npass + nfail} PASS')
