import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def create_box_plot(data):
    # To avoid problems with 'NaN's you can filter your data for missing values, while assigning the objects
    plt.figure(figsize=(16, 6))

    value1 = data["artificial intelligence"]
    accu1 = value1[~np.isnan(value1)]

    value2 = data["python"]
    accu2 = value2[~np.isnan(value2)]

    value3 = data["machine learning"]
    accu3 = value3[~np.isnan(value3)]

    value4 = data["big data"]
    accu4 = value4[~np.isnan(value4)]

    # Assigning the boxplot data
    plot_data = [accu1, accu2, accu3, accu4]

    # Defining the colors
    colors = ['red', 'yellow', 'blue', 'black']

    bp = plt.boxplot(plot_data,
                     patch_artist=True,
                     notch=True)
    for i in range(len(bp['boxes'])):
        bp['boxes'][i].set(facecolor=colors[i])
        bp['caps'][2 * i + 1].set(color=colors[i])

    plt.xticks([1, 2, 3, 4], ['Artificial intelligence', 'Python', 'Machine Learning', 'Big Data'])

    return plt, plot_data


def create_violin_plot(data):
    colors = ['red', 'yellow', 'blue', 'black']

    # Plotting the distribution of Artificial Intelligence, Python and Machine Learning values from weeks to weeks
    plt.figure(figsize=(20, 6))
    vp = plt.violinplot(plot_data,
                        showmedians=True)
    plt.xticks([1, 2, 3, 4], ['Artificial intelligence', 'Python', 'Machine Mearning', 'Big Data'])

    for i in range(len(vp['bodies'])):
        vp['bodies'][i].set(facecolor=colors[i])

    return plt


if __name__ == '__main__':
    # read data
    data_frame = pd.read_csv(
        r"C:\Users\Mahdi Islam\Documents\github_\data_visualization"
        r"\data_visulazation_with_deffernt_plot_type\data_set.csv",
        skiprows=1)

    # plot for pie chart

    result_plot, plot_data = create_box_plot(data_frame)

    # For save box
    result_plot.savefig(
        r'C:\Users\Mahdi Islam\Documents\github_\data_visualization'
        r'\data_visulazation_with_deffernt_plot_type\plot_view\box_plot_with_different_attributes.png')

    # For show box
    result_plot.show()

    result_violin_plot = create_violin_plot(plot_data)

    # For save violin
    result_violin_plot.savefig(
        r'C:\Users\Mahdi Islam\Documents\github_\data_visualization'
        r'\data_visulazation_with_deffernt_plot_type\plot_view\violin_with_different_attributes.png')

    # For show violin
    result_violin_plot.show()
