import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def create_stack_plot(data):
    # Applying the rolling mean in 10 km steps (= 20 windows) on the accumulation data
    rmean1 = data['data science'].rolling(window=20, min_periods=1).mean()
    rmean2 = data['python'].rolling(window=20, min_periods=1).mean()
    rmean3 = data['machine learning'].rolling(window=20, min_periods=1).mean()

    # Defining the size of the figure [link](https://kite.com/python/examples/1875/matplotlib-change-the-figure-size)
    plt.figure(figsize=(12, 6))

    # Assign x-axis variable
    x = data['week']

    # a = (i.split('/')[-1] for i in df['week'])
    # x = [*a]

    # Assign y-axis variables
    y = np.vstack([rmean1, rmean2, rmean3])

    # Defining the labels
    labels = ['Data Science',
              'Python',
              'Machine Learning']

    # Defining the color
    colors = ['black',
              'red',
              'yellow']

    # Plot data as stackplot, with afore defined labels and color.
    # The color that seperates the different stacks is chosen to be 'white'

    plt.stackplot(x, y,
                  labels=labels,
                  colors=colors,
                  edgecolor='white')

    # Define x- and y-label
    plt.xlabel('Weeks')
    plt.ylabel('Search per week')

    # Add a legend and define its position using loc= 'a number between 0 and 11'
    plt.legend(loc=9)

    # Automatically arranges a tight layout of your graph
    plt.tight_layout()



    return plt


if __name__ == '__main__':
    # read data
    data_frame = pd.read_csv(
        r"C:\Users\Mahdi Islam\Documents\github_\data_visualization"
        r"\data_visulazation_with_deffernt_plot_type\data_set.csv",
        skiprows=1)

    # plot for pie chart

    result_plot = create_stack_plot(data_frame)
    #
    # # For save
    # result_plot.savefig(
    #     r'C:\Users\Mahdi Islam\Documents\github_\data_visualization'
    #     r'\data_visulazation_with_deffernt_plot_type\plot_view\line_plot_per_week.png')

    # For show
    result_plot.show()
