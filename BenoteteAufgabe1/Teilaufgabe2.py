import BenoteteAufgabe1.CrudOperationen as Crud
import csv
import os
import operator


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
dateiname = "tb01_FaelleGrundtabelleKreise_csv.csv"
#dateiname = "/Users/maxbotta/PycharmProjects/Vertiefung_Programmierung/Max/Adressbuch/contacts.csv"
daten = Crud.read(dateiname)


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
                if item[key].find(keyword) >= 0:
                #if item[key] == keyword:
                    #print(re.search(keyword, item[key]))
                    result_list.append(item)
                    break
    return result_list


def get_keyword_input():
    while True:
        keyword = input("Geben Sie ein Suchwort ein: ")
        if len(keyword) > 0:
            return keyword
        else:
            "Falsche Eingabe!"


# Feldnamen abfragen.
# Wiederholen, bis eine korrekte Eingabe vorgenommen wurde.
def get_fieldname_input(d):
    while True:
        fieldname = input("Wählen Sie ein Feld aus: ")
        if fieldname.isnumeric() and int(fieldname) <= len(d):
            return fieldname
        else:
            print("Falsche Eingabe!")


# Alle Header ausgeben mit Index.
def show_header_with_index(d):
    index = 0
    if isinstance(d, dict):
        for key in d[0]:
            index = index + 1
            print(str(index) + ": " + key)
    elif isinstance(d, list):
        for item in d:
            index = index + 1
            print(str(index) + ": " + item)


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
            result = len(item[header]) + 4
            string = item[header]
    if len(header) > result:
        result = len(header) + 4
        string = header
    return result, string


def get_range_list(d):
    result_dict = {}
    for key in d[0]:
        if get_range(d, key)[0] >= 14:
            result_dict[key] = get_range(d, key)[0]
        else:
            result_dict[key] = 14
    return result_dict


# TODO Try catch falls es ein Problem mit der Darstellung gibt, einfach Liste ausgeben.
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


def check_if_file_exists(name):
    file_list = get_all_csv()
    print(file_list)
    for item in file_list:
        if item == name + ".csv":
            return True
    return False


def save_as_csv(d):
    while True:
        print("Bitte geben Sie einen Dateinamen ein: ")
        file_name = input("Ihre Eingabe: ")

        # Überprüfen, ob eine Datei mit diesem Namen bereits existiert.
        name_exists = check_if_file_exists(file_name)

        # Falls diese existiert überschreiben oder erneut nach dem Namen fragen.
        if name_exists:
            print("Eine Datei mit diesem namen existiert bereits. Möchten Sie diese überschreiben? (j/n)")
            overwrite = input("Ihre Eingabe: ")
            while True:
                if overwrite == "j":
                    Crud.write(file_name + ".csv", d, get_fieldnames(d))
                    print("Gespeichert!")
                    return
                elif overwrite == "n":
                    break
                else:
                    print("Falsche Eingabe!")

        elif not name_exists:
            Crud.write(file_name + ".csv", d, get_fieldnames(d))
            print("Gespeichert!")
            return


def get_fieldnames(d):
    fieldnames = []
    for key in d[0]:
        fieldnames.append(key)
    return fieldnames


def get_all_csv():
    # Liste mit sämtlichen Dateien ertsellen, die sich im selben Ordner befinden.
    dir_list = os.listdir('.')
    new_list = []
    # Jeden Dateinamen mit der Endung '.csv' der Liste new_list hinzufügen.
    for file in dir_list:
        if file.find(".csv") > -1:
            new_list.append(file)
    return new_list


def print_to_csv_or_console(d):
    while True:
        csv_or_console = input("Möchten Sie die Ergebnisse als CSV-Datei ('csv') speichern oder in der Konsole ('con') anzeigen?")
        if csv_or_console == "con":
            show_result(d)
            return
        elif csv_or_console == "csv":
            save_as_csv(d)
            return
        else:
            print("Falsche Eingabe!")


def suchen_von_daten(d):
    # ---1. Suchfeld angeben und überprüfen.---
    show_header_with_index(d)
    suchfeld = get_fieldname_input(d)

    # ---2. Suchwort angeben und überprüfen.---
    suchwort = get_keyword_input()

    # ---3. Nach Einträgen suchen.---
    result_list = search_for_header_and_key(d, suchfeld, suchwort)

    # ---4. Ergebnis in der Konsole ausgeben oder als CSV Speichern.---
    if len(result_list) == 0:
        print("Keine Einträge gefunden!")
    else:
        print_to_csv_or_console(result_list)


# suchen_von_daten(daten)


def get_numeric_fields(d):
    numeric_fields = []
    for key in d[0]:
        if d[0][key].isdigit():
            numeric_fields.append(key)
    return numeric_fields


# Fragt den Nutzer nach dem Vergleichsoperator
def get_operator_input():
    while True:
        operator = input("Geben Sie einen Vergleichsoperator ein (>, <, =): ")
        if len(operator) > 0 and operator == "<" or operator == ">" or operator == "=":
            return operator
        else:
            print("Falsche Eingabe!")


# Fragt den Nutzer nach dem zu Vergleichenden Wert.
def get_comparison_input():
    while True:
        comparison = input("Geben Sie einen Vergleichswert ein: ")
        if len(comparison) > 0 and comparison.isdigit():
            return comparison
        else:
            print("Falsche Eingabe!")


# Fragt den Nutzer nach dem logischen Operator.
def get_logical_operator_input():
    while True:
        logical_operator = input("Geben Sie einen logischen Operator ein (UND oder ODER): ")
        if len(logical_operator) > 0 and logical_operator == "UND" or logical_operator == "ODER":
            return logical_operator
        else:
            print("Falsche Eingabe!")


# Nimmt einen Datensatz, einen Headername, einen Vergleichsoperator und einen Vergleichswert und gibt
# die zutrefenden Einträge zurück.
def get_comparison_result(d, fieldname, operator, value):
    list_of_dicts = []
    for item in d:
        for key in item:
            if key == fieldname:
                if operator == ">":
                    if item[key] > value:
                        list_of_dicts.append(item)
                elif operator == "<":
                    if item[key] < value:
                        list_of_dicts.append(item)
                elif operator == "=":
                    if item[key] == value:
                        list_of_dicts.append(item)
    return list_of_dicts


# Vergleicht zwei Werte miteinander und gibt True oder False zurück.
# Vorteil der Funktion ist, dass die Vergleichsoperatoren als String übergeben werden können.
# Die Funktion nutzt das Modul 'operator'.
def get_truth(first_value, relate , second_value):
    ops = {'>': operator.gt,
           '<': operator.lt,
           '=': operator.eq}
    return ops[relate](first_value, second_value)


# Diese Funktion durchläuft alle Items einer Liste und schaut ob es passende Einträge zu
# den übergebenen Parametern gibt.
def get_logical_operator_result(d, fieldname1, fieldname2, operator1, operator2, value1, value2, logical_operator):
    list_of_dicts = []
    for item in d:
        if logical_operator == "UND":
            if get_truth(int(item[fieldname1]), operator1, value1) and get_truth(int(item[fieldname2]), operator2, value2):
                list_of_dicts.append(item)
        elif logical_operator == "ODER":
            if get_truth(int(item[fieldname1]), operator1, value1) or get_truth(int(item[fieldname2]), operator2, value2):
                list_of_dicts.append(item)

    return list_of_dicts


def filtern_von_daten(d):
    #1. Zwei Felder mit numerischen Inhalt auswählen.
    #2. Für jedes Feld einen Wert und einen Vergleichsoperator (größer, kleiner, gleich) angeben.
    #3. Diese beiden Vergleiche können nach Benutzerwunsch mit UND oder ODER logisch verknüpft werden.
    #4. Ergebnise als CSV speichern oder in der Konsole ausgeben.

    # Alle Numerischen Felder anzeigen.
    numeric_fields = get_numeric_fields(d)
    show_header_with_index(numeric_fields)

    # 1. Zwei Felder mit numerischen Inhalt auswählen.
    # 2. Für jedes Feld einen Wert und einen Vergleichsoperator (größer, kleiner, gleich) angeben.

    # Erste Eingabe abfragen.
    field1 = get_fieldname_input(numeric_fields)
    fieldname1 = numeric_fields[int(field1) - 1]
    operator1 = get_operator_input()
    comparison_value1 = get_comparison_input()
    # Erste Eingabe ausgeben.
    print("Erste Eingabe: " + fieldname1 + " " + operator1 + " " + comparison_value1)

    # Nach logischem Operator fragen und hinterlegen.
    logical_operator = get_logical_operator_input()

    # Zweite Eingabe abfragen.
    field2 = get_fieldname_input(numeric_fields)
    fieldname2 = numeric_fields[int(field2) - 1]
    operator2 = get_operator_input()
    comparison_value2 = get_comparison_input()
    print("Zweite Eingabe: " + fieldname2 + " " + operator2 + " " + comparison_value2)

    # 3. Diese beiden Vergleiche mit UND oder ODER logisch verknüpfen.
    result_list = get_logical_operator_result(d, fieldname1, fieldname2, operator1, operator2, int(comparison_value1), int(comparison_value2), logical_operator)

    # 4. Ergebnise als CSV speichern oder in der Konsole ausgeben.
    if len(result_list) == 0:
        print("Keine Einträge gefunden!")
    else:
        print_to_csv_or_console(result_list)


filtern_von_daten(daten)

#test = get_truth(int(daten[0]["erfasste Faelle"]), ">", 1000)
#print(test)



