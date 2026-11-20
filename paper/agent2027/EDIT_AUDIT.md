# Paper-writing skill pass — terminology, evidence and Overleaf checks

Date: 2026-11-18. Base: merged PR #1, commit `23972f3`. This branch changes manuscript wording, links and layout only. It does not change benchmark tasks, model runs, grading rules or publication status.

## Editorial changes

- Open with the recorded payment example: one agent repeated a payment without checking; another checked the saved record first.
- Consolidate the version-2/version-3 design explanation and retain the warning that several features changed together.
- Keep the main result table beside Results and add the two-run payment comparison.
- Replace abstract shorthand with descriptions of the actual action and saved database result.
- Keep general technical terms (API, HTTP, SQLite, idempotency) undefined in the paper, as expected by an agent-systems audience; plain-language explanations live in [README.md](README.md).
- Keep links only to Harbor and to TrustVal's own evidence (design notes, control script, reference solution, trace audit, recorded traces), pinned to commit `fbba895` so they cannot drift after submission. A footnote gives the repository URL for print readers, since `hidelinks` makes in-text links invisible on paper.
- Use "exactly-once requirement" (the `exactly_once` verifier field) instead of "one-effect rule".

## Scientific facts preserved

- v3 seven-model totals remain 19/40, 35/40, 39/40, 40/40, 40/40, 34/40 and 40/40.
- Haiku 4.5 and Sonnet 4.6 remain 19/40 and 35/40. The run-level mean gap remains 1.6 tasks; the exact two-sided permutation-test result remains `p=2.3e-4`.
- The 26 Claude 4.x failed attempts still have `exactly_once=0` in saved checks. The underlying agent-action explanation remains based on the results notes and representative trace checks, not a reinspection of every trajectory.
- The three GPT-6-family pilots remain outside the seven-model table.
- v4 remains three runs per model.
- The paper still states the key limitation: version 3 has no matching case where the same injected error occurs but the requested change was not saved.
- Version 2 to version 3 changed multiple features together. The reference solution for the reservation task still avoids the batch request that triggers the evaluated agents' failure.
- No new experiment, score, statistical comparison, or submission claim was added.

## Build status

The abstract, link and caption revision of 2026-11-20 has **not** been rebuilt. Earlier hashes, page counts and PDF/ZIP checksums recorded here no longer applied after later edits and were removed rather than kept stale. Before submission, run `pdflatex → bibtex → pdflatex → pdflatex`, confirm the page count is within the five-page limit, and inspect the footnote URL and table layout.

## Remaining publication gates

Owner confirmation is still required for authorship, final title, overlap/originality review against LIMBO/AFT-Bench/UndoBench, and the decision to submit. This PR is not a conference submission or acceptance.
