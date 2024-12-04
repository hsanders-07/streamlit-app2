import pandas as pd
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
    ("scoring", "elapsed", "plays", "start_yards_to_goal", "yards", "off_points_gained"),
)

    option2 = st.selectbox(
    "Second Variable",
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












    #n_names = st.radio('Number of names per sex', [3, 5, 10])
    #on = st.toggle("Activate features")