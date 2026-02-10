#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "${ROOT_DIR}"

echo "[1/10] Building print/PDF (tectonic)…"
tectonic -X compile --pass default --reruns 2 --keep-intermediates --keep-logs ece657_notes.tex >/dev/null

echo "[2/10] Checking citations/BibTeX hygiene…"
/usr/bin/python3 scripts/check_citations.py

echo "[3/10] Checking cross-reference/label hygiene…"
/usr/bin/python3 scripts/check_crossrefs.py

echo "[4/10] Auditing chapter template consistency…"
/usr/bin/python3 scripts/chapter_format_audit.py --write

echo "[5/10] Checking equation hygiene…"
/usr/bin/python3 scripts/check_equations.py

if [[ "${ALLOW_TEX_WARNINGS:-}" != "1" ]]; then
  echo "[6/10] Enforcing camera-ready TeX warning gate…"
  /usr/bin/python3 scripts/check_build_warnings.py --log ece657_notes.log --max-overfull-pt "${MAX_OVERFULL_PT:-3.0}"
else
  echo "[6/10] Skipping TeX warning gate (ALLOW_TEX_WARNINGS=1)."
fi

if [[ "${ALLOW_REF_COVERAGE_GAPS:-}" != "1" ]]; then
  if [[ "${STRICT_REF_ORDER:-}" == "1" ]]; then
    echo "[7/10] Auditing figure/table reference coverage (strict-order)…"
    /usr/bin/python3 scripts/check_ref_coverage.py --root "${ROOT_DIR}" --strict-order
  else
    echo "[7/10] Auditing figure/table reference coverage…"
    /usr/bin/python3 scripts/check_ref_coverage.py --root "${ROOT_DIR}"
  fi
else
  echo "[7/10] Auditing figure/table reference coverage (non-blocking)…"
  /usr/bin/python3 scripts/check_ref_coverage.py --root "${ROOT_DIR}" || true
fi

echo "[8/10] Running bibliography style policy audit…"
/usr/bin/python3 scripts/check_bib_style.py --bib refs.bib

echo "[9/10] Running automated publishing QC…"
/usr/bin/python3 scripts/publish_qc.py \
  --root "${ROOT_DIR}" \
  --pdf ece657_notes.pdf \
  --log ece657_notes.log \
  --style editorial_style.toml \
  --out artifacts/qc/publish_qc_report.md || true

echo "[10/10] Wrote report:"
echo "  ${ROOT_DIR}/artifacts/qc/publish_qc_report.md"
