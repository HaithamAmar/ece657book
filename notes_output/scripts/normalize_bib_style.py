#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


VENUE_MAP = {
    "Proceedings of ICLR": "International Conference on Learning Representations (ICLR)",
    "Proc. ICLR": "International Conference on Learning Representations (ICLR)",
    "International Conference on Learning Representations": "International Conference on Learning Representations (ICLR)",
    "Proceedings of NeurIPS": "Advances in Neural Information Processing Systems (NeurIPS)",
    "Advances in Neural Information Processing Systems": "Advances in Neural Information Processing Systems (NeurIPS)",
    "Proceedings of EMNLP": "Conference on Empirical Methods in Natural Language Processing (EMNLP)",
    "EMNLP": "Conference on Empirical Methods in Natural Language Processing (EMNLP)",
    "Proceedings of ACL": "Annual Meeting of the Association for Computational Linguistics (ACL)",
    "ACL": "Annual Meeting of the Association for Computational Linguistics (ACL)",
    "COLING": "International Conference on Computational Linguistics (COLING)",
    "International Conference on Machine Learning": "International Conference on Machine Learning (ICML)",
    "IEEE Conference on Computer Vision and Pattern Recognition": "IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)",
    "Conference of the European Chapter of the Association for Computational Linguistics": "Conference of the European Chapter of the Association for Computational Linguistics (EACL)",
    "Proceedings of NAACL-HLT": "North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT)",
    "Proceedings of the 32nd International Conference on Machine Learning": "International Conference on Machine Learning (ICML)",
    "Proceedings of the 34th International Conference on Machine Learning": "International Conference on Machine Learning (ICML)",
    "Proc. Interspeech": "Interspeech",
    "Proc. Fifth Berkeley Symposium on Mathematical Statistics and Probability": "Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability",
    "JMLR": "Journal of Machine Learning Research",
    "IEEE Trans. Evolutionary Computation": "IEEE Transactions on Evolutionary Computation",
}


def normalize(raw: str) -> tuple[str, dict[str, int]]:
    text = raw
    counts = {"venue": 0, "arxiv": 0, "doi": 0}

    for src, dst in VENUE_MAP.items():
        pattern = re.compile(
            rf"(^\s*(?:journal|booktitle)\s*=\s*)\{{{re.escape(src)}\}}(\s*,\s*$)",
            re.M,
        )
        text, n = pattern.subn(rf"\1{{{dst}}}\2", text)
        counts["venue"] += n

    def repl_preprint(match: re.Match[str]) -> str:
        counts["arxiv"] += 1
        prefix = match.group(1)
        arxiv_id = match.group(2)
        return (
            f"{prefix}{{arXiv preprint}},\n"
            f"  eprint       = {{{arxiv_id}}},\n"
            f"  archivePrefix = {{arXiv}},"
        )

    text = re.sub(
        r"(^\s*(?:journal|booktitle)\s*=\s*)\{arXiv preprint arXiv:([0-9]{4}\.[0-9]{4,5}(?:v[0-9]+)?)\}\s*,\s*$",
        repl_preprint,
        text,
        flags=re.M,
    )

    def repl_note(match: re.Match[str]) -> str:
        counts["arxiv"] += 1
        arxiv_id = match.group(1)
        return f"  eprint       = {{{arxiv_id}}},\n  archivePrefix = {{arXiv}},"

    text = re.sub(
        r"^\s*note\s*=\s*\{arXiv:([0-9]{4}\.[0-9]{4,5}(?:v[0-9]+)?)\}\s*,?\s*$",
        repl_note,
        text,
        flags=re.M,
    )

    def repl_doi(match: re.Match[str]) -> str:
        counts["doi"] += 1
        prefix, doi_raw, suffix = match.group(1), match.group(2), match.group(3)
        cleaned = re.sub(r"^(?:https?://(?:dx\.)?doi\.org/)", "", doi_raw, flags=re.I).rstrip("/")
        return f"{prefix}{cleaned}{suffix}"

    text = re.sub(r"(^\s*doi\s*=\s*\{)([^}]+)(\}\s*,?\s*$)", repl_doi, text, flags=re.M)
    return text, counts


def main() -> int:
    parser = argparse.ArgumentParser(description="Safe BibTeX normalization pass.")
    parser.add_argument("--bib", default="notes_output/refs.bib", help="BibTeX file path")
    parser.add_argument("--write", action="store_true", help="Write normalized content to disk")
    args = parser.parse_args()

    path = Path(args.bib).resolve()
    raw = path.read_text(encoding="utf-8", errors="ignore")
    normalized, counts = normalize(raw)
    print(
        f"venue_changes={counts['venue']} "
        f"arxiv_changes={counts['arxiv']} "
        f"doi_changes={counts['doi']}"
    )
    if args.write and normalized != raw:
        path.write_text(normalized, encoding="utf-8")
        print(f"updated={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
