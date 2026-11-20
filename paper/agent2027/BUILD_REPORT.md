# IEEE/Overleaf preflight

**Status (2026-11-20): not rebuilt since the abstract, link and caption revision.** The previous report's page count, link count and file hashes described an older revision and were removed.

**Build:** `pdflatex → bibtex → pdflatex → pdflatex` using IEEEtran conference [10pt].

**Checks to run before submission:** page count within the five-page short-paper limit including references; all citations and cross-references resolve; no overfull boxes in the margins; the repository footnote URL wraps cleanly; the last page looks acceptable without `\balance`.

**Overleaf package:** five files: `main.tex`, `references.bib`, `tables/v3-primary.tex`, `tables/revisions.tex`, and `tables/trace-comparison.tex`. Create it from a repository checkout:
```sh
python paper/agent2027/export_overleaf.py --output trustval-overleaf.zip
```
Then use Overleaf **New Project → Upload Project** and compile `main.tex` with pdfLaTeX.

A successful PDF build does not establish originality, acceptance, external replication or a completed conference submission. The matched case where an error occurs but the requested change was not saved remains the main experimental gap.
