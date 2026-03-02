# Publishability QA Report

Date: 2026-02-28

This report captures the mechanical checks we run to keep the manuscript "publisher-ready":
clean builds, no unresolved references, and basic placeholder hygiene. It also notes the
minimal attribution + bibliography normalization work completed in this pass.

## 1) Placeholder / hygiene scans

Scanned the book sources (excluding `notes_output/review/**` and `notes_output/artifacts/**`) for common
draft placeholders:

```bash
rg -n "TODO|FIXME|TBD|\\?\\?" notes_output --glob '*.tex' \
  --glob '!notes_output/review/**' --glob '!notes_output/artifacts/**'
```

Result: no matches.

## 2) Production QA gates (PDF + EPUB)

Strict numeric verification:

```bash
python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict
```

Full production checks (PDF build + crossref/citation gates + EPUB build + EPUBCheck):

```bash
bash notes_output/scripts/run_production_checks.sh
```

Result: PASS (including the TeX warning gate: no undefined refs/cites and no overfull `\\hbox` above the
configured threshold).

## 3) Rights / attribution sweep (figures)

For raster/vector assets included via `\\includegraphics` in the main book build, captions now include a
one-line `Source:` statement so rights/ownership is explicit at the point of use.

Edits made:
- Added `Source: author-generated.` to the affected figure captions.
- Removed template-y "Use it when ..." phrasing from two captions while preserving the meaning.

## 4) Reference normalization (URLs + access dates)

Bibliography entries with a `url = {...}` field now include a consistent access-date note:
`note = {Accessed 2026-02-28}`.

Keys updated in `notes_output/refs.bib`:
- `Radford2019`
- `Radford2018`
- `MacQueen1967`
- `DebAgrawal1995`
- `Zitzler2002`
- `Fritzke1994GrowingNeuralGas`

