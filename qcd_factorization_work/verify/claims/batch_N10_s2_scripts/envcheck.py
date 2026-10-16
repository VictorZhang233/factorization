import sys,os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy, sympy, mpmath
print(sys.version)
print("numpy", numpy.__version__, "sympy", sympy.__version__, "mpmath", mpmath.__version__)
try:
    import scipy; print("scipy", scipy.__version__)
except Exception as e:
    print("no scipy", e)
