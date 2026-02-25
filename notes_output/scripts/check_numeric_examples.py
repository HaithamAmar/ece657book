"""
Quick sanity checks for numerical examples up to Chapter 18.

- Hopfield 3-neuron energy monotonicity (Ch. 10)
- Perceptron OR-gate update trace (Ch. 5)
- 1D stride/padding attention toy (Ch. 11)
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
        for line in qc2:
            parts = line.split()
            tag = parts[0]
            if tag == "b":
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

        energies["hebbian_single_pattern_h1"] = float(h[0])
        energies["hebbian_single_pattern_h2"] = float(h[1])
        energies["hebbian_single_pattern_h3"] = float(h[2])
        energies["hebbian_single_pattern_h4"] = float(h[3])

    return energies


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
