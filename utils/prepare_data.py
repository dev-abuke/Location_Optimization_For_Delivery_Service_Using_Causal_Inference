from math import radians, cos, sin, asin, sqrt
import pandas as pd
import numpy as np


class DataPreparation:
    """
    Performs feature engineering
    """
    def __init__(self, ) -> None:
        pass

    def get_hour_of_day(self, df_column: pd.DatetimeIndex):
        """
        Parameters: dataframe column of datatype datetime
        Returns: the hour of the day of the datetime object - 24 hour format
        """
        return df_column.hour

    def get_trip_duration(self, df_start_col, df_end_col):
        """
        calculate the time taken to complete an order
        Parameters: start datetime, end datetime 
        Returns: duration in minutes
        """
        time_diff = df_end_col - df_start_col
        return time_diff
    
    def remove_outliers(self, df: pd.DataFrame):
        # Calculate the Interquartile Range (IQR)
        Q1 = df['Trip Duration'].quantile(0.25)
        Q3 = df['Trip Duration'].quantile(0.75)
        IQR = Q3 - Q1

        # Determine outlier thresholds
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        # Filter out outliers
        completed_orders_no_outliers = df[
            (df['Trip Duration'] >= lower_bound) &
            (df['Trip Duration'] <= upper_bound)
        ]

        return completed_orders_no_outliers
    
    def export_csv(self, df: pd.DataFrame, path: str):
        """
        Export a DataFrame to a file.

        This function takes in two parameters:
        - df: The DataFrame to be exported.
        - path: The file path where the DataFrame will be saved.

        This function returns a value. The return value is the result of calling the to_csv method on the DataFrame.
        The to_csv method is called with two arguments:
        - path: The file path where the DataFrame will be saved.
        - index=False: This argument is used to exclude the index column from the saved file.

        The purpose of this function is to save a DataFrame to a file in the CSV format.
        The CSV file will not include the index column of the DataFrame.

        """
        # Save the DataFrame to the specified file path
        out = df.to_csv(path, index=False)
        
        return out
    
    def get_trip_duration(self, df_start_col: pd.DataFrame, df_end_col: pd.DataFrame):
        """
        calculate the time taken to complete an order
        Parameters: start datetime, end datetime
        Returns: duration in minutes
        """
        time_diff = df_end_col - df_start_col.dt.total_seconds() / 60
        
        return time_diff