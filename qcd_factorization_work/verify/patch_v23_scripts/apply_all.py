"""Master patch applier: restores each target file from the pre-patch backup and applies all patch modules in order.
Each patch module defines TARGET (file name in spec_v2) and OPS: list of ops:
  ('rep', old, new)            exact substring replacement, old must occur exactly once
  ('repn', old, new, n)        exact substring replacement, old must occur exactly n times (all replaced)
  ('range', start, end, new, incl_end)  replace from start anchor (inclusive) to end anchor (inclusive if incl_end) ; anchors unique
"""
import sys, os, glob, importlib.util, shutil
SPEC = '/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/spec_v2'
BACK = '/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/patch_backup_spec_v2_prepatch'
HERE = os.path.dirname(os.path.abspath(__file__))
mods = sorted(glob.glob(os.path.join(HERE, 'p[0-9][0-9]_*.py')))
only = sys.argv[1:]  # optional list of targets to rebuild
texts = {}
def load(target):
    if target not in texts:
        texts[target] = open(os.path.join(BACK, target), encoding='utf-8').read()
    return texts[target]
sys.path.insert(0, HERE)
import src as _src
_src.TEXTS = texts
for m in mods:
    spec = importlib.util.spec_from_file_location(os.path.basename(m)[:-3], m)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    t = load(mod.TARGET)
    for k, op in enumerate(mod.OPS):
        kind = op[0]
        if kind == 'rep':
            _, old, new = op
            c = t.count(old)
            if c != 1:
                raise SystemExit('%s op %d (rep): old occurs %d times: %r' % (os.path.basename(m), k, c, old[:160]))
            t = t.replace(old, new)
        elif kind == 'repn':
            _, old, new, n = op
            c = t.count(old)
            if c != n:
                raise SystemExit('%s op %d (repn): old occurs %d times (expected %d): %r' % (os.path.basename(m), k, c, n, old[:160]))
            t = t.replace(old, new)
        elif kind == 'range':
            _, start, end, new, incl = op
            cs, ce = t.count(start), t.count(end)
            if cs != 1 or ce < 1:
                raise SystemExit('%s op %d (range): start %d / end %d occurrences: %r ... %r' % (os.path.basename(m), k, cs, ce, start[:100], end[:100]))
            i = t.index(start); j = t.index(end, i)
            if incl: j += len(end)
            t = t[:i] + new + t[j:]
        elif kind == 'func':
            t = op[1](t)
        elif kind == 'sub':
            # ('sub', old, new, line_contains): replace old -> new only on the unique line containing line_contains
            _, old, new, key = op
            lines = t.split('\n')
            idx = [i for i, l in enumerate(lines) if key in l]
            if len(idx) != 1:
                raise SystemExit('%s op %d (sub): key occurs on %d lines: %r' % (os.path.basename(m), k, len(idx), key[:120]))
            i = idx[0]
            c = lines[i].count(old)
            if c != 1:
                raise SystemExit('%s op %d (sub): old occurs %d times on line %d: %r' % (os.path.basename(m), k, c, i + 1, old[:120]))
            lines[i] = lines[i].replace(old, new)
            t = '\n'.join(lines)
        else:
            raise SystemExit('unknown op ' + kind)
    texts[mod.TARGET] = t
    print('applied', os.path.basename(m), '->', mod.TARGET, len(mod.OPS), 'ops')
for target, t in texts.items():
    if only and target not in only:
        continue
    open(os.path.join(SPEC, target), 'w', encoding='utf-8').write(t)
    print('wrote', target, len(t))
