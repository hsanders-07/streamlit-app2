import plotly.express as px
import pandas as pd


def scatter_plot_on_off(df, option1, option2):
    fig = px.scatter(
        df,
        x=option1,
        y=option2,
        color_discrete_sequence=["red"],  # Ensures all points are red
        title=f"{option1} vs {option2} (Utah on Offense)",
        labels={option1: option1, option2: option2})
    return fig


def scatter_plot_on_def(df, option1, option2):
    fig = px.scatter(
        df,
        x=option1,
        y=option2,
        color_discrete_sequence=["red"],  # Ensures all points are red
        title=f"{option1} vs {option2} (Utah on Defense)",
        labels={option1: option1, option2: option2})
    return fig


def box_plot_on_off(df, option3):
    fig3 = px.box(df, y=df[option3], title=f"Box Plot of {option3} when Utah is on Offense", 
             color_discrete_sequence=["red"])
    return fig3


def box_plot_on_def(df, option3):
    fig4 = px.box(df, y=df[option3], title=f"Box Plot of {option3} when Utah is on Defense", 
             color_discrete_sequence=["white"])
    return fig4
    
