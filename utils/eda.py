import pandas as pd
import matplotlib.pyplot as plt

# Example EDA script
def eda():
    # Load processed data
    completed_orders_cleaned = pd.read_csv('data/completed_orders_cleaned.csv')
    
    # Perform EDA
    completed_orders_cleaned['Trip Duration'] = (completed_orders_cleaned['Trip End Time'] - completed_orders_cleaned['Trip Start Time']).dt.total_seconds() / 60
    plt.figure(figsize=(10, 6))
    plt.hist(completed_orders_cleaned['Trip Duration'], bins=100, edgecolor='k')
    plt.xlabel('Trip Duration (minutes)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Trip Durations')
    plt.show()

if __name__ == '__main__':
    eda()
