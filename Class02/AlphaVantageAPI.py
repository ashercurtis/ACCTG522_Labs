## Code to get monthly stock prices for a ticker of your choice using AlphaVantage's free API 

import requests
import json
import csv

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=AAPL&apikey=demo'
r = requests.get(url)
data = r.json()

print(data)

# Specify the CSV file name
csv_file = "financial_data.csv"

# Access the 'Monthly Time Series' part of the data
time_series = data['Monthly Time Series']

# Open a file to write
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
    
    # Iterate through the time series data and write to the CSV file
    for date, metrics in time_series.items():
        writer.writerow([date, metrics['1. open'], metrics['2. high'], metrics['3. low'], metrics['4. close'], metrics['5. volume']])

print(f"Data has been written to {csv_file}")