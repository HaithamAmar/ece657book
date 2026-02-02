import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

from figure_style import apply_style

apply_style(
    font_size=11,
    axes_labelsize=12,
    axes_titlesize=13,
    linewidth=1.6,
    extra_rc={
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
    },
)

# synthetic ROC curve
fpr = np.linspace(0, 1, 200)
tpr = 1 - (1 - fpr) ** 2
# add slight sag
roc = tpr - 0.08 * np.exp(-((fpr - 0.15) ** 2) / 0.01)

# PR curve
recall = np.linspace(0, 1, 200)
precision = 0.9 - 0.6 * recall + 0.05 * np.sin(5 * recall)
precision = np.clip(precision, 0.2, 1.0)

op_idx = 90
op_point_roc = (fpr[op_idx], roc[op_idx])
op_point_pr = (recall[op_idx], precision[op_idx])

fig, axes = plt.subplots(1, 2, figsize=(6.6, 3.2), constrained_layout=True)

# ROC
ax = axes[0]
ax.plot(fpr, roc, color="#1f77b4", lw=2.4)
ax.plot([0, 1], [0, 1], ls="--", color="gray", lw=1.4)
# iso-cost example (slope ~ cost ratio)
for slope in [0.5, 1.5]:
    y = slope * fpr
    ax.plot(fpr, y, ls=":", color="gray", lw=1.1, alpha=0.7)
ax.scatter(*op_point_roc, color="#ffb000", edgecolor="k", s=80, zorder=5)
ax.text(op_point_roc[0] + 0.02, op_point_roc[1] - 0.08, "op. point", fontsize=10)
ax.set_xlim(0,1)
ax.set_ylim(0,1.02)
ax.set_xlabel("FPR")
ax.set_ylabel("TPR")
ax.set_title("ROC")
ax.grid(True, alpha=0.2)

# PR
ax = axes[1]
ax.plot(recall, precision, color="#1f77b4", lw=2.4)
ax.hlines(0.2, 0, 1, ls="--", color="gray", lw=1.4, label="prevalence")
ax.scatter(*op_point_pr, color="#ffb000", edgecolor="k", s=80, zorder=5)
ax.text(op_point_pr[0] + 0.02, op_point_pr[1] + 0.02, "op. point", fontsize=10)
# iso-F1 lines
for f1 in [0.3, 0.5, 0.7]:
    prec_iso = (f1 * recall) / (2*recall - f1 + 1e-9)
    mask = (prec_iso >= 0) & (prec_iso <= 1)
    ax.plot(recall[mask], prec_iso[mask], ls=":", color="gray", lw=1.1, alpha=0.7)
ax.set_xlim(0,1)
ax.set_ylim(0,1.02)
ax.set_xlabel("Recall")
ax.set_ylabel("Precision")
ax.set_title("PR")
ax.grid(True, alpha=0.2)

out_dir = Path(__file__).resolve().parents[1] / "assets" / "lec2_part2"
out_dir.mkdir(parents=True, exist_ok=True)
fig.savefig(out_dir / "lec2_roc_pr.pdf")
fig.savefig(out_dir / "lec2_roc_pr.png", dpi=300)
print(f"Saved to {out_dir}")
