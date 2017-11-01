import AdresslisteCRUD


kontakte = []
kontakte = AdresslisteCRUD.read()


def neuerEintrag():
    Anrede = input("Bitte geben Sie die Anrede ein (max. 7 Zeichen):")
    Name = input("Bitte geben Sie den Nachnamen ein (max. 20 Zeichen):")
    Vorname = input("Bitte geben Sie den Vornamen ein (max. 15 Zeichen):")
    Straße = input("Bitte geben Sie die Straße ein (max. 20 Zeichen):")
    Hausnummer = input("Bitte geben Sie die Hausnummer ein (max. 10 Zeichen):")
    PLZ = input("Bitte geben Sie die PLZ ein (max. 7 Zeichen):")
    Stadt = input("Bitte geben Sie die Stadt ein (max. 20 Zeichen):")
    Telefon_1 = input("Bitte geben Sie die Telefonnummer ein (max. 15 Zeichen):")
    Telefon_2 = input("Bitte geben Sie die zweite Telefonnummer ein (max. 15 Zeichen):")
    Email = input("Bitte geben Sie die Email-Adresse ein (max. 20 Zeichen):")
    neuerKontakt = {'Anrede': Anrede[:7], 'Name': Name[:20], 'Vorname': Vorname[:15], 'Straße': Straße[:20], 'Hausnummer': Hausnummer[:11], 'PLZ': PLZ[:7], 'Stadt': Stadt[:20], 'Telefon 1': Telefon_1[:15], 'Telefon 2': Telefon_2[:15], 'Email': Email[:20]}

    temp = []
    temp.append(neuerKontakt)
    alleAnzeigen(temp)
    ruckfrage = input("Wollen Sie den angezeigten Kontakt in ihre Kontaktliste übernehmen? (ja/nein):")
    if ruckfrage == "ja":
        kontakte.append(neuerKontakt)
    else:
        print("\n~~~~Kontaktdaten verworfen~~~~\n")


def kontaktSuchen():
    fragenstatus = True

    while fragenstatus:
        name = input("Wollen Sie nach Vor- oder Nachname suchen?\n1. Vorname\n2. Nachname\n3. Abrechen\n")
        if name.isnumeric():
            if name == "1":
                vorname = input("Bitte geben Sie den Vornamen ein:\n")
                ergebnis = getSuchresultate(1, vorname)
                if len(ergebnis) > 0:
                    alleAnzeigen(ergebnis)
                else:
                    print("\n~~~~Suche ergab keine Treffer~~~~\n")
                fragenstatus = False
            elif name == "2":
                nachname = input("Bitte geben Sie den Nachnamen ein:\n")
                ergebnis = getSuchresultate(2, nachname)
                if len(ergebnis) > 0:
                    alleAnzeigen(ergebnis)
                else:
                    print("\n~~~~Suche ergab keine Treffer~~~~\n")
                fragenstatus = False
            elif name == "3":
                return
            else:
                print("\n~~~~Fehlerhafte Eingabe~~~~\n")
        else:
            print("\n~~~~Fehlerhafte Eingabe~~~~\n")


def getSuchresultate(option, suchbegriff):
    ergebnis = []
    if option == 1:
        for v in kontakte:
            if suchbegriff.lower() in v['Vorname'].lower():
                ergebnis.append(v)
    elif option == 2:
        for v in kontakte:
            if suchbegriff.lower() in v['Name'].lower():
                ergebnis.append(v)
    return ergebnis





def alleAnzeigen(listOfDicts):
    if len(listOfDicts) > 0:
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        header = listOfDicts[0].keys()
        counter = 0
        different_spaces = [7, 20, 15, 20, 11, 7, 20, 15, 15, 20]
        for i in header:
            print(i + define_spacing(i, different_spaces[counter]), end="")
            counter = counter + 1
        print("")
        for v in listOfDicts:
            print("")
            values = v.values()
            counter = 0
            for s in values:
                print(s + define_spacing(s, different_spaces[counter]), end="")
                counter = counter + 1
        print("")
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    else:
        print("\n~~~~Die Kontaktliste ist leer~~~~\n")
        return


def define_spacing(string, spaltenbreite):
    laenge = len(string)
    spacing = ""
    while laenge <= spaltenbreite:
        leerzeichen = " "
        spacing = spacing + leerzeichen
        laenge = laenge + 1
    return spacing


while True:
    user_auswahl = input(
            "Bitte geben Sie Ziffer einer der nachfolgenden Optionen ein: \n1. Neuer Eintrag, \n2. Kontakte suchen, \n3. Eintrag ändern, \n4. Eintrag löschen, \n5. Alle Kontakte anzeigen, \n6. Adressbuch aus CSV-Datei laden,\n7. Adressbuch als CSV-Datei speichern:\n")
    if user_auswahl.isnumeric():
        auswahl_index = int(user_auswahl)
        if auswahl_index > 0 < 8:
            if auswahl_index == 1:
                neuerEintrag()
            elif auswahl_index == 2:
                kontaktSuchen()
            elif auswahl_index == 3:
                print("hallo welt")
            elif auswahl_index == 4:
                print("hallo welt")
            elif auswahl_index == 5:
                alleAnzeigen(kontakte)
            elif auswahl_index == 6:
                print("hallo welt")
            elif auswahl_index == 7:
                print("hallo welt")
        else:
            print("Bitte geben Sie eine gültige Ziffer aus der Liste ein!")
    else:
        print("Bitte geben Sie eine gültige Ziffer aus der Liste ein!")
