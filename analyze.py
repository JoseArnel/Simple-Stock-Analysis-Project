import csv
import pandas as pd
from matplotlib import pyplot as plt

# TO-DO
# How to sum a row in Pandas
# indicies i, i+4

# PSUEDO
# learn to interate in Pandas


def analyze():
    df = pd.read_csv('DataSets/AMZN.csv', skipinitialspace=True)
    print(df.AdjClose)

    # with open('DataSets/AMZN.csv', newline='') as file:
    #     read = csv.reader(file)
    #     for row in read()sta
    #         print(row[0])

# Simple sum
def sum():
    with open('DataSets/AMZN.csv') as file:
        headerline = next(file)
        ma = 0
        for row in csv.reader(file):
            ma += int(float(row[1]))
        print(ma)   

# def read():
#     data = pd.read_csv('AMZN.csv')
#     plt.plot(data.AdjClose/100)
#     plt.show()

analyze()

#123456
