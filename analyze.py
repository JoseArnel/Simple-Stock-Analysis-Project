import csv
import pandas as pd
from matplotlib import pyplot as plt



def analyze():
    with open('AMZN.csv', newline='') as file:
        csvreader = pd.read_csv(file)
        ma = 0
        for i, row in csvreader.iterrows():
            print(i[0], row['AdjClose'])


# def analyze1():
#     with open('analyze.csv', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(["MovingAverage"])
#         with open('AMZN.csv', newline='') as file1:
#             ma = 0
#             csvreader = csv.DictReader(file1):
#             for row in csvreader:
#                 ma += row
#

# def read():
#     data = pd.read_csv('AMZN.csv')
#     plt.plot(data.AdjClose/100)
#     plt.show()

analyze()
