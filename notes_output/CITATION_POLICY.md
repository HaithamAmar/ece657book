# Citation policy (publisher-grade)

This book is a paid academic reference. Every **attribution** and every **non-obvious factual claim** must be traceable to a citation.

## Rules of thumb

- **Must cite**
  - Named results / algorithms when introduced or relied upon.
  - Historical attributions (“X introduced Y in YEAR”).
  - Quantitative claims (benchmarks, reported accuracies, dataset facts).
  - Figures/tables adapted from other sources (cite in caption).
- **Does not need a citation**
  - Widely known math facts (chain rule, Bayes’ theorem), unless attributing the name.
  - Purely pedagogical framing (“In this chapter we…”).

## LaTeX usage

- Prefer `\citet{Key}` when the authors are part of the sentence.
- Prefer `\citep{Key}` when the citation is parenthetical.
- Avoid informal inline citations like `(Author, 2012)`; convert them to `\citet{...}` / `\citep{...}`.

## Automated checks

From repo root:

- Citation/BibTeX hygiene:
  - `python3 notes_output/scripts/check_citations.py`
- Production checks (includes EPUB checks):
  - `bash notes_output/scripts/run_production_checks.sh`

`check_citations.py` enforces:
- Every cite key used in `notes_output/*.tex` exists in `notes_output/refs.bib`.
- No duplicate BibTeX keys in `notes_output/refs.bib`.

