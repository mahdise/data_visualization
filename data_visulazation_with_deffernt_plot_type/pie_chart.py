import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


def create_pie_chart(data):

    # Calculating the frequency of individual density values
    freq_bigData = stats.itemfreq(data["big data"])

    # Calculations on frequency are transformed to DataFrame(df1)
    df1 = pd.DataFrame(freq_bigData, columns=['big data', 'Frequency'])

    # F = df1['Frequency'].iloc[0:37]
    F = df1['Frequency'].iloc[0:6]

    # Calculating percentage distribution (902 = number of rows)
    Frequency_bigData = F * 100 / 260

    # lables of my data column
    # labels ='53  search/week', '54 search/week','76 search/week', '78 search/week',
    # '79 search/week','81 search/week', '83 search/week','82 search/week','87 search/week',
    #  '84 search/week','89 search/week','86 search/week','90 search/week','85 search/week',
    # '77 search/week','73 search/week','74 search/week','72 search/week','75 search/week',
    # '71 search/week','80 search/week','60 search/week','55 search/week','92 search/week',
    # '91 search/week','70 search/week','62 search/week','93 search/week','57 search/week',
    # '97 search/week','98 search/week','96 search/week','88 search/week','95 search/week',
    # '67 search/week','100 search/week','68 search/week'
    labels = '53  search/week', '76 search/week', '81 search/week', '90 search/week', '60 search/week', '100 search/week'

    # Define the size of the slice
    sizes = Frequency_bigData

    # Defining that everything is plotted together.
    fig1, ax1 = plt.subplots()

    # print(len(labels),len(sizes))
    # #Filling the pie with Information
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.axis('equal')

    # Add a title
    plt.title("Six unique search values of Big Data ")

    return plt




if __name__ == '__main__':
    # read data
    data_frame = pd.read_csv(
        r"C:\Users\Mahdi Islam\Documents\github_\data_visualization"
        r"\data_visulazation_with_deffernt_plot_type\data_set.csv",
        skiprows=1)

    # plot for pie chart

    result_plot = create_pie_chart(data_frame)

    # For save
    result_plot.savefig(
        r'C:\Users\Mahdi Islam\Documents\github_\data_visualization'
        r'\data_visulazation_with_deffernt_plot_type\plot_view\pie_chart.png')

    # For show
    result_plot.show()
