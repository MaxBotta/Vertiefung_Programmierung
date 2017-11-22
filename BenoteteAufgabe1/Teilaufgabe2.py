import BenoteteAufgabe1.CrudOperationen as Crud
import os
import operator

# Variable, die den Pfad der aktuel geladenen CSV-Datei enthält.
path = ""

# Liste aus Dicitonaries, die aus einer CSV-Datei mittels read Methode gelesen wird.
data = []


# Diese Methode gibt eine Liste mit den Feldnamen (keys) eines Datensatzes zurück.
def get_fieldnames(d):
    fieldnames = []
    for key in d[0]:
        fieldnames.append(key)
    return fieldnames


# Dieser Methode wird ein Datensatz, ein Feldname und ein keyword übergeben.
# Anschließend werden alle Einträge der Spalte auf ein Suchwort geprüft.
# Alle passenden Einträge werden in einer neuen Liste zurückgegeben.
def search_for_header_and_key(d, header, keyword):
    key_list = get_fieldnames(d)
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


# Fordert den Nutzer auf ein Suchwort einzugeben, prüft die EIngabe und gibt die Antwort zurück.
# Die Frage wird solange wiederholt, bis eine korrekte Eingabe stattgefunden hat.
def get_keyword_input():
    while True:
        keyword = input("--> Geben Sie ein Suchwort ein: ")
        if len(keyword) > 0:
            return keyword
        else:
            "Falsche Eingabe!"


# Fordert den Nutzer auf, ein Feldname auszuwählen.
# Die Frage wird solange wiederholt, bis eine korrekte Eingabe stattgefunden hat.
def get_fieldname_input(d):
    while True:
        fieldname = input("--> Wählen Sie ein Feld aus: ")
        if fieldname.isnumeric() and int(fieldname) <= len(d):
            return fieldname
        else:
            print("Falsche Eingabe!")


# Gibt alle Feldnamen mit einem Index in der Konsole aus.
def show_header_with_index(d):
    index = 0
    # Falls es sich um eine Liste von Dicts handelt
    if isinstance(d[0], dict):
        # Alle keys des ersten EIntrags durchlaufen und in der Konsole ausgeben
        for key in d[0]:
            index = index + 1
            print(str(index) + ": " + key)
        print("")
    # Falls es sich um eine einfache Liste handelt
    else:
        # Alle EInträge durchlaufen und in der Konsole ausgeben.
        for item in d:
            index = index + 1
            print(str(index) + ": " + str(item))
        print("")


# Dieser Methode muss ein String und ein numerischer Wert übergeben werden.
# Zurückgegeben wird ein String gefüllt mit Leerzeichen entsprechend der
# angegeben Länge minus des übergeben Strings.
# Die Methode findet Verwendung bei der Darstellung als Tabelle in der Konsole.
# Sie ermöglicht einen einheitlichen Abstand zur nächsten Spalte.
def set_spacing(string, x):
    i = len(string)
    spacing = ""
    while i <= x:
        space = " "
        spacing = spacing + space
        i = i + 1
    return spacing


# Diese Methode durchsucht alle Einträge einer Spalte und gibt den
# längsten String und dessen Länge zurück.
def get_range(d, header):
    # Variable, die den Längenwert enthält.
    result = 0
    # Variable, die den längsten String enthält
    string = ""
    # Durchsuche alle Einträge der Liste
    for item in d:
        # Falls der Eintrag im gewählten Feldnamen länger als der aktuelle Wert
        # in der Variable result ist, wird diese überschrieben.
        if len(item[header]) > result:
            result = len(item[header]) + 4
            string = item[header]
    # Falls der Feldname selbst der längste String ist, wird dessen Länge in result gespeichert.
    if len(header) > result:
        result = len(header) + 4
        string = header
    return result, string


# Gibt ein Dictionary zurück mit den Feldnamen als Keys und der Spaltenlänge als Wert.
# Die Spaltenlänge wird mit der Methode get_range ermittelt.
def get_range_list(d):
    result_dict = {}
    for key in d[0]:
        if get_range(d, key)[0] >= 14:
            result_dict[key] = get_range(d, key)[0]
        else:
            result_dict[key] = 14
    return result_dict


# Diese Methode nimmt einen Datensatz als Parameter und gibt dessen Einträge als
# Tabelle in der Konsole aus.
def show_result(d):
    if len(d) > 0:
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Ergebnis")
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        # Dictionary, der die Längen der jeweiligen Spalten enthält.
        # Ermöglicht eine saubere Darstellung in Tabellenform.
        range_dict = get_range_list(d)

        # Überschriften in der Konsole ausgeben
        # Der Methode set_spacing wird der jeweilige Feldname übergeben und die Länge der Spalte.
        # Dese gibt einen String mit Leerzeichen zurück.
        for key in d[0]:
            print(key + ":" + set_spacing(key + ":", range_dict[key]), end="")
        print("")
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        # Alle Einträge in der Kosnole ausgeben.
        # Jeder Eintrag wird in eine neue Zeile geschrieben.
        for item in d:
            for key in item:
                print(item[key] + set_spacing(item[key], range_dict[key]), end="")
            print("")
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    else:
        print("Die Liste ist leer!")


# Prüft ob eine Datei mit einem bestimmten Namen bereits existiert.
def check_if_file_exists(name):
    file_list = get_all_csv()
    for item in file_list:
        if item == name + ".csv":
            return True
    return False


# Speichert eine List of Dicts als CSV-Datei
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


# Fordert den Nutzer auf, die Ergebnisse einer Suche als CSV zu speichern
# oder als Tabelle in der Konsole auszugeben.
def print_to_csv_or_console(d):
    print("Es wurden " + str(len(d)) + " Einträge gefunden!")
    while True:
        csv_or_console = input("--> Möchten Sie die Ergebnisse als CSV-Datei ('csv') speichern oder in der Konsole ('con') anzeigen? ")
        if csv_or_console == "con":
            # Liste als Tabelle ausgeben.
            show_result(d)
            # Nochmals fragen, ob die Ergebnisse als CSV gespeichert werden sollen.
            save_yes_no = input("Als CSV-Datei Speichern? (j/n)")
            # Wiederholen, bis korrekte Eingabe.
            while True:
                if save_yes_no == "j":
                    save_as_csv(d)
                    return
                elif save_yes_no == "n":
                    return
                else:
                    print("Falsche Eingabe!")

        elif csv_or_console == "csv":
            # Direkt als CSV speichern.
            save_as_csv(d)
            return
        else:
            print("Falsche Eingabe!")


# Gibt eine Liste aller Spalten zurück, die numerische Werte enthalen.
def get_numeric_fields(d):
    numeric_fields = []
    for key in d[0]:
        try:
            # Um sicherzustellen, dass float Werte ebenfalls berücksichtigt werden, werden diese
            # druch eine Typumwandlung getestet. Scheitert die Typumwandlung, wird der nächste
            # Wert überprüft.
            if float(d[0][key]):
                numeric_fields.append(key)
        except ValueError:
            continue
    return numeric_fields


# Fragt den Nutzer nach dem Vergleichsoperator
def get_operator_input():
    while True:
        operator = input("--> Geben Sie einen Vergleichsoperator ein (>, <, =): ")
        if len(operator) > 0 and operator == "<" or operator == ">" or operator == "=":
            return operator
        else:
            print("Falsche Eingabe!")


# Fragt den Nutzer nach dem zu Vergleichenden Wert.
def get_comparison_input():
    while True:
        comparison = input("--> Geben Sie einen Vergleichswert ein: ")
        # Überprüfen, ob eine Eingabe stattgefunden  hat und ob es eine Zahl ist.
        if len(comparison) > 0 and comparison.isdigit():
            return float(comparison)
        else:
            print("Falsche Eingabe!")


# Fragt den Nutzer nach dem logischen Operator.
def get_logical_operator_input():
    while True:
        logical_operator = input("--> Geben Sie einen logischen Operator ein (UND oder ODER): ")
        if len(logical_operator) > 0 and logical_operator == "UND" or logical_operator == "ODER":
            return logical_operator
        else:
            print("Falsche Eingabe!")


# Nimmt einen Datensatz, einen Headername, einen Vergleichsoperator und einen Vergleichswert und gibt
# die zutrefenden Einträge zurück.
def get_comparison_result(d, fieldname, operator, value):
    list_of_dicts = []
    #Alle EInträge des Datensatzes durchlaufen
    for item in d:
        # Alle Spalten durchlaufen
        for key in item:
            # Falls der Spaltenname dem gewünschten Feldnamen entspricht
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
def get_second_filter_result(d, fieldname1, fieldname2, operator1, operator2, value1, value2, logical_operator):
    list_of_dicts = []
    # Alle Einträge durchlaufen
    for item in d:
        # Falls der UND Operator gewählt wurde
        if logical_operator == "UND":
            # Überprüfe ob der Wert in der Spalte ><= dem zu vergleichenden Wert True ergibt
            # UND
            # Überprüfe ob der Wert in der zweiten Spalte ><= dem zweiten zu vergleichenden Wert True ergibt
            if get_truth(float(item[fieldname1]), operator1, value1) and get_truth(float(item[fieldname2]), operator2, value2):
                list_of_dicts.append(item)
        elif logical_operator == "ODER":
            # Überprüfe ob der Wert in der Spalte ><= dem zu vergleichenden Wert True ergibt
            # ODER
            # Überprüfe ob der Wert in der zweiten Spalte ><= dem zweiten zu vergleichenden Wert True ergibt
            if get_truth(float(item[fieldname1]), operator1, value1) or get_truth(float(item[fieldname2]), operator2, value2):
                list_of_dicts.append(item)

    return list_of_dicts


# Diese Funktion wendet einen einfachen Filter an und gibt die zutreffenden Einträge als Liste zurück.
def get_result(d, fieldname, operator, comparison_value):
    list_of_dicts = []
    # Übergebene Liste durchlaufen.
    for item in d:
        # Falls ein Eintrag dem Filter entspricht, gibt die Methode get_truth ein True zurück.
        if get_truth(float(item[fieldname]), operator, comparison_value):
            # Eintrag der Liste hinzufügen
            list_of_dicts.append(item)

    return list_of_dicts


# Fragt den Nutzer, welche CSV-Datei geladen werden soll.
def get_files():
    repeat = True
    while repeat:
        print("Alle CSV-Dateien:")
        file_list = Crud.get_all_csv()

        # Überprüfen, ob die List leer ist.
        # Sind CSV Dateien vorhanden, werden diese in der Konsole ausgegeben.
        if len(file_list) > 0:
            index = 0
            for file in file_list:
                index = index + 1
                print(" " + str(index) + ": " + file)

            # Nutzer auffordern, eine CSV-Datei zu wählen.
            answer = input("\n-->Welche CSV-Datei wollen Sie laden? ('cancel' für Abbrechen)")
            if answer.isnumeric():
                answer_int = int(answer)
                if answer_int > 0 and answer_int <= len(file_list):
                    # path den Dateinamen zuweisen
                    global path
                    path = file_list[answer_int - 1]

                    # Datensatz in der data speichern
                    global data
                    data = Crud.read(path)
                    print("\nDatei geladen!\n")
                    return
                else:
                    print("\nFalsche Eingabe!\n")
            elif answer == "cancel":
                return
            else:
                print("\nFalsche Eingabe!\n")
        else:
            print("Keine CSV-Dateien vorhanden!")


def suchen_von_daten(d):
    if len(d) > 0:
        print("\n--- SUCHEN VON DATEN ---\n")
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
    else:
        print("Die Liste ist leer!")


def filtern_von_daten(d):
    if len(d) > 0:
        #1. Zwei Felder mit numerischen Inhalt auswählen.
        #2. Für jedes Feld einen Wert und einen Vergleichsoperator (größer, kleiner, gleich) angeben.
        #3. Diese beiden Vergleiche können nach Benutzerwunsch mit UND oder ODER logisch verknüpft werden.
        #4. Ergebnise als CSV speichern oder in der Konsole ausgeben.

        result_list = []

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
        print("Erste Eingabe: " + fieldname1 + " " + operator1 + " " + str(comparison_value1))

        # Fragen, ob ein zweiter Filter hinzugefügt werden soll
        while True:
            second_filter = input("--> Möchten Sie einen zweiten Filter wählen? (j/n) ")
            if second_filter == "j":
                # Nach logischem Operator fragen und hinterlegen.
                logical_operator = get_logical_operator_input()

                # Zweite Eingabe abfragen.
                field2 = get_fieldname_input(numeric_fields)
                fieldname2 = numeric_fields[int(field2) - 1]
                operator2 = get_operator_input()
                comparison_value2 = get_comparison_input()
                print("Zweite Eingabe: " + fieldname2 + " " + operator2 + " " + str(comparison_value2))

                # 3. Diese beiden Vergleiche mit UND oder ODER logisch verknüpfen.
                result_list = get_second_filter_result(d, fieldname1, fieldname2, operator1, operator2, float(comparison_value1), float(comparison_value2), logical_operator)
                break
            elif second_filter == "n":
                result_list = get_result(d, fieldname1, operator1, float(comparison_value1))
                break
            else:
                print("Falsche Eingabe!")

        # 4. Ergebnise als CSV speichern oder in der Konsole ausgeben.
        if len(result_list) == 0:
            print("Keine Einträge gefunden!")
        else:
            print_to_csv_or_console(result_list)
    else:
        print("Die Liste ist leer!")


# Diese Methode beinhaltet ein Menü zur Ausführung der einzelnen Funktionen.
def execute():
    welcome = True
    while True:
        if welcome:
            print("-------------------------------------------------------------------------------------------")
            print("0000  0000  0000  0     000  0000  0000       0000  0  0  0000")
            print("      0  0  0  0  0      0   0     0          0  0  0  0      ")
            print("0000  0000  0  0  0      0   0     0000       0000  0000  0000")
            print("      0     0  0  0      0   0     0             0     0      ")
            print("0000  0     0000  0000  000  0000  0000          0     0  0000")
            print("-------------------------------------------------------------------------------------------")
            welcome = False

        dateiname = ""
        if path == "":
            dateiname = "Keine Datei ausgewählt!"
        else:
            dateiname = path

        print("\nMENÜ")
        print("------------------------------------------------------------------------------------------")

        print("Datei: " + dateiname + "    Einträge: " + str(len(data)))
        print("------------------------------------------------------------------------------------------")
        print("1: CSV-Datei Laden   2: Liste anzeigen   3: Suchen von Daten   4: Filtern von Daten")
        print("5: Beenden")

        x = input("\nIhre Eingabe: ")
        print("")

        if x == "1":
            get_files()
        elif x == "2":
            show_result(data)
        elif x == "3":
            suchen_von_daten(data)
        elif x == "4":
            filtern_von_daten(data)
        elif x == "5":
            exit()
        else:
            print("Falsche Eingabe")


#execute()


