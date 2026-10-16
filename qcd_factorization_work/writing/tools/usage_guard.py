#!/usr/bin/env python3
"""Usage guard for long multi-agent runs (read-only with respect to Claude Code; standard library only).

Claude Code does not expose the plan-usage percentages to this session, so the guard ESTIMATES them:
  * it meters the API usage recorded in this project's local transcripts (cost-weighted tokens
    w = input + 1.25*cache_creation + 0.1*cache_read + 5*output, deduplicated per API message), incrementally;
  * it converts tokens to percentages with calibration constants measured on this project's own history
    (2026-10-14: a fresh 5-hour window went from 0 % to the limit after ≈271 M weighted tokens; a weekly limit
    was reached after ≈813 M) — K5 ≈ 2.71 M per % of the 5-hour window, KW ≈ 8.13 M per % of the week;
  * it is anchored to the percentages the user reads from /usage (command `calibrate`), and re-anchored at every
    5-hour reset.

Commands
  calibrate --five P --five-reset 'YYYY-MM-DD HH:MM' --week P --week-reset 'YYYY-MM-DD HH:MM' [--account NAME]
  status
  watch [--five-max 75] [--week-max 66] [--interval 120]     exit 10: limit reached (pause now); 12: not calibrated
  wait  [--five-max 75] [--week-max 66] [--interval 300]     exit 0: may resume; 20: weekly limit (wait for the
                                                             weekly reset or another account)
PRIMARY SOURCE (since 2026-10-14): the user's local menu-bar app "Claude Usage" (bundle HamedElfayome.Claude-Usage)
stores the official per-account numbers (5-hour sessionPercentage/sessionResetTime, weeklyPercentage/weeklyResetTime,
model-specific weekly percentages, lastUpdated) in its preferences; the guard reads them via `defaults export`
(credentials in that data are never printed or used). The profile is matched to the account Claude Code is logged in
with (email in ~/.claude.json vs. the profile's account JSON), else the app's active profile. The token estimate above
is the fallback when the app data are stale (> STALE_S seconds) or missing.
Times are local. State: writing/state/usage_state.json, meter cache writing/state/meter_cache.json, log usage_log.tsv.
"""
import os, sys, json, glob, time, argparse, datetime as dt

W = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STATE = os.path.join(W, 'writing', 'state')
SFILE = os.path.join(STATE, 'usage_state.json')
CFILE = os.path.join(STATE, 'meter_cache.json')
LOG = os.path.join(STATE, 'usage_log.tsv')
ROOTS = [os.path.expanduser('~/.claude/projects/-Users-hao-cheng-Desktop-theorem-proof'),
         '/private/tmp/claude-501/-Users-hao-cheng-Desktop-theorem-proof']
K5 = 2.71e6     # weighted tokens per % of the 5-hour window (calibrated 2026-10-14, Max 20x)
KW = 8.13e6     # weighted tokens per % of the weekly quota (calibrated 2026-10-10/11)
FIVE_H = 5 * 3600
APP_DOMAIN = 'HamedElfayome.Claude-Usage'
STALE_S = 600
APPLE_EPOCH = 978307200

def _ts(x):
    if not x: return None
    return x + APPLE_EPOCH if x < 1.5e9 else x

def app_profiles():
    """Return (profiles, matched_index) from the Claude Usage app, or (None, None). No credential is returned."""
    import subprocess, plistlib
    try:
        raw = subprocess.run(['defaults', 'export', APP_DOMAIN, '-'], capture_output=True, timeout=20).stdout
        d = plistlib.loads(raw)
        P = json.loads(d['profiles_v3'])
    except Exception:
        return None, None
    try:
        me = (json.load(open(os.path.expanduser('~/.claude.json'))).get('oauthAccount') or {}).get('emailAddress')
    except Exception:
        me = None
    out, match = [], None
    for i, p in enumerate(P):
        u = p.get('claudeUsage') or {}
        try:
            em = (json.loads(p.get('oauthAccountJSON') or '{}') or {}).get('emailAddress')
        except Exception:
            em = None
        if me and em and em == me: match = i
        out.append(dict(name=p.get('name'), active=(p.get('id') == d.get('activeProfileId')),
                        five=u.get('sessionPercentage'), five_reset=_ts(u.get('sessionResetTime')),
                        week=max([x for x in (u.get('weeklyPercentage'), u.get('opusWeeklyPercentage')) if x is not None] or [None]),
                        week_reset=_ts(u.get('weeklyResetTime')), updated=_ts(u.get('lastUpdated'))))
    if match is None:
        match = next((i for i, q in enumerate(out) if q['active']), None)
    return out, match

def app_line(q, tag=''):
    f = lambda t: fmt(t) if t else '-'
    return (f"{tag}{q['name']}: 5h {q['five']}% (resets {f(q['five_reset'])}), week {q['week']}% (resets {f(q['week_reset'])}), "
            f"updated {f(q['updated'])}")

def now(): return time.time()
def fmt(t): return dt.datetime.fromtimestamp(t).strftime('%m-%d %H:%M')
def parse_local(s): return dt.datetime.strptime(s, '%Y-%m-%d %H:%M').timestamp()

# ---------------------------------------------------------------- incremental meter
def load_cache():
    try: return json.load(open(CFILE))
    except Exception: return {'offsets': {}, 'buckets': {}, 'keys': []}

def meter_update(since):
    """Read new transcript bytes; accumulate weighted tokens in 1-minute buckets (keys = unix minute)."""
    c = load_cache()
    off, buckets = c['offsets'], c['buckets']
    keys = set(c['keys'])
    paths = []
    for r in ROOTS:
        paths += glob.glob(os.path.join(r, '**', '*.jsonl'), recursive=True)
        paths += glob.glob(os.path.join(r, '**', '*.output'), recursive=True)
    for p in paths:
        try:
            st = os.stat(p)
        except OSError:
            continue
        if st.st_mtime < since: continue
        o = off.get(p, 0)
        if st.st_size < o: o = 0            # file rewritten
        if st.st_size == o: continue
        try:
            with open(p, 'rb') as f:
                f.seek(o)
                data = f.read()
        except OSError:
            continue
        last_nl = data.rfind(b'\n')
        if last_nl < 0: continue
        chunk, o2 = data[:last_nl + 1], o + last_nl + 1
        for line in chunk.split(b'\n'):
            if b'"usage"' not in line: continue
            try: e = json.loads(line)
            except Exception: continue
            m = e.get('message') or {}
            u = m.get('usage') or {}
            if not u or m.get('model') == '<synthetic>' or not e.get('timestamp'): continue
            k = m.get('id') or e.get('requestId')
            if k and k in keys: continue
            if k: keys.add(k)
            t = dt.datetime.fromisoformat(e['timestamp'].replace('Z', '+00:00')).timestamp()
            w = (u.get('input_tokens') or 0) + 1.25 * (u.get('cache_creation_input_tokens') or 0) \
                + 0.1 * (u.get('cache_read_input_tokens') or 0) + 5 * (u.get('output_tokens') or 0)
            b = str(int(t // 60))
            buckets[b] = buckets.get(b, 0) + w
        off[p] = o2
    # prune: buckets older than 9 days, keep the most recent 60k keys
    cutoff = int((now() - 9 * 86400) // 60)
    c['buckets'] = {b: v for b, v in buckets.items() if int(b) >= cutoff}
    c['keys'] = list(keys)[-60000:]
    c['offsets'] = off
    tmp = CFILE + '.tmp'
    json.dump(c, open(tmp, 'w'))
    os.replace(tmp, CFILE)
    return c['buckets']

def tokens(buckets, a, b):
    lo, hi = int(a // 60), int(b // 60)
    return sum(v for k, v in buckets.items() if lo <= int(k) <= hi)

# ---------------------------------------------------------------- estimates
def load_state():
    try: return json.load(open(SFILE))
    except Exception: return None

def save_state(s):
    tmp = SFILE + '.tmp'
    json.dump(s, open(tmp, 'w'), indent=1)
    os.replace(tmp, SFILE)

def estimate(s, buckets, t=None):
    t = t or now()
    # 5-hour window: roll the anchor forward over every reset that has passed
    a5, p5, r5 = s['five_anchor'], s['five_pct'], s['five_reset']
    while t >= r5:
        a5, p5, r5 = r5, 0.0, r5 + FIVE_H
    est5 = p5 + tokens(buckets, a5, t) / K5
    aw, pw, rw = s['week_anchor'], s['week_pct'], s['week_reset']
    while t >= rw:
        aw, pw, rw = rw, 0.0, rw + 7 * 86400
    estw = pw + tokens(buckets, aw, t) / KW
    return dict(five=est5, five_reset=r5, week=estw, week_reset=rw)

def log(line):
    with open(LOG, 'a') as f: f.write(line + '\n')

def report(s, e):
    return (f"{fmt(now())}  account={s.get('account','?')}  5h≈{e['five']:.1f}% (resets {fmt(e['five_reset'])})  "
            f"week≈{e['week']:.1f}% (resets {fmt(e['week_reset'])})")

# ---------------------------------------------------------------- commands
def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='cmd', required=True)
    c = sub.add_parser('calibrate')
    c.add_argument('--five', type=float, required=True); c.add_argument('--five-reset', required=True)
    c.add_argument('--week', type=float, required=True); c.add_argument('--week-reset', required=True)
    c.add_argument('--account', default='?')
    sub.add_parser('status')
    for name, iv in (('watch', 60), ('wait', 120)):
        x = sub.add_parser(name)
        x.add_argument('--five-max', type=float, default=77.0)
        x.add_argument('--week-max', type=float, default=69.0)
        x.add_argument('--interval', type=int, default=iv)
    a = ap.parse_args()
    os.makedirs(STATE, exist_ok=True)

    if a.cmd == 'calibrate':
        t = now()
        s = dict(account=a.account, calibrated_at=t, five_anchor=t, five_pct=a.five, five_reset=parse_local(a.five_reset),
                 week_anchor=t, week_pct=a.week, week_reset=parse_local(a.week_reset))
        meter_update(t - 6 * 3600)
        save_state(s)
        print('calibrated:', report(s, estimate(s, load_cache()['buckets'])))
        return 0
    def current():
        """(five, week, five_reset, week_reset, source, line) for the logged-in account."""
        P, i = app_profiles()
        if P is not None and i is not None and P[i]['updated'] and now() - P[i]['updated'] <= STALE_S and P[i]['five'] is not None:
            q = P[i]
            five = q['five'] if not (q['five_reset'] and now() >= q['five_reset']) else 0.0
            return five, q['week'], q['five_reset'], q['week_reset'], 'app', app_line(q, '[app] ')
        s = load_state()
        if not s:
            return None, None, None, None, 'none', 'no fresh app data and not calibrated'
        e = estimate(s, meter_update(min(s['five_anchor'], s['week_anchor']) - 60))
        return e['five'], e['week'], e['five_reset'], e['week_reset'], 'estimate', '[estimate] ' + report(s, e)

    if a.cmd == 'status':
        P, i = app_profiles()
        if P:
            for j, q in enumerate(P): print(app_line(q, '* ' if j == i else '  '))
        print('current:', current()[5]); return 0
    while True:
        five, week, r5, rw, src, line = current()
        log(f"{fmt(now())}\t{src}\t{line}")
        if src == 'none':
            print('NO DATA:', line); return 12
        if a.cmd == 'watch':
            if week >= a.week_max:
                print('PAUSE (weekly):', line); return 10
            if five >= a.five_max:
                print('PAUSE (5-hour):', line); return 10
        else:  # wait
            if week >= a.week_max:
                P, i = app_profiles()
                others = '; '.join(app_line(q) for j, q in enumerate(P or []) if j != i)
                print('WEEKLY LIMIT —', line, '| other accounts:', others); return 20
            if five < min(10.0, a.five_max):
                print('RESUME:', line); return 0
        time.sleep(a.interval)

if __name__ == '__main__':
    sys.exit(main())
