#!/usr/bin/env python3
from __future__ import annotations

import argparse
import fnmatch
import os
import re
import subprocess
import sys
import ast
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def _which(cmd: str) -> str | None:
    for p in os.environ.get("PATH", "").split(os.pathsep):
        cand = Path(p) / cmd
        if cand.exists() and os.access(str(cand), os.X_OK):
            return str(cand)
    return None


def _run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)


def _parse_toml_list(value: str) -> list[str]:
    try:
        parsed = ast.literal_eval(value)
        if isinstance(parsed, list):
            return [str(x) for x in parsed]
    except Exception:
        pass
    return []


def _load_style_config(path: Path) -> dict:
    raw = _read_text(path)
    style: dict = {"spelling": [], "lint": {"include_globs": [], "exclude_globs": []}}
    current_section: str | None = None
    current_spelling: dict | None = None

    lines = raw.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        line = line.split("#", 1)[0].strip()
        if not line:
            i += 1
            continue
        if line == "[lint]":
            current_section = "lint"
            current_spelling = None
            i += 1
            continue
        if line == "[[spelling]]":
            current_section = "spelling"
            current_spelling = {}
            style["spelling"].append(current_spelling)
            i += 1
            continue

        if "=" not in line:
            i += 1
            continue
        key, value = [x.strip() for x in line.split("=", 1)]
        if value.startswith("[") and not value.rstrip().endswith("]"):
            buf = [value]
            j = i + 1
            while j < len(lines):
                nxt = lines[j].split("#", 1)[0].strip()
                buf.append(nxt)
                if nxt.endswith("]"):
                    break
                j += 1
            value = " ".join(buf)
            i = j

        if current_section == "lint":
            if key in ("include_globs", "exclude_globs"):
                style["lint"][key] = _parse_toml_list(value)
            i += 1
            continue

        if current_section == "spelling" and current_spelling is not None:
            if key == "name" and value.startswith('"') and value.endswith('"'):
                current_spelling["name"] = value[1:-1]
            if key in ("variants", "preferred"):
                current_spelling[key] = _parse_toml_list(value)

        i += 1
    return style


def _iter_files(root: Path, include_globs: list[str], exclude_globs: list[str]) -> Iterable[Path]:
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()
        if any(fnmatch.fnmatch(rel, g) for g in exclude_globs):
            continue
        if include_globs and not any(fnmatch.fnmatch(rel, g) for g in include_globs):
            continue
        yield path


@dataclass(frozen=True)
class Finding:
    kind: str
    message: str
    path: str | None = None
    line: int | None = None


def _parse_tectonic_log(log_text: str) -> list[Finding]:
    findings: list[Finding] = []
    overfull = re.compile(r"Overfull \\hbox .*? at lines? (\d+)(?:--(\d+))?")
    underfull = re.compile(r"Underfull \\hbox .*? at lines? (\d+)(?:--(\d+))?")
    file_line = re.compile(r"\(([^()\s]+\.tex)")
    current_file: str | None = None

    for raw in log_text.splitlines():
        m_file = file_line.search(raw)
        if m_file:
            current_file = m_file.group(1)
        m = overfull.search(raw)
        if m:
            findings.append(
                Finding(
                    kind="overfull_hbox",
                    message=raw.strip(),
                    path=current_file,
                    line=int(m.group(1)),
                )
            )
            continue
        m = underfull.search(raw)
        if m:
            findings.append(
                Finding(
                    kind="underfull_hbox",
                    message=raw.strip(),
                    path=current_file,
                    line=int(m.group(1)),
                )
            )
            continue
        if "LaTeX Warning:" in raw or "Package" in raw and "Warning:" in raw:
            findings.append(Finding(kind="latex_warning", message=raw.strip(), path=current_file))
    return findings


def _scan_pdf_text_for_toc_anomalies(pdf_text: str) -> list[Finding]:
    findings: list[Finding] = []
    lines = [ln.rstrip("\n") for ln in pdf_text.splitlines()]
    # Examples from screenshots:
    # - "19.25Pseudocode Representation" (missing space after numbering)
    # - "... Parameter Sharing233" (page number glued to title)
    missing_space = re.compile(r"\\b\\d+(?:\\.\\d+)+[A-Za-z]")
    glued_page = re.compile(r"[A-Za-z)]\\d{2,4}\\b")

    for idx, ln in enumerate(lines, start=1):
        if not ln.strip():
            continue
        if missing_space.search(ln):
            findings.append(Finding(kind="toc_spacing", message=ln.strip(), line=idx))
        if glued_page.search(ln) and "Figure" not in ln and "Table" not in ln:
            # Ignore legitimate math-like tokens by requiring some dotted-leader context.
            if " . " in ln or "..." in ln or "·" in ln:
                findings.append(Finding(kind="toc_page_glue", message=ln.strip(), line=idx))
    return findings


def _scan_files_for_whitespace(files: Iterable[Path], root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for path in files:
        rel = path.relative_to(root).as_posix()
        text = _read_text(path)
        for i, line in enumerate(text.splitlines(), start=1):
            if "\t" in line:
                findings.append(Finding(kind="tab_char", message="Tab character", path=rel, line=i))
            if line.rstrip("\n") != line.rstrip():
                findings.append(Finding(kind="trailing_ws", message="Trailing whitespace", path=rel, line=i))
    return findings


def _scan_files_for_dash_style(files: Iterable[Path], root: Path) -> list[Finding]:
    findings: list[Finding] = []
    # Flag " - " in prose; allow in itemize labels like `\item -` or in ranges like `x - y` in math.
    suspect = re.compile(r"\\s-\\s")
    for path in files:
        if path.suffix.lower() != ".tex":
            continue
        rel = path.relative_to(root).as_posix()
        text = _read_text(path)
        for i, line in enumerate(text.splitlines(), start=1):
            if "\\item" in line:
                continue
            if "$" in line:
                continue
            if suspect.search(line):
                findings.append(Finding(kind="dash_style", message=line.strip(), path=rel, line=i))
    return findings


def _scan_files_for_spelling(files: Iterable[Path], root: Path, style: dict) -> list[Finding]:
    groups = (style.get("spelling") or []) if isinstance(style, dict) else []
    if not groups:
        return []
    findings: list[Finding] = []
    word_re = re.compile(r"[A-Za-z][A-Za-z']+")
    cmd_re = re.compile(r"\\[A-Za-z@]+\\*?")
    corpus: dict[str, int] = {}
    for path in files:
        if path.suffix.lower() != ".tex":
            continue
        text = _read_text(path)
        # Drop verbatim blocks to avoid counting code identifiers as prose.
        text = re.sub(r"\\begin\{verbatim\}.*?\\end\{verbatim\}", " ", text, flags=re.DOTALL)
        # Drop common non-prose arguments (labels, refs, cites, URLs) so keys don't trigger spelling checks.
        text = re.sub(
            r"\\(?:label|ref|pageref|cref|Cref|crefrange|Crefrange|cite|citet|citep|Cite|Citep|url)\{[^}]*\}",
            " ",
            text,
        )
        # Drop inline math ($...$) best-effort.
        text = re.sub(r"\$(?:\\.|[^$\\])+\$", " ", text)
        # Remove TeX command names but keep their arguments (so section titles still count).
        text = cmd_re.sub(" ", text)
        for w in word_re.findall(text):
            corpus[w.lower()] = corpus.get(w.lower(), 0) + 1

    for group in groups:
        if not isinstance(group, dict):
            continue
        name = str(group.get("name", "group"))
        variants = [str(v).lower() for v in (group.get("variants") or [])]
        preferred = {str(v).lower() for v in (group.get("preferred") or [])}
        present = [(v, corpus.get(v, 0)) for v in variants if corpus.get(v, 0)]
        nonpreferred = [(v, c) for v, c in present if v not in preferred]
        if not nonpreferred:
            continue
        msg = f"Non-preferred spelling group '{name}': " + ", ".join(f"{v}={c}" for v, c in nonpreferred)
        findings.append(Finding(kind="spelling_nonpreferred", message=msg))
    return findings


def _write_report(out_path: Path, findings: list[Finding], meta: dict) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)

    def fline(f: Finding) -> str:
        loc = ""
        if f.path:
            loc = f"{f.path}"
            if f.line:
                loc += f":{f.line}"
            loc = f"`{loc}`: "
        elif f.line:
            loc = f"line {f.line}: "
        return f"- `{f.kind}`: {loc}{f.message}"

    parts: list[str] = []
    parts.append("# Publishing QC report\n")
    parts.append("## Inputs\n")
    for k, v in meta.items():
        parts.append(f"- `{k}`: `{v}`")
    parts.append("")

    if not findings:
        parts.append("## Findings\n")
        parts.append("- No issues detected by automated checks.")
        parts.append("")
        out_path.write_text("\n".join(parts), encoding="utf-8")
        return

    by_kind: dict[str, list[Finding]] = {}
    for f in findings:
        by_kind.setdefault(f.kind, []).append(f)

    parts.append("## Findings\n")
    for kind in sorted(by_kind.keys()):
        parts.append(f"### {kind}\n")
        for f in by_kind[kind][:50]:
            parts.append(fline(f))
        extra = len(by_kind[kind]) - 50
        if extra > 0:
            parts.append(f"- (… {extra} more)")
        parts.append("")

    parts.append("## Suggested next actions\n")
    parts.append("- Fix TOC/LOF/LOT spacing by adjusting widths in `ece657_notes.tex` if `toc_spacing`/`toc_page_glue` appear.")
    parts.append("- Fix table layout by revisiting `tabularx`/column widths and avoiding overly long unbreakable tokens; prioritize `overfull_hbox` entries.")
    parts.append("- Decide and enforce a single dialect via `editorial_style.toml` if `spelling_*` items appear.")
    parts.append("- Re-run this script after each batch of edits.")
    parts.append("")

    out_path.write_text("\n".join(parts), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Automated editorial/publishing QC checks.")
    parser.add_argument("--root", default=".", help="notes_output root directory")
    parser.add_argument("--pdf", default="ece657_notes.pdf", help="PDF to scan (optional)")
    parser.add_argument("--log", default="ece657_notes.log", help="Tectonic log to scan (optional)")
    parser.add_argument("--style", default="editorial_style.toml", help="Editorial style config (TOML)")
    parser.add_argument(
        "--out",
        default="artifacts/qc/publish_qc_report.md",
        help="Report output path (relative to --root)",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    style_path = (root / args.style).resolve()
    style = _load_style_config(style_path)

    include_globs = []
    exclude_globs = []
    lint_cfg = style.get("lint") if isinstance(style, dict) else None
    if isinstance(lint_cfg, dict):
        include_globs = [str(x) for x in (lint_cfg.get("include_globs") or [])]
        exclude_globs = [str(x) for x in (lint_cfg.get("exclude_globs") or [])]

    files = list(_iter_files(root, include_globs, exclude_globs))

    findings: list[Finding] = []

    log_path = root / args.log
    if log_path.exists():
        findings.extend(_parse_tectonic_log(_read_text(log_path)))

    pdf_path = root / args.pdf
    if pdf_path.exists() and _which("pdftotext"):
        proc = _run(["pdftotext", str(pdf_path), "-"])
        if proc.returncode == 0:
            findings.extend(_scan_pdf_text_for_toc_anomalies(proc.stdout))
        else:
            findings.append(Finding(kind="pdftotext_error", message=proc.stderr.strip()[:500]))

    findings.extend(_scan_files_for_whitespace(files, root))
    findings.extend(_scan_files_for_dash_style(files, root))
    findings.extend(_scan_files_for_spelling(files, root, style))

    out_path = root / args.out
    meta = {
        "root": root,
        "pdf": pdf_path if pdf_path.exists() else "(missing)",
        "log": log_path if log_path.exists() else "(missing)",
        "style": style_path if style_path.exists() else "(missing or unreadable TOML)",
        "file_count": len(files),
    }
    _write_report(out_path, findings, meta)

    # Return non-zero if there are high-severity items.
    high = {"overfull_hbox", "toc_page_glue", "toc_spacing", "spelling_nonpreferred"}
    if any(f.kind in high for f in findings):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
