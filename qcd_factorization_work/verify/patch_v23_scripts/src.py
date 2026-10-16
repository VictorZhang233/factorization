"""Helpers: original (pre-patch) lines of the spec files, by line number."""
import os
BACK = '/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/patch_backup_spec_v2_prepatch'
_cache = {}
def lines(fname):
    if fname not in _cache:
        _cache[fname] = open(os.path.join(BACK, fname), encoding='utf-8').read().split('\n')
    return _cache[fname]
def ln(n, fname='FINAL_OUTLINE_v2.md'):
    return lines(fname)[n - 1]
def block(a, b, fname='FINAL_OUTLINE_v2.md'):
    """lines a..b inclusive joined with newlines (no trailing newline)"""
    return '\n'.join(lines(fname)[a - 1:b])
def find(sub, fname='FINAL_OUTLINE_v2.md'):
    hits = [i + 1 for i, l in enumerate(lines(fname)) if sub in l]
    if len(hits) != 1:
        raise SystemExit('src.find: %r occurs on %d lines %s' % (sub[:80], len(hits), hits[:5]))
    return hits[0]
