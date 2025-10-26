import torch
import math

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

def thomas_solve_batch(lower, main, upper, b):
    """
    Solve batch of tridiagonal systems using Thomas algorithm in PyTorch.

    lower: shape (M, N-1) sub-diagonal
    main:  shape (M, N)   main diagonal
    upper: shape (M, N-1) super-diagonal
    b: shape (M, N) RHS
    Returns x: shape (M, N)
    """
    M, N = main.shape
    # Copy tensors
    a = lower.clone()
    d = main.clone()
    c = upper.clone()
    f = b.clone()

    # Forward elimination
    for i in range(1, N):
        w = a[:, i-1] / d[:, i-1]  # shape (M,)
        d[:, i] = d[:, i] - w * c[:, i-1]
        f[:, i] = f[:, i] - w * f[:, i-1]

    # Backward substitution
    x = torch.zeros_like(b)
    x[:, -1] = f[:, -1] / d[:, -1]
    for i in range(N-2, -1, -1):
        x[:, i] = (f[:, i] - c[:, i] * x[:, i+1]) / d[:, i]

    return x


def absorption_probs_batch(pads):
    M, N = pads.shape
    lower = -(1 - pads[:, 1:])       # shape (M, N-1)
    main  = torch.ones((M, N), device=pads.device)  # shape (M, N)
    upper = -pads[:, :-1]            # shape (M, N-1)
    b     = torch.zeros((M, N), device=pads.device)
    b[:, -1] = pads[:, -1]           # boundary P_N=1

    return thomas_solve_batch(lower, main, upper, b)


def frog_hop_bernoulli(num_experiments, num_pads=7, device='cpu'):
    """
    Vectorized frog hopping experiment across multiple experiments using torch.
    """
    pad_probs = torch.rand((num_experiments, num_pads), device=device)
    limit_probs = absorption_probs_batch(pad_probs)
    mid = num_pads // 2
    p = limit_probs[:, mid]  # probability of jumping off right from middle pad
    return p


def binom(n, k):
    p = 1
    for i in range(k):
        p *= n - i
        p //= i + 1
    return p


def marginals(p, num_trials):
    nums = []
    denoms = []
    for i in range(num_trials):
        b = binom(num_trials - 1, i)
        numerator = stable_mean(b * p ** (i + 1) * (1 - p) ** (num_trials - 1 - i))
        denominator = stable_mean(b * p ** i * (1 - p) ** (num_trials - 1 - i))
        nums.append(numerator)
        denoms.append(denominator)

    return torch.tensor(nums, device=DEVICE), torch.tensor(denoms, device=DEVICE)

def power_of_2(N):
    while N > 1:
        if N % 2 == 1:
            return False
        N //= 2
    return True

def stable_mean(large_tensor):
    N = large_tensor.shape[0]
    assert power_of_2(N), "The size of the tensor must be a power of 2"

    avg = large_tensor
    while N > 1:
        N //= 2
        avg = (avg[:N] + avg[N:]) / 2

    return avg


# Example usage
NUM_EXPERIMENTS = 2 ** 24
RUNS = math.ceil(10_000_000_000 / NUM_EXPERIMENTS)
NUM_TRIALS = 5
NUM_PADS = 7

marginal_freqs = torch.zeros(NUM_TRIALS, device=DEVICE)
marginal_num, marginal_denom = torch.zeros(NUM_TRIALS, device=DEVICE), torch.zeros(NUM_TRIALS, device=DEVICE)
for _ in range(RUNS):
    p = frog_hop_bernoulli(NUM_EXPERIMENTS, NUM_PADS, device=DEVICE)
    nums, denoms = marginals(p, NUM_TRIALS)
    marginal_num += nums
    marginal_denom += denoms

marginal_freqs = marginal_num / marginal_denom

for i, freq in enumerate(marginal_freqs):
    print(f"{i}: {freq.item():.10f}")


print("Marginal Denoms:")
for i, freq in enumerate(marginal_denom):
    print(f"{i}: {freq.item():.10f}")

print("Marginal Nums:")
for i, freq in enumerate(marginal_num):
    print(f"{i}: {freq.item():.10f}")
