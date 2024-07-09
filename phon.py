import csv

file = open("phone.csv", "a")

name = input("name: ")
number = int(input("Number: "))

writer = csv.Dictwriter(file, fieldnames = ["name", "number"])
writer.writerow({"name ": name, "number ": number})

file.close()
