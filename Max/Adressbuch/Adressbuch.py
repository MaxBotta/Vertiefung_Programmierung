import crud

# Anmerkung: Wir manipulieren eine Liste von Dictioniaries. Diese wird am Anfang ausgelesen
# und erst beim speichern wird die csv-Datei überschrieben.

global contacts
contacts = []
global path
path = ""
global file_type
file_type = ""

# Gibt an, wie viele Zeichen für die jeweilige Spalte erlaubt sind.
range = {"Anrede": 10, "Name": 15, "Vorname": 15, "Straße": 20, "Hausnummer": 15, "PLZ": 10, "Stadt": 15, "Telefon": 15, "Mobil": 15, "Email": 30}


def set_spacing(string, x):
    i = len(string)
    spacing = ""
    while i <= x:
        space = " "
        spacing = spacing + space
        i = i + 1
    return spacing


def split_string(name):
        names = name.split(" ")
        return names


def is_alphabetic(value):
    if all(i.isalpha() or i == ' ' for i in value):
        return True
    return False


def is_number(value):
    if value.isdigit():
        return True
    return False


def is_in_range(value, header):
    if len(value) <= range[header]:
        return True
    return False


def is_number_or_alpha(value):
    if is_number(value) or is_alphabetic(value):
        return True
    return False


#Überarbeiten
# - Zeichen nach @ gibt Fehler, wenn kein Zeichen nach @ (Index nicht vorhanden)
def is_email(value):
    at = False
    second_at = False
    before = False
    after = False
    dot = False
    space = False

    # Überprüfe ob ein @ existiert und ob es mehr als ein @ gibt
    at_index = value.find("@")
    second = value.find("@", at_index + 1)

    if at_index >= 0:
        at = True
    if second >= 0:
        second_at = True

    # Überprüfe ob Zeichen vor und nach dem @-Zeichen existieren
    if is_number_or_alpha(value[at_index-1]):
        before = True
    if len(value) > at_index + 1:
        if is_number_or_alpha(value[at_index+1]):
            after = True

    # Überprüfe ob ein Punkt nach dem @ vorhanden ist
    if value.find(".", at_index) >= 0:
        dot = True

    # Überprüfe ob ein Leerzeichen existiert
    if value.find(" ") >= 0:
        space = True

    if at and not second_at and before and after and dot and not space:
        return True, "Email validiert!"
    elif not at:
        return False, "@-Zeichen vergessen!"
    elif second_at:
        return False, "Zu viele @-Zeichen!"
    elif not before or not after:
        return False, "Vor und nach dem @ muss ein Zeichen stehen!"
    elif not dot:
        return False, "Punkt vergessen!"
    elif space:
        return False, "Leerzeichen vorhanden!"


# Dieser Funktion wird ein Key übergeben und gibt dann den Inhalt zurück.
# Vorsicht, der Inhalt kann auch eine Liste sein!
def get_key(myjson, key):
    if type(myjson) is dict:
        for jsonkey in myjson:
            if jsonkey == key:
                print(myjson[jsonkey])
            elif type(myjson[jsonkey]) in (list, dict):
                get_key(myjson[jsonkey], key)
    elif type(myjson) is list:
        for item in myjson:
            if type(item) in (list, dict):
                get_key(item, key)


def get_file_type(filename):
    if filename.find(".csv"):
        return "csv"
    elif filename.find(".json"):
        return "json"


def get_files():
    repeat = True
    while repeat:
        print("Alle CSV-Dateien:\n")
        file = crud.get_all_csv_and_json()
        answer = input("Welche CSV-Datei wollen Sie laden? ('cancel' für Abbrechen)")

        if answer.isnumeric():
            answer_int = int(answer)

            if answer_int > 0 and answer_int <= len(file):
                global path
                path = file[answer_int - 1]
                global contacts

                # Überprüfe Dateiendung und rufe READ-Funktion auf.
                file_type = get_file_type(path)
                contacts = crud.read(path, file_type)

                print("\nDatei geladen!\n")

                return
            else:
                print("\nFalsche Eingabe!\n")

        elif answer == "cancel":
            return
        else:
            print("\nFalsche Eingabe!\n")


# Alle Abfragen laufen über diese Funktion. Ermöglicht sich wiederholende Abfragen,
# sowie die Abfrage einzelner Eingaben.
def get_input(header):
    repeat = True
    while repeat:
        answer = input("--> " + header + ": (Max. " + str(range[header]) + " Zeichen)")

        # Wenn es sich um eine numerische Eingabe handelt
        if header == "Hausnummer" or header == "PLZ" or header == "Telefon 1" or header == "Telefon 2":

            # Auf Ziffern prüfen und ob es zu viele Zeichen sind
            if (is_number(answer) and is_in_range(answer, header)) or answer == "":
                repeat = False
                return answer
            else:
                print("Falsche Eingabe oder zu viele Zeichen!")

        # Überprüfen, ob es sich um eine gültige Email handelt
        # is_email gibt einen boolean und String zurück
        elif header == "Email":

            if answer == "":
                repeat = False
                return answer
            elif is_email(answer)[0]:
                if is_in_range(answer, header):
                    repeat = False
                    return answer
                else:
                    print("Zu viele Zeichen!")
            else:
                print(is_email(answer)[1])

        # Wenn es sich um eine alphabetische Eingabe handelt
        else:

            if (is_alphabetic(answer) and is_in_range(answer, header)) or answer == "":
                repeat = False
                return answer
            else:
                print(answer)
                print("Falsche Eingabe oder zu viele Zeichen!")


def show_list(list):
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Adressbuch")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    if len(contacts) > 0:
        # Abstand zwischen den Einträgen (für die Methode set_spacing)
        range_values = []
        for key in range:
            range_values.append(range[key])

        # Überschriften ausgeben
        counter = 0
        print("Pos:" + set_spacing("Pos:", 5), end="")
        for key in list[0]:
            print(key + ":" + set_spacing(key + ":", range[key]), end="")
            counter = counter + 1
        print("")

        position = 0
        # Alle Einträge ausgeben
        for contact in list:
            counter = 0
            print(str(position + 1) + set_spacing(str(position + 1), 5), end="")
            for key in contact:
                print(contact[key] + set_spacing(contact[key], range[key]), end="")
                counter = counter + 1
            print("")
            position = position + 1
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    else:
        print("Die Liste ist leer!")


def add_contact():
    anrede = get_input("Anrede")
    name = get_input("Name")
    vorname = get_input("Vorname")
    straße = get_input("Straße")
    hausnummer = get_input("Hausnummer")
    plz = get_input("PLZ")
    stadt = get_input("Stadt")
    telefon1 = get_input("Telefon 1")
    telefon2 = get_input("Telefon 2")
    email = get_input("Email")

    repeat = True

    # Wiederholen, bis eine korrekte Eingabe stattgefunden hat
    while repeat:
        confirm = input("--> Möchten Sie den Kontakt '" + vorname + " " + name + "' wirklich der Liste hinzufügen? (j/n)")
        if confirm == "j":
            new_dict = {"Anrede": anrede,
                        "Name": name,
                        "Vorname": vorname,
                        "Straße": straße,
                        "Hausnummer": hausnummer,
                        "PLZ": plz,
                        "Stadt": stadt,
                        "Telefon 1": telefon1,
                        "Telefon 2": telefon2,
                        "Email": email}

            contacts.append(new_dict)
            repeat = False
            print("Der Kontakt '" + vorname + " " + name + "' wurde hinzugefügt.")
        elif confirm == "n":
            print("Abgebrochen!")
            repeat = False
        else:
            print("Falsche Eingabe!")


def change_contact():
    repeat = True
    while repeat:
        contact_index = input("--> Welche Position möchten Sie ändern? ('cancel' für Abbrechen)")

        # Prüfen, ob die Eingabe numerisch ist und ob die Position existiert.
        if contact_index.isnumeric():
            contact_index = int(contact_index)

            if contact_index <= len(contacts) and contact_index > 0:
                repeat = False

                # Kontakt als Variable festhalten.
                contact = contacts[contact_index - 1]

                # Abfragen, welche Spalte geändert werden soll.
                repeat2 = True
                while repeat2:
                    print("")
                    print("Welche Spalte möchten Sie ändern?\n"
                          "1: Anrede    2: Name    3: Vorname   4: Straße   5: Hausnummer 6: PLZ\n"
                          "7: Stadt     8: Tel. 1  9: Tel. 2   10: E-Mail  11: Abbrechen")
                    print("")
                    column_index = input("Ihre Eingabe:")

                    # Überprüfen, ob Eingabe numerisch und kleiner 11.
                    if column_index.isnumeric():
                        column_index = int(column_index)
                        if column_index <= 10:
                            repeat2 = False


                            # Änderung wird abgebrochen.
                            if column_index == 11:
                                repeat2 = False

                            # Spalte wurde ausgewählt und entsprechende Abfrage wird ausgeführt.
                            else:

                                # Liste, um die Strings den Funktionen get_input und change_column zu übergeben.
                                columns = ["Anrede", "Name", "Vorname", "Straße", "Hausnummer", "PLZ", "Stadt", "Telefon 1", "Telefon 2", "Email"]
                                column = columns[column_index - 1]

                                old_value = contact[column]
                                new_value = get_input(column)

                                # Alten Wert überschreiben
                                contact[column] = new_value

                                print("Die Spalte " + column + " wurde erfolreich von " + old_value + " zu " + new_value + " geändert!")
                        else:
                            print("Bitte einen Wert zwischen 1 und 10 eingeben!")
                    else:
                        print("Bitte eine Nummer eingeben!")
            else:
                print("Falsche Eingabe!")

        elif contact_index == "cancel":
            return
        else:
            print("Falsche Eingabe!")


def delete_contact():
    index = input("--> Welche Position möchten Sie löschen?")
    if index.isnumeric():
        index = int(index)
        if index <= len(contacts):
            repeat = True
            while repeat:
                name = contacts[index - 1]["Name"]
                vorname = contacts[index - 1]["Vorname"]
                delete = input("--> Möchten Sie den Kontakt " + vorname + " " + name + " wirklich löschen? (j/n)")
                if delete == "j":
                    repeat = False
                    del contacts[index - 1]
                    print("Der Kontakt " + vorname + " " + name + "wurde erfolgreich gelöscht!")
                elif delete == "n":
                    repeat = False
                    print("Abgebrochen!")
                else:
                    repeat = True
                    print("Falsche Eingabe!")

        else:
            print("Diese Position ist nicht vergeben!")

    else:
        print("Falsche Eingabe!")


def search_contact():
    name = input("--> Geben Sie den Vor/Nachnamen oder vollständigen Namen ein.")

    # Eingabe in einzelne Suchwörter aufteilen
    keywords = split_string(name)
    result_list = []

    # Nach passenden Kontakten suchen
    for contact in contacts:
        if len(keywords) == 1:
            if contact["Name"].find(keywords[0]) >= 0 or contact["Vorname"].find(keywords[0]) >= 0:
                    result_list.append(contact)
        elif len(keywords) > 1:
            # Jedes Suchwort auf den Namen prüfen
            for v in keywords:
                if contact["Name"].find(v) >= 0:
                    # Falls passender Name, alle suchwörter auf Vornamen prüfen
                    for x in keywords:
                        if contact["Vorname"].find(x) >= 0:
                            result_list.append(contact)

    if len(result_list) > 0:
        print("")
        print("Alle Kontakte mit dem Namen '" + name + "':")
        show_list(result_list)
    else:
        print("Keine Kontake gefunden!")


def save(list_of_dicts):
    global path
    if path == "":
        name = input("Bitte geben Sie einen Dateinamen ein:")
        path = name + ".csv"
        crud.write(path, list_of_dicts)
    elif len(path) > 0:
        crud.write(path, list_of_dicts)
        print("Erfolgreich gespeichert!")


def check_if_saved():
    repeat = True
    while repeat:
        if len(path) == 0 and len(contacts) > 0:
            answer = input("Es gibt nicht gespeicherte Änderungen. Möchten Sie jetzt Speichen? (j/n)")
            if answer == "j":
                save(contacts)
                repeat = False
                print("Erfolgreich gespeichert. Auf Wiedersehen!")
            elif answer == "n":
                repeat = False
                print("Auf Wiedersehen!")
            else:
                print("Falsche Eingabe")

        elif len(path) > 0:
            old_contacts = crud.read(path)
            if contacts == old_contacts:
                answer = input("Es gibt nicht gespeicherte Änderungen. Möchten Sie jetzt Speichen? (j/n)")
                if answer == "j":
                    save(contacts)
                    repeat = False
                    print("Erfolgreich gespeichert. Auf Wiedersehen!")
                elif answer == "n":
                    repeat = False
                    print("Auf Wiedersehen!")
                else:
                    print("Falsche Eingabe")
            else:
                repeat = False
                print("Auf Wiedersehen")
        else:
            repeat = False
            print("Auf Wiedersehen!")





def new_file(name):
    print(name)


def execute():
    welcome = True
    while True:
        if welcome:
            print("-------------------------------------------------------------------------------------------")
            print("   0000   0000  0000  0  0  0000   00   0000  0000  0000    0000  0  0  0000  ")
            print("         0     0  0  00 0   00   0  0  0      00   0       0  0  0  0        ")
            print(" 0000   0     0  0  0000   00   0000  0      00   0000    0000  0000  0000  ")
            print("       0     0  0  0 00   00   0  0  0      00      0       0     0          ")
            print("0000  0000  0000  0  0   00   0  0  0000   00   0000       0     0  0000  ")
            print("-------------------------------------------------------------------------------------------")
            welcome = False

        x = input("\nMenü: \n1: Liste anzeigen      2: Kontakt suchen      3: Neuer Eintrag      4: Eintrag ändern \n"
                  "5: Eintrag löschen     6: In Excel öffnen     7: Speichern          8: CSV/JSON-Datei laden\n"
                  "9: Beenden"
                  "\n\nIhre Eingabe: ")

        if x == "Liste anzeigen" or x == "1":
            show_list(contacts)
        elif x == "Kontakt suchen" or x == "2":
            search_contact()
        elif x == "Neuer Eintrag" or x == "3":
            add_contact()
        elif x == "Eintrag ändern" or x == "4":
            change_contact()
        elif x == "Eintrag löschen" or x == "5":
            delete_contact()
        elif x == "In Excel öffnen" or x == "6":
            if len(path) == 0:
                print("Erst muss die Datei gespeichert werden!")
            else:
                crud.open_file(path)
        elif x == "Speichern" or x == "7":
            save(contacts)
        elif x == "Liste laden" or x == "8":
            get_files()
        elif x == "Beenden" or x == "9":
            check_if_saved()
            exit()
        else:
            print("Falsche Eingabe")


execute()

