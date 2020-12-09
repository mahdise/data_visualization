import pandas as pd
import matplotlib.pyplot as plt


def hist_with_give_range(data, range=None):
    hist_plot = plt.hist(data["big data"],
                         facecolor="gold",
                         edgecolor="tomato",
                         bins=10,
                         range=(50, 70))
    # For save
    plt.savefig(
        r'C:\Users\Mahdi Islam\Documents\github_\data_visualization\data_visulazation_with_deffernt_plot_type\plot_view\range.png')

    # For show
    plt.show()


def hist_cumalitive_property(data):
    hist_plot = plt.hist(data["data mining"],
                         facecolor="tomato",
                         edgecolor="gold",
                         bins=10,
                         cumulative=True)
    # For save
    plt.savefig(
        r'C:\Users\Mahdi Islam\Documents\github_\data_visualization'
        r'\data_visulazation_with_deffernt_plot_type\plot_view\poperty.png')

    # For show
    plt.show()


def hist_combined_cumalitive_propertye_and_given_range(data):
    y = plt.hist(data["data mining"],
                 facecolor="tomato",
                 edgecolor="gold",
                 bins=10,
                 cumulative=True)

    y = plt.hist(data["big data"],
                 facecolor="gold",
                 edgecolor="tomato",
                 bins=10,
                 range=(10, 100))
    # For save
    plt.savefig(
        r'C:\Users\Mahdi Islam\Documents\github_\data_visualization'
        r'\data_visulazation_with_deffernt_plot_type\plot_view\combined.png')

    # For show
    plt.show()


if __name__ == '__main__':
    # read data
    data_frame = pd.read_csv(
        r"C:\Users\Mahdi Islam\Documents\github_\data_visualization"
        r"\data_visulazation_with_deffernt_plot_type\data_set.csv",
        skiprows=1)

    # plot for given range
    hist_with_give_range(data_frame)
    hist_cumalitive_property(data_frame)
    hist_combined_cumalitive_propertye_and_given_range(data_frame)
