import pandas as pd
import matplotlib.pyplot as plt
from pvlib.location import Location

def fetch_sunlight_hours(latitude, longitude, year):
    
    # Generate hourly timestamps for the full year
    times = pd.date_range(start=f"{year}-01-01", end=f"{year}-12-31", freq='h', tz='UTC')

    # Get clearsky data
    location = Location(latitude, longitude)
    clearsky = location.get_clearsky(times)

    # Define sunlight hours where GHI > 120 
    sunlight_hours = clearsky['ghi'] > 120

    # Resample to get monthly total sunlight hours
    monthly_sunlight_hours = sunlight_hours.resample('ME').sum()

    # Compute daily average sunlight hours
    days_in_month = monthly_sunlight_hours.index.days_in_month
    daily_avg_sunlight_hours = monthly_sunlight_hours / days_in_month

    # Total yearly sunlight hours
    yearly_sunlight_hours = sunlight_hours.sum()

    return monthly_sunlight_hours, daily_avg_sunlight_hours, yearly_sunlight_hours

def plot_sunlight_hours(monthly_sunlight_hours):
   
    plt.figure(figsize=(10, 6))
    plt.bar(monthly_sunlight_hours.index.strftime('%B'), monthly_sunlight_hours, color='goldenrod')
    plt.xlabel("Month")
    plt.ylabel("Sunlight Hours")
    plt.title("Monthly Sunlight Hours in 2024 (GHI > 120 W/m²)")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Set location
latitude = 52.5204
longitude = 13.4050
year = 2024

# Get sunlight hour calculations
monthly_sunlight_hours, daily_avg_sunlight_hours, yearly_sunlight_hours = fetch_sunlight_hours(latitude, longitude, year)

# Print results
print("\nMonthly Sunlight Hours (hours per month):\n", monthly_sunlight_hours)
print("\nDaily Average Sunlight Hours (hours per day):\n", daily_avg_sunlight_hours)
print(f"\nTotal Sunlight Hours in {year}: {yearly_sunlight_hours:.2f} hours")

# Plot the monthly sunlight hours
plot_sunlight_hours(monthly_sunlight_hours)
