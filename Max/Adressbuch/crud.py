import csv
import os

path = "contacts.csv"


def read():
    with open(path, "r", encoding="utf8") as file:
        csv_reader = csv.DictReader(file)
        list_of_dicts = []
        for line in csv_reader:
            list_of_dicts.append(line)
        return list_of_dicts


def write(list_of_dicts):
    with open(path, "w", encoding="utf8") as new_file:
        fieldnames = ["Anrede", "Name", "Vorname", "Straße", "Hausnummer", "PLZ", "Stadt", "Telefon 1", "Telefon 2" "Email"]
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=",")
        csv_writer.writeheader()
        for line in list_of_dicts:
            csv_writer.writerow(line)


def open_file():
    os.system("open " + path)
