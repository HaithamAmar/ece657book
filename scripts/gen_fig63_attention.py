import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

from figure_style import apply_style

apply_style(
    font_size=11,
    axes_labelsize=12,
    extra_rc={
        "figure.figsize": (4.6, 3.0),
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
    },
)

out_dir = Path(__file__).resolve().parents[1] / "assets" / "lec13"
out_dir.mkdir(parents=True, exist_ok=True)

# toy attention weights (decoder steps x encoder steps)
weights = np.array([
    [0.80, 0.10, 0.05, 0.03, 0.02],
    [0.10, 0.15, 0.55, 0.15, 0.05],
    [0.05, 0.10, 0.15, 0.60, 0.10],
    [0.02, 0.05, 0.10, 0.15, 0.68],
    [0.01, 0.04, 0.10, 0.15, 0.70],
])

source = ["I", "want", "to", "buy", "."]
target = ["je", "veux", "acheter", "un", "livre"]

fig, ax = plt.subplots()
im = ax.imshow(weights, cmap="viridis", aspect="auto", vmin=0, vmax=0.85)

ax.set_xticks(np.arange(len(target)))
ax.set_yticks(np.arange(len(source)))
ax.set_xticklabels(target, rotation=35, ha="right")
ax.set_yticklabels(source)
ax.set_xlabel("Target tokens")
ax.set_ylabel("Source tokens")

cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
cbar.ax.tick_params(labelsize=10)
cbar.ax.set_ylabel("Attention weight", rotation=90)

fig.tight_layout()
fig.savefig(out_dir / "lec13_attention_heatmap.pdf")
fig.savefig(out_dir / "lec13_attention_heatmap.png", dpi=300)
print(f"Saved {out_dir/'lec13_attention_heatmap.pdf'}")
