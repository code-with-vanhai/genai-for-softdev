import pandas as pd
import numpy as np

# Load weather data from a CSV file into a Pandas DataFrame
weather_df = pd.read_csv('april2024_station_data.csv')

# Convert relevant columns to NumPy arrays for faster numerical computations
wind_speed = weather_df['wind_speed'].to_numpy()  # Extract wind speed as a NumPy array
wind_direction = weather_df['wind_direction'].to_numpy()  # Extract wind direction as a NumPy array

# Convert wind direction from degrees to radians for mathematical calculations
wind_direction_rad = np.deg2rad(wind_direction)  # NumPy has a built-in function for this
