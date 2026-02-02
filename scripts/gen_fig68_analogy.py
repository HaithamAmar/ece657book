import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

from figure_style import apply_style

apply_style(font_size=12)

points = {
    "king": (-3.2, 2.3),
    "man": (-1.0, 0.25),
    "queen": (2.0, 2.1),
    "woman": (4.1, 0.25),
    "doctor": (-2.1, -0.9),
    "nurse": (2.5, -1.0),
}

palette = {
    "royalty": "#0072B2",
    "gender": "#E69F00",
    "profession": "#009E73",
    "guide": "#555555",
}

markers = {"king": "o", "man": "o", "queen": "s", "woman": "s", "doctor": "^", "nurse": "^"}

fig, ax = plt.subplots(figsize=(6.8, 4.6))


def add_band(x0: float, y0: float, width: float, height: float, color: str) -> None:
    ax.add_patch(
        FancyBboxPatch(
            (x0, y0),
            width,
            height,
            boxstyle="round,pad=0.02,rounding_size=0.2",
            facecolor=color,
            edgecolor=color,
            linewidth=0.8,
            alpha=0.12,
            zorder=0,
        )
    )


# Soft horizontal bands to hint at semantic groupings
add_band(-3.8, 1.6, 6.4, 1.3, palette["royalty"])   # king/queen band
add_band(-1.6, -0.2, 6.4, 1.0, palette["gender"])   # man/woman band
add_band(-2.6, -1.6, 5.8, 1.0, palette["profession"])  # doctor/nurse band

# Scatter + labels
for word, coord in points.items():
    if word in {"king", "queen"}:
        color = palette["royalty"]
    elif word in {"man", "woman"}:
        color = palette["gender"]
    else:
        color = palette["profession"]
    ax.scatter(
        *coord,
        color=color,
        s=90,
        marker=markers[word],
        edgecolor="white",
        linewidth=0.8,
        zorder=3,
    )
    ax.text(coord[0], coord[1] + 0.18, word, color=palette["guide"], ha="center", va="bottom", fontsize=11)

# Analogy arrows
arrow = dict(arrowstyle="-|>", color=palette["guide"], lw=2.1, mutation_scale=12, shrinkA=4, shrinkB=4)
ax.annotate("", xy=points["queen"], xytext=points["king"], arrowprops=arrow)
ax.annotate("", xy=points["woman"], xytext=points["man"], arrowprops=arrow)
ax.annotate("", xy=points["nurse"], xytext=points["doctor"], arrowprops=dict(**arrow, ls=(0, (4, 3))))

# Parallelogram guide
king = np.array(points["king"])
man = np.array(points["man"])
queen = np.array(points["queen"])
woman = np.array(points["woman"])
poly = np.vstack([king, man, woman, queen, king])
ax.fill(poly[:, 0], poly[:, 1], color=palette["guide"], alpha=0.08, zorder=1)
ax.plot(poly[:, 0], poly[:, 1], color=palette["guide"], alpha=0.55, lw=1.4, zorder=2)
ax.text(-0.1, 2.55, "analogy plane", color=palette["guide"], fontsize=10, ha="center", va="bottom")

ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_xlim(-4.8, 5.2)
ax.set_ylim(-2.1, 3.1)
ax.set_aspect("equal", adjustable="box")
ax.set_xticks([])
ax.set_yticks([])
ax.grid(False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
for spine in ("left", "bottom"):
    ax.spines[spine].set_color(palette["guide"])
    ax.spines[spine].set_linewidth(1.0)

fig.tight_layout()
out_dir = Path(__file__).resolve().parents[1] / "assets" / "lec14"
out_dir.mkdir(parents=True, exist_ok=True)
fig.savefig(out_dir / "lec14_analogy_geometry.pdf")
fig.savefig(out_dir / "lec14_analogy_geometry.png", dpi=300)
print(f"Saved to {out_dir}")
