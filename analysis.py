import matplotlib.pyplot as plt
import numpy as np

# --- Data ---
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
turnover_data = {
    'Q1': 0.23,
    'Q2': 2.89,
    'Q3': 3.44,
    'Q4': 5.25,
}
industry_benchmark = 8
average_turnover = 2.95

# --- Analysis ---
turnover_values = list(turnover_data.values())
quarterly_gap = {q: industry_benchmark - v for q, v in turnover_data.items()}
average_gap = industry_benchmark - average_turnover

# --- Console Output ---
print("--- Retail Inventory Turnover Analysis ---")
print(f"Industry Benchmark Target: {industry_benchmark}")
print("\nQuarterly Turnover:")
for q, v in turnover_data.items():
    print(f"  - {q}: {v:.2f} (Gap: {quarterly_gap[q]:.2f})")
print(f"\nAverage Turnover: {average_turnover:.2f}")
print(f"Average Gap to Benchmark: {average_gap:.2f}")


# --- Visualization ---
fig, ax = plt.subplots(figsize=(10, 6))

# Bar chart for quarterly turnover
bars = ax.bar(quarters, turnover_values, color='skyblue', label='Quarterly Turnover')

# Benchmark line
ax.axhline(y=industry_benchmark, color='r', linestyle='--', linewidth=2, label=f'Industry Benchmark ({industry_benchmark})')

# Add labels and title
ax.set_ylabel('Inventory Turnover Rate')
ax.set_xlabel('Quarter')
ax.set_title('Quarterly Inventory Turnover vs. Industry Benchmark')
ax.set_ylim(0, industry_benchmark + 1)
ax.legend()

# Add data labels on bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval + 0.1, f'{yval:.2f}', ha='center', va='bottom')

# Save the figure
plt.savefig('inventory_turnover.png')

print("\nVisualization saved as 'inventory_turnover.png'")
