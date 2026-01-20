import matplotlib.pyplot as plt
import numpy as np

# Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
turnover_ratios = [0.23, 2.89, 3.44, 5.25]
average_ratio = 2.95
industry_target = 8

# Create the figure and axes objects
fig, ax = plt.subplots(figsize=(10, 6))

# Create the bar chart
ax.bar(quarters, turnover_ratios, label='Quarterly Turnover Ratio', color='skyblue')

# Add a line for the industry target
ax.axhline(y=industry_target, color='r', linestyle='--', label='Industry Target (8)')

# Add a line for the average
ax.axhline(y=average_ratio, color='g', linestyle=':', label=f'Average Ratio ({average_ratio})')

# Add labels and title
ax.set_xlabel('Quarter')
ax.set_ylabel('Inventory Turnover Ratio')
ax.set_title('Quarterly Inventory Turnover Ratio vs. Industry Target')
ax.legend()

# Add data labels on top of the bars
for i, v in enumerate(turnover_ratios):
    ax.text(i, v + 0.1, str(v), ha='center', va='bottom')

# Save the chart
plt.savefig('inventory_analysis/inventory_turnover_trend.png')

print("Chart saved as inventory_turnover_trend.png")
