from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TikzBlock:
    start: int
    end: int
    content: str


_INPUT_RE = re.compile(r"\\(input|include)\{([^}]+)\}")


def _resolve_input(target: str, *, root_dir: Path) -> Path:
    name = target.strip()
    if not name.endswith(".tex"):
        name += ".tex"
    p = (root_dir / name).resolve()
    if p.exists():
        return p
    # Allow nested relative paths (as written) from the root_dir.
    p2 = (root_dir / target).with_suffix(".tex")
    if p2.exists():
        return p2.resolve()
    raise FileNotFoundError(f"Missing input file for \\input{{{target}}} under {root_dir}")


def flatten_latex_inputs(entry_tex: Path, *, root_dir: Path) -> str:
    seen: set[Path] = set()

    def _read(path: Path) -> str:
        path = path.resolve()
        if path in seen:
            return f"\n% [epub_builder] Skipping already-included file: {path.name}\n"
        seen.add(path)
        text = path.read_text(encoding="utf-8")

        def _sub(m: re.Match[str]) -> str:
            target = m.group(2)
            child = _resolve_input(target, root_dir=root_dir)
            return "\n" + _read(child) + "\n"

        return _INPUT_RE.sub(_sub, text)

    return _read(entry_tex)


def select_ifdefined_hcode_branch(text: str) -> str:
    """
    Keep the `\\ifdefined\\HCode ... \\else ... \\fi` "false" (\\else) branch.

    For the Pandoc pipeline we want the normal LaTeX path (as if `\\HCode` is
    *not* defined). The TeX4ht-specific branch often references assets or
    commands that only exist in that toolchain.
    """
    # Line-based implementation: treat \ifdefined\HCode / \else / \fi tokens only
    # when they appear as standalone control lines (ignoring indentation). This
    # avoids confusing TeX conditionals inside macro bodies like:
    #   \gdef<{\ifmmode ... \else ... \fi}
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    stack: list[bool] = []  # True = taking else branch, False = taking ifdefined branch
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("\\ifdefined\\HCode"):
            stack.append(False)
            continue
        if stripped.startswith("\\else") and stack:
            stack[-1] = True
            continue
        if stripped.startswith("\\fi") and stack:
            stack.pop()
            continue
        if all(stack) if stack else True:
            out.append(line)
    return "".join(out)


def strip_document_environment(text: str) -> str:
    m_begin = re.search(r"\\begin\{document\}", text)
    m_end = re.search(r"\\end\{document\}", text)
    if not m_begin or not m_end or m_end.start() <= m_begin.end():
        return text
    return text[m_begin.end() : m_end.start()]


def load_aux_label_numbers(*, aux_path: Path) -> dict[str, str]:
    """
    Parse a LaTeX `.aux` file and return a map of `label -> rendered number`.

    We use this for EPUB cross-reference text (Pandoc does not reliably resolve
    LaTeX `\\eqref{...}` / equation labels into numbered links).
    """
    if not aux_path.exists():
        return {}
    def _normalize(value: str) -> str:
        """
        Normalize `.aux` label values into the visible "number" we want in EPUB.

        Some LaTeX toolchains emit values like `[equation][2][1]1.2`; we want `1.2`.
        """
        v = value.strip()
        if not v:
            return v
        m = re.search(r"\]([A-Za-z0-9.]+)\s*$", v)
        if m:
            return m.group(1).strip()
        return v.strip("()")

    def _is_simple(value: str) -> bool:
        # Accept common numbering styles: 4, 4.2, 4.2.1, A.1, C.3, etc.
        return bool(re.fullmatch(r"[A-Za-z0-9]+(?:\.[A-Za-z0-9]+)*", value))

    out: dict[str, str] = {}
    # Typical forms:
    #   \newlabel{chap:supervised}{{3}{7}{...}{...}{}}
    #   \newlabel{eq:logit_linear}{{(12)}{43}{...}{}{}}
    #   \newlabel{eq:foo}{{2.10}{43}{...}{}{}}
    newlabel_re = re.compile(r"\\newlabel\{([^}]+)\}\{\{([^}]*)\}\{")
    try:
        for line in aux_path.read_text(encoding="utf-8", errors="ignore").splitlines():
            m = newlabel_re.search(line)
            if not m:
                continue
            label = m.group(1).strip()
            value = _normalize(m.group(2))
            if not label or not value:
                continue
            if label not in out:
                out[label] = value
                continue
            # Prefer a simple normalized value over verbose bracketed variants.
            if _is_simple(value) and not _is_simple(out[label]):
                out[label] = value
    except OSError:
        return {}
    return out


def inject_equation_targets(text: str) -> str:
    """
    Pandoc's LaTeX reader often keeps `\\label{...}` inside MathML annotations
    rather than emitting a proper HTML anchor, which breaks equation links.

    Workaround: for each equation-like environment containing `\\label{eq:...}`,
    inject a `\\hypertarget{eq:...}{}` immediately before the environment.
    """
    envs = ["equation", "equation*", "align", "align*", "gather", "gather*", "multline", "multline*", "alignat", "alignat*"]
    out: list[str] = []
    i = 0
    while i < len(text):
        next_pos = -1
        next_env = None
        for env in envs:
            p = text.find(f"\\begin{{{env}}}", i)
            if p != -1 and (next_pos == -1 or p < next_pos):
                next_pos = p
                next_env = env
        if next_pos == -1 or next_env is None:
            out.append(text[i:])
            break
        out.append(text[i:next_pos])
        end_tag = f"\\end{{{next_env}}}"
        end_pos = text.find(end_tag, next_pos)
        if end_pos == -1:
            out.append(text[next_pos:])
            break
        block = text[next_pos : end_pos + len(end_tag)]
        labels = []
        for m in re.finditer(r"\\label\{(eq:[^}]+)\}", block):
            lab = m.group(1).strip()
            if lab and lab not in labels:
                labels.append(lab)
        if labels:
            # Avoid double-injecting when re-running transforms.
            prefix = text[max(0, next_pos - 160) : next_pos]
            for lab in labels:
                if f"\\hypertarget{{{lab}}}{{}}" in prefix:
                    continue
                out.append(f"\\hypertarget{{{lab}}}{{}}\n")
        out.append(block)
        i = end_pos + len(end_tag)
    text = "".join(out)

    # Also handle display-math blocks written as \[ ... \] (common in the manuscript).
    # Important: avoid matching `\\[<len>]` line breaks (common in TikZ/node text and tables).
    out2: list[str] = []
    i = 0
    while True:
        s = text.find("\\[", i)
        if s == -1:
            out2.append(text[i:])
            break
        if s > 0 and text[s - 1] == "\\":  # skip `\\[` (newline + optional spacing)
            out2.append(text[i : s + 2])
            i = s + 2
            continue
        e = text.find("\\]", s + 2)
        if e == -1:
            out2.append(text[i:])
            break
        while e > 0 and text[e - 1] == "\\":  # skip `\\]` (rare, but symmetric guard)
            e = text.find("\\]", e + 2)
            if e == -1:
                break
        if e == -1:
            out2.append(text[i:])
            break
        block = text[s : e + 2]
        labels: list[str] = []
        for m in re.finditer(r"\\label\{(eq:[^}]+)\}", block):
            lab = m.group(1).strip()
            if lab and lab not in labels:
                labels.append(lab)
        out2.append(text[i:s])
        if labels:
            prefix = text[max(0, s - 160) : s]
            for lab in labels:
                if f"\\hypertarget{{{lab}}}{{}}" in prefix:
                    continue
                out2.append(f"\\hypertarget{{{lab}}}{{}}\n")
        out2.append(block)
        i = e + 2
    return "".join(out2)


def _join_refs(labels: list[str]) -> str:
    parts = [f"\\ref{{{lab}}}" for lab in labels]
    if not parts:
        return ""
    if len(parts) == 1:
        return parts[0]
    if len(parts) == 2:
        return parts[0] + " and " + parts[1]
    return ", ".join(parts[:-1]) + ", and " + parts[-1]

def _join_hyper_numbers(labels: list[str], *, aux_numbers: dict[str, str]) -> str:
    """
    Join labels as hyperlinked reference numbers using `.aux` numbering.

    We intentionally avoid `\\ref{...}` because Pandoc will renumber refs based
    on its own counters (often per-chapter), which can diverge from the global
    PDF numbering we want to preserve for publishing.
    """
    # Use \hyperlink{...}{...} (not \hyperref[...]{...}) to avoid introducing
    # `]` into contexts like `tcolorbox` option lists (which are bracket-delimited
    # and parsed by our preprocessors).
    parts = [f"\\hyperlink{{{lab}}}{{{aux_numbers.get(lab, '?')}}}" for lab in labels]
    if not parts:
        return ""
    if len(parts) == 1:
        return parts[0]
    if len(parts) == 2:
        return parts[0] + " and " + parts[1]
    return ", ".join(parts[:-1]) + ", and " + parts[-1]

def _hyperlink_phrase(label: str, phrase: str) -> str:
    # Use \hyperlink{...}{...} (not \hyperref[...]{...}) to avoid introducing
    # `]` into contexts like bracket-delimited option lists (e.g., tcolorbox).
    return f"\\hyperlink{{{label}}}{{{phrase}}}"

def _hyperlink_noun_number(label: str, *, noun: str, aux_numbers: dict[str, str]) -> str:
    return _hyperlink_phrase(label, f"{noun}~{aux_numbers.get(label, '?')}")


def _join_eq_links(labels: list[str], *, aux_numbers: dict[str, str]) -> str:
    # Use \hyperref[...]{} (not \href{#...}{}) because Pandoc's math parser accepts
    # \hyperref inside math environments, while \href with a '#' URL can break
    # MathML conversion.
    parts = [f"\\hyperref[{lab}]{{({aux_numbers.get(lab, '?')})}}" for lab in labels]
    if not parts:
        return ""
    if len(parts) == 1:
        return parts[0]
    if len(parts) == 2:
        return parts[0] + " and " + parts[1]
    return ", ".join(parts[:-1]) + ", and " + parts[-1]


def rewrite_crossrefs(text: str, *, aux_numbers: dict[str, str]) -> str:
    """
    Rewrite common LaTeX cross-reference commands into forms that render well in EPUB.

    - Chapter refs: ensure the word "Chapter" is present.
    - Equation refs: replace `\\eqref{...}` / `\\Cref{eq:...}` with explicit
      hyperlinked numbers using `.aux` data.
    """

    def _rewrite_crefrange(m: re.Match[str]) -> str:
        a = m.group(1).strip()
        b = m.group(2).strip()
        if not a or not b:
            return m.group(0)

        # Pandoc does not understand cleveref's \Crefrange macro and will
        # silently drop it. Rewrite into fixed-number hyperlinks based on the
        # PDF's `.aux` numbering.
        if a.startswith("app:") and b.startswith("app:"):
            na = aux_numbers.get(a, "?")
            nb = aux_numbers.get(b, "?")
            return f"Appendices~\\hyperlink{{{a}}}{{{na}}}–\\hyperlink{{{b}}}{{{nb}}}"
        if a.startswith("chap:") and b.startswith("chap:"):
            na = aux_numbers.get(a, "?")
            nb = aux_numbers.get(b, "?")
            return f"Chapters~\\hyperlink{{{a}}}{{{na}}}–\\hyperlink{{{b}}}{{{nb}}}"
        if a.startswith("sec:") and b.startswith("sec:"):
            na = aux_numbers.get(a, "?")
            nb = aux_numbers.get(b, "?")
            return f"Sections~\\hyperlink{{{a}}}{{{na}}}–\\hyperlink{{{b}}}{{{nb}}}"
        if a.startswith("fig:") and b.startswith("fig:"):
            na = aux_numbers.get(a, "?")
            nb = aux_numbers.get(b, "?")
            return f"Figures~\\hyperlink{{{a}}}{{{na}}}–\\hyperlink{{{b}}}{{{nb}}}"
        if a.startswith("tab:") and b.startswith("tab:"):
            na = aux_numbers.get(a, "?")
            nb = aux_numbers.get(b, "?")
            return f"Tables~\\hyperlink{{{a}}}{{{na}}}–\\hyperlink{{{b}}}{{{nb}}}"
        if a.startswith("eq:") and b.startswith("eq:"):
            na = aux_numbers.get(a, "?")
            nb = aux_numbers.get(b, "?")
            return f"\\hyperref[{a}]{{({na})}}–\\hyperref[{b}]{{({nb})}}"

        # Mixed-type range: fall back to two readable endpoints.
        def _render_one(lab: str) -> str:
            if lab.startswith("chap:"):
                return _hyperlink_noun_number(lab, noun="Chapter", aux_numbers=aux_numbers)
            if lab.startswith("sec:"):
                return _hyperlink_noun_number(lab, noun="Section", aux_numbers=aux_numbers)
            if lab.startswith("fig:"):
                return _hyperlink_noun_number(lab, noun="Figure", aux_numbers=aux_numbers)
            if lab.startswith("tab:"):
                return _hyperlink_noun_number(lab, noun="Table", aux_numbers=aux_numbers)
            if lab.startswith("eq:"):
                return f"\\hyperref[{lab}]{{({aux_numbers.get(lab,'?')})}}"
            return f"\\ref{{{lab}}}"

        return _render_one(a) + "–" + _render_one(b)

    # Handle \Crefrange{...}{...} / \crefrange{...}{...} early (before \Cref),
    # otherwise Pandoc will drop the macro entirely.
    text = re.sub(r"\\[cC]refrange\{([^}]+)\}\{([^}]+)\}", _rewrite_crefrange, text)

    def _rewrite_cref(m: re.Match[str]) -> str:
        raw = m.group(1)
        labels = [s.strip() for s in raw.split(",") if s.strip()]
        if not labels:
            return m.group(0)
        if all(l.startswith("app:") for l in labels):
            if len(labels) == 1:
                # Appendices are lettered in the PDF (A/B/C); keep that in EPUB.
                return _hyperlink_noun_number(labels[0], noun="Appendix", aux_numbers=aux_numbers)
            return "Appendices~" + _join_hyper_numbers(labels, aux_numbers=aux_numbers)
        if all(l.startswith("chap:") for l in labels):
            if len(labels) == 1:
                return _hyperlink_noun_number(labels[0], noun="Chapter", aux_numbers=aux_numbers)
            return "Chapters~" + _join_hyper_numbers(labels, aux_numbers=aux_numbers)
        if all(l.startswith("eq:") for l in labels):
            return _join_eq_links(labels, aux_numbers=aux_numbers)
        if all(l.startswith("fig:") for l in labels):
            if len(labels) == 1:
                return _hyperlink_noun_number(labels[0], noun="Figure", aux_numbers=aux_numbers)
            return "Figures~" + _join_hyper_numbers(labels, aux_numbers=aux_numbers)
        if all(l.startswith("tab:") for l in labels):
            if len(labels) == 1:
                return _hyperlink_noun_number(labels[0], noun="Table", aux_numbers=aux_numbers)
            return "Tables~" + _join_hyper_numbers(labels, aux_numbers=aux_numbers)
        if all(l.startswith("sec:") for l in labels):
            if len(labels) == 1:
                return _hyperlink_noun_number(labels[0], noun="Section", aux_numbers=aux_numbers)
            return "Sections~" + _join_hyper_numbers(labels, aux_numbers=aux_numbers)
        # Mixed types: keep a readable list.
        rendered = []
        for lab in labels:
            if lab.startswith("eq:"):
                rendered.append(f"\\hyperref[{lab}]{{({aux_numbers.get(lab,'?')})}}")
            elif lab.startswith("app:"):
                rendered.append(_hyperlink_noun_number(lab, noun="Appendix", aux_numbers=aux_numbers))
            elif lab.startswith("chap:"):
                rendered.append(_hyperlink_noun_number(lab, noun="Chapter", aux_numbers=aux_numbers))
            elif lab.startswith("fig:"):
                rendered.append(_hyperlink_noun_number(lab, noun="Figure", aux_numbers=aux_numbers))
            elif lab.startswith("tab:"):
                rendered.append(_hyperlink_noun_number(lab, noun="Table", aux_numbers=aux_numbers))
            elif lab.startswith("sec:"):
                rendered.append(_hyperlink_noun_number(lab, noun="Section", aux_numbers=aux_numbers))
            else:
                rendered.append(f"\\ref{{{lab}}}")
        return ", ".join(rendered)

    # Handle \Cref{...} / \cref{...}
    text = re.sub(r"\\[cC]ref\{([^}]+)\}", _rewrite_cref, text)

    # Handle \eqref{eq:...}
    def _rewrite_eqref(m: re.Match[str]) -> str:
        lab = m.group(1).strip()
        if not lab:
            return m.group(0)
        return f"\\hyperref[{lab}]{{({aux_numbers.get(lab, '?')})}}"

    text = re.sub(r"\\eqref\{([^}]+)\}", _rewrite_eqref, text)

    # Handle bare \ref{...} for chapters/equations (avoid double-prefixing).
    ref_re = re.compile(r"\\ref\{([^}]+)\}")
    out: list[str] = []
    last = 0
    for m in ref_re.finditer(text):
        lab = m.group(1).strip()
        start = m.start()
        out.append(text[last:start])
        before = text[max(0, start - 16) : start]
        before_wide = text[max(0, start - 48) : start]
        if lab.startswith("app:"):
            # If prose already says "Appendix", keep only the letter/number as link text.
            if re.search(r"(Appendix|Appendices)[\\s~]*$", before) or ("Appendices" in before_wide) or ("Appendix" in before_wide):
                out.append(_hyperlink_phrase(lab, aux_numbers.get(lab, "?")))
            else:
                out.append(_hyperlink_noun_number(lab, noun="Appendix", aux_numbers=aux_numbers))
        elif lab.startswith("chap:"):
            if re.search(r"(Chapter|Chapters)[\\s~]*$", before) or ("Chapters" in before_wide):
                out.append(_hyperlink_phrase(lab, aux_numbers.get(lab, "?")))
            else:
                out.append(_hyperlink_noun_number(lab, noun="Chapter", aux_numbers=aux_numbers))
        elif lab.startswith("fig:"):
            if re.search(r"(Figure|Figures)[\\s~]*$", before) or ("Figures" in before_wide):
                out.append(_hyperlink_phrase(lab, aux_numbers.get(lab, "?")))
            else:
                out.append(_hyperlink_noun_number(lab, noun="Figure", aux_numbers=aux_numbers))
        elif lab.startswith("tab:"):
            if re.search(r"(Table|Tables)[\\s~]*$", before) or ("Tables" in before_wide):
                out.append(_hyperlink_phrase(lab, aux_numbers.get(lab, "?")))
            else:
                out.append(_hyperlink_noun_number(lab, noun="Table", aux_numbers=aux_numbers))
        elif lab.startswith("sec:"):
            if re.search(r"(Section|Sections)[\\s~]*$", before) or ("Sections" in before_wide):
                out.append(_hyperlink_phrase(lab, aux_numbers.get(lab, "?")))
            else:
                out.append(_hyperlink_noun_number(lab, noun="Section", aux_numbers=aux_numbers))
        elif lab.startswith("eq:"):
            out.append(f"\\hyperref[{lab}]{{({aux_numbers.get(lab,'?')})}}")
        else:
            out.append(m.group(0))
        last = m.end()
    out.append(text[last:])
    return "".join(out)

def extract_tikz_blocks(text: str) -> list[TikzBlock]:
    blocks: list[TikzBlock] = []
    start_pat = r"\begin{tikzpicture}"
    end_pat = r"\end{tikzpicture}"
    i = 0
    while True:
        s = text.find(start_pat, i)
        if s == -1:
            break
        # Find the matching \end{tikzpicture}, accounting for nested tikzpicture
        # environments (e.g., a small legend picture inside a node).
        depth = 1
        j = s + len(start_pat)
        while depth > 0:
            next_start = text.find(start_pat, j)
            next_end = text.find(end_pat, j)
            if next_end == -1:
                # Unbalanced; give up and stop scanning.
                return blocks
            if next_start != -1 and next_start < next_end:
                depth += 1
                j = next_start + len(start_pat)
                continue
            depth -= 1
            j = next_end + len(end_pat)
        e2 = j
        blocks.append(TikzBlock(start=s, end=e2, content=text[s:e2]))
        i = e2
    return blocks


def replace_tikz_blocks_with_images(text: str, rendered: dict[TikzBlock, str | None]) -> str:
    if not rendered:
        return text
    blocks = sorted(rendered.keys(), key=lambda b: b.start)
    out: list[str] = []
    cursor = 0
    for b in blocks:
        out.append(text[cursor : b.start])
        img = rendered[b]
        if img:
            # Insert only the image include. Many TikZ blocks already live inside
            # a surrounding `figure` environment; wrapping another `figure` here can
            # cause Pandoc/EPUB readers to drop the image while keeping the caption.
            out.append(f"\\includegraphics{{{img}}}\n")
        else:
            out.append("\\begin{quote}\n")
            out.append("\\textbf{Figure could not be rendered.}\\\\\n")
            out.append("This TikZ figure failed to compile in the EPUB pipeline. ")
            out.append("Check `epub_builder/artifacts/tikz_logs/` for details.\n")
            out.append("\\end{quote}\n")
        cursor = b.end
    out.append(text[cursor:])
    return "".join(out)


def prefix_chapter_sections(text: str, *, aux_numbers: dict[str, str]) -> str:
    """
    Convert `\\section{Title}\\label{chap:foo}` into `\\section{Chapter N: Title}...`
    using chapter numbers parsed from `ece657_notes.aux`.
    """
    # Regex is too brittle for titles containing nested braces/macros like:
    #   \section{\texorpdfstring{Foo\\bar}{Foo bar}}\label{chap:som}
    # Use a brace-aware scan instead.
    out: list[str] = []
    i = 0
    while i < len(text):
        s = text.find("\\section", i)
        if s == -1:
            out.append(text[i:])
            break
        out.append(text[i:s])
        j = s + len("\\section")
        # Skip starred headings (intentionally unnumbered).
        if j < len(text) and text[j] == "*":
            out.append(text[s : j + 1])
            i = j + 1
            continue
        while j < len(text) and text[j].isspace():
            j += 1
        if j >= len(text) or text[j] != "{":
            out.append("\\section")
            i = s + len("\\section")
            continue
        title_end = _find_matching_brace(text, j)
        if title_end is None:
            out.append(text[s:])
            break
        title = text[j + 1 : title_end].strip()
        k = title_end + 1
        while k < len(text) and text[k].isspace():
            k += 1
        if not text.startswith("\\label{", k):
            # No immediate chapter/appendix label; keep original.
            out.append(text[s:k])
            i = k
            continue
        lab_end = text.find("}", k + len("\\label{"))
        if lab_end == -1:
            out.append(text[s:])
            break
        lab = text[k + len("\\label{") : lab_end].strip()
        if not (lab.startswith("chap:") or lab.startswith("app:")):
            out.append(text[s : lab_end + 1])
            i = lab_end + 1
            continue
        num = aux_numbers.get(lab)
        if not num:
            out.append(text[s : lab_end + 1])
            i = lab_end + 1
            continue

        if lab.startswith("chap:"):
            if title.lower().startswith("chapter "):
                out.append(text[s : lab_end + 1])
            else:
                out.append(f"\\section{{Chapter {num}: {title}}}\\label{{{lab}}}")
        else:
            if title.lower().startswith("appendix "):
                out.append(text[s : lab_end + 1])
            else:
                out.append(f"\\section{{Appendix {num}: {title}}}\\label{{{lab}}}")
        i = lab_end + 1

    return "".join(out)

def number_unlabeled_headings(text: str, *, aux_numbers: dict[str, str]) -> str:
    """
    Ensure subsection/subsubsection numbering is consistent even when headings
    are not labeled.

    Pandoc will not preserve LaTeX counters for unlabeled headings in the way we
    need for a publish-grade EPUB. We therefore apply LaTeX-style counters
    deterministically in preprocessing, but only once we're inside the numbered
    body (after the first `chap:` or `app:` section).
    """

    def _starts_with_number(title: str) -> bool:
        t = title.strip()
        # 4.2, 4.2.1, A.1, C.1.2, etc.
        return bool(re.match(r"^(?:[A-Z]|\d+)(?:\.\d+){1,3}\b", t))

    def _scan_cmd(s: str, start: int, cmd: str) -> tuple[int, int, str, str] | None:
        """
        Return (cmd_start, after_title_end, opt_arg, title) for \\cmd{title}
        handling optional [..] and brace-matched title. Returns None if parsing fails.
        """
        if not s.startswith("\\" + cmd, start):
            return None
        i = start + 1 + len(cmd)
        # starred headings are intentionally unnumbered
        if i < len(s) and s[i] == "*":
            return None
        # skip whitespace
        while i < len(s) and s[i].isspace():
            i += 1
        opt = ""
        if i < len(s) and s[i] == "[":
            j = s.find("]", i + 1)
            if j == -1:
                return None
            opt = s[i : j + 1]
            i = j + 1
            while i < len(s) and s[i].isspace():
                i += 1
        if i >= len(s) or s[i] != "{":
            return None
        j = _find_matching_brace(s, i)
        if j is None:
            return None
        title = s[i + 1 : j]
        return start, j + 1, opt, title

    # Counters
    current_major: str | None = None
    current_kind: str | None = None  # 'chap' or 'app'
    sub = 0
    subsub = 0
    enabled = False

    out: list[str] = []
    i = 0
    while i < len(text):
        # Find next heading command among section/subsection/subsubsection.
        next_pos = -1
        next_cmd = ""
        for cmd in ("section", "subsection", "subsubsection"):
            p = text.find("\\" + cmd, i)
            if p != -1 and (next_pos == -1 or p < next_pos):
                next_pos = p
                next_cmd = cmd
        if next_pos == -1:
            out.append(text[i:])
            break

        out.append(text[i:next_pos])
        parsed = _scan_cmd(text, next_pos, next_cmd)
        if parsed is None:
            # leave untouched (likely starred or malformed)
            out.append(text[next_pos : next_pos + len(next_cmd) + 1])
            i = next_pos + len(next_cmd) + 1
            continue
        cmd_start, after_title, opt, title = parsed

        # Look ahead for an immediate label: \label{...}
        rest = text[after_title:]
        m_lab = re.match(r"\s*\\label\{([^}]+)\}", rest)
        lab = m_lab.group(1).strip() if m_lab else None

        if next_cmd == "section":
            sub = 0
            subsub = 0
            if lab and (lab.startswith("chap:") or lab.startswith("app:")):
                current_kind = "chap" if lab.startswith("chap:") else "app"
                current_major = aux_numbers.get(lab)
                if current_major:
                    enabled = True
            out.append(text[cmd_start:after_title])
            i = after_title
            continue

        # Only number subsections within numbered body.
        if not enabled or not current_major or not current_kind:
            out.append(text[cmd_start:after_title])
            i = after_title
            continue

        if next_cmd == "subsection":
            sub += 1
            subsub = 0
            num = aux_numbers.get(lab) if lab else f"{current_major}.{sub}"
        else:
            subsub += 1
            num = aux_numbers.get(lab) if lab else f"{current_major}.{sub}.{subsub}"

        if _starts_with_number(title):
            out.append(text[cmd_start:after_title])
            i = after_title
            continue

        new_title = f"{num} {title.strip()}"
        # Reconstruct command preserving optional short title.
        out.append(f"\\{next_cmd}{opt}{{{new_title}}}")
        i = after_title

    return "".join(out)


def prefix_numbered_headings(text: str, *, aux_numbers: dict[str, str]) -> str:
    """
    Prefix labeled subsection/subsubsection headings with their number from `.aux`.

    Example:
      \\subsection{Title}\\label{sec:foo} -> \\subsection{4.2 Title}\\label{sec:foo}
    """
    def _find_matching_bracket(s: str, start: int) -> int | None:
        if start < 0 or start >= len(s) or s[start] != "[":
            return None
        depth = 0
        i = start
        while i < len(s):
            ch = s[i]
            if ch == "[":
                depth += 1
            elif ch == "]":
                depth -= 1
                if depth == 0:
                    return i
            i += 1
        return None

    def _starts_with_number(title: str) -> bool:
        t = title.strip()
        return bool(re.match(r"^[A-Za-z0-9]+(?:\\.[A-Za-z0-9]+)*\\s", t))

    out: list[str] = []
    i = 0
    while i < len(text):
        m = re.search(r"\\(subsection|subsubsection)\b", text[i:])
        if not m:
            out.append(text[i:])
            break
        cmd = m.group(1)
        cmd_start = i + m.start()
        j = i + m.end()

        # Skip starred variants.
        if j < len(text) and text[j] == "*":
            out.append(text[i : j + 1])
            i = j + 1
            continue

        # Optional short title [...]
        opt = ""
        if j < len(text) and text[j] == "[":
            j_end = _find_matching_bracket(text, j)
            if j_end is None:
                out.append(text[i : j + 1])
                i = j + 1
                continue
            opt = text[j : j_end + 1]
            j = j_end + 1

        # Required title {...} (brace-matched, supports nested braces).
        while j < len(text) and text[j].isspace():
            j += 1
        if j >= len(text) or text[j] != "{":
            out.append(text[i : j + 1])
            i = j + 1
            continue
        t_end = _find_matching_brace(text, j)
        if t_end is None:
            out.append(text[i:])
            break
        title = text[j + 1 : t_end]
        after_title = t_end + 1

        # Look for an immediate label after whitespace.
        k = after_title
        while k < len(text) and text[k].isspace():
            k += 1
        if not text.startswith("\\label{", k):
            out.append(text[i:after_title])
            i = after_title
            continue
        lab_start = k + len("\\label{")
        lab_end = text.find("}", lab_start)
        if lab_end == -1:
            out.append(text[i:after_title])
            i = after_title
            continue
        lab = text[lab_start:lab_end].strip()
        after_label = lab_end + 1

        num = aux_numbers.get(lab)
        if not num or _starts_with_number(title) or title.lstrip().startswith(num):
            out.append(text[i:after_label])
            i = after_label
            continue

        ws = text[after_title:k]
        new_title = f"{num} {title.strip()}"
        out.append(text[i:cmd_start])
        out.append(f"\\{cmd}{opt}{{{new_title}}}{ws}\\label{{{lab}}}")
        i = after_label

    return "".join(out)


def _find_matching_brace(s: str, start: int) -> int | None:
    if start < 0 or start >= len(s) or s[start] != "{":
        return None
    depth = 0
    i = start
    while i < len(s):
        ch = s[i]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return None


def prefix_caption_numbers(text: str, *, aux_numbers: dict[str, str]) -> str:
    """
    Make figure/table numbers visible in EPUB by prefixing captions using `.aux`:
      caption -> "Figure 2. ..." / "Table 5. ..."
    """
    def _scan_env(buf: str, *, env: str, label_prefix: str, noun: str) -> str:
        out: list[str] = []
        begin = f"\\begin{{{env}}}"
        end = f"\\end{{{env}}}"
        i = 0
        while True:
            s = buf.find(begin, i)
            if s == -1:
                out.append(buf[i:])
                return "".join(out)
            out.append(buf[i:s])
            e = buf.find(end, s)
            if e == -1:
                out.append(buf[s:])
                return "".join(out)
            block = buf[s : e + len(end)]

            # Match e.g. \label{fig:roadmap} / \label{tab:foo}
            m_lab = re.search(rf"\\label\{{({re.escape(label_prefix)}[^}}]+)\}}", block)
            if not m_lab:
                out.append(block)
                i = e + len(end)
                continue
            lab = m_lab.group(1)
            num = aux_numbers.get(lab)
            if not num:
                out.append(block)
                i = e + len(end)
                continue

            # Find the actual \caption command (not \captionsetup).
            cap_m = re.search(r"\\caption(?!setup)\s*(?:\[[^\]]*\])?\s*\{", block)
            if not cap_m:
                out.append(block)
                i = e + len(end)
                continue

            j = cap_m.end() - 1  # points to the opening "{"
            j_end = _find_matching_brace(block, j)
            if j_end is None:
                out.append(block)
                i = e + len(end)
                continue

            cap = block[j + 1 : j_end]
            prefix = f"{noun} {num}. "
            if cap.lstrip().startswith(prefix) or cap.lstrip().startswith(f"{noun} "):
                out.append(block)
                i = e + len(end)
                continue
            new_cap = prefix + cap.lstrip()
            new_block = block[: j + 1] + new_cap + block[j_end:]
            out.append(new_block)
            i = e + len(end)

    buf = _scan_env(text, env="figure", label_prefix="fig:", noun="Figure")
    buf = _scan_env(buf, env="table", label_prefix="tab:", noun="Table")
    return buf


def promote_displaystyle_math(text: str) -> str:
    """
    Convert `\\(\\displaystyle ...\\)` that is likely meant as display math into
    `\\[ ... \\]` so Pandoc emits block MathML and long expressions don't get
    clipped in reflowable EPUB layouts.

    Heuristic: promote when content is long or includes integral symbols.
    """
    pat = re.compile(r"\\\(\s*\\displaystyle\s*(.*?)\\\)", flags=re.DOTALL)

    def _sub(m: re.Match[str]) -> str:
        inner = m.group(1).strip()
        if "\\int" not in inner and len(inner) < 80:
            return m.group(0)
        return "\\[\n" + inner + "\n\\]"

    out = pat.sub(_sub, text)
    # Remove forced linebreaks immediately before promoted display math.
    out = re.sub(r"\\\\\s*\n\s*\\\[", r"\n\\[", out)
    return out

def promote_long_inline_math(text: str) -> str:
    """
    Promote long inline math `\\(...\\)` to display math `\\[...\\]` to avoid
    reader-specific inline MathML clipping.
    """
    pat = re.compile(r"\\\(\s*(?!\\displaystyle)(.*?)\\\)", flags=re.DOTALL)
    heavy = ("\\frac", "\\int", "\\sum", "\\prod", "\\begin{", "\\left", "\\right", "=")

    def _sub(m: re.Match[str]) -> str:
        inner = m.group(1).strip()
        if len(inner) < 120 and not any(h in inner for h in heavy):
            return m.group(0)
        # Avoid promoting truly tiny inline symbols even if they contain '='.
        if len(inner) < 80 and inner.count("=") <= 1 and "\\int" not in inner and "\\frac" not in inner:
            return m.group(0)
        return "\\[\n" + inner + "\n\\]"

    out = pat.sub(_sub, text)
    out = re.sub(r"\\\\\s*\n\s*\\\[", r"\n\\[", out)
    return out


def add_visible_equation_numbers(text: str, *, aux_numbers: dict[str, str]) -> str:
    """
    Add a visible equation number line after each labeled equation-like environment.
    """
    envs = ["equation", "equation*", "align", "align*", "gather", "gather*", "multline", "multline*", "alignat", "alignat*"]
    out: list[str] = []
    i = 0
    while i < len(text):
        next_pos = -1
        next_env = None
        for env in envs:
            p = text.find(f"\\begin{{{env}}}", i)
            if p != -1 and (next_pos == -1 or p < next_pos):
                next_pos = p
                next_env = env
        if next_pos == -1 or next_env is None:
            out.append(text[i:])
            break
        out.append(text[i:next_pos])
        end_tag = f"\\end{{{next_env}}}"
        end_pos = text.find(end_tag, next_pos)
        if end_pos == -1:
            out.append(text[next_pos:])
            break
        block = text[next_pos : end_pos + len(end_tag)]
        labels: list[str] = []
        for m in re.finditer(r"\\label\{(eq:[^}]+)\}", block):
            lab = m.group(1).strip()
            if lab and lab not in labels:
                labels.append(lab)
        out.append(block)
        nums = []
        for lab in labels:
            num = aux_numbers.get(lab)
            if num:
                nums.append(num)
        if nums:
            # Pandoc's MathML output does not include equation numbers, so we
            # add a small right-aligned line after the display block.
            rendered = "\\\\\n".join(f"({n})" for n in nums)
            out.append(f"\n\n\\begin{{flushright}}\\small {rendered}\\end{{flushright}}\n")
        i = end_pos + len(end_tag)
    text2 = "".join(out)

    # Also add visible numbers for display math written as \[...\].
    # Guard against `\\[<len>]` line breaks (common in TikZ/node text and tables).
    out3: list[str] = []
    i = 0
    while True:
        s = text2.find("\\[", i)
        if s == -1:
            out3.append(text2[i:])
            break
        if s > 0 and text2[s - 1] == "\\":  # skip `\\[` (newline + optional spacing)
            out3.append(text2[i : s + 2])
            i = s + 2
            continue
        e = text2.find("\\]", s + 2)
        if e == -1:
            out3.append(text2[i:])
            break
        while e > 0 and text2[e - 1] == "\\":  # skip `\\]` (rare, but symmetric guard)
            e = text2.find("\\]", e + 2)
            if e == -1:
                break
        if e == -1:
            out3.append(text2[i:])
            break
        block = text2[s : e + 2]
        labels: list[str] = []
        for m in re.finditer(r"\\label\{(eq:[^}]+)\}", block):
            lab = m.group(1).strip()
            if lab and lab not in labels:
                labels.append(lab)
        out3.append(text2[i : e + 2])
        nums = []
        for lab in labels:
            num = aux_numbers.get(lab)
            if num:
                nums.append(num)
        if nums:
            rendered = "\\\\\n".join(f"({n})" for n in nums)
            out3.append(f"\n\n\\begin{{flushright}}\\small {rendered}\\end{{flushright}}\n")
        i = e + 2
    return "".join(out3)


def strip_captionsetup_commands(text: str) -> str:
    """
    Remove `\\captionsetup{...}` / `\\captionsetup[...] { ... }` commands.

    Pandoc does not interpret caption setup directives and, when combined with
    `\\resizebox{...}{...}{...}`, it can end up dropping the wrapped graphic.
    """
    cmd = "\\captionsetup"
    out: list[str] = []
    i = 0
    while True:
        s = text.find(cmd, i)
        if s == -1:
            out.append(text[i:])
            break
        out.append(text[i:s])
        j = s + len(cmd)
        # Optional [..] argument (no nesting expected).
        if j < len(text) and text[j] == "[":
            k = text.find("]", j + 1)
            if k != -1:
                j = k + 1
        # Brace argument.
        while j < len(text) and text[j].isspace():
            j += 1
        if j >= len(text) or text[j] != "{":
            # Not a form we recognize; keep literal text.
            out.append(cmd)
            i = s + len(cmd)
            continue
        j_end = _find_matching_brace(text, j)
        if j_end is None:
            # Unbalanced; keep rest.
            out.append(text[s:])
            break
        i = j_end + 1
    return "".join(out)


def unwrap_graphics_wrappers(text: str) -> str:
    """
    Unwrap common graphics scaling wrappers so Pandoc reliably emits `<img>`.

    In this book, many figures use `\\resizebox{...}{...}{\\includegraphics{...}}`.
    Pandoc's LaTeX reader can drop unknown wrappers, leaving caption-only figures.
    """
    # Some figures wrap the actual content in an `adjustbox` environment, e.g.
    # `\begin{adjustbox}{max width=\linewidth,center} ... \end{adjustbox}`.
    # Pandoc does not understand `adjustbox` and can leak its option string as
    # literal text in the EPUB (e.g., "max width=,center"). Unwrap it early.
    begin_env = "\\begin{adjustbox}"
    end_env = "\\end{adjustbox}"
    if begin_env in text:
        out_env: list[str] = []
        i_env = 0

        def _parse_optional_bracket_arg(s: str, pos: int) -> int | None:
            # Optional [..] argument. We do not expect nesting.
            while pos < len(s) and s[pos].isspace():
                pos += 1
            if pos < len(s) and s[pos] == "[":
                end = s.find("]", pos + 1)
                if end == -1:
                    return None
                return end + 1
            return pos

        while i_env < len(text):
            s = text.find(begin_env, i_env)
            if s == -1:
                out_env.append(text[i_env:])
                break
            out_env.append(text[i_env:s])
            j = s + len(begin_env)
            j2 = _parse_optional_bracket_arg(text, j)
            if j2 is None:
                # Unbalanced optional arg; keep literal and bail out.
                out_env.append(text[s:])
                break
            j = j2
            while j < len(text) and text[j].isspace():
                j += 1
            # Required `{...}` argument (typically the adjustbox options).
            if j >= len(text) or text[j] != "{":
                out_env.append(begin_env)
                i_env = s + len(begin_env)
                continue
            j_end = _find_matching_brace(text, j)
            if j_end is None:
                out_env.append(text[s:])
                break
            content_start = j_end + 1

            # Find the matching \end{adjustbox}, accounting for nesting.
            depth = 1
            k = content_start
            content_end = None
            while depth > 0:
                b = text.find(begin_env, k)
                e = text.find(end_env, k)
                if e == -1:
                    break
                if b != -1 and b < e:
                    depth += 1
                    k = b + len(begin_env)
                else:
                    depth -= 1
                    if depth == 0:
                        content_end = e
                        k = e + len(end_env)
                        break
                    k = e + len(end_env)

            if content_end is None:
                out_env.append(text[s:])
                break

            out_env.append(text[content_start:content_end].strip() + "\n")
            i_env = k

        text = "".join(out_env)

    wrappers = [
        ("\\resizebox", 3, 2),  # (macro, nargs, content_arg_index)
        ("\\scalebox", 2, 1),
    ]
    out: list[str] = []
    i = 0

    def _parse_brace_arg(s: str, pos: int) -> tuple[int, int] | None:
        while pos < len(s) and s[pos].isspace():
            pos += 1
        if pos >= len(s) or s[pos] != "{":
            return None
        end = _find_matching_brace(s, pos)
        if end is None:
            return None
        return pos, end

    while i < len(text):
        next_pos = -1
        which = None
        for w in wrappers:
            p = text.find(w[0], i)
            if p != -1 and (next_pos == -1 or p < next_pos):
                next_pos = p
                which = w
        if next_pos == -1 or which is None:
            out.append(text[i:])
            break

        macro, nargs, content_idx = which
        out.append(text[i:next_pos])
        j = next_pos + len(macro)
        args: list[tuple[int, int]] = []
        ok = True
        for _ in range(nargs):
            parsed = _parse_brace_arg(text, j)
            if not parsed:
                ok = False
                break
            a_s, a_e = parsed
            args.append((a_s, a_e))
            j = a_e + 1

        if not ok:
            out.append(text[next_pos : next_pos + len(macro)])
            i = next_pos + len(macro)
            continue

        content_s, content_e = args[content_idx]
        content = text[content_s + 1 : content_e]
        # Only unwrap when it actually wraps an image include.
        if "\\includegraphics" in content:
            out.append(content.strip() + "\n")
        else:
            out.append(text[next_pos:j])
        i = j

    return "".join(out)


def transform_tcolorbox_to_quote(text: str) -> str:
    """
    Convert simple `tcolorbox` environments to `quote` blocks.

    This is intentionally conservative: it handles the common pattern
    `\\begin{tcolorbox}[...,title={...}] ... \\end{tcolorbox}`.
    """
    begin_re = re.compile(r"\\begin\{tcolorbox\}\[([^\]]*)\]")

    def _extract_title(opts: str) -> str | None:
        # Parse `title={...}` with brace depth (titles can contain macros like `\hyp{}`).
        m = re.search(r"(?:^|,)\s*title\s*=\s*\{", opts)
        if m:
            i = m.end()  # points just after the opening "{"
            depth = 1
            buf: list[str] = []
            while i < len(opts):
                ch = opts[i]
                if ch == "{":
                    depth += 1
                    buf.append(ch)
                elif ch == "}":
                    depth -= 1
                    if depth == 0:
                        return "".join(buf).strip()
                    buf.append(ch)
                else:
                    buf.append(ch)
                i += 1
        # If no explicit title is provided, fall back to the style token when present.
        # These styles define a default `title=...` in the book preamble.
        if re.search(r"(^|,)\s*summarybox\s*(,|$)", opts):
            return "Summary"
        if re.search(r"(^|,)\s*pitfallbox\s*(,|$)", opts):
            return "Pitfall"
        if re.search(r"(^|,)\s*perspectivebox\s*(,|$)", opts):
            return "Perspective"
        return None

    out: list[str] = []
    i = 0
    while True:
        m = begin_re.search(text, i)
        if not m:
            out.append(text[i:])
            break
        start = m.start()
        out.append(text[i:start])
        opts = m.group(1)
        title = _extract_title(opts)
        body_start = m.end()
        end = text.find("\\end{tcolorbox}", body_start)
        if end == -1:
            out.append(text[start:])
            break
        body = text[body_start:end]
        out.append("\\begin{quote}\n")
        if title:
            out.append(f"\\textbf{{{title}}}\\\\\n")
        out.append(body.strip() + "\n")
        out.append("\\end{quote}\n")
        i = end + len("\\end{tcolorbox}")
    return "".join(out)


def resolve_bare_includegraphics(text: str, *, repo_root: Path) -> str:
    """
    Convert `\\includegraphics{foo}` into `\\includegraphics{assets/.../foo.png}`
    when `foo` exists under `assets/` in the repo.

    The LaTeX sources sometimes rely on editor/TeX search paths for bare image
    names; Pandoc does not, so we make paths explicit.
    """
    assets_root = (repo_root / "assets").resolve()
    if not assets_root.exists():
        return text

    def _pick_asset(stem: str) -> str | None:
        # Prefer vector sources first, then raster formats. PDF/SVG will be
        # rasterized at high DPI for EPUB later in the pipeline.
        ext_order = [".pdf", ".svg", ".png", ".jpg", ".jpeg"]
        candidates: list[Path] = []
        for ext in ext_order:
            candidates.extend(assets_root.rglob(stem + ext))
        if not candidates:
            return None
        ext_rank = {ext: i for i, ext in enumerate(ext_order)}
        candidates.sort(key=lambda p: (ext_rank.get(p.suffix.lower(), 999), "-" in p.stem, str(p)))
        chosen = candidates[0]
        return chosen.relative_to(repo_root).as_posix()

    def _pick_from_path_noext(rel_path: str) -> str | None:
        """
        If LaTeX references `assets/foo/bar` with no extension, prefer a raster
        image (`.png/.jpg`) over `.pdf` so Pandoc doesn't embed PDFs in EPUB.
        """
        base = (repo_root / rel_path).resolve()
        # Only allow resolutions that stay inside the repo.
        try:
            base.relative_to(repo_root.resolve())
        except ValueError:
            return None
        exts = [".png", ".jpg", ".jpeg", ".svg", ".pdf"]
        for ext in exts:
            candidate = base.with_suffix(ext)
            if candidate.exists():
                return candidate.relative_to(repo_root).as_posix()
        return None

    include_re = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}")

    def _sub(m: re.Match[str]) -> str:
        target = m.group(1).strip()
        # If an extension is already present, keep it.
        if "." in Path(target).name:
            rel = target.replace("\\", "/")
            lower = rel.lower()

            # If a raster is referenced but a sibling vector exists, prefer vector.
            # We will rasterize PDFs at high DPI later for crisp EPUB rendering.
            if lower.endswith((".png", ".jpg", ".jpeg")):
                base_noext = rel.rsplit(".", 1)[0]
                # Try pdf first, then svg.
                for ext in (".pdf", ".svg"):
                    candidate = (repo_root / (base_noext + ext)).resolve()
                    try:
                        candidate.relative_to(repo_root.resolve())
                    except ValueError:
                        candidate = None
                    if candidate and candidate.exists():
                        return m.group(0).replace("{" + target + "}", "{" + (base_noext + ext) + "}")

            # Prefer raster formats over embedded PDFs in EPUB whenever possible,
            # but if the source is a PDF and a raster exists, swap to the raster.
            if lower.endswith(".pdf"):
                candidate = _pick_from_path_noext(rel[:-4])
                if candidate and not candidate.lower().endswith(".pdf"):
                    return m.group(0).replace("{" + target + "}", "{" + candidate + "}")

            return m.group(0)

        # Prefer resolving explicit relative paths (e.g., assets/foo/bar) to a
        # raster format so the EPUB doesn't contain embedded PDFs.
        if "/" in target or "\\" in target:
            rel = target.replace("\\", "/")
            resolved = _pick_from_path_noext(rel)
            if not resolved:
                return m.group(0)
            return m.group(0).replace("{" + target + "}", "{" + resolved + "}")

        resolved = _pick_asset(target)
        if not resolved:
            return m.group(0)
        return m.group(0).replace("{" + target + "}", "{" + resolved + "}")

    return include_re.sub(_sub, text)


def rasterize_pdf_includegraphics(
    text: str, *, repo_root: Path, notes_output_dir: Path, media_dir: Path, dpi: int
) -> str:
    """
    Convert `\\includegraphics{...pdf}` into `\\includegraphics{assetpdf_XXXX.png}`.

    Pandoc will otherwise rasterize PDFs at reader/tool defaults that can look
    soft. We pre-rasterize at a high DPI via `pdftoppm` and cache outputs in the
    EPUB media dir.
    """
    media_dir.mkdir(parents=True, exist_ok=True)
    include_re = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}")

    def _resolve(rel: str) -> Path | None:
        p = Path(rel)
        if p.is_absolute() or rel.startswith("~") or "://" in rel:
            return None
        rel_norm = rel[2:] if rel.startswith("./") else rel
        cand = (media_dir / rel_norm).resolve()
        if cand.exists():
            return cand
        for root in (repo_root, notes_output_dir):
            c = (root / rel_norm).resolve()
            if c.exists():
                return c
        return None

    def _rasterize(src_pdf: Path) -> str | None:
        if src_pdf.suffix.lower() != ".pdf":
            return None
        # Stable cache key: relative path + mtime + dpi.
        try:
            rel = src_pdf.resolve().relative_to(repo_root.resolve()).as_posix()
        except ValueError:
            rel = src_pdf.name
        mtime = int(src_pdf.stat().st_mtime)
        key = f"{rel}|{mtime}|{dpi}"
        import hashlib

        stem = "assetpdf_" + hashlib.sha1(key.encode("utf-8")).hexdigest()[:12]
        out_png = media_dir / f"{stem}.png"
        if out_png.exists() and out_png.stat().st_size > 0:
            return out_png.name
        # Render first page to PNG.
        prefix = media_dir / stem
        cmd = ["pdftoppm", "-r", str(dpi), "-png", "-singlefile", str(src_pdf), str(prefix)]
        subprocess.run(cmd, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if out_png.exists() and out_png.stat().st_size > 0:
            return out_png.name
        return None

    out_parts: list[str] = []
    last = 0
    for m in include_re.finditer(text):
        target = m.group(1).strip()
        lower = target.lower()
        src: Path | None = None

        if lower.endswith(".pdf"):
            src = _resolve(target)
        elif lower.endswith((".png", ".jpg", ".jpeg")):
            # If a raster is referenced but a sibling PDF exists, prefer rasterizing
            # the PDF at high DPI for crispness.
            base = target.rsplit(".", 1)[0] + ".pdf"
            src = _resolve(base)
        else:
            continue

        if not src or not src.exists():
            continue

        png_name = _rasterize(src)
        if not png_name:
            continue
        out_parts.append(text[last : m.start()])
        out_parts.append(m.group(0).replace("{" + target + "}", "{" + png_name + "}"))
        last = m.end()
    out_parts.append(text[last:])
    return "".join(out_parts)


_INCLUDEGRAPHICS_RE = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}")


def verify_includegraphics_targets(
    text: str, *, repo_root: Path, notes_output_dir: Path, media_dir: Path
) -> None:
    """
    In strict mode, treat missing `\\includegraphics{...}` files as fatal.

    Pandoc can silently drop missing assets, producing caption-only figures.
    This check ensures every referenced image resolves to an existing file within
    the repo's build roots (repo_root/notes_output/media cache).
    """
    allowed_roots = [media_dir.resolve(), notes_output_dir.resolve(), repo_root.resolve()]
    missing: list[str] = []
    disallowed: list[str] = []

    def _paths_for(raw: str) -> list[Path]:
        p = Path(raw)
        if p.is_absolute() or raw.startswith("~"):
            disallowed.append(raw)
            return []
        raw_norm = raw[2:] if raw.startswith("./") else raw
        p_norm = Path(raw_norm)
        if p_norm.suffix:
            return [(root / p_norm) for root in allowed_roots]
        # No extension: try common image formats.
        exts = [".png", ".jpg", ".jpeg", ".svg", ".pdf"]
        out: list[Path] = []
        for root in allowed_roots:
            base = root / p_norm
            out.extend(base.with_suffix(ext) for ext in exts)
        return out

    for m in _INCLUDEGRAPHICS_RE.finditer(text):
        raw = m.group(1).strip()
        if not raw:
            continue
        if raw.startswith("http://") or raw.startswith("https://"):
            disallowed.append(raw)
            continue

        candidates = _paths_for(raw)
        if not candidates:
            continue

        found = False
        for c in candidates:
            try:
                resolved = c.resolve()
            except OSError:
                continue
            if not resolved.exists():
                continue
            # Ensure the resolved file stays within one of the allowed roots.
            for root in allowed_roots:
                if resolved == root:
                    found = True
                    break
                if str(resolved).startswith(str(root) + "/"):
                    found = True
                    break
            if found:
                break
            disallowed.append(raw)
            found = True
            break

        if not found:
            missing.append(raw)

    if disallowed:
        raise SystemExit(
            "Disallowed external/absolute includegraphics targets found:\n- "
            + "\n- ".join(sorted(set(disallowed))[:60])
        )
    if missing:
        raise SystemExit(
            "Missing includegraphics assets (would produce caption-only figures):\n- "
            + "\n- ".join(sorted(set(missing))[:120])
        )
