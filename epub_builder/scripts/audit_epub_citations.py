#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Offender:
    xhtml: str
    kind: str
    snippet: str


def _strip_tags(s: str) -> str:
    # Simple tag stripper for small inline spans; good enough for audit output.
    return re.sub(r"<[^>]+>", "", s)


def _compact(s: str, *, limit: int = 260) -> str:
    s2 = re.sub(r"\s+", " ", s).strip()
    if len(s2) <= limit:
        return s2
    return s2[: limit - 1] + "…"


def audit_epub(epub_path: Path, *, max_offenders: int) -> int:
    if not epub_path.exists():
        print(f"Missing EPUB: {epub_path}", file=sys.stderr)
        return 2

    offenders: list[Offender] = []
    citation_span_re = re.compile(r'<span class="citation"[^>]*>(.*?)</span>', re.S)

    total_citation_spans = 0
    empty_citation_spans = 0
    inspired_by_dot = 0

    with zipfile.ZipFile(epub_path) as z:
        xhtml_files = [
            n
            for n in z.namelist()
            if n.endswith(".xhtml") and ("/EPUB/text/" in n or n.startswith("EPUB/text/"))
        ]
        for name in sorted(xhtml_files):
            raw = z.read(name).decode("utf-8", errors="ignore")

            # 1) Empty citation spans: classic failure mode when citeproc is not applied.
            for m in citation_span_re.finditer(raw):
                total_citation_spans += 1
                inner = _strip_tags(m.group(1))
                if re.sub(r"\s+", "", inner) == "":
                    empty_citation_spans += 1
                    start = max(0, m.start() - 140)
                    end = min(len(raw), m.end() + 140)
                    offenders.append(
                        Offender(
                            xhtml=name,
                            kind="empty_citation_span",
                            snippet=_compact(raw[start:end]),
                        )
                    )

            # 2) Known symptom string: "inspired by ." (usually a blank cite in a caption).
            if "inspired by ." in raw:
                inspired_by_dot += raw.count("inspired by .")
                # Record one representative snippet per file.
                idx = raw.find("inspired by .")
                start = max(0, idx - 140)
                end = min(len(raw), idx + 140)
                offenders.append(
                    Offender(
                        xhtml=name,
                        kind="inspired_by_dot",
                        snippet=_compact(raw[start:end]),
                    )
                )

    blocking = (empty_citation_spans > 0) or (inspired_by_dot > 0)
    status = "FAIL" if blocking else "OK"

    print(f"Citation audit ({epub_path.name}): {status}")
    print(f"  citation_spans_total: {total_citation_spans}")
    print(f"  citation_spans_empty: {empty_citation_spans}")
    print(f"  inspired_by_dot_hits: {inspired_by_dot}")

    if blocking:
        print("")
        print(f"Top offenders (up to {max_offenders}):")
        for off in offenders[:max_offenders]:
            print(f"- {off.kind}: {off.xhtml}")
            print(f"  {off.snippet}")
        return 2

    return 0


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--epub", required=True, type=Path)
    ap.add_argument("--max-offenders", type=int, default=10)
    args = ap.parse_args(argv)
    return audit_epub(args.epub, max_offenders=int(args.max_offenders))


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

