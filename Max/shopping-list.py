from Max.txt_crad import *


shopping_list = ["Banane", "Apfel"]


def show_list():
    print("------------")
    #print("Einkaufszettel:")
    #print("")
    count = 0
    lines = get_all_lines()
    for v in lines:
        print(count + 1, ": ", lines[count])
        count = count + 1
    print("------------")


def change_entry():
    index = input("--> Welche Position möchten Sie ändern?")

    if index.isnumeric():
        index = int(index)
        lines = get_all_lines()
        if index <= len(lines):
            old_value = lines[index-1]
            new_value = input("--> Welchen neuen Eintrag möchten Sie vornehmen?")
            do_change = input("--> Möchten Sie die Änderung wirklich vornehmen? (ja oder nein)")

            if do_change == "ja":
                change_line(index - 1, new_value)
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
    new_entry = input("--> Möchten Sie " + new_item + " wirklich der Liste hinzufügen? (ja oder nein)")
    if new_entry == "ja":
        set_line(new_item)
        print("Produkt %s wurde dem Einkaufszettel hinzugefügt" % new_item)
    elif new_entry == "nein":
        print("Abgebrochen!")


def delete_item():
    index = input("--> Welche Position möchten Sie löschen?")
    if index.isnumeric():
        index = int(index)
        lines = get_all_lines()
        if index <= len(lines):
            delete = input("--> Möchten Sie " + lines[index-1] + " an der Position " + str(index) + " wirklich löschen? (ja oder nein)")
            if delete == "ja":
                old_value = get_line(index-1)
                delete_line(index - 1)
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
        print(str(index) + ": " + get_line(index-1))
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
