import csv
with open("csv1.csv",newline='')as csvfile:
    d=csv.reader(csvfile)
    for row in d:
        print(''.join(row))