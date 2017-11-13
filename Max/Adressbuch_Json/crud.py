import csv
import json
import os


# Diese Methode kann JSON und CSV Dateien lesen und als Liste zurückgeben.
def read(path):
    try:
        with open(path) as file:
            data = json.load(file)
            return data
    except IOError:
        print('An error occured trying to read the file.')


def write(path, data):
    try:
        with open(path, 'w') as outfile:
            json.dump(data, outfile)

    except IOError:
        print('An error occured trying to write the file.')


def get_all_json():
    # Liste mit sämtlichen Dateien ertsellen, die sich im selben Ordner befinden.
    dir_list = os.listdir('.')
    new_list = []
    # Jeden Dateinamen mit der Endung '.csv' oder '.json' der Liste new_list hinzufügen.
    for file in dir_list:
        if file.find(".json") > -1:
            new_list.append(file)

    index = 0
    for file in new_list:
        index = index + 1
        print("  " + str(index) + ": " + file)
    return new_list

