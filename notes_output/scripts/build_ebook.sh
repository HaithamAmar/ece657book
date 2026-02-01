#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT_DIR="${ROOT_DIR}/artifacts/ebook"

# Tuning knobs (use env vars to override):
# - Kindle PNG width dominates file size; 1600 is usually plenty for reflow.
# - PDF DPI only affects embedded PDF figures (rare; prefer PNG assets anyway).
KINDLE_PNG_WIDTH="${KINDLE_PNG_WIDTH:-1600}"
KINDLE_INLINE_PNG_WIDTH="${KINDLE_INLINE_PNG_WIDTH:-800}"
KINDLE_PDF_DPI="${KINDLE_PDF_DPI:-300}"

# Ensure common package-manager prefixes are on PATH so helper binaries (notably
# Ghostscript for dvisvgm) are discoverable in non-login shells.
for cmd in tex4ebook python3; do
  if ! command -v "${cmd}" >/dev/null 2>&1; then
    echo "Missing dependency: ${cmd}. Ensure it is installed and on PATH." >&2
    exit 1
  fi
done
if ! command -v gs >/dev/null 2>&1; then
  echo "Missing dependency: gs (Ghostscript). Install Ghostscript and ensure 'gs' is on PATH." >&2
  exit 1
fi

rm -rf "${OUT_DIR}"
mkdir -p "${OUT_DIR}"

cd "${ROOT_DIR}"

# TeX4ht can leave behind intermediates that break subsequent builds if the
# previous run aborted (including a stray `\r`-suffixed xref file such as
# `ece657_ebook.xref\r`). Remove the usual suspects up front.
rm -f "${ROOT_DIR}/ece657_ebook".{4ct,4tc,aux,css,dvi,idv,lg,log,tmp,xhtml} 2>/dev/null || true
rm -f "${ROOT_DIR}/ece657_ebook".{ncx,xref,xdv} 2>/dev/null || true
rm -f "${ROOT_DIR}/ece657_ebook.xref"* 2>/dev/null || true
rm -f "${ROOT_DIR}/ece657_ebook"*x.svg 2>/dev/null || true
rm -f "${ROOT_DIR}/ece657_ebook"li*.xhtml "${ROOT_DIR}/ece657_ebook"se*.xhtml 2>/dev/null || true
rm -f "${ROOT_DIR}/ece657_ebook".{bbl,blg} 2>/dev/null || true

# Build EPUB3 using tex4ebook (TeX4ht). This keeps color figures for ebook.
# We start with MathML output for speed and size; Apple Books gets a hybrid
# post-process that replaces display equations with SVG for stable rendering.

tex4ebook -f epub3 -d "${OUT_DIR}" ece657_ebook.tex "mathml"

# Preserve the raw TeX4ht output under a clearer name; the Kindle-friendly
# post-processed EPUB is the default artifact for publishing tests.
if [[ -f "${OUT_DIR}/ece657_ebook.epub" ]]; then
  mv -f "${OUT_DIR}/ece657_ebook.epub" "${OUT_DIR}/ece657_ebook_raw.epub"
fi

# Apple Books variant: keep inline MathML, but swap display math to SVG.
APPLE_OUT="${OUT_DIR}/ece657_ebook_apple.epub"
METADATA_JSON="${ROOT_DIR}/book_metadata.json"
METADATA_ARGS=()
if [[ -f "${METADATA_JSON}" ]]; then
  METADATA_ARGS=( --metadata "${METADATA_JSON}" )
fi
APPLE_COVER="${ROOT_DIR}/BookCover.png"
APPLE_COVER_ARGS=()
if [[ -f "${APPLE_COVER}" ]]; then
  APPLE_COVER_ARGS=( --cover "${APPLE_COVER}" )
fi
/usr/bin/python3 "${ROOT_DIR}/scripts/postprocess_epub_apple.py" \
  --input "${OUT_DIR}/ece657_ebook_raw.epub" \
  --output "${APPLE_OUT}" \
  "${METADATA_ARGS[@]}" \
  "${APPLE_COVER_ARGS[@]}"

# Kindle-friendly variant: convert SVG-heavy output to PNG and add CSS overrides.
KINDLE_OUT="${OUT_DIR}/ece657_ebook_kindle.epub"
KINDLE_COVER="${ROOT_DIR}/BookCover.png"
KINDLE_COVER_ARGS=()
if [[ -f "${KINDLE_COVER}" ]]; then
  KINDLE_COVER_ARGS=( --cover "${KINDLE_COVER}" )
fi
/usr/bin/python3 "${ROOT_DIR}/scripts/postprocess_epub_kindle.py" \
  --input "${OUT_DIR}/ece657_ebook_raw.epub" \
  --output "${KINDLE_OUT}" \
  --png-width "${KINDLE_PNG_WIDTH}" \
  --inline-png-width "${KINDLE_INLINE_PNG_WIDTH}" \
  --pdf-dpi "${KINDLE_PDF_DPI}" \
  "${METADATA_ARGS[@]}" \
  "${KINDLE_COVER_ARGS[@]}"

# Convenience: make the default-named EPUB the Apple-friendly one.
cp -f "${APPLE_OUT}" "${OUT_DIR}/ece657_ebook.epub"

# Smoke-test the Kindle EPUB (offline structural QA).
{
  /usr/bin/python3 "${ROOT_DIR}/scripts/epub_smoke_test.py" "${KINDLE_OUT}" || true
  echo
  /usr/bin/python3 "${ROOT_DIR}/scripts/epub_smoke_test.py" --allow-svg "${APPLE_OUT}" || true
} > "${OUT_DIR}/ece657_ebook_smoke_report.txt"

# Keep the EPUB output, but clean TeX4ht intermediates that otherwise clutter
# `notes_output/` and make it easy to accidentally publish the wrong artifacts.
if [[ -f "${ROOT_DIR}/ece657_ebook.log" ]]; then
  cp -f "${ROOT_DIR}/ece657_ebook.log" "${OUT_DIR}/ece657_ebook_build.log"
fi

rm -f "${ROOT_DIR}/ece657_ebook".{4ct,4tc,aux,css,dvi,idv,lg,log,tmp,xhtml} 2>/dev/null || true
rm -f "${ROOT_DIR}/ece657_ebook".{ncx,xref,xdv} 2>/dev/null || true
rm -f "${ROOT_DIR}/ece657_ebook.xref"* 2>/dev/null || true
rm -f "${ROOT_DIR}/ece657_ebook"*x.svg 2>/dev/null || true
rm -f "${ROOT_DIR}/ece657_ebook"li*.xhtml "${ROOT_DIR}/ece657_ebook"se*.xhtml 2>/dev/null || true
rm -f "${ROOT_DIR}/ece657_ebook".{bbl,blg} 2>/dev/null || true

echo "Wrote EPUB outputs to: ${OUT_DIR}"
