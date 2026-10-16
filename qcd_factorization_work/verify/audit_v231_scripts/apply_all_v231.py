"""Re-apply the audit fixes v2.3.1 to a copy of the v2.3 files (reproducibility check).

Usage:  python3 -I apply_all_v231.py TARGETDIR
Copies verify/audit_v231_backup/ (the v2.3 state of the edited files, plus the unchanged files needed by the
checkers) into TARGETDIR, runs parts a-k in order and leaves the result there; compare it with spec_v2/.
"""
import sys, os, shutil, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.dirname(os.path.dirname(HERE))
SPEC = os.path.join(WORK, 'spec_v2')
BACK = os.path.join(WORK, 'verify', 'audit_v231_backup')
T = sys.argv[1]
os.makedirs(os.path.join(T, 'checks'), exist_ok=True)
for fn in os.listdir(BACK):
    dst = os.path.join(T, 'checks', fn) if fn.endswith('.py') else os.path.join(T, fn)
    shutil.copy2(os.path.join(BACK, fn), dst)
for fn in ('refs_merged_v2.bib', 'key_aliases_v2.tsv'):       # unchanged by the audit
    shutil.copy2(os.path.join(SPEC, fn), os.path.join(T, fn))
for part in ('apply_audit_v231.py', 'apply_audit_v231b.py', 'apply_audit_v231c.py', 'apply_audit_v231d.py', 'apply_audit_v231e.py', 'apply_audit_v231f.py', 'apply_audit_v231g.py', 'apply_audit_v231h.py', 'apply_audit_v231i.py', 'apply_audit_v231j.py', 'apply_audit_v231k.py'):
    subprocess.run([sys.executable, '-I', os.path.join(HERE, part), T], check=True)
print('done:', T)
