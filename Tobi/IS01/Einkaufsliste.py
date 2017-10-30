import file_CRUD

def anzeigen(option):
    einkaufsliste = file_CRUD.readfile()
    listenlaenge = len(einkaufsliste)
    if listenlaenge > 0:
        count = 0
        print("-----------------------------")
        print(" E I N K A U F S L I S T E ")
        for e in einkaufsliste:
            print("  " + str(count+1) + ". " + einkaufsliste[count])
            count += 1
        print("-----------------------------")
        if option == 1:
            return
    else:
        print("-----------------------------")
        print("Die Einkaufsliste ist leer")
        print("-----------------------------")



def hinzufuegen():
    neuer_eintrag = input("Bitte geben Sie den neuen Eintrag ein:")
    try:
        file_CRUD.writefile(neuer_eintrag)
    except ValueError:
        print("Hinzufügen fehlgeschlagen")
    else:
        print("~~~Hinzufügen erfolgreich~~~")
        anzeigen(1)


def loeschen():
    anzeigen(2)
    einkaufsliste = file_CRUD.readfile()
    loeschindex = input("Geben Sie die Nummer der Zutat ein, die Sie löschen wollen:\n")
    if loeschindex.isnumeric():
        loeschindex_int = int(loeschindex)-1
        if loeschindex_int >= 0 and loeschindex_int < len(einkaufsliste):
            frage = input("Wollen Sie " + einkaufsliste[loeschindex_int] + " löschen? (ja / nein)")
            if frage == "ja":

                file_CRUD.deletefile(loeschindex_int)
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
    einkaufsliste = file_CRUD.readfile()
    bearbIndex = input("Geben Sie die Nummer der Zutat ein, die Sie bearbeiten wollen:\n")
    if bearbIndex.isnumeric():
        bearbIndex_int = int(bearbIndex)-1
        if bearbIndex_int >= 0 and bearbIndex_int < len(einkaufsliste):
            frage = input("Auf welchen Wert wollen Sie '" + einkaufsliste[bearbIndex_int] + "' ändern?")
            file_CRUD.changefile(bearbIndex_int, frage)
            print("~~~Bearbeiten erfolgreich~~~")
            anzeigen(1)
        else:
            print("~~~Listennummer ausserhalb des Listenbereichs~~~")
            bearbeiten()
    else:
        print("~~~Fehlerhafte Eingabe~~~")
        bearbeiten()


def einzel_anzeigen():
    anzeigen(4)
    einkaufsliste = file_CRUD.readfile()
    Index = input("Geben Sie die Nummer der Zutat ein, die Sie anzeigen lassen wollen:\n")
    if Index.isnumeric():
        anzIndex_int = int(Index)-1
        if anzIndex_int >= 0 and anzIndex_int < len(einkaufsliste):
            print("-----------------------------\n")
            print("--->> " + einkaufsliste[anzIndex_int] + " <<---")
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
