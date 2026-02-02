import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

from figure_style import apply_style

np.random.seed(1)
apply_style(font_size=11)

# XOR data
X = np.array([[0, 0], [1, 0], [0, 1], [1, 1]], dtype=float)
y = np.array([0, 1, 1, 0], dtype=float)

centers = X.copy()
sigma = 0.8
lam = 1e-3

# radial basis features
def rbf(x, c):
    return np.exp(-np.sum((x - c) ** 2, axis=-1) / (2 * sigma ** 2))

Phi = np.stack([rbf(X, c) for c in centers], axis=1)
w = np.linalg.solve(Phi.T @ Phi + lam * np.eye(Phi.shape[1]), Phi.T @ y)

# grid
x1 = np.linspace(-0.2, 1.2, 200)
x2 = np.linspace(-0.2, 1.2, 200)
xx1, xx2 = np.meshgrid(x1, x2)
grid = np.stack([xx1.ravel(), xx2.ravel()], axis=1)
Phi_grid = np.stack([rbf(grid, c) for c in centers], axis=1)
outputs = Phi_grid @ w
outputs = outputs.reshape(xx1.shape)
pred = outputs >= 0.5

out_dir = Path(__file__).resolve().parents[1] / "assets" / "lec8"
out_dir.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(4.5, 3.6))
ax.contourf(
    xx1,
    xx2,
    pred.astype(int),
    levels=[-0.5, 0.5, 1.5],
    # Ebook-first, but still grayscale-friendly: two light tints with distinct luminance.
    # class 0 -> light blue, class 1 -> light orange
    colors=["#E8F1FB", "#FFF0D6"],
)
ax.contour(xx1, xx2, outputs, levels=[0.5], colors="k", linewidths=2.0)

ax.scatter(
    X[y == 0][:, 0],
    X[y == 0][:, 1],
    facecolors="white",
    edgecolors="black",
    s=70,
    label="class 0",
)
ax.scatter(
    X[y == 1][:, 0],
    X[y == 1][:, 1],
    facecolors="black",
    edgecolors="black",
    s=70,
    marker="s",
    label="class 1",
)
ax.set_xlabel(r"$x_1$")
ax.set_ylabel(r"$x_2$")
ax.set_xlim(-0.2, 1.2)
ax.set_ylim(-0.2, 1.2)
ax.grid(True, color="0.88", linewidth=0.8)
ax.legend(
    loc="upper center",
    # Place legend outside the axes so it doesn't cover the XOR corner points.
    bbox_to_anchor=(0.5, 1.18),
    ncol=2,
    frameon=False,
    borderaxespad=0.25,
)
fig.subplots_adjust(top=0.82)

fig.savefig(out_dir / "lec8_rbf_xor.pdf")
fig.savefig(out_dir / "lec8_rbf_xor.png", dpi=300)
print(f"Saved to {out_dir}")
