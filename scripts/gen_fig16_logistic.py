import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

np.random.seed(3)
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
})

# synthetic 2D data
n = 14
class0 = np.random.randn(n, 2) * 0.5 + np.array([-0.6, 0.8])
class1 = np.random.randn(n, 2) * 0.5 + np.array([1.1, -0.3])

X = np.vstack([class0, class1])
y = np.hstack([np.zeros(n), np.ones(n)])

# set logistic weights to separate roughly along w = [1,-1], b=0.2
w = np.array([1.0, -1.0])
b = 0.2

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# grid for probabilities
x1 = np.linspace(-2, 2, 400)
x2 = np.linspace(-2, 2, 400)
xx1, xx2 = np.meshgrid(x1, x2)
zz = w[0] * xx1 + w[1] * xx2 + b
probs = sigmoid(zz)

out_dir = Path(__file__).resolve().parents[1] / "assets" / "lec2_part2"
out_dir.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(4.5, 3.6))
levels = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
# Ebook-first: keep a vivid palette, but choose one with monotone luminance so it
# still degrades gracefully in grayscale.
ax.contourf(xx1, xx2, probs, levels=levels, cmap="viridis")

# probability contours (print-friendly)
contour_levels = [0.2, 0.4, 0.6, 0.8]
linestyles = ["dotted", "dashdot", "dashed", "solid"]
cs = ax.contour(
    xx1,
    xx2,
    probs,
    levels=contour_levels,
    colors="k",
    linewidths=0.9,
    linestyles=linestyles,
    alpha=0.55,
)
ax.clabel(cs, fmt="%.1f", fontsize=9, inline=True)

# decision boundary: pi(x)=0.5
ax.contour(xx1, xx2, probs, levels=[0.5], colors="k", linewidths=2.0, linestyles="--")
ax.text(-1.85, 1.85, r"$\pi(\mathbf{x})$ contours", fontsize=10, color="k", alpha=0.75)

ax.scatter(
    class0[:, 0],
    class0[:, 1],
    facecolors="white",
    edgecolors="black",
    label=r"$\mathcal{R}_0$",
)
ax.scatter(
    class1[:, 0],
    class1[:, 1],
    facecolors="black",
    edgecolors="black",
    marker="s",
    label=r"$\mathcal{R}_1$",
)

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_xlabel(r"$x_1$")
ax.set_ylabel(r"$x_2$")
ax.legend(
    frameon=True,
    loc="lower center",
    bbox_to_anchor=(0.5, 1.02),
    ncol=2,
    borderaxespad=0.0,
)
ax.grid(True, alpha=0.15)

fig.tight_layout(rect=(0, 0, 1, 0.95))

fig.savefig(out_dir / "lec2_logistic_boundary.pdf")
fig.savefig(out_dir / "lec2_logistic_boundary.png", dpi=300)
print(f"Saved to {out_dir}")
