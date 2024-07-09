import csv

#prints the second column row[1] being programming language
with open("program_names.csv") as file:
    reader  = csv.reader(file)
    for row in reader:
        print(row[1])

