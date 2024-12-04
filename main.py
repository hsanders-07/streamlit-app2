import pandas as pd

import matplotlib.pyplot as plt
import requests

from my_plots import *
import streamlit as st


@st.cache_data
def load_utah_data():
    data = pd.read_csv('dataset.csv')
    return data

utah_data = load_utah_data()

st.title('Numbers Behind Perfection')

tab1, tab2 = st.tabs(["Utah on Offense", "Utah on Defense"])

with st.sidebar:
    option1 = st.selectbox(
    "First Variable",
    ("scoring", "elapsed", "plays", "start_yards_to_goal", "yards", "drive_result", "off_points_gained"),
)

    option2 = st.selectbox(
    "Second Variable",
    ("scoring", "elapsed", "plays", "start_yards_to_goal", "yards", "drive_result", "off_points_gained"),
)

with tab1:
    fig1 = scatter_plot_on_off(utah_data, option1, option2)
    st.plotly_chart(fig1)


with tab2:
    fig2 = scatter_plot_on_def(utah_data, option1, option2)
    st.plotly_chart(fig2)












    #n_names = st.radio('Number of names per sex', [3, 5, 10])
    #on = st.toggle("Activate features")