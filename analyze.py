import csv

def analyze():
    with open('AMZN.csv', 'r') as file:
        csvreader = csv.read_csv(file)
        print(csvreader)