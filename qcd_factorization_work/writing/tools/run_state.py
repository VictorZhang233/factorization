#!/usr/bin/env python3
"""Compute the resume plan for all registered workflow runs (writing/state/active_runs.json).
For each entry, `runs` lists the run IDs of the chain (oldest first; the last one is resumed). The `done` list is the
union of the labels that produced a result in ANY run of the chain. Writes writing/state/RESUME_PLAN.json with, per
entry: scriptPath, resumeFromRunId, args = base args + {resume: true, done: [...], skip: [...]}.
Also persists every completed agent's structured result to writing/state/results/<run>/<label>.md."""
import os, sys, json, subprocess
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = '/Users/hao-cheng/.claude/projects/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/subagents/workflows'
runs = json.load(open(os.path.join(W, 'state', 'active_runs.json')))
plan = []
for r in runs:
    done = []
    inflight = set()
    for rid in r['runs']:
        J = os.path.join(D, rid, 'journal.jsonl')
        if not os.path.exists(J): continue
        L = [json.loads(l) for l in open(J)]
        lab = {}
        for e in L:
            if e.get('type') == 'started': lab[e['agentId']] = e['label']
        res_ids = {e['agentId'] for e in L if e.get('type') == 'result'}
        for aid, l in lab.items():
            if aid in res_ids and l not in done: done.append(l)
        inflight |= {l for aid, l in lab.items() if aid not in res_ids}
        subprocess.run([sys.executable, '-I', os.path.join(W, 'tools', 'persist_journal.py'), J,
                        os.path.join(W, 'state', 'results', rid)], capture_output=True)
    args = dict(r.get('base_args') or json.load(open(os.path.join(W, r['base_args_file']))))
    args.update(resume=True, done=done)
    if r.get('skip'): args['skip'] = r['skip']
    plan.append(dict(name=r['name'], scriptPath=r['script'], resumeFromRunId=r['runs'][-1], args=args,
                     n_done=len(done), inflight=sorted(inflight - set(done))))
json.dump(plan, open(os.path.join(W, 'state', 'RESUME_PLAN.json'), 'w'), indent=1, ensure_ascii=False)
for p in plan:
    print(f"{p['name']:12s} resume {p['resumeFromRunId']}  done {p['n_done']:3d}  in flight: {', '.join(p['inflight'])[:150]}")
