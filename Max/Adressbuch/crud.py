import csv
import os


def read(path):
    try:
        with open(path, "r", newline='', encoding="utf8") as file:
            reader = csv.DictReader(file)
            list_of_dicts = []
            for v in reader:
                list_of_dicts.append(v)
            return list_of_dicts

    except IOError:
        print('An error occured trying to read the file.')


def write(path, list_of_dicts):
    try:
        with open(path, "w", newline='', encoding="utf8") as file:
            fieldnames=['Anrede', 'Name', 'Vorname', 'Straße', 'Hausnummer', 'PLZ', 'Stadt', 'Telefon 1', 'Telefon 2', 'Email']
            writer = csv.DictWriter(file, fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(list_of_dicts)

    except IOError:
        print('An error occured trying to write the file.')


def open_file(path):
    os.system("open " + path)


def get_all_csv():
    dir_list = os.listdir('.')
    new_list = []
    for file in dir_list:
        if file.find('.csv') > -1:
            new_list.append(file)

    index = 0
    for file in new_list:
        index = index + 1
        print(str(index) + ": " + file)
    return new_list

