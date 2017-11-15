import BenoteteAufgabe1.CrudOperationen as Crud
import csv


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

#Der Name der einzulesenden Datei
#dateiname = "tb01_FaelleGrundtabelleKreise_csv.csv"
dateiname = "/Users/maxbotta/PycharmProjects/Vertiefung_Programmierung/Max/Adressbuch/contacts.csv"
daten = read(dateiname, "csv")
print(daten)
#print(daten)


def set_key_list(d):
    key_list = []
    for key in d[0]:
        key_list.append(key)
    return key_list


def search_for_header_and_key(d, header, keyword):
    key_list = set_key_list(d)
    result_list = []
    for item in d:
        for key in item:
            if key == key_list[int(header) - 1]:
                if item[key] == keyword:
                    result_list.append(item)
                    break
    return result_list


def get_keyword():
    while True:
        print("Geben Sie ein Suchwort ein.")
        keyword = input("Ihre Eingabe: ")
        if len(keyword) > 0:
            return keyword
        else:
            "Falsche Eingabe!"


def get_fieldname(d):
    while True:
        fieldname = input("Ihre Eingabe: ")
        if fieldname.isnumeric() and int(fieldname) <= len(d):
            return fieldname
        else:
            print("Falsche Eingabe!")


def show_header_names(d):
    index = 0
    for key in d[0]:
        index = index + 1
        print(str(index) + ": " + key)


def suchen_von_daten(d):
    # search:
    # 1. Suchfeld angeben und überprüfen.
    # 2. Suchwort angeben und überprüfen.
    # 3. Nach Einträgen suchen
    # 4. Ergebnis in der Konsole ausgeben oder als CSV Speichern.

    # ---1. Suchfeld angeben und überprüfen.---
    print("In welchem Feld möchten Sie suchen?")
    # Alle Header ausgeben mit Index.
    show_header_names(d)

    # Eingabe überprüfen
    # Wiederholen, bis eine korrekte Eingabe vorgenommen wurde.
    suchfeld = get_fieldname(d)

    # ---2. Suchwort angeben und überprüfen.---
    suchwort = get_keyword()

    # ---3. Nach Einträgen suchen.---
    result_list = search_for_header_and_key(d, suchfeld, suchwort)

    # ---4. Ergebnis in der Konsole ausgeben oder als CSV Speichern.---
    print("Ergebnis:")
    for item in result_list:
        print(item)

suchen_von_daten(daten)




