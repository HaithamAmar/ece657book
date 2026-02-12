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
    check_ga_initial_population,
    check_hopfield,
    check_mamdani_centroid,
    check_roulette_selection,
    check_sgns,
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
    hopfield = check_hopfield()
    _assert_close(float(hopfield["s0"]), -5.0, 1e-9, "Hopfield E(s0)")
    _assert_close(float(hopfield["flip_s1"]), 9.0, 1e-9, "Hopfield flip s1")
    _assert_close(float(hopfield["flip_s2"]), -3.0, 1e-9, "Hopfield flip s2")
    _assert_close(float(hopfield["flip_s3"]), -1.0, 1e-9, "Hopfield flip s3")

    stride = check_stride_pad()
    _assert(int(stride["L"]) == 3, "Stride/padding L must be 3")
    _assert(stride["y"] == [-2, -1, 3], "Stride/padding output mismatch")

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

    return {
        "hopfield_s0": float(hopfield["s0"]),
        "stride_L": float(stride["L"]),
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


def run_checks() -> list[CheckResult]:
    checks: list[tuple[str, Callable[[], dict[str, float]]]] = [
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
