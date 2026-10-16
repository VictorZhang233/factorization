#!/usr/bin/env python3
"""Persist the structured results of a workflow journal as readable files.
usage: python3 -I persist_journal.py <journal.jsonl> <outdir>
Writes <outdir>/<label>.md for every completed agent (writer reports, reviews, revisions, pre-writing stages)."""
import json, os, sys

def fmt(v, depth=2):
    if v is None: return '(null)\n'
    if isinstance(v, str): return v + '\n'
    if isinstance(v, list):
        out = []
        for i, x in enumerate(v):
            if isinstance(x, dict) and {'severity', 'location', 'problem', 'fix'} <= set(x):
                out.append(f"{i+1}. **[{x['severity']}]** {x['location']}\n   - problem: {x['problem']}\n   - fix: {x['fix']}\n")
            elif isinstance(x, dict):
                out.append(f"{i+1}. " + '; '.join(f"**{k}**: {x[k]}" for k in x) + '\n')
            else:
                out.append(f"{i+1}. {x}\n")
        return ''.join(out)
    if isinstance(v, dict):
        out = []
        for k, x in v.items():
            out.append('#' * depth + f' {k}\n\n' + fmt(x, depth + 1) + '\n')
        return ''.join(out)
    return str(v) + '\n'

def main():
    J, out = sys.argv[1], sys.argv[2]
    os.makedirs(out, exist_ok=True)
    L = [json.loads(l) for l in open(J)]
    lab = {e['key']: e.get('label') for e in L if e.get('type') == 'started'}
    n = 0
    for e in L:
        if e.get('type') != 'result': continue
        label = lab.get(e.get('key')) or e.get('key')
        val = e.get('value', e.get('result'))
        if val is None: continue
        with open(os.path.join(out, f'{label}.md'), 'w') as f:
            f.write(f'# {label}\n\n(structured result persisted from {os.path.basename(os.path.dirname(J))})\n\n')
            f.write(fmt(val))
        n += 1
    print(f'{n} results written to {out}')

if __name__ == '__main__':
    main()
