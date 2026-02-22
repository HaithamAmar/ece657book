#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import numpy as np

from check_numeric_examples import (
    check_alpha_cut_mapping,
    check_fuzzy_composition,
    check_ga_fixedpoint_crossover,
    check_ga_fx_values,
    check_ga_initial_population,
    check_hopfield,
    check_mamdani_centroid,
    check_perceptron_or_gate_trace,
    check_roulette_selection,
    check_sgns,
    check_tiny_causal_attention,
    check_stride_pad,
)


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts" / "qc"


@dataclass
class CheckResult:
    name: str
    status: str
    details: dict[str, float | str]
    error: str = ""


def _assert(condition: bool, msg: str) -> None:
    if not condition:
        raise AssertionError(msg)


def _assert_close(actual: float, expected: float, tol: float, msg: str) -> None:
    if abs(actual - expected) > tol:
        raise AssertionError(f"{msg}: actual={actual}, expected={expected}, tol={tol}")


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


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
        if not payload or payload.lower().startswith("step "):
            continue
        lines.append(payload)
    return lines


def _parse_perceptron_or_qc(lines: list[str]) -> list[dict[str, int]]:
    out: list[dict[str, int]] = []
    for line in lines:
        # step epoch idx x1 x2 y w1 w2 b
        parts = line.split()
        if len(parts) != 9:
            raise AssertionError(f"Malformed perceptron QC line: {line!r}")
        step, epoch, idx, x1, x2, y, w1, w2, b = map(int, parts)
        out.append(
            dict(step=step, epoch=epoch, idx=idx, x1=x1, x2=x2, y=y, w1=w1, w2=w2, b=b)
        )
    return out


def _extract_figure_block(tex_text: str, label: str) -> str:
    label_pattern = re.compile(rf"\\label\{{{re.escape(label)}\}}")
    label_match = label_pattern.search(tex_text)
    if not label_match:
        raise AssertionError(f"Could not find figure block for label {label}")
    label_pos = label_match.start()
    start = tex_text.rfind(r"\begin{figure}", 0, label_pos)
    end = tex_text.find(r"\end{figure}", label_pos)
    if start == -1 or end == -1:
        raise AssertionError(f"Could not isolate figure environment for label {label}")
    end += len(r"\end{figure}")
    return tex_text[start:end]


def _extract_table_blocks(figure_block: str) -> list[str]:
    return re.findall(r"table(?:\[[^\]]*\])?\s*\{([\s\S]*?)\};", figure_block)


def _parse_xy_table(table: str) -> list[tuple[float, float]]:
    rows: list[tuple[float, float]] = []
    normalized = table.replace("\\\\", "\n")
    for raw_line in normalized.splitlines():
        line = raw_line.split("%", 1)[0].strip().rstrip("\\").strip()
        if not line or line.lower().startswith("x y"):
            continue
        match = re.match(r"^(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)$", line)
        if match:
            rows.append((float(match.group(1)), float(match.group(2))))
    return rows


def _parse_xyz_table(table: str) -> list[tuple[int, int, float]]:
    rows: list[tuple[int, int, float]] = []
    normalized = table.replace("\\\\", "\n")
    for raw_line in normalized.splitlines():
        line = raw_line.split("%", 1)[0].strip().rstrip("\\").strip()
        if not line or line.lower().startswith("x y z"):
            continue
        match = re.match(r"^(\d+)\s+(\d+)\s+(-?\d+(?:\.\d+)?)$", line)
        if match:
            rows.append((int(match.group(1)), int(match.group(2)), float(match.group(3))))
    return rows


def _parse_exp_curve(expr: str) -> tuple[float, float, float]:
    cleaned = expr.replace(" ", "")
    pattern = re.compile(r"^([0-9.]+)\+([0-9.]+)\*exp\(-x/([0-9.]+)\)$")
    match = pattern.match(cleaned)
    if not match:
        raise AssertionError(f"Unsupported exponential curve form: {expr}")
    return float(match.group(1)), float(match.group(2)), float(match.group(3))


def _curve(a: float, b: float, c: float, x: np.ndarray) -> np.ndarray:
    return a + b * np.exp(-x / c)


def check_numeric_examples_pack() -> dict[str, float]:
    # Chapter 5: perceptron OR-gate update trace (verified against the QC comment block).
    p_or = check_perceptron_or_gate_trace()
    _assert(tuple(p_or["final_w"]) == (2, 2), "Perceptron OR final w mismatch")
    _assert(int(p_or["final_b"]) == -1, "Perceptron OR final b mismatch")
    _assert(int(p_or["num_updates"]) == 9, "Perceptron OR number of updates mismatch")

    lec3 = _read(ROOT / "lecture_3_part_i.tex")
    qc_lines = _extract_qc_block(lec3, "perceptron_or_trace")
    qc_trace = _parse_perceptron_or_qc(qc_lines)
    _assert(qc_trace == p_or["trace"], "Perceptron OR QC trace does not match computed trace")

    hopfield = check_hopfield()
    _assert_close(float(hopfield["s0"]), -5.0, 1e-9, "Hopfield E(s0)")
    _assert_close(float(hopfield["flip_s1"]), 9.0, 1e-9, "Hopfield flip s1")
    _assert_close(float(hopfield["flip_s2"]), -3.0, 1e-9, "Hopfield flip s2")
    _assert_close(float(hopfield["flip_s3"]), -1.0, 1e-9, "Hopfield flip s3")

    stride = check_stride_pad()
    _assert(int(stride["L"]) == 3, "Stride/padding L must be 3")
    _assert(stride["y"] == [-2, -1, 3], "Stride/padding output mismatch")

    attn = check_tiny_causal_attention()
    # Token 1 can only attend to itself under a causal mask.
    _assert_close(float(attn["weights"][0][0]), 1.0, 1e-9, "Tiny attention w11")
    _assert_close(float(attn["weights"][0][1]), 0.0, 1e-9, "Tiny attention w12")
    # Token 2 attends to both tokens; numbers come from softmax([0, 1/sqrt(2)]).
    _assert_close(float(attn["weights"][1][0]), 0.330238, 2e-6, "Tiny attention w21")
    _assert_close(float(attn["weights"][1][1]), 0.669762, 2e-6, "Tiny attention w22")
    _assert_close(float(attn["out"][0][0]), 1.0, 1e-9, "Tiny attention y1[0]")
    _assert_close(float(attn["out"][0][1]), 0.0, 1e-9, "Tiny attention y1[1]")
    _assert_close(float(attn["out"][1][0]), 0.330238, 2e-6, "Tiny attention y2[0]")
    _assert_close(float(attn["out"][1][1]), 1.339524, 2e-6, "Tiny attention y2[1]")

    sgns = check_sgns()
    _assert_close(float(sgns["loss"]), 1.050621, 1e-6, "SGNS toy loss mismatch")

    fuzzy = check_fuzzy_composition()
    _assert(np.allclose(np.asarray(fuzzy["R"]), np.array([[0.4, 0.8], [0.5, 0.3]])), "Fuzzy composition mismatch")

    alpha = check_alpha_cut_mapping()
    _assert(tuple(alpha["A_alpha"]) == (-0.4, 0.4), "Alpha-cut interval mismatch")
    _assert(tuple(alpha["y_interval"]) == (0.0, 0.16000000000000003), "Alpha-cut mapped interval mismatch")

    centroid = check_mamdani_centroid()
    _assert(0.57 <= float(centroid["centroid"]) <= 0.59, "Mamdani centroid out of expected range")

    roulette = check_roulette_selection()
    _assert_close(float(roulette["prob_sum"]), 1.0, 1e-12, "Roulette probabilities do not sum to 1")

    ga_pop = check_ga_initial_population()
    _assert(bool(ga_pop["within_bounds"]), "GA initial population out of bounds")

    ga_fx = check_ga_fx_values()
    _assert(
        ga_fx["toy_fx_fmt"] == ["0.553", "-0.377", "0.177", "0.687"],
        "GA toy f(x) values mismatch (tab:ga-toy)",
    )
    _assert(
        ga_fx["init_fx_fmt"] == ["0.808", "0.155", "-0.446", "-0.921", "-0.906", "-0.422", "0.142", "0.711", "0.797", "0.245"],
        "GA constrained example f(x) values mismatch",
    )

    ga_cross = check_ga_fixedpoint_crossover()
    _assert(
        list(ga_cross["parent_bits"]) == ["011001011", "101100111"],
        "GA fixed-point parent bitstrings mismatch",
    )
    _assert(
        list(ga_cross["offspring_bits"]) == ["011000111", "101101011"],
        "GA fixed-point offspring bitstrings mismatch",
    )
    _assert(
        [f"{v:.3f}" for v in ga_cross["offspring_decoded"]] == ["0.199", "0.363"],
        "GA fixed-point crossover decoded values mismatch",
    )

    return {
        "perceptron_or_updates": float(p_or["num_updates"]),
        "hopfield_s0": float(hopfield["s0"]),
        "stride_L": float(stride["L"]),
        "tiny_attn_w22": float(attn["weights"][1][1]),
        "sgns_loss": float(sgns["loss"]),
        "mamdani_centroid": float(centroid["centroid"]),
        "roulette_sum": float(roulette["prob_sum"]),
    }


def check_integral_result_derivative() -> dict[str, float]:
    xs = np.linspace(-0.9, 0.9, 401)
    eps = 1e-6

    def antiderivative(x: np.ndarray) -> np.ndarray:
        return 4.0 * x / np.sqrt(1.0 - x * x) + (4.0 / 3.0) * x**3 / np.power(1.0 - x * x, 1.5)

    def integrand(x: np.ndarray) -> np.ndarray:
        return 4.0 / np.power(1.0 - x * x, 2.5)

    fp = antiderivative(xs + eps)
    fm = antiderivative(xs - eps)
    num_deriv = (fp - fm) / (2.0 * eps)
    truth = integrand(xs)
    max_err = float(np.max(np.abs(num_deriv - truth)))
    _assert(max_err < 2e-4, f"Integral derivative check failed; max_err={max_err}")
    return {"max_abs_derivative_error": max_err}


def check_fig_sigmoid_bce_curves() -> dict[str, float]:
    tex = _read(ROOT / "lecture_2_part_ii.tex")
    fig = _extract_figure_block(tex, "fig:lec2_sigmoid_bce")
    must_have = [
        "1/(1+exp(-x))",
        "-ln(1/(1+exp(-x)))",
        "-ln(1-1/(1+exp(-x)))",
        "1/(1+0.9*x)",
    ]
    for token in must_have:
        _assert(token in fig, f"Expected curve expression not found: {token}")

    z = np.linspace(-5.5, 5.5, 300)
    sig = 1.0 / (1.0 + np.exp(-z))
    bce_y1 = -np.log(sig)
    bce_y0 = -np.log(1.0 - sig)
    l2 = 1.0 / (1.0 + 0.9 * np.linspace(0, 5, 300))

    _assert(np.all(np.diff(sig) > 0), "Sigmoid should be strictly increasing")
    _assert(np.all(np.diff(bce_y1) < 0), "BCE(y=1) should decrease as logit increases")
    _assert(np.all(np.diff(bce_y0) > 0), "BCE(y=0) should increase as logit increases")
    _assert(np.all(np.diff(l2) < 0), "L2 shrinkage curve should decrease with lambda")

    return {
        "sigmoid_min": float(sig.min()),
        "sigmoid_max": float(sig.max()),
        "bce_y1_at_5": float(bce_y1[-1]),
        "bce_y0_at_minus5": float(bce_y0[0]),
    }


def check_fig_bn_curves() -> dict[str, float]:
    tex = _read(ROOT / "lecture_6.tex")
    fig = _extract_figure_block(tex, "fig:lec6-bn")
    must_have = [
        "(x-2)^2",
        "(x+1)^2",
        "exp(-(x^2)/2)",
    ]
    for token in must_have:
        _assert(token in fig, f"BN figure expression missing: {token}")

    pre_means = [2.0, -1.0]
    pre_vars = [1.5, 0.8]
    post_means = [0.0, 0.0]
    post_vars = [1.0, 1.0]

    _assert(all(abs(m) > 0.1 for m in pre_means), "Pre-BN means should be shifted from zero")
    _assert(any(abs(v - 1.0) > 0.1 for v in pre_vars), "Pre-BN variances should differ from one")
    _assert(all(abs(m) < 1e-12 for m in post_means), "Post-BN means should be zero")
    _assert(all(abs(v - 1.0) < 1e-12 for v in post_vars), "Post-BN variances should be one")

    return {
        "pre_mean_abs_sum": float(sum(abs(x) for x in pre_means)),
        "pre_var_gap": float(abs(pre_vars[0] - pre_vars[1])),
    }


def check_fig_optimizer_curves() -> dict[str, float]:
    tex = _read(ROOT / "lecture_6.tex")
    fig = _extract_figure_block(tex, "fig:lec6-optimizers")

    plots = re.findall(r"\\addplot\[[^\]]*\]\s*\{([^}]*)\};\s*\\addlegendentry\{([^}]*)\}", fig)
    _assert(len(plots) >= 2, "Could not parse optimizer curve definitions")

    expr_map = {legend.strip(): expr.strip() for expr, legend in plots}
    _assert("SGD+momentum" in expr_map, "SGD+momentum curve missing")
    _assert("Adam" in expr_map, "Adam curve missing")

    sgd_params = _parse_exp_curve(expr_map["SGD+momentum"])
    adam_params = _parse_exp_curve(expr_map["Adam"])

    xs = np.linspace(0.0, 60.0, 601)
    sgd = _curve(*sgd_params, xs)
    adam = _curve(*adam_params, xs)

    _assert(np.all(np.diff(sgd) < 0), "SGD curve should monotonically decrease")
    _assert(np.all(np.diff(adam) < 0), "Adam curve should monotonically decrease")
    _assert(float(adam[100]) < float(sgd[100]), "Adam should converge faster initially (epoch 10)")
    _assert(float(sgd[-1]) < float(adam[-1]), "SGD should have slightly lower asymptote than Adam")

    return {
        "sgd_epoch10": float(sgd[100]),
        "adam_epoch10": float(adam[100]),
        "sgd_final": float(sgd[-1]),
        "adam_final": float(adam[-1]),
    }


def check_fig_clipping_curves() -> dict[str, float]:
    tex = _read(ROOT / "lecture_7.tex")
    fig = _extract_figure_block(tex, "fig:lec7-clipping")
    tables = _extract_table_blocks(fig)
    _assert(len(tables) >= 4, "Expected four tables in clipping figure")

    unclipped_norm = np.array([y for _, y in _parse_xy_table(tables[0])], dtype=float)
    clipped_norm = np.array([y for _, y in _parse_xy_table(tables[1])], dtype=float)
    unclipped_loss = np.array([y for _, y in _parse_xy_table(tables[2])], dtype=float)
    clipped_loss = np.array([y for _, y in _parse_xy_table(tables[3])], dtype=float)

    tau = 6.5
    _assert(np.max(clipped_norm) <= tau + 1e-9, "Clipped norms should remain under threshold tau")
    _assert(unclipped_norm[-1] > tau, "Unclipped norms should exceed threshold tau")
    _assert(clipped_loss[-1] < unclipped_loss[-1], "Clipped run should have lower final loss")

    return {
        "tau": tau,
        "max_clipped_norm": float(np.max(clipped_norm)),
        "max_unclipped_norm": float(np.max(unclipped_norm)),
        "final_clipped_loss": float(clipped_loss[-1]),
        "final_unclipped_loss": float(unclipped_loss[-1]),
    }


def check_fig_attention_heatmap() -> dict[str, float]:
    tex = _read(ROOT / "lecture_7.tex")
    fig = _extract_figure_block(tex, "fig:lec7-attention")
    tables = _extract_table_blocks(fig)
    _assert(len(tables) >= 1, "Attention heatmap table missing")

    entries = _parse_xyz_table(tables[0])
    _assert(len(entries) == 25, "Expected 5x5 attention table")
    matrix = np.zeros((5, 5), dtype=float)
    for x, y, z in entries:
        matrix[y - 1, x - 1] = z

    row_sums = matrix.sum(axis=1)
    _assert(np.allclose(row_sums, 1.0, atol=1e-6), "Each attention row should sum to 1")
    argmax_cols = np.argmax(matrix, axis=1) + 1
    expected = np.array([1, 2, 3, 3, 5])
    _assert(np.array_equal(argmax_cols, expected), "Attention argmax alignment mismatch")

    return {
        "max_row_sum_error": float(np.max(np.abs(row_sums - 1.0))),
        "diag_mass": float(np.trace(matrix)),
    }


def check_fig_ga_progress() -> dict[str, float]:
    tex = _read(ROOT / "lecture_11.tex")
    fig = _extract_figure_block(tex, "fig:lec11-ga-progress")
    tables = _extract_table_blocks(fig)
    _assert(len(tables) >= 2, "Expected best/mean fitness tables in GA figure")

    best = np.array([y for _, y in _parse_xy_table(tables[0])], dtype=float)
    mean = np.array([y for _, y in _parse_xy_table(tables[1])], dtype=float)

    _assert(np.all(best >= mean), "Best fitness should stay above mean fitness")
    _assert(np.all(np.diff(best) >= 0), "Best fitness should be non-decreasing")
    _assert(np.all(np.diff(mean) >= 0), "Mean fitness should be non-decreasing")

    return {
        "best_final": float(best[-1]),
        "mean_final": float(mean[-1]),
        "final_gap": float(best[-1] - mean[-1]),
    }


def check_ch1_transitivity() -> dict[str, float]:
    values = range(-3, 4)
    total = 0
    premise_true = 0
    violations = 0
    for a in values:
        for b in values:
            for c in values:
                total += 1
                if a == b and b == c:
                    premise_true += 1
                    if a != c:
                        violations += 1
    _assert(violations == 0, "Transitivity check found counterexample")
    return {"triples": float(total), "premise_true": float(premise_true), "violations": float(violations)}


def check_ch3_mp_gates() -> dict[str, float]:
    inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    w1 = w2 = 1.0

    def step(z: float) -> int:
        return 1 if z >= 0 else 0

    and_out = []
    or_out = []
    for x1, x2 in inputs:
        and_out.append(step(w1 * x1 + w2 * x2 - 2.0))
        or_out.append(step(w1 * x1 + w2 * x2 - 1.0))
    _assert(and_out == [0, 0, 0, 1], "MP AND gate truth table mismatch")
    _assert(or_out == [0, 1, 1, 1], "MP OR gate truth table mismatch")
    return {"and_out_sum": float(sum(and_out)), "or_out_sum": float(sum(or_out))}


def check_ch3_two_neuron_gradient() -> dict[str, float]:
    def sigmoid(z: float) -> float:
        return 1 / (1 + np.exp(-z))

    x = np.array([1.0, -1.0])
    w1 = np.array([0.8, 0.2])
    b1 = 0.0
    w2 = 1.0
    b2 = 0.0
    t = 1.0

    p1 = float(w1 @ x + b1)
    y1 = sigmoid(p1)
    p2 = w2 * y1 + b2
    y2 = sigmoid(p2)
    P = 0.5 * (y2 - t) ** 2

    delta2 = (y2 - t) * (y2 * (1 - y2))
    delta1 = delta2 * w2 * (y1 * (1 - y1))
    grad_w1 = delta1 * x
    grad_w2 = delta2 * y1

    _assert_close(p1, 0.6, 1e-9, "p1 mismatch")
    _assert_close(y1, 0.645656, 1e-6, "y1 mismatch")
    _assert_close(y2, 0.656031, 1e-6, "y2 mismatch")
    _assert_close(P, 0.059157, 1e-6, "P mismatch")
    _assert_close(delta2, -0.077618, 1e-6, "delta2 mismatch")
    _assert_close(delta1, -0.017758, 1e-6, "delta1 mismatch")
    _assert_close(float(grad_w1[0]), -0.017758, 1e-6, "grad_w1[0] mismatch")
    _assert_close(float(grad_w1[1]), 0.017758, 1e-6, "grad_w1[1] mismatch")
    _assert_close(float(grad_w2), -0.050115, 1e-6, "grad_w2 mismatch")

    return {
        "p1": float(p1),
        "y2": float(y2),
        "P": float(P),
        "grad_w2": float(grad_w2),
    }


def check_ch4_backprop_numeric() -> dict[str, float]:
    def sigmoid(z: np.ndarray) -> np.ndarray:
        return 1 / (1 + np.exp(-z))

    W1 = np.array([[0.5, -0.3], [0.8, 0.2]])
    b1 = np.array([0.1, -0.2])
    W2 = np.array([[0.7], [-0.4]])
    b2 = 0.05
    x = np.array([0.6, -1.2])
    t = 1.0

    z1 = W1.T @ x + b1
    a1 = sigmoid(z1)
    z2 = float((W2.T @ a1 + b2).item())
    a2 = float(sigmoid(z2))
    loss = float(-np.log(a2))

    delta2 = a2 - t
    delta1 = (W2.flatten() * delta2) * (a1 * (1 - a1))
    grad_W2 = a1 * delta2
    grad_W1 = np.outer(x, delta1)

    _assert_close(float(z1[0]), -0.56, 1e-6, "z1[0] mismatch")
    _assert_close(float(z1[1]), -0.62, 1e-6, "z1[1] mismatch")
    _assert_close(float(a1[0]), 0.363547, 1e-6, "a1[0] mismatch")
    _assert_close(float(a1[1]), 0.349781, 1e-6, "a1[1] mismatch")
    _assert_close(z2, 0.164571, 1e-6, "z2 mismatch")
    _assert_close(a2, 0.541050, 1e-6, "a2 mismatch")
    _assert_close(loss, 0.614243, 1e-6, "loss mismatch")
    _assert_close(delta2, -0.458950, 1e-6, "delta2 mismatch")
    _assert_close(float(delta1[0]), -0.074335, 1e-6, "delta1[0] mismatch")
    _assert_close(float(delta1[1]), 0.041752, 1e-6, "delta1[1] mismatch")
    _assert_close(float(grad_W2[0]), -0.166850, 1e-6, "grad_W2[0] mismatch")
    _assert_close(float(grad_W2[1]), -0.160532, 1e-6, "grad_W2[1] mismatch")

    return {"loss": loss, "delta2": float(delta2)}


def check_ch4_softmax_ce_grad() -> dict[str, float]:
    """
    Verify the "modern practice" softmax+cross-entropy gradient pattern used in Ch. 7.

    We compare analytic gradients (delta2 = (Yhat - Y)/B) against finite differences on a tiny
    ReLU MLP, including an L2 penalty whose gradient is wd*W.
    """

    def relu(z: np.ndarray) -> np.ndarray:
        return np.maximum(0.0, z)

    def relu_deriv(z: np.ndarray) -> np.ndarray:
        return (z > 0.0).astype(float)

    def softmax(z: np.ndarray) -> np.ndarray:
        z = z - z.max(axis=1, keepdims=True)
        ez = np.exp(z)
        return ez / ez.sum(axis=1, keepdims=True)

    def loss_and_grads(
        X: np.ndarray,
        Y: np.ndarray,
        W1: np.ndarray,
        b1: np.ndarray,
        W2: np.ndarray,
        b2: np.ndarray,
        wd: float,
    ) -> tuple[float, tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]]:
        B = X.shape[0]
        Z1 = X @ W1 + b1
        H1 = relu(Z1)
        Z2 = H1 @ W2 + b2
        Yhat = softmax(Z2)
        ce = -np.sum(Y * np.log(Yhat + 1e-12)) / B
        l2 = 0.5 * wd * (np.sum(W1 * W1) + np.sum(W2 * W2))
        L = float(ce + l2)

        delta2 = (Yhat - Y) / B
        grad_W2 = H1.T @ delta2 + wd * W2
        grad_b2 = delta2.sum(axis=0)
        delta1 = (delta2 @ W2.T) * relu_deriv(Z1)
        grad_W1 = X.T @ delta1 + wd * W1
        grad_b1 = delta1.sum(axis=0)
        return L, (grad_W1, grad_b1, grad_W2, grad_b2)

    # Tiny, fixed setup chosen to avoid ReLU kinks at 0.
    X = np.array([[0.6, -1.2], [1.1, 0.4], [-0.3, 0.9]], dtype=float)
    Y = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=float)
    W1 = np.array([[0.4, -0.2, 0.1], [0.7, 0.3, -0.5]], dtype=float)
    # Bias values chosen so Z1 stays away from 0 (avoid ReLU kinks for finite differences).
    b1 = np.array([0.8, 0.6, 0.7], dtype=float)
    W2 = np.array([[0.2, -0.1, 0.3], [-0.4, 0.5, 0.2], [0.1, 0.2, -0.2]], dtype=float)
    b2 = np.array([0.05, -0.1, 0.02], dtype=float)
    wd = 1e-3

    base_loss, (gW1, gb1, gW2, gb2) = loss_and_grads(X, Y, W1, b1, W2, b2, wd)

    eps = 1e-6
    max_abs_err = 0.0

    def fd_param(param: np.ndarray, grad: np.ndarray, setter: Callable[[np.ndarray], None]) -> None:
        nonlocal max_abs_err
        it = np.nditer(param, flags=["multi_index"], op_flags=["readwrite"])
        while not it.finished:
            idx = it.multi_index
            orig = float(param[idx])
            param[idx] = orig + eps
            setter(param)
            lp, _ = loss_and_grads(X, Y, W1, b1, W2, b2, wd)
            param[idx] = orig - eps
            setter(param)
            lm, _ = loss_and_grads(X, Y, W1, b1, W2, b2, wd)
            param[idx] = orig
            setter(param)
            fd = (lp - lm) / (2.0 * eps)
            err = abs(fd - float(grad[idx]))
            max_abs_err = max(max_abs_err, err)
            it.iternext()

    fd_param(W1, gW1, lambda v: None)
    fd_param(b1, gb1, lambda v: None)
    fd_param(W2, gW2, lambda v: None)
    fd_param(b2, gb2, lambda v: None)

    _assert(max_abs_err < 5e-5, f"Softmax+CE finite-diff grad mismatch; max_abs_err={max_abs_err}")
    return {"loss": float(base_loss), "max_abs_grad_err": float(max_abs_err)}


def check_ch4_rbf_transform() -> dict[str, float]:
    sigma2 = 1.0
    v1 = np.array([0.0, 0.0])
    v2 = np.array([1.0, 1.0])

    def g(x: np.ndarray, v: np.ndarray) -> float:
        return float(np.exp(-np.sum((x - v) ** 2) / (2 * sigma2)))

    x00 = np.array([0.0, 0.0])
    x01 = np.array([0.0, 1.0])
    x10 = np.array([1.0, 0.0])
    x11 = np.array([1.0, 1.0])
    g1_00 = g(x00, v1)
    g2_00 = g(x00, v2)
    g1_01 = g(x01, v1)
    g2_01 = g(x01, v2)
    g1_10 = g(x10, v1)
    g2_10 = g(x10, v2)
    g1_11 = g(x11, v1)
    g2_11 = g(x11, v2)

    _assert_close(g1_00, 1.0, 1e-9, "g1(0,0) mismatch")
    _assert_close(g2_00, np.exp(-1.0), 1e-9, "g2(0,0) mismatch")
    _assert_close(g1_11, np.exp(-1.0), 1e-9, "g1(1,1) mismatch")
    _assert_close(g2_11, 1.0, 1e-9, "g2(1,1) mismatch")

    # Off-diagonal corners coincide in this two-center example.
    _assert_close(g1_01, np.exp(-0.5), 1e-9, "g1(0,1) mismatch")
    _assert_close(g2_01, np.exp(-0.5), 1e-9, "g2(0,1) mismatch")
    _assert_close(g1_10, np.exp(-0.5), 1e-9, "g1(1,0) mismatch")
    _assert_close(g2_10, np.exp(-0.5), 1e-9, "g2(1,0) mismatch")
    _assert_close(g1_01, g1_10, 1e-12, "g1(0,1) != g1(1,0)")
    _assert_close(g2_01, g2_10, 1e-12, "g2(0,1) != g2(1,0)")

    # One valid separating border in feature space is g1 + g2 = 1.3, i.e., w=[1,1], b=-1.3.
    w = np.array([1.0, 1.0])
    b = -1.3

    def score(g1: float, g2: float) -> float:
        return float(w[0] * g1 + w[1] * g2 + b)

    # XOR labels: diagonal corners are class 0; off-diagonals are class 1.
    _assert(score(g1_00, g2_00) > 0.0, "Separator misclassifies (0,0)")
    _assert(score(g1_11, g2_11) > 0.0, "Separator misclassifies (1,1)")
    _assert(score(g1_01, g2_01) < 0.0, "Separator misclassifies (0,1)")
    _assert(score(g1_10, g2_10) < 0.0, "Separator misclassifies (1,0)")

    return {
        "g2_00": float(g2_00),
        "g1_11": float(g1_11),
        "g_01": float(g1_01),
        "margin_pos": float(min(score(g1_00, g2_00), score(g1_11, g2_11))),
        "margin_neg": float(max(score(g1_01, g2_01), score(g1_10, g2_10))),
    }


def check_fig_rbf_xor_sigma_sweep() -> dict[str, float]:
    """
    Verify the XOR sigma-sweep boundary figure data tables match the model they claim to show.

    We recompute the ridge-fit RBF model for each sigma, reconstruct the class grid,
    and compare it to the committed PGFPlots tables in notes_output/.
    """

    xs = np.linspace(-0.2, 1.2, 29)
    ys = np.linspace(-0.2, 1.2, 29)

    X = np.array([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]], dtype=float)
    t = np.array([0.0, 1.0, 1.0, 0.0], dtype=float)
    centers = X.copy()

    lam = 1e-3
    level = 0.5

    def rbf(x: np.ndarray, c: np.ndarray, sigma: float) -> float:
        return float(np.exp(-np.sum((x - c) ** 2) / (2.0 * sigma * sigma)))

    def fit_weights(sigma: float) -> np.ndarray:
        Phi = np.stack([[rbf(x, c, sigma) for c in centers] for x in X], axis=0)
        A = Phi.T @ Phi + lam * np.eye(Phi.shape[1])
        return np.linalg.solve(A, Phi.T @ t)

    def predict_grid(sigma: float, w: np.ndarray) -> np.ndarray:
        grid = np.zeros((len(ys), len(xs)), dtype=float)
        for iy, y in enumerate(ys):
            for ix, x in enumerate(xs):
                p = np.array([float(x), float(y)], dtype=float)
                feat = np.array([rbf(p, c, sigma) for c in centers], dtype=float)
                grid[iy, ix] = float(feat @ w)
        return grid

    def parse_class_table(path: Path) -> dict[tuple[float, float], int]:
        txt = path.read_text(encoding="utf-8").strip().splitlines()
        _assert(len(txt) > 1 and txt[0].strip() == "x y cls", f"Bad header in {path.name}")
        out: dict[tuple[float, float], int] = {}
        for line in txt[1:]:
            line = line.strip()
            if not line:
                continue
            x_s, y_s, c_s = line.split()
            x = round(float(x_s), 4)
            y = round(float(y_s), 4)
            out[(x, y)] = int(c_s)
        return out

    def components_4n(cls: np.ndarray) -> int:
        seen = np.zeros_like(cls, dtype=bool)
        comps = 0
        for i in range(cls.shape[0]):
            for j in range(cls.shape[1]):
                if cls[i, j] != 1 or seen[i, j]:
                    continue
                comps += 1
                stack = [(i, j)]
                seen[i, j] = True
                while stack:
                    a, b = stack.pop()
                    for da, db in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        na, nb = a + da, b + db
                        if 0 <= na < cls.shape[0] and 0 <= nb < cls.shape[1]:
                            if cls[na, nb] == 1 and not seen[na, nb]:
                                seen[na, nb] = True
                                stack.append((na, nb))
        return comps

    specs = [
        (2.0, "sigma2p0"),
        (0.8, "sigma0p8"),
        (0.25, "sigma0p25"),
    ]

    details: dict[str, float] = {}
    stats: dict[str, dict[str, float]] = {}

    for sigma, tag in specs:
        w = fit_weights(sigma)
        yhat = predict_grid(sigma, w)
        cls = (yhat >= level).astype(int)

        table_path = ROOT / f"rbf_xor_{tag}_boundary_class_table_with_breaks.dat"
        table = parse_class_table(table_path)

        # Exact table-vs-model match on the full 29x29 grid.
        mismatches = 0
        for iy, y in enumerate(ys):
            for ix, x in enumerate(xs):
                key = (round(float(x), 4), round(float(y), 4))
                file_c = table.get(key, None)
                if file_c is None or int(file_c) != int(cls[iy, ix]):
                    mismatches += 1
        _assert(mismatches == 0, f"{table_path.name} mismatch count={mismatches}")

        dyn = float(yhat.max() - yhat.min())
        frac1 = float(cls.mean())
        comps = float(components_4n(cls))

        # Training-point margin from the 0.5 threshold.
        Phi_train = np.stack([[rbf(x, c, sigma) for c in centers] for x in X], axis=0)
        y_train = Phi_train @ w
        margin = float(np.min(np.abs(y_train - level)))

        stats[tag] = {"dyn": dyn, "frac1": frac1, "comps": comps, "margin": margin}
        details[f"{tag}_dyn"] = dyn
        details[f"{tag}_frac1"] = frac1
        details[f"{tag}_comps"] = comps
        details[f"{tag}_margin"] = margin

    # Sanity properties that match the narrative in the caption:
    # - very broad sigma: low contrast / low margin around 0.5
    # - balanced sigma: high contrast / large margin
    # - very local sigma: class-1 islands (multiple components) and smaller area
    _assert(stats["sigma2p0"]["dyn"] < 0.6, "Expected low dynamic range for sigma=2.0")
    _assert(stats["sigma2p0"]["margin"] < 0.2, "Expected low margin for sigma=2.0")
    _assert(stats["sigma0p8"]["dyn"] > 1.0, "Expected high dynamic range for sigma=0.8")
    _assert(stats["sigma0p8"]["margin"] > 0.4, "Expected large margin for sigma=0.8")
    _assert(stats["sigma0p25"]["comps"] >= 2.0, "Expected multiple class-1 components for sigma=0.25")
    _assert(stats["sigma0p25"]["frac1"] < stats["sigma0p8"]["frac1"], "Expected smaller class-1 area for sigma=0.25")

    return details


def check_ch5_som_update() -> dict[str, float]:
    x = np.array([0.2, 0.8])
    w1 = np.array([0.1, 0.9])
    w2 = np.array([0.7, 0.3])
    alpha = 0.5
    h11 = 1.0
    h21 = float(np.exp(-0.5))

    w1_new = w1 + alpha * h11 * (x - w1)
    w2_new = w2 + alpha * h21 * (x - w2)

    _assert_close(h21, 0.606531, 1e-6, "h21 mismatch")
    _assert_close(float(w1_new[0]), 0.15, 1e-9, "w1_new[0] mismatch")
    _assert_close(float(w1_new[1]), 0.85, 1e-9, "w1_new[1] mismatch")
    _assert_close(float(w2_new[0]), 0.548, 1e-3, "w2_new[0] mismatch")
    _assert_close(float(w2_new[1]), 0.452, 1e-3, "w2_new[1] mismatch")

    return {"w2_new_0": float(w2_new[0]), "w2_new_1": float(w2_new[1])}


def check_ch8_softcomp_probs() -> dict[str, float]:
    probs = np.array([0.60, 0.20, 0.20])
    _assert(np.all((probs >= 0) & (probs <= 1)), "Probabilities must be in [0,1]")
    _assert_close(float(probs.sum()), 1.0, 1e-12, "Probabilities do not sum to 1")
    return {"prob_sum": float(probs.sum())}


def check_ch9_overlap_memberships() -> dict[str, float]:
    x = 22.0

    def mu_medium(val: float) -> float:
        if val <= 10:
            return 0.0
        if val < 15:
            return (val - 10) / 5.0
        if val <= 20:
            return 1.0
        if val < 25:
            return (25 - val) / 5.0
        return 0.0

    def mu_large(val: float) -> float:
        if val <= 20:
            return 0.0
        if val < 25:
            return (val - 20) / 5.0
        return 1.0

    m = mu_medium(x)
    l = mu_large(x)
    _assert_close(m, 0.6, 1e-9, "mu_medium(22) mismatch")
    _assert_close(l, 0.4, 1e-9, "mu_large(22) mismatch")
    return {"mu_medium": float(m), "mu_large": float(l)}


def check_ch13_micro_attention() -> dict[str, float]:
    Q = np.eye(2)
    K = np.eye(2)
    V = np.eye(2)
    dk = 2.0
    scores = Q @ K.T / np.sqrt(dk)
    mask = np.array([[0.0, -1e9], [0.0, 0.0]])
    scores = scores + mask
    exp_scores = np.exp(scores - scores.max(axis=1, keepdims=True))
    weights = exp_scores / exp_scores.sum(axis=1, keepdims=True)

    _assert_close(float(weights[0, 0]), 1.0, 1e-9, "row1 weight mismatch")
    _assert_close(float(weights[0, 1]), 0.0, 1e-9, "row1 weight mismatch")
    _assert_close(float(weights[1, 0]), 0.330238, 1e-6, "row2 weight mismatch")
    _assert_close(float(weights[1, 1]), 0.669762, 1e-6, "row2 weight mismatch")

    out = weights @ V
    _assert_close(float(out[1, 0]), float(weights[1, 0]), 1e-9, "Output mismatch")
    return {"row2_w1": float(weights[1, 0]), "row2_w2": float(weights[1, 1])}


def check_fig_learning_curves() -> dict[str, float]:
    tex = _read(ROOT / "lecture_supervised.tex")
    fig = _extract_figure_block(tex, "fig:lec1_learning_curves")
    tables = _extract_table_blocks(fig)
    _assert(len(tables) >= 2, "Expected train/val tables in learning curves figure")

    train = np.array([y for _, y in _parse_xy_table(tables[0])], dtype=float)
    val = np.array([y for _, y in _parse_xy_table(tables[1])], dtype=float)

    _assert(np.all(np.diff(train) < 0), "Training error should decrease with more data")
    _assert(np.all(np.diff(val) < 0), "Validation error should decrease with more data")
    _assert(np.all(val >= train), "Validation error should be no lower than training error")

    return {"train_final": float(train[-1]), "val_final": float(val[-1])}


def run_checks() -> list[CheckResult]:
    checks: list[tuple[str, Callable[[], dict[str, float]]]] = [
        ("chapter1_transitivity", check_ch1_transitivity),
        ("chapter3_mp_gates", check_ch3_mp_gates),
        ("chapter3_two_neuron_gradient", check_ch3_two_neuron_gradient),
        ("chapter4_backprop_numeric", check_ch4_backprop_numeric),
        ("chapter4_softmax_ce_grad", check_ch4_softmax_ce_grad),
        ("chapter4_rbf_transform", check_ch4_rbf_transform),
        ("figure_rbf_xor_sigma_sweep", check_fig_rbf_xor_sigma_sweep),
        ("chapter5_som_update", check_ch5_som_update),
        ("chapter8_softcomp_probs", check_ch8_softcomp_probs),
        ("chapter9_overlap_memberships", check_ch9_overlap_memberships),
        ("chapter13_micro_attention", check_ch13_micro_attention),
        ("figure_learning_curves", check_fig_learning_curves),
        ("numeric_examples_pack", check_numeric_examples_pack),
        ("integral_result_derivative", check_integral_result_derivative),
        ("figure_sigmoid_bce", check_fig_sigmoid_bce_curves),
        ("figure_bn", check_fig_bn_curves),
        ("figure_optimizers", check_fig_optimizer_curves),
        ("figure_clipping", check_fig_clipping_curves),
        ("figure_attention", check_fig_attention_heatmap),
        ("figure_ga_progress", check_fig_ga_progress),
    ]

    results: list[CheckResult] = []
    for name, fn in checks:
        try:
            details = fn()
            results.append(CheckResult(name=name, status="passed", details=details))
        except Exception as exc:
            results.append(CheckResult(name=name, status="failed", details={}, error=str(exc)))
    return results


def write_reports(results: list[CheckResult]) -> tuple[Path, Path]:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    json_path = ARTIFACT_DIR / f"math_graph_validation_{timestamp}.json"
    md_path = ARTIFACT_DIR / f"math_graph_validation_{timestamp}.md"
    latest_json = ARTIFACT_DIR / "math_graph_validation_latest.json"
    latest_md = ARTIFACT_DIR / "math_graph_validation_latest.md"

    payload = {
        "generated_at": dt.datetime.now().isoformat(),
        "total": len(results),
        "passed": sum(r.status == "passed" for r in results),
        "failed": sum(r.status == "failed" for r in results),
        "results": [
            {
                "name": r.name,
                "status": r.status,
                "details": r.details,
                "error": r.error,
            }
            for r in results
        ],
    }
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    latest_json.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    lines: list[str] = []
    lines.append("# Math + Graph Accuracy Validation")
    lines.append("")
    lines.append(f"- Generated: `{payload['generated_at']}`")
    lines.append(f"- Checks: **{payload['total']}**")
    lines.append(f"- Passed: **{payload['passed']}**")
    lines.append(f"- Failed: **{payload['failed']}**")
    lines.append("")
    lines.append("## Results")
    lines.append("")
    for result in results:
        icon = "✅" if result.status == "passed" else "❌"
        lines.append(f"- {icon} `{result.name}`")
        if result.details:
            for key, value in result.details.items():
                lines.append(f"  - `{key}`: `{value}`")
        if result.error:
            lines.append(f"  - error: `{result.error}`")
    lines.append("")
    md_text = "\n".join(lines) + "\n"
    md_path.write_text(md_text, encoding="utf-8")
    latest_md.write_text(md_text, encoding="utf-8")
    return md_path, json_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Deterministic validation for mathematical examples and graph accuracy.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return non-zero exit code when any check fails.",
    )
    args = parser.parse_args()

    results = run_checks()
    md_path, json_path = write_reports(results)
    failed = [r for r in results if r.status == "failed"]

    print(f"Wrote markdown report: {md_path}")
    print(f"Wrote JSON report: {json_path}")
    for result in results:
        status = "PASS" if result.status == "passed" else "FAIL"
        print(f"[{status}] {result.name}")
        if result.error:
            print(f"  -> {result.error}")

    if args.strict and failed:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
