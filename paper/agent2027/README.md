# TrustVal short benchmark paper for AGENT 2027

**Early working draft, not yet compiled or submission-ready.** The canonical task code, results and traces remain outside this directory. Nothing in this branch changes the experiment or records an official paper submission.

- [PLAN.md](PLAN.md): AGENT eligibility and page limit, clear scientific claim, closest prior art, schedule and acceptance gates.
- [CLAIM_LEDGER.md](CLAIM_LEDGER.md): precise numerical claims, original run traces and verification checklist.
- [main.tex](main.tex): initial paper text in IEEE conference mode.
- [references.bib](references.bib): initial verified literature shortlist (not exhaustive).
- [build_tables.py](build_tables.py): generates [tables/v3-primary.tex](tables/v3-primary.tex) from the saved regraded v3 summary.

## Rebuild the results table

From the repository root:

```bash
python scripts/aggregate.py v3
python paper/agent2027/build_tables.py
git diff -- paper/agent2027/tables/v3-primary.tex
```

The first script compares each saved regrade with the hosted Valkyrie score before calculating the summary. The second uses only the resulting summary JSON and asserts ten runs for every model in the main table. Do not manually alter pass counts to fit the narrative.

## Compile and review (still outstanding)

From `paper/agent2027/` in a working IEEEtran + BibTeX toolchain:

```bash
pdflatex -halt-on-error -interaction=nonstopmode main.tex
bibtex main
pdflatex -halt-on-error -interaction=nonstopmode main.tex
pdflatex -halt-on-error -interaction=nonstopmode main.tex
pdfinfo main.pdf | grep Pages
```

Confirm the full paper is **no more than five pages including references**. Render and inspect **each** page visually: figures, table, math, citations, author details, pagination, and page breaks. The current environment has **not** compiled this branch's exact LaTeX source or independently inspected saved state traces; those gates remain open.

## Editorial guardrails

No paper claims outside the exact [RESULTS.md](../../RESULTS.md) and source artifacts. Explicitly compare with earlier LIMBO, UndoBench and protocol-aware recovery work; use the design-validity and regression-test contribution only if it survives that comparison. No hype, no unsupported causal interpretation, no fabricated multi-seed numbers, no proxy vs real failures conflation, no generic AI prose or gratuitous em dashes. No submission without an independent final PDF check and author approval.

Official venue: https://conf.researchr.org/home/icse-2027/agent-2027. Deadline: November 20, 2026, 23:59 AoE. Portal: https://icse2027-agent.hotcrp.com/.
