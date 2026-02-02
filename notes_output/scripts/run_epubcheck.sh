#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

OUT_DIR="${ROOT_DIR}/artifacts/epubcheck"
EPUBS=()

usage() {
  cat <<'EOF'
Usage:
  bash notes_output/scripts/run_epubcheck.sh [--out DIR] [EPUB ...]

Defaults:
  - If no EPUBs are provided, checks:
      notes_output/artifacts/ebook/ece657_ebook_kindle.epub
      notes_output/artifacts/ebook/ece657_ebook_apple.epub
  - Output directory: notes_output/artifacts/epubcheck

EPUBCheck discovery:
  1) Use `epubcheck` if present on PATH
  2) Else use a jar at:
       $EPUBCHECK_JAR
       notes_output/tools/epubcheck/epubcheck.jar
       notes_output/tools/epubcheck/epubcheck-*.jar
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    -h|--help)
      usage
      exit 0
      ;;
    --out)
      OUT_DIR="$2"
      shift 2
      ;;
    --out=*)
      OUT_DIR="${1#--out=}"
      shift 1
      ;;
    -*)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
    *)
      EPUBS+=("$1")
      shift 1
      ;;
  esac
done

if [[ ${#EPUBS[@]} -eq 0 ]]; then
  # Default to the Pandoc-based builder outputs (repo-root /epub_builder/dist).
  REPO_ROOT="$(cd "${ROOT_DIR}/.." && pwd)"
  EPUBS+=("${REPO_ROOT}/epub_builder/dist/ece657_ebook_kindle.epub")
  EPUBS+=("${REPO_ROOT}/epub_builder/dist/ece657_ebook_apple.epub")
fi

mkdir -p "${OUT_DIR}"

EPUBCHECK_CMD=()
if command -v epubcheck >/dev/null 2>&1; then
  EPUBCHECK_CMD=(epubcheck)
else
  JAR_CANDIDATES=()
  if [[ -n "${EPUBCHECK_JAR:-}" ]]; then
    JAR_CANDIDATES+=("${EPUBCHECK_JAR}")
  fi
  JAR_CANDIDATES+=("${ROOT_DIR}/tools/epubcheck/epubcheck.jar")
  if compgen -G "${ROOT_DIR}/tools/epubcheck/epubcheck-*.jar" >/dev/null 2>&1; then
    while IFS= read -r -d '' jar; do
      JAR_CANDIDATES+=("$jar")
    done < <(find "${ROOT_DIR}/tools/epubcheck" -maxdepth 1 -name 'epubcheck-*.jar' -print0 | sort -z)
  fi

  JAR=""
  for cand in "${JAR_CANDIDATES[@]}"; do
    if [[ -f "$cand" ]]; then
      JAR="$cand"
      break
    fi
  done

  if [[ -z "$JAR" ]]; then
    cat <<EOF >&2
EPUBCheck not found.

Install one of:
  - Homebrew: brew install epubcheck
  - Jar: download an EPUBCheck release jar and place it at:
      ${ROOT_DIR}/tools/epubcheck/epubcheck.jar
    (or set EPUBCHECK_JAR=/path/to/epubcheck.jar)
EOF
    exit 2
  fi

  if ! command -v java >/dev/null 2>&1; then
    echo "java not found on PATH (required to run EPUBCheck jar: ${JAR})" >&2
    exit 2
  fi

  EPUBCHECK_CMD=(java -jar "$JAR")
fi

status=0
for epub in "${EPUBS[@]}"; do
  if [[ ! -f "$epub" ]]; then
    echo "Missing EPUB: ${epub}" >&2
    status=2
    continue
  fi
  base="$(basename "$epub")"
  log="${OUT_DIR}/${base%.epub}.epubcheck.txt"
  echo "==> EPUBCheck: ${base}"
  set +e
  "${EPUBCHECK_CMD[@]}" "$epub" >"$log" 2>&1
  rc=$?
  set -e
  if [[ $rc -ne 0 ]]; then
    status=1
    echo "    FAIL (exit ${rc}) — see: ${log}"
  else
    echo "    OK — wrote: ${log}"
  fi
done

exit $status
