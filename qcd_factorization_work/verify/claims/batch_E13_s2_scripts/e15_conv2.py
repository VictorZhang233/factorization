import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
exec(open('e15_conv.py').read().split('eps = 0.1')[0])
def nat(h, delta=0.5, L=6.0):
    x = np.arange(-L, L + h/2, h) + h/2
    ER, PR = np.meshgrid(x, x, indexing='ij'); E = ER + 1j*delta; p = PR + 0j
    return (1j*np.exp(-(E**2+p**2)/Q**2)/(E - p**2/(2*m))).sum()*h*h
for h in [0.004, 0.002, 0.001]:
    r = nat(h)
    a2 = integ('anom2', 1, 0.0, h, offset=h/2)
    a1 = integ('anom1', 1, 0.0, h, offset=h/2)
    print(f'h={h}: ref {r:.9f}  anom2(eps=0) {a2:.9f} diff {abs(a2-r):.2e}   anom1(eps=0) {a1:.9f} diff {abs(a1-r):.2e}')
