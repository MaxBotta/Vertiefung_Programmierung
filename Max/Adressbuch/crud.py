import csv
import json
import os


# Diese Methode kann JSON und CSV Dateien lesen und als Liste zurückgeben.
def read(path, type):
    try:
        list_of_dicts = []
        if type == "csv":
            with open(path, "r", newline='', encoding="utf8") as file:
                reader = csv.DictReader(file)
                for v in reader:
                    list_of_dicts.append(v)
                return list_of_dicts
        elif type == "json":
            with open(path) as file:
                list_of_dicts = json.load(file)
                return list_of_dicts
    except IOError:
        print('An error occured trying to read the file.')


def write(path, list_of_dicts):
    try:
        with open(path, "w", newline='', encoding="utf8") as file:
            fieldnames=['Anrede', 'Name', 'Vorname', 'Straße', 'Hausnummer', 'PLZ', 'Stadt', 'Telefon', 'Mobil', 'Email']
            writer = csv.DictWriter(file, fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(list_of_dicts)

    except IOError:
        print('An error occured trying to write the file.')


def open_file(path):
    os.system("open " + path)


def get_all_csv_and_json():
    # Liste mit sämtlichen Dateien ertsellen, die sich im selben Ordner befinden.
    dir_list = os.listdir('.')
    new_list = []
    # Jeden Dateinamen mit der Endung '.csv' oder '.json' der Liste new_list hinzufügen.
    for file in dir_list:
        if file.find(".csv") > -1 or file.find(".json") > -1:
            new_list.append(file)

    index = 0
    for file in new_list:
        index = index + 1
        print(str(index) + ": " + file)
    return new_list

