shopping_list = ["Banane", "Apfel"]
file = open('list.txt', 'r+')

print("Name of the file: ", file.name)


def show_list():
    print("------------")
    #print("Einkaufszettel:")
    #print("")
    count = 0
    for v in shopping_list:
        print(count + 1, ": ", shopping_list[count])
        count = count + 1
    print("------------")
    execute()


def change_entry():
    index = input("--> Welche Position möchten Sie ändern?")

    if index.isnumeric():
        index = int(index)
        if index <= len(shopping_list):
            old_value = shopping_list[index-1]
            new_value = input("--> Welchen neuen Eintrag möchten Sie vornehmen?")
            do_change = input("--> Möchten Sie die Änderung wirklich vornehmen? (ja oder nein)")

            if do_change == "ja":
                shopping_list[index - 1] = new_value
                print("Die Position " + str(index) + " wurde erfolgreich von " + old_value + " zu " + new_value + " geändert!")
                execute()
            elif do_change == "nein":
                execute()
        else:
            print("Diese Position ist nicht vergeben!")
            execute()
    else:
        print("Bitte geben Sie eine Nummer an!")
        execute()


def add_item():
    new_item = input("--> Welches Produkt wollen Sie dem Einkaufszettel hinzufügen?")
    new_entry = input("--> Möchten Sie " + new_item + " wirklich der Liste hinzufügen? (ja oder nein)")
    if new_entry == "ja":
        shopping_list.append(new_item)
        print("Produkt %s wurde dem Einkaufszettel hinzugefügt" % new_item)
        execute()
    elif new_entry == "nein":
        execute()


def delete_item():
    index = input("--> Welche Position möchten Sie löschen?")
    if index.isnumeric():
        index = int(index)
        if index <= len(shopping_list):
            delete = input("--> Möchten Sie " + shopping_list[index-1] + " an der Position " + str(index) + " wirklich löschen? (ja oder nein)")
            if delete == "ja":
                old_value = shopping_list[index-1]
                del shopping_list[index-1]
                print(old_value + " an der Position " + str(index) + " wurde erfolgreich gelöscht!")
                execute()
            elif delete == "nein":
                execute()
            else:
                print("falsche Eingabe")
                execute()
        else:
            print("Diese Position ist nicht vergeben!")
            execute()
    else:
        print("Bitte geben Sie eine Nummer an!")
        execute()


def show_item():
    index = input("--> Welche Position möchten Sie anzeigen?")
    index = int(index)
    if index <= len(shopping_list):
        print("------------")
        print(str(index) + ": " + shopping_list[index-1])
        print("------------")
        execute()
    else:
        print("Diese Position ist nicht vergeben!")
        execute()


def execute():
    print("---------------------------------------------------------------------------------------------")
    x = input("Folgende Möglichkeiten: 1: Liste anzeigen, 2: Position anzeigen, 3: Neuer Eintrag, 4: Eintrag ändern, 5: Eintrag löschen, 6: Beenden")

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


execute()
