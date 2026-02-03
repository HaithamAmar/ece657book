#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "${ROOT_DIR}"

echo "[1/3] Building print/PDF (tectonic)…"
tectonic -X compile --pass default --reruns 2 --keep-intermediates --keep-logs ece657_notes.tex >/dev/null

echo "[2/5] Checking citations/BibTeX hygiene…"
/usr/bin/python3 scripts/check_citations.py

echo "[3/5] Checking cross-reference/label hygiene…"
/usr/bin/python3 scripts/check_crossrefs.py

echo "[4/7] Auditing chapter template consistency…"
/usr/bin/python3 scripts/chapter_format_audit.py --write

echo "[5/7] Checking equation hygiene…"
/usr/bin/python3 scripts/check_equations.py

echo "[6/7] Running automated publishing QC…"
/usr/bin/python3 scripts/publish_qc.py \
  --root "${ROOT_DIR}" \
  --pdf ece657_notes.pdf \
  --log ece657_notes.log \
  --style editorial_style.toml \
  --out artifacts/qc/publish_qc_report.md || true

echo "[7/7] Wrote report:"
echo "  ${ROOT_DIR}/artifacts/qc/publish_qc_report.md"
