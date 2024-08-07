import csv

#prints the second column row[1] being programming language
with open("program_names.csv") as file:
    reader  = csv.DictReader(file)
    php, ruby, python = 0, 0, 0,
    for row in reader:
        favor = row["Language"].strip().lower()
        if favor == "python":
            python += 1
        elif favor == "php":
            php += 1
        elif favor == "ruby":
            ruby += 1

print(f"php:  {php}")
print(f"python:  {python}")
print(f"ruby: {ruby}")

