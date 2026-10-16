#!/usr/bin/env python3
"""Local token meter (read-only): sums the API usage recorded in Claude Code transcripts (*.jsonl under
~/.claude/projects/<project>/ and the session's task outputs), deduplicated per API message, as cost-weighted tokens
  w = input + 1.25*cache_creation + 0.1*cache_read + 5*output   (Anthropic price ratios).
usage: token_meter.py hourly [--since ISO] | window START_ISO END_ISO
Times are local (America/New_York offset taken from the system)."""
import os, sys, json, glob, datetime as dt
PROJ = os.path.expanduser('~/.claude/projects/-Users-hao-cheng-Desktop-theorem-proof')
TASKS = '/private/tmp/claude-501/-Users-hao-cheng-Desktop-theorem-proof'

def files(since_ts):
    out = []
    for root in (PROJ, TASKS):
        for p in glob.glob(os.path.join(root, '**', '*.jsonl'), recursive=True) + glob.glob(os.path.join(root, '**', '*.output'), recursive=True):
            try:
                if os.path.getmtime(p) >= since_ts: out.append(p)
            except OSError: pass
    return out

def records(since_ts):
    seen = {}
    for p in files(since_ts):
        try:
            with open(p, errors='ignore') as f:
                for line in f:
                    if '"usage"' not in line: continue
                    try: e = json.loads(line)
                    except Exception: continue
                    m = e.get('message') or {}
                    u = m.get('usage') or {}
                    if not u or m.get('model') == '<synthetic>': continue
                    ts = e.get('timestamp')
                    if not ts: continue
                    t = dt.datetime.fromisoformat(ts.replace('Z', '+00:00')).timestamp()
                    if t < since_ts: continue
                    key = m.get('id') or e.get('requestId') or (p, ts)
                    w = (u.get('input_tokens') or 0) + 1.25 * (u.get('cache_creation_input_tokens') or 0) \
                        + 0.1 * (u.get('cache_read_input_tokens') or 0) + 5 * (u.get('output_tokens') or 0)
                    if key not in seen or w > seen[key][1]: seen[key] = (t, w)
        except OSError: pass
    return sorted(seen.values())

def parse(s):
    return dt.datetime.fromisoformat(s).timestamp()

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'hourly'
    if mode == 'hourly':
        since = parse(sys.argv[3]) if len(sys.argv) > 3 else dt.datetime.now().timestamp() - 30 * 3600
        R = records(since)
        b = {}
        for t, w in R:
            h = dt.datetime.fromtimestamp(t).strftime('%m-%d %H:00')
            b[h] = b.get(h, 0) + w
        for h in sorted(b): print(f'{h}  {b[h]/1e6:9.2f} M weighted tokens')
    elif mode == 'window':
        a, z = parse(sys.argv[2]), parse(sys.argv[3])
        R = [x for x in records(a) if x[0] <= z]
        print(f'{sys.argv[2]} .. {sys.argv[3]}: {sum(w for _, w in R)/1e6:.2f} M weighted tokens, {len(R)} API messages')
