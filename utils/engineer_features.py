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
     
    def get_location_name_from_coordinates(self, lat, long):
        import pandas as pd

        # Get the unique values of the "Trip Origin" column
        unique_values = self.df['Trip Origin'].unique()

        print("The unique values in the 'Trip Origin' column are: ",len(unique_values))
        # Create an empty list to store the reverse geocoded values
        reverse_geocoded_values = []

        # Create a geocoder object
        geolocator = Photon(user_agent="measurements")

        # Iterate over each unique value and perform reverse geocoding
        i = 1
        for value in unique_values:
            location = geolocator.reverse(value)
            if location:
                reverse_geocoded_values.append(location.address)
                print(i, ". Address is :: ", location.address)
            else:
                reverse_geocoded_values.append(None)
                print(i, ". Address Not Found :: ", value)
            i = i + 1
        # Create a new column in the DataFrame with the reverse geocoded values
        self.df['Location Name'] = pd.Series(reverse_geocoded_values)