import csv

#prints the second column row[1] being programming language
with open("program_names.csv") as file:
    reader  = csv.DictReader(file)
    PHP, Ruby, Python = 0, 0, 0
    for row in reader:
        favor = row["Language"]
        if favor == "Python":
            Python += 1
        elif favor == "PHP":
            PHP += 1
        elif favor == "Ruby":
            Ruby += 1

print(f"PHP:  {PHP}")
print(f"Python:  {Python}")
print(f"Ruby: {Ruby}")

