import csv


dateiname = "Adressliste.csv"


def read():
    with open(dateiname, newline='', encoding="utf8") as file:
        reader = csv.DictReader(file)
        list_of_dicts = []
        for v in reader:
            list_of_dicts.append(v)
        return list_of_dicts


def write(list_of_dicts):
    with open(dateiname, "w", newline='', encoding="utf8") as file:
        feldnamen=['Anrede', 'Name', 'Vorname', 'Straße', 'Hausnummer', 'PLZ', 'Stadt', 'Telefon 1', 'Telefon 2', 'Email']
        writer = csv.DictWriter(file, feldnamen, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(list_of_dicts)

