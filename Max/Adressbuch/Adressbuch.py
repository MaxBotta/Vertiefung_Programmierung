import crud

contacts = crud.read()
range = {"anrede": 10, "name": 15, "vorname": 15, "strasse": 20, "hausnummer:": 15, "plz": 10, "stadt": 15, "telefon1": 15, "telefon2": 15, "email": 20}


def set_spacing(string, x):
    i = len(string)
    spacing = ""
    while i <= x:
        space = " "
        spacing = spacing + space
        i = i + 1
    return spacing


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


def show_list():
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Adressbuch")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    # Abstand zwischen den Einträgen (für die Methode set_spacing)
    range_values = []
    for key in range:
        range_values.append(range[key])

    # Überschriften ausgeben
    counter = 0
    for key in contacts[0]:
        print(key + ":" + set_spacing(key + ":", range_values[counter]), end="")
        counter = counter + 1
    print("")

    # Alle Einträge ausgeben
    for contact in contacts:
        counter = 0
        for key in contact:
            print(contact[key] + set_spacing(contact[key], range_values[counter]), end="")
            counter = counter + 1
        print("")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")


def add_item():
    repeat = True
    anrede = input("--> Anrede: (Max. 10 Zeichen)")
    name = input("--> Nachname: (Max. 15 Zeichen)")
    vorname = input("--> Vorname: (Max. 15 Zeichen)")
    strasse = input("--> Straße: (Max. 20 Zeichen)")
    hausnummer = input("--> Hausnummer: (Max. 15 Zeichen)")
    plz = input("--> Postleitzahl: (Max. 10 Zeichen)")
    stadt = input("--> Stadt: (Max. 15 Zeichen)")
    telefon1 = input("--> Telefon 1: (Max. 15 Zeichen)")
    telefon2 = input("--> Telefon 2: (Max. 15 Zeichen)")
    email = input("--> Email: (Max. 20 Zeichen)")

    if input_validation(new_item):
        if len(new_item) <= 16:
            amount = input("--> Wie viel von " + new_item + " möchten Sie hinzufügen?")
            if amount_input_validation(amount):
                answer = input("--> Möchten Sie " + new_item + " wirklich der Liste hinzufügen? (ja oder nein)")
                while repeat:
                    if answer == "ja":
                        repeat = False
                        new_entry(new_item, amount)
                        print("Produkt %s wurde dem Einkaufszettel hinzugefügt" % new_item)
                    elif answer == "nein":
                        repeat = False
                        print("Abgebrochen!")
                    else:
                        repeat = True
                        print("Falsche Eingabe!")
                        answer = input("--> Möchten Sie " + new_item + " wirklich der Liste hinzufügen? (ja oder nein)")
            else:
                print("Falsche Eingabe! (Nur Zahlen)")
        else:
            print("Zu viele Zeichen! (Maximal 16)")

    else:
        print("Falsche Eingabe! (Nur Buchstaben)")


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


def delete_item():
    index = input("--> Welche Position möchten Sie löschen?")
    if index.isnumeric():
        index = int(index)
        lines = get_all_entries()
        if index <= len(lines)-1:
            repeat = True
            while repeat:
                delete = input("--> Möchten Sie " + lines[index][0] + " an der Position " + str(index) + " wirklich löschen? (ja oder nein)")
                if delete == "ja":
                    repeat = False
                    old_value = get_entry(index)[0]
                    delete_entry(int(index))
                    print(old_value + " an der Position " + str(index) + " wurde erfolgreich gelöscht!")
                elif delete == "nein":
                    repeat = False
                    print("Abgebrochen!")
                else:
                    repeat = True
                    print("Falsche Eingabe!")

        else:
            print("Diese Position ist nicht vergeben!")

    else:
        print("Bitte geben Sie eine Nummer an!")


def show_item():
    index = input("--> Welche Position möchten Sie anzeigen?")
    if index.isnumeric():
        index = int(index)
        lines = get_all_entries()
        if index <= len(get_all_entries()):
            print("-------------------------------------")
            print("Pos:  " + lines[0][0] + ":         " + lines[0][1] + ":")
            #print("-------------------------------------")
            item = get_entry(index)
            spacing = set_spacing(item[0], 16)
            spacing2 = set_spacing(str(index), 5)
            print(str(index) + spacing2 + item[0] + spacing + item[1])
            print("-------------------------------------")
        else:
            print("Diese Position ist nicht vergeben!")
    else:
        print("Falsche Eingabe!")


def execute():
    welcome = True
    while True:
        if welcome:
            print("-------------------------------------------------------------------------------------------")
            print("0000  0  0  0000  0000  0000  0000  0  0  0000      00    0000  0000  0000      0000  0  0 ")
            print("0     0  0  0  0  0  0  0  0   00   00 0  0         00     00   0      00       0  0  0  0 ")
            print("0000  0000  0  0  0000  0000   00   0000  0 00      00     00   0000   00       0000  0000 ")
            print("   0  0  0  0  0  0     0      00   0 00  0  0      00     00      0   00          0     0 ")
            print("0000  0  0  0000  0     0     0000  0  0  0000      0000  0000  0000   00          0     0 ")
            print("-------------------------------------------------------------------------------------------")
            welcome = False

        x = input("\nMenü: \n1: Liste anzeigen    2: Position anzeigen    3: Neuer Eintrag    4: Eintrag ändern \n5: Eintrag löschen   6: In Excel öffnen      7: Beenden \n\nIhre Eingabe: ")

        if x == "Liste anzeigen" or x == "1":
            show_list()
        elif x == "Position anzeigen" or x == "2":
            show_item()
        elif x == "Neuer Eintrag" or x == "3":
            add_item()
        elif x == "Eintrag ändern" or x == "4":
            change_item()
        elif x == "Eintrag löschen" or x == "5":
            delete_item()
        elif x == "In Excel öffnen" or x == "6":
            open_file()
        elif x == "Beenden" or x == "7":
            print("Auf Wiedersehen!")
            exit()
        else:
            print("Falsche Eingabe")


#execute()
