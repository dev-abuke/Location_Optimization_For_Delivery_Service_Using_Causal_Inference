import pandas as pd
from meteostat import Point, Daily
from geopy.geocoders import Photon

class FeatureEngineer:
    def __init__(self, df):
        self.df = df
        self.df['Trip Start Time'] = pd.to_datetime(self.df['Trip Start Time'])
        self.df['Trip End Time'] = pd.to_datetime(self.df['Trip End Time'])
        self.df['Trip Duration'] = (self.df['Trip End Time'] - self.df['Trip Start Time']).dt.total_seconds() / 60
    
    def get_weather_data(self, weather_data):

        # Define location for Lagos, Nigeria
        lagos = Point(6.5244, 3.3792)

        # Define time range for the data
        start_date = self.df['Trip Start Time'].min().to_pydatetime()
        # decrease one day from the start date
        start_date = start_date - pd.Timedelta(days=1)
        end_date = self.df['Trip Start Time'].max().to_pydatetime()
        
        # Get daily weather data for Lagos
        weather_data = Daily(lagos, start_date, end_date)
        weather_data = weather_data.fetch()

        return weather_data
   