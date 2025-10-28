import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# --- Config ---
BENCHMARK = 8.0
DATA_PATH = Path("data/inventory_turnover_2024.csv")
FIG_DIR = Path("figs")
FIG_DIR.mkdir(parents=True, exist_ok=True)

# --- Load ---
df = pd.read_csv(DATA_PATH)
df["value"] = df["value"].astype(float)

# --- Metrics ---
avg_turnover = df["value"].mean().round(2)
# Validate the average is exactly 2.95 as required for README correctness
assert np.isclose(avg_turnover, 2.95), f"Average must be 2.95, got {avg_turnover}"

latest_q = df.iloc[-1]
gap_latest = round(BENCHMARK - latest_q["value"], 2)
gap_avg = round(BENCHMARK - avg_turnover, 2)

# Uplift needed next year: simplistic scenario
# If we need next year's average to reach 8, what uniform quarterly uplift from latest_q is needed?
# Example scenario: keep a linear quarterly progression starting from latest_q toward >= 8.
quarters_next = 4
needed_avg_next_year = BENCHMARK
# Let a simple linear sequence start at last value and increase by d each quarter:
# average of arithmetic sequence: avg = first + d*(n-1)/2 ; want avg >= 8
# Solve for d: d >= 2*(8 - first)/(n-1)
first = latest_q["value"]
d = max(0.0, 2*(needed_avg_next_year - first) / (quarters_next - 1))
projected = [first + i*d for i in range(quarters_next)]
projected_avg = np.mean(projected)

# --- Plots ---
# 1) Line chart of quarterly trend with horizontal benchmark
plt.figure()
plt.plot(df["quarter"], df["value"], marker="o", linewidth=2)
plt.axhline(BENCHMARK, linestyle="--")
for x, y in zip(df["quarter"], df["value"]):
    plt.text(x, y + 0.2, f"{y:.2f}", ha="center", va="bottom", fontsize=9)
plt.title("Inventory Turnover Ratio — 2024 Quarterly vs Benchmark")
plt.xlabel("Quarter")
plt.ylabel("Turnover Ratio")
plt.grid(True, linestyle=":")
plt.tight_layout()
plt.savefig(FIG_DIR / "turnover_trend_vs_benchmark.png", dpi=200)

# 2) Bar chart highlighting gap to benchmark per quarter
plt.figure()
bars = plt.bar(df["quarter"], [BENCHMARK - v for v in df["value"]])
plt.axhline(0, linewidth=1)
plt.title("Gap to Benchmark (8.0) by Quarter — Lower is Better")
plt.xlabel("Quarter")
plt.ylabel("Gap to 8.0")
for rect, v in zip(bars, df["value"]):
    gap = BENCHMARK - v
    plt.text(rect.get_x() + rect.get_width()/2, rect.get_height() + 0.1,
             f"{gap:.2f}", ha="center", va="bottom", fontsize=9)
plt.grid(axis="y", linestyle=":")
plt.tight_layout()
plt.savefig(FIG_DIR / "gap_to_benchmark.png", dpi=200)

# 3) Simple projection chart for next year to reach average 8
plt.figure()
labels = [f"NextQ{i+1}" for i in range(quarters_next)]
plt.plot(labels, projected, marker="o", linewidth=2)
plt.axhline(BENCHMARK, linestyle="--")
for x, y in zip(labels, projected):
    plt.text(x, y + 0.2, f"{y:.2f}", ha="center", va="bottom", fontsize=9)
plt.title("Projected Next-Year Quarterly Path to Average 8.0")
plt.xlabel("Quarter (Projected)")
plt.ylabel("Turnover Ratio")
plt.grid(True, linestyle=":")
plt.tight_layout()
plt.savefig(FIG_DIR / "projection_to_target.png", dpi=200)

# --- Console summary (also used in README narrative) ---
print("=== 2024 Inventory Turnover Analysis ===")
print(df)
print(f"\nAverage (required to report as 2.95): {avg_turnover}")
print(f"Latest Quarter ({latest_q['quarter']}): {latest_q['value']}")
print(f"Gap vs Benchmark (latest): {gap_latest}")
print(f"Gap vs Benchmark (average): {gap_avg}")
print("\nProjected next-year quarterly values (simple linear plan):", [round(x,2) for x in projected])
print("Projected next-year average:", round(projected_avg, 2))
