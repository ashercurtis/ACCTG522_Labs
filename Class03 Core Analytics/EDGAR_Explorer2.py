import json
import requests
import pandas as pd

# Set the CIK for Tesla and format it to be 10-digits long
cik = "1318605"
cik10 = f"{cik:0>10}"  # Format to 10 digits

# Set the URL for Tesla's filings using the SEC's EDGAR API
url = f"https://data.sec.gov/submissions/CIK{cik10}.json"

# Set the headers with user-agent for making requests to SEC
headers = {'User-Agent' : 'University Name your.email@university.edu'}

# Make a GET request to the SEC API
response = requests.get(url, headers=headers)

# Parse the JSON response data
data = response.json()

# Confirm that the JSON object is a dictionary
print(type(data))  # Should return <class 'dict'>

# Identify the keys in the top-level dictionary
print(data.keys())

# Confirm Tesla's CIK and name
print(data['cik'])
print(data['name'])

# Check the data types of each value in the dictionary
for k, v in data.items():
    print(k, type(v))

# Access the filings dictionary
data2 = data['filings']
for k, v in data2.items():
    print(k, type(v))

# Check the type of 'files' within 'filings'
print(type(data['filings']['files']))

# Print the files to see the content of the list
print(data['filings']['files'])

# Check the type of 'recent' within 'filings'
print(type(data['filings']['recent']))

# Explore the 'recent' dictionary
data2 = data['filings']['recent']
for k, v in data2.items():
    print(k, type(v))

# Check the type of the 'form' field within 'recent'
print(type(data['filings']['recent']['form']))

# Save the 'recent' filings as a pandas DataFrame
alldata = pd.DataFrame(data['filings']['recent'])

# Create a new DataFrame with just the 'form' field
data3 = pd.DataFrame(data['filings']['recent']['form'], columns=['form'])

# Filter out all 10-K filings
all10ks = alldata[alldata['form'] == '10-K']

# Output the filtered 10-K filings to a CSV file
all10ks.to_csv('tesla_10k_filings.csv', index=False)

# Confirm the file was created by printing a success message
print("10-K filings have been saved to 'tesla_10k_filings.csv'.")

# Identify the most recent filing, including its form, filing date, and timestamp
print(data2['form'][0])  # Most recent form
print(data2['filingDate'][0])  # Filing date of the most recent form
print(data2['acceptanceDateTime'][0])  # Timestamp of acceptance for the most recent form

# Identify the number of unique forms filed by the entity
uniqueFilings = pd.unique(data3['form'])
print(uniqueFilings)

# Count the number of unique filings
nUnique = len(uniqueFilings)
print(nUnique)

# Count how many times each form was filed and identify the most popular one
form_counts = data3['form'].value_counts()
print(form_counts)


