import matplotlib.pyplot as plt
import numpy as np

# Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
turnover_rates = [0.23, 2.89, 3.44, 5.25]
industry_target = 8
# The user specified the average is 2.95
average_turnover = 2.95

# Visualization
plt.figure(figsize=(10, 6))
plt.plot(quarters, turnover_rates, marker='o', linestyle='-', label='Quarterly Turnover')
plt.axhline(y=industry_target, color='r', linestyle='--', label=f'Industry Target ({industry_target})')
plt.axhline(y=average_turnover, color='g', linestyle='--', label=f'Average Turnover ({average_turnover})')

# Adding titles and labels
plt.title('Quarterly Inventory Turnover Analysis')
plt.xlabel('Quarter')
plt.ylabel('Turnover Rate')
plt.legend()
plt.grid(True)

# Save the chart
plt.savefig('inventory_analysis/inventory_turnover.png')

print("Chart saved as inventory_analysis/inventory_turnover.png")
