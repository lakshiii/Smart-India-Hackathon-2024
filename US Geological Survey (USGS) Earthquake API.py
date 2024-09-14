#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[3]:


import pandas as pd

# Load the USGS earthquake data from a CSV file
df = pd.read_csv('usgs_earthquake_data.csv')

# Display the first few rows and the column names to inspect the structure
print("First few rows of the DataFrame:")
print(df.head())
print("\nColumn Names:")
print(df.columns)


# In[ ]:




