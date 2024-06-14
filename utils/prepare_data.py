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
    
    def convert_to_datetime(self, df: pd.DataFrame,
                            columns: list) -> pd.DataFrame:
        """
        This method converts specified columns in a DataFrame to the datetime
        data type. It takes in two parameters:
        
        - df: The DataFrame containing the columns to be converted.
        - columns: A list of column names in the DataFrame that should be
          converted to the datetime data type.
        
        It returns the modified DataFrame with the specified columns converted
        to the datetime data type. If an error occurs during the conversion,
        the error message is printed to the console.
        """
        try:
            # Iterate over each column in the specified list
            for col in columns:
                # Convert the column to the datetime data type using the
                # pd.to_datetime function. If an error occurs during the
                # conversion, the error message is raised.
                df[col] = pd.to_datetime(df[col], errors='raise')
                # Print a message indicating that the conversion was
                # successful for the current column.
                print(f'feature: {col} successfully changed to datetime')
        except Exception as e:
            # If an error occurs during the conversion, print the error
            # message to the console.
            print(e)
        finally:
            # Return the modified DataFrame with the specified columns
            # converted to the datetime data type.
            return df
    def drop_features(self, df: pd.DataFrame, cols: list,
                             use_reg_ex: bool = False) -> pd.DataFrame:
        """
        This method removes specified columns from a DataFrame.

        Parameters:
        - df: The DataFrame from which to remove the specified columns.
        - cols: A list of column names to be removed from the DataFrame.
        - use_reg_ex: A boolean indicating whether the column names in 'cols'
          should be interpreted as regular expressions. Default is False.

        Returns:
        - df: The DataFrame with the specified columns removed.

        This method iterates over each column name in 'cols' and performs the
        following steps:
        1. If 'use_reg_ex' is True, it uses the 'filter' method of the DataFrame
           to find all columns that match the regular expression in the current
           column name. It then converts the resulting Series to a list and
           removes those columns from the DataFrame.
        2. If 'use_reg_ex' is False, it removes the current column from the
           DataFrame.
        3. It prints a message indicating that the column was successfully
           removed.

        If any error occurs during the removal process, it prints the error
        message to the console.

        Finally, it returns the modified DataFrame.
        """
        try:
            if use_reg_ex:
                # Iterate over each column name in cols
                for col in cols:
                    # Use the filter method to find all columns that match the
                    # regular expression in the current column name
                    regex_cols = df.filter(regex=col).columns.tolist()
                    # Convert the resulting Series to a list
                    regex_cols = list(regex_cols)
                    # Remove the identified columns from the DataFrame
                    df = df[df.columns.drop(regex_cols)]
                    # Print a message indicating that the column was removed
                    print(f'feature: {col} removed successfully')
            else:
                # Iterate over each column name in cols
                for col in cols:
                    # Remove the current column from the DataFrame
                    df = df.drop(columns=[col])
                    # Print a message indicating that the column was removed
                    print(f'feature: {col} removed successfully')
        except Exception as e:
            # If an error occurs during the removal process, print the error
            # message to the console
            print(e)
        finally:
            # Return the modified DataFrame
            return df
    def haversine_distance(self, lat1, lon1, lat2, lon2):
        # Convert latitude and longitude from degrees to radians
        lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
        
        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
        r = 6371  # Radius of Earth in kilometers
        return c * r