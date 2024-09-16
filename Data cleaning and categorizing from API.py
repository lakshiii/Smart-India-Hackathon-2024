#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
df = pd.read_csv('D:/Disaster.csv')
df








   



# In[22]:


import os
print(os.getcwd()) 




# In[26]:


import pandas as pd

# Load the dataset (make sure the path is correct)
df = pd.read_csv('D:/Disaster.csv')

# Initial dataset overview
print("Initial Dataset:")
print(df.head())

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Handle missing values by dropping rows with any NaN values
df.dropna(inplace=True)

# Reset index after cleaning
df.reset_index(drop=True, inplace=True)

# Save the cleaned dataset to a new CSV file
df.to_csv('D:/Disaster.csv', index=False)

# Print dataset info after cleaning
print("Cleaned Dataset:")
df.info()


# In[27]:


df = pd.read_csv('D:/Disaster.csv')
df


# In[30]:


import pandas as pd

# Load the dataset
df = pd.read_csv('D:/Disaster.csv')

# Define categories for different disaster types based on the 'incident_type' column
disaster_categories = {
    'Natural': ['Severe Storm', 'Flood', 'Hurricane', 'Tornado', 'Wildfire', 'Earthquake', 'Volcano', 'Drought'],
    'Technological': ['Chemical Spill', 'Nuclear', 'Transportation Accident'],
    'Biological': ['Pandemic', 'Disease Outbreak'],
    'Other': ['Terrorism', 'Civil Unrest', 'Cyber Attack']
}

# Function to categorize each disaster
def categorize_disaster(incident_type):
    for category, types in disaster_categories.items():
        if incident_type in types:
            return category
    return 'Unknown'

# Apply the categorization function to the 'incident_type' column
df['disaster_category'] = df['incident_type'].apply(categorize_disaster)

# Save the updated dataset with the disaster categories
df.to_csv('D:/Disaster.csv', index=False)

# Display the first few rows of the categorized dataset
df.head()



# In[31]:


import pandas as pd

# Load the dataset
df = pd.read_csv('D:/Disaster.csv')

# Filter the data to include only rows where 'incident_type' is 'Flood'
df_flood = df[df['incident_type'] == 'Flood']

# Save the filtered dataset to a new CSV file
df_flood.to_csv('D:/Disaster.csv', index=False)

# Display the first few rows of the flood-only dataset
df_flood.head()


# In[34]:


import pandas as pd

# Load the dataset
df = pd.read_csv('D:/Disaster.csv')

# Filter the data to include only rows where 'incident_type' is 'Flood'
df_flood = df[df['incident_type'] == 'Earthquake']

# Save the filtered dataset to a new CSV file
df_flood.to_csv('D:/Disaster.csv', index=False)

# Display the first few rows of the flood-only dataset
df_flood.head()


# In[ ]:







# In[ ]:





# In[ ]:




