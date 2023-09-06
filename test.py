import csv

import os

csvpath= os.path.join('budget_data.csv')

with open(csvpath) as csvfile:
    csvreader= csv.reader(csvfile, delimiter= ',')
    print(csvreader)
    csv_header= next(csvreader)
    for r in csvreader:
        print(r)
