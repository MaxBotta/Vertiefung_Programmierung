import csv
import os



def read(dateiname):
    with open(dateiname, newline='', encoding="utf8") as file:
        reader = csv.DictReader(file, skipinitialspace=True)
        list_of_dicts = []
        for v in reader:
            list_of_dicts.append(v)
        return list_of_dicts


def write(dateiname, list_of_dicts):
    with open(dateiname, "w", newline='', encoding="utf8") as file:
        feldnamen=['Anrede', 'Name', 'Vorname', 'Straße', 'Hausnummer', 'PLZ', 'Stadt', 'Telefon 1', 'Telefon 2', 'Email']
        writer = csv.DictWriter(file, feldnamen, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(list_of_dicts)


def getAllCSV():
    dirList = os.listdir('.')
    newList = []
    for File in dirList:
        if File.find('.csv') == -1:
            continue
        else:
            newList.append(File)
    index = 0
    for File in newList:
        index = index + 1
        print(str(index) + ". '" + File + "'")
    return newList
