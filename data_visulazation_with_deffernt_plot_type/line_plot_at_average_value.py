import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


def create_line_plot(data):
    # replacing na values in college with No college
    data["week"].fillna(method='ffill', inplace=True)

    # Define the size of the whole figure (width/height)
    fig = plt.figure(figsize=(20, 8))

    # Add a title
    plt.suptitle(
        "Search per week by keywords of Big Data, Data science, Python and Artificial Intelligence, Machine Learning",
        fontsize=18)

    # Create plot ax1 = "bigdata"
    ax1 = fig.add_subplot(221)  # position of individual subplot (Matrix = 111)
    ax1.set_title("Data Science")  # Title of subplot
    ax1.plot(data['week'],
             data['data science'],
             color="cornflowerblue")  # choose individual colors
    plt.axhline(y=data['data science'].mean(), linewidth=2, color='m')  # Insert horizontal line

    # Create plot ax2 = "2005"
    ax2 = fig.add_subplot(222)
    ax2.set_title("Big Data")
    ax2.plot(data['week'],
             data['big data'],
             color="cornflowerblue")
    plt.axhline(y=data['big data'].mean(), linewidth=2, color='m')

    # Create plot ax3 = "2006"
    ax3 = fig.add_subplot(223)
    ax3.set_title("Artificial Intelligence")
    ax3.plot(data['week'],
             data['artificial intelligence'],
             color="cornflowerblue")
    plt.axhline(y=data['artificial intelligence'].mean(), linewidth=2, color='m')

    # Create plot ax4 = "2007"
    ax4 = fig.add_subplot(224)
    ax4.set_title("2007")
    ax4.plot(data['week'],
             data['machine learning'],
             color="cornflowerblue")
    plt.axhline(y=0, linewidth=2, color='m')  # I like to draw a line at 0 position only for this graph

    plt.setxlabel = "search/week"

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
        r'\data_visulazation_with_deffernt_plot_type\plot_view\line_plot_average_value.png')

    # For show
    result_plot.show()
