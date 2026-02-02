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

echo "[3/4] Generate previews + manifest"
/usr/bin/python3 "${ROOT_DIR}/scripts/generate_previews.py" \
  --pdf "${ROOT_DIR}/ece657_notes.pdf" \
  --epub "${REPO_ROOT}/epub_builder/dist/ece657_ebook_kindle.epub" \
  --out "${OUT_DIR}" \
  --config "${ROOT_DIR}/critical_checks.json" \
  --pdf-dpi 150

echo "[4/4] Wrote:"
echo "  ${OUT_DIR}/report.txt"
echo "  ${OUT_DIR}/manifest.json"
echo "  ${OUT_DIR}/pdf/"
echo "  ${OUT_DIR}/epub/"
