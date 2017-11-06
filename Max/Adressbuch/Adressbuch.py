import crud

# Anmerkung: Wir manipulieren eine Liste von Dictioniaries. Diese wird am Anfang ausgelesen,
# und erst beim speichern wird die csv-Datei überschrieben.

contacts = crud.read()

# Gibt an, wie viele Zeichen für die jeweilige Spalte erlaubt sind.
range = {"Anrede": 10, "Name": 15, "Vorname": 15, "Straße": 20, "Hausnummer": 15, "PLZ": 10, "Stadt": 15, "Telefon1": 15, "Telefon2": 15, "Email": 20}


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


# Alle Abfragen laufen über diese Funktion. Ermöglicht sich wiederholende Abfragen,
# sowie die Abfrage einzelner Eingaben.
def get_input(header):
    repeat = True
    while repeat:
        answer = input("--> " + header + ": (Max. " + str(range[header]) + " Zeichen)")

        # Wenn es sich um eine numerische Eingabe handelt
        if header == "Hausnummer" or header == "PLZ" or header == "Telefon1" or header == "Telefon2":

            # Auf Ziffern prüfen und ob es zu viele Zeichen sind
            if is_number(answer) and is_in_range(answer, header):
                repeat = False
                return answer
            else:
                print("Falsche Eingabe oder zu viele Zeichen!")

        # Überprüfen, ob es sich um eine gültige Email handelt
        # is_email gibt einen boolean und String zurück
        elif header == "Email":

            if is_email(answer)[0] and is_in_range(answer, header):
                repeat = False
                return answer
            else:
                print(is_email(answer)[1])

        # Wenn es sich um eine alphabetische Eingabe handelt
        else:

            if is_alphabetic(answer) and is_in_range(answer, header):

                repeat = False
                return answer
            else:
                print(answer)
                print("Falsche Eingabe oder zu viele Zeichen!")


def show_list(list):
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Adressbuch")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    # Abstand zwischen den Einträgen (für die Methode set_spacing)
    range_values = []
    for key in range:
        range_values.append(range[key])

    # Überschriften ausgeben
    counter = 0
    print("Pos:" + set_spacing("Pos:", 5), end="")
    for key in list[0]:
        print(key + ":" + set_spacing(key + ":", range_values[counter]), end="")
        counter = counter + 1
    print("")

    position = 0
    # Alle Einträge ausgeben
    for contact in list:
        counter = 0
        print(str(position + 1) + set_spacing(str(position + 1), 5), end="")
        for key in contact:
            print(contact[key] + set_spacing(contact[key], range_values[counter]), end="")
            counter = counter + 1
        print("")
        position = position + 1
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")


def add_item():
    anrede = get_input("Anrede")
    name = get_input("Name")
    vorname = get_input("Vorname")
    straße = get_input("Straße")
    hausnummer = get_input("Hausnummer")
    plz = get_input("PLZ")
    stadt = get_input("Stadt")
    telefon1 = get_input("Telefon1")
    telefon2 = get_input("Telefon2")
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
                        "Telefon1": telefon1,
                        "Telefon2": telefon2,
                        "Email": email}

            contacts.append(new_dict)
            repeat = False
            print("Der Kontakt '" + vorname + " " + name + "' wurde hinzugefügt.")
        elif confirm == "n":
            print("Abgebrochen!")
            repeat = False
        else:
            print("Falsche Eingabe!")


def change_item():
    index = input("--> Welche Position möchten Sie ändern?")

    if index.isnumeric():
        index = int(index)
        lines = get_all_entries()
        if index <= len(lines)-1:
            repeat = True
            old_item = lines[index][0]
            #decision = input("--> 1:Name oder 2:Menge ändern?")

            new_item = input("--> Welchen neuen Eintrag möchten Sie vornehmen?")
            if input_validation(new_item):
                amount = input("--> Wie viel von " + new_item + " möchten Sie hinzufügen?")
                if amount_input_validation(amount):
                    do_change = input("--> Möchten Sie die Änderung wirklich vornehmen? (ja oder nein)")

                    while repeat:
                        if do_change == "ja":
                            repeat = False
                            change_entry(index, new_item, amount)
                            print("Die Position " + str(index) + " wurde erfolgreich von " + old_item + " zu " + new_item + " geändert!")
                        elif do_change == "nein":
                            repeat = False
                            print("Abgebrochen!")
                        else:
                            repeat = True
                            print("Falsche Eingabe")
                            do_change = input("--> Möchten Sie die Änderung wirklich vornehmen? (ja oder nein)")
                else:
                    print("Falsche Eingabe! (Nur Zahlen)")
            else:
                print("Falsche Eingabe! (Nur Buchstaben)")
        else:
            print("Diese Position ist nicht vergeben!")
    else:
        print("Bitte geben Sie eine Nummer an!")


def delete_contact():
    index = input("--> Welche Position möchten Sie löschen?")
    if index.isnumeric():
        index = int(index)
        if index <= len(contacts)-1:
            repeat = True
            while repeat:
                name = contacts[index-1]["Name"]
                vorname = contacts[index-1]["Vorname"]
                delete = input("--> Möchten Sie den Kontakt" + vorname + " " + name + "wirklich löschen? (j/n)")
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
        print("Bitte geben Sie eine Nummer an!")


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
        print("Alle Kontakte mit dem Namen '" + name + "'.")
        show_list(result_list)
    else:
        print("Keine Kontake gefunden!")


def save(list_of_dicts):
    crud.write(list_of_dicts)
    print("Erfolgreich gespeichert!")


def execute():
    welcome = True
    while True:
        if welcome:
            print("-------------------------------------------------------------------------------------------")
            print("0000  0000  0  0  0000   0000  0  0    ")
            print("0     0  0  00 0   00    0  0  0  0    ")
            print("0     0  0  0000   00    0000  0000    ")
            print("0     0  0  0 00   00       0     0    ")
            print("0000  0000  0  0   00       0     0    ")
            print("-------------------------------------------------------------------------------------------")
            welcome = False

        x = input("\nMenü: \n1: Liste anzeigen    2: Kontakt suchen    3: Neuer Eintrag    4: Eintrag ändern \n5: Eintrag löschen   6: In Excel öffnen      7: Beenden \n\nIhre Eingabe: ")

        if x == "Liste anzeigen" or x == "1":
            show_list(contacts)
        elif x == "Kontakt suchen" or x == "2":
            search_contact()
        elif x == "Neuer Eintrag" or x == "3":
            add_item()
        elif x == "Eintrag ändern" or x == "4":
            change_item()
        elif x == "Eintrag löschen" or x == "5":
            delete_item()
        elif x == "In Excel öffnen" or x == "6":
            crud.open_file()
        elif x == "Speichern" or x == "7":
            save()
        elif x == "Beenden" or x == "8":
            print("Auf Wiedersehen!")
            exit()
        else:
            print("Falsche Eingabe")


#execute()
#add_item()
show_list(contacts)
