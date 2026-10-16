# RESUME — how to continue after the pause of 2026-10-14 (≈22:00 EDT)

All workflows and agents were stopped **deliberately** (user request: pause before the 5-hour limit). Nothing is lost:
completed agents are cached in their workflow runs and persisted as files; in-flight agents left their partial
outputs on disk, and on resume they get a RESUMPTION NOTE telling them to continue from those outputs.

## 1. State at the pause (`writing/state/RUN_STATE_20261014.json`)

| run | script | content | done | in flight (will resume with the note) |
|---|---|---|---|---|
| wf_1b1b7a35-b6e | factorization-writing | group A | W03-write, W06-write | W04, W05, W09, W13, W16, W22 writers (W02 → group R) |
| wf_3924630b-621 | factorization-writing | group B | X1-glauber-final2, X3-ope-final2, W10-write, W12-write, W14-write | X2-subtraction-final2, X1/X3-confirm2, W17, W21 writers (W07 → group R); then spec sync v2.4, figure sync, W08/W11/W15 |
| wf_2e53ffea-c6f | factorization-writing | group C | W26-write | W18, W19, W20, W23, W24, W25 writers (W27 → group R) |
| wf_e30388b7-c05 | factorization-writing | group R | — | W02, W07, W27 writers |
| wf_6971bc3e-f8c | factorization-deep-research | X4 non-abelian Glauber | — | X4 survey |
| wf_7c986a86-ad7 | factorization-proof-completion | triage T1–T5 + proofs | — | triage T1–T5 |
| wf_f2b311b2-bad | factorization-proof-completion | triage T6–T10 + proofs | — | triage T6–T10 |

Units already drafted on disk (`chapters/`): Ch3–Ch6, Ch8–Ch10, Ch12, Ch15, Ch16, Ch20–Ch23, App A–F, I, K, L,
`part7_preface.tex` (several still being completed by their writers). Persisted results of completed agents:
`writing/state/results/<run>/<label>.md`. Final2 reports: `verify/extend_reports/X1-glauber_final2.md`, `X2-…_final2.md`
(partial, being completed), `X3-ope_final2.md`. Tooling: `writing/tools/*.py`, `build/build.sh`, tests in `build/`.

## 2. Resume procedure (automated: `python3 -I writing/tools/run_state.py` writes RESUME_PLAN.json from
`writing/state/active_runs.json`; usage guard: see GUARD.md — calibrate with the user's /usage numbers first)

### Manual details (scripts already patched: `args.resume`, `args.done`, `args.skip`)

Scripts (session dir `/Users/hao-cheng/.claude/projects/-Users-hao-cheng-Desktop-theorem-proof-qcd-factorization-work/c211c739-758d-4b40-bbac-67f4e1a65da4/workflows/scripts/`):
`factorization-writing-wf_55541c51-5f2.js`, `factorization-deep-research-wf_6971bc3e-f8c.js`, `factorization-proof-completion-wf_7c986a86-ad7.js`.

Mechanism: with `resume: true`, every agent whose label is **not** in `done` gets the RESUMPTION NOTE appended (continue
from partial outputs); agents in `done` keep byte-identical prompts, so `resumeFromRunId` replays their cached results.
`skip` removes units from a writing group (W02/W07/W27 are handled by group R — never run them twice).

1. Recompute `done` from the journals (in case anything finished after the snapshot) — same code as used for
   RUN_STATE (labels with a `result` event).
2. Launch (Workflow tool, `scriptPath` + `resumeFromRunId`):
   - group A: `{"group":"A","resume":true,"skip":["W02"],"done":["W03-write","W06-write"]}`, resumeFromRunId `wf_1b1b7a35-b6e`
   - group B: `{"group":"B","resume":true,"skip":["W07"],"done":["X3-ope-final2","W14-write","X1-glauber-final2","W12-write","W10-write"]}`, resumeFromRunId `wf_3924630b-621`
   - group C: `{"group":"C","resume":true,"skip":["W27"],"done":["W26-write"]}`, resumeFromRunId `wf_2e53ffea-c6f`
   - group R: `{"group":"R","resume":true,"done":[]}`, resumeFromRunId `wf_e30388b7-c05`
   - X4: contents of `args_x4.json` plus `"resume":true,"done":[]`, resumeFromRunId `wf_6971bc3e-f8c`
   - proofs P1: `args_proof_P1.json` plus `"resume":true,"done":[]`, resumeFromRunId `wf_7c986a86-ad7`
   - proofs P2: `args_proof_P2.json` plus `"resume":true,"done":[]`, resumeFromRunId `wf_f2b311b2-bad`
3. Tooling: start a new agent ("integration-tooling continuation") — previous progress notes are in the conversation
   handover (all six tools built; synthetic suite 133/133; partial build exit 0; remaining: App P overfull boxes, ε glyph in
   appP_register, fresh partial build + renders).
4. After each resume the run IDs change: update this file and PROGRESS.md with the new run IDs and a new RUN_STATE.

## 3. If a cache is ever lost

Re-launch the same script without `resumeFromRunId`, with `resume: true` and `done: []`: then EVERY agent gets the
RESUMPTION NOTE, so agents whose work is already complete on disk only audit it and finish quickly instead of redoing it.
The structured results of completed agents are also in `writing/state/results/<run>/<label>.md`.
