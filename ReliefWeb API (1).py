#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install requests


# In[22]:


import requests
import json

# Example function to fetch disaster data from a ReliefWeb API
def fetch_disaster_data():
    # API Endpoint
    url = 'https://api.reliefweb.int/v1/reports'

    # Parameters to customize the request (e.g., limiting to disaster-related reports)
    params = {
        'appname': 'disaster-collector', # Your application name
        'filter[field]': 'disaster',    # Filter for disaster-related reports
        'fields[include][]': 'title',   # What data fields to include in the response
        'fields[include][]': 'date',    
        'fields[include][]': 'url',
        'limit': 10                     # Limit number of results
    }

    # Making a request to the API
    response = requests.get(url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

# Example usage of the function
if __name__ == "__main__":
    disaster_data = fetch_disaster_data()
    
    if disaster_data:
        # Print the titles of disaster reports fetched from the API
        for report in disaster_data['data']:
            title = report['fields']['title']
            
            # Check if the date field exists
            event_date = report['fields'].get('date', {}).get('created', 'No date available')
            
            url = report['fields'].get('url', 'No URL available')
            
            print(f"Title: {title}\nDate: {event_date}\nURL: {url}\n")


# In[23]:


import pandas as pd

# Sample data structure (replace this with your actual data)
data = {
    'title': [
        'UNICEF Myanmar Humanitarian Situation Report No. 6: 29 July to 28 September 2021',
        'UNICEF Democratic Republic of the Congo Humanitarian Situation Report No. 9 for October and November 2021',
        'Philippines USAID/BHA Response to Super Typhoon Rai (01/26/22)',
        # Add more titles as needed
    ],
    'date': [
        None,  # Simulating missing date
        '2021-10-01',  # Valid date
        None,  # Simulating missing date
    ],
    'url': [
        'https://reliefweb.int/node/3780021',
        'https://reliefweb.int/node/3830561',
        None,  # Simulating missing URL
    ]
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original Data:")
print(df)

# Data Cleaning Steps

# 1. Handle missing values
# Fill missing dates with a placeholder or drop them
df['date'].fillna('No date available', inplace=True)
df['url'].fillna('No URL available', inplace=True)

# 2. Trim whitespace from string columns
df['title'] = df['title'].str.strip()
df['url'] = df['url'].str.strip()

# 3. Drop duplicates if any
df.drop_duplicates(inplace=True)

# Display the cleaned DataFrame
print("\nCleaned Data:")
print(df)

# Optionally, save to CSV
df.to_csv('cleaned_disaster_data.csv', index=False)
print("\nData has been saved to 'cleaned_disaster_data.csv'.")



# In[ ]:





# In[ ]:



    



# In[ ]:





# In[ ]:






# In[ ]:




