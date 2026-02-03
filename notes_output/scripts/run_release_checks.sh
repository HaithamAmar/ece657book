#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT_DIR="${ROOT_DIR}/artifacts/release_checks"
REPO_ROOT="$(cd "${ROOT_DIR}/.." && pwd)"

mkdir -p "${OUT_DIR}"

echo "[1/4] Build + QC (PDF)"
bash "${ROOT_DIR}/scripts/run_editorial_qc.sh"

echo "[2/4] Build (EPUB)"
/usr/bin/python3 "${REPO_ROOT}/epub_builder/build.py" --variant both --clean >/dev/null

echo "[3/5] Generate previews + manifest"
/usr/bin/python3 "${ROOT_DIR}/scripts/generate_previews.py" \
  --pdf "${ROOT_DIR}/ece657_notes.pdf" \
  --epub "${REPO_ROOT}/epub_builder/dist/ece657_ebook_kindle.epub" \
  --out "${OUT_DIR}" \
  --config "${ROOT_DIR}/critical_checks.json" \
  --pdf-dpi 150

echo "[4/5] PDF vs EPUB spot-check bundle (Apple)"
QC_OUT="${OUT_DIR}/pdf_vs_epub_apple"
rm -rf "${QC_OUT}"
mkdir -p "${QC_OUT}"

if [ -x "${REPO_ROOT}/epub_builder/.venv/bin/python" ]; then
  "${REPO_ROOT}/epub_builder/.venv/bin/python" "${REPO_ROOT}/epub_builder/scripts/qc_epub_vs_pdf.py" \
    --epub "${REPO_ROOT}/epub_builder/dist/ece657_ebook_apple.epub" \
    --pdf "${ROOT_DIR}/ece657_notes.pdf" \
    --aux "${REPO_ROOT}/epub_builder/artifacts/tmp/aux/ece657_notes_epub_aux.aux" \
    --out "${QC_OUT}" \
    --max-eq 40 >/dev/null || true
else
  echo "WARN: skipping qc_epub_vs_pdf (missing ${REPO_ROOT}/epub_builder/.venv)."
  echo "      To enable: create venv and install Playwright per notes_output/PRODUCTION_ROADMAP.md."
fi

echo "[5/7] EPUB audits (Apple)"
IMG_JSON="${OUT_DIR}/epub_image_quality.json"
IMG_MD="${OUT_DIR}/epub_image_quality.md"
TABLE_JSON="${OUT_DIR}/epub_table_audit.json"
TABLE_MD="${OUT_DIR}/epub_table_audit.md"
LAYOUT_MD="${OUT_DIR}/epub_layout_audit_1000w.md"

# Image quality and layout audits require the epub_builder venv (Playwright/Pillow).
if [ -x "${REPO_ROOT}/epub_builder/.venv/bin/python" ]; then
  "${REPO_ROOT}/epub_builder/.venv/bin/python" "${REPO_ROOT}/epub_builder/scripts/audit_epub_image_quality.py" \
    --epub "${REPO_ROOT}/epub_builder/dist/ece657_ebook_apple.epub" \
    --out-json "${IMG_JSON}" \
    --out-md "${IMG_MD}" \
    --top 60 >/dev/null || true

  export TMPDIR=/tmp
  "${REPO_ROOT}/epub_builder/.venv/bin/python" "${REPO_ROOT}/epub_builder/scripts/audit_epub_layout.py" \
    --epub "${REPO_ROOT}/epub_builder/dist/ece657_ebook_apple.epub" \
    --out-md "${LAYOUT_MD}" \
    --viewport-w 1000 \
    --viewport-h 1400 >/dev/null || true
else
  echo "WARN: skipping image/layout audits (missing ${REPO_ROOT}/epub_builder/.venv)."
fi

# Table audit is pure-Python (no browser); run it regardless.
/usr/bin/python3 "${REPO_ROOT}/epub_builder/scripts/audit_epub_tables.py" \
  --epub "${REPO_ROOT}/epub_builder/dist/ece657_ebook_apple.epub" \
  --out-json "${TABLE_JSON}" \
  --out-md "${TABLE_MD}" \
  --flag-cols 5 >/dev/null || true

echo "[6/7] Wrote:"
echo "  ${OUT_DIR}/report.txt"
echo "  ${OUT_DIR}/manifest.json"
echo "  ${OUT_DIR}/pdf/"
echo "  ${OUT_DIR}/epub/"
echo "  ${OUT_DIR}/pdf_vs_epub_apple/manifest.json"
echo "  ${OUT_DIR}/epub_image_quality.md"
echo "  ${OUT_DIR}/epub_layout_audit_1000w.md"
echo "  ${OUT_DIR}/epub_table_audit.md"

echo "[7/7] Done."
