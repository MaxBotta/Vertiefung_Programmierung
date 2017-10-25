from Max.csv_crad import *


shopping_list = ["Banane", "Apfel"]


def show_list():
    print("------------")
    #print("Einkaufszettel:")
    #print("")
    count = 0
    lines = get_all_entries()
    print("   " + lines[count][0] + "          " + lines[count][1])
    count = 1
    while count < len(lines):
        spacing = set_spacing(lines[count][0], 16)
        print(str(count) + ": " + lines[count][0] + spacing + lines[count][1])
        count = count + 1
    print("------------")


def set_spacing(string, x):
    i = len(string)
    spacing = ""
    while i <= x:
        space = " "
        spacing = spacing + space
        i = i + 1

    return spacing


def change_entry():
    index = input("--> Welche Position möchten Sie ändern?")

    if index.isnumeric():
        index = int(index)
        lines = get_all_entries()
        if index <= len(lines):
            old_value = lines[index-1]
            new_value = input("--> Welchen neuen Eintrag möchten Sie vornehmen?")
            do_change = input("--> Möchten Sie die Änderung wirklich vornehmen? (ja oder nein)")

            if do_change == "ja":
                change_entry(index - 1, new_value)
                print("Die Position " + str(index) + " wurde erfolgreich von " + old_value + " zu " + new_value + " geändert!")
            elif do_change == "nein":
                print("Abgebrochen!")
            else:
                print("Falsche Eingabe")
        else:
            print("Diese Position ist nicht vergeben!")
    else:
        print("Bitte geben Sie eine Nummer an!")


def add_item():
    new_item = input("--> Welches Produkt wollen Sie dem Einkaufszettel hinzufügen?")
    answer = input("--> Möchten Sie " + new_item + " wirklich der Liste hinzufügen? (ja oder nein)")
    if new_entry == "ja":
        new_entry(new_item)
        print("Produkt %s wurde dem Einkaufszettel hinzugefügt" % new_item)
    elif answer == "nein":
        print("Abgebrochen!")


def delete_item():
    index = input("--> Welche Position möchten Sie löschen?")
    if index.isnumeric():
        index = int(index)
        lines = get_all_entries()
        if index <= len(lines):
            delete = input("--> Möchten Sie " + lines[index-1] + " an der Position " + str(index) + " wirklich löschen? (ja oder nein)")
            if delete == "ja":
                old_value = new_entry(index-1)
                delete_entry(index - 1)
                print(old_value + " an der Position " + str(index) + " wurde erfolgreich gelöscht!")
            elif delete == "nein":
                print("Abgebrochen!")
            else:
                print("falsche Eingabe")

        else:
            print("Diese Position ist nicht vergeben!")

    else:
        print("Bitte geben Sie eine Nummer an!")


def show_item():
    index = input("--> Welche Position möchten Sie anzeigen?")
    index = int(index)
    if index <= len(shopping_list):
        print("------------")
        print(str(index) + ": " + get_entry(index-1))
        print("------------")
    else:
        print("Diese Position ist nicht vergeben!")


def execute():
    while True:
        print("---------------------------------------------------------------------------------------------")
        x = input("Folgende Möglichkeiten: \n1: Liste anzeigen \n2: Position anzeigen \n3: Neuer Eintrag \n4: Eintrag ändern \n5: Eintrag löschen \n6: Beenden \n\nIhre Eingabe: ")

        if x == "Liste anzeigen" or x == "1":
            show_list()
        elif x == "Position anzeigen" or x == "2":
            show_item()
        elif x == "Neuer Eintrag" or x == "3":
            add_item()
        elif x == "Eintrag ändern" or x == "4":
            change_entry()
        elif x == "Eintrag löschen" or x == "5":
            delete_item()
        elif x == "Beenden" or x == "6":
            exit()
        else:
            print("Falsche Eingabe")


execute()
