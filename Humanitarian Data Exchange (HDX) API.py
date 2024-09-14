#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
import pandas as pd

# Function to fetch data from HDX API
def fetch_hdx_data():
    # HDX API endpoint to fetch datasets
    url = 'https://data.humdata.org/api/3/action/package_search?q=disaster'

    # Make the request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

# Function to structure the HDX dataset data
def structure_hdx_data(data):
    # Initialize lists to store structured data
    titles = []
    ids = []
    descriptions = []
    urls = []
    updated_dates = []

    # Check if there are datasets in the data
    if 'result' not in data or len(data['result']['results']) == 0:
        print("No datasets found in the data.")
        return pd.DataFrame()  # Return an empty DataFrame if no datasets

    # Loop through each dataset and extract relevant fields
    for dataset in data['result']['results']:
        title = dataset.get('title', 'N/A')
        dataset_id = dataset.get('id', 'N/A')
        description = dataset.get('notes', 'No description available')
        url = f"https://data.humdata.org/dataset/{dataset_id}"
        updated_date = dataset.get('last_modified', 'No date available')

        # Append the data to lists
        titles.append(title)
        ids.append(dataset_id)
        descriptions.append(description)
        urls.append(url)
        updated_dates.append(updated_date)

    # Create a DataFrame using the structured lists
    df = pd.DataFrame({
        'Title': titles,
        'Dataset ID': ids,
        'Description': descriptions,
        'URL': urls,
        'Last Updated': updated_dates
    })

    return df

# Main script execution
if __name__ == "__main__":
    hdx_data = fetch_hdx_data()

    if hdx_data:
        # Structure the data into a DataFrame
        structured_data = structure_hdx_data(hdx_data)

        if not structured_data.empty:
            # Print the structured data
            print(structured_data.to_string(index=False))

            # Save the data to a CSV file
            structured_data.to_csv('hdx_data.csv', index=False)
            print("\nData has been saved to 'hdx_data.csv'")
        else:
            print("No structured data to display.")




# In[6]:


import pandas as pd

# Load the HDX disaster data from a CSV file
df = pd.read_csv('hdx_data.csv')

# Display the column names
print("Column Names:")
print(df.columns)


# In[7]:


import pandas as pd

# Load the HDX disaster data from a CSV file
df = pd.read_csv('hdx_data.csv')

# Display the column names
print("Column Names:")
print(df.columns)

# 1. Remove duplicate rows
df.drop_duplicates(inplace=True)

# 2. Handle missing values
# Check if 'Date' or its equivalent exists
if 'Date' in df.columns:
    df['Date'].fillna('No date available', inplace=True)
elif 'date' in df.columns:  # If the column is named 'date'
    df['date'].fillna('No date available', inplace=True)
else:
    print("No date column found.")

# 3. Standardize date formats
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
elif 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

# 4. Trim whitespace from string columns
df['Title'] = df['Title'].str.strip()
df['Description'] = df['Description'].str.strip()  # If you have a Description column
df['URL'] = df['URL'].str.strip()

# 5. Remove any unwanted characters (if necessary)
df['Title'] = df['Title'].str.replace(r'[^\w\s]', '', regex=True)

# 6. Reset index after cleaning
df.reset_index(drop=True, inplace=True)

# Display the cleaned DataFrame
print("\nCleaned Data:")
print(df.head())

# Save the cleaned data to a new CSV file
df.to_csv('cleaned_hdx_data.csv', index=False)
print("\nCleaned data has been saved to 'cleaned_hdx_data.csv'")


# In[ ]:




