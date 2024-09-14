#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install requests


# In[7]:


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
 

  



# In[9]:


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


# In[ ]:




