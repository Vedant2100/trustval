# Local PDF preflight, 2026-11-17

A **locally mirrored** copy of the current short-paper LaTeX draft, with its IEEE table and bibliography, was compiled using the container's TeX Live 2025 / pdfLaTeX toolchain. This is a build and layout preflight, **not a CI build from the GitHub head commit**, and it does not establish that the exact byte-for-byte committed source has been rebuilt in a fresh clone.

## Commands executed

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex.original main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdfinfo main.pdf | grep Pages
python /home/oai/skills/pdfs/scripts/render_pdf.py main.pdf --out_dir render4 --dpi 100
```

- IEEEtran 10-point conference, US Letter, two columns: **3 pages including references**, below the official AGENT 2027 short-paper limit of 5 pages including references.
- BibTeX ran using the system's `bibtex.original` binary because the `latexmk` wrapper did not find the `bibtex` executable in its subprocess PATH; after manual BibTeX execution, the LaTeX build succeeded.
- All five citation keys resolved and there were no missing cross-references, fatal TeX errors or reported overfull-box warnings. Minor `Underfull \\hbox` warnings appeared around the short contributions paragraph; visual review did not find clipped text.
- **Layout defect identified and corrected:** the initial two-column table float appeared on a nearly blank page 3. The `\\input{tables/v3-primary.tex}` call was relocated before the benchmark-design section, yielding a full-width results table at the top of page 2 and references on page 3.
- Rendered pages 1, 2 and 3 were individually inspected. Title, abstract, two-column text, source-generated results table and bibliography are legible; no overlapping elements observed.
- The author and affiliation block still contains placeholders and **must be completed before submission**. A skeptical technical review of originality against LIMBO/UndoBench is still pending before the archival decision.

## Next exact-source gate

From a fresh clone of **this PR head**, run:

```sh
cd paper/agent2027
pdflatex -halt-on-error -interaction=nonstopmode main.tex
bibtex main
pdflatex -halt-on-error -interaction=nonstopmode main.tex
pdflatex -halt-on-error -interaction=nonstopmode main.tex
pdfinfo main.pdf | grep Pages
```

Verify `git diff --exit-code` after rebuilding the generated results table from `results/summary_v3.json`, and inspect all rendered pages of the resulting exact-source PDF. Build and visual review are *necessary* but not sufficient: the scientific originality and venue-specific author/submission checks remain open.

**No paper submitted and no paper accepted.**
