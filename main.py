import pandas as pd
from my_plots import *
import streamlit as st
from plotly.subplots import make_subplots

@st.cache_data
def load_utah_data():
    data = pd.read_csv('dataset.csv')
    return data

utah_data = load_utah_data()

st.title('Numbers Behind Perfection')

tab1, tab2, tab3 = st.tabs(["Utah on Offense", "Utah on Defense", "Compare"])

with st.sidebar:
    option1 = st.selectbox(
    "First Variable for Scatterplot",
    ("scoring", "elapsed", "plays", "start_yards_to_goal", "yards", "off_points_gained"),
)

    option2 = st.selectbox(
    "Second Variable for Scatterplot",
    ("scoring", "elapsed", "plays", "start_yards_to_goal", "yards", "off_points_gained"),
)

with tab1:
    utah_off_data = utah_data[utah_data['offense'] == 'Utah'].select_dtypes(include=['number'])

    fig1 = scatter_plot_on_off(utah_off_data, option1, option2)
    st.plotly_chart(fig1)



with tab2:
    utah_def_data = utah_data[utah_data['defense'] == 'Utah'].select_dtypes(include=['number'])
    fig2 = scatter_plot_on_def(utah_def_data, option1, option2)
    st.plotly_chart(fig2)


with tab3:
     options = ["elapsed", "plays", "start_yards_to_goal", "yards", "off_points_gained"]
     selection = st.pills("Variables", options, selection_mode="single", default='elapsed')

     utah_off_data2 = utah_data[utah_data['offense'] == 'Utah'][['offense', 'defense', selection]]
     utah_off_data2['Type'] = 'Offense'  # Add a column indicating offense

     utah_def_data2 = utah_data[utah_data['defense'] == 'Utah'][['offense', 'defense', selection]]
     utah_def_data2['Type'] = 'Defense'  # Add a column indicating defense


     # Combine the data
     combined_data = pd.concat([utah_off_data2, utah_def_data2])

# Create the box plot with 'Type' as the category
     fig3 = px.box(combined_data, x='Type', y=selection, color='Type', 
             title=f"Box Plot of {selection}: Utah on Offense vs Utah on Defense",
             color_discrete_sequence=["red", "white"])  # Customize colors for offense and defense

# Show the plot
     st.plotly_chart(fig3)
