"""
Generate the embedding-cluster figure for Chapter 14 (Fig. 54).

Design goals:
- Two well-separated clusters (countries vs. capitals).
- Soft elliptical hulls with subtle borders.
- Two analogy arrows with readable labels.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from pathlib import Path


def main() -> None:
    # Global styling tuned for print
    plt.rcParams.update(
        {
            "font.family": "serif",
            "font.size": 13,
            "axes.labelsize": 14,
            "axes.titlesize": 14,
        }
    )

    out_dir = Path(__file__).resolve().parents[1] / "assets" / "lec14"
    out_dir.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------
    # Synthetic data (fixed, not random, for reproducibility)
    # ------------------------------------------------------------
    countries = np.array(
        [
            [-4.5, 1.9],
            [-3.8, 2.2],
            [-3.2, 1.3],
            [-2.4, 1.1],
            [-3.0, 0.7],
        ]
    )

    capitals = np.array(
        [
            [4.2, 1.1],
            [4.5, 1.5],
            [3.9, 0.8],
            [5.1, 0.4],
            [4.3, 0.9],
        ]
    )

    # Portugal–Lisbon and France–Paris pairs
    arrow_start1 = countries[1]
    arrow_end1 = capitals[1]
    arrow_start2 = countries[3]
    arrow_end2 = capitals[3]

    palette = {
        "blue": "#0072B2",
        "orange": "#E69F00",
        "gray": "#606060",
    }

    fig, ax = plt.subplots(figsize=(10.5, 6))

    # Soft hulls around clusters
    ax.add_patch(
        Ellipse(
            (-3.5, 1.4),
            width=3.4,
            height=2.1,
            angle=-10,
            facecolor=palette["blue"],
            edgecolor=palette["blue"],
            lw=1.1,
            alpha=0.14,
            zorder=0,
        )
    )
    ax.add_patch(
        Ellipse(
            (4.4, 1.0),
            width=2.7,
            height=1.9,
            angle=8,
            facecolor=palette["orange"],
            edgecolor=palette["orange"],
            lw=1.1,
            alpha=0.14,
            zorder=0,
        )
    )

    # Scatter points
    ax.scatter(
        countries[:, 0],
        countries[:, 1],
        s=90,
        color=palette["blue"],
        edgecolor="white",
        linewidth=0.8,
        label="Countries",
        zorder=3,
    )
    ax.scatter(
        capitals[:, 0],
        capitals[:, 1],
        s=90,
        color=palette["orange"],
        edgecolor="white",
        linewidth=0.8,
        label="Capitals",
        zorder=3,
    )

    # Beautiful arrows and labels
    arrowprops = dict(
        arrowstyle="-|>",
        lw=2.2,
        color=palette["gray"],
        shrinkA=14,
        shrinkB=14,
        mutation_scale=12,
    )

    ax.annotate("", xy=arrow_end1, xytext=arrow_start1, arrowprops=arrowprops)
    ax.text(
        (arrow_start1[0] + arrow_end1[0]) / 2,
        (arrow_start1[1] + arrow_end1[1]) / 2 + 0.25,
        "Portugal \N{RIGHTWARDS ARROW} Lisbon",
        color=palette["gray"],
        fontsize=12,
        ha="center",
        bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="none", alpha=0.75),
    )

    ax.annotate("", xy=arrow_end2, xytext=arrow_start2, arrowprops=arrowprops)
    ax.text(
        (arrow_start2[0] + arrow_end2[0]) / 2,
        (arrow_start2[1] + arrow_end2[1]) / 2 - 0.32,
        "France \N{RIGHTWARDS ARROW} Paris",
        color=palette["gray"],
        fontsize=12,
        ha="center",
        bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="none", alpha=0.75),
    )

    # Axes + styling
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
    ax.set_xlim(-6, 6)
    ax.set_ylim(-1.2, 3.2)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.legend(frameon=False, loc="upper left")

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    for spine in ("left", "bottom"):
        ax.spines[spine].set_color(palette["gray"])
        ax.spines[spine].set_linewidth(1.0)

    fig.tight_layout()
    pdf_path = out_dir / "lec14_embeddings_clusters.pdf"
    png_path = out_dir / "lec14_embeddings_clusters.png"
    fig.savefig(pdf_path)
    fig.savefig(png_path, dpi=300)
    print(f"Saved {pdf_path}")


if __name__ == "__main__":
    main()
