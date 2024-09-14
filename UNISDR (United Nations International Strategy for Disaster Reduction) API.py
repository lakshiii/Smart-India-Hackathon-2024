#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import pandas as pd

# Function to fetch data from UNISDR API
def fetch_unisdr_data():
    # UNISDR API endpoint for disaster risk reduction data
    url = 'https://www.unisdr.org/we/inform/disaster-statistics'

    # Since the UNISDR API might not have a straightforward JSON endpoint, we simulate the process
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parsing the HTML or relevant content could be necessary depending on the endpoint
        return response.text
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

# Function to extract relevant data (simulation)
def extract_relevant_data(html_content):
    # This function should parse the HTML content and extract relevant information
    # For now, we'll simulate the structured data
    data = [
        {
            'Title': 'Global Platform for Disaster Risk Reduction',
            'Date': '2023-05-25',
            'Description': 'A global conference on disaster risk reduction.',
            'URL': 'https://www.unisdr.org/conference/2023',
        },
        {
            'Title': 'Disaster Risk Reduction Strategies',
            'Date': '2022-11-15',
            'Description': 'Reports on national disaster risk reduction strategies.',
            'URL': 'https://www.unisdr.org/reports/2022',
        },
    ]
    
    return data

# Function to structure the extracted data into a DataFrame
def structure_unisdr_data(data):
    # Create a DataFrame using the structured data
    df = pd.DataFrame(data)
    return df

# Main script execution
if __name__ == "__main__":
    unisdr_data = fetch_unisdr_data()

    if unisdr_data:
        # Extract relevant data (this is a simulation)
        structured_data = extract_relevant_data(unisdr_data)

        if structured_data:
            # Convert the list of dictionaries to a DataFrame
            df = structure_unisdr_data(structured_data)

            # Print the structured data
            print(df.to_string(index=False))

            # Save the data to a CSV file
            df.to_csv('unisdr_data.csv', index=False)
            print("\nData has been saved to 'unisdr_data.csv'")
        else:
            print("No structured data to display.")


# In[3]:


import pandas as pd

# Load the UNISDR disaster data from a CSV file
# Replace 'unisdr_data.csv' with your actual CSV file name
df = pd.read_csv('unisdr_data.csv')

# Display the first few rows of the original DataFrame
print("Original Data:")
print(df.head())

# 1. Remove duplicate rows
df.drop_duplicates(inplace=True)

# 2. Handle missing values
# Fill missing dates with a placeholder or drop them
df['Date'].fillna('No date available', inplace=True)

# Alternatively, you can drop rows with any missing values
# df.dropna(inplace=True)

# 3. Standardize date formats
# Convert 'Date' column to datetime format if applicable
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# 4. Trim whitespace from string columns
df['Title'] = df['Title'].str.strip()
df['Description'] = df['Description'].str.strip()  # If you have a Description column
df['URL'] = df['URL'].str.strip()

# 5. Remove any unwanted characters (if necessary)
# Example: removing any special characters from titles
df['Title'] = df['Title'].str.replace(r'[^\w\s]', '', regex=True)

# 6. Reset index after cleaning
df.reset_index(drop=True, inplace=True)

# Display the cleaned DataFrame
print("\nCleaned Data:")
print(df.head())

# Save the cleaned data to a new CSV file
df.to_csv('cleaned_unisdr_data.csv', index=False)
print("\nCleaned data has been saved to 'cleaned_unisdr_data.csv'")


# In[ ]:




