# IEEE/Overleaf preflight — linked terminology pass (2026-11-18)

This report covers the latest revision of the TrustVal AGENT 2027 paper. The LaTeX inputs in the Overleaf package match the current PR branch exactly; their Git blob hashes are recorded in [EDIT_AUDIT.md](EDIT_AUDIT.md).

**Build:** `pdflatex → bibtex.original → pdflatex → pdflatex` using IEEEtran conference [10pt] and the project's listed LaTeX packages.

**Result:** 4 US Letter pages including references, within the venue's five-page short-paper limit. All eight bibliography entries cited by the manuscript resolved; all table and section references resolved. No text extends beyond page margins. A few nonfatal line-spacing warnings remain. All four pages were rendered and visually inspected.

**Terminology:** specialized terms and acronyms are explained in plain English at first use and linked to primary sources or official documentation. Table captions define their abbreviations and pass criteria. Project-specific test names link to the relevant TrustVal design notes or control code. The rendered PDF contains 64 clickable link annotations, including links from the one-effect rule and the two example run IDs to their source records.

**Overleaf package:** five files only: `main.tex`, `references.bib`, `tables/v3-primary.tex`, `tables/revisions.tex`, and `tables/trace-comparison.tex`. The ZIP passed integrity testing. It was unpacked into a clean directory and independently compiled to the same four-page result. It has not been uploaded to an Overleaf account.

Create the package from a repository checkout:
```sh
python paper/agent2027/export_overleaf.py --output trustval-overleaf.zip
```
Then use Overleaf **New Project → Upload Project** and compile `main.tex` with pdfLaTeX.

A successful PDF build does not establish originality, acceptance, external replication or a completed conference submission. The matched case where an error occurs but the requested change was not saved remains the main experimental gap.
