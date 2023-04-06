import csv

def analyze():
    with open('AMZN.csv', newline='') as file:
        csvreader = csv.DictReader(file)
        for row in csvreader:
            print(row['Adj Close'])

analyze()
