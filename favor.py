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
def get_value(Language):
    return counts[Language]

for favor in sorted(counts, key=lambda Language: counts[Language], reverse=True):
    print(f"{favor}: {counts[favor]}")
