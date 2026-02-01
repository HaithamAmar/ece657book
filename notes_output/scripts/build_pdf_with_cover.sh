#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT_DIR="${ROOT_DIR}/artifacts/preview"

# For KDP print, the cover is uploaded separately; the interior PDF should not
# include it. This helper generates a separate "with cover" PDF for sharing and
# review, without changing the print interior build.

COVER_IMG="${ROOT_DIR}/BookCover.png"
if [[ ! -f "${COVER_IMG}" ]]; then
  echo "Missing cover image: ${COVER_IMG}" >&2
  exit 1
fi

mkdir -p "${OUT_DIR}"

# Ensure Ghostscript is available (do not rely on hard-coded Homebrew paths).
if ! command -v gs >/dev/null 2>&1; then
  echo "Missing dependency: gs (Ghostscript). Install Ghostscript and ensure 'gs' is on PATH." >&2
  exit 1
fi

# Build (or reuse) the standard interior PDF.
if [[ ! -f "${ROOT_DIR}/ece657_notes.pdf" ]]; then
  echo "Building ece657_notes.pdf ..."
  tectonic -X compile --pass default --reruns 2 --keep-logs ece657_notes.tex >/dev/null
fi

TMP_ROOT="${ROOT_DIR}/artifacts/tmp"
mkdir -p "${TMP_ROOT}"
TMP_DIR="$(mktemp -d "${TMP_ROOT}/build_pdf_with_cover.XXXXXX")"
trap 'rm -rf "${TMP_DIR}"' EXIT

cp -f "${COVER_IMG}" "${TMP_DIR}/BookCover.png"
cat > "${TMP_DIR}/cover_page.tex" <<'TEX'
\documentclass[11pt]{article}
\usepackage[
  paperwidth=7in,
  paperheight=10in,
  margin=0in
]{geometry}
\usepackage{graphicx}
\pagestyle{empty}
\begin{document}
\noindent\includegraphics[width=\paperwidth,height=\paperheight,keepaspectratio]{BookCover.png}
\end{document}
TEX

(
  cd "${TMP_DIR}"
  tectonic -X compile --reruns 0 cover_page.tex >/dev/null
)

gs -dSAFER -dBATCH -dNOPAUSE -sDEVICE=pdfwrite \
  -sOutputFile="${OUT_DIR}/ece657_notes_with_cover.pdf" \
  "${TMP_DIR}/cover_page.pdf" \
  "${ROOT_DIR}/ece657_notes.pdf" \
  >/dev/null

echo "Wrote: ${OUT_DIR}/ece657_notes_with_cover.pdf"
