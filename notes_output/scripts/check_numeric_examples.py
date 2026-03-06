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

import re
import numpy as np
from math import exp
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _read_tex(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8", errors="ignore")


def _clean_tex_number(s: str) -> str:
    # Examples we expect to see in the book:
    #   6{,}553{,}600
    #   65,536
    #   3/4
    #   -0.75
    s2 = s.replace(r"\,", "")
    s2 = s2.replace("{,}", "")
    s2 = re.sub(r"[{},\s]", "", s2)
    return s2


def _parse_tex_number(s: str) -> float:
    cleaned = _clean_tex_number(s)
    if re.fullmatch(r"-?\d+/\d+", cleaned):
        num, den = cleaned.split("/", 1)
        return float(num) / float(den)
    return float(cleaned)


def _slice_between(tex_text: str, start: str, end: str) -> str:
    i0 = tex_text.find(start)
    if i0 == -1:
        raise AssertionError(f"Missing start marker: {start!r}")
    i1 = tex_text.find(end, i0 + len(start))
    if i1 == -1:
        raise AssertionError(f"Missing end marker: {end!r}")
    return tex_text[i0:i1]


def _extract_tcolorbox_body(tex_text: str, title: str) -> str:
    pattern = re.compile(
        r"\\begin\{tcolorbox\}\[[^\]]*title=\{" + re.escape(title) + r"\}[^\]]*\]([\s\S]*?)\\end\{tcolorbox\}",
        re.MULTILINE,
    )
    m = pattern.search(tex_text)
    if not m:
        raise AssertionError(f"Missing tcolorbox with title={title!r}")
    return m.group(1)


def _parse_matrix_body(body: str) -> np.ndarray:
    # Parse the content between \begin{bmatrix}...\end{bmatrix} (or pmatrix)
    # into a numeric numpy array. Cells are separated by '&' and rows by '\\'.
    rows: list[list[float]] = []
    for raw_row in re.split(r"\\\\", body):
        row = raw_row.strip()
        if not row:
            continue
        cells = [c.strip() for c in row.split("&")]
        if not cells:
            continue
        rows.append([_parse_tex_number(c) for c in cells])
    if not rows:
        raise AssertionError("Parsed empty matrix body")
    ncols = {len(r) for r in rows}
    if len(ncols) != 1:
        raise AssertionError(f"Ragged matrix rows: column counts={sorted(ncols)}")
    return np.array(rows, dtype=float)


def _parse_int_tuple(s: str) -> tuple[int, ...]:
    s2 = s.replace(r"\,", "").replace(" ", "")
    parts = [p for p in s2.split(",") if p]
    return tuple(int(p) for p in parts)


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


def check_hopfield():
    """
    Hopfield numerical examples (Ch. 10), verified against book-visible values.

    This check is intentionally tied to what is printed in the chapter: matrices,
    states, and energies are parsed from the LaTeX source (not from QC comments).
    """
    tex = _read_tex("lecture_5_part_ii.tex")
    energies: dict[str, float] = {}

    # ------------------------------------------------------------------
    # 3-neuron energy example: parse W, states, and energies from the text.
    # ------------------------------------------------------------------
    sec3 = _slice_between(
        tex,
        r"\subsection{Example: Energy Calculation and State Updates}",
        r"\subsection{Energy Function and Convergence of Hopfield Networks}",
    )

    mW = re.search(r"W\s*=\s*\\begin\{bmatrix\}([\s\S]*?)\\end\{bmatrix\}", sec3, re.DOTALL)
    if not mW:
        raise AssertionError("Could not parse 3-neuron Hopfield W matrix from the chapter text")
    W = _parse_matrix_body(mW.group(1))
    if W.shape != (3, 3):
        raise AssertionError(f"Unexpected Hopfield W shape: {W.shape}, expected (3,3)")

    # Baseline state (as written) and its reported energy.
    ms0 = re.search(r"initial state be\s*\\\(\\mathbf\{s\}\s*=\s*\(([^)]*)\)\\\)", sec3)
    if not ms0:
        raise AssertionError("Could not parse the initial state tuple for the Hopfield example")
    s0 = np.array(_parse_int_tuple(ms0.group(1)), dtype=float)
    if s0.shape != (3,):
        raise AssertionError(f"Unexpected Hopfield initial state length: {s0.shape}")

    mE0 = re.search(r"\\Big\[[\s\S]*?\\Big\]\s*=\s*(-?\d+(?:\.\d+)?)\s*\.", sec3, re.DOTALL)
    if not mE0:
        raise AssertionError("Could not parse the reported E(s) value in the 3-neuron example derivation")
    E0_expected = float(mE0.group(1))

    theta = np.zeros(3, dtype=float)
    E0_actual = hopfield_energy(W, s0, theta=theta)
    if abs(E0_actual - E0_expected) > 1e-9:
        raise AssertionError(f"Hopfield E(s0) mismatch: actual={E0_actual}, expected={E0_expected}")
    energies["s0"] = float(E0_actual)

    # The text reports the energies of three single-bit flips explicitly.
    flip_re = re.compile(r"E\(([^)]*)\)\s*=\s*(-?\d+(?:\.\d+)?)")
    flip_expected: dict[tuple[int, int, int], float] = {}
    for state_str, E_str in flip_re.findall(sec3):
        tup = _parse_int_tuple(state_str)
        if len(tup) != 3:
            continue
        flip_expected[tup] = float(E_str)

    expected_states = {
        "flip_s1": (-1, 1, -1),
        "flip_s2": (1, -1, -1),
        "flip_s3": (1, 1, 1),
    }
    for key, st in expected_states.items():
        if st not in flip_expected:
            raise AssertionError(f"Missing reported energy for Hopfield state {st} in the text")
        E_exp = flip_expected[st]
        E_act = hopfield_energy(W, np.array(st, dtype=float), theta=theta)
        if abs(E_act - E_exp) > 1e-9:
            raise AssertionError(f"Hopfield {key} energy mismatch: actual={E_act}, expected={E_exp}")
        energies[key] = float(E_act)

    # Noisy probe update (as described): (1,1,1) -> update neuron 3 -> (1,1,-1).
    m_noisy = re.search(r"noisy pattern\s*\\\(\(([^)]*)\)\\\)", sec3)
    m_after = re.search(r"returning to\s*\\\(\(([^)]*)\)\\\)", sec3)
    if not m_noisy or not m_after:
        raise AssertionError("Could not parse noisy probe and recovered state tuples from the Hopfield text")
    s_noisy = np.array(_parse_int_tuple(m_noisy.group(1)), dtype=float)
    s_after = np.array(_parse_int_tuple(m_after.group(1)), dtype=float)
    if s_noisy.shape != (3,) or s_after.shape != (3,):
        raise AssertionError("Malformed noisy/probe tuples in Hopfield example")

    update_i = 3  # The text explicitly discusses neuron 3 and sets s_3 <- -1.
    i = update_i - 1
    h = float(W[i] @ s_noisy - theta[i])
    s_next = s_noisy.copy()
    s_next[i] = 1.0 if h >= 0.0 else -1.0
    if not np.allclose(s_next, s_after):
        raise AssertionError(f"Hopfield noisy update state mismatch: actual={s_next}, expected={s_after}")
    E_after = hopfield_energy(W, s_next, theta=theta)
    if abs(E_after - E0_expected) > 1e-9:
        raise AssertionError(f"Hopfield noisy update energy mismatch: actual={E_after}, expected={E0_expected}")
    energies["noisy_after"] = float(E_after)

    # ------------------------------------------------------------------
    # 4-neuron Hebbian single-pattern weight example + recall trace.
    # ------------------------------------------------------------------
    sec4 = _slice_between(
        tex,
        r"\subsection{Example: Weight Calculation for a Single Pattern}",
        r"\subsection{Finalizing the Hopfield Network Derivation and Discussion}",
    )

    m_xi = re.search(r"\\mathbf\{\\xi\}\s*=\s*\(([^)]*)\)", sec4)
    if not m_xi:
        raise AssertionError("Could not parse the 4-neuron pattern xi in the Hopfield chapter")
    xi = np.array(_parse_int_tuple(m_xi.group(1)), dtype=float)
    if xi.shape != (4,):
        raise AssertionError(f"Unexpected xi length: {xi.shape}")

    iW = sec4.find(r"\mathbf{W}")
    if iW == -1:
        raise AssertionError("Could not find the W definition in the 4-neuron Hopfield example")
    subW = sec4[iW:]
    mW4 = re.search(
        r"\\frac\{(\d+)\}\{(\d+)\}\s*\\begin\{(bmatrix|pmatrix)\}([\s\S]*?)\\end\{\3\}",
        subW,
        re.DOTALL,
    )
    if not mW4:
        raise AssertionError("Could not parse the scaled 4x4 W matrix in the Hopfield chapter")
    scale = float(mW4.group(1)) / float(mW4.group(2))
    W4_int = _parse_matrix_body(mW4.group(4))
    W4 = scale * W4_int
    if W4.shape != (4, 4):
        raise AssertionError(f"Unexpected W shape: {W4.shape}, expected (4,4)")

    W4_expected = np.outer(xi, xi) / float(xi.size)
    np.fill_diagonal(W4_expected, 0.0)
    if not np.allclose(W4, W4_expected, atol=1e-12, rtol=0.0):
        raise AssertionError("Hopfield single-pattern W mismatch vs Hebbian formula")

    # Parse the printed local field vector h.
    mh = re.search(r"\\mathbf\{h\}[\s\S]*?\\begin\{bmatrix\}([\s\S]*?)\\end\{bmatrix\}", sec4, re.DOTALL)
    if not mh:
        raise AssertionError("Could not parse the printed Hopfield local field vector h")
    h_print = _parse_matrix_body(mh.group(1)).reshape(-1)
    if h_print.shape != (4,):
        raise AssertionError(f"Unexpected h vector length: {h_print.shape}")
    h_act = W4 @ xi
    if not np.allclose(h_act, h_print, atol=1e-12, rtol=0.0):
        raise AssertionError(f"Hopfield h mismatch: actual={h_act}, expected={h_print}")
    if not np.allclose(np.where(h_act >= 0.0, 1.0, -1.0), xi):
        raise AssertionError("Hopfield fixed-point sanity check failed: sign(W xi) != xi")

    # Parse recall trace table (two asynchronous flips) and the energy sequence.
    box_title = "Numeric recall trace (two asynchronous flips)"
    box = _extract_tcolorbox_body(sec4, box_title)
    mEseq = re.search(r"E=([0-9.+-]+)\s*\\rightarrow\s*([0-9.+-]+)\s*\\rightarrow\s*([0-9.+-]+)", box)
    if not mEseq:
        raise AssertionError("Could not parse the printed Hopfield recall energy sequence")
    E_seq_expected = [float(mEseq.group(1)), float(mEseq.group(2)), float(mEseq.group(3))]

    steps: list[tuple[int, int, float, tuple[int, int, int, int]]] = []
    mtab = re.search(r"\\begin\{tabular\}[\s\S]*?\\midrule([\s\S]*?)\\bottomrule", box, re.DOTALL)
    if mtab:
        tab = mtab.group(1)
        for raw in tab.splitlines():
            line = raw.strip()
            if not line or "&" not in line or line.startswith("%"):
                continue
            line = line.rstrip("\\").strip()
            cells = [c.strip() for c in line.split("&")]
            if len(cells) < 4:
                continue
            step = int(cells[0])
            if step == 0:
                mstate = re.search(r"(?<!\\)\(([^)]*)\)", cells[3])
                if not mstate:
                    raise AssertionError("Could not parse Hopfield recall step-0 state")
                steps.append((0, 0, 0.0, _parse_int_tuple(mstate.group(1))))
                continue

            mi = re.search(r"i\s*=\s*(\d+)", cells[1])
            mhv = re.search(r"=\s*([0-9.+-]+)", cells[2])
            mstate = re.search(r"(?<!\\)\(([^)]*)\)", cells[3])
            if not (mi and mhv and mstate):
                continue
            update_i = int(mi.group(1))
            h_val = float(mhv.group(1))
            state_tup = _parse_int_tuple(mstate.group(1))
            if len(state_tup) != 4:
                raise AssertionError("Malformed state tuple in Hopfield recall table")
            steps.append((step, update_i, h_val, state_tup))
    else:
        mstep0 = re.search(
            r"\\textbf\{Step 0:\}\s*\\\(\\mathbf\{s\}\^\{\(0\)\}=\\?([([][^])]+[)\]])\\\)",
            box,
        )
        if not mstep0:
            raise AssertionError("Could not parse Hopfield recall trace table")
        steps.append((0, 0, 0.0, _parse_int_tuple(mstep0.group(1).strip("[]()"))))

        for match in re.finditer(
            r"\\textbf\{Step\s+(\d+)\s+\(update\s+\\\(i=(\d+)\\\)\):\}\s*\\\(h_(\d+)=([0-9.+-]+)\\\),\s*so\s*\\\(\\mathbf\{s\}\^\{\(\d+\)\}=\\?([([][^])]+[)\]])(?:=\\mathbf\{\\xi\})?\\\)",
            box,
        ):
            step = int(match.group(1))
            update_i = int(match.group(2))
            field_index = int(match.group(3))
            h_val = float(match.group(4))
            state_tup = _parse_int_tuple(match.group(5).strip("[]()"))
            if len(state_tup) != 4:
                raise AssertionError("Malformed state tuple in Hopfield recall table")
            if field_index != update_i:
                raise AssertionError(
                    f"Hopfield recall trace used h_{field_index} for update i={update_i}"
                )
            steps.append((step, update_i, h_val, state_tup))

    steps_sorted = sorted(steps, key=lambda t: t[0])
    if [t[0] for t in steps_sorted] != [0, 1, 2]:
        raise AssertionError(f"Unexpected recall trace steps: {[t[0] for t in steps_sorted]}")

    s_prev = np.array(steps_sorted[0][3], dtype=float)
    # Verify step 1 and step 2, plus energies.
    E0 = hopfield_energy(W4, s_prev, theta=np.zeros_like(s_prev))
    if abs(E0 - E_seq_expected[0]) > 1e-12:
        raise AssertionError(f"Hopfield recall E0 mismatch: actual={E0}, expected={E_seq_expected[0]}")
    for idx, (step, update_i, h_expected, s_after_tup) in enumerate(steps_sorted[1:], start=1):
        i = update_i - 1
        h_step = float(W4[i] @ s_prev)
        if abs(h_step - h_expected) > 1e-12:
            raise AssertionError(f"Hopfield recall step {step} h mismatch: actual={h_step}, expected={h_expected}")
        s_next = s_prev.copy()
        s_next[i] = 1.0 if h_step >= 0.0 else -1.0
        if not np.allclose(s_next, np.array(s_after_tup, dtype=float), atol=1e-12, rtol=0.0):
            raise AssertionError(f"Hopfield recall step {step} state mismatch: actual={s_next}, expected={s_after_tup}")
        E_step = hopfield_energy(W4, s_next, theta=np.zeros_like(s_next))
        if abs(E_step - E_seq_expected[idx]) > 1e-12:
            raise AssertionError(
                f"Hopfield recall step {step} energy mismatch: actual={E_step}, expected={E_seq_expected[idx]}"
            )
        s_prev = s_next

    energies["hebbian_single_pattern_h1"] = float(h_act[0])
    energies["hebbian_single_pattern_h2"] = float(h_act[1])
    energies["hebbian_single_pattern_h3"] = float(h_act[2])
    energies["hebbian_single_pattern_h4"] = float(h_act[3])

    # ------------------------------------------------------------------
    # 4-neuron one-flip memory recovery example (book-visible).
    # ------------------------------------------------------------------
    m_mem_start = tex.find(r"\paragraph{Example: Memory recovery (one flip)}")
    if m_mem_start != -1:
        mem = tex[m_mem_start : tex.find(r"\paragraph{Spurious attractors}", m_mem_start)]

        m_xi2 = re.search(r"\\mathbf\{\\xi\}\s*=\s*\(([^)]*)\)\^T", mem)
        if not m_xi2:
            raise AssertionError("Could not parse xi in the Hopfield memory-recovery example")
        xi2 = np.array(_parse_int_tuple(m_xi2.group(1)), dtype=float)
        if xi2.shape != (4,):
            raise AssertionError("Unexpected xi shape in memory-recovery example")

        iW2 = mem.find(r"\mathbf{W} = \frac{1}{4}")
        if iW2 == -1:
            raise AssertionError("Could not find the printed W matrix in the memory-recovery example")
        mW2 = re.search(
            r"\\frac\{(\d+)\}\{(\d+)\}\s*\\begin\{pmatrix\}([\s\S]*?)\\end\{pmatrix\}",
            mem[iW2:],
            re.DOTALL,
        )
        if not mW2:
            raise AssertionError("Could not parse the printed W matrix in the memory-recovery example")
        scale2 = float(mW2.group(1)) / float(mW2.group(2))
        W2_int = _parse_matrix_body(mW2.group(3))
        W2 = scale2 * W2_int
        W2_expected = np.outer(xi2, xi2) / float(xi2.size)
        np.fill_diagonal(W2_expected, 0.0)
        if not np.allclose(W2, W2_expected, atol=1e-12, rtol=0.0):
            raise AssertionError("Hopfield memory-recovery W mismatch vs Hebbian formula")

        ms_probe = re.search(r"\\mathbf\{s\}\^\{\(0\)\}=\[([^\]]+)\]\^T", mem)
        if not ms_probe:
            raise AssertionError("Could not parse s^(0) in the Hopfield memory-recovery example")
        s_probe = np.array(_parse_int_tuple(ms_probe.group(1)), dtype=float)

        mi = re.search(r"update neuron\s*\\\(\s*(\d+)\s*\\\)", mem)
        if not mi:
            raise AssertionError("Could not parse which neuron is updated in the memory-recovery example")
        update_i = int(mi.group(1))
        if update_i != 4:
            raise AssertionError(f"Memory-recovery example is expected to update neuron 4, got neuron {update_i}")

        mh4 = re.search(r"h_4=.*?=\s*([+-]?[0-9.]+)", mem, re.DOTALL)
        if not mh4:
            raise AssertionError("Could not parse the printed h4 value in memory-recovery example")
        h4_expected = float(mh4.group(1))

        mEdrop = re.search(
            r"energy drops from\s*\\\(\s*E=([+-]?[0-9.]+)\s*\\\)\s*to\s*\\\(\s*E=([+-]?[0-9.]+)\s*\\\)",
            mem,
        )
        if not mEdrop:
            raise AssertionError("Could not parse the printed energy drop in memory-recovery example")
        E0_exp = float(mEdrop.group(1))
        E1_exp = float(mEdrop.group(2))

        E0_act = hopfield_energy(W2, s_probe, theta=np.zeros_like(s_probe))
        if abs(E0_act - E0_exp) > 1e-12:
            raise AssertionError(f"Hopfield memory-recovery E0 mismatch: actual={E0_act}, expected={E0_exp}")

        i = update_i - 1
        h4_act = float(W2[i] @ s_probe)
        if abs(h4_act - h4_expected) > 1e-12:
            raise AssertionError(f"Hopfield memory-recovery h mismatch: actual={h4_act}, expected={h4_expected}")
        s_next = s_probe.copy()
        s_next[i] = 1.0 if h4_act >= 0.0 else -1.0

        E1_act = hopfield_energy(W2, s_next, theta=np.zeros_like(s_next))
        if abs(E1_act - E1_exp) > 1e-12:
            raise AssertionError(f"Hopfield memory-recovery E1 mismatch: actual={E1_act}, expected={E1_exp}")

        energies["memory_recovery_h"] = float(h4_act)
        energies["memory_recovery_E0"] = float(E0_act)
        energies["memory_recovery_E1"] = float(E1_act)

    return energies


def check_cnn_flatten_params() -> dict[str, float]:
    """
    CNN flattening parameter-count sanity check (Ch. 11), verified against book-visible values.

    Verifies the vectorized input dimension and the first-layer parameter count used in the
    ``fully connected layers break on images'' motivation.
    """
    tex = _read_tex("lecture_6.tex")
    sec = _slice_between(
        tex,
        r"\subsection{Why fully connected layers break on images}",
        r"\subsection{Sparse connectivity and parameter sharing}",
    )

    mHW = re.search(r"\\mathbb\{R\}\^\{(\d+)\s*\\times\s*(\d+)\}", sec)
    if not mHW:
        raise AssertionError("Could not parse image dimensions for CNN flatten example")
    H = int(mHW.group(1))
    W = int(mHW.group(2))

    mvec = re.search(r"\\mathrm\{vec\}\(X\)\s*\\in\s*\\mathbb\{R\}\^\{([^}]*)\}", sec)
    if not mvec:
        raise AssertionError("Could not parse vec(X) dimension for CNN flatten example")
    vec = int(_parse_tex_number(mvec.group(1)))

    # Two explicit arithmetic equations: vec*hidden=W1 and hidden*classes=W2.
    mult_re = re.compile(r"([0-9{,}\\,]+)\s*\\times\s*([0-9{,}\\,]+)\s*=\s*([0-9{,}\\,]+)")
    mults = [(a, b, c) for (a, b, c) in mult_re.findall(sec)]
    if len(mults) < 2:
        raise AssertionError("Could not find the two arithmetic parameter-count equations in the CNN chapter")

    # Heuristic: the large product is vec*hidden (~millions) and the small is hidden*classes (~hundreds).
    parsed = [(int(_parse_tex_number(a)), int(_parse_tex_number(b)), int(_parse_tex_number(c))) for (a, b, c) in mults]
    parsed_sorted = sorted(parsed, key=lambda t: t[2], reverse=True)
    vec_lhs, hidden, W1 = parsed_sorted[0]
    hidden2, classes, W2 = parsed_sorted[-1]

    if vec_lhs != vec:
        raise AssertionError(f"CNN W1 equation uses vec={vec_lhs}, but vec(X) line reports {vec}")
    if hidden2 != hidden:
        raise AssertionError("CNN hidden dimension mismatch between equations")

    # Back-of-envelope sample rule: 10 x 6,553,600 ≈ 65,536,000.
    m_rule = re.search(r"10\s*\\times\s*([0-9{,}\\,]+)\s*\\approx\s*([0-9{,}\\,]+)", sec)
    if not m_rule:
        raise AssertionError("Could not parse the sample-rule back-of-envelope equation in the CNN chapter")
    nparams = int(_parse_tex_number(m_rule.group(1)))
    approx = int(_parse_tex_number(m_rule.group(2)))

    # Verify arithmetic.
    computed_vec = int(H * W)
    if computed_vec != vec:
        raise AssertionError(f"CNN vec mismatch: actual={computed_vec}, expected={vec}")
    computed_W1 = int(vec * hidden)
    if computed_W1 != W1:
        raise AssertionError(f"CNN W1 mismatch: actual={computed_W1}, expected={W1}")
    computed_W2 = int(hidden * classes)
    if computed_W2 != W2:
        raise AssertionError(f"CNN W2 mismatch: actual={computed_W2}, expected={W2}")
    computed_approx = int(10 * nparams)
    if computed_approx != approx:
        raise AssertionError(f"CNN sample-rule approx mismatch: actual={computed_approx}, expected={approx}")

    # Sanity check that the printed "N_parameters" corresponds to W1 in this toy.
    if nparams != W1:
        raise AssertionError(f"CNN N_parameters mismatch: expected {W1}, got {nparams}")

    return dict(vec=float(vec), W1=float(W1), W2=float(W2), approx=float(approx))


def check_cnn_1d_xcorr_stride_pad() -> dict[str, float | list[float]]:
    """
    1D cross-correlation numeric example (Ch. 11), verified against book-visible values.

    Verifies the output length and values for the stride/padding worked example.
    """
    tex = _read_tex("lecture_6.tex")
    box = _extract_tcolorbox_body(tex, "Worked example: 1D cross-correlation values (stride + padding)")

    def _parse_bracket_list(name: str) -> np.ndarray:
        m = re.search(rf"\\mathbf\{{{re.escape(name)}\}}=\[([^\]]+)\]", box)
        if not m:
            raise AssertionError(f"Could not parse {name} list in CNN xcorr example")
        vals = [_parse_tex_number(v) for v in m.group(1).split(",")]
        return np.array(vals, dtype=float)

    x = _parse_bracket_list("x")
    w = _parse_bracket_list("w")

    mp = re.search(r"padding\s*\\\(p=([0-9]+)\\\)", box)
    ms = re.search(r"stride\s*\\\(s=([0-9]+)\\\)", box)
    if not mp or not ms:
        raise AssertionError("Could not parse padding/stride in CNN xcorr example")
    p = int(mp.group(1))
    s = int(ms.group(1))

    mL = re.search(r"=([0-9]+)\s*\.\s*\]\s*Sliding", box, re.DOTALL)
    if not mL:
        # Fall back: parse the last integer after the output-length equation.
        mL = re.search(r"output length is[\s\S]*?=\s*([0-9]+)\s*\.", box, re.DOTALL)
    if not mL:
        raise AssertionError("Could not parse the output length L in CNN xcorr example")
    L = int(mL.group(1))

    my = re.search(r"\\mathbf\{y\}=\[([^\]]+)\]", box)
    if not my:
        raise AssertionError("Could not parse the output y list in CNN xcorr example")
    y_expected = [float(_parse_tex_number(v)) for v in my.group(1).split(",")]

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
    CNN shape bookkeeping example (Ch. 11), verified against book-visible values.

    Verifies the conv output size, pooling output size, and flatten dimension.
    """
    tex = _read_tex("lecture_6.tex")
    box = _extract_tcolorbox_body(tex, "Dimensionality accounting example")

    # Input tensor size HxWxCin.
    m_in = re.search(r"size\s*\\\((\d+)\\times(\d+)\\times(\d+)\\\)", box)
    if not m_in:
        raise AssertionError("Could not parse CNN shape input dimensions")
    H, W, Cin = map(int, m_in.groups())

    m_conv = re.search(
        r"Apply\s*\\\((\d+)\\\)\s*filters of size\s*\\\((\d+)\\times(\d+)\\\)\s*with stride\s*\\\((\d+)\\\)\s*and valid padding",
        box,
    )
    if not m_conv:
        raise AssertionError("Could not parse CNN conv hyperparameters in shape example")
    Cout = int(m_conv.group(1))
    k = int(m_conv.group(2))
    _k2 = int(m_conv.group(3))
    if _k2 != k:
        raise AssertionError("CNN shape example expects square kxk filters")
    stride = int(m_conv.group(4))
    pad = 0

    m_out = re.search(r"output is\s*\\\((\d+)\\times(\d+)\\times(\d+)\\\)", box)
    if not m_out:
        raise AssertionError("Could not parse CNN conv output dimensions in shape example")
    outH, outW, outC = map(int, m_out.groups())
    if outC != Cout:
        raise AssertionError("CNN shape example conv output channel mismatch")

    m_pool = re.search(r"Apply\s*\\\((\d+)\\times(\d+)\\\)\s*max pooling with stride\s*\\\((\d+)\\\)", box)
    if not m_pool:
        raise AssertionError("Could not parse CNN pooling hyperparameters in shape example")
    pool = int(m_pool.group(1))
    _p2 = int(m_pool.group(2))
    if _p2 != pool:
        raise AssertionError("CNN shape example expects square pooling window")
    pool_stride = int(m_pool.group(3))

    m_pool_out = re.search(r"pooled output is\s*\\\((\d+)\\times(\d+)\\times(\d+)\\\)", box)
    if not m_pool_out:
        raise AssertionError("Could not parse CNN pooled output dimensions in shape example")
    poolH, poolW, poolC = map(int, m_pool_out.groups())
    if poolC != Cout:
        raise AssertionError("CNN shape example pooled output channel mismatch")

    m_flat = re.search(r"=([0-9]+)(?:\\\))?\s*features", box)
    if not m_flat:
        raise AssertionError("Could not parse CNN flatten feature count in shape example")
    flat = int(m_flat.group(1))

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
