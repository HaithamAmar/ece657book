#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "${ROOT_DIR}"

echo "[1/3] Building print/PDF (tectonic)…"
tectonic -X compile --pass default --reruns 2 --keep-intermediates --keep-logs ece657_notes.tex >/dev/null

echo "[2/4] Checking citations/BibTeX hygiene…"
/usr/bin/python3 scripts/check_citations.py

echo "[3/4] Running automated publishing QC…"
/usr/bin/python3 scripts/publish_qc.py \
  --root "${ROOT_DIR}" \
  --pdf ece657_notes.pdf \
  --log ece657_notes.log \
  --style editorial_style.toml \
  --out artifacts/qc/publish_qc_report.md || true

echo "[4/4] Wrote report:"
echo "  ${ROOT_DIR}/artifacts/qc/publish_qc_report.md"
