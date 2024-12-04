
import matplotlib.pyplot as plt
import pandas as pd


def scatter_plot_on_off(df, option1, option2):
    plt.scatter(df[option1], df[option2], alpha=0.7, color='red')
    plt.xlabel(option1)
    plt.ylabel(option2)
    plt.title(f"{option1} vs {option2} (Utah on Offense)")


def scatter_plot_on_def(df, option1, option2):
    plt.scatter(df[option1], df[option2], alpha=0.7, color='red')
    plt.xlabel(option1)
    plt.ylabel(option2)
    plt.title(f"{option1} vs {option2} (Utah on Defense)")