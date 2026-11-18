# TrustVal short benchmark paper for AGENT 2027

**Four-page IEEE review draft from exact SHA-verified GitHub source; not submitted.** The canonical task code, results and traces remain outside this directory. Nothing in this branch changes the experiment or records an official paper submission.

- [PLAN.md](PLAN.md): AGENT eligibility and page limit, clear scientific claim, closest prior art, schedule and acceptance gates.
- [CLAIM_LEDGER.md](CLAIM_LEDGER.md): precise numerical claims, original run traces and verification checklist.
- [main.tex](main.tex): revised IEEE short paper, including the no-commit-counterfactual limitation and narrowly positioned literature.
- [references.bib](references.bib): eight directly checked relevant academic sources.
- [build_tables.py](build_tables.py): generates [tables/v3-primary.tex](tables/v3-primary.tex) from the saved regraded v3 summary; source counts checked against the table.
- [tables/revisions.tex](tables/revisions.tex): benchmark-revision validity matrix.
- [NOVELTY_REVIEW.md](NOVELTY_REVIEW.md), [TRACE_AUDIT.md](TRACE_AUDIT.md), [BUILD_REPORT.md](BUILD_REPORT.md): independent quality gates and outstanding submission checks.

## Rebuild the results table

From the repository root:

```bash
python scripts/aggregate.py v3
python paper/agent2027/build_tables.py
git diff -- paper/agent2027/tables/v3-primary.tex
```

The first script compares each saved regrade with the hosted Valkyrie score before calculating the summary. The second uses only the resulting summary JSON and asserts ten runs for every model in the main table. Do not manually alter pass counts to fit the narrative.

## Compile and review (verified locally; repeat after any edits)

From `paper/agent2027/` in a working IEEEtran + BibTeX toolchain:

```bash
pdflatex -halt-on-error -interaction=nonstopmode main.tex
bibtex main
pdflatex -halt-on-error -interaction=nonstopmode main.tex
pdflatex -halt-on-error -interaction=nonstopmode main.tex
pdfinfo main.pdf | grep Pages
```

Confirm the full paper is **no more than five pages including references**. Render and inspect **each** page visually: figures, table, math, citations, author details, pagination, and page breaks. The current branch's four compile inputs have been matched by Git blob SHA to the local sources and compiled into a **4-page** PDF. Each rendered page was visually inspected. Selected raw traces and all twenty Claude v3 saved regrades were separately audited. See [BUILD_REPORT.md](BUILD_REPORT.md) and [TRACE_AUDIT.md](TRACE_AUDIT.md). The binary SQLite exports were not independently reread; an owner-approved HotCRP submission has not occurred.

## Editorial guardrails

No paper claims outside the exact [RESULTS.md](../../RESULTS.md) and source artifacts. Explicitly compare with earlier LIMBO, UndoBench and protocol-aware recovery work; use the design-validity and regression-test contribution only if it survives that comparison. No hype, no unsupported causal interpretation, no fabricated multi-seed numbers, no proxy vs real failures conflation, no generic AI prose or gratuitous em dashes. No submission without an independent final PDF check and author approval.

Official venue: https://conf.researchr.org/home/icse-2027/agent-2027. Deadline: November 20, 2026, 23:59 AoE. Portal: https://icse2027-agent.hotcrp.com/.
