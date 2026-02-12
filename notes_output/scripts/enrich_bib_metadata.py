#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path


ENTRY_START_RE = re.compile(r"@([A-Za-z]+)\s*\{", re.M)
KEY_RE = re.compile(r"\s*([^,\s]+)\s*,", re.S)
ARXIV_ID_RE = re.compile(r"\b(\d{4}\.\d{4,5}(?:v\d+)?)\b")


@dataclass
class Entry:
    kind: str
    key: str
    fields: dict[str, str]
    start: int
    end: int


def parse_fields(blob: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    i = 0
    n = len(blob)
    while i < n:
        while i < n and blob[i] in " \t\r\n,":
            i += 1
        if i >= n:
            break
        j = i
        while j < n and (blob[j].isalnum() or blob[j] in "_-"):
            j += 1
        name = blob[i:j].lower()
        i = j
        while i < n and blob[i] in " \t\r\n":
            i += 1
        if i >= n or blob[i] != "=":
            while i < n and blob[i] != ",":
                i += 1
            continue
        i += 1
        while i < n and blob[i] in " \t\r\n":
            i += 1
        if i >= n:
            break

        if blob[i] == "{":
            depth = 0
            k = i
            while k < n:
                if blob[k] == "{":
                    depth += 1
                elif blob[k] == "}":
                    depth -= 1
                    if depth == 0:
                        break
                k += 1
            value = blob[i + 1 : k].strip()
            i = k + 1
        elif blob[i] == '"':
            k = i + 1
            while k < n:
                if blob[k] == '"' and blob[k - 1] != "\\":
                    break
                k += 1
            value = blob[i + 1 : k].strip()
            i = k + 1
        else:
            k = i
            while k < n and blob[k] not in ",\n":
                k += 1
            value = blob[i:k].strip()
            i = k
        fields[name] = value
    return fields


def parse_entries(raw: str) -> list[Entry]:
    entries: list[Entry] = []
    idx = 0
    n = len(raw)
    while idx < n:
        m = ENTRY_START_RE.search(raw, idx)
        if not m:
            break
        kind = m.group(1).lower()
        entry_start = m.start()
        start_brace = raw.find("{", m.start())
        depth = 0
        end = start_brace
        while end < n:
            ch = raw[end]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    break
            end += 1
        if end >= n:
            break
        body = raw[start_brace + 1 : end].strip()
        km = KEY_RE.match(body)
        if not km:
            idx = end + 1
            continue
        key = km.group(1).strip()
        fields = parse_fields(body[km.end() :].strip())
        entries.append(Entry(kind=kind, key=key, fields=fields, start=entry_start, end=end + 1))
        idx = end + 1
    return entries


def normalize_title(title: str) -> str:
    t = re.sub(r"\\[a-zA-Z]+\{([^}]*)\}", r"\1", title)
    t = t.replace("{", "").replace("}", "")
    t = t.lower()
    t = re.sub(r"[^a-z0-9 ]+", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def first_author_family(author_field: str) -> str:
    first = author_field.split(" and ")[0].strip()
    first = first.replace("{", "").replace("}", "")
    if "," in first:
        fam = first.split(",")[0].strip().lower()
    else:
        fam = first.split()[-1].strip().lower() if first.split() else ""
    return re.sub(r"[^a-z\-]", "", fam)


def request_json(url: str, timeout: float = 20.0) -> dict:
    with urllib.request.urlopen(url, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8", errors="ignore"))


def lookup_crossref_doi(title: str, author: str, year: str) -> tuple[str | None, float, str]:
    query = f"{title} {author} {year}".strip()
    url = (
        "https://api.crossref.org/works?"
        + urllib.parse.urlencode(
            {
                "query.bibliographic": query,
                "rows": 8,
                "select": "DOI,title,author,issued,published-print,published-online",
            }
        )
    )
    data = request_json(url)
    items = data.get("message", {}).get("items", [])
    if not items:
        return None, 0.0, "no-candidates"

    target_title = normalize_title(title)
    target_author = first_author_family(author)
    try:
        target_year = int(year)
    except Exception:
        target_year = None

    best_doi = None
    best_score = 0.0
    best_reason = "low-confidence"

    for item in items:
        doi = item.get("DOI")
        c_title = " ".join(item.get("title", [])) if isinstance(item.get("title"), list) else ""
        c_title_n = normalize_title(c_title)
        sim = SequenceMatcher(None, target_title, c_title_n).ratio()

        author_match = 0.0
        cand_authors = item.get("author", []) or []
        cand_fams = {str(a.get("family", "")).lower() for a in cand_authors if isinstance(a, dict)}
        if target_author and target_author in cand_fams:
            author_match = 0.1

        year_match = 0.0
        year_src = item.get("issued") or item.get("published-print") or item.get("published-online") or {}
        year_parts = year_src.get("date-parts", [[]])
        cand_year = None
        if year_parts and year_parts[0]:
            try:
                cand_year = int(year_parts[0][0])
            except Exception:
                cand_year = None
        if target_year and cand_year:
            if cand_year == target_year:
                year_match = 0.1
            elif abs(cand_year - target_year) == 1:
                year_match = 0.05

        score = sim + author_match + year_match
        if score > best_score and doi:
            best_score = score
            best_doi = doi
            best_reason = f"sim={sim:.3f},author={author_match:.2f},year={year_match:.2f}"

    if best_doi and best_score >= 0.88:
        return best_doi, best_score, best_reason
    return None, best_score, best_reason


def list_crossref_candidates(title: str, author: str, year: str, rows: int = 8) -> list[dict[str, str]]:
    query = f"{title} {author} {year}".strip()
    url = (
        "https://api.crossref.org/works?"
        + urllib.parse.urlencode(
            {
                "query.bibliographic": query,
                "rows": rows,
                "select": "DOI,title,author,issued,published-print,published-online,container-title,type",
            }
        )
    )
    data = request_json(url)
    items = data.get("message", {}).get("items", [])
    target_title = normalize_title(title)
    target_author = first_author_family(author)
    out: list[dict[str, str]] = []
    for item in items:
        c_title = " ".join(item.get("title", [])) if isinstance(item.get("title"), list) else ""
        c_title_n = normalize_title(c_title)
        sim = SequenceMatcher(None, target_title, c_title_n).ratio()
        cand_authors = item.get("author", []) or []
        cand_fams = {str(a.get("family", "")).lower() for a in cand_authors if isinstance(a, dict)}
        author_match = "yes" if target_author and target_author in cand_fams else "no"
        year_src = item.get("issued") or item.get("published-print") or item.get("published-online") or {}
        year_parts = year_src.get("date-parts", [[]])
        cand_year = ""
        if year_parts and year_parts[0]:
            cand_year = str(year_parts[0][0])
        container = " ".join(item.get("container-title", [])) if isinstance(item.get("container-title"), list) else ""
        out.append(
            {
                "doi": str(item.get("DOI", "")),
                "title": c_title,
                "sim": f"{sim:.3f}",
                "author_match": author_match,
                "year": cand_year,
                "type": str(item.get("type", "")),
                "container": container,
            }
        )
    return out


def lookup_arxiv_id(title: str, author: str, year: str) -> tuple[str | None, float, str]:
    query = f'ti:"{title}"'
    url = "http://export.arxiv.org/api/query?" + urllib.parse.urlencode({"search_query": query, "start": 0, "max_results": 5})
    try:
        with urllib.request.urlopen(url, timeout=20.0) as resp:
            xml_text = resp.read().decode("utf-8", errors="ignore")
    except Exception:
        return None, 0.0, "arxiv-network-error"

    ns = {"a": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(xml_text)
    entries = root.findall("a:entry", ns)
    if not entries:
        return None, 0.0, "no-arxiv-candidates"

    target_title = normalize_title(title)
    best_id = None
    best_score = 0.0
    for e in entries:
        tnode = e.find("a:title", ns)
        inode = e.find("a:id", ns)
        if tnode is None or inode is None:
            continue
        cand_title = normalize_title(tnode.text or "")
        sim = SequenceMatcher(None, target_title, cand_title).ratio()
        id_match = ARXIV_ID_RE.search(inode.text or "")
        if sim > best_score and id_match:
            best_score = sim
            best_id = id_match.group(1)
    if best_id and best_score >= 0.92:
        return best_id, best_score, f"sim={best_score:.3f}"
    return None, best_score, "low-confidence"


def audit_existing_dois(entries: list[Entry], min_similarity: float) -> list[tuple[str, str, str, float, str]]:
    flagged: list[tuple[str, str, str, float, str]] = []
    for e in entries:
        doi = (e.fields.get("doi") or "").strip()
        if not doi:
            continue
        title = (e.fields.get("title") or "").strip()
        if not title:
            continue
        try:
            url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
            data = request_json(url)
            item = data.get("message", {})
            c_title = " ".join(item.get("title", [])) if isinstance(item.get("title"), list) else ""
            sim = SequenceMatcher(None, normalize_title(title), normalize_title(c_title)).ratio()

            reasons: list[str] = []
            title_ok_by_containment = False
            target_title_n = normalize_title(title)
            crossref_title_n = normalize_title(c_title)
            if target_title_n and crossref_title_n:
                title_ok_by_containment = (
                    target_title_n in crossref_title_n or crossref_title_n in target_title_n
                )
            if sim < min_similarity and not title_ok_by_containment:
                reasons.append("title-sim")

            author_field = (e.fields.get("author") or "").strip()
            target_author = first_author_family(author_field)
            cand_authors = item.get("author", []) or []
            cand_fams = {str(a.get("family", "")).lower() for a in cand_authors if isinstance(a, dict)}
            if target_author and target_author not in cand_fams:
                reasons.append("author-mismatch")

            year_field = (e.fields.get("year") or "").strip()
            target_year = None
            try:
                target_year = int(year_field)
            except Exception:
                target_year = None

            year_src = item.get("issued") or item.get("published-print") or item.get("published-online") or {}
            year_parts = year_src.get("date-parts", [[]])
            cand_year = None
            if year_parts and year_parts[0]:
                try:
                    cand_year = int(year_parts[0][0])
                except Exception:
                    cand_year = None
            if target_year and cand_year and abs(target_year - cand_year) > 1:
                reasons.append(f"year-mismatch:{target_year}!={cand_year}")

            if reasons:
                flagged.append((e.key, doi, c_title, sim, ",".join(reasons)))
        except Exception:
            continue
    return flagged


def set_or_add_field(block: str, field: str, value: str) -> str:
    field_re = re.compile(rf"(^\s*{re.escape(field)}\s*=\s*)\{{[^}}]*\}}(\s*,?\s*$)", re.M)
    if field_re.search(block):
        return field_re.sub(rf"\1{{{value}}}\2", block)
    close_idx = block.rfind("}")
    prefix = block[:close_idx].rstrip()
    lines = prefix.splitlines()
    if lines and "=" in lines[-1] and not lines[-1].rstrip().endswith(","):
        lines[-1] = lines[-1].rstrip() + ","
    prefix = "\n".join(lines)
    return prefix + f"\n  {field:<12}= {{{value}}},\n" + block[close_idx:]


def main() -> int:
    parser = argparse.ArgumentParser(description="Enrich missing DOI/arXiv metadata in refs.bib")
    parser.add_argument("--bib", default="notes_output/refs.bib")
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--sleep", type=float, default=0.3, help="Delay between API queries")
    parser.add_argument("--limit", type=int, default=999, help="Max entries to process")
    parser.add_argument(
        "--audit-doi",
        action="store_true",
        help="Audit existing DOI fields against Crossref title similarity and write a mismatch report",
    )
    parser.add_argument(
        "--audit-threshold",
        type=float,
        default=0.90,
        help="Minimum normalized title similarity for DOI audit (default: 0.90)",
    )
    parser.add_argument(
        "--inspect-key",
        default="",
        help="Inspect one BibTeX key and print Crossref candidate DOIs without writing changes",
    )
    parser.add_argument(
        "--report",
        default="notes_output/artifacts/qc/bib_metadata_enrichment_report.md",
    )
    args = parser.parse_args()

    bib_path = Path(args.bib).resolve()
    raw = bib_path.read_text(encoding="utf-8", errors="ignore")
    entries = parse_entries(raw)

    if args.inspect_key:
        target = None
        for e in entries:
            if e.key == args.inspect_key:
                target = e
                break
        if target is None:
            print(f"missing-key={args.inspect_key}")
            return 2
        title = (target.fields.get("title") or "").strip()
        author = (target.fields.get("author") or "").strip()
        year = (target.fields.get("year") or "").strip()
        cands = list_crossref_candidates(title, author, year)
        print(f"key={target.key}")
        print(f"title={title}")
        print(f"year={year}")
        print("candidates:")
        for index, item in enumerate(cands, start=1):
            print(
                f"  {index}. doi={item['doi']} sim={item['sim']} "
                f"author_match={item['author_match']} year={item['year']} type={item['type']} "
                f"title={item['title']}"
            )
        return 0

    if args.audit_doi:
        flagged = audit_existing_dois(entries, min_similarity=args.audit_threshold)
        report_path = Path(args.report).resolve()
        report_path.parent.mkdir(parents=True, exist_ok=True)
        lines: list[str] = []
        lines.append("# Bibliography DOI Audit Report")
        lines.append("")
        lines.append(f"- Entries scanned: `{len(entries)}`")
        lines.append(f"- Threshold: `{args.audit_threshold:.2f}`")
        lines.append(f"- Flagged DOI entries: `{len(flagged)}`")
        lines.append("")
        if flagged:
            lines.append("## Flagged")
            lines.append("")
            for key, doi, c_title, sim, reason in flagged:
                lines.append(f"- `{key}` doi=`{doi}` sim={sim:.3f} reason=`{reason}` crossref_title=`{c_title}`")
            lines.append("")
        report_path.write_text("\n".join(lines), encoding="utf-8")
        print(f"flagged={len(flagged)}")
        print(f"report={report_path}")
        return 0

    targets = [
        e
        for e in entries
        if e.kind in {"article", "inproceedings", "misc"}
        and not (e.fields.get("doi") or "").strip()
        and not (e.fields.get("eprint") or "").strip()
    ][: args.limit]

    updates: dict[str, dict[str, str]] = {}
    unresolved: list[tuple[str, str]] = []
    diagnostics: list[tuple[str, str, str]] = []

    for e in targets:
        title = e.fields.get("title", "")
        author = e.fields.get("author", "")
        year = e.fields.get("year", "")
        doi, score, reason = lookup_crossref_doi(title, author, year)
        if doi:
            updates[e.key] = {"doi": doi}
            diagnostics.append((e.key, "doi", f"{doi} ({score:.3f}; {reason})"))
            time.sleep(args.sleep)
            continue
        arxiv_id, a_score, a_reason = lookup_arxiv_id(title, author, year)
        if arxiv_id:
            updates[e.key] = {"eprint": arxiv_id, "archivePrefix": "arXiv"}
            diagnostics.append((e.key, "arxiv", f"{arxiv_id} ({a_score:.3f}; {a_reason})"))
        else:
            unresolved.append((e.key, f"crossref={score:.3f}({reason}); arxiv={a_score:.3f}({a_reason})"))
        time.sleep(args.sleep)

    if args.write and updates:
        rebuilt: list[str] = []
        cursor = 0
        for e in entries:
            rebuilt.append(raw[cursor : e.start])
            block = raw[e.start : e.end]
            if e.key in updates:
                for field, value in updates[e.key].items():
                    block = set_or_add_field(block, field, value)
            rebuilt.append(block)
            cursor = e.end
        rebuilt.append(raw[cursor:])
        raw = "".join(rebuilt)
        bib_path.write_text(raw, encoding="utf-8")

    report_path = Path(args.report).resolve()
    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    lines.append("# Bibliography Metadata Enrichment Report")
    lines.append("")
    lines.append(f"- Targets scanned: `{len(targets)}`")
    lines.append(f"- Enriched entries: `{len(updates)}`")
    lines.append(f"- Unresolved entries: `{len(unresolved)}`")
    lines.append("")
    lines.append("## Enriched")
    lines.append("")
    for key, mode, info in diagnostics:
        lines.append(f"- `{key}` ({mode}): {info}")
    lines.append("")
    lines.append("## Unresolved")
    lines.append("")
    for key, info in unresolved:
        lines.append(f"- `{key}`: {info}")
    lines.append("")
    report_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"targets={len(targets)} enriched={len(updates)} unresolved={len(unresolved)}")
    print(f"report={report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
