import os, re
TARGET = 'key_aliases_v2.tsv'
PART10 = '/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/spec_v2/checks/refs_part10_v23.bib'
KEYS = re.findall(r'@\w+\{([^,]+),', open(PART10, encoding='utf-8').read())
MANUAL = {'Hormander2003', 'Vladimirov2002', 'NilssonPassare2013'}

def add_rows(t):
    have = set(l.split('\t')[0] for l in t.split('\n') if l)
    rows = []
    for k in KEYS:
        if k in have:
            continue
        rows.append('%s\t%s\t%s' % (k, k, 'spec-v2.3 manual new entry (Crossref)' if k in MANUAL else 'spec-v2.3 INSPIRE new entry'))
    body = t.rstrip('\n')
    return body + '\n' + '\n'.join(rows) + '\n'

OPS = [('func', add_rows)]
