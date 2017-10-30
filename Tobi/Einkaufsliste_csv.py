import csv_CRUD


def anzeigen(option):
    einkaufsliste = csv_CRUD.readfile()
    listenlaenge = len(einkaufsliste)
    if listenlaenge > 1:
        count = 0
        print("--------------------------------")
        print("  E I N K A U F S L I S T E ")
        for e in einkaufsliste:
            if count == 0:
                spacing = define_spacing(e[0], 12)
                print("    " + str(e[0]) + spacing + e[1])
            else:
                spacing = define_spacing(e[0], 12)
                print(str(count)+".  " + str(e[0]) + spacing + e[1])
            count += 1
        print("--------------------------------")
        if option == 1:
            return
    else:
        print("--------------------------------")
        print("Die Einkaufsliste ist leer")
        print("--------------------------------")


def define_spacing(string, spaltenbreite):
    laenge = len(string)
    spacing = ""
    while laenge <= spaltenbreite:
        leerzeichen = " "
        spacing = spacing + leerzeichen
        laenge = laenge + 1
    return spacing


def hinzufuegen():
    neue_bezeichnung = input("Bitte geben Sie die Bezeichnung des neuen Listeneintrags ein:")
    neue_menge = input("Bitte geben Sie die Menge des neuen Listeneintrags ein:")
    neuer_eintrag = [neue_menge, neue_bezeichnung]
    try:
        csv_CRUD.writefile(neuer_eintrag)
    except ValueError:
        print("Hinzufügen fehlgeschlagen")
    else:
        print("~~~Hinzufügen erfolgreich~~~")
        anzeigen(1)


def loeschen():
    anzeigen(2)
    einkaufsliste = csv_CRUD.readfile()
    loeschindex = input("Geben Sie die Nummer der Zutat ein, die Sie löschen wollen:\n")
    if loeschindex.isnumeric():
        loeschindex_int = int(loeschindex)
        if loeschindex_int > 0 and loeschindex_int < len(einkaufsliste):
            zeile = einkaufsliste[loeschindex_int]
            frage = input("Wollen Sie '" + str(zeile[1]) + "' löschen? (ja / nein)")
            if frage == "ja":

                csv_CRUD.deletefile(loeschindex_int)
                anzeigen(1)
                print("~~~Löschen erfolgreich~~~")

            else:
                print("~~~Löschen abgebrochen~~~")

        else:
            print("~~~Listennummer ausserhalb des Listenbereichs~~~")
            loeschen()
    else:
        print("~~~Fehlerhafte Eingabe~~~")
        loeschen()


def bearbeiten():
    anzeigen(3)
    einkaufsliste = csv_CRUD.readfile()
    bearbIndex = input("Geben Sie die Nummer der Zutat ein, die Sie bearbeiten wollen:\n")
    if bearbIndex.isnumeric():
        bearbIndex_int = int(bearbIndex)
        if bearbIndex_int > 0 and bearbIndex_int < len(einkaufsliste):
            listeneintrag = einkaufsliste[bearbIndex_int]
            print("Bisher haben Sie '" + listeneintrag[0] + " " + listeneintrag[1] + "' notiert.")

            bezeichnung = input("Auf welchen Wert wollen Sie '" + listeneintrag[1] + "' ändern?")
            menge = input("Auf welchen Wert wollen Sie '" + listeneintrag[0] + "' ändern?")
            csv_CRUD.changefile(bearbIndex_int, menge, bezeichnung)
            anzeigen(1)
        else:
            print("~~~Listennummer ausserhalb des Listenbereichs~~~")
            bearbeiten()
    else:
        print("~~~Fehlerhafte Eingabe~~~")
        bearbeiten()


def einzel_anzeigen():
    anzeigen(4)
    einkaufsliste = csv_CRUD.readfile()
    Index = input("Geben Sie die Nummer der Zutat ein, die Sie anzeigen lassen wollen:\n")
    if Index.isnumeric():
        anzIndex_int = int(Index)
        if anzIndex_int > 0 and anzIndex_int < len(einkaufsliste):
            zeile = einkaufsliste[anzIndex_int]
            print("-----------------------------\n")
            print("--->> " + zeile[0] + " " + zeile[1] + " <<---")
            print("\n-----------------------------")
        else:
            print("~~~Listennummer ausserhalb des Listenbereichs~~~")
            einzel_anzeigen()
    else:
        print("~~~Fehlerhafte Eingabe~~~")
        einzel_anzeigen()


while (True):
    auswahloptionen = ["Neuer Eintrag", "Liste Anzeigen", "Eintrag loeschen", "Eintrag bearbeiten",
                       "Eintrag anzeigen"]
    user_auswahl = input(
        "************************************************\nBitte geben Sie Ziffer einer der nachfolgenden Optionen ein: \n1. Neuer Eintrag, \n2. Liste Anzeigen, \n3. Eintrag loeschen, \n4. Eintrag bearbeiten, \n5. Eintrag anzeigen:\n")

    if user_auswahl.isnumeric():
        auswahl_index = int(user_auswahl) - 1
        if auswahl_index >= 0 and auswahl_index < len(auswahloptionen):
            if auswahl_index == 0:
                hinzufuegen()
            elif auswahl_index == 1:
                anzeigen(1)
            elif auswahl_index == 2:
                loeschen()
            elif auswahl_index == 3:
                bearbeiten()
            elif auswahl_index == 4:
                einzel_anzeigen()
        else:
            print("Bitte geben Sie eine gültige Ziffer aus der Liste ein!")
    else:
        print("Bitte geben Sie eine gültige Ziffer aus der Liste ein!")
