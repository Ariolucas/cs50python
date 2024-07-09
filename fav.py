import csv

with open("fav.csv") as file:
    reader  = csv.reader(file)
    for row in reader:
        print(row[1])

