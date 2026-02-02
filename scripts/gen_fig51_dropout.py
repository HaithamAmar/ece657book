import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

from figure_style import apply_style

apply_style(
    font_size=10,
    axes_labelsize=11,
    axes_titlesize=11,
    extra_rc={
        "figure.figsize": (4.0, 2.6),
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
    },
)

cb_green = "#1b9e77"
cb_orange = "#d95f02"
cb_gray = "#7f7f7f"

out_dir = Path(__file__).resolve().parents[1] / "assets" / "lec6"
out_dir.mkdir(parents=True, exist_ok=True)

epochs = np.linspace(0, 50, 200)

# synthetic curves: dropout keeps training low, val flattens
train_drop = 0.2 + 0.9 * np.exp(-epochs / 15)
val_drop = 0.25 + 0.45 * (1 - np.exp(-epochs / 30))
val_nodrop = 0.25 + 0.55 * (1 - np.exp(-epochs / 45)) + 0.08 * np.sin(epochs / 12)

fig, ax = plt.subplots()
ax.plot(epochs, train_drop, color=cb_green, label="train (dropout)", linewidth=2)
ax.plot(epochs, val_drop, color=cb_orange, label="val (dropout)", linewidth=2)
ax.plot(epochs, val_nodrop, color=cb_orange, linestyle="--", label="val (no dropout)", linewidth=2)

ax.set_xlim(0, 50)
ax.set_ylim(0, 1.15)
ax.set_xlabel("epoch")
ax.set_ylabel("loss")
ax.grid(True, alpha=0.25)
ax.legend(frameon=False)

fig.tight_layout()
fig.savefig(out_dir / "lec6_dropout_curves.pdf")
fig.savefig(out_dir / "lec6_dropout_curves.png", dpi=300)
print(f"Saved {out_dir/'lec6_dropout_curves.pdf'}")
