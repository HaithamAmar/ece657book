"""
Quick sanity checks for numerical examples up to Chapter 18.

- Hopfield 3-neuron energy monotonicity (Ch. 10)
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


def hopfield_energy(w, s, theta=None):
    """Energy E = -0.5 sum_{i,j} w_ij s_i s_j + sum_i theta_i s_i."""
    s = np.asarray(s)
    w = np.asarray(w)
    theta = np.zeros_like(s) if theta is None else np.asarray(theta)
    return -0.5 * np.sum(w * np.outer(s, s)) + np.sum(theta * s)


def check_hopfield():
    w = np.array([[0, 3, -4],
                  [3, 0, 2],
                  [-4, 2, 0]], dtype=float)
    s0 = np.array([1, 1, -1])
    energies = {
        "s0": hopfield_energy(w, s0),
        "flip_s1": hopfield_energy(w, [-1, 1, -1]),
        "flip_s2": hopfield_energy(w, [1, -1, -1]),
        "flip_s3": hopfield_energy(w, [1, 1, 1]),
    }
    return energies


def check_stride_pad():
    x = np.array([1, 2, 0, 3, 1])
    w = np.array([1, 0, -1])
    p, s = 1, 2
    xp = np.pad(x, (p, p))
    L = (len(xp) - len(w)) // s + 1
    y = np.array([np.dot(w, xp[i : i + len(w)]) for i in range(0, L * s, s)])
    return dict(L=L, xp=xp.tolist(), y=y.tolist())


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


if __name__ == "__main__":
    print("Hopfield energies (Ch.10 example):", check_hopfield())
    print("1D stride/pad attention toy (Ch.11):", check_stride_pad())
    print("SGNS loss example (Ch.14):", check_sgns())
    print("Fuzzy composition (Ch.17):", check_fuzzy_composition())
    print("Alpha-cut mapping y=x^2 (Ch.17):", check_alpha_cut_mapping())
    print("Mamdani centroid (Ch.18):", check_mamdani_centroid())
    print("Roulette selection (Ch.19):", check_roulette_selection())
    print("GA toy initial population (Ch.19):", check_ga_initial_population())
