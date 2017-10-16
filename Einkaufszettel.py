shopping_list = ["Banane", "Apfel"]
#file = open('list.txt', 'r+')


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
                del shopping_list[index-1]
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


def execute():
    print("---------------------------------------------------------------------------------------------")
    x = input("Folgende Möglichkeiten: Liste anzeigen, Neuer Eintrag, Eintrag ändern, Eintrag löschen, beenden")

    if x == "Liste anzeigen":
        show_list()
    elif x == "Neuer Eintrag":
        add_item()
    elif x == "Eintrag ändern":
        change_entry()
    elif x == "Eintrag löschen":
        delete_item()
    elif x == "beenden":
        exit()
    else:
        print("Falsche Eingabe")
        execute()


execute()
