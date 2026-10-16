import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import t3_regulator as T
m = T.model(1.0, 'author'); lamB = abs(m['d0B']); a = np.sqrt(m['a1']*m['a2'])
for Kr in (1.0, 0.1):
    K = Kr*a/lamB
    for th in (np.pi/8, np.pi/4, 3*np.pi/8):
        print(f"K = {Kr} a/lamB, theta/pi = {th/np.pi:.3f}: W12 = {0.5 + T.Phi(m, th, K=K):.8f}", flush=True)
