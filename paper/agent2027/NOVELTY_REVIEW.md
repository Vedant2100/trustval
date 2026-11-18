# AGENT 2027 originality review: TrustVal against close prior work

**Date:** 2026-11-17. Read **full public HTML versions** of [LIMBO](https://arxiv.org/abs/2609.29095), [UndoBench](https://arxiv.org/abs/2610.05622), and [Evidence-Guided Recovery](https://arxiv.org/abs/2610.41453), not just secondary summaries. This is a gate for *archival* submission, not a rubber stamp. An AGENT short benchmark/tool/experience paper is allowed, but it must still be original.

## Closest overlap

| Dimension | TrustVal | [LIMBO, Sep 2026](https://arxiv.org/abs/2609.29095) | [UndoBench, Oct 2026](https://arxiv.org/abs/2610.05622) | Implication |
|---|---|---|---|---|
| Ambiguous write acknowledgment, retry duplicates | Four synthetic stateful operational tasks; three v3 error-injection tasks plus v3 stale read | **Already investigates this problem** across six services and twelve fault modes including late commits, redelivery, partial batches | Lost-acknowledgment and partial mutation among multiple execution phases | **No novelty claim possible** for problem or duplicate-retry observation. |
| State-based evaluation | SQLite sidecar, hidden verifier of final effects and no duplicates | Ledger of committed effects, with stricter effect-history reasoning and counterfactual contracts | Wire-level effect history and state oracles, paired controls | **Not the first** state/effect-based grading; the isolated agent/sidecar implementation is a reproducible artifact detail. |
| Experimental breadth | Four fixed scenarios, 10 repeated runs per seven models; three 1-run GPT-6 probes | 25,930 episodes, nine models, three production harnesses, two contract variants and 15 recovery conditions | 36 base workflows + 36 fault cases across 8 domains; 5,760 confirmatory executions | TrustVal is considerably **narrower**. Do not advertise it as comprehensive or frontier-separating. |
| Model/harness separation | Claude Code vs Codex; cross-provider comparisons confounded | Crosses models over shared harness/tool contracts and explicitly studies harness effects | Multiple frameworks and models with pairing | No novel cross-harness factorization in TrustVal. |
| Fault visibility / bounded waits | v4 30 s hidden commit after fault and help states visibility up to 60 s | Eventually consistent/missing read paths; in-flight late commits; documented bounds and wait policies studied | Fault boundaries explicitly separated | v4 is **not a new fault class** or a solution. One failure tied to harness wait handling. |
| Benchmark *instrument* failure and repair | v2 revealed outcomes and deduplicated writes; v3 changed contract, hints and task behavior. Explicit naive/control check validates ability to distinguish recovery. | Provides extensive benchmark-validity analyses and tool contract manipulations; includes documentation/rules variants | Prospective paired oracles and audit checks | Version-history case study may offer **practical engineering lessons** but is **not a controlled ablation**; multiple changes together. |
| Final answer accuracy | False completion in 4/5 Sonnet 4.6 failed v3 trials, independent DB grade | Reports success in 90% of its duplicate episodes | Recovery correctness focuses on state and effect histories | Not a new type of failure, but a directly traceable result for this *particular* realistic CLI harness. |
| Reproducibility format | Native Harbor/Valkyrie task spec, Compose sidecar and stored full Claude/Codex traces with regrader | Deterministic simulation + public benchmark tooling (inspect artifact license/execution before claiming superior reproducibility) | Open benchmark components, paired-run audit | This is the **strongest plausible specific AGENT engineering artifact**, if packaging is genuinely easy to reuse and comparisons are honest. |

[Evidence-Guided Recovery](https://arxiv.org/abs/2610.41453) further covers partial execution, admissible actions, evidence-supported planning, and independent replay. TrustVal does not develop an algorithm or solve the unknown-outcome decision problem.

## Independent assessment

**Most likely AGENT contribution:** an empirical **benchmark-engineering experience / tool short paper**. Narrative:

> A four-task, real terminal-agent evaluation can appear to validate safe recovery even when the fault text leaks the answer and the server masks incorrect retries. Inspecting traces led to revised task semantics and a hidden state verifier; those changes exposed specific unsafe retries in some evaluated agents. Applying the same evaluation to newer agents demonstrated near-ceiling behavior, making it a useful limited regression test rather than a broad safety verdict.

This is supported by actual results, but **incremental scientific novelty is modest**. The distinction from LIMBO and UndoBench must be practical and explicit (Valkyrie/Harbor interoperability, locally verifiable artifact, transparent engineering iteration), not a scale or security claim. Avoid calling the study a controlled assessment of which single factor mattered: the v2 -> v3 redesign changed several simultaneously.

### What would strengthen a paper without large new experiments?

1. Add a **reproducibility matrix** from the actual artifact: v2 outcome-revealing and dedup; v3 neutral errors, non-idempotent writes and exposed API reads; v4 delayed reads. Document oracle and naive controls *per version*, including the partial_batch oracle bypass.
2. Add **two trace-level comparative examples**: blind retry after a 504 (failed), and state query after the same 504 (passed). They distinguish model behavior more effectively than a model ranking. Cite exact run IDs and independently checked `regrade.json`.
3. Publicly document the **build/portability boundary**: agent allowed network access, sidecar isolation, saved artifact regrade, which task files were actually exercised. This should provide engineering value beyond a restatement of the failure class.
4. **Do not** add unvalidated complexity or chase failures in newer models to inflate novelty. The instrument's ceiling is itself an important limitation.

### Go/no-go recommendation

Proceed with **drafting and peer review**, but do **not promise AGENT submission solely because the deadline is close**. I would require a skeptical reader to name at least one transferable new engineering lesson, supported by code and traces, that is **not already demonstrated in LIMBO**. If that cannot be articulated in the final intro/contributions, release a standalone technical report rather than an archival short paper. The current draft has a plausible *artifact report*, but not yet a convincingly original *research finding*.

**Do not merge TrustVal with ContagionBench/ProvenanceTrap** to disguise this issue: their threat models and evidence are different.
