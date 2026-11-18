# Paper-writing skill pass — terminology, evidence and Overleaf checks

Date: 2026-11-18. Base: merged PR #1, commit `23972f3`. This branch changes manuscript wording, links and layout only. It does not change benchmark tasks, model runs, grading rules or publication status.

## Editorial changes

- Open with the recorded payment example: one agent repeated a payment without checking; another checked the saved record first.
- Consolidate the version-2/version-3 design explanation and retain the warning that several features changed together.
- Keep the main result table beside Results and add the two-run payment comparison.
- Replace abstract shorthand with descriptions of the actual action and saved database result.
- Define technical terms and acronyms in ordinary language at first use, with clickable sources. Table captions explain their abbreviations and pass criteria.
- Link general concepts to primary or official sources: [API](https://developer.mozilla.org/en-US/docs/Glossary/API), [HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview), [safe API retries](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/), [SQLite](https://www.sqlite.org/about.html), [Harbor](https://github.com/harbor-framework/harbor), [Modal](https://modal.com/docs/guide), [Claude Code](https://docs.anthropic.com/en/docs/claude-code/getting-started), [Codex](https://developers.openai.com/codex/cli/), and [permutation tests](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.permutation_test.html).
- Link TrustVal-specific terms and controls to the relevant [version-3 design](https://github.com/Vedant2100/trustval/blob/main/DESIGN_V3.md), [version-4 design](https://github.com/Vedant2100/trustval/blob/main/DESIGN_V4.md), and [control script](https://github.com/Vedant2100/trustval/blob/main/scripts/naive_cases.inc).

## Scientific facts preserved

- v3 seven-model totals remain 19/40, 35/40, 39/40, 40/40, 40/40, 34/40 and 40/40.
- Haiku 4.5 and Sonnet 4.6 remain 19/40 and 35/40. The run-level mean gap remains 1.6 tasks; the exact two-sided permutation-test result remains `p=2.3e-4`.
- The 26 Claude 4.x failed attempts still have `exactly_once=0` in saved checks. The underlying agent-action explanation remains based on the results notes and representative trace checks, not a reinspection of every trajectory.
- The three GPT-6-family pilots remain outside the seven-model table.
- v4 remains three runs per model.
- The paper still states the key limitation: version 3 has no matching case where the same timeout occurs but the requested change was not saved.
- Version 2 to version 3 changed multiple features together. The reference solution for the reservation task still avoids the batch request that triggers the evaluated agents' failure.
- No new experiment, score, statistical comparison, or submission claim was added.

## Exact-source build and Overleaf import

The five local LaTeX inputs match the GitHub branch's exact file hashes:

| File | Git blob |
|---|---|
| `main.tex` | `92f0c77bfd3842225bedcfdb00fe91cdd02bf965` |
| `references.bib` | `0091b93b4c0f853fa40bcf72f621af1ffe0c78ef` |
| `tables/v3-primary.tex` | `1970e500946f956a8e353772870a6a6a9d1bf395` |
| `tables/revisions.tex` | `4b6ac493cc1c11599439cd3bdacaa50cfd94d493` |
| `tables/trace-comparison.tex` | `96566a5c6757c124d9a950f8bc40719a761e2d01` |

- Built with [pdfLaTeX](https://www.overleaf.com/learn/latex/PDF) and [BibTeX](https://www.overleaf.com/learn/latex/Bibliography_management_with_bibtex): **4 US Letter pages including references**, within the five-page short-paper limit.
- All eight citations and all cross-references resolved. No text extends beyond page margins. A few nonfatal line-spacing warnings remain.
- All four pages were rendered and visually inspected. The PDF contains **59 clickable links**.
- The five-file Overleaf ZIP passed archive-integrity testing, was extracted into a clean directory, and compiled independently to the same four-page PDF.
- The ZIP has not been uploaded to an Overleaf account; it is ready for **New Project → Upload Project**.

SHA-256:
- PDF: `9423924f9526212b73f851adb899d8a5fb8688c39d4ddb17475983c511bcb588`
- ZIP: `4825a564e469067e4b0249290c04ccdb8c25d01c0cf6009ca6ca8c65ae4ba45b`

## Remaining publication gates

Owner confirmation is still required for authorship, final title, overlap/originality review against LIMBO/AFT-Bench/UndoBench, and the decision to submit. This PR is not a conference submission or acceptance.
