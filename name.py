import sys

names = ["dave","jpy","jake"]

name = input("name: ")

for n in names:
    if name.lower() == n:
        print("Found")
        sys.exit(0)

print("Not found")
sys.exit(1)
