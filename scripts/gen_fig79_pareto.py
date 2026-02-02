import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

from figure_style import apply_style

apply_style(
    font_size=10,
    axes_labelsize=11,
    axes_titlesize=11,
    extra_rc={
        "figure.figsize": (3.3, 2.6),
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "legend.fontsize": 9,
    },
)

cb_blue = "#1f77b4"
cb_orange = "#ff7f0e"

out_dir = Path(__file__).resolve().parents[1] / "assets" / "lec19"
out_dir.mkdir(parents=True, exist_ok=True)

# synthetic front: sorted by f1
f1 = np.array([0.15, 0.22, 0.30, 0.38, 0.55, 0.65, 0.80, 0.88])
f2 = np.array([0.95, 0.92, 0.82, 0.72, 0.62, 0.48, 0.30, 0.55])

# dominated points (for illustration)
dom_f1 = np.array([0.28, 0.50, 0.70])
dom_f2 = np.array([0.98, 0.78, 0.68])

fig, ax = plt.subplots()
ax.scatter(f1, f2, color=cb_blue, label="Pareto front", s=26)
ax.scatter(dom_f1, dom_f2, color=cb_orange, marker="^", label="Dominated solutions", s=32)
ax.set_xlim(0, 1.02)
ax.set_ylim(0, 1.05)
ax.set_xlabel(r"$f_1$ (minimise)")
ax.set_ylabel(r"$f_2$ (minimise)")
ax.grid(True, alpha=0.25)
ax.legend(frameon=False, loc="upper right")

fig.tight_layout()
fig.savefig(out_dir / "lec19_pareto.pdf")
fig.savefig(out_dir / "lec19_pareto.png", dpi=300)
print(f"Saved {out_dir/'lec19_pareto.pdf'}")
