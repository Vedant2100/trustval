# TrustVal paper: AGENT 2027 short paper

**Paper source:** [`main.tex`](main.tex). It is written in [LaTeX](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes), a system for preparing typeset documents, and uses [IEEEtran](https://ctan.org/pkg/ieeetran), the template for conference papers from the Institute of Electrical and Electronics Engineers (IEEE). The rendered paper is a [PDF](https://www.adobe.com/acrobat/about-adobe-pdf.html), or Portable Document Format file. The target venue describes its review as **single-anonymous**: reviewers can see the authors' names, while authors do not see reviewers' names ([AGENT 2027 call for papers](https://conf.researchr.org/home/icse-2027/agent-2027)). This is a draft; it has not been uploaded to the conference or to Overleaf.

## Paper and experiment files

- [`main.tex`](main.tex): manuscript, results, limitations and linked explanations of technical terms.
- [`references.bib`](references.bib): bibliography entries used by LaTeX.
- [`tables/v3-primary.tex`](tables/v3-primary.tex): **generated** seven-model results table; do not hand-edit the counts.
- [`tables/revisions.tex`](tables/revisions.tex): comparison of the three test versions.
- [`tables/trace-comparison.tex`](tables/trace-comparison.tex): two actual recorded payment attempts, including what each agent did after the timeout.
- [`CLAIM_EVIDENCE.md`](CLAIM_EVIDENCE.md), [`TRACE_AUDIT.md`](TRACE_AUDIT.md), [`NOVELTY_REVIEW.md`](NOVELTY_REVIEW.md): evidence behind the claims, checks of recorded agent actions, and remaining questions about what is new.

A **task manifest** is a configuration file describing a test task and how it is run. The repository also contains supporting services that run beside the main database, prewritten control programs, recorded run IDs, and scripts that check saved database files again. See the [TrustVal repository](https://github.com/Vedant2100/trustval).

## How the evaluation software was used

- [Harbor](https://github.com/harbor-framework/harbor) is the open-source framework used to launch AI agents on repeatable tasks, collect their actions, and run the task checks.
- [Modal](https://modal.com/docs) provides the cloud computing environments used to run the tasks.
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code/getting-started) and [Codex](https://developers.openai.com/codex/cli/) are the agent programs evaluated. A **harness** is the surrounding software that starts an agent, gives it access to tools, and records what it does.
- [SQLite](https://www.sqlite.org/about.html) is the file-based database engine used to store the task records.

## View the paper in Overleaf

Create a self-contained Overleaf project ZIP from a checkout of this branch:

```bash
python paper/agent2027/export_overleaf.py --output trustval-overleaf.zip
```

On [Overleaf](https://www.overleaf.com/project), choose **New Project → Upload Project** and select `trustval-overleaf.zip`. Set `main.tex` as the main document if it is not selected automatically.

The ZIP contains only the five files LaTeX needs: `main.tex`, `references.bib`, and the three table files. It does not include experiment data, compiled output, or credentials. See [Overleaf's upload instructions](https://docs.overleaf.com/managing-projects-and-files/uploading-a-project).

**This creates an import, not a live connection.** Overleaf's [GitHub synchronization](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/github-synchronization) is a separate feature, requires an eligible paid plan, and is manually triggered rather than automatic.

## Recreate the results table

From the repository root:

```bash
python scripts/aggregate.py v3
python paper/agent2027/build_tables.py
git diff --exit-code -- results/summary_v3.json paper/agent2027/tables/v3-primary.tex
```

The first command checks each saved task result against the database checks. The second writes the LaTeX table from the verified summary file. The final command uses Git, a version-control system, to show whether either file changed ([Git diff documentation](https://git-scm.com/docs/git-diff)). Each model must have ten complete runs of the same four tasks.

## Compile without Overleaf

From `paper/agent2027/`:

```bash
pdflatex -halt-on-error -interaction=nonstopmode main.tex
bibtex main
pdflatex -halt-on-error -interaction=nonstopmode main.tex
pdflatex -halt-on-error -interaction=nonstopmode main.tex
pdfinfo main.pdf | grep Pages
```

[`pdfLaTeX`](https://www.overleaf.com/learn/latex/PDF) turns the LaTeX manuscript into a PDF. [BibTeX](https://www.overleaf.com/learn/latex/Bibliography_management_with_bibtex) formats the reference list using `references.bib`. [`pdfinfo`](https://manpages.debian.org/bookworm/poppler-utils/pdfinfo.1.en.html) is a utility that reads a PDF's metadata; here it prints the page count. The project uses the IEEEtran template and LaTeX packages (add-ons that provide table formatting, equations, links and page layout): [booktabs](https://ctan.org/pkg/booktabs), [amsmath](https://ctan.org/pkg/amsmath), [url](https://ctan.org/pkg/url), [graphicx](https://ctan.org/pkg/graphicx), [balance](https://ctan.org/pkg/balance), [float](https://ctan.org/pkg/float), and [hyperref](https://ctan.org/pkg/hyperref). Render and inspect every page; a successful compile alone does not show that the paper is readable.

## Study limits and submission status

The study reports **four fixed tasks**, with ten repeated runs per model for version 3 and only three runs per model in the version-4 follow-up. It does **not** include matching timeouts where the same error occurs but the requested change was not saved. Several features changed together between versions 2 and 3. Different model providers used different agent software, so their scores cannot be attributed to model differences alone. The reference solution for the reservation task avoids the batch request that triggers the failure for evaluated agents. Preserve these limits in every version of the paper.

A **CFP** is a call for papers: the venue's official description of topics, format, eligibility and deadlines. The [AGENT 2027 CFP](https://conf.researchr.org/home/icse-2027/agent-2027) lists a short-paper limit of five pages including references and a deadline of November 20, 2026 at 23:59 **AoE**. AoE means Anywhere on Earth, the time zone at UTC−12 ([time-zone explanation](https://www.timeanddate.com/time/zones/aoe)). This repository's review and Overleaf import are **not** a conference submission or acceptance.
