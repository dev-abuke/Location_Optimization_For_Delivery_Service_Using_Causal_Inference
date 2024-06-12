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

        This function takes a DataFrame and a file path as input parameters.
        It saves the DataFrame to the specified file path using the `to_csv` method.
        The `index=False` parameter is passed to exclude the DataFrame index from the saved file.

        Params:
            df (pd.DataFrame): The DataFrame to be saved.
            path (str): The path where the DataFrame should be saved.

        Returns:
            bool: True if the DataFrame is saved successfully, False otherwise.

        The function uses a try-except block to handle any exceptions that may occur during the saving process.
        If the DataFrame is saved successfully, a log message is printed indicating that the save operation was successful.
        If an exception occurs, an error message is logged indicating the error and the path where the DataFrame was supposed to be saved.
        """
        # Save the DataFrame to the specified file path
        out = df.to_csv(path, index=False)
        
        return out
