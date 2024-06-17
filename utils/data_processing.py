import pandas as pd
import numpy as np

# Example data processing script
def process_data():
    # Load data
    completed_orders = pd.read_csv('data/completed_orders.csv')
    driver_locations = pd.read_csv('data/driver_locations_during_request.csv')
    
    # Process data
    completed_orders_cleaned = completed_orders.dropna(subset=['Trip Start Time', 'Trip End Time'])
    completed_orders_cleaned['Trip Start Time'] = pd.to_datetime(completed_orders_cleaned['Trip Start Time'])
    completed_orders_cleaned['Trip End Time'] = pd.to_datetime(completed_orders_cleaned['Trip End Time'])
    
    # Save processed data
    completed_orders_cleaned.to_csv('data/completed_orders_cleaned.csv', index=False)

if __name__ == '__main__':
    process_data()
