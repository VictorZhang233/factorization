# Common helpers for the W23 (Ch20 heavy) verification scripts.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

class Check:
    def __init__(self, title):
        self.title = title; self.n_pass = 0; self.n_fail = 0
        print('=' * 100); print(title); print('=' * 100)
    def __call__(self, label, ok, info=''):
        ok = bool(ok)
        if ok: self.n_pass += 1
        else: self.n_fail += 1
        print(('PASS ' if ok else 'FAIL ') + label + (('   [' + str(info) + ']') if info != '' else ''))
    def summary(self):
        print('-' * 100)
        print('%s: %d PASS, %d FAIL' % (self.title, self.n_pass, self.n_fail))
        return self.n_fail == 0
