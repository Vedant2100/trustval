# TrustVal paper: AGENT 2027 short experience / benchmark report

**Paper source:** [main.tex](main.tex) (IEEEtran conference format, 10 pt, single-anonymous). The paper is a draft; no upload to AGENT HotCRP or Overleaf is implied.

## Read and edit the paper

- `main.tex`: manuscript, results, engineering lessons and limitations.
- `references.bib`: cited literature.
- `tables/v3-primary.tex`: **generated** seven-model results table; do not hand-edit.
- `tables/revisions.tex`: descriptive v2/v3/v4 instrument-design comparison.
- `tables/trace-comparison.tex`: observed command-level difference between one failed and one successful payout recovery.
- `CLAIM_LEDGER.md`, `TRACE_AUDIT.md`, `NOVELTY_REVIEW.md`: evidence, raw-trace spot checks and unresolved scientific threats.

All paper sources live under `paper/agent2027/`; the research datasets and runtime artifacts remain in the repository's `results/` and `tasks/` folders.

## View in Overleaf (no premium integration required)

To make a self-contained Overleaf import ZIP from a checkout of this branch:

```bash
python paper/agent2027/export_overleaf.py --output trustval-overleaf.zip
```

On [Overleaf](https://www.overleaf.com/project), select **New Project → Upload Project**, choose `trustval-overleaf.zip`, set **main document** to `main.tex` (usually autodetected), and compile using **pdfLaTeX**. The ZIP contains only the five LaTeX inputs in the directory layout they require; no full GitHub repository, dataset, compiled output, or private credentials are needed. [Overleaf's official project-upload instructions](https://docs.overleaf.com/managing-projects-and-files/uploading-a-project).

**This is an import, not live sync.** Overleaf GitHub synchronization requires an eligible premium account and a new Overleaf project imported from a GitHub repository; it pulls from GitHub manually rather than automatically. Because this repository also includes run outputs and agent code, GitHub-syncing the whole repository to Overleaf is not the recommended paper-editing workflow. [Official GitHub sync instructions](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/github-synchronization).

## Reproduce the results table

From the repository root:

```bash
python scripts/aggregate.py v3
python paper/agent2027/build_tables.py
git diff --exit-code -- results/summary_v3.json paper/agent2027/tables/v3-primary.tex
```

The aggregator checks locally regraded task success against stored hosted results. The generator requires ten complete four-task runs per model and preserves exact denominators.

## Compile without Overleaf

From `paper/agent2027/`:

```bash
pdflatex -halt-on-error -interaction=nonstopmode main.tex
bibtex main
pdflatex -halt-on-error -interaction=nonstopmode main.tex
pdflatex -halt-on-error -interaction=nonstopmode main.tex
pdfinfo main.pdf | grep Pages
```

Use IEEEtran/TeX Live with `booktabs`, `amsmath`, `url`, `graphicx`, and `balance` packages. Render and inspect every page; passing LaTeX alone is insufficient.

## Scientific and submission boundaries

This study reports **four fixed tasks**, ten repeated runs per model for v3, and only a small three-run v4 pilot. It does **not** include indistinguishable timeouts both with and without a committed write, and v2→v3 changed several factors together. Cross-provider comparisons are harness-confounded, while the batch reference policy avoids the batch endpoint. Preserve these facts during writing edits. The title, author list, and final venue submission remain subject to owner approval.

Official CFP: [AGENT 2027](https://conf.researchr.org/home/icse-2027/agent-2027). Short paper: **at most five pages including references**; deadline **November 20, 2026 at 23:59 AoE**. This repo's PR review and Overleaf import are **not** an archival submission.
