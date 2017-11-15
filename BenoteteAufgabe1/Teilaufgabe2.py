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


# Feldnamen abfragen.
# Wiederholen, bis eine korrekte Eingabe vorgenommen wurde.
def get_fieldname(d):
    while True:
        fieldname = input("Ihre Eingabe: ")
        if fieldname.isnumeric() and int(fieldname) <= len(d):
            return fieldname
        else:
            print("Falsche Eingabe!")


# Alle Header ausgeben mit Index.
def show_header_with_index(d):
    index = 0
    for key in d[0]:
        index = index + 1
        print(str(index) + ": " + key)


def set_spacing(string, x):
    i = len(string)
    spacing = ""
    while i <= x:
        space = " "
        spacing = spacing + space
        i = i + 1
    return spacing


def get_range(d, header):
    #Höchsten Wert finden und zurückgeben.
    result = 0
    string = ""
    for item in d:
        if len(item[header]) > result:
            result = len(item[header])
            string = item[header]
    return result, string


def get_range_list(d):
    result_dict = {}
    for key in d[0]:
        if get_range(d, key)[0] >= 14:
            result_dict[key] = get_range(d, key)[0]
        else:
            result_dict[key] = 14
    return result_dict


print(get_range_list(daten))


def show_result(d):
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Ergebnis")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    range_dict = get_range_list(d)

    # Überschriften ausgeben
    for key in d[0]:
        print(key + ":" + set_spacing(key + ":", range_dict[key]), end="")
    print("")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    # Alle Einträge ausgeben
    for item in d:
        for key in item:
            print(item[key] + set_spacing(item[key], range_dict[key]), end="")
        print("")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")


def suchen_von_daten(d):
    # ---1. Suchfeld angeben und überprüfen.---
    print("In welchem Feld möchten Sie suchen?")
    show_header_with_index(d)
    suchfeld = get_fieldname(d)
    # ---2. Suchwort angeben und überprüfen.---
    suchwort = get_keyword()
    # ---3. Nach Einträgen suchen.---
    result_list = search_for_header_and_key(d, suchfeld, suchwort)
    # ---4. Ergebnis in der Konsole ausgeben oder als CSV Speichern.---
    show_result(result_list)


suchen_von_daten(daten)




