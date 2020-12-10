import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def create_steam_plot(data):
    # Create a copy of your data set
    stem_data = data.copy()

    # Compare two data sets or variables using `diff()`
    stem_data[['big_data_comp', 'machine_learning_comp']] = data[['big data', 'machine learning']].diff()

    # replacing na values in college with No college
    data["week"].fillna(method='ffill', inplace=True)

    plt.figure(figsize=(15, 11))

    # Add a main title and define position(y=) and letter size(fontsize=)
    plt.suptitle('Search for Big Data and Machine Learning change from one week to another', y=1.03, fontsize=20)

    # Define the x-axis for both plots
    dist = data['week']

    # a = (i.split('/')[-1] for i in df['week'])
    # dist = [*a]

    # Create first subplot(position matrix)
    plt.subplot(311)
    plt.stem(dist,  # x-axis
             stem_data['big_data_comp'],  # y-axis first plot
             markerfmt='g_',  # Defining the format of the markers at x/y-position -> 'g_' = "green, flat line"
             linefmt='b--',  # Defining the format of the lines towards x/y-position -> 'b--' = "blue, dashed line"
             basefmt='r-')  # Defining the format of the bottom line (by default at position 0) -> 'r-' = "red, solid line"
    plt.title('Big Data search Change from week to week')

    plt.subplot(312)
    plt.stem(dist,  # x-axis
             stem_data['machine_learning_comp'],  # y-axis second plot
             markerfmt='g_',
             linefmt='b--',
             basefmt='r-')
    plt.title('Machine Learning search result Change from week to week')

    # Add a little text box inside the plot, by adding this function to the addressed plot
    plt.text(65, -110, 'Differences in data size between the years, due to the loss of measuring stakes',
             style='italic',
             bbox={'facecolor': 'azure', 'alpha': 0.5, 'pad': 10})  # Define th style of the box

    # Improves the layout to a tight version
    plt.tight_layout()


    return plt


if __name__ == '__main__':
    # read data
    data_frame = pd.read_csv(
        r"C:\Users\Mahdi Islam\Documents\github_\data_visualization"
        r"\data_visulazation_with_deffernt_plot_type\data_set.csv",
        skiprows=1)

    # plot for pie chart

    result_plot = create_steam_plot(data_frame)

    # For save
    result_plot.savefig(
        r'C:\Users\Mahdi Islam\Documents\github_\data_visualization'
        r'\data_visulazation_with_deffernt_plot_type\plot_view\steam_plot.png')

    # For show
    result_plot.show()
