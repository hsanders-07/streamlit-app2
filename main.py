import pandas as pd
#import zipfile
#import plotly.express as px
import matplotlib.pyplot as plt
import requests
#from io import BytesIO
#import plotly.graph_objects as go
#from plotly.subplots import make_subplots
from my_plots import *
import streamlit as st


@st.cache_data
def load_utah_data():
#     url = "https://api.collegefootballdata.com/drives?seasonType=regular&year=2008&team=Utah"

#     with open('cfb_apikey.txt', 'r') as file:
#         apikey = f"Bearer {file.read()}"

#     headers = {
#     "Authorization": apikey,
#     "Content-Type": "application/json"}

#     r = requests.get(url, headers=headers)

#     my_dict = r.json()
#     df = pd.DataFrame(my_dict)
#     columns_wanted = ['offense', 'defense', 'scoring', 'elapsed', 'plays', 'start_yards_to_goal', 'yards', 'drive_result']

#     df_to_use = df[columns_wanted].copy()
# # Filter out rows with specific values in 'drive_result due to misleading data'
#     df_to_use= df_to_use[~df_to_use['drive_result'].isin(['INT RETURN TOUCH', 'FUMBLE RETURN TD', 'Uncategorized'])]


# # Create the 'points' column in the copied DataFrame
#     df_to_use['off_points_gained'] = df_to_use['drive_result'].apply(lambda x: -2 if 'SF' in x 
#                                                       else 3 if 'GOOD' in x 
#                                                       else 6 if 'TD' in x
#                                                       else 0)
# # Replace True/False with Binary response (1 = True, 0 = False)
#     df_to_use['scoring'] = df_to_use['scoring'].astype(int)
# # Convert 'elapsed' column to decimal minutes
#     df_to_use['elapsed'] = df_to_use['elapsed'].apply(lambda x: x['minutes'] + x['seconds'] / 60)
#     return df_to_use

    data = pd.read_csv('dataset.csv')
    return data

st.title('Numbers Behind Perfection')

tab1, tab2 = st.tabs(["Utah on Offense", "Utah on Defense"])

with st.sidebar:
    




    input_name = st.text_input('Enter a name: ')
    year_input = st.slider("Year", min_value= 1880, max_value= 2023, value= 2000)
    n_names = st.radio('Number of names per sex', [3, 5, 10])
    on = st.toggle("Activate features")