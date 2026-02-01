import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({
    "figure.figsize": (7.0, 3.2),
    "font.size": 11,
    "axes.titlesize": 13,
    "axes.labelsize": 12,
    "legend.fontsize": 10,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "lines.linewidth": 1.4,
    "font.family": "serif",
})

out_path = Path(__file__).resolve().parents[1] / "assets" / "lec1"
out_path.mkdir(parents=True, exist_ok=True)

cb_blue = "#1f77b4"
cb_orange = "#ff7f0e"
cb_gray = "#444444"

fig, axes = plt.subplots(1, 2, constrained_layout=True)

# Reliability diagram
ax = axes[0]
bins = np.linspace(0, 1, 11)
bin_centers = 0.5 * (bins[:-1] + bins[1:])
# synthetic slightly miscalibrated accuracies (ECE ≈ 0.02)
acc = np.array([0.02, 0.15, 0.28, 0.33, 0.47, 0.52, 0.68, 0.725, 0.87, 0.92])
ax.bar(bin_centers, acc, width=0.09, color=cb_blue, alpha=0.9, edgecolor="none")
# diagonal reference: heavier, higher-contrast so it is visible in print
ax.plot([0, 1], [0, 1], linestyle="--", color=cb_gray, linewidth=2.0)
ece = np.mean(np.abs(acc - bin_centers))
ax.text(0.05, 0.88, rf"ECE $\approx$ {ece:.02f}", transform=ax.transAxes, fontsize=11)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.05)
ax.set_xlabel("Predicted prob.")
ax.set_ylabel("Empirical accuracy")
ax.set_title("Reliability")
ax.grid(True, alpha=0.3)

# Double descent / scaling
ax = axes[1]
model_sizes = np.logspace(2, 6, 200)
# synthetic risk curve: initial descent, peak near interpolation, second descent
risk = 0.35 + 0.25 * np.exp(-((np.log10(model_sizes) - 2.8) ** 2) / 0.2)
risk += 0.06 * np.sin(0.8 * np.log10(model_sizes))
risk = risk + 0.06  # shift
ax.plot(model_sizes, risk, color=cb_blue, linewidth=2.4)
# heuristic scaling line: darker and thicker for print visibility
ax.plot(model_sizes, 0.55 * (model_sizes / model_sizes.max()) ** -0.08,
        linestyle="--", color=cb_gray, linewidth=2.0, label="scaling trend")
ax.set_xscale("log")
ax.set_xlim(model_sizes.min(), model_sizes.max())
ax.set_ylim(0.2, 1.05)
ax.set_xlabel("Model size (log scale)")
ax.set_ylabel("Validation loss")
ax.set_title("Double descent / scaling")
ax.grid(True, which="both", alpha=0.3)

fig.savefig(out_path / "lec1_reliability_double.pdf")
fig.savefig(out_path / "lec1_reliability_double.png", dpi=300)
print(f"Saved to {out_path}")
