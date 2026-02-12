#!/usr/bin/python3
from __future__ import annotations

"""
Deterministic proof-to-code integrity checks for the book.

What this script does:
- Converts selected derivations/equations into executable numerical checks.
- Verifies that the coded equations produce the expected outcomes.
- Uses finite-difference gradient checks where applicable.
- Emits machine + human reports under notes_output/artifacts/qc/.

What this script does NOT do:
- It is not a formal theorem prover.
- It does not prove every equation in the manuscript.
- It provides a deterministic, high-signal "can this proof be implemented and trusted?" gate.
"""

import argparse
import datetime as dt
import json
import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import numpy as np


ROOT = Path(__file__).resolve().parents[1]  # notes_output/


def _sigmoid(x: np.ndarray | float) -> np.ndarray | float:
    return 1.0 / (1.0 + np.exp(-x))


def _assert_close(
    lhs: np.ndarray | float,
    rhs: np.ndarray | float,
    *,
    atol: float = 1e-9,
    rtol: float = 1e-9,
    msg: str,
) -> float:
    lhs_arr = np.asarray(lhs, dtype=float)
    rhs_arr = np.asarray(rhs, dtype=float)
    diff = float(np.max(np.abs(lhs_arr - rhs_arr)))
    if not np.allclose(lhs_arr, rhs_arr, atol=atol, rtol=rtol):
        raise AssertionError(f"{msg} (max_abs_diff={diff:.3e})")
    return diff


def _finite_diff_grad(fn: Callable[[np.ndarray], float], x: np.ndarray, eps: float = 1e-6) -> np.ndarray:
    grad = np.zeros_like(x, dtype=float)
    for i in range(x.size):
        x_pos = x.copy()
        x_neg = x.copy()
        x_pos[i] += eps
        x_neg[i] -= eps
        grad[i] = (fn(x_pos) - fn(x_neg)) / (2.0 * eps)
    return grad


def _collect_equation_labels(root: Path) -> set[str]:
    labels: set[str] = set()
    pattern = re.compile(r"\\label\{(eq:[^}]+)\}")
    for tex in root.rglob("*.tex"):
        if "artifacts" in tex.parts or "archive" in tex.parts:
            continue
        text = tex.read_text(encoding="utf-8", errors="ignore")
        labels.update(pattern.findall(text))
    return labels


@dataclass(frozen=True)
class CheckSpec:
    name: str
    labels: tuple[str, ...]
    fn: Callable[[], dict[str, float | str]]


@dataclass
class CheckResult:
    name: str
    labels: tuple[str, ...]
    status: str
    details: dict[str, float | str]
    error: str = ""


def check_bayes_theorem_and_posterior_normalization() -> dict[str, float]:
    # Eq. reference: eq:bayes_theorem
    likelihood = np.array([0.21, 0.42, 0.07], dtype=float)
    prior = np.array([0.2, 0.5, 0.3], dtype=float)
    denom = float(np.sum(likelihood * prior))
    posterior = (likelihood * prior) / denom

    if not np.all((posterior >= 0.0) & (posterior <= 1.0)):
        raise AssertionError("Posterior probabilities are outside [0,1]")

    _assert_close(
        float(np.sum(posterior)),
        1.0,
        atol=1e-12,
        rtol=0.0,
        msg="Posterior does not normalize to 1",
    )
    winner_post = int(np.argmax(posterior))
    winner_num = int(np.argmax(likelihood * prior))
    if winner_post != winner_num:
        raise AssertionError("argmax posterior disagrees with argmax Bayes numerator")

    return {
        "posterior_sum": float(np.sum(posterior)),
        "denominator": denom,
        "winning_class_index": float(winner_post),
    }


def check_logistic_nll_gradient() -> dict[str, float]:
    # Eq. reference: eq:lec2_logistic_grad
    X = np.array(
        [
            [1.0, -1.0, 0.3],
            [1.0, -0.3, 1.2],
            [1.0, 0.1, -0.8],
            [1.0, 0.7, 0.6],
            [1.0, 1.2, -0.4],
            [1.0, 2.0, 1.1],
        ],
        dtype=float,
    )
    y = np.array([0, 0, 0, 1, 1, 1], dtype=float)
    beta = np.array([0.2, -0.4, 0.7], dtype=float)

    def nll(b: np.ndarray) -> float:
        z = X @ b
        p = _sigmoid(z)
        p = np.clip(p, 1e-12, 1.0 - 1e-12)
        return float(-np.sum(y * np.log(p) + (1.0 - y) * np.log(1.0 - p)))

    p = _sigmoid(X @ beta)
    grad_analytic = X.T @ (p - y)
    grad_fd = _finite_diff_grad(nll, beta, eps=1e-6)
    max_err = _assert_close(
        grad_analytic,
        grad_fd,
        atol=1e-6,
        rtol=1e-6,
        msg="Logistic NLL gradient mismatch (analytic vs finite difference)",
    )
    return {"max_abs_grad_error": max_err, "nll": nll(beta)}


def check_two_neuron_worked_example_values() -> dict[str, float]:
    # Eq. references: eq:grad_w1, eq:grad_w2, eq:delta1, eq:delta2
    x = np.array([1.0, -1.0], dtype=float)
    t = 1.0
    w1 = np.array([0.8, 0.2], dtype=float)
    b1 = 0.0
    w2 = 1.0
    b2 = 0.0

    p1 = float(np.dot(w1, x) + b1)
    y1 = float(_sigmoid(p1))
    p2 = float(w2 * y1 + b2)
    y2 = float(_sigmoid(p2))
    loss = 0.5 * (y2 - t) ** 2
    delta2 = (y2 - t) * y2 * (1.0 - y2)
    delta1 = delta2 * w2 * y1 * (1.0 - y1)
    grad_w1 = delta1 * x
    grad_w2 = delta2 * y1

    # Chapter-embedded sanity numbers (rounded in prose).
    _assert_close(y1, 0.646, atol=1e-3, rtol=0.0, msg="y1 differs from worked-example value")
    _assert_close(y2, 0.656, atol=1e-3, rtol=0.0, msg="y2 differs from worked-example value")
    _assert_close(loss, 0.059, atol=2e-3, rtol=0.0, msg="loss differs from worked-example value")
    _assert_close(delta2, -0.078, atol=2e-3, rtol=0.0, msg="delta2 differs from worked-example value")
    _assert_close(delta1, -0.018, atol=2e-3, rtol=0.0, msg="delta1 differs from worked-example value")
    _assert_close(grad_w1, np.array([-0.018, 0.018]), atol=2e-3, rtol=0.0, msg="grad_w1 differs from worked-example value")
    _assert_close(grad_w2, -0.050, atol=2e-3, rtol=0.0, msg="grad_w2 differs from worked-example value")

    return {
        "p1": p1,
        "y1": y1,
        "p2": p2,
        "y2": y2,
        "loss": loss,
        "delta2": delta2,
        "delta1": delta1,
    }


def check_two_neuron_gradient_via_finite_difference() -> dict[str, float]:
    # Eq. references: eq:grad_w1, eq:grad_w2, eq:grad_b1, eq:grad_b2
    x = np.array([0.6, -1.1, 0.3], dtype=float)
    t = 0.25
    w1 = np.array([0.4, -0.2, 0.7], dtype=float)
    b1 = -0.15
    w2 = -0.8
    b2 = 0.35

    def forward(params: np.ndarray) -> float:
        ww1 = params[:3]
        bb1 = params[3]
        ww2 = params[4]
        bb2 = params[5]
        p1 = float(np.dot(ww1, x) + bb1)
        y1 = float(_sigmoid(p1))
        p2 = float(ww2 * y1 + bb2)
        y2 = float(_sigmoid(p2))
        return 0.5 * (y2 - t) ** 2

    params = np.array([*w1, b1, w2, b2], dtype=float)

    p1 = float(np.dot(w1, x) + b1)
    y1 = float(_sigmoid(p1))
    p2 = float(w2 * y1 + b2)
    y2 = float(_sigmoid(p2))
    delta2 = (y2 - t) * y2 * (1.0 - y2)
    delta1 = delta2 * w2 * y1 * (1.0 - y1)
    grad_analytic = np.array(
        [
            *(delta1 * x),
            delta1,
            delta2 * y1,
            delta2,
        ],
        dtype=float,
    )
    grad_fd = _finite_diff_grad(forward, params, eps=1e-6)
    max_err = _assert_close(
        grad_analytic,
        grad_fd,
        atol=1e-6,
        rtol=1e-6,
        msg="Two-neuron gradients mismatch (analytic vs finite difference)",
    )
    return {"max_abs_grad_error": max_err, "loss": forward(params)}


def _hopfield_energy(s: np.ndarray, W: np.ndarray, theta: np.ndarray) -> float:
    return float(-0.5 * s @ W @ s + theta @ s)


def check_hopfield_deltaE_identity_and_descent() -> dict[str, float]:
    # Eq. references: eq:energy_function, eq:deltaE, eq:hopfield_update_rule
    W = np.array(
        [
            [0.0, 0.6, -0.2, 0.1],
            [0.6, 0.0, 0.3, -0.4],
            [-0.2, 0.3, 0.0, 0.5],
            [0.1, -0.4, 0.5, 0.0],
        ],
        dtype=float,
    )
    theta = np.array([0.1, -0.2, 0.0, 0.15], dtype=float)
    s = np.array([1.0, -1.0, 1.0, -1.0], dtype=float)

    max_delta_err = 0.0
    for i in range(s.size):
        h_i = float(np.dot(W[i], s) - theta[i])
        s_new_i = 1.0 if h_i >= 0.0 else -1.0
        s_new = s.copy()
        s_new[i] = s_new_i
        delta_energy_direct = _hopfield_energy(s_new, W, theta) - _hopfield_energy(s, W, theta)
        delta_energy_formula = -(s_new_i - s[i]) * h_i
        delta_err = abs(delta_energy_direct - delta_energy_formula)
        max_delta_err = max(max_delta_err, delta_err)
        _assert_close(
            delta_energy_direct,
            delta_energy_formula,
            atol=1e-10,
            rtol=1e-10,
            msg=f"Hopfield deltaE mismatch at neuron index {i}",
        )

    # Deterministic asynchronous updates should never increase energy.
    idx_schedule = [0, 1, 2, 3] * 8
    energy = _hopfield_energy(s, W, theta)
    max_energy_increase = 0.0
    s_iter = s.copy()
    for i in idx_schedule:
        h_i = float(np.dot(W[i], s_iter) - theta[i])
        s_iter[i] = 1.0 if h_i >= 0.0 else -1.0
        new_energy = _hopfield_energy(s_iter, W, theta)
        increase = new_energy - energy
        max_energy_increase = max(max_energy_increase, increase)
        if increase > 1e-10:
            raise AssertionError(f"Hopfield asynchronous step increased energy by {increase:.3e}")
        energy = new_energy

    return {
        "max_abs_deltaE_error": max_delta_err,
        "max_energy_increase": max_energy_increase,
        "final_energy": energy,
    }


def check_cnn_stride_padding_output_formula() -> dict[str, float]:
    # Formula source: lecture_6 ("With stride s and padding p...")
    def formula(n: int, k: int, s: int, p: int) -> int:
        return math.floor((n + 2 * p - k) / s) + 1

    def explicit_count(n: int, k: int, s: int, p: int) -> int:
        length = n + 2 * p
        if length < k:
            return 0
        count = 0
        start = 0
        while start + k <= length:
            count += 1
            start += s
        return count

    cases = [
        (6, 3, 1, 0),
        (6, 3, 2, 0),
        (6, 3, 1, 1),
        (11, 5, 2, 2),
        (17, 3, 4, 1),
    ]
    mismatches = 0
    for n, k, s, p in cases:
        lhs = formula(n, k, s, p)
        rhs = explicit_count(n, k, s, p)
        if lhs != rhs:
            mismatches += 1
            raise AssertionError(f"CNN output-size mismatch for (n={n}, k={k}, s={s}, p={p}): formula={lhs}, explicit={rhs}")
    return {"tested_cases": float(len(cases)), "mismatches": float(mismatches)}


def check_rnn_bptt_gradient() -> dict[str, float]:
    # Eq. references: eq:simple_rnn_hidden, eq:simple_rnn_output
    x = np.array([0.4, -1.1, 0.3, 0.8], dtype=float)
    y_target = np.array([0.2, -0.1, 0.4, 0.0], dtype=float)

    def unpack(params: np.ndarray) -> tuple[float, float, float, float, float]:
        return float(params[0]), float(params[1]), float(params[2]), float(params[3]), float(params[4])

    def forward(params: np.ndarray) -> tuple[float, np.ndarray, np.ndarray]:
        W_xh, W_hh, b_h, W_hy, b_y = unpack(params)
        h_prev = 0.0
        hs = np.zeros_like(x)
        ys = np.zeros_like(x)
        loss = 0.0
        for t in range(x.size):
            a_t = x[t] * W_xh + h_prev * W_hh + b_h
            h_t = math.tanh(a_t)
            y_t = h_t * W_hy + b_y
            hs[t] = h_t
            ys[t] = y_t
            loss += 0.5 * (y_t - y_target[t]) ** 2
            h_prev = h_t
        return float(loss), hs, ys

    def loss_only(params: np.ndarray) -> float:
        return forward(params)[0]

    params = np.array([0.7, -0.25, 0.15, 1.1, -0.05], dtype=float)
    loss, hs, ys = forward(params)
    W_xh, W_hh, _, W_hy, _ = unpack(params)

    # Backprop through time
    grad = np.zeros_like(params)
    dh_next = 0.0
    h_prev = np.concatenate([[0.0], hs[:-1]])
    for t in range(x.size - 1, -1, -1):
        dL_dy = ys[t] - y_target[t]
        grad[3] += hs[t] * dL_dy  # W_hy
        grad[4] += dL_dy          # b_y

        dL_dh = dL_dy * W_hy + dh_next
        dL_da = dL_dh * (1.0 - hs[t] ** 2)

        grad[0] += x[t] * dL_da        # W_xh
        grad[1] += h_prev[t] * dL_da   # W_hh
        grad[2] += dL_da               # b_h

        dh_next = dL_da * W_hh

    grad_fd = _finite_diff_grad(loss_only, params, eps=1e-6)
    max_err = _assert_close(
        grad,
        grad_fd,
        atol=1e-6,
        rtol=1e-6,
        msg="RNN BPTT gradient mismatch (analytic vs finite difference)",
    )
    return {"max_abs_grad_error": max_err, "loss": loss}


def check_fuzzy_demorgan_and_tnorm_snorm_duality() -> dict[str, float]:
    # Eq. references: eq:fuzzy_union, eq:fuzzy_intersection, eq:fuzzy_complement, eq:tnorm-snorm-complement
    values = np.linspace(0.0, 1.0, 101, dtype=float)
    max_err = 0.0
    for a in values:
        for b in values:
            lhs1 = 1.0 - min(a, b)
            rhs1 = max(1.0 - a, 1.0 - b)
            lhs2 = 1.0 - max(a, b)
            rhs2 = min(1.0 - a, 1.0 - b)
            lhs3 = min(a, b)
            rhs3 = 1.0 - max(1.0 - a, 1.0 - b)
            for lhs, rhs in [(lhs1, rhs1), (lhs2, rhs2), (lhs3, rhs3)]:
                diff = abs(lhs - rhs)
                max_err = max(max_err, diff)
                if diff > 1e-12:
                    raise AssertionError("Fuzzy De Morgan/complementarity identity violated")
    return {"max_abs_identity_error": max_err, "grid_points": float(values.size * values.size)}


def check_fuzzy_relation_composition_example() -> dict[str, float]:
    # Eq. reference: eq:fuzzy_composition
    R1 = np.array([[0.2, 0.9], [0.5, 0.1]], dtype=float)
    R2 = np.array([[0.7, 0.3], [0.4, 0.8]], dtype=float)
    out = np.zeros((R1.shape[0], R2.shape[1]), dtype=float)
    for i in range(R1.shape[0]):
        for k in range(R2.shape[1]):
            out[i, k] = np.max(np.minimum(R1[i, :], R2[:, k]))
    expected = np.array([[0.4, 0.8], [0.5, 0.3]], dtype=float)
    max_err = _assert_close(
        out,
        expected,
        atol=1e-12,
        rtol=0.0,
        msg="Fuzzy composition example mismatch",
    )
    return {"max_abs_matrix_error": max_err}


def check_word2vec_negative_sampling_gradients() -> dict[str, float]:
    # Eq. references: eq:neg-sample-prob, eq:neg-sample-loss
    v = np.array([0.35, -0.22, 0.61], dtype=float)
    u_pos = np.array([0.5, 0.1, -0.3], dtype=float)
    u_negs = np.array(
        [
            [-0.4, 0.2, 0.7],
            [0.3, -0.6, 0.4],
        ],
        dtype=float,
    )

    def objective(flat: np.ndarray) -> float:
        vv = flat[:3]
        up = flat[3:6]
        un = flat[6:].reshape(2, 3)
        pos = float(vv @ up)
        val = math.log(_sigmoid(pos))
        for row in un:
            neg_score = float(vv @ row)
            val += math.log(_sigmoid(-neg_score))
        return float(val)

    flat = np.concatenate([v, u_pos, u_negs.reshape(-1)])

    pos = float(v @ u_pos)
    sigma_pos = float(_sigmoid(pos))
    grad_v = (1.0 - sigma_pos) * u_pos
    grad_u_pos = (1.0 - sigma_pos) * v
    grad_u_negs = np.zeros_like(u_negs)
    for i in range(u_negs.shape[0]):
        score = float(v @ u_negs[i])
        sigma_score = float(_sigmoid(score))
        grad_v += -sigma_score * u_negs[i]
        grad_u_negs[i] = -sigma_score * v

    grad_analytic = np.concatenate([grad_v, grad_u_pos, grad_u_negs.reshape(-1)])
    grad_fd = _finite_diff_grad(objective, flat, eps=1e-6)
    max_err = _assert_close(
        grad_analytic,
        grad_fd,
        atol=1e-6,
        rtol=1e-6,
        msg="Negative-sampling gradient mismatch (analytic vs finite difference)",
    )
    return {"max_abs_grad_error": max_err, "objective": objective(flat)}


def check_ga_selection_probability_consistency() -> dict[str, float]:
    # Eq. references: eq:selection_probability, eq:linear_ranking
    fitness = np.array([10.0, 20.0, 5.0, 15.0, 50.0], dtype=float)
    p = fitness / np.sum(fitness)
    _assert_close(np.sum(p), 1.0, atol=1e-12, rtol=0.0, msg="Roulette selection probabilities do not sum to 1")
    if np.any(p <= 0.0):
        raise AssertionError("Roulette selection probabilities must be positive for positive fitness")

    # Linear ranking formula as printed: verify non-negativity and normalization.
    N = 7
    s = 1.8
    ranks = np.arange(1, N + 1, dtype=float)
    p_rank = (2.0 - s) / N + (2.0 * (ranks - 1.0) * (s - 1.0)) / (N * (N - 1.0))
    _assert_close(np.sum(p_rank), 1.0, atol=1e-12, rtol=0.0, msg="Linear ranking probabilities do not sum to 1")
    if np.min(p_rank) < -1e-12:
        raise AssertionError("Linear ranking produced a negative probability")

    return {
        "roulette_sum": float(np.sum(p)),
        "linear_ranking_sum": float(np.sum(p_rank)),
        "linear_ranking_min_prob": float(np.min(p_rank)),
    }


def _build_checks() -> list[CheckSpec]:
    return [
        CheckSpec(
            name="Bayes posterior normalization",
            labels=("eq:bayes_theorem",),
            fn=check_bayes_theorem_and_posterior_normalization,
        ),
        CheckSpec(
            name="Logistic NLL gradient",
            labels=("eq:lec2_logistic_grad",),
            fn=check_logistic_nll_gradient,
        ),
        CheckSpec(
            name="Two-neuron worked example values",
            labels=("eq:grad_w1", "eq:grad_w2", "eq:delta1", "eq:delta2"),
            fn=check_two_neuron_worked_example_values,
        ),
        CheckSpec(
            name="Two-neuron finite-difference gradient",
            labels=("eq:grad_w1", "eq:grad_w2", "eq:grad_b1", "eq:grad_b2"),
            fn=check_two_neuron_gradient_via_finite_difference,
        ),
        CheckSpec(
            name="Hopfield energy descent identity",
            labels=("eq:energy_function", "eq:deltaE", "eq:hopfield_update_rule"),
            fn=check_hopfield_deltaE_identity_and_descent,
        ),
        CheckSpec(
            name="CNN stride/padding output-size formula",
            labels=("eq:auto:lecture_6:1",),
            fn=check_cnn_stride_padding_output_formula,
        ),
        CheckSpec(
            name="RNN BPTT gradient",
            labels=("eq:simple_rnn_hidden", "eq:simple_rnn_output"),
            fn=check_rnn_bptt_gradient,
        ),
        CheckSpec(
            name="Fuzzy De Morgan and t/s-norm complementarity",
            labels=("eq:fuzzy_union", "eq:fuzzy_intersection", "eq:fuzzy_complement", "eq:tnorm-snorm-complement"),
            fn=check_fuzzy_demorgan_and_tnorm_snorm_duality,
        ),
        CheckSpec(
            name="Fuzzy relation composition example",
            labels=("eq:fuzzy_composition",),
            fn=check_fuzzy_relation_composition_example,
        ),
        CheckSpec(
            name="Word2Vec negative-sampling gradients",
            labels=("eq:neg-sample-prob", "eq:neg-sample-loss"),
            fn=check_word2vec_negative_sampling_gradients,
        ),
        CheckSpec(
            name="GA selection-probability normalization",
            labels=("eq:selection_probability", "eq:linear_ranking"),
            fn=check_ga_selection_probability_consistency,
        ),
    ]


def _render_markdown(results: list[CheckResult], *, report_path: Path) -> None:
    passed = sum(1 for r in results if r.status == "PASS")
    failed = sum(1 for r in results if r.status == "FAIL")
    timestamp = dt.datetime.now().isoformat(timespec="seconds")

    lines: list[str] = []
    lines.append("# Proof Integrity Report")
    lines.append("")
    lines.append(f"- Generated: `{timestamp}`")
    lines.append(f"- Suite size: **{len(results)}** checks")
    lines.append(f"- Passed: **{passed}**")
    lines.append(f"- Failed: **{failed}**")
    lines.append("")
    lines.append("## Results")
    lines.append("")
    lines.append("| Check | Status | Linked equation labels | Notes |")
    lines.append("|---|---|---|---|")
    for r in results:
        labels = ", ".join(f"`{x}`" for x in r.labels) if r.labels else "-"
        if r.status == "PASS":
            if r.details:
                detail_frag = ", ".join(
                    f"{k}={v:.6g}" if isinstance(v, (float, int)) else f"{k}={v}"
                    for k, v in r.details.items()
                )
            else:
                detail_frag = "ok"
            notes = detail_frag
        else:
            notes = r.error.replace("\n", " ")
        lines.append(f"| {r.name} | **{r.status}** | {labels} | {notes} |")

    lines.append("")
    lines.append("## Verdict")
    lines.append("")
    if failed == 0:
        lines.append(
            "All deterministic proof-to-code checks passed. "
            "For this audited subset, the derivations are implementable and numerically consistent."
        )
    else:
        lines.append(
            "At least one deterministic proof-to-code check failed. "
            "Treat the failed checks as release blockers for mathematical integrity."
        )
    lines.append("")

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines), encoding="utf-8")


def _write_json(results: list[CheckResult], *, json_path: Path) -> None:
    payload = {
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "checks": [
            {
                "name": r.name,
                "labels": list(r.labels),
                "status": r.status,
                "details": r.details,
                "error": r.error,
            }
            for r in results
        ],
    }
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="Deterministic proof-to-code integrity checks")
    ap.add_argument("--root", default=str(ROOT), help="LaTeX root (default: notes_output)")
    ap.add_argument(
        "--report",
        default=str(ROOT / "artifacts" / "qc" / "proof_integrity_report.md"),
        help="Markdown report path",
    )
    ap.add_argument(
        "--json",
        default=str(ROOT / "artifacts" / "qc" / "proof_integrity_report.json"),
        help="JSON report path",
    )
    args = ap.parse_args()

    root = Path(args.root).resolve()
    labels_available = _collect_equation_labels(root)

    checks = _build_checks()
    results: list[CheckResult] = []
    failures = 0

    for check in checks:
        missing = [label for label in check.labels if label not in labels_available]
        if missing:
            failures += 1
            results.append(
                CheckResult(
                    name=check.name,
                    labels=check.labels,
                    status="FAIL",
                    details={},
                    error=f"Missing equation labels in sources: {', '.join(missing)}",
                )
            )
            continue
        try:
            details = check.fn()
            results.append(
                CheckResult(
                    name=check.name,
                    labels=check.labels,
                    status="PASS",
                    details=details,
                )
            )
        except AssertionError as exc:
            failures += 1
            results.append(
                CheckResult(
                    name=check.name,
                    labels=check.labels,
                    status="FAIL",
                    details={},
                    error=str(exc),
                )
            )
        except Exception as exc:  # pragma: no cover
            failures += 1
            results.append(
                CheckResult(
                    name=check.name,
                    labels=check.labels,
                    status="FAIL",
                    details={},
                    error=f"Unexpected runtime error: {exc}",
                )
            )

    report_path = Path(args.report).resolve()
    json_path = Path(args.json).resolve()
    _render_markdown(results, report_path=report_path)
    _write_json(results, json_path=json_path)

    passed = sum(1 for r in results if r.status == "PASS")
    print(f"Proof-integrity checks: {passed}/{len(results)} passed")
    print(f"Markdown report: {report_path}")
    print(f"JSON report: {json_path}")

    if failures:
        print("ERROR: proof integrity failures detected", file=sys.stderr)
        for r in results:
            if r.status == "FAIL":
                print(f"  - {r.name}: {r.error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

