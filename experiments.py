import csv
import random

random.seed(11111)


def fair_coin():
    return random.random() < 0.5

def slider_coin(x):
    return random.random() < x

def frog_hop(pad_probs):
    N = len(pad_probs)
    pos = N // 2
    while  0 <= pos < N:
        if random.random() < pad_probs[pos]:
            pos -= 1
        else:
            pos += 1
    
    return pos == N


def fair_coin_experiment(num_trials):
    return [fair_coin() for _ in range(num_trials)]

def slider_coin_experiment(num_trials):
    x = random.random()
    return [slider_coin(x) for _ in range(num_trials)]

def filtered_slider_coin_experiment(num_trials, num_filter_trials, filter_total):
    while True:
        x = random.random()
        f = sum(slider_coin(x) for _ in range(num_filter_trials))
        if f == filter_total:
            return [slider_coin(x) for _ in range(num_trials)]
        

def frog_hop_experiment(num_trials, num_pads=7):
    pad_probs = [random.random() for _ in range(num_pads)]
    return [frog_hop(pad_probs) for _ in range(num_trials)]



EXPERIMENT_TYPES = {
    "fair_coin": "Fair Coin",
    "slider_coin": "Slider Coin",
    "filtered_slider_coin": "Filtered Slider Coin",
    "frog_hop": "Frog Hop"
}

EXPERIMENT_COUNTS = {
    "fair_coin": 100000,
    "slider_coin": 100000,
    "filtered_slider_coin": 100000,
    "frog_hop": 700000
}

def run_experiments(experiment_counts, num_trials):
    return {
        "fair_coin": [fair_coin_experiment(num_trials) for _ in range(experiment_counts["fair_coin"])],
        "slider_coin": [slider_coin_experiment(num_trials) for _ in range(experiment_counts["slider_coin"])],
        "filtered_slider_coin": [filtered_slider_coin_experiment(num_trials, 3, f) for f in {0, 3} for _ in range(experiment_counts["filtered_slider_coin"] // 2)],
        "frog_hop": [frog_hop_experiment(num_trials) for _ in range(experiment_counts["frog_hop"])]
    }


NUM_TRIALS = 5
ALL_EXPERIMENTS = run_experiments(EXPERIMENT_COUNTS, NUM_TRIALS)

def save_all_data(save_path):
    headers = ["Experiment Type"] + [f"Trial {i}" for i in range(1, NUM_TRIALS + 1)]

    data = [
        [type_name] + ["R" if t else "L" for t in experiment]
        for experiment_type, type_name in EXPERIMENT_TYPES.items()
        for experiment in ALL_EXPERIMENTS[experiment_type]
    ]

    with open(save_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)


def save_public_data(save_path):
    headers = [f"Trial {i}" for i in range(1, NUM_TRIALS)]
    data = [
        ["R" if t else "L" for t in experiment[:NUM_TRIALS - 1]]
        for experiments in ALL_EXPERIMENTS.values()
        for experiment in experiments
    ]
    random.shuffle(data)

    with open(save_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)

def save_marginals(save_path):
    headers = ["Rs Visible", "# Hidden = R", "# Experiments", "% Hidden = R"]
    counts = {
        Rs_visible: [0, 0]
        for Rs_visible in range(NUM_TRIALS)
    }
    for experiments in ALL_EXPERIMENTS.values():
        for experiment in experiments:
            Rs_visible = sum(experiment[:-1])
            counts[Rs_visible][0] += experiment[-1]
            counts[Rs_visible][1] += 1

    with open(save_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for Rs_visible in counts:
            num_hidden_R, num_experiments = counts[Rs_visible]
            percent = (100 * num_hidden_R) / num_experiments
            writer.writerow(
                [Rs_visible, num_hidden_R, num_experiments, f"{percent:.2f}"]
            )

save_all_data("all_data.csv")
save_public_data("public.csv")
save_marginals("marginals.csv")
