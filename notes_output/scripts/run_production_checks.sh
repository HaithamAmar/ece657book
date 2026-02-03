#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REPO_ROOT="$(cd "${ROOT_DIR}/.." && pwd)"

cd "${ROOT_DIR}"

echo "[1/3] Release checks (PDF + EPUB build + snapshots)…"
bash "${ROOT_DIR}/scripts/run_release_checks.sh"

echo "[2/4] Sanity-check publishing inputs…"
if [[ ! -f "${ROOT_DIR}/BookCover.png" ]]; then
  echo "Missing cover image: ${ROOT_DIR}/BookCover.png" >&2
  echo "Add a production cover (PNG) before publishing." >&2
  exit 2
fi

# Basic cover sanity: KDP/Apple Books generally expect a reasonably high-res cover.
# Allow bypass for drafts via `ALLOW_LOWRES_COVER=1`.
if [[ "${ALLOW_LOWRES_COVER:-}" != "1" ]]; then
  /usr/bin/python3 - <<'PY'
from __future__ import annotations

import struct
from pathlib import Path

cover = Path("BookCover.png")
data = cover.read_bytes()
if data[:8] != b"\x89PNG\r\n\x1a\n":
    raise SystemExit(f"BookCover.png is not a valid PNG: {cover}")

# IHDR chunk starts at byte 8: length(4) + type(4) + data...
# Width/height are the first 8 bytes of IHDR data.
ihdr_type = data[12:16]
if ihdr_type != b"IHDR":
    raise SystemExit("Invalid PNG: missing IHDR chunk")
width, height = struct.unpack(">II", data[16:24])

# Conservative ebook cover target: short side >= 1600px and long side >= 2560px.
short_side = min(width, height)
long_side = max(width, height)
min_short = 1600
min_long = 2560
if short_side < min_short or long_side < min_long:
    raise SystemExit(
        f"Cover resolution too small: {width}x{height}px. "
        f"Target at least {min_short}x{min_long}px (set ALLOW_LOWRES_COVER=1 to bypass for drafts)."
    )
print(f"BookCover.png: OK ({width}x{height}px)")
PY
fi

/usr/bin/python3 - <<'PY'
import json
from pathlib import Path

path = Path("book_metadata.json")
raw = json.loads(path.read_text(encoding="utf-8"))
required = ["title", "creator", "language", "identifier", "publisher", "rights"]
missing = [k for k in required if not isinstance(raw.get(k), str) or not raw.get(k).strip()]
if missing:
    raise SystemExit(f"book_metadata.json missing/empty fields: {', '.join(missing)}")
print("book_metadata.json: OK")
PY

echo "[3/4] Gatekeeper audits (Apple EPUB)…"

# Gatekeeper defaults: fail if any of these audits flag a problem.
# Allow bypass for drafts via:
# - ALLOW_FLAGGED_IMAGES=1
# - ALLOW_WIDE_TABLES=1
# - ALLOW_OVERFLOW=1
RELEASE_DIR="${ROOT_DIR}/artifacts/release_checks"
IMG_QC_JSON="${RELEASE_DIR}/epub_image_quality.json"
TABLE_QC_JSON="${RELEASE_DIR}/epub_table_audit.json"
LAYOUT_QC_MD="${RELEASE_DIR}/epub_layout_audit_1000w.md"

if [[ -f "${IMG_QC_JSON}" && "${ALLOW_FLAGGED_IMAGES:-}" != "1" ]]; then
  /usr/bin/python3 - <<'PY'
import json
from pathlib import Path

p = Path("artifacts/release_checks/epub_image_quality.json")
d = json.loads(p.read_text(encoding="utf-8"))
flagged = int(d.get("summary", {}).get("flagged_images", 0))
total = int(d.get("summary", {}).get("total_images", 0))
if flagged:
    raise SystemExit(f"Image QC failed: flagged_images={flagged}/{total}. Set ALLOW_FLAGGED_IMAGES=1 to bypass for drafts.")
print(f"Image QC: OK (flagged_images=0/{total})")
PY
fi

if [[ -f "${TABLE_QC_JSON}" && "${ALLOW_WIDE_TABLES:-}" != "1" ]]; then
  /usr/bin/python3 - <<'PY'
import json
from pathlib import Path

p = Path("artifacts/release_checks/epub_table_audit.json")
tables = json.loads(p.read_text(encoding="utf-8"))
flag_cols = 5
wide = [t for t in tables if int(t.get("n_cols", 0)) >= flag_cols]
if wide:
    sample = ", ".join(sorted({t.get("xhtml", "?") for t in wide})[:10])
    raise SystemExit(
        f"Table QC failed: {len(wide)} table(s) with >= {flag_cols} columns. "
        f"Example XHTML: {sample}. Set ALLOW_WIDE_TABLES=1 to bypass for drafts."
    )
print(f"Table QC: OK (no tables with >= {flag_cols} columns)")
PY
fi

if [[ -f "${LAYOUT_QC_MD}" && "${ALLOW_OVERFLOW:-}" != "1" ]]; then
  /usr/bin/python3 - <<'PY'
import re
from pathlib import Path

p = Path("artifacts/release_checks/epub_layout_audit_1000w.md")
s = p.read_text(encoding="utf-8", errors="ignore")
m = re.search(r"Issues found:\s*(\d+)", s)
issues = int(m.group(1)) if m else None
if issues is None:
    raise SystemExit("Layout QC failed: could not parse Issues found from epub_layout_audit_1000w.md")
if issues:
    raise SystemExit(f"Layout QC failed: Issues found={issues}. Set ALLOW_OVERFLOW=1 to bypass for drafts.")
print("Layout QC: OK (Issues found=0)")
PY
fi

echo "[4/4] EPUBCheck (required for production)…"
EPUBCHECK_OUT="${ROOT_DIR}/artifacts/release_checks/epubcheck"
mkdir -p "${EPUBCHECK_OUT}"

echo "Structural verify (EPUB)…"
/usr/bin/python3 "${REPO_ROOT}/epub_builder/scripts/verify_epub_structure.py" \
  --epub "${REPO_ROOT}/epub_builder/dist/ece657_ebook_apple.epub" \
  --aux "${REPO_ROOT}/epub_builder/artifacts/tmp/aux/ece657_notes_epub_aux.aux"
/usr/bin/python3 "${REPO_ROOT}/epub_builder/scripts/verify_epub_structure.py" \
  --epub "${REPO_ROOT}/epub_builder/dist/ece657_ebook_kindle.epub" \
  --aux "${REPO_ROOT}/epub_builder/artifacts/tmp/aux/ece657_notes_epub_aux.aux"

bash "${ROOT_DIR}/scripts/run_epubcheck.sh" --out "${EPUBCHECK_OUT}" \
  "${REPO_ROOT}/epub_builder/dist/ece657_ebook_kindle.epub" \
  "${REPO_ROOT}/epub_builder/dist/ece657_ebook_apple.epub"

echo "Wrote:"
echo "  ${ROOT_DIR}/artifacts/release_checks/report.txt"
echo "  ${ROOT_DIR}/artifacts/release_checks/manifest.json"
echo "  ${EPUBCHECK_OUT}/"
