import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

from figure_style import apply_style

apply_style(
    font_size=11,
    axes_labelsize=12,
    extra_rc={
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
    },
)

a = np.linspace(0, 1, 200)
b = np.linspace(0, 1, 200)
A, B = np.meshgrid(a, b)

T_min = np.minimum(A, B)
T_prod = A * B

out_dir = Path(__file__).resolve().parents[1] / "assets" / "lec16"
out_dir.mkdir(parents=True, exist_ok=True)

fig, axes = plt.subplots(1, 2, figsize=(6.4, 3.2), constrained_layout=True)
for ax, Z, title in zip(axes, [T_min, T_prod], [r"$T_{\min}(a,b)$", r"$T_{\Pi}(a,b)=ab$"]):
    levels = np.linspace(0, 1, 11)
    # Ebook-first: keep a vivid palette, but choose one with monotone luminance so it
    # still degrades gracefully in grayscale.
    ax.contourf(A, B, Z, levels=levels, cmap="viridis", vmin=0, vmax=1)
    cs = ax.contour(A, B, Z, levels=np.linspace(0, 1, 6), colors="k", linewidths=0.7, alpha=0.45)
    ax.clabel(cs, fmt="%.1f", fontsize=9, inline=True)
    ax.set_xlabel(r"$a$")
    ax.set_ylabel(r"$b$")
    ax.set_title(title)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.grid(False)

fig.savefig(out_dir / "lec16_fuzzy_and.pdf")
fig.savefig(out_dir / "lec16_fuzzy_and.png", dpi=300)
print(f"Saved to {out_dir}")
