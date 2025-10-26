import numpy as np


def binom(n, k):
    p = 1
    for i in range(k):
        p *= n - i
        p //= i + 1
    return p


# Each freqs list contains the five pairs (P(n $R$s), P(n+1 $R$s | n $R$s))
# for n=0, 1, ..., 4.

fair_coin_freqs = np.array([
    [binom(4, i) / 16, 0.5]
    for i in range(5)
])

slider_coin_freqs = np.array([
    [1 / 5, (i + 1) / 6]
    for i in range(5)
])

B_1_4_freqs = np.array([
    [binom(i + 3, 3) / binom(8, 4), (i + 4) / 9]
    for i in range(5)
])
B_4_1_freqs = np.array([
    [binom(7 - i, 3) / binom(8, 4), (i + 1) / 9]
    for i in range(5)
])

frog_hop_denoms = [
    171.3977355957,
    88.6547470093,
    76.8949356079,
    88.6554641724,
    171.3971099854
]
sum_d = sum(frog_hop_denoms)
frog_hop_nums = [
    15.7557201385,
    25.6319026947,
    38.4470863342,
    63.0240097046,
    155.6412048340
]

frog_hop_freqs = np.array([
    [d / sum_d, n / d]
    for d, n in zip(frog_hop_denoms, frog_hop_nums)
])

weights = [
    (fair_coin_freqs, 0.1),
    (slider_coin_freqs, 0.1),
    (B_1_4_freqs, 0.05),
    (B_4_1_freqs, 0.05),
    (frog_hop_freqs, 0.7)
]

mixture_denom = sum(d[:, 0] * w for d, w in weights)
mixture_num = sum(d[:, 0] * d[:, 1] * w for d, w in weights)

mixture_freqs = mixture_num / mixture_denom

for i, freq in enumerate(mixture_freqs):
    print(f"{i}: {freq.item():.10f}")
