import csv

with open('contacts.csv', "rt") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        print(', '.join(row))
