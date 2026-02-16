#!/usr/bin/env python3
from __future__ import annotations

"""Reproduce the Hopfield memory-recovery example from Chapter 10."""

import numpy as np

PATTERN = np.array([-1, -1, 1, -1], dtype=float)
START = np.array([-1, -1, 1, 1], dtype=float)


def sign(value: float) -> float:
    return 1.0 if value >= 0 else -1.0


def energy(state: np.ndarray, weights: np.ndarray) -> float:
    return -0.5 * state @ weights @ state


def main() -> None:
    print("Hopfield pattern:", PATTERN)
    weights = np.outer(PATTERN, PATTERN) / PATTERN.size
    np.fill_diagonal(weights, 0.0)
    print("Weight matrix W:")
    print(weights)

    state = START.copy()
    print("Initial state:", state)
    print("Initial energy:", energy(state, weights))

    trace = [energy(state, weights)]
    for epoch in range(4):
        changed = False
        for i in range(state.size):
            field = weights[i] @ state
            state_i = sign(field)
            if state_i != state[i]:
                changed = True
            state[i] = state_i
            trace.append(energy(state, weights))
        if not changed:
            break

    print("Final state:", state)
    print("Energy trace:", trace)


if __name__ == "__main__":
    main()
