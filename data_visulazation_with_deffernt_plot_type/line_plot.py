import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


def create_line_plot(data):
    # In the following example, the distribution of data science and Big data gets displayed

    # replacing na values in college with No college
    data["week"].fillna(method='ffill', inplace=True)

    # Define the size of the whole figure (width/height)
    fig = plt.figure(figsize=(12, 6))

    # Define size and position of the large graph(ax1) and insert graph(ax2): [x-position,y-position,width]
    '''Try some different numbers and see what happens. Negative values are also possible, but stay in a small range,
    otherwise your plot gets too small!'''
    ax1 = fig.add_axes([0, 0, 1, 1])
    ax2 = fig.add_axes([0.45, 0.6, 0.5, 0.3])

    # Set a title
    ax1.set_title("Python and Big Data search per week")

    '''In my example, only the first 200 km (first 400 data points) shall be displayed in this graph.
    Therefore, the data is subsetted with iloc -> iloc[0:401]'''

    # Set attributes for large graph
    ax1.plot(data['week'].iloc[0:228],
             data['big data'].iloc[0:228],
             color="blue")  # set color
    ax1.set_xlabel("weeks")  # set x-label
    ax1.set_ylabel("search/week")  # set y-label

    # Set attributes for insert graph
    ax2.plot(data['week'].iloc[0:228],
             data['python'].iloc[0:228],
             color="lightblue")  # set color
    ax2.set_xlabel("week")  # set x-label
    ax2.set_ylabel("search/week")  # set y-label

    return plt


if __name__ == '__main__':
    # read data
    data_frame = pd.read_csv(
        r"C:\Users\Mahdi Islam\Documents\github_\data_visualization"
        r"\data_visulazation_with_deffernt_plot_type\data_set.csv",
        skiprows=1)

    # plot for pie chart

    result_plot = create_line_plot(data_frame)

    # For save
    result_plot.savefig(
        r'C:\Users\Mahdi Islam\Documents\github_\data_visualization'
        r'\data_visulazation_with_deffernt_plot_type\plot_view\line_plot_per_week.png')

    # For show
    result_plot.show()
