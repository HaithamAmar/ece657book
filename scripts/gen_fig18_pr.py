import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

plt.rcParams.update({
    "figure.figsize": (3.6, 2.6),
    "font.size": 10,
    "axes.labelsize": 11,
    "axes.titlesize": 11,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "font.family": "serif",
})

cb_blue = "#1f77b4"
cb_orange = "#ff7f0e"
cb_gray = "#7f7f7f"

out_dir = Path(__file__).resolve().parents[1] / "assets" / "lec3"
out_dir.mkdir(parents=True, exist_ok=True)

recall = np.linspace(0, 1, 200)
# smooth PR curves
prec_a = 0.25 + 0.65 * (1 - recall**1.2) * (0.8 - 0.3 * recall)
prec_b = 0.25 + 0.45 * (1 - recall**0.9) * (0.9 - 0.2 * recall)

fig, ax = plt.subplots()
ax.plot(recall, prec_a, color=cb_blue, label="Model A", linewidth=2)
ax.plot(recall, prec_b, color=cb_orange, linestyle="--", label="Model B", linewidth=2)

# operating point on Model A
op_r = 0.78
op_p = np.interp(op_r, recall, prec_a)
ax.plot(op_r, op_p, marker="o", color=cb_blue, markersize=5)
# operating threshold marker
ax.annotate("τ*", xy=(op_r, op_p), xytext=(op_r+0.03, op_p+0.04),
            arrowprops=dict(arrowstyle="->", color=cb_blue, lw=0.8), fontsize=9)

# baseline prevalence
baseline = 0.25
ax.axhline(baseline, color=cb_gray, linestyle="--", linewidth=1)
ax.text(0.02, baseline + 0.015, "baseline (prevalence)", color=cb_gray, fontsize=9)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1.02)
ax.set_xlabel("Recall")
ax.set_ylabel("Precision")
ax.grid(True, alpha=0.25)
ax.legend(frameon=False)

fig.tight_layout()
fig.savefig(out_dir / "lec3_pr_curves.pdf")
fig.savefig(out_dir / "lec3_pr_curves.png", dpi=300)
print(f"Saved {out_dir/'lec3_pr_curves.pdf'}")
