import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from pathlib import Path


plt.rcParams.update(
    {
        "font.family": "serif",
        "font.size": 11,
        "axes.axisbelow": True,
    }
)

out_dir = Path(__file__).resolve().parents[1] / "assets" / "lec7"
out_dir.mkdir(parents=True, exist_ok=True)


def draw_box(ax, center, width, height, label, facecolor="#d0e4f5"):
    x, y = center
    rect = Rectangle(
        (x - width / 2, y - height / 2),
        width,
        height,
        facecolor=facecolor,
        edgecolor="black",
        linewidth=1.0,
        zorder=2,
    )
    ax.add_patch(rect)
    ax.text(x, y, label, ha="center", va="center", zorder=3)
    return rect


def draw_circle(ax, center, radius, label):
    x, y = center
    circ = Circle(
        (x, y),
        radius,
        facecolor="white",
        edgecolor="black",
        linewidth=1.0,
        zorder=2,
    )
    ax.add_patch(circ)
    ax.text(x, y, label, ha="center", va="center", zorder=3)
    return circ


def connect(ax, p1, p2, **kwargs):
    ax.annotate(
        "",
        xy=p2,
        xytext=p1,
        arrowprops=dict(arrowstyle="->", linewidth=1.2, **kwargs),
        zorder=1,
    )


def fig_lstm():
    fig, ax = plt.subplots(figsize=(6, 3))

    # positions
    c_in = (-3.5, 1.5)
    h_in = (-3.5, 0.0)
    x_in = (-3.5, -1.5)

    ft_box = draw_box(ax, (-1.5, 1.5), 1.6, 0.8, r"$f_t=\sigma(\cdot)$")
    it_box = draw_box(ax, (-1.5, 0.0), 1.6, 0.8, r"$i_t=\sigma(\cdot)$")
    ct_box = draw_box(ax, (-1.5, -1.5), 1.9, 0.8, r"$\tilde c_t=\tanh(\cdot)$")

    mul_f = draw_circle(ax, (0.2, 1.5), 0.25, r"$\times$")
    mul_i = draw_circle(ax, (0.2, 0.0), 0.25, r"$\times$")
    plus = draw_circle(ax, (1.5, 0.75), 0.25, r"$+$")
    tanh = draw_box(ax, (2.8, 0.75), 1.4, 0.8, r"$\tanh(\cdot)$", facecolor="#f4e0c9")
    mul_o = draw_circle(ax, (4.3, 0.75), 0.25, r"$\times$")
    ot_box = draw_box(ax, (2.8, 1.8), 1.6, 0.8, r"$o_t=\sigma(\cdot)$")

    # inputs
    ax.text(*c_in, r"$c_{t-1}$", ha="right", va="center")
    ax.text(*h_in, r"$h_{t-1}$", ha="right", va="center")
    ax.text(*x_in, r"$x_t$", ha="right", va="center")

    connect(ax, (c_in[0] + 0.1, c_in[1]), (ft_box.get_x(), c_in[1]))
    connect(ax, (h_in[0] + 0.1, h_in[1]), (it_box.get_x(), h_in[1]))
    connect(ax, (x_in[0] + 0.1, x_in[1]), (ct_box.get_x(), x_in[1]))

    # gates to multipliers
    connect(ax, (ft_box.get_x() + ft_box.get_width(), 1.5), (mul_f.center[0] - 0.3, 1.5))
    connect(ax, (c_in[0] + 0.8, c_in[1]), (mul_f.center[0] - 0.3, 1.8))

    connect(ax, (it_box.get_x() + it_box.get_width(), 0.0), (mul_i.center[0] - 0.3, 0.0))
    connect(ax, (ct_box.get_x() + ct_box.get_width(), -1.5), (mul_i.center[0] - 0.3, -0.3))

    # into plus
    connect(ax, (mul_f.center[0] + 0.3, 1.5), (plus.center[0] - 0.3, 1.1))
    connect(ax, (mul_i.center[0] + 0.3, 0.0), (plus.center[0] - 0.3, 0.4))

    # plus to tanh and c_t label
    connect(ax, (plus.center[0] + 0.3, plus.center[1]), (tanh.get_x() - 0.2, plus.center[1]))
    ax.text(plus.center[0] + 0.4, plus.center[1] + 0.4, r"$c_t$", ha="left", va="bottom")

    # tanh to mult
    connect(ax, (tanh.get_x() + tanh.get_width(), tanh.get_y() + tanh.get_height() / 2),
            (mul_o.center[0] - 0.3, mul_o.center[1]))

    # o_t to mult
    connect(ax, (ot_box.get_x() + ot_box.get_width(), ot_box.get_y() + ot_box.get_height() / 2),
            (mul_o.center[0], mul_o.center[1] + 0.5))

    # output
    connect(ax, (mul_o.center[0] + 0.3, mul_o.center[1]),
            (mul_o.center[0] + 1.2, mul_o.center[1]))
    ax.text(mul_o.center[0] + 1.25, mul_o.center[1], r"$h_t$", ha="left", va="center")

    ax.set_xlim(-4.2, 5.2)
    ax.set_ylim(-2.2, 2.4)
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(out_dir / "lec7_lstm_cell.pdf")
    fig.savefig(out_dir / "lec7_lstm_cell.png", dpi=300)


def fig_gru():
    fig, ax = plt.subplots(figsize=(6, 3))

    h_in = (-3.5, 1.0)
    x_in = (-3.5, -1.0)

    z_box = draw_box(ax, (-1.5, 1.0), 1.6, 0.8, r"$z_t=\sigma(\cdot)$")
    r_box = draw_box(ax, (-1.5, -1.0), 1.6, 0.8, r"$r_t=\sigma(\cdot)$")
    htilde_box = draw_box(ax, (1.0, -1.0), 2.0, 0.8, r"$\tilde h_t=\tanh(\cdot)$", facecolor="#f4e0c9")

    mix1 = draw_circle(ax, (3.0, -1.0), 0.25, r"$\times$")
    mix2 = draw_circle(ax, (3.0, 1.0), 0.25, r"$\times$")
    plus = draw_circle(ax, (4.5, 0.0), 0.25, r"$+$")

    ax.text(*h_in, r"$h_{t-1}$", ha="right", va="center")
    ax.text(*x_in, r"$x_t$", ha="right", va="center")

    # inputs to gates
    connect(ax, (h_in[0] + 0.1, h_in[1]), (z_box.get_x(), h_in[1]))
    connect(ax, (x_in[0] + 0.1, x_in[1]), (r_box.get_x(), x_in[1]))

    # gate to candidate
    connect(ax, (r_box.get_x() + r_box.get_width(), -1.0),
            (htilde_box.get_x() - 0.2, -1.0))
    connect(ax, (h_in[0] + 0.7, h_in[1]), (htilde_box.get_x() - 0.2, -0.4))

    # candidate and gates to mixers
    connect(ax, (htilde_box.get_x() + htilde_box.get_width(), -1.0),
            (mix2.center[0] - 0.3, -1.0))
    connect(ax, (h_in[0] + 0.7, h_in[1]),
            (mix1.center[0] - 0.3, 1.0))
    connect(ax, (z_box.get_x() + z_box.get_width(), 1.0),
            (mix1.center[0] - 0.3, 1.0))
    connect(ax, (z_box.get_x() + z_box.get_width(), 1.0),
            (mix2.center[0] - 0.3, -0.4))

    # to plus and output
    connect(ax, (mix1.center[0] + 0.3, 1.0),
            (plus.center[0] - 0.3, 0.4))
    connect(ax, (mix2.center[0] + 0.3, -1.0),
            (plus.center[0] - 0.3, -0.4))

    connect(ax, (plus.center[0] + 0.3, 0.0),
            (plus.center[0] + 1.2, 0.0))
    ax.text(plus.center[0] + 1.25, 0.0, r"$h_t$", ha="left", va="center")

    ax.set_xlim(-4.2, 5.5)
    ax.set_ylim(-2.0, 2.0)
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(out_dir / "lec7_gru_cell.pdf")
    fig.savefig(out_dir / "lec7_gru_cell.png", dpi=300)


if __name__ == "__main__":
    fig_lstm()
    fig_gru()
    print(f"Saved LSTM/GRU cell diagrams to {out_dir}")

