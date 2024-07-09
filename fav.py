import csv

#prints the second column row[1] being programming language
with open("program_names.csv") as file:
    reader  = csv.DictReader(file)
    for row in reader:
        favor = row["language"]
        print(favor)

