import math
import csv

TRUE_PROBS = [
    0.1108103645,
    0.3250147865,
    0.4999972381,
    0.6749900232,
    0.8891884564,
]

def KL_divergence(p, q):
    return p * math.log(p / q) + (1 - p) * math.log((1 - p) / (1 - q))

def score(guess_probs):
    return sum(KL_divergence(p, q) for p, q in zip(TRUE_PROBS, guess_probs))

results = []

with open("submissions.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row["Name"]
        try:
            guess_probs = [float(row[f"R{i}"]) for i in range(5)]
            s = score(guess_probs)
            results.append((name, s))
        except Exception as e:
            print(f"Skipping {name} due to error: {e}")

# Sort by score (ascending)
results.sort(key=lambda x: x[1])

# Print results
for name, s in results:
    print(f"{name}: {s:.10f}")
