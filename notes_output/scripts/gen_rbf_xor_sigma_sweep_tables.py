#!/usr/bin/env python3
"""
Generate deterministic PGFPlots tables for the RBF XOR sigma-sweep figure.

We keep the data files in notes_output/ so LaTeX can include them with simple
relative paths during book builds.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import numpy as np


@dataclass(frozen=True)
class SweepSpec:
    sigma: float
    tag: str  # file-name safe tag (e.g., "sigma0p8")


def rbf(x: np.ndarray, c: np.ndarray, sigma: float) -> float:
    return float(math.exp(-float(np.sum((x - c) ** 2)) / (2.0 * sigma * sigma)))


def solve_ridge_weights(
    X: np.ndarray, t: np.ndarray, centers: np.ndarray, sigma: float, lam: float
) -> np.ndarray:
    Phi = np.stack([[rbf(x, c, sigma) for c in centers] for x in X], axis=0)
    A = Phi.T @ Phi + lam * np.eye(Phi.shape[1])
    w = np.linalg.solve(A, Phi.T @ t)
    return w


def predict_grid(
    xs: np.ndarray, ys: np.ndarray, centers: np.ndarray, w: np.ndarray, sigma: float
) -> np.ndarray:
    grid = np.zeros((len(ys), len(xs)), dtype=float)
    for iy, y in enumerate(ys):
        for ix, x in enumerate(xs):
            p = np.array([float(x), float(y)], dtype=float)
            feat = np.array([rbf(p, c, sigma) for c in centers], dtype=float)
            grid[iy, ix] = float(feat @ w)
    return grid


def write_class_table_with_breaks(path: Path, xs: np.ndarray, ys: np.ndarray, cls: np.ndarray) -> None:
    lines: list[str] = ["x y cls"]
    for iy, y in enumerate(ys):
        for ix, x in enumerate(xs):
            lines.append(f"{x:0.4f} {y:0.4f} {int(cls[iy, ix])}")
        lines.append("")  # row break (matches existing *_with_breaks.dat format)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def _interp(p0: tuple[float, float], p1: tuple[float, float], f0: float, f1: float) -> tuple[float, float]:
    # Linear interpolation on an edge for f==0.
    if f0 == f1:
        return p0
    t = f0 / (f0 - f1)
    return (p0[0] + t * (p1[0] - p0[0]), p0[1] + t * (p1[1] - p0[1]))


def iter_marching_squares_segments(xs: np.ndarray, ys: np.ndarray, f: np.ndarray) -> Iterable[tuple[tuple[float, float], tuple[float, float]]]:
    """
    Yield contour segments for level 0 on the rect grid for f(x,y).

    We emit per-cell segments (not stitched polylines). This matches the existing
    contour-table style used in the book (many small segments separated by NaNs).
    """

    ny, nx = f.shape
    assert ny == len(ys) and nx == len(xs)

    for iy in range(ny - 1):
        y0 = float(ys[iy])
        y1 = float(ys[iy + 1])
        for ix in range(nx - 1):
            x0 = float(xs[ix])
            x1 = float(xs[ix + 1])

            # Corner values: bottom-left, bottom-right, top-right, top-left
            f_bl = float(f[iy, ix])
            f_br = float(f[iy, ix + 1])
            f_tr = float(f[iy + 1, ix + 1])
            f_tl = float(f[iy + 1, ix])

            # Bitmask for marching squares.
            idx = 0
            if f_bl >= 0:
                idx |= 1
            if f_br >= 0:
                idx |= 2
            if f_tr >= 0:
                idx |= 4
            if f_tl >= 0:
                idx |= 8

            if idx == 0 or idx == 15:
                continue

            # Edge intersections (compute lazily when needed).
            p_bl = (x0, y0)
            p_br = (x1, y0)
            p_tr = (x1, y1)
            p_tl = (x0, y1)

            def e_left() -> tuple[float, float]:
                return _interp(p_bl, p_tl, f_bl, f_tl)

            def e_right() -> tuple[float, float]:
                return _interp(p_br, p_tr, f_br, f_tr)

            def e_bottom() -> tuple[float, float]:
                return _interp(p_bl, p_br, f_bl, f_br)

            def e_top() -> tuple[float, float]:
                return _interp(p_tl, p_tr, f_tl, f_tr)

            # Segment table (standard marching squares; ambiguous cases 5/10 split).
            if idx in (1, 14):
                yield (e_left(), e_bottom())
            elif idx in (2, 13):
                yield (e_bottom(), e_right())
            elif idx in (3, 12):
                yield (e_left(), e_right())
            elif idx in (4, 11):
                yield (e_right(), e_top())
            elif idx == 5:
                yield (e_left(), e_top())
                yield (e_bottom(), e_right())
            elif idx in (6, 9):
                yield (e_bottom(), e_top())
            elif idx in (7, 8):
                yield (e_left(), e_top())
            elif idx == 10:
                yield (e_left(), e_bottom())
                yield (e_right(), e_top())


def write_contour_table(path: Path, xs: np.ndarray, ys: np.ndarray, f: np.ndarray) -> None:
    lines: list[str] = ["x y"]
    for (p0, p1) in iter_marching_squares_segments(xs, ys, f):
        lines.append(f"{p0[0]:0.6f} {p0[1]:0.6f}")
        lines.append(f"{p1[0]:0.6f} {p1[1]:0.6f}")
        lines.append("nan nan")
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    notes_dir = repo_root / "notes_output"

    X = np.array([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]], dtype=float)
    t = np.array([0.0, 1.0, 1.0, 0.0], dtype=float)
    centers = X.copy()

    lam = 1e-3
    level = 0.5

    # Match the existing book grid (29x29, step 0.05 over [-0.2, 1.2]).
    xs = np.linspace(-0.2, 1.2, 29)
    ys = np.linspace(-0.2, 1.2, 29)

    sweep = [
        SweepSpec(2.0, "sigma2p0"),
        SweepSpec(0.8, "sigma0p8"),
        SweepSpec(0.25, "sigma0p25"),
    ]

    for spec in sweep:
        w = solve_ridge_weights(X, t, centers, spec.sigma, lam)
        yhat = predict_grid(xs, ys, centers, w, spec.sigma)
        cls = (yhat >= level).astype(int)
        f = yhat - level

        class_path = notes_dir / f"rbf_xor_{spec.tag}_boundary_class_table_with_breaks.dat"
        contour_path = notes_dir / f"rbf_xor_{spec.tag}_contour_0p5.dat"

        write_class_table_with_breaks(class_path, xs, ys, cls)
        write_contour_table(contour_path, xs, ys, f)

    print("Wrote:")
    for spec in sweep:
        print(f"  {notes_dir / f'rbf_xor_{spec.tag}_boundary_class_table_with_breaks.dat'}")
        print(f"  {notes_dir / f'rbf_xor_{spec.tag}_contour_0p5.dat'}")


if __name__ == "__main__":
    main()

