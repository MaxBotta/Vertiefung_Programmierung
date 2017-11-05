import crud

contacts = crud.read()
range = {"Anrede": 10, "Name": 15, "Vorname": 15, "Straße": 20, "Hausnummer": 15, "PLZ": 10, "Stadt": 15, "Telefon1": 15, "Telefon2": 15, "Email": 20}


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

def is_number_or_alpha(value):
    if is_number(value) or is_alphabetic(value):
        return True
    return False


#print(is_alphabetic("Herr") and is_in_range("Herr", "Anrede"))


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

    # Überprüfe ob mindestens ein Punkt vorhanden ist
    if value.find(".") >= 0:
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






test = "maxgmail.com"
print(is_email(test)[1])

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

        # Wenn es sich um die Email handelt. Hier sind alle Zeichen erlaubt
        # und es wird auf ein @ Zeichen geprüft
        elif header == "Email":

            if is_email(answer) and is_in_range(answer, header):
                repeat = False
                return answer
            else:
                print("Falsche Eingabe (@ Zeichen vergessen?) oder zu viele Zeichen!")

        # Wenn es sich um eine alphabetische Eingabe handelt
        else:

            if is_alphabetic(answer) and is_in_range(answer, header):

                repeat = False
                return answer
            else:
                print(answer)
                print("Falsche Eingabe oder zu viele Zeichen!")


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
    anrede = get_input("Anrede")
    name = get_input("Name")
    vorname = get_input("Vorname")
    strasse = get_input("Straße")
    hausnummer = get_input("Hausnummer")
    plz = get_input("PLZ")
    stadt = get_input("Stadt")
    telefon1 = get_input("Telefon1")
    telefon2 = get_input("Telefon2")
    email = get_input("Email")

    # if input_validation(new_item):
    #     if len(new_item) <= 16:
    #         amount = input("--> Wie viel von " + new_item + " möchten Sie hinzufügen?")
    #         if amount_input_validation(amount):
    #             answer = input("--> Möchten Sie " + new_item + " wirklich der Liste hinzufügen? (ja oder nein)")
    #             while repeat:
    #                 if answer == "ja":
    #                     repeat = False
    #                     new_entry(new_item, amount)
    #                     print("Produkt %s wurde dem Einkaufszettel hinzugefügt" % new_item)
    #                 elif answer == "nein":
    #                     repeat = False
    #                     print("Abgebrochen!")
    #                 else:
    #                     repeat = True
    #                     print("Falsche Eingabe!")
    #                     answer = input("--> Möchten Sie " + new_item + " wirklich der Liste hinzufügen? (ja oder nein)")
    #         else:
    #             print("Falsche Eingabe! (Nur Zahlen)")
    #     else:
    #         print("Zu viele Zeichen! (Maximal 16)")
    #
    # else:
    #     print("Falsche Eingabe! (Nur Buchstaben)")


#add_item()


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
