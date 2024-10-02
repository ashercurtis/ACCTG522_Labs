import csv

# Open the CSV file
with open('ACCTG522_Labs/Class01/appl_tsla.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    
    # Read the first row (headers)
    headers = next(reader)
    
    # Print the headers as a list
    #print(headers)

import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('ACCTG522_Labs/Class01/appl_tsla.csv')

# Check if relevant columns exist
if 'NetIncomeLoss_USD' in df.columns and 'Revenues_USD' in df.columns:
    # Calculate Profit Margin
    df['ProfitMargin'] = (df['NetIncomeLoss_USD'] / df['Revenues_USD']) * 100

    # Display Profit Margin
    print("Profit Margin Calculated:")
    print(df[['NetIncomeLoss_USD', 'Revenues_USD', 'ProfitMargin']].head())

# Assuming 'TotalAssets_USD' is a column in your dataset
if 'Revenues_USD' in df.columns and 'TotalAssets_USD' in df.columns:
    # Calculate Asset Turnover
    df['AssetTurnover'] = df['Revenues_USD'] / df['TotalAssets_USD']

    # Display Asset Turnover
    print("Asset Turnover Calculated:")
    print(df[['Revenues_USD', 'TotalAssets_USD', 'AssetTurnover']].head())
