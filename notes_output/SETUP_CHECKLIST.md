# Setup Checklist (Fresh Machine)

This checklist targets a clean macOS install and is written to make this repo reproducible.
All paths are relative to the repo root `ece657Book/`.

## 1) Required command-line tools

The EPUB builder requires these binaries on `PATH`:
- `pandoc` (tested with `pandoc 3.8.2`)
- `pdflatex` (TeX Live)
- `pdftoppm` (Poppler)

Optional but strongly recommended for production:
- `epubcheck` **or** Java (`java`) + an EPUBCheck jar (see `notes_output/scripts/run_epubcheck.sh`)
- `tectonic` (for fast, reproducible PDF builds via `notes_output/scripts/run_editorial_qc.sh`)

Sanity check:
```bash
command -v pandoc pdflatex pdftoppm >/dev/null
pandoc --version | head -n 2
pdflatex --version | head -n 1
pdftoppm -v | head -n 1
```

## 2) Python (system)

- Requires `python3` (macOS system python is OK for the builder).

Sanity check:
```bash
python3 --version
```

## 3) Optional: QC dependencies for screenshot/layout/image audits

Some QC scripts use headless Chromium and image analysis.
Install once into `epub_builder/.venv`:

```bash
python3 -m venv epub_builder/.venv
epub_builder/.venv/bin/pip install --upgrade pip
epub_builder/.venv/bin/pip install playwright pillow numpy opencv-python
epub_builder/.venv/bin/python -m playwright install chromium
```

## 4) One-command “am I ready to publish?” check

This runs:
- PDF build + editorial QC
- EPUB build (Apple + Kindle) via `epub_builder/`
- Snapshot bundle generation
- EPUBCheck on the built EPUBs

```bash
bash notes_output/scripts/run_production_checks.sh
```

Outputs:
- `notes_output/artifacts/release_checks/report.txt`
- `notes_output/artifacts/release_checks/manifest.json`
- `notes_output/artifacts/release_checks/pdf/`
- `notes_output/artifacts/release_checks/epub/`
- `notes_output/artifacts/release_checks/epubcheck/`

