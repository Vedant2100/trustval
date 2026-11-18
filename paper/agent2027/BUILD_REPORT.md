# IEEE/Overleaf preflight — editorial PR (2026-11-17)

This report supersedes the earlier build log for the **merged** v1 manuscript. The current source was checked out by exact GitHub file contents (five Git blob SHAs listed in [EDIT_AUDIT.md](EDIT_AUDIT.md)) and rebuilt in the local TeX toolchain.

**Compilation:** `pdflatex → bibtex.original → pdflatex → pdflatex` using IEEEtran conference [10pt], `booktabs`, `amsmath`, `url`, `graphicx`, `balance`, `float`. The local `bibtex.original` binary is this container's working BibTeX command.

**Result:** 3 US Letter pages **including references**, within AGENT's 5-page short-paper limit; all eight citation keys resolved; no undefined references or overfull boxes. Nonfatal underfull text/column warnings remain (no visible clipping). Pages 1–3 were rendered and visually inspected. Tables I–III follow their discussion; the final columns were balanced without the previous `balance`-in-second-column warning.

The Overleaf package contains only the five exact compile inputs (`main.tex`, `references.bib`, `tables/v3-primary.tex`, `tables/revisions.tex`, `tables/trace-comparison.tex`). The export ZIP was unpacked in a temporary directory, built independently with the same toolchain, and again produced a 3-page document with resolved citations and no overfull boxes. **It has not been uploaded to any Overleaf account.**

To create it from a repo checkout:
```sh
python paper/agent2027/export_overleaf.py --output trustval-overleaf.zip
```
Then [import as an Overleaf project](https://docs.overleaf.com/managing-projects-and-files/uploading-a-project) and compile with pdfLaTeX.

A successful PDF build is **not** evidence of originality, acceptance, external replication or a completed conference submission. The prior-art overlap and construct-validity limitation remain open.
