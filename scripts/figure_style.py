"""
Shared Matplotlib styling for book figures.

Goal: consistent typography + tight bounding boxes across all generated assets.
"""

from __future__ import annotations

from typing import Any

import matplotlib as mpl


def apply_style(
    *,
    font_family: str = "serif",
    font_size: int = 12,
    axes_labelsize: int | None = None,
    axes_titlesize: int | None = None,
    linewidth: float = 1.5,
    axes_linewidth: float = 1.0,
    savefig_dpi: int = 300,
    pad_inches: float = 0.05,
    extra_rc: dict[str, Any] | None = None,
) -> None:
    mpl.rcParams.update(
        {
            "font.family": font_family,
            "font.size": font_size,
            "axes.labelsize": axes_labelsize if axes_labelsize is not None else font_size + 1,
            "axes.titlesize": axes_titlesize if axes_titlesize is not None else font_size + 1,
            "lines.linewidth": linewidth,
            "axes.linewidth": axes_linewidth,
            # Prefer tight output for both PDF and PNG to reduce whitespace.
            "savefig.bbox": "tight",
            "savefig.pad_inches": pad_inches,
            "savefig.dpi": savefig_dpi,
        }
    )
    if extra_rc:
        mpl.rcParams.update(extra_rc)

