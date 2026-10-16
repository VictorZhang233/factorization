import re, sys
f = sys.argv[1]; a = int(sys.argv[2]); b = int(sys.argv[3]); w = int(sys.argv[4]) if len(sys.argv) > 4 else 350
L = open(f, encoding='utf-8').read().split('\n')
pat = re.compile(r'PENDING-VERIFY|待文献核查|文献待补|文献待補|PENDING')
for i in range(a - 1, min(b, len(L))):
    l = L[i]
    if not pat.search(l):
        continue
    print('=' * 8, i + 1, 'len', len(l), 'START:', l[:110])
    last = -1
    for m in pat.finditer(l):
        if m.start() < last:
            continue
        s = max(0, m.start() - w); e = min(len(l), m.end() + w)
        print('   ...', l[s:e])
        last = e
