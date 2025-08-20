import pandas as pd
import matplotlib.pyplot as plt

def analyze_inventory_turnover():
    """
    Loads inventory turnover data, calculates the average,
    and generates a plot of the quarterly trend.
    """
    # Load the data
    df = pd.read_csv('retail_inventory_analysis/inventory_turnover_2024.csv')

    # Compute the average turnover
    average_turnover = df['TurnoverRatio'].mean()
    print(f"Average Inventory Turnover: {average_turnover:.2f}")

    # Plot the quarterly trend
    plt.figure(figsize=(10, 6))
    plt.plot(df['Quarter'], df['TurnoverRatio'], marker='o', linestyle='-', label='2024 Quarterly Turnover')
    plt.axhline(y=8, color='r', linestyle='--', label='Industry Target (8)')

    plt.title('Inventory Turnover Trend vs. Target - 2024')
    plt.xlabel('Quarter')
    plt.ylabel('Turnover Ratio')
    plt.grid(True)
    plt.legend()
    plt.ylim(0, 10)

    # Save the plot
    plt.savefig('retail_inventory_analysis/plot_inventory_turnover_vs_target.png')
    print("Plot saved as plot_inventory_turnover_vs_target.png")

if __name__ == '__main__':
    analyze_inventory_turnover()
