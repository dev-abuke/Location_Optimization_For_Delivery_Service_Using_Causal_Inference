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
    