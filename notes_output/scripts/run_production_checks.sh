#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "${ROOT_DIR}"

echo "[1/3] Release checks (PDF + EPUB build + snapshots)…"
bash "${ROOT_DIR}/scripts/run_release_checks.sh"

echo "[2/3] Sanity-check publishing inputs…"
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

echo "[3/3] EPUBCheck (required for production)…"
EPUBCHECK_OUT="${ROOT_DIR}/artifacts/release_checks/epubcheck"
mkdir -p "${EPUBCHECK_OUT}"
bash "${ROOT_DIR}/scripts/run_epubcheck.sh" --out "${EPUBCHECK_OUT}"

echo "Wrote:"
echo "  ${ROOT_DIR}/artifacts/release_checks/report.txt"
echo "  ${ROOT_DIR}/artifacts/release_checks/manifest.json"
echo "  ${EPUBCHECK_OUT}/"
