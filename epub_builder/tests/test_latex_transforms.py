import unittest
import sys
from pathlib import Path


# Make `epub_builder/lib` imports work when running from repo root.
_EPUB_BUILDER_DIR = Path(__file__).resolve().parents[1]
if str(_EPUB_BUILDER_DIR) not in sys.path:
    sys.path.insert(0, str(_EPUB_BUILDER_DIR))


class TestLatexTransforms(unittest.TestCase):
    def test_rewrite_crossrefs_chapter(self) -> None:
        from lib.latex import rewrite_crossrefs

        aux = {"chap:supervised": "3"}
        s = r"Proceed to \Cref{chap:supervised}."
        out = rewrite_crossrefs(s, aux_numbers=aux)
        self.assertIn(r"\hyperlink{chap:supervised}{Chapter~3}", out)

    def test_rewrite_crossrefs_appendix(self) -> None:
        from lib.latex import rewrite_crossrefs

        aux = {"app:logistics": "C"}
        s = r"See \Cref{app:logistics} for details."
        out = rewrite_crossrefs(s, aux_numbers=aux)
        self.assertIn(r"\hyperlink{app:logistics}{Appendix~C}", out)

    def test_rewrite_crossrefs_equation(self) -> None:
        from lib.latex import rewrite_crossrefs

        aux = {"eq:bayes_theorem": "4.1"}
        s = r"Equation \eqref{eq:bayes_theorem} is central."
        out = rewrite_crossrefs(s, aux_numbers=aux)
        self.assertIn(r"\hyperref[eq:bayes_theorem]{(4.1)}", out)

    def test_promote_displaystyle_math(self) -> None:
        from lib.latex import promote_displaystyle_math

        s = r"\\ \(\displaystyle \int_0^1 x\,dx\)"
        out = promote_displaystyle_math(s)
        self.assertIn(r"\[", out)
        self.assertIn(r"\]", out)
        self.assertNotIn(r"\(\displaystyle", out)

    def test_prefix_chapter_sections(self) -> None:
        from lib.latex import prefix_chapter_sections

        aux = {"chap:intro": "1"}
        s = r"\section{About This Book}\label{chap:intro}"
        out = prefix_chapter_sections(s, aux_numbers=aux)
        self.assertIn("Chapter 1:", out)

    def test_prefix_caption_numbers(self) -> None:
        from lib.latex import prefix_caption_numbers

        aux = {"fig:roadmap": "1"}
        s = r"\\begin{figure}\\caption{Schematic: Roadmap.}\\label{fig:roadmap}\\end{figure}"
        out = prefix_caption_numbers(s, aux_numbers=aux)
        self.assertIn("Figure 1.", out)


if __name__ == '__main__':
    unittest.main()
