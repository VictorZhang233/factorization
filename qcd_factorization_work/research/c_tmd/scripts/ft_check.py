# Check of the d-dimensional Fourier transform used for b-space TMDs:
#   int d^d k e^{-i k.b} (k^2)^{-a} = pi^{d/2} 2^{d-2a} Gamma(d/2-a)/Gamma(a) (b^2)^{a-d/2}
# via the radial (Hankel) representation
#   int d^d k e^{-i k.b} F(|k|) = (2 pi)^{d/2} b^{1-d/2} int_0^inf dk k^{d/2} J_{d/2-1}(k b) F(k)
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 30

def lhs(d, a, b):
    nu = mp.mpf(d) / 2 - 1
    f = lambda k: k**(mp.mpf(d) / 2) * mp.besselj(nu, k * b) * k**(-2 * a)
    # endpoint singularity at k=0 handled by tanh-sinh on [0,1]; oscillatory tail by quadosc
    I = mp.quad(f, [0, mp.mpf(1)/4, 1]) + mp.quadosc(f, [1, mp.inf], omega=b)
    return (2 * mp.pi)**(mp.mpf(d) / 2) * b**(1 - mp.mpf(d) / 2) * I

def rhs(d, a, b):
    d = mp.mpf(d)
    return mp.pi**(d / 2) * 2**(d - 2 * a) * mp.gamma(d / 2 - a) / mp.gamma(a) * (b**2)**(a - d / 2)

ok = True
for (d, a, b) in [(2, 0.6, 1.3), (2, 0.8, 0.7), (2.4, 0.9, 1.1), (2.6, 1.05, 0.5), (1.8, 0.7, 2.0)]:
    l, r = lhs(d, mp.mpf(a), mp.mpf(b)), rhs(d, mp.mpf(a), mp.mpf(b))
    rel = abs(l / r - 1)
    ok &= rel < 1e-8
    print('d=%.2f a=%.2f b=%.2f   numeric=%s  formula=%s  rel.diff=%.1e' % (d, a, b, mp.nstr(l, 15), mp.nstr(r, 15), rel))
print('FT formula: PASS' if ok else 'FT formula: FAIL')
