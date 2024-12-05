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

    
