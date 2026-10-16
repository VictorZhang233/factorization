# Usage guard — policy and procedure (user requirement 2026-10-14)

Policy (binding unless the user explicitly says the quota may be used up now): 5-hour window ≤ 80 %, weekly ≤ 70 %.
Completed work must never be lost (cache + persisted results; interrupted agents continue from their files).

## Primary source (2026-10-14): the user's "Claude Usage" menu-bar app
`writing/tools/usage_guard.py` reads the official per-account numbers that the app (bundle HamedElfayome.Claude-Usage)
keeps in its preferences (`defaults export`): 5-hour %, reset time, weekly % (max of all-model and Opus weekly), reset
time, last update. The profile is matched to the account Claude Code is logged in with. Credentials stored by the app
are never printed or used. `usage_guard.py status` prints all profiles. Thresholds: pause at 5h ≥ 77 %, week ≥ 69 %
(polling every 60 s; the app refreshes about every minute). The token estimate below is only the fallback when the
app data are older than 10 minutes.

## Fallback: why estimates
Claude Code shows the percentages only to the user (/usage); this session cannot read them. A status-line based capture
was attempted and blocked by a safety check — do not modify Claude Code's settings. The guard therefore estimates
usage from the local transcripts (writing/tools/usage_guard.py), anchored to the numbers the user reads from /usage.

Calibration (cost-weighted tokens w = input + 1.25·cache_write + 0.1·cache_read + 5·output):
- 5-hour window ≈ 271 M (account gaogaogao960, 2026-10-14 16:00 → limit at 17:43); cross-check: account xszhang2003
  used 218 M from 21:00 to 22:05 when the user said the window was almost used up (≈80 %). K5 = 2.71 M per %.
- week ≈ 813 M (previous account, 2026-10-10 04:00 → weekly limit 2026-10-11 13:05). KW = 8.13 M per %.
- Thresholds with margin for estimation error: pause at 5h ≈ 75 %, week ≈ 66 %.

## Procedure
1. Before any launch/resume: `usage_guard.py status` (app data). Only if the app is unavailable: ask the user for the /usage numbers and run
   `python3 -I writing/tools/usage_guard.py calibrate --five P --five-reset 'YYYY-MM-DD HH:MM' --week P --week-reset 'YYYY-MM-DD HH:MM' --account NAME`
   (re-calibrate after every account switch).
2. Start the watcher in the background: `python3 -I writing/tools/usage_guard.py watch` (exit 10 = pause now).
3. On exit 10: `python3 -I writing/tools/run_state.py` (RESUME_PLAN.json + persisted results), TaskStop every active run,
   then start `python3 -I writing/tools/usage_guard.py wait` in the background; tell the user.
4. On wait exit 0 (new 5-hour window): run_state.py again, resume every entry of RESUME_PLAN.json (Workflow with
   scriptPath, resumeFromRunId, args), append the new run IDs to writing/state/active_runs.json, restart the watcher.
   On exit 20 (weekly): stop; tell the user (wait for the weekly reset or a login to another account).
5. The guard needs this Claude Code session to stay open.
