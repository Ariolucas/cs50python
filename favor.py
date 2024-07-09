import csv

#prints the second column row[1] being programming language
with open("program_names.csv") as file:
    reader  = csv.DictReader(file)
    counts = {}
    php, ruby, python = 0, 0, 0,
    for row in reader:
        favor = row["Language"].strip().lower()
        if favor in counts:
            counts[favor] += 1
        else:
            counts[favor] = 1

for favor in counts:
    print(f"{favor}: {counts[favor]}")
