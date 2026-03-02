# Release Candidate Packet (Publish-Readiness Evidence)

- Date: 2026-03-02
- Branch: `codex/publishability-qa`
- Release-candidate source commit: `be3bdb4`

## What changed in this RC

- EPUB citations now render as visible text (citeproc enabled during Pandoc conversion).
- New required production gate: EPUB citation visibility audit (fails on empty citation spans / “inspired by .” symptom).
- Chapter 14 seq2seq attention block: fixed an EPUB orphan-punctuation artifact by restructuring the softmax explanation.
- Publishing QC cleanup: removed tab characters and trailing whitespace in the files flagged by the QC report.
- Figure truthfulness + placement polish (P2.2): tightened a handful of captions/lead-ins so schematic plots are not overstated, and moved a few figures closer to first mention to reduce EPUB float drift.
- Bibliography metadata corrections: updated three high-visibility references (IEEE EAD, Jurafsky/Martin SLP3, Zadeh 1997 granulation paper) to verified, searchable metadata and kept the soft-computing attribution sentence historically honest.

## Commands run (for reproducibility)

```sh
python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict
bash notes_output/scripts/run_production_checks.sh
```

Standalone citation audit (also run inside production checks):

```sh
python3 epub_builder/scripts/audit_epub_citations.py --epub epub_builder/dist/ece657_ebook_apple.epub
python3 epub_builder/scripts/audit_epub_citations.py --epub epub_builder/dist/ece657_ebook_kindle.epub
```

## PASS/FAIL summary (this RC)

- Strict numeric + plot verification (`--strict`): **PASS** (27/27)
- Production checks (PDF + Apple/Kindle EPUB builds + QC + release audits): **PASS**
- EPUB citation audit (Apple + Kindle): **PASS** (empty spans = 0)
- EPUBCheck (Apple + Kindle): **PASS**

## Artifacts (evidence bundle)

### Build outputs
- PDF: `/Users/Haitham.Amar/Documents/ece657Book/notes_output/ece657_notes.pdf`
- Apple EPUB: `/Users/Haitham.Amar/Documents/ece657Book/epub_builder/dist/ece657_ebook_apple.epub`
- Kindle EPUB: `/Users/Haitham.Amar/Documents/ece657Book/epub_builder/dist/ece657_ebook_kindle.epub`

### Release checks
- Root: `/Users/Haitham.Amar/Documents/ece657Book/notes_output/artifacts/release_checks/`
- Summary report: `/Users/Haitham.Amar/Documents/ece657Book/notes_output/artifacts/release_checks/report.txt`
- Manifest: `/Users/Haitham.Amar/Documents/ece657Book/notes_output/artifacts/release_checks/manifest.json`
- EPUBCheck logs:
  - `/Users/Haitham.Amar/Documents/ece657Book/notes_output/artifacts/release_checks/epubcheck/ece657_ebook_apple.epubcheck.txt`
  - `/Users/Haitham.Amar/Documents/ece657Book/notes_output/artifacts/release_checks/epubcheck/ece657_ebook_kindle.epubcheck.txt`

### QC / audits
- Root: `/Users/Haitham.Amar/Documents/ece657Book/notes_output/artifacts/qc/`
- Strict validator report:
  - `/Users/Haitham.Amar/Documents/ece657Book/notes_output/artifacts/qc/math_graph_validation_20260301_225026.md`
  - `/Users/Haitham.Amar/Documents/ece657Book/notes_output/artifacts/qc/math_graph_validation_20260301_225026.json`
- Publishing QC report:
  - `/Users/Haitham.Amar/Documents/ece657Book/notes_output/artifacts/qc/publish_qc_report.md`
- Chapter format audit report:
  - `/Users/Haitham.Amar/Documents/ece657Book/notes_output/artifacts/qc/chapter_format_audit_20260301_225250.md`

### Rights / attribution
- Rights inventory: `/Users/Haitham.Amar/Documents/ece657Book/notes_output/review/rights_attribution_inventory_20260228.md`

## Known residual risks (what still needs human judgment)

- **Permissions are legal, not technical:** the rights inventory is a heuristic screen. If a publisher requires formal permissions for specific adapted figures (even when redrawn), that still needs human follow-up.
- **Non-blocking LaTeX warnings remain:** underfull boxes and benign float-spec warnings persist; they do not break layout in the release checks, but a publisher may still request tightening in a later pass.
