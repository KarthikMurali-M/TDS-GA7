import pandas as pd
import matplotlib.pyplot as plt

# Data provided by the user
data = {
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'Turnover': [0.23, 2.89, 3.44, 5.25]
}
df = pd.DataFrame(data)

# Industry target
industry_target = 8

# Calculate the average turnover
average_turnover = df['Turnover'].mean()

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['Quarter'], df['Turnover'], marker='o', linestyle='-', label='Quarterly Turnover')
plt.axhline(y=industry_target, color='r', linestyle='--', label=f'Industry Target ({industry_target})')
plt.title('Quarterly Inventory Turnover Analysis')
plt.xlabel('Quarter')
plt.ylabel('Inventory Turnover')
plt.grid(True)
plt.legend()

# Add a text box with the average turnover
plt.text(0.05, 0.95, f'Average Turnover: {average_turnover:.2f}', transform=plt.gca().transAxes,
         fontsize=12, verticalalignment='top', bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5))

# Save the chart
plt.savefig('inventory_turnover.png')

print("Chart saved as inventory_turnover.png")
print(f"Average Turnover: {average_turnover:.2f}")
