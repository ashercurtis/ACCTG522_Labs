import requests
import json
import os

# Define the user-agent as required by the SEC API
headers = {
    "User-Agent": "your-email@example.com"
}

# Function to get filings for a company based on CIK and save it as a JSON file
def get_and_save_company_filings(cik, filename="filings.json"):
    """
    Downloads the full filings data for a given company by CIK from the SEC API
    and saves the result as a JSON file.
    
    Parameters:
    cik: Central Index Key of the company.
    filename: Name of the file where the JSON data will be saved.
    
    Returns:
    None
    """
    # SEC EDGAR API endpoint for company submissions
    base_url = f"https://data.sec.gov/submissions/CIK{cik}.json"
    
    # Send request to SEC EDGAR API
    response = requests.get(base_url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        
        # Save JSON data to a file
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        
        print(f"Data successfully saved to {filename}")
    else:
        print(f"Failed to retrieve data: {response.status_code}")

# Example usage
if __name__ == "__main__":
    # Example CIK for Apple Inc.
    cik = "0000320193"  # CIKs are zero-padded, so leading zeros are important
    
    # Save the full filings data to a JSON file
    get_and_save_company_filings(cik, filename="apple_filings.json") #Needs to be updated
