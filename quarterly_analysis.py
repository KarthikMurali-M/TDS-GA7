# quarterly_analysis.py
# Author: Jules
# Contact: 24f2001293@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def generate_quarterly_data():
    """
    Generates synthetic quarterly data with a specific average and a downward trend.
    """
    # Data designed to have an average of 2.95
    data = {
        'Quarter': ['2022 Q1', '2022 Q2', '2022 Q3', '2022 Q4', '2023 Q1', '2023 Q2', '2023 Q3', '2023 Q4'],
        'Metric': [5.0, 4.5, 4.0, 3.5, 2.5, 2.0, 1.5, 0.6]
    }
    df = pd.DataFrame(data)
    return df

def create_and_save_visualization(df):
    """
    Creates and saves a line chart of the quarterly metric.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df['Quarter'], df['Metric'], marker='o', linestyle='-', color='b', label='Quarterly Metric')
    plt.axhline(y=8, color='r', linestyle='--', label='Target (8)')
    plt.title('Quarterly Metric Trend Analysis')
    plt.xlabel('Quarter')
    plt.ylabel('Metric Value')
    plt.grid(True)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('trend.png')
    print("Visualization saved as trend.png")

def main():
    """
    Main function to run the analysis.
    """
    # Generate the data
    df = generate_quarterly_data()

    # Verify the average
    average_metric = df['Metric'].mean()
    print(f"The average of the metric is: {average_metric:.2f}")

    # Create and save the visualization
    create_and_save_visualization(df)

if __name__ == '__main__':
    main()
