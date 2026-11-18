# AGENT 2027 TrustVal PDF quality gate — 2026-11-17

## Exact-source build verification

The four **actual GitHub draft-branch file contents** were reproduced in the local TeX working directory and checked against GitHub Git blob SHAs; no prose approximation remained. This is exact source matching for the complete compile inputs, **not** a claim that all of the separate research repository was freshly cloned, its agent episodes rerun, or the uploaded submission portal tested.

| File | Matched Git blob SHA |
|---|---|
| `paper/agent2027/main.tex` | `d5a56a85443253e5eb0c84ecef21783876ace3bf` |
| `paper/agent2027/references.bib` | `0091b93b4c0f853fa40bcf72f621af1ffe0c78ef` |
| `paper/agent2027/tables/v3-primary.tex` | `ebe805562ff716dfe931a4cf4d4b48c6fa0cc549` |
| `paper/agent2027/tables/revisions.tex` | `1ade69f3d7d26c109b1c32a8753188ed35fb466e` |

Built with TeX Live 2025 pdfLaTeX/BibTeX and IEEEtran `[10pt,conference]`, US Letter, two columns. Commands:

```bash
cd paper/agent2027
pdflatex -halt-on-error -interaction=nonstopmode main.tex
bibtex main   # bibtex.original if this environment's wrapper does not expose bibtex
pdflatex -halt-on-error -interaction=nonstopmode main.tex
pdflatex -halt-on-error -interaction=nonstopmode main.tex
pdfinfo main.pdf | grep Pages
```

**Result: 4 pages including all 8 bibliographic entries; AGENT short-paper maximum is 5 pages including references.** No undefined citations/references, fatal LaTeX errors or overfull boxes reported in the final pass. One nonfatal underfull paragraph warning remains near the abstract/intro transition. The bibliography uses `balance` to avoid leaving an entirely empty right column. Each of the four pages was rendered and inspected; normal text, data tables and citations are legible, no overlap/clipping detected.

## Numerical and literature audits

- Checked `results/summary_v3.json` against the full seven-model LaTeX table; **all seven rows exactly match**. Main counts: 19/40, 35/40, 39/40, 40/40, 40/40, 34/40, 40/40.
- Recomputed the run-level two-sided exact permutation comparison, Haiku 4.5 vs Sonnet 4.6: **42 / 184756 = 0.00022732685**, reported as `2.3e-4` for ten independent four-task runs/model.
- Read **all 20 saved Claude v3 `regrade.json` files**: 21/40 failures for Haiku 4.5, 5/40 for Sonnet 4.6; every failed task has `exactly_once=0`. This checks the outcome, **not** every trajectory's blind-retry attribution.
- Independently checked representative raw trajectories and saved regrades for successful and failed payout and batch recovery, plus the v4 sleep/harness interaction. The actual binary SQLite exports were not independently inspected in this turn.
- Checked official AGENT CFP and full available peer-reviewed/preprint prior work, including **LIMBO, UndoBench, Verified Tool Calls, AFT-Bench, Evidence-Guided Recovery, and AgentFaultBench (posted Nov 16, 2026)**. The paper no longer claims novelty for timeout-after-commit recovery, effect-ledger grading, false success reports, or interface effects.
- Added the principal design defect that remains: **no matched non-commit timeout** in v3, so a no-retry strategy could succeed on some single-write cases without diagnosing the outcome. The main claims are limited accordingly.

## Remaining gates that do not block the *best draft* but do block external submission

1. Author list and affiliation are provisionally set to **Vedant D. Borkute, University of California, Riverside**; owner must confirm before publication or add any coauthors accurately.
2. Independent skeptical novelty review remains important. The short **engineering experience / benchmark case study** might be publishable at AGENT; a general exactly-once research novelty claim would not be credible.
3. Publication ethics and dual-submission check, final owner approval, and conference HotCRP upload/receipt are deliberately **not** automated. No paper was submitted or accepted.
4. An external reproduction of all hosted models or full direct SQL audit would strengthen the study, but is not part of this writing-only pass.

**Summary:** PDF and evidence editorial preflight complete; best current-evidence draft prepared. It is not automatically an original accepted paper.
