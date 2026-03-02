"""
Quick sanity checks for numerical examples up to Chapter 18.

- Hopfield 3-neuron energy monotonicity (Ch. 10)
- Perceptron OR-gate update trace (Ch. 5)
- CNN flattening parameter count + 1D stride/padding cross-correlation + shape bookkeeping (Ch. 11)
- 1D stride/padding attention toy (Ch. 11)
- RNN 2-step BPTT gradient accumulation sanity check (Ch. 12)
- Skip-gram with negative sampling loss (Ch. 14)
- Max–min fuzzy relation composition matrix (Ch. 17)
- Alpha-cut mapping for y = x^2 (Ch. 17)
- Mamdani thermostat centroid (Ch. 18)
- Roulette selection example (Ch. 19)
- GA toy initial population bounds (Ch. 19)
"""

import numpy as np
from math import exp
from pathlib import Path


def check_perceptron_or_gate_trace():
    """
    Perceptron mistake-driven update trace for the OR gate (Ch. 5).

    Setup:
      - Inputs in fixed cycle order: (0,0),(0,1),(1,0),(1,1)
      - Targets y in {-1,+1}: (-1,+1,+1,+1)
      - Learning rate eta=1
      - Initialize w=(0,0), b=0
      - Update on margin <= 0: w <- w + y x, b <- b + y

    Returns the post-update (w,b) states for each mistake.
    """
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
    y = np.array([-1, 1, 1, 1], dtype=float)

    w = np.zeros(2, dtype=float)
    b = 0.0
    eta = 1.0

    trace = []
    step = 0
    for epoch in range(1, 51):
        mistakes = 0
        for idx, (x, yi) in enumerate(zip(X, y), start=1):
            margin = yi * (float(w @ x) + b)
            if margin <= 0.0:
                w = w + eta * yi * x
                b = b + eta * yi
                step += 1
                mistakes += 1
                trace.append(
                    dict(
                        step=step,
                        epoch=epoch,
                        idx=idx,
                        x1=int(x[0]),
                        x2=int(x[1]),
                        y=int(yi),
                        w1=int(w[0]),
                        w2=int(w[1]),
                        b=int(b),
                    )
                )
        if mistakes == 0:
            break

    return dict(
        final_w=(int(w[0]), int(w[1])),
        final_b=int(b),
        epochs=epoch,
        num_updates=step,
        trace=trace,
    )


def check_chapter12_bptt_two_step() -> dict[str, float]:
    """
    Two-step scalar RNN + squared-error objective to show that shared weights
    accumulate gradient contributions across time (Ch. 12).

    Model:
      h_t = W_hh h_{t-1} + W_xh x_t,  y_t = h_t
      L = 0.5 * [(y1-t1)^2 + (y2-t2)^2]

    Parameters (as used in the boxed example):
      h0=1, W_hh=0.5, W_xh=1, x1=1, x2=2, t1=1, t2=2
    """

    h0 = 1.0
    W_hh = 0.5
    W_xh = 1.0
    x1, x2 = 1.0, 2.0
    t1, t2 = 1.0, 2.0

    def forward(W_hh_val: float, W_xh_val: float) -> tuple[float, float, float, float, float]:
        h1 = W_hh_val * h0 + W_xh_val * x1
        h2 = W_hh_val * h1 + W_xh_val * x2
        e1 = h1 - t1
        e2 = h2 - t2
        L = 0.5 * (e1 * e1 + e2 * e2)
        return L, h1, h2, e1, e2

    L, h1, h2, e1, e2 = forward(W_hh, W_xh)

    dh1_dWhh = h0
    dh2_dWhh = h1 + W_hh * dh1_dWhh
    dL_dWhh = e1 * dh1_dWhh + e2 * dh2_dWhh

    eps = 1e-6
    Lp, *_ = forward(W_hh + eps, W_xh)
    Lm, *_ = forward(W_hh - eps, W_xh)
    fd = (Lp - Lm) / (2.0 * eps)

    return dict(
        L=L,
        h1=h1,
        h2=h2,
        e1=e1,
        e2=e2,
        dL_dWhh=dL_dWhh,
        dL_dWhh_fd=fd,
        dL_dWhh_abs_err=abs(fd - dL_dWhh),
    )


def hopfield_energy(w, s, theta=None):
    """Energy E = -0.5 sum_{i,j} w_ij s_i s_j + sum_i theta_i s_i."""
    s = np.asarray(s)
    w = np.asarray(w)
    theta = np.zeros_like(s) if theta is None else np.asarray(theta)
    return -0.5 * np.sum(w * np.outer(s, s)) + np.sum(theta * s)


def _extract_qc_block(tex_text: str, name: str) -> list[str]:
    begin = f"% QC-BEGIN: {name}"
    end = f"% QC-END: {name}"
    i0 = tex_text.find(begin)
    if i0 == -1:
        raise AssertionError(f"Missing QC block begin marker for {name}")
    i1 = tex_text.find(end, i0)
    if i1 == -1:
        raise AssertionError(f"Missing QC block end marker for {name}")
    block = tex_text[i0 + len(begin) : i1].splitlines()
    lines = []
    for raw in block:
        s = raw.strip()
        if not s.startswith("%"):
            continue
        payload = s.lstrip("%").strip()
        if not payload:
            continue
        lines.append(payload)
    return lines


def check_hopfield():
    """
    Hopfield 3-neuron energy check (Ch. 10), QC-backed from the TeX source.

    Verifies the energies reported in the example, plus one asynchronous update
    from a noisy probe back to the stored pattern.
    """
    root = Path(__file__).resolve().parents[1]
    tex = (root / "lecture_5_part_ii.tex").read_text(encoding="utf-8", errors="ignore")
    qc = _extract_qc_block(tex, "hopfield_energy_example")

    W_rows = []
    theta = None
    cases = {}
    noisy = None

    for line in qc:
        parts = line.split()
        tag = parts[0]
        if tag == "W":
            if len(parts) != 4:
                raise AssertionError(f"Malformed Hopfield QC W row: {line!r}")
            W_rows.append([float(parts[1]), float(parts[2]), float(parts[3])])
        elif tag == "theta":
            if len(parts) != 4:
                raise AssertionError(f"Malformed Hopfield QC theta row: {line!r}")
            theta = np.array([float(parts[1]), float(parts[2]), float(parts[3])], dtype=float)
        elif tag in ("s0", "flip_s1", "flip_s2", "flip_s3"):
            if len(parts) != 6 or parts[4] != "E":
                raise AssertionError(f"Malformed Hopfield QC case row: {line!r}")
            s = np.array([float(parts[1]), float(parts[2]), float(parts[3])], dtype=float)
            E = float(parts[5])
            cases[tag] = (s, E)
        elif tag == "noisy":
            # noisy 1 1 1 update_i 3 s1 1 1 -1 E -5
            if len(parts) != 12 or parts[4] != "update_i" or parts[6] != "s1" or parts[10] != "E":
                raise AssertionError(f"Malformed Hopfield QC noisy row: {line!r}")
            s_noisy = np.array([float(parts[1]), float(parts[2]), float(parts[3])], dtype=float)
            update_i = int(parts[5])
            s_after = np.array([float(parts[7]), float(parts[8]), float(parts[9])], dtype=float)
            E_after = float(parts[11])
            noisy = (s_noisy, update_i, s_after, E_after)

    if len(W_rows) != 3:
        raise AssertionError("Hopfield QC must include 3 W rows")
    if theta is None:
        raise AssertionError("Hopfield QC missing theta row")
    if set(cases.keys()) != {"s0", "flip_s1", "flip_s2", "flip_s3"}:
        raise AssertionError("Hopfield QC missing one of s0/flip_s1/flip_s2/flip_s3")
    if noisy is None:
        raise AssertionError("Hopfield QC missing noisy update row")

    W = np.array(W_rows, dtype=float)

    energies = {}
    for name, (s, E_expected) in cases.items():
        E = hopfield_energy(W, s, theta=theta)
        if abs(E - E_expected) > 1e-9:
            raise AssertionError(f"Hopfield {name} energy mismatch: actual={E}, expected={E_expected}")
        energies[name] = E

    s_noisy, update_i, s_after, E_after_expected = noisy
    i = update_i - 1
    h = float(W[i] @ s_noisy - theta[i])
    s_next = s_noisy.copy()
    s_next[i] = 1.0 if h >= 0.0 else -1.0
    if not np.allclose(s_next, s_after):
        raise AssertionError(f"Hopfield noisy update state mismatch: actual={s_next}, expected={s_after}")
    E_after = hopfield_energy(W, s_next, theta=theta)
    if abs(E_after - E_after_expected) > 1e-9:
        raise AssertionError(f"Hopfield noisy update energy mismatch: actual={E_after}, expected={E_after_expected}")
    energies["noisy_after"] = E_after

    # Optional QC-backed Hebbian single-pattern weight example (4 neurons).
    # This is separate from the 3-neuron energy-descent example and is meant
    # to verify the explicit matrix shown in the text.
    if "% QC-BEGIN: hopfield_single_pattern_weights" in tex:
        qc2 = _extract_qc_block(tex, "hopfield_single_pattern_weights")
        b = None
        W2_rows = []
        h_expected = None
        recall_s0 = None
        recall_E0 = None
        recall_steps = []
        for line in qc2:
            parts = line.split()
            tag = parts[0]
            if tag in ("b", "xi"):
                if len(parts) != 5:
                    raise AssertionError(f"Malformed Hopfield QC b row: {line!r}")
                b = np.array([float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4])], dtype=float)
            elif tag == "W":
                if len(parts) != 5:
                    raise AssertionError(f"Malformed Hopfield QC W row (4D): {line!r}")
                W2_rows.append([float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4])])
            elif tag == "h":
                if len(parts) != 5:
                    raise AssertionError(f"Malformed Hopfield QC h row: {line!r}")
                h_expected = np.array(
                    [float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4])], dtype=float
                )
            elif tag == "recall_s0":
                # recall_s0 1 -1 -1 -1 E 0.5
                if len(parts) != 7 or parts[5] != "E":
                    raise AssertionError(f"Malformed Hopfield QC recall_s0 row: {line!r}")
                recall_s0 = np.array([float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4])], dtype=float)
                recall_E0 = float(parts[6])
            elif tag == "recall_step":
                # recall_step 1 update_i 2 h 0.25 s 1 1 -1 -1 E 0.0
                if (
                    len(parts) != 13
                    or parts[2] != "update_i"
                    or parts[4] != "h"
                    or parts[6] != "s"
                    or parts[11] != "E"
                ):
                    raise AssertionError(f"Malformed Hopfield QC recall_step row: {line!r}")
                step = int(parts[1])
                update_i = int(parts[3])
                h = float(parts[5])
                s_after = np.array([float(parts[7]), float(parts[8]), float(parts[9]), float(parts[10])], dtype=float)
                E_after = float(parts[12])
                recall_steps.append((step, update_i, h, s_after, E_after))

        if b is None:
            raise AssertionError("Hopfield QC (single pattern) missing b row")
        if len(W2_rows) != 4:
            raise AssertionError("Hopfield QC (single pattern) must include 4 W rows")
        if h_expected is None:
            raise AssertionError("Hopfield QC (single pattern) missing h row")

        n = b.size
        W2 = np.array(W2_rows, dtype=float)
        W2_expected = np.outer(b, b) / float(n)
        np.fill_diagonal(W2_expected, 0.0)
        if not np.allclose(W2, W2_expected, atol=1e-12, rtol=0.0):
            raise AssertionError("Hopfield single-pattern W mismatch vs Hebbian formula")

        h = W2 @ b
        if not np.allclose(h, h_expected, atol=1e-12, rtol=0.0):
            raise AssertionError(f"Hopfield single-pattern h mismatch: actual={h}, expected={h_expected}")

        b_hat = np.where(h >= 0.0, 1.0, -1.0)
        if not np.allclose(b_hat, b):
            raise AssertionError(f"Hopfield single-pattern fixed-point mismatch: sign(Wb)={b_hat}, b={b}")

        if recall_s0 is not None:
            if recall_E0 is None:
                raise AssertionError("Hopfield QC recall_s0 missing E value")
            E0 = hopfield_energy(W2, recall_s0, theta=np.zeros_like(recall_s0))
            if abs(E0 - recall_E0) > 1e-12:
                raise AssertionError(f"Hopfield recall E0 mismatch: actual={E0}, expected={recall_E0}")

            # Validate each step as an asynchronous sign update from the previous state.
            s_prev = recall_s0.copy()
            for (step, update_i, h_exp, s_after, E_after_exp) in sorted(recall_steps, key=lambda t: t[0]):
                i = update_i - 1
                h_act = float(W2[i] @ s_prev)
                if abs(h_act - h_exp) > 1e-12:
                    raise AssertionError(f"Hopfield recall step {step} h mismatch: actual={h_act}, expected={h_exp}")
                s_next = s_prev.copy()
                s_next[i] = 1.0 if h_act >= 0.0 else -1.0
                if not np.allclose(s_next, s_after, atol=1e-12, rtol=0.0):
                    raise AssertionError(
                        f"Hopfield recall step {step} state mismatch: actual={s_next}, expected={s_after}"
                    )
                E_act = hopfield_energy(W2, s_next, theta=np.zeros_like(s_next))
                if abs(E_act - E_after_exp) > 1e-12:
                    raise AssertionError(
                        f"Hopfield recall step {step} energy mismatch: actual={E_act}, expected={E_after_exp}"
                    )
                s_prev = s_next

        energies["hebbian_single_pattern_h1"] = float(h[0])
        energies["hebbian_single_pattern_h2"] = float(h[1])
        energies["hebbian_single_pattern_h3"] = float(h[2])
        energies["hebbian_single_pattern_h4"] = float(h[3])

    # QC-backed 4-neuron, one-flip memory recovery example (separate section).
    if "% QC-BEGIN: hopfield_memory_recovery_4n" in tex:
        qc3 = _extract_qc_block(tex, "hopfield_memory_recovery_4n")
        xi = None
        W3_rows = []
        s0 = None
        E0_expected = None
        step = None
        update_i = None
        h_expected = None
        s_after_expected = None
        E_after_expected = None

        for line in qc3:
            parts = line.split()
            tag = parts[0]
            if tag == "xi":
                if len(parts) != 5:
                    raise AssertionError(f"Malformed Hopfield QC xi row: {line!r}")
                xi = np.array([float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4])], dtype=float)
            elif tag == "W":
                if len(parts) != 5:
                    raise AssertionError(f"Malformed Hopfield QC W row (4D): {line!r}")
                W3_rows.append([float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4])])
            elif tag == "s0":
                if len(parts) != 7 or parts[5] != "E":
                    raise AssertionError(f"Malformed Hopfield QC s0 row (4D): {line!r}")
                s0 = np.array([float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4])], dtype=float)
                E0_expected = float(parts[6])
            elif tag == "step":
                # step 1 update_i 4 h -0.75 s -1 -1 1 -1 E -1.5
                if (
                    len(parts) != 13
                    or parts[2] != "update_i"
                    or parts[4] != "h"
                    or parts[6] != "s"
                    or parts[11] != "E"
                ):
                    raise AssertionError(f"Malformed Hopfield QC step row (4D): {line!r}")
                step = int(parts[1])
                update_i = int(parts[3])
                h_expected = float(parts[5])
                s_after_expected = np.array([float(parts[7]), float(parts[8]), float(parts[9]), float(parts[10])], dtype=float)
                E_after_expected = float(parts[12])

        if xi is None:
            raise AssertionError("Hopfield QC (memory recovery) missing xi row")
        if len(W3_rows) != 4:
            raise AssertionError("Hopfield QC (memory recovery) must include 4 W rows")
        if s0 is None or E0_expected is None:
            raise AssertionError("Hopfield QC (memory recovery) missing s0/E0")
        if step is None or update_i is None or h_expected is None or s_after_expected is None or E_after_expected is None:
            raise AssertionError("Hopfield QC (memory recovery) missing step payload")
        if step != 1:
            raise AssertionError("Hopfield QC (memory recovery) expects exactly step 1")

        W3 = np.array(W3_rows, dtype=float)
        n = xi.size
        W3_expected = np.outer(xi, xi) / float(n)
        np.fill_diagonal(W3_expected, 0.0)
        if not np.allclose(W3, W3_expected, atol=1e-12, rtol=0.0):
            raise AssertionError("Hopfield memory-recovery W mismatch vs Hebbian formula")

        theta3 = np.zeros_like(xi)
        E0 = hopfield_energy(W3, s0, theta=theta3)
        if abs(E0 - E0_expected) > 1e-12:
            raise AssertionError(f"Hopfield memory-recovery E0 mismatch: actual={E0}, expected={E0_expected}")

        i = update_i - 1
        h_act = float(W3[i] @ s0)
        if abs(h_act - h_expected) > 1e-12:
            raise AssertionError(f"Hopfield memory-recovery h mismatch: actual={h_act}, expected={h_expected}")

        s_next = s0.copy()
        s_next[i] = 1.0 if h_act >= 0.0 else -1.0
        if not np.allclose(s_next, s_after_expected, atol=1e-12, rtol=0.0):
            raise AssertionError(
                f"Hopfield memory-recovery state mismatch: actual={s_next}, expected={s_after_expected}"
            )

        E_after = hopfield_energy(W3, s_next, theta=theta3)
        if abs(E_after - E_after_expected) > 1e-12:
            raise AssertionError(f"Hopfield memory-recovery E_after mismatch: actual={E_after}, expected={E_after_expected}")

        energies["memory_recovery_h"] = float(h_act)
        energies["memory_recovery_E0"] = float(E0)
        energies["memory_recovery_E1"] = float(E_after)

    return energies


def check_cnn_flatten_params() -> dict[str, float]:
    """
    CNN flattening parameter-count sanity check (Ch. 11), QC-backed from the TeX source.

    Verifies the vectorized input dimension and the first-layer parameter count used in the
    ``fully connected layers break on images'' motivation.
    """
    root = Path(__file__).resolve().parents[1]
    tex = (root / "lecture_6.tex").read_text(encoding="utf-8", errors="ignore")
    qc = _extract_qc_block(tex, "cnn_flatten_params")

    H = W = vec = hidden = W1 = classes = W2 = rule = nparams = approx = None
    for line in qc:
        parts = line.split()
        tag = parts[0]
        if tag == "H":
            # H 256 W 256 vec 65536
            if len(parts) != 6 or parts[2] != "W" or parts[4] != "vec":
                raise AssertionError(f"Malformed CNN flatten QC line: {line!r}")
            H = int(parts[1])
            W = int(parts[3])
            vec = int(parts[5])
        elif tag == "hidden":
            # hidden 100 W1 6553600
            if len(parts) != 4 or parts[2] != "W1":
                raise AssertionError(f"Malformed CNN flatten QC hidden line: {line!r}")
            hidden = int(parts[1])
            W1 = int(parts[3])
        elif tag == "classes":
            # classes 4 W2 400
            if len(parts) != 4 or parts[2] != "W2":
                raise AssertionError(f"Malformed CNN flatten QC classes line: {line!r}")
            classes = int(parts[1])
            W2 = int(parts[3])
        elif tag == "samples_rule":
            # samples_rule 10 Nparams 6553600 approx 65536000
            if len(parts) != 6 or parts[2] != "Nparams" or parts[4] != "approx":
                raise AssertionError(f"Malformed CNN flatten QC samples_rule line: {line!r}")
            rule = int(parts[1])
            nparams = int(parts[3])
            approx = int(parts[5])

    for name, val in (
        ("H/W/vec", (H, W, vec)),
        ("hidden/W1", (hidden, W1)),
        ("classes/W2", (classes, W2)),
        ("rule/nparams/approx", (rule, nparams, approx)),
    ):
        if any(v is None for v in val):
            raise AssertionError(f"CNN flatten QC missing {name}")

    computed_vec = int(H * W)
    if computed_vec != vec:
        raise AssertionError(f"CNN vec mismatch: actual={computed_vec}, expected={vec}")
    computed_W1 = int(vec * hidden)
    if computed_W1 != W1:
        raise AssertionError(f"CNN W1 mismatch: actual={computed_W1}, expected={W1}")
    computed_W2 = int(hidden * classes)
    if computed_W2 != W2:
        raise AssertionError(f"CNN W2 mismatch: actual={computed_W2}, expected={W2}")
    computed_approx = int(rule * nparams)
    if computed_approx != approx:
        raise AssertionError(f"CNN sample-rule approx mismatch: actual={computed_approx}, expected={approx}")

    return dict(vec=float(vec), W1=float(W1), W2=float(W2), approx=float(approx))


def check_cnn_1d_xcorr_stride_pad() -> dict[str, float | list[float]]:
    """
    1D cross-correlation numeric example (Ch. 11), QC-backed from the TeX source.

    Verifies the output length and values for the stride/padding worked example.
    """
    root = Path(__file__).resolve().parents[1]
    tex = (root / "lecture_6.tex").read_text(encoding="utf-8", errors="ignore")
    qc = _extract_qc_block(tex, "cnn_1d_xcorr_stride_pad")

    x = w = None
    p = s = L = None
    y_expected = None
    for line in qc:
        parts = line.split()
        tag = parts[0]
        if tag == "x":
            x = np.array([float(v) for v in parts[1:]], dtype=float)
        elif tag == "w":
            w = np.array([float(v) for v in parts[1:]], dtype=float)
        elif tag == "p":
            p = int(parts[1])
        elif tag == "s":
            s = int(parts[1])
        elif tag == "L":
            L = int(parts[1])
        elif tag == "y":
            y_expected = [float(v) for v in parts[1:]]

    if x is None or w is None or p is None or s is None or L is None or y_expected is None:
        raise AssertionError("CNN 1D xcorr QC missing x/w/p/s/L/y")

    n = int(x.shape[0])
    k = int(w.shape[0])
    L_computed = int((n + 2 * p - k) // s + 1)
    if L_computed != L:
        raise AssertionError(f"CNN 1D xcorr L mismatch: actual={L_computed}, expected={L}")

    x_pad = np.pad(x, (p, p), mode="constant", constant_values=0.0)
    y = []
    for i in range(L_computed):
        start = i * s
        window = x_pad[start : start + k]
        y.append(float(np.dot(window, w)))

    if len(y_expected) != len(y) or any(abs(a - b) > 1e-9 for a, b in zip(y, y_expected)):
        raise AssertionError(f"CNN 1D xcorr y mismatch: actual={y}, expected={y_expected}")

    return dict(L=float(L_computed), y=y)


def check_cnn_shape_bookkeeping() -> dict[str, float]:
    """
    CNN shape bookkeeping example (Ch. 11), QC-backed from the TeX source.

    Verifies the conv output size, pooling output size, and flatten dimension.
    """
    root = Path(__file__).resolve().parents[1]
    tex = (root / "lecture_6.tex").read_text(encoding="utf-8", errors="ignore")
    qc = _extract_qc_block(tex, "cnn_shape_bookkeeping")

    H = W = Cin = None
    k = stride = pad = Cout = outH = outW = None
    pool = pool_stride = poolH = poolW = None
    flat = None

    for line in qc:
        parts = line.split()
        tag = parts[0]
        if tag == "input":
            if len(parts) != 4:
                raise AssertionError(f"Malformed CNN shape QC input line: {line!r}")
            H, W, Cin = map(int, parts[1:])
        elif tag == "conv":
            # conv k 3 stride 1 pad 0 cout 10 out_hw 48 48
            if len(parts) != 12 or parts[1] != "k" or parts[3] != "stride" or parts[5] != "pad" or parts[7] != "cout" or parts[9] != "out_hw":
                raise AssertionError(f"Malformed CNN shape QC conv line: {line!r}")
            k = int(parts[2])
            stride = int(parts[4])
            pad = int(parts[6])
            Cout = int(parts[8])
            outH = int(parts[10])
            outW = int(parts[11])
        elif tag == "pool":
            # pool window 2 stride 2 out_hw 24 24
            if len(parts) != 8 or parts[1] != "window" or parts[3] != "stride" or parts[5] != "out_hw":
                raise AssertionError(f"Malformed CNN shape QC pool line: {line!r}")
            pool = int(parts[2])
            pool_stride = int(parts[4])
            poolH = int(parts[6])
            poolW = int(parts[7])
        elif tag == "flatten":
            if len(parts) != 2:
                raise AssertionError(f"Malformed CNN shape QC flatten line: {line!r}")
            flat = int(parts[1])

    if any(v is None for v in (H, W, Cin, k, stride, pad, Cout, outH, outW, pool, pool_stride, poolH, poolW, flat)):
        raise AssertionError("CNN shape QC missing one or more required fields")

    outH_c = int((H + 2 * pad - k) // stride + 1)
    outW_c = int((W + 2 * pad - k) // stride + 1)
    if outH_c != outH or outW_c != outW:
        raise AssertionError(f"CNN conv out_hw mismatch: actual={(outH_c, outW_c)}, expected={(outH, outW)}")

    poolH_c = int((outH_c - pool) // pool_stride + 1)
    poolW_c = int((outW_c - pool) // pool_stride + 1)
    if poolH_c != poolH or poolW_c != poolW:
        raise AssertionError(f"CNN pool out_hw mismatch: actual={(poolH_c, poolW_c)}, expected={(poolH, poolW)}")

    flat_c = int(poolH_c * poolW_c * Cout)
    if flat_c != flat:
        raise AssertionError(f"CNN flatten mismatch: actual={flat_c}, expected={flat}")

    return dict(out_hw=float(outH_c), pool_hw=float(poolH_c), flat=float(flat_c))


def check_stride_pad():
    x = np.array([1, 2, 0, 3, 1])
    w = np.array([1, 0, -1])
    p, s = 1, 2
    xp = np.pad(x, (p, p))
    L = (len(xp) - len(w)) // s + 1
    y = np.array([np.dot(w, xp[i : i + len(w)]) for i in range(0, L * s, s)])
    return dict(L=L, xp=xp.tolist(), y=y.tolist())


def _softmax_row(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    x = x - np.max(x)
    ex = np.exp(x)
    return ex / np.sum(ex)


def check_tiny_causal_attention():
    """
    Two-token, one-head causal self-attention sanity check (Ch. 14).

    Q = [[1,0],[0,1]]
    K = [[1,0],[1,1]]
    V = [[1,0],[0,2]]

    Scores = Q K^T / sqrt(2) = [[0.707, 0.707], [0, 0.707]]
    Causal mask forces token 1 to attend only to itself.
    """
    Q = np.array([[1.0, 0.0], [0.0, 1.0]])
    K = np.array([[1.0, 0.0], [1.0, 1.0]])
    V = np.array([[1.0, 0.0], [0.0, 2.0]])
    dk = Q.shape[1]

    scores = (Q @ K.T) / np.sqrt(dk)

    # Causal mask: disallow attending to future positions (upper triangle).
    masked = scores.copy()
    masked[np.triu(np.ones_like(masked, dtype=bool), k=1)] = -1e9

    weights = np.vstack([_softmax_row(masked[i]) for i in range(masked.shape[0])])
    out = weights @ V
    return dict(scores=scores.tolist(), weights=weights.tolist(), out=out.tolist())


def sigmoid(z: float) -> float:
    return 1 / (1 + exp(-z))


def check_sgns():
    """
    Skip-gram with negative sampling: one positive, k=2 negatives.
    Dot products: pos=1.0, negs = [-0.5, -1.2].
    Loss = -log σ(pos) - sum log σ(-neg_i)
    """
    pos = 1.0
    negs = [-0.5, -1.2]
    loss = -np.log(sigmoid(pos)) - sum(np.log(sigmoid(-n)) for n in negs)
    return dict(loss=loss, pos=pos, negs=negs)


def check_fuzzy_composition():
    """Reproduce the max–min composition matrix in Ch. 17."""
    R1 = np.array([[0.2, 0.9], [0.5, 0.1]])
    R2 = np.array([[0.7, 0.3], [0.4, 0.8]])
    R = np.zeros((2, 2))
    for i in range(R1.shape[0]):
        for k in range(R2.shape[1]):
            acc = 0.0
            for j in range(R1.shape[1]):
                acc = max(acc, min(R1[i, j], R2[j, k]))
            R[i, k] = acc
    return dict(R=R.tolist())


def check_alpha_cut_mapping():
    """Map a symmetric triangular fuzzy number under y = x^2 via alpha-cuts."""
    # Triangle with support [-1,1], peak at 0: mu(x)=1-|x|
    def mu_A(x):
        return max(0.0, 1 - abs(x))

    alpha = 0.6
    # A_alpha = [-0.4, 0.4]
    A_alpha = (-1 + alpha, 1 - alpha)
    # Map via y=x^2: intervals [0, 0.16] and [0, 0.16] collapse; image is [0, 0.16]
    y_interval = (0.0, A_alpha[1] ** 2)
    # Peak membership stays at 1; at y=0.16 membership = alpha
    return dict(alpha=alpha, A_alpha=A_alpha, y_interval=y_interval, mu_peak=1.0)


def check_mamdani_centroid():
    """
    Replicate the thermostat example (Ch. 18): T=27C, min-implication,
    max aggregation, centroid defuzzification.
    """
    # Triangle helper: given (a,b,c), return mu(x)
    def tri_mu(x, a, b, c):
        if x <= a or x >= c:
            return 0.0
        if x == b:
            return 1.0
        if x < b:
            return (x - a) / (b - a)
        return (c - x) / (c - b)

    # Temperature memberships (Cold, Warm, Hot)
    def mu_cold(t):
        return max(0.0, 1 - (t - 0) / (15 - 0)) if t <= 15 else 0.0

    def mu_warm(t):
        return max(0.0, 1 - abs(t - 20) / 10)

    def mu_hot(t):
        return 0.0 if t <= 25 else min(1.0, (t - 25) / (40 - 25))

    T = 27.0
    alpha_cold = mu_cold(T)
    alpha_warm = mu_warm(T)
    alpha_hot = mu_hot(T)

    # Fan speed triangles (Low, Medium, High)
    def mu_low(s):
        return tri_mu(s, 0.0, 0.0, 0.5)

    def mu_med(s):
        return tri_mu(s, 0.25, 0.5, 0.75)

    def mu_high(s):
        return tri_mu(s, 0.5, 1.0, 1.0)

    # Min-implication (clipping), max aggregation
    s = np.linspace(0, 1, 10001)
    mu_low_clip = np.minimum(alpha_cold, [mu_low(x) for x in s])
    mu_med_clip = np.minimum(alpha_warm, [mu_med(x) for x in s])
    mu_high_clip = np.minimum(alpha_hot, [mu_high(x) for x in s])
    mu_agg = np.maximum.reduce([mu_low_clip, mu_med_clip, mu_high_clip])

    num = np.trapz(s * mu_agg, s)
    den = np.trapz(mu_agg, s)
    centroid = num / den if den > 0 else None
    return dict(
        alpha_cold=alpha_cold,
        alpha_warm=alpha_warm,
        alpha_hot=alpha_hot,
        centroid=centroid,
    )


def check_roulette_selection():
    """Roulette example: fitness [10,20,5,15,50] -> probabilities sum to 1."""
    fitness = np.array([10, 20, 5, 15, 50], dtype=float)
    probs = fitness / fitness.sum()
    return dict(fitness=fitness.tolist(), probs=probs.tolist(), prob_sum=float(probs.sum()))


def check_ga_initial_population():
    """Verify GA toy initial population is within [0,0.5] and length 10."""
    pop = np.array([0.041, 0.178, 0.203, 0.247, 0.311, 0.328, 0.359, 0.402, 0.435, 0.496])
    return dict(size=len(pop), min=float(pop.min()), max=float(pop.max()), within_bounds=bool((pop >= 0).all() and (pop <= 0.5).all()))


def _ga_example_fx(x: np.ndarray) -> np.ndarray:
    """Fitness/objective used in the Ch. 19 toy examples: f(x)=cos(5*pi*x)*exp(-x^2)."""
    x = np.asarray(x, dtype=float)
    return np.cos(5.0 * np.pi * x) * np.exp(-(x * x))


def check_ga_fx_values():
    """Verify the rounded f(x) values used in the Ch. 19 GA toy traces."""
    toy_x = np.array([0.0625, 0.125, 0.3125, 0.4375], dtype=float)
    toy_fx = _ga_example_fx(toy_x)

    init_x = np.array([0.04, 0.09, 0.13, 0.18, 0.22, 0.27, 0.31, 0.36, 0.42, 0.48], dtype=float)
    init_fx = _ga_example_fx(init_x)

    return dict(
        toy_x=toy_x.tolist(),
        toy_fx_fmt=[f"{v:.3f}" for v in toy_fx.tolist()],
        init_x=init_x.tolist(),
        init_fx_fmt=[f"{v:.3f}" for v in init_fx.tolist()],
    )


def check_ga_fixedpoint_crossover():
    """
    Verify the fixed-point one-point crossover example (Ch. 19).

    Encoding: x = n/1000 with n in [0,500], stored as a 9-bit binary integer (since 2^9=512).
    Example: parents 0.203 (n=203) and 0.359 (n=359), one-point cut after 5 MSB bits.
    """
    bits = 9
    cut = 5  # MSB-first: keep the first 5 bits, swap the last 4 bits
    n1, n2 = 203, 359
    b1 = format(n1, f"0{bits}b")
    b2 = format(n2, f"0{bits}b")
    o1 = b1[:cut] + b2[cut:]
    o2 = b2[:cut] + b1[cut:]
    n_o1 = int(o1, 2)
    n_o2 = int(o2, 2)
    return dict(
        parent_bits=(b1, b2),
        offspring_bits=(o1, o2),
        offspring_decoded=(n_o1 / 1000.0, n_o2 / 1000.0),
    )


if __name__ == "__main__":
    print("Hopfield energies (Ch.10 example):", check_hopfield())
    print("1D stride/pad attention toy (Ch.11):", check_stride_pad())
    print("SGNS loss example (Ch.14):", check_sgns())
    print("Fuzzy composition (Ch.17):", check_fuzzy_composition())
    print("Alpha-cut mapping y=x^2 (Ch.17):", check_alpha_cut_mapping())
    print("Mamdani centroid (Ch.18):", check_mamdani_centroid())
    print("Roulette selection (Ch.19):", check_roulette_selection())
    print("GA toy initial population (Ch.19):", check_ga_initial_population())
    print("GA toy f(x) values (Ch.19):", check_ga_fx_values())
    print("GA fixed-point crossover (Ch.19):", check_ga_fixedpoint_crossover())
