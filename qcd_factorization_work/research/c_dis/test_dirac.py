"""
test_dirac.py -- independent numerical validation of dirac_d.py.
Explicit Clifford algebras in D = 4 (4x4) and D = 6 (8x8 matrices), metric (+,-,...,-).
For D = 6 the explicit trace has Tr 1 = 8, so it is compared with (8/4) * symbolic(D=6).
Checks contracted strings typical of the DIS calculation (two contracted index pairs).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import sympy as sp
import itertools
import dirac_d as dd

s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
id2 = np.eye(2, dtype=complex)


def kron_list(ms):
    out = np.array([[1]], dtype=complex)
    for m in ms:
        out = np.kron(out, m)
    return out


def clifford(Dim):
    """Minkowski gammas: gamma^0 hermitian, gamma^i antihermitian; {g^mu,g^nu} = 2 eta^{mu nu}"""
    m = Dim // 2
    euc = []
    for k in range(m):
        pre = [s3] * k
        post = [id2] * (m - k - 1)
        euc.append(kron_list(pre + [s1] + post))
        euc.append(kron_list(pre + [s2] + post))
    gam = [euc[0]] + [1j * e for e in euc[1:]]
    eta = np.diag([1.0] + [-1.0] * (Dim - 1))
    for a in range(Dim):
        for b in range(Dim):
            ac = gam[a] @ gam[b] + gam[b] @ gam[a]
            assert np.allclose(ac, 2 * eta[a, b] * np.eye(2 ** m))
    return gam, eta


def slash(v, gam, eta):
    return sum(eta[a, a] * v[a] * gam[a] for a in range(len(v)))


def numeric_trace(slots, vecs, gam, eta):
    """slots as for dd.tr; contracted indices summed explicitly with the metric."""
    Dim = len(eta)
    idx_names = sorted({s[1] for s in slots if isinstance(s, tuple)})
    total = 0
    for vals in itertools.product(range(Dim), repeat=len(idx_names)):
        asg = dict(zip(idx_names, vals))
        # one upper and one lower index per pair: lower = eta * upper (diagonal metric)
        seen = set()
        mat = np.eye(gam[0].shape[0], dtype=complex)
        fac = 1.0
        for s in slots:
            if isinstance(s, tuple):
                a = asg[s[1]]
                if s[1] in seen:
                    fac *= eta[a, a]
                seen.add(s[1])
                mat = mat @ gam[a]
            else:
                v = sum(c * vecs[n] for n, c in s.items())
                mat = mat @ slash(v, gam, eta)
        total += fac * np.trace(mat)
    return total


def check(Dim, slots, rng):
    gam, eta = clifford(Dim)
    names = sorted({n for s in slots if isinstance(s, dict) for n in s})
    vecs = {n: rng.normal(size=Dim) for n in names}
    table = {}
    for a in names:
        for b in names:
            table[(a, b)] = float(vecs[a] @ eta @ vecs[b])
    dd.set_dots(table)
    sym = dd.tr(slots).subs(dd.D, Dim)
    num = numeric_trace(slots, vecs, gam, eta) * (4.0 / gam[0].shape[0])
    return complex(sym), num


if __name__ == '__main__':
    rng = np.random.default_rng(1)
    I, V = dd.I, dd.V
    tests = {
        'Tr[g^a g_a]': [I('a'), I('a')],
        'Tr[g^a p g_a k]': [I('a'), V(p=1), I('a'), V(k=1)],
        'Tr[p g^m (p+q) g^r k g_r (p-k) g_m]  (2 pairs, nested)':
            [V(p=1), I('m'), V(p=1, q=1), I('r'), V(k=1), I('r'), V(p=1, k=-1), I('m')],
        'real-emission type: Tr[p g^m (p+q) g^s p2 g^s (p+q) g^m] interleaved':
            [V(p=1), I('m'), V(p=1, q=1), I('s'), V(k=1), I('m'), V(p=1, k=-1), I('s')],
        '10 gammas, 3 pairs': [V(p=1), I('a'), V(q=1), I('b'), V(k=1), I('a'), V(p=1, q=2),
                               I('c'), I('b'), I('c')],
    }
    ok = True
    for Dim in (2, 4, 6, 8):
        for name, sl in tests.items():
            s, n = check(Dim, sl, rng)
            good = abs(s - n) < 1e-9 * (1 + abs(n))
            ok &= good
            print(f'D={Dim}  {name:70s} sym={s.real: .10f} num={n.real: .10f}  {"PASS" if good else "FAIL"}')
    print('ALL PASS' if ok else 'SOME FAIL')
