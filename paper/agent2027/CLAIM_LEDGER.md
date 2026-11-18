# TrustVal AGENT 2027 claim-to-evidence ledger

**Draft review tool.** Every numerical or causal statement in `main.tex` must have a primary source, correct denominator and explicit status. Source repository is the canonical [TrustVal](https://github.com/Vedant2100/trustval), not the frozen master copy. Current branch includes drafts only, not new experiments.

| Intended claim | Direct evidence | Qualifications / reviewer check |
|---|---|---|
| Four API-backed tasks with isolated durable SQLite state and hidden verifier | [README task description](../../README.md), `tasks/*/task.toml`, `tasks/*/tests/test.sh` / sidecar implementation, `scripts/compose_smoke_test.sh` | Inspect actual image/Compose network isolation and verifier read paths. Agent root in its container is not root in sidecar. Model answers do not establish state success. |
| v2 Haiku 4.5 and Sonnet 4.6 passed 4/4 | [RESULTS.md v2](../../RESULTS.md) and two specific run IDs `998e9992-83cc-4927-8145-61d651f9feda`, `8ff83c9b-5e90-4363-be60-7c211e69a2c9` | One run per task per model. v2 committed-outcome disclosure plus server-side dedup. Not robustness evidence. |
| v3 removed leaks and enabled duplicate writes | [DESIGN_V3.md](../../DESIGN_V3.md) and source code diff between dataset `@2` and `@3` | **Many changes at once**: error wording, API semantics, task hints, stale read, batch command. Do not call a single-factor causal ablation. |
| v3 controls show careful success vs blind-retry failure | [DESIGN_V3.md controls](../../DESIGN_V3.md), `scripts/compose_smoke_test.sh`, hosted oracle run `1217913d-e1cb-401e-878c-705dda7093b8` | Reference `partial_batch` solution uses single-item reserve and avoids its batch fault; record this limitation. |
| v3 task successes for seven models (ten runs each) | [RESULTS.md](../../RESULTS.md), `results/summary_v3.json`, regraded `results/*-v3-*/regrade.json` | Primary `tables/v3-primary.tex` is generated from summary JSON. Fixed **four** tasks × repeated ten runs, not forty distinct tasks. Dataset `@v3.1` adds API allowlist for Codex. |
| Haiku 4.5 19/40 vs Sonnet 4.6 35/40; per-run mean gap 1.6 | `results/summary_v3.json` and `scripts/aggregate.py` | Independent check of exact two-sided run-score permutation: 42 extreme partitions / 184,756 total = **0.00022732685**. Test samples runs on the same 4 tasks; do not extrapolate to task populations. Both same Claude Code harness. |
| All 26 Claude 4.x failed v3 task-trials involved blind retry/duplicates | [RESULTS.md manual classification](../../RESULTS.md), trace directories listed therein | Check at least one raw trajectory and final DB for each mechanism, and sample false-report examples. Models: Haiku 21 failures, Sonnet 5. |
| False final-success reports: Haiku 4/21, Sonnet 4/5 failures | [RESULTS.md failure-report classification](../../RESULTS.md) | Counts conditional on FAILED trials. 17/21 Haiku failures mention duplicate, 1/5 Sonnet mentions duplicate. Report "claimed completion" separately from "noticed/reporting mistake." |
| GPT-5.3-Codex 34/40; GPT-5.4 40/40 | [RESULTS.md OpenAI runs](../../RESULTS.md) and summary JSON | Different Codex harness from Claude; cannot infer provider-independent model ranking. Six GPT-5.3 failures were duplicate retries. |
| Claude Haiku/Sonnet/Opus 5.5 39/40, 40/40, 40/40 | [RESULTS.md](../../RESULTS.md) and `results/summary_v3.json` | One Haiku 5.5 failure is swapped argument order, fault did not fire. No 5.5-to-5.5 discriminative conclusion. |
| GPT-6 Astra/6.1 Sol/6.1 Terra each 4/4 | [RESULTS.md](../../RESULTS.md) | **Only one four-task run per model.** Do not pool or call significant. Harness allowlist extended with names only. |
| v4 delayed-visibility experiment and controls | [DESIGN_V4.md](../../DESIGN_V4.md), `results/summary_v4.json` | 30-second hidden write, help text allows up to 60 seconds. Reference solution and hosted oracle 4/4; check-once policy 0/4. Not a v3 matched-sample comparison. |
| v4 Haiku 5.5 11/12, Sonnet 5.5 12/12, GPT-6.1 Terra 12/12 | [RESULTS.md v4](../../RESULTS.md), `results/summary_v4.json` | Three runs each, ceiling. One Haiku mistake involved background sleep after CLI restriction; do not infer general model flaw. |
| Infrastructure failed on earlier datasets before the model ran | [RESULTS.md infrastructure attempts](../../RESULTS.md) | Modal VM configuration and agent permissions. Exclude from scored model denominator. |
| Benchmark is a focused regression test, not new exactly-once theory | [LIMBO](https://arxiv.org/abs/2609.29095), [UndoBench](https://arxiv.org/abs/2610.05622), [Evidence-Guided Recovery](https://arxiv.org/abs/2610.41453) | High novelty overlap. Independent prior-art review required before deciding AGENT archival submission. |

## Audit sequence

1. Re-run the repo's `scripts/aggregate.py v3` against saved per-run `regrade.json` and `results.json`; regenerate `tables/v3-primary.tex`. Inspect full `git diff` if any tracked number changes.
2. Independently inspect archived traces and DB files for representative `commit_timeout`, `partial_batch`, `duplicate_delivery`, v4 wait interaction and one verified passing recovery.
3. Verify `DESIGN_V3.md` and `DESIGN_V4.md` predate corresponding evaluations, rather than calling post hoc changes preregistered without evidence.
4. Line-edit the paper's method and related-work statements against source and full-text prior work, not abstracts alone.
5. Compile and visually inspect IEEE PDF, cross-check counts, and require owner approval before archival submission.

**Progress as of Nov 17:** Original trajectories, final messages, and saved regrades for multiple failed and passing v3/v4 examples independently spot-checked; see [TRACE_AUDIT.md](TRACE_AUDIT.md). Full-text prior-work comparison recorded in [NOVELTY_REVIEW.md](NOVELTY_REVIEW.md). A mirrored IEEE source compiled as 3 pages and every rendered page was inspected; see [BUILD_REPORT.md](BUILD_REPORT.md). Still open: direct independent inspection of binary SQLite snapshots (not retrievable via linked GitHub file content), exact PR-head fresh-clone build and source-generator rerun, independent manuscript novelty review, and author approval. **Not submission-ready.**

## Additional independent score audit (2026-11-17)

Read all **20 saved v3 `regrade.json` files** for Claude Haiku 4.5 (10 runs) and Claude Sonnet 4.6 (10 runs) directly from the canonical repository and compared their task-success fields with the pinned `results/summary_v3.json`.

- **Haiku 4.5:** 21 failed task-trials, each with `exactly_once=0`; failure breakdown by scenario: commit timeout **4**, partial batch **7**, duplicate delivery **10**, stale read **0**.
- **Sonnet 4.6:** 5 failed task-trials, each with `exactly_once=0`; failure breakdown: commit timeout **0**, partial batch **3**, duplicate delivery **2**, stale read **0**.
- **Total:** 26 failed out of 80 repeated task-trials; all 26 saved verifiers identify an exactly-once violation. This directly checks the score-level and duplication consequences. Attribution to an agent's `blind retry` action still rests on the trajectory classification in `RESULTS.md`, supported by representative independent raw-trace checks described in `TRACE_AUDIT.md`. This is **not** a reread of all 80 trajectories or of all binary SQLite exports.

**New central limitation after further prior-work review:** all injected v3 transport errors follow a committed (or partially committed) operation. No matched, indistinguishable *uncommitted* timeout is included; never present success as verified mastery of the full uncertainty problem. In particular, no-retry can succeed on the single-write commit cases. Existing LIMBO, UndoBench, AFT-Bench, Verified Tool Calls and newly posted AgentFaultBench directly investigate neighboring or stronger designs; the paper focuses on an honest engineering case study.
