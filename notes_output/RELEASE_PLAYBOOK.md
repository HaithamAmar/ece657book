# Release Playbook (Draft → Candidate → Publish)

This is the operator runbook for producing a release candidate and publishing it.
All paths are relative to the repo root `ece657Book/`.

## 0) Preconditions

- Cover and metadata exist:
  - `notes_output/BookCover.png`
  - `notes_output/book_metadata.json`
- You can build the book locally (see `notes_output/SETUP_CHECKLIST.md`).

## 1) Build a release candidate (RC)

```bash
bash notes_output/scripts/run_production_checks.sh
```

Deliverables:
- PDF: `notes_output/ece657_notes.pdf`
- Apple EPUB: `epub_builder/dist/ece657_ebook_apple.epub`
- Kindle EPUB: `epub_builder/dist/ece657_ebook_kindle.epub`
- QC bundle: `notes_output/artifacts/release_checks/`

Gatekeeper audits (fail the run by default):
- Image quality: `notes_output/artifacts/release_checks/epub_image_quality.json`
- Layout overflow: `notes_output/artifacts/release_checks/epub_layout_audit_1000w.md`
- Wide tables (>= 5 columns): `notes_output/artifacts/release_checks/epub_table_audit.json`

Notes:
- One intentionally wide table is allowlisted in the production gatekeeper: the word-feature vectorization table (`ch016.xhtml`) that demonstrates graded feature values (e.g., 0.5 for shared attributes). This table is expected to be horizontally scrollable in reflowable EPUB layouts.

Draft bypass env vars:
- `ALLOW_FLAGGED_IMAGES=1`
- `ALLOW_OVERFLOW=1`
- `ALLOW_WIDE_TABLES=1`

## 2) Human visual QA (required)

Automated checks are not enough. Minimum manual pass:

- Apple Books (macOS):
  - Cover thumbnail shows.
  - TOC depth is reasonable; navigation works.
  - Spot-check: dense-math page, wide table, figure-heavy chapter, callout box.
- Kindle Previewer:
  - Cover shows in library view.
  - Largest images render (no blanks).
  - No “microscopic” tables; no clipped math.

## 3) Tagging (git)

Pick a versioning scheme before first public release. Suggested:
- `vYYYY.MM.DD` for early releases
- move to semantic versions later if desired

Example:
```bash
git status
git tag -a v2026.02.02 -m "Release candidate"
git push origin v2026.02.02
```

## 4) What to upload (platform-facing)

This repo produces two EPUBs; which one you upload depends on the platform:

- Apple Books: upload `epub_builder/dist/ece657_ebook_apple.epub`
- KDP (Kindle): upload `epub_builder/dist/ece657_ebook_kindle.epub`

Keep the QC bundle archived for each release:
- `notes_output/artifacts/release_checks/` (copy it to a dated folder if needed).
