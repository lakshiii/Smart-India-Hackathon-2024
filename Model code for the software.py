#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install dash plotly pandas


# In[5]:


import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import datetime

# Load the disaster dataset
data = pd.read_csv('D:/Disaster.csv')

# Data processing
data['declaration_date'] = pd.to_datetime(data['declaration_date'])
data['year'] = data['declaration_date'].dt.year
data['state'] = data['state'].str.upper()

# Disaster type counts
disaster_type_counts = data.groupby('incident_type').size().reset_index(name='type_count')

# Dash app
app = dash.Dash(__name__)

app.layout = html.Div(style={'font-family': 'Arial'}, children=[
    # Header
    html.Div([
        html.H1("Disaster Dashboard", style={'text-align': 'center', 'color': '#1E3D59'}),
        html.H3(f"{datetime.datetime.now().strftime('%A, %d %B %Y, %H:%M:%S')}", 
                style={'text-align': 'center', 'color': '#4A4A4A'})
    ], style={'padding': '20px', 'background-color': '#f1f1f1'}),

    # First row (Summary cards)
    html.Div([
        html.Div([
            html.H4("Total Disasters"),
            html.P(f"{len(data)}")
        ], style={'background-color': '#ffdd57', 'padding': '20px', 'width': '15%', 'display': 'inline-block'}),
        html.Div([
            html.H4("IA Program Declared"),
            html.P(f"{data['ia_program_declared'].sum()}")
        ], style={'background-color': '#77dd77', 'padding': '20px', 'width': '15%', 'display': 'inline-block'}),
        html.Div([
            html.H4("PA Program Declared"),
            html.P(f"{data['pa_program_declared'].sum()}")
        ], style={'background-color': '#ff6961', 'padding': '20px', 'width': '15%', 'display': 'inline-block'}),
        html.Div([
            html.H4("HM Program Declared"),
            html.P(f"{data['hm_program_declared'].sum()}")
        ], style={'background-color': '#84b6f4', 'padding': '20px', 'width': '15%', 'display': 'inline-block'}),
    ], style={'display': 'flex', 'justify-content': 'space-around', 'padding': '20px'}),

    # Row 2 (Graphs)
    html.Div([
        html.Div([
            dcc.Graph(
                id='disaster-types-pie',
                figure=px.pie(disaster_type_counts, names='incident_type', values='type_count',
                              title='Disaster Types Distribution', hole=0.4)
            )
        ], style={'width': '45%', 'display': 'inline-block'}),
        
        html.Div([
            dcc.Graph(
                id='disasters-by-state',
                figure=px.choropleth(data, locations='state', locationmode='USA-states', color='incident_type',
                                     title="Disasters by State", scope="usa")
            )
        ], style={'width': '45%', 'display': 'inline-block'}),
    ], style={'padding': '20px', 'display': 'flex', 'justify-content': 'space-around'}),

    # Row 3 (Live update / table)
    html.Div([
        html.Div([
            html.H4("Recent Disasters"),
            html.Table([
                html.Thead(
                    html.Tr([html.Th(col) for col in ['Date', 'State', 'Incident Type']])
                ),
                html.Tbody([
                    html.Tr([
                        html.Td(row['declaration_date'].date()), 
                        html.Td(row['state']), 
                        html.Td(row['incident_type'])
                    ]) for _, row in data.tail(10).iterrows()
                ])
            ], style={'width': '100%', 'text-align': 'center', 'border': '1px solid #ddd'})
        ], style={'width': '45%', 'padding': '20px', 'background-color': '#e6e6e6'}),
        
        html.Div([
            dcc.Graph(
                id='yearly-disasters',
                figure=px.line(data.groupby('year').size().reset_index(name='disaster_count'), 
                               x='year', y='disaster_count', title="Disasters per Year")
            )
        ], style={'width': '45%', 'padding': '20px'}),
    ], style={'display': 'flex', 'justify-content': 'space-around'}),
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True, port=8060)

     



# In[ ]:




