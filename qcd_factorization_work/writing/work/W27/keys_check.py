import re, sys, os
W = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(W, '..', '..', '..'))
bib = open(os.path.join(ROOT, 'spec_v2', 'refs_merged_v2.bib'), encoding='utf-8').read()
keys = set(re.findall(r'@\w+\{([^,\s]+),', bib))
pack = open(os.path.join(ROOT, 'writing', 'packs', 'W27', 'PACK.md'), encoding='utf-8').read()
# key list section of the pack
i = pack.index('### Key citation keys (Ch24)'); j = pack.index('### Verification outcomes (Ch24')
sec = pack[i:j]
cand = sorted(set(re.findall(r'`([A-Za-z][A-Za-z0-9:\-_]+)`', sec)))
missing = [k for k in cand if k not in keys]
print('candidate keys in pack list:', len(cand))
print('missing from bib:', missing)
# extra keys mentioned elsewhere in the Ch24 outline section
k0 = pack.index('## Chapter 24'); k1 = pack.index('# Part VII annexes')
ch = pack[k0:k1]
cand2 = sorted(set(re.findall(r'`([A-Z][A-Za-z\-]+:?[0-9]{4}[a-z]{0,3}|[A-Z][A-Za-z\-]+[0-9]{4}[a-z]?)`', ch)))
print('keys mentioned in Ch24 section:', len(cand2))
print('missing (Ch24 section):', [k for k in cand2 if k not in keys])
