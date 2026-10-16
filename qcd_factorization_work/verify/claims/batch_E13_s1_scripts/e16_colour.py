import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np

def sun_generators(N):
    """Hermitian generators t^A of SU(N), Tr(t^A t^B) = delta/2"""
    gens = []
    for i in range(N):
        for j in range(i+1, N):
            m = np.zeros((N, N), complex); m[i, j] = m[j, i] = 0.5; gens.append(m)
            m = np.zeros((N, N), complex); m[i, j] = -0.5j; m[j, i] = 0.5j; gens.append(m)
    for k in range(1, N):
        m = np.zeros((N, N), complex)
        for l in range(k): m[l, l] = 1
        m[k, k] = -k
        m *= 1/np.sqrt(2*k*(k+1))
        gens.append(m)
    return np.array(gens)

def structure_constants(t):
    # [t^A, t^B] = i f^{ABC} t^C  ->  f^{ABC} = -2 i Tr([t^A,t^B] t^C)
    comm = np.einsum('aij,bjk->abik', t, t) - np.einsum('bij,ajk->abik', t, t)
    f = -2j*np.einsum('abik,cki->abc', comm, t)
    return f.real

def run(N, emitter):
    t = sun_generators(N); f = structure_constants(t); NA = N*N - 1
    F = -1j*f            # adjoint generators (F^A)_{BC} = -i f^{ABC}
    # index layout of 4-parton tensors: emitter='q': M[ia, B, ic, D]  (a=incoming q, b=incoming g, c=outgoing q, d=gluon)
    #                                  emitter='g': M[A, ib, ic, D]   (a=incoming g, b=incoming q, c=outgoing q, d=gluon)
    def T(i, A, M):
        kind = {'q': ['qin', 'g', 'qout', 'g'], 'g': ['g', 'qin', 'qout', 'g']}[emitter][i]
        if kind == 'qout':   # left multiplication on that index
            return np.moveaxis(np.tensordot(t[A], M, axes=([1], [i])), 0, i)
        if kind == 'qin':    # minus right multiplication: (T M)_{..j..} = - sum_k M_{..k..} t^A_{k j}
            return -np.moveaxis(np.tensordot(t[A], M, axes=([0], [i])), 0, i)
        if kind == 'g':
            return np.moveaxis(np.tensordot(F[A], M, axes=([1], [i])), 0, i)
    def TdotT(i, j, M):
        return sum(T(i, A, T(j, A, M)) for A in range(NA))
    # Born amplitude and emission
    if emitter == 'q':
        born = np.einsum('Bci->iBc', t)                    # M[ia, B, ic] = t^B_{ic ia}
        # emission off incoming quark a: insert generator for index a ; new gluon index D
        M4 = np.zeros((N, NA, N, NA), complex)
        for D in range(NA):
            M4[:, :, :, D] = -np.einsum('iBc,ij->jBc', born, t[D])   # T_a^D acting on the incoming-quark index
    else:
        born = np.einsum('Aci->Aic', t)                    # M[A, ib, ic] = t^A_{ic ib}
        M4 = np.zeros((NA, N, N, NA), complex)
        for D in range(NA):
            M4[:, :, :, D] = np.tensordot(F[D], born, axes=([1], [0]))  # T_a^D on the incoming-gluon index
    norm_born = np.vdot(born, born).real
    # checks: colour conservation in 4-parton space and Casimir of emitter
    cons = max(np.abs(sum(T(i, A, M4) for i in range(4))).max() for A in range(NA))
    Ca = np.vdot(M4, M4).real/norm_born
    S = lambda M: TdotT(0, 0, M) + TdotT(1, 1, M) + 2*TdotT(0, 1, M)
    pairs = [(i, j) for i in range(4) for j in range(i+1, 4) if (i, j) != (0, 3)]
    Tad = lambda M: sum(TdotT(i, j, M) for (i, j) in pairs)
    v = M4
    SSv = S(S(v)); Sv = S(v); Tv = Tad(v)
    val = (np.vdot(SSv, Tv) - 2*np.vdot(Sv, Tad(Sv)) + np.vdot(Tv, SSv))/3
    return cons, Ca, val/norm_born

TR = 0.5
for N in (2, 3, 4):
    for em in ('q', 'g'):
        cons, Ca, r = run(N, em)
        pred = (8/3)*N**2*TR**4 if em == 'q' else -(32/3)*N**2*TR**4
        print("N=%d emitter=%s: colour conservation residual %.1e, t_a^2 = %.4f, A_a/sigma0 = %.6f%+.1ei, BFH: %.6f" % (N, em, cons, Ca, r.real, r.imag, pred))
