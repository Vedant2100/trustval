# AGENT 2027 TrustVal short-paper drafting plan

**Status:** manuscript development plan, 2026-11-17. **NOT** a submission or a claim that a publication is accepted. No new experiment authorized by this document. Work only in `Vedant2100/trustval`; do not edit the frozen `research-master-` copy.

## 1. Target and hard submission rules

Official conference: [AGENT 2027, 2nd International Workshop on Agentic Engineering (ICSE 2027)](https://conf.researchr.org/home/icse-2027/agent-2027).

- **Category:** Short **benchmark/tool/empirical** paper, not a full 8-page research paper.
- **Length:** maximum **5 IEEE-formatted pages, references included**; no paid extra pages. Do not count references as an extra page.
- **Template:** IEEE conference proceedings, `\documentclass[10pt,conference]{IEEEtran}`; no `compsoc` or `compsocconf` option. Use actual two-column pagination, not a word-count approximation.
- **Review:** single-anonymous, not double-anonymous. Do not falsely assert anonymization is required. The paper provisionally names Vedant D. Borkute (University of California, Riverside); final author list and affiliation still require owner approval.
- **Publication:** accepted papers published by IEEE; treat later archival overlap and dual submission seriously.
- **Deadline:** **2026-11-20, 23:59 AoE (UTC-12)**, which is **2026-11-21, 03:59 PST**. [Submission portal](https://icse2027-agent.hotcrp.com/). Acceptance notification Dec 11, 2026; camera-ready Jan 29, 2027. No submission is attempted by this plan.
- **Scope:** engineering, testing, benchmarking, tool-use reliability, operational recoverability. Avoid treating generic financial automation or "AI safety" as the contribution.

## 2. Honest thesis and originality gate

**Working title:** *TrustVal: An Engineering Case Study of Agent Recovery After Ambiguous Writes*.

**Thesis:** The result of a tool invocation is not the same as its durable side effects. TrustVal is a compact, executable four-task regression benchmark that grades database effects rather than fluent reports. Its design history demonstrates how outcome-revealing errors and server-side deduplication can make unsafe retry strategies look correct. On a revised version with ordinary errors and non-idempotent writes, some evaluated older models duplicate effects while newer evaluated models mostly reconcile the state. A separate delayed-visibility variant shows the present test's limits.

**This is not a newly discovered failure mode. A serious prior-art challenge exists.**

- [LIMBO / *Where Does Exactly-Once Live?*](https://arxiv.org/abs/2609.29095), posted **2026-09-24**, studies six services, twelve faults, 25,930 episodes, multiple harnesses and exactly-once tool contracts. It already reports frontier verification on resolvable faults, failures on late commit/redelivery, and differences between model, harness and server-side contract. **Do not claim TrustVal first introduced ambiguous-commit duplicate effects, state-ledger grading, contract effects, or cross-harness evaluation.**
- [UndoBench](https://arxiv.org/abs/2610.05622), posted **2026-10-04**, studies paired nominal/fault recovery across enterprise tasks and dual-oracle grading. Do not claim the first separation of nominal competence and recovery.
- [Evidence-Guided Recovery](https://arxiv.org/abs/2610.41453), posted **2026-10-30**, studies capability-aware recovery and partial execution. Do not claim novel recovery theory or compensating protocol.
- Earlier stateful-tool evaluations include [ToolSandbox](https://aclanthology.org/2025.findings-naacl.65/) and [tau-bench](https://arxiv.org/abs/2406.12045).

**Proposed distinct value:** a small, runnable **Harbor/Valkyrie agent benchmark** with explicit private sidecar state, independent final-state verifier, trace-linked failure classification, documented **v2 -> v3 -> v4 construct-validity corrections**, model comparisons within the same harness, and an explicit negative conclusion (current models saturate the instrument). This is a reproducible **engineering case study and regression instrument**, not a comprehensive generalization of exactly-once reasoning.

**Go/no-go before submission:** A reviewer must be able to answer, using 5 pages, why a *four-scenario benchmark design case study* contributes anything beyond LIMBO/UndoBench. If we cannot make that difference concrete, do **not** submit generic "agent retries can duplicate" results merely to hit the deadline. Assess whether design-time leakage + implementation lesson + trace audit constitutes a legitimate short benchmark contribution, or if the work is better released as a technical report with no archival claim.

## 3. Exactly what we built and ran

**Artifact:** four synthetic operational tasks (`commit_timeout`, `stale_read`, `partial_batch`, `duplicate_delivery`) backed by an isolated SQLite sidecar, API help and narrow CLI, terminal agents in separate containers, and hidden verifier grading recovered durable state. Commands and the final answer do not set the grade. A client `reference` can be looked up but does not itself make writes idempotent.

**Revision history, no fake causal ablation:**
- v2: one run/task/model with Haiku 4.5 and Sonnet 4.6; both **4/4**. This benchmark version leaked committed outcomes in error strings and included server-side deduplication. It did **not** demonstrate robust recovery. Multiple variables changed together between v2/v3; do **not** infer one change's isolated causal effect.
- v3: documented `DESIGN_V3.md` before model trials. Neutral 502/504 responses, non-idempotent writes, authoritative reads, no fault-specific hints in task prompt, partial-batch single-item completion, hidden final-state grading. Naive retry policy fails all four, careful reference passes all four; hosted oracle **4/4**. Ten repeated four-task runs per model for seven models, plus three GPT-6-family pilot models one run each.
- v3 main per-model outcomes: Haiku 4.5 **19/40**, Sonnet 4.6 **35/40**, Haiku 5.5 **39/40**, Sonnet 5.5 **40/40**, Opus 5.5 **40/40**, GPT-5.3-Codex **34/40**, GPT-5.4 **40/40**. Each task is repeated, not 40 different tasks. GPT-6 Astra, GPT-6.1 Sol/Terra each **4/4 once**, too few for strong comparative inference.
- v3 within-Claude-harness comparison: per-run two-sided exact permutation p ~ **2.3e-4** for 4.5 Haiku vs 4.6 Sonnet; per-run score is the independent resampling unit, but the **four fixed scenarios** do not support a population-wide claim. Audit numeric p from `results/summary_v3.json` and `scripts/aggregate.py` before finalizing paper.
- All **26 Claude 4.x failures** were duplicate effects after blind retries. Haiku 4.5 failed 21/40, Sonnet 4.6 failed 5/40. False *final success* claims in **4/21** Haiku and **4/5** Sonnet failure cases. GPT-5.3-Codex's six failures were likewise blind retries. Some failures were noticed and disclosed by the agent: avoid saying every failed agent falsely claimed success.
- Different harnesses: Claude via `claude_code-v1.0.0`; GPT-5.x via `codex-v1.0.0`; GPT-6 via minimally allowlist-extended Codex harness; GPT agent API egress enabled in `@v3.1`. **Do not attribute cross-provider differences solely to models.** Same-harness comparisons are stronger.
- v4: independently documented `DESIGN_V4.md` before the hard-split runs. Add **30 s hidden write visibility** and disclose an up-to-60 s visibility delay; hosted oracle **4/4**, local careful and naive controls separate. Three 4-task runs per tested model: Haiku 5.5 **11/12**, Sonnet 5.5 **12/12**, GPT-6.1 Terra **12/12**. The single Haiku failure involved a long-sleep harness interaction. v4 is largely saturated; three repeats are **not** powered to estimate subtle differences.
- Root/Compose setup failures in `RESULTS.md` were infrastructure, **not model trials**. Regrade of saved databases agrees with hosted scores; record actual sample sizes and failure definitions.
- Each case is a **variant of the same capability**, not four independent research contributions. The stale-read v3 task had no error and all models passed; the reference solution for partial batch uses per-item operations and bypasses the batch fault, whereas evaluated agents invoked the batch endpoint. Disclose both explicitly.
- There is no real bank, no rollback API, no live operations outcome, no model training, and no learning-from-experience experiment.

## 4. Paper outline and page budget (all pages include references)

| Section | Budget | Essential content |
|---|---:|---|
| Abstract + Introduction | 0.65 page | concrete lost-ack example, narrow thesis, scope and 2 RQs; do not market new problem |
| Related work and novelty boundary | 0.50 page | explicit LIMBO/UndoBench comparison; what is reused vs incremental |
| Benchmark design/construct validity | 1.05 pages | four fault tasks, sidecar and verifier, version history, naive/careful controls, grading definition |
| Experimental protocol | 0.50 page | Valkyrie/Harbor, actual models/harnesses, n=10 vs n=1, datasets and independent runs |
| Results + trace diagnosis | 1.00 page | source-generated 7-model v3 table, exact 26 failures, 4/5 false reports, v2 and v4 qualifications |
| Threats, implications, conclusion | 0.55 page | synthetic fixed scenarios, ceiling, sample size, harness confounds, no general claims |
| References | >=0.75 page | full verified bibliographic data; counted within 5 |

Page budgets are **targets**, not a license to shrink to unreadable type or violate IEEE margins. Trade off prose and tables after compiling the actual IEEE PDF. If references consume more room, cut claims/text, not citations.

**Research questions:**
- **RQ1:** Which properties of an execution benchmark make a recovery failure observable to the evaluator, and what did the v2 -> v3 redesign reveal in the saved trajectories?
- **RQ2:** Under fixed v3 tasks, which unsafe retries and failure reports do the evaluated agents produce, and where do v3/v4 cease to distinguish systems?

Do **not** ask whether v3/v4 proves modern models generally safe. It does not.

## 5. FrontierMemory paper workflow to reuse, with safeguards

1. **Freeze evidence first:** a claim-to-source ledger with exact run IDs, task version, sidecar state, controls, model labels, stats and a separate infrastructure-failures bucket. Verify `RESULTS.md` against `results/summary_v3.json`, `results/summary_v4.json`, `scripts/aggregate.py`, `DESIGN_V3.md` and `DESIGN_V4.md`. For selected anecdotes independently inspect trace and final database, not just the summary.
2. **Write contribution thesis before polished prose:** begin from "what exactly is the new, publishable artifact" and the specific comparator to LIMBO and UndoBench. Treat results as evidence, not a promotional story. If the originality test fails, keep a technical report and do not submit an archival duplicate.
3. **Draft with definitions at first use:** define ambiguous outcome, commit/acknowledgement, state reconciliation, exactly-once effects *in this benchmark*, sidecar, reference solution, naive retry and false success report. Separate observations from likely mechanisms and from infrastructure artefacts.
4. **Generate quantitative tables from `results/summary_v3.json`** using the checked `build_tables.py` helper; never hand-edit counts in LaTeX. Each figure/table has model, dataset version, harness, denominator, caption, and source pointer. No mixed v3/v4 denominator or exploratory one-run models pooled with n=10 models.
5. **Academic voice, independently reviewed:** normal research-paper prose. No abstract-as-inventory, promotional adjectives, unsupported causal language, generic "robustness" claims, AI-sounding transition filler, or authored em/en dashes. No unsupported source citations. Preserve natural readable explanations as in the final FrontierMemory paper, while keeping precise limitations.
6. **No unseen edits or self-certification:** review the full Markdown/TeX diff against the original evidence ledger; verify nomenclature, p-values, partial-batch reference exception, versions, false-success counts and quotes. Fix editorial errors in follow-up PRs instead of hiding changes inside sweeping rewrites.
7. **Actual PDF acceptance check:** compile IEEEtran from a clean environment with BibTeX; verify citations resolve, exactly <=5 pages INCLUDING references, figure/table legibility, no overflow, no orphaned bibliography, no TODOs or unsupported statements. Inspect every rendered PDF page, not CI alone. If build tools unavailable or compilation not performed, explicitly mark the submission not ready.
8. **Final submission gate:** check author names, funding/AI-use declaration if required by applicable publisher/conference policies, conflicts, HotCRP PDF, originality and no simultaneous archival submission; archive confirmation receipt. Do not upload/submit without owner approval.

## 6. Schedule (all times Pacific; relative to Nov 20 AoE)

- **Nov 17:** Plan and readable initial LaTeX draft on isolated branch. Explicit LIMBO/UndoBench novelty assessment, claim-to-source map. No auto-merge.
- **Nov 18:** Independently inspect selected trace/SQLite samples and source-generated table. Draft substantive methods, results, comparison and limitations. Remove every unsupported line.
- **Nov 19:** Full independent editor pass, reconcile results, citations and section-level argument; compile and visually inspect PDF. Target all scientific work completed, not a last-minute new experiment.
- **Nov 20:** Venue-format and 5-page verification, human approval of authorship, overlap/receipt and submission metadata. Submit manually through official HotCRP only if originality and quality gates pass. Exact AoE expiry corresponds to **Nov 21, 03:59 PST**.

## 7. Definition of done

- [ ] LIMBO / UndoBench / Evidence-Guided Recovery / relevant benchmark comparison is accurate and materially differentiated.
- [ ] Manuscript meets short benchmark-paper scope; no invented improvements, task families or novelty.
- [ ] Results are strictly trace- and state-grounded; counts, denominators and p-values independently verified.
- [ ] Main v3 experiment, version leakage audit and v4 ceiling all represented, including negative results.
- [ ] All limitations are explicit: 4 fixed scenarios, v2/v3 multiple changes, v3 stale-read ceiling, partial-batch oracle bypass, distinct harnesses, small v4, public task contamination possibility.
- [ ] IEEEtran compile succeeds; <=5 pages **including references**; rendered PDF reviewed page by page.
- [ ] No unanswered TODO, stale claims, accidental private data, unverifiable references or AI-like boilerplate.
- [ ] Owner reviews paper and explicitly authorizes any external submission. Store submission receipt if submitted.


## November 17 manuscript maturity update

- **Revised IEEE PDF:** 4 pages **including references**, exact GitHub compile-input files SHA-verified against the successful local pdfLaTeX/BibTeX build and visually checked on every page. Source and complete build report: [BUILD_REPORT.md](BUILD_REPORT.md).
- **Primary score re-audit:** all 20 saved Claude v3 per-run regrades checked; 21 Haiku + 5 Sonnet failures, each with `exactly_once=0`. Main table directly compared against seven models' `results/summary_v3.json` rows; exact run-level permutation p = 42/184756.
- **Newly audited primary limitation:** all injected v3 transport errors occur after a full or partial commit. No observationally matched uncommitted timeout is tested; a 'never retry' policy could pass some single-write tasks. This is stated prominently under Threats to Validity.
- **Wider direct prior art:** added Verified Tool Calls (arXiv:2608.02645), AFT-Bench (2608.23628), and AgentFaultBench (2611.20711, posted Nov 16) alongside LIMBO and UndoBench. The manuscript no longer contains internal editorial commentary about whether reviewers should accept the work.
- **Author:** provisional Vedant D. Borkute / University of California, Riverside; confirm any coauthors before submission.
- **Conclusion:** best current-evidence *short benchmark/engineering experience* draft, with credible but modest incremental novelty. No new model experiments, no external conference submission, no acceptance implied. User approval and double-submission check remain prerequisites for an official submission.
