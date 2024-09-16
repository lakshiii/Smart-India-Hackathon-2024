#!/usr/bin/env python
# coding: utf-8

# In[31]:


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


# In[2]:


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


# In[3]:


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




# In[4]:


import pandas as pd

# Load the HDX disaster data from a CSV file
df = pd.read_csv('hdx_data.csv')

# Display the column names
print("Column Names:")
print(df.columns)


# In[5]:


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


# In[6]:


import requests
import pandas as pd

# Function to fetch earthquake data from USGS Earthquake API
def fetch_usgs_earthquake_data():
    # USGS Earthquake API endpoint
    url = 'https://earthquake.usgs.gov/fdsnws/event/1/query'

    # Parameters for the API request
    params = {
        'format': 'geojson',      # Response format
        'starttime': '2023-09-01',  # Start date (YYYY-MM-DD)
        'endtime': '2023-09-30',    # End date (YYYY-MM-DD)
        'minmagnitude': 5.0         # Minimum magnitude for earthquakes
    }

    # Make the request to the API
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

# Function to structure the earthquake data
def structure_earthquake_data(data):
    # Initialize lists to store structured data
    event_ids = []
    magnitudes = []
    locations = []
    times = []
    depths = []

    # Check if there are features in the data
    if 'features' not in data or len(data['features']) == 0:
        print("No earthquakes found in the data.")
        return pd.DataFrame()  # Return an empty DataFrame if no earthquakes

    # Loop through each earthquake event and extract relevant fields
    for feature in data['features']:
        event_id = feature['id']
        magnitude = feature['properties']['mag']
        location = feature['properties']['place']
        time = feature['properties']['time']
        depth = feature['geometry']['coordinates'][2]

        # Append the data to lists
        event_ids.append(event_id)
        magnitudes.append(magnitude)
        locations.append(location)
        times.append(pd.to_datetime(time, unit='ms'))  # Convert to datetime
        depths.append(depth)

    # Create a DataFrame using the structured lists
    df = pd.DataFrame({
        'Event ID': event_ids,
        'Magnitude': magnitudes,
        'Location': locations,
        'Time': times,
        'Depth (km)': depths
    })

    return df

# Main script execution
if __name__ == "__main__":
    usgs_data = fetch_usgs_earthquake_data()
    
    if usgs_data:
        # Structure the data into a DataFrame
        structured_data = structure_earthquake_data(usgs_data)
        
        if not structured_data.empty:
            # Print the structured data
            print(structured_data.to_string(index=False))

            # Save the data to a CSV file
            structured_data.to_csv('usgs_earthquake_data.csv', index=False)
            print("\nData has been saved to 'usgs_earthquake_data.csv'")
        else:
            print("No structured data to display.")


# In[7]:


import pandas as pd

# Load the USGS earthquake data from a CSV file
df = pd.read_csv('usgs_earthquake_data.csv')

# Display the first few rows and the column names to inspect the structure
print("First few rows of the DataFrame:")
print(df.head())
print("\nColumn Names:")
print(df.columns)


# In[9]:


import requests
import pandas as pd

# Function to fetch natural event data from NASA EONET API
def fetch_nasa_eonet_data():
    # NASA EONET API endpoint
    url = 'https://eonet.gsfc.nasa.gov/api/v3/events'

    # Make the request to the API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

# Function to structure the event data
def structure_eonet_data(data):
    # Initialize lists to store structured data
    event_ids = []
    titles = []
    categories = []
    dates = []
    sources = []
    geometries = []

    # Check if there are events in the data
    if 'events' not in data or len(data['events']) == 0:
        print("No events found in the data.")
        return pd.DataFrame()  # Return an empty DataFrame if no events

    # Loop through each event and extract relevant fields
    for event in data['events']:
        event_id = event.get('id', 'N/A')
        title = event.get('title', 'N/A')
        
        # Get the category name
        category = event['categories'][0].get('title', 'Unknown') if event['categories'] else 'Unknown'
        
        # Get the date of the event
        date = event['geometry'][0].get('date', 'No date available') if event.get('geometry') else 'No date available'
        
        # Get the source URL
        source = event['sources'][0].get('url', 'No source available') if event.get('sources') else 'No source available'
        
        # Get the geometry (latitude and longitude)
        geometry = event['geometry'][0].get('coordinates', 'No coordinates available') if event.get('geometry') else 'No coordinates available'

        # Append the data to lists
        event_ids.append(event_id)
        titles.append(title)
        categories.append(category)
        dates.append(date)
        sources.append(source)
        geometries.append(geometry)

    # Create a DataFrame using the structured lists
    df = pd.DataFrame({
        'Event ID': event_ids,
        'Title': titles,
        'Category': categories,
        'Date': dates,
        'Source': sources,
        'Coordinates': geometries
    })

    return df

# Main script execution
if __name__ == "__main__":
    eonet_data = fetch_nasa_eonet_data()
    
    if eonet_data:
        # Structure the data into a DataFrame
        structured_data = structure_eonet_data(eonet_data)
        
        if not structured_data.empty:
            # Print the structured data
            print(structured_data.to_string(index=False))

            # Save the data to a CSV file
            structured_data.to_csv('nasa_eonet_data.csv', index=False)
            print("\nData has been saved to 'nasa_eonet_data.csv'")
        else:
            print("No structured data to display.")
  

   


# In[12]:


import requests
import pandas as pd

# Function to fetch natural event data from NASA EONET API
def fetch_nasa_eonet_data():
   # NASA EONET API endpoint
   url = 'https://eonet.gsfc.nasa.gov/api/v3/events'

   # Make the request to the API
   response = requests.get(url)
   
   # Check if the request was successful
   if response.status_code == 200:
       data = response.json()
       return data
   else:
       print(f"Failed to fetch data. Status code: {response.status_code}")
       return None

# Function to structure the event data
def structure_eonet_data(data):
   # Initialize lists to store structured data
   event_ids = []
   titles = []
   categories = []
   dates = []
   sources = []
   geometries = []

   # Check if there are events in the data
   if 'events' not in data or len(data['events']) == 0:
       print("No events found in the data.")
       return pd.DataFrame()  # Return an empty DataFrame if no events

   # Loop through each event and extract relevant fields
   for event in data['events']:
       event_id = event.get('id', 'N/A')
       title = event.get('title', 'N/A')
       
       # Get the category name
       category = event['categories'][0].get('title', 'Unknown') if event['categories'] else 'Unknown'
       
       # Get the date of the event
       date = event['geometry'][0].get('date', 'No date available') if event.get('geometry') else 'No date available'
       
       # Get the source URL
       source = event['sources'][0].get('url', 'No source available') if event.get('sources') else 'No source available'
       
       # Get the geometry (latitude and longitude)
       geometry = event['geometry'][0].get('coordinates', 'No coordinates available') if event.get('geometry') else 'No coordinates available'

       # Append the data to lists
       event_ids.append(event_id)
       titles.append(title)
       categories.append(category)
       dates.append(date)
       sources.append(source)
       geometries.append(geometry)

   # Create a DataFrame using the structured lists
   df = pd.DataFrame({
       'Event ID': event_ids,
       'Title': titles,
       'Category': categories,
       'Date': dates,
       'Source': sources,
       'Coordinates': geometries
   })

   return df

# Main script execution
if __name__ == "__main__":
   eonet_data = fetch_nasa_eonet_data()
   
   if eonet_data:
       # Structure the data into a DataFrame
       structured_data = structure_eonet_data(eonet_data)
       
       if not structured_data.empty:
           # Print the structured data
           print(structured_data.to_string(index=False))

           # Save the data to a CSV file
           structured_data.to_csv('nasa_eonet_data.csv', index=False)
           print("\nData has been saved to 'nasa_eonet_data.csv'")
       else:
           print("No structured data to display.")
 


# In[13]:


import pandas as pd

# Load the USGS earthquake data from a CSV file
df = pd.read_csv('nasa_eonet_data.csv')

# Display the first few rows and column names
print("First few rows of the DataFrame:")
print(df.head())
print("\nColumn Names:")
print(df.columns)

# 1. Remove duplicate rows
df.drop_duplicates(inplace=True)

# 2. Handle missing values
# Check for the 'time' column
if 'time' in df.columns:
    df['time'].fillna('No date available', inplace=True)
else:
    print("No 'time' column found.")

# 3. Standardize date formats
if 'time' in df.columns:
    df['time'] = pd.to_datetime(df['time'], unit='ms', errors='coerce')

# 4. Trim whitespace from string columns
# Update 'place' and 'url' to the correct column names based on your inspection
if 'place' in df.columns:
    df['place'] = df['place'].str.strip()  # Check if this column exists
else:
    print("No 'place' column found.")

if 'url' in df.columns:
    df['url'] = df['url'].str.strip()      # Check if this column exists
else:
    print("No 'url' column found.")

# 5. Remove any unwanted characters (if necessary)
if 'place' in df.columns:
    df['place'] = df['place'].str.replace(r'[^\w\s,]', '', regex=True)

# 6. Reset index after cleaning
df.reset_index(drop=True, inplace=True)

# Display the cleaned DataFrame
print("\nCleaned Data:")
print(df.head())

# Save the cleaned data to a new CSV file
df.to_csv('cleaned_usgs_earthquake_data.csv', index=False)
print("\nCleaned data has been saved to 'cleaned_usgs_earthquake_data.csv'")


# In[14]:


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


# In[15]:


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



# In[41]:


import requests
import pandas as pd

# Function to fetch data from ReliefWeb API
def fetch_reliefweb_data():
    url = 'https://api.reliefweb.int/v1/reports?appname=apidoc&query[value]=disaster'
    
    # Fetching the data
    response = requests.get(url)
    
    if response.status_code == 200:
        try:
            data = response.json()
            return data
        except ValueError:
            print("Error decoding JSON. The response might not be valid JSON.")
            return None
    else:
        print(f"Error fetching data from ReliefWeb: {response.status_code}")
        return None

# Function to categorize data by disaster type
def categorize_by_disaster_type(reports):
    disaster_categories = {}
    
    for report in reports:
        fields = report['fields']
        disaster_type = fields.get('disaster_type', [{}])[0].get('name', 'Unknown')
        
        # Extract relevant information for each report
        disaster_info = {
            'title': fields['title'],
            'date': fields.get('date', {}).get('created', 'N/A'),
            'country': fields.get('primary_country', {}).get('name', 'N/A'),
            'source': fields.get('source', [{}])[0].get('name', 'N/A'),
        }
        
        # Categorize by disaster type
        if disaster_type not in disaster_categories:
            disaster_categories[disaster_type] = []
        disaster_categories[disaster_type].append(disaster_info)
    
    return disaster_categories

# Fetch the ReliefWeb data
reliefweb_data = fetch_reliefweb_data()

# Check if data is fetched and proceed with categorization
if reliefweb_data and 'data' in reliefweb_data:
    reports = reliefweb_data['data']
    
    # Categorize the data by disaster type
    categorized_data = categorize_by_disaster_type(reports)
    
    # Display categorized data
    for disaster_type, details in categorized_data.items():
        print(f"\nDisaster Type: {disaster_type}")
        df = pd.DataFrame(details)
        print(df)
else:
    print("No valid data fetched.")

 



# In[ ]:


import requests
import pandas as pd

# Function to fetch data from NASA EONET API
def fetch_nasa_eonet_data():
    url = 'https://eonet.gsfc.nasa.gov/api/v3/events'
    
    # Fetching the data
    response = requests.get(url)
    
    if response.status_code == 200:
        try:
            data = response.json()
            print("Data fetched successfully.")
            return data
        except ValueError:
            print("Error decoding JSON. The response might not be valid JSON.")
            return None
    else:
        print(f"Error fetching data from NASA EONET API: {response.status_code}")
        return None

# Function to categorize data by disaster type
def categorize_by_disaster_type(events):
    disaster_categories = {}
    
    for event in events:
        # Adding debug print to check the event structure
        print(f"Event Data: {event}")
        
        # Get the disaster type from the categories field
        if event['categories']:
            disaster_type = event['categories'][0]['title']
        else:
            disaster_type = 'Unknown'
        
        # Extract relevant information for each event
        disaster_info = {
            'title': event['title'],
            'date': event['geometry'][0]['date'],
            'location': ', '.join([str(coord) for coord in event['geometry'][0]['coordinates']]),
            'source': 'NASA EONET',
        }
        
        # Categorize by disaster type
        if disaster_type not in disaster_categories:
            disaster_categories[disaster_type] = []
        disaster_categories[disaster_type].append(disaster_info)
    
    return disaster_categories

# Fetch the NASA EONET data
nasa_eonet_data = fetch_nasa_eonet_data()

# Check if data is fetched and proceed with categorization
if nasa_eonet_data and 'events' in nasa_eonet_data:
    print(f"Fetched events: {len(nasa_eonet_data['events'])}")
    
    events = nasa_eonet_data['events']
    
    # Categorize the data by disaster type
    categorized_data = categorize_by_disaster_type(events)
    
    # Display categorized data
    for disaster_type, details in categorized_data.items():
        print(f"\nDisaster Type: {disaster_type}")
        df = pd.DataFrame(details)
        print(df)
else:
    print("No valid data fetched.")





# In[ ]:






   


# In[ ]:




