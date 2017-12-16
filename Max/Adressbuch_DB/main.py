import Max.Adressbuch_xml.crud as CRUD

# Anmerkung: Wir manipulieren eine Liste von Dictioniaries. Diese wird am Anfang ausgelesen
# und erst beim speichern wird die json-Datei überschrieben.


global contacts
contacts = []

#Für Testzwecke
#contacts = crud.read("Ingo.json")

global path
path = ""

global made_changes
made_changes = False

# Gibt an, wie viele Zeichen für die jeweilige Spalte erlaubt sind.
range = {"Anrede": 10, "Name": 15, "Vorname": 15, "Straße": 20, "Hausnummer": 15, "PLZ": 10, "Stadt": 15, "Rufnummern": 20, "E-Mail-Adressen": 30}


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


def yes_no_repeat(question):
    # Abfragen, ob weitere E-Mails hinzugefügt werden sollen
    repeat_j_n = True
    while repeat_j_n:
        answer = input(question)
        if answer == "j":
            repeat_j_n = False
            return True
        elif answer == "n":
            repeat_j_n = False
            return False
        else:
            print("Falsche Eingabe!")


def get_files():
    repeat = True
    while repeat:
        print("\nAlle Dateien:")
        file = CRUD.get_all_json_and_xml()
        answer = input("\nWelche Datei wollen Sie laden? ('cancel' für Abbrechen)")

        if answer.isnumeric():
            answer_int = int(answer)

            if answer_int > 0 and answer_int <= len(file):
                global path
                path = file[answer_int - 1]
                global contacts

                # Dateityp überprüfen
                if path.find(".json") > -1:
                    contacts = CRUD.read_json(path)
                elif path.find(".xml") > -1:
                    contacts = CRUD.read_xml(path)

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
        if header == "Hausnummer" or header == "PLZ":
            # Auf Ziffern prüfen und ob es zu viele Zeichen sind
            if (is_number(answer) and is_in_range(answer, header)) or answer == "":
                repeat = False
                return answer
            else:
                print("Falsche Eingabe oder zu viele Zeichen!")

        # Wenn es sich um eine alphabetische Eingabe handelt
        elif header == "Name" or header == "Vorname":
            if (is_alphabetic(answer) and is_in_range(answer, header)):
                repeat = False
                return answer
            elif answer == "":
                print("Dieses Feld muss ausgefüllt werden!")
            else:
                print("Falsche Eingabe oder zu viele Zeichen!")

        else:
            if (is_alphabetic(answer) and is_in_range(answer, header)) or answer == "":
                repeat = False
                return answer
            else:
                print("Falsche Eingabe oder zu viele Zeichen!")


def get_email_input():
    # Typbezeichnung abfragen.
    email_typ = input("--> E-Mail Bezeichnung: ")
    if email_typ == "":
        return {"Typ": "", "E-Mail": ""}
    elif len(email_typ) > 0:
        # E-Mail abfragen und validieren.
        repeat = True
        while repeat:
            email = input("--> E-Mail: ")
            validate = is_email(email)
            if validate[0]:
                repeat = False
                return {"Typ": email_typ, "E-Mail": email}
            else:
                print(validate[1])


def get_phone_number_input():
    # Typbezeichnung abfragen.
    number_typ = input("--> Rufnummer Bezeichnung: ")
    if number_typ == "":
        return {"Typ": "", "Nummer": ""}
    elif len(number_typ) > 0:
        # Nummer abfragen
        number = input("--> Nummer: ")
        return {"Typ": number_typ, "Nummer": number}


# Diese Methode liest den höchsten Wert jeweils für Telefonnummern (Alle Nummern + Name) und
# Emails (Alles Emails + Name) aus und setzt einen Abstandswert für den Header.
def set_rufnummern_and_email_range():
    largest_number = 0
    largest_email = 0
    x_numbers = 0
    x_emails = 0
    number_string = ""
    email_string = ""

    for contact in contacts:
        #Höchsten Rufnummer Wert finden und setzen.
        counter = 0
        string = ""
        for item in contact["Rufnummern"]:
            counter = counter + 1
            string = string + item["Typ"] + item["Nummer"] + ""
            if int(len(string)) > largest_number:
                largest_number = int(len(string))
                number_string = string
                x_numbers = counter
        #Höchsten Email Wert finden und setzen.
        string = ""
        for item in contact["E-Mail-Adressen"]:
            counter = counter + 1
            string = string + str(item["Typ"]) + str(item["E-Mail"]) + ""
            if int(len(string)) > largest_email:
                largest_email = int(len(string))
                email_string = string
                x_emails = counter

    range["Rufnummern"] = largest_number + 4 * x_numbers
    range["E-Mail-Adressen"] = largest_email + 4 * x_emails
    return number_string, email_string


def show_list(list):
    largest_strings = set_rufnummern_and_email_range()
    # for item in contacts:
    #     print(item)

    if len(contacts) > 0:
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Kontakte in " + path)
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")

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
                if key == "Rufnummern":
                    string = ""
                    for item in contact[key]:
                        string = string + item["Typ"] + ": " + item["Nummer"] + "  "
                        print(item["Typ"] + ": " + item["Nummer"], end="  ")
                    print(set_spacing(string, range["Rufnummern"]), end="")
                    #print(string)
                elif key == "E-Mail-Adressen":
                    string = ""
                    for item in contact[key]:
                        string = string + str(item["Typ"]) + ": " + str(item["E-Mail"]) + "  "
                        print(str(item["Typ"]) + ": " + str(item["E-Mail"]), end="  ")
                    print(set_spacing(string, range["E-Mail-Adressen"]), end="")
                    #print(string)
                else:
                    print(str(contact[key]) + set_spacing(str(contact[key]), range[key]), end="")
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

    # Abfrage der Rufnummern. Es können beliebig viele hinzugefügt werden.
    repeat_number = True
    rufnummern = []
    while repeat_number:
        rufnummer = get_phone_number_input()
        rufnummern.append(rufnummer)
        # Abfragen, ob weitere Rufnummern hinzugefügt werden sollen
        repeat_number = yes_no_repeat("Möchten Sie eine weitere Rufnummern hinzufügen? (j/n)")

    # Abfrage der E-Mail-Adressen:
    repeat_email = True
    emails = []
    while repeat_email:
        email = get_email_input()
        emails.append(email)
        # Abfragen, ob weitere E-Mails hinzugefügt werden sollen
        repeat_email = yes_no_repeat("Möchten Sie eine weitere E-Mail-Adresse hinzufügen? (j/n)")


    # Wiederholen, bis eine korrekte Eingabe stattgefunden hat
    repeat = True
    while repeat:
        confirm = input("--> Möchten Sie den Kontakt '" + vorname + " " + name + "' wirklich der Liste hinzufügen? (j/n)")
        if confirm == "j":
            new_contact = {"Anrede": anrede,
                        "Name": name,
                        "Vorname": vorname,
                        "Straße": straße,
                        "Hausnummer": hausnummer,
                        "PLZ": plz,
                        "Stadt": stadt,
                        "Rufnummern": rufnummern,
                        "E-Mail-Adressen": emails
                        }

            # Kontakt wird in die Datenbank geschrieben
            # TODO CRUD Funktionen implentieren
            crud_db.write(new_contact)
            repeat = False
            made_changes = True
            print("Der Kontakt '" + vorname + " " + name + "' wurde hinzugefügt.")
        elif confirm == "n":
            print("Abgebrochen!")
            repeat = False
        else:
            print("Falsche Eingabe!")


# Diese Funktion kann eine Rufnummer löschen oder bearbeiten.
def change_phone_number(contact):
    # Alle Rufnummern eines Kontaktes ausgeben.
    print("\nDer Kontakt hat folgende Rufnummern: ")
    counter = 0
    for item in contact["Rufnummern"]:
        counter = counter + 1
        print(str(counter) + ":   " + item["Typ"] + ": " + item["Nummer"])

    # Abfrage, welche Rufnummer geändert werden soll.
    repeat = True
    while repeat:
        index = input("\nWelche Rufnummer möchten sie bearbeiten? ('cancel' für Abbrechen)")
        if is_number(index):
            index = int(index)
            # Überprüfen, ob der angegebene Index existiert.
            if index > 0 and index <= len(contact["Rufnummern"]):
                repeat = False
                # Abfrage, ob die Rufnummer geändert oder gelöscht werden soll.
                repeat2 = True
                while repeat2:
                    change_or_delete = input("Möchten Sie die Rufnummer ändern (change) oder löschen (delete)? ('cancel' für Abbrechen)")
                    if change_or_delete == "change":
                        repeat2 = False
                        contact["Rufnummern"][index - 1] = get_phone_number_input()
                        made_changes = True
                        print("Erfolgreich geändert!")
                    elif change_or_delete == "delete":
                        repeat2 = False
                        del contact["Rufnummern"][index - 1]
                        made_changes = True
                        print("Erfolgreich gelöscht!")
                    elif change_or_delete == "cancel":
                        repeat2 = False
                        print("Abgebrochen")
                    else:
                        print("Falsche Eingabe!")

            else:
                print("Dieser Index ist nicht vergeben!")
        elif index == "cancel":
            print("Abgebrochen!")
        else:
            print("Bitte einen Index angeben!")


# Diese Funktion kann eine E-Mail-Adresse löschen oder bearbeiten.
def change_email(contact):
    # Alle E-Mails eines Kontaktes ausgeben.
    print("\nDer Kontakt hat folgende E-Mail-Adressen: ")
    counter = 0
    for item in contact["E-Mail-Adressen"]:
        counter = counter + 1
        print(str(counter) + ":   " + item["Typ"] + ": " + item["E-Mail"])

    # Abfrage, welche E-Mail geändert werden soll.
    repeat = True
    while repeat:
        index = input("\nWelche E-Mail-Adresse möchten sie bearbeiten? ('cancel' für Abbrechen)")
        if is_number(index):
            index = int(index)
            # Überprüfen, ob der angegebene Index existiert.
            if index > 0 and index <= len(contact["E-Mail-Adressen"]):
                repeat = False
                # Abfrage, ob die E-Mail geändert oder gelöscht werden soll.
                repeat2 = True
                while repeat2:
                    change_or_delete = input("Möchten Sie die E-Mail-Adresse ändern (change) oder löschen (delete)? ('cancel' für Abbrechen)")
                    if change_or_delete == "change":
                        repeat2 = False
                        contact["E-Mail-Adressen"][index - 1] = get_email_input()
                        made_changes = True
                        print("Erfolgreich geändert!")
                    elif change_or_delete == "delete":
                        repeat2 = False
                        del contact["E-Mail-Adressen"][index - 1]
                        made_changes = True
                        print("Erfolgreich gelöscht!")
                    elif change_or_delete == "cancel":
                        repeat2 = False
                        print("Abgebrochen")
                    else:
                        print("Falsche Eingabe!")
            else:
                print("Dieser Index ist nicht vergeben!")
        elif index == "cancel":
            print("Abgebrochen!")
        else:
            print("Bitte einen Index angeben!")


def add_phone_number(contact):
    new_number = get_phone_number_input()
    contact["Rufnummern"].append(new_number)
    made_changes = True


def add_email(contact):
    new_email = get_email_input()
    contact["E-Mail-Adressen"].append(new_email)
    made_changes = True


def change_contact():
    # 1. Liste auf Einträge prüfen.
    # 2. Position (Kontakt) auswählen.
    # 3. Die zu bearbeitende Spalte auswählen.
    # 4. Falls Email oder Rufnummer: bearbeiten oder neues Objekt hinzufügen
    #    Entsprechende change und add Funktionen aufrufen.
    # 5. Falls Name, Straße etc. nach Input abfragen.

    # Überprüfen, ob die Liste leer ist.
    if len(contacts) == 0:
        print("Die Liste ist leer!")
    else:
        repeat = True
        while repeat:
            contact_index = input("--> Welche Position möchten Sie ändern? ('cancel' für Abbrechen)")

            # Prüfen, ob die Eingabe numerisch ist und ob die Position existiert.
            if contact_index.isnumeric():
                contact_index = int(contact_index)

                # Kontakt als Variable festhalten.
                contact = crud_db.search_by_id(contact_index)

                # Wenn Contact auch einen Kontakt enthält
                if not contact == -1:
                    repeat = False


                    # Abfragen, welche Spalte geändert werden soll.
                    repeat2 = True
                    while repeat2:
                        print("")
                        print("Welche Spalte möchten Sie bearbeiten?\n"
                              "1: Anrede   2: Name    3: Vorname       4: Straße            5: Hausnummer")
                        print("6: PLZ      7: Stadt   8: Rufnummern    9: E-Mail-Adressen  10: Abbrechen")
                        print("")
                        column_index = input("Ihre Eingabe:")

                        # Überprüfen, ob Eingabe numerisch und kleiner 11.
                        if column_index.isnumeric():
                            column_index = int(column_index)
                            if column_index < 10 and column_index > 0:
                                repeat2 = False
                                # Änderung wird abgebrochen.
                                if column_index == 11:
                                    repeat2 = False

                                # Spalte wurde ausgewählt und entsprechende Abfrage wird ausgeführt.
                                else:
                                    # Liste, um die Strings den Funktionen get_input und change_column zu übergeben.
                                    columns = ["Anrede", "Name", "Vorname", "Straße", "Hausnummer", "PLZ", "Stadt", "Rufnummern", "E-Mail-Adressen"]
                                    column = columns[column_index - 1]

                                    # Überprüfen, ob Rufnummern oder E-Mail-Adressen geändert werden sollen.
                                    if column == "Rufnummern":
                                        repeat3 = True
                                        while repeat3:
                                            change_or_add = input("Möchten Sie eine Rufummer bearbeiten (change) oder hinzufügen (new)? ('cancel' für abbrechen)")
                                            if change_or_add == "change":
                                                change_phone_number(contact)
                                                repeat3 = False
                                            elif change_or_add == "new":
                                                add_phone_number(contact)
                                                repeat3 = False
                                            elif change_or_add == "cancel":
                                                print("Abgebrochen!")
                                                return
                                            else:
                                                print("Falsche Eingabe!")
                                    elif column == "E-Mail-Adressen":
                                        repeat3 = True
                                        while repeat3:
                                            change_or_add = input("Möchten Sie eine E-Mail-Adresse bearbeiten (change) oder hinzufügen (new)? ('cancel' für abbrechen)")
                                            if change_or_add == "change":
                                                change_email(contact)
                                                repeat3 = False
                                            elif change_or_add == "new":
                                                add_email(contact)
                                                repeat3 = False
                                            elif change_or_add == "cancel":
                                                print("Abgebrochen!")
                                                return
                                            else:
                                                print("Falsche Eingabe!")

                                    else:
                                        old_value = contact[column]
                                        new_value = get_input(column)
                                        # Alten Wert überschreiben
                                        contact[column] = new_value
                                        made_changes = True
                                        print("Die Spalte wurde geändert!")

                            else:
                                print("Bitte einen Wert von 1 bis 9 eingeben!")
                        else:
                            print("Bitte eine Nummer eingeben!")
                else:
                    print("Falsche Eingabe!")

            elif contact_index == "cancel":
                print("Abgebrochen!")
                return
            else:
                print("Falsche Eingabe!")


def delete_contact():
    index = input("--> Welche Position möchten Sie löschen?")
    if index.isnumeric():
        index = int(index)
        if index <= len(contacts) and index > 0:
            repeat = True
            while repeat:
                name = contacts[index - 1]["Name"]
                vorname = contacts[index - 1]["Vorname"]
                delete = input("--> Möchten Sie den Kontakt " + vorname + " " + name + " wirklich löschen? (j/n)")
                if delete == "j":
                    repeat = False
                    del contacts[index - 1]
                    made_changes = True
                    print("Der Kontakt " + vorname + " " + name + " wurde erfolgreich gelöscht!")
                elif delete == "n":
                    repeat = False
                    print("Abgebrochen!")
                else:
                    print("Falsche Eingabe!")

        else:
            print("Diese Position ist nicht vergeben!")

    else:
        print("Falsche Eingabe!")


def search_contact():
    if len(contacts) == 0:
        print("Die Liste ist leer!")
    else:
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
        name = input("Bitte geben Sie einen Dateinamen ein ('cancel' für abbrechen):")
        if name == "cancel":
            print("Nicht gespeichert!")
        else:
            # Dateityp überprüfen
                if path.find(".json") > -1:
                    path = name + ".json"
                    CRUD.write_json(path, list_of_dicts)
                elif path.find(".xml") > -1:
                    path = name + ".xml"
                    CRUD.write_xml(path, list_of_dicts)

    elif len(path) > 0:
        if path.find(".json") > -1:
            CRUD.write_json(path, list_of_dicts)
            print("Erfolgreich gespeichert!")
        elif path.find(".xml") > -1:
            CRUD.write_xml(path, list_of_dicts)
            print("Erfolgreich gespeichert!")


def check_if_saved():
    repeat = True
    while repeat:
        if made_changes:
            answer = input("Es gibt nicht gespeicherte Änderungen. Möchten Sie jetzt Speichern? (j/n)")
            if answer == "j":
                save(contacts)
                repeat = False
                print("Auf Wiedersehen!")
            elif answer == "n":
                repeat = False
                print("Auf Wiedersehen!")
            else:
                print("Falsche Eingabe")
        else:
            repeat = False
            print("Auf Wiedersehen!")


def execute():
    welcome = True
    while True:
        if welcome:
            print("------------------------------------------------------------------------------------------")
            print("   0000   0000  0000  0  0  0000   00   0000  0000  0000    0000  0  0  0000  ")
            print("         0     0  0  00 0   00   0  0  0      00   0       0  0  0  0        ")
            print(" 0000   0     0  0  0000   00   0000  0      00   0000    0000  0000  0000  ")
            print("       0     0  0  0 00   00   0  0  0      00      0       0     0          ")
            print("0000  0000  0000  0  0   00   0  0  0000   00   0000       0     0  0000  ")
            print("------------------------------------------------------------------------------------------")
            welcome = False

        dateiname = ""
        if path == "":
            dateiname = "Keine Datei ausgewählt!"
        else:
            dateiname = path

        print("\nMENÜ")
        print("------------------------------------------------------------------------------------------")

        print("Datei: " + dateiname + "    Kontakte: " + str(len(contacts)))
        print("------------------------------------------------------------------------------------------")
        print("1: Liste anzeigen        2: Kontakt suchen       3: Neuer Eintrag        4: Eintrag ändern")
        print("5: Eintrag löschen       6: Speichern            7: Datei laden          8: Beenden")
        x = input("\n\nIhre Eingabe: ")

        if x == "Liste anzeigen" or x == "1":
            try:
                show_list(contacts)
            except IOError:
                print('An error occured trying to read the file.')
        elif x == "Kontakt suchen" or x == "2":
            search_contact()
        elif x == "Neuer Eintrag" or x == "3":
            add_contact()
        elif x == "Eintrag ändern" or x == "4":
            change_contact()
        elif x == "Eintrag löschen" or x == "5":
            delete_contact()
        elif x == "Speichern" or x == "6":
            save(contacts)
        elif x == "Liste laden" or x == "7":
            get_files()
        elif x == "Beenden" or x == "8":
            check_if_saved()
            exit()
        else:
            print("Falsche Eingabe")


execute()
