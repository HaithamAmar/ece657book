import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

plt.rcParams.update({
    "figure.figsize": (4.0, 2.6),
    "font.size": 10,
    "axes.labelsize": 11,
    "axes.titlesize": 11,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "font.family": "serif",
})

cb_blue = "#1f77b4"
cb_orange = "#ff7f0e"

out_dir = Path(__file__).resolve().parents[1] / "assets" / "lec7"
out_dir.mkdir(parents=True, exist_ok=True)

steps = np.arange(0, 41)
vanish = 0.2 * (0.9 ** steps)
explode = 0.2 * (1.08 ** steps)

fig, ax = plt.subplots()
ax.plot(steps, vanish, color=cb_blue, label="Vanishing", linewidth=2)
# use a contrasting linestyle for exploding gradients so curves remain
# distinguishable in grayscale prints
ax.plot(steps, explode, color=cb_orange, label="Exploding", linewidth=2, linestyle="--")
ax.fill_between(steps, 0.08, 0.25, color="gray", alpha=0.15)

ax.set_yscale("log")
ax.set_xlim(0, 40)
ax.set_ylim(1e-3, 1.5)
ax.set_xlabel("Time steps")
ax.set_ylabel(r"$\| \partial \mathcal{L} / \partial h_t \|$")
ax.text(1.0, 0.12, "safe band", color="gray", fontsize=9)
ax.legend(frameon=False, loc="lower right")
ax.grid(True, which="both", alpha=0.3)

fig.tight_layout()
fig.savefig(out_dir / "lec7_vanish_explode.pdf")
fig.savefig(out_dir / "lec7_vanish_explode.png", dpi=300)
print(f"Saved {out_dir/'lec7_vanish_explode.pdf'}")
