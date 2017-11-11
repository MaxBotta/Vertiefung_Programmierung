import AdresslisteCRUD


kontakte = []
dateiname = ""


def neuerEintrag():
    Anrede = input("Bitte geben Sie die Anrede ein (max. 20 Zeichen):")
    Name = input("Bitte geben Sie den Nachnamen ein (max. 20 Zeichen):")
    Vorname = input("Bitte geben Sie den Vornamen ein (max. 20 Zeichen):")
    Straße = input("Bitte geben Sie die Straße ein (max. 20 Zeichen):")
    Hausnummer = input("Bitte geben Sie die Hausnummer ein (max. 20 Zeichen):")
    PLZ = input("Bitte geben Sie die PLZ ein (max. 20 Zeichen):")
    Stadt = input("Bitte geben Sie die Stadt ein (max. 20 Zeichen):")
    Telefon_1 = input("Bitte geben Sie die Telefonnummer ein (max. 20 Zeichen):")
    Telefon_2 = input("Bitte geben Sie die zweite Telefonnummer ein (max. 20 Zeichen):")
    Email = input("Bitte geben Sie die Email-Adresse ein (max. 20 Zeichen):")
    neuerKontakt = {'Anrede': Anrede[:19], 'Name': Name[:19], 'Vorname': Vorname[:19], 'Straße': Straße[:19], 'Hausnummer': Hausnummer[:19], 'PLZ': PLZ[:19], 'Stadt': Stadt[:19], 'Telefon 1': Telefon_1[:19], 'Telefon 2': Telefon_2[:19], 'Email': Email[:19]}

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
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        header = listOfDicts[0].keys()
        rowcounter = 0
        print("     ", end="")
        for i in header:
            print(i + define_spacing(i, 20), end="")
        print("")
        for v in listOfDicts:
            print("")
            rowcounter = int(rowcounter) + 1
            values = v.values()
            print(str(rowcounter) + define_spacing(rowcounter, 4), end="")
            for s in values:
                print(s[:21] + define_spacing(s, 20), end="")
        print("")
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    else:
        print("\n~~~~Die Kontaktliste ist leer~~~~\n")
        return


def define_spacing(string, spaltenbreite):
    laenge = len(str(string))
    spacing = ""
    while laenge <= spaltenbreite:
        leerzeichen = " "
        spacing = spacing + leerzeichen
        laenge = laenge + 1
    return spacing


def aendernEintrag():
    if len(kontakte)>0:
        alleAnzeigen(kontakte)
        auswahl = input("Bitte geben Sie die Listennummer des Eintrags an, den Sie ändern wollen:\n")
        if auswahl.isnumeric():
            aus = int(auswahl)
            if aus > 0 and aus <= len(kontakte):
                change = kontakte[aus - 1]
                Anrede = input("Auf welchen Wert wollen Sie die Anrede '" + change['Anrede'] + "' ändern? (max. 20 Zeichen, überspringen mit ENTER):")
                Name = input("Auf welchen Wert wollen Sie den Nachnamen '"+ change['Name'] +"' ändern? (max. 20 Zeichen, überspringen mit ENTER):")
                Vorname = input("Auf welchen Wert wollen Sie den Vornamen '"+ change['Vorname'] + "' ändern?(max. 20 Zeichen, überspringen mit ENTER):")
                Straße = input("Auf welchen Wert wollen Sie die Straße '" + change['Straße'] + "' ändern? (max. 20 Zeichen, überspringen mit ENTER):")
                Hausnummer = input("Auf welchen Wert wollen Sie die Hausnummer '" + change['Hausnummer'] + "' ändern?  (max. 20 Zeichen, überspringen mit ENTER):")
                PLZ = input("Auf welchen Wert wollen Sie die PLZ '" + change['PLZ'] + "' ändern?  (max. 20 Zeichen, überspringen mit ENTER):")
                Stadt = input("Auf welchen Wert wollen Sie die Stadt '" + change['Stadt'] + "' ändern?  (max. 20 Zeichen, überspringen mit ENTER):")
                Telefon_1 = input("Auf welchen Wert wollen Sie die Telefonnummer '" + change['Telefon 1'] + "' ändern?  (max. 20 Zeichen, überspringen mit ENTER):")
                Telefon_2 = input("Auf welchen Wert wollen Sie die zweite Telefonnummer '" + change['Telefon 2'] + "' ändern?  (max. 20 Zeichen, überspringen mit ENTER):")
                Email = input("Auf welchen Wert wollen Sie die Email-Adresse '" + change['Email'] + "' ändern?  (max. 20 Zeichen, überspringen mit ENTER):")
                if len(Anrede) > 0:
                    change['Anrede'] = Anrede[:19]
                if len(Name) > 0:
                    change['Name'] = Name[:19]
                if len(Vorname) > 0:
                    change['Vorname'] = Vorname[:19]
                if len(Straße) > 0:
                    change['Straße'] = Straße[:19]
                if len(Hausnummer) > 0:
                    change['Hausnummer'] = Hausnummer[:19]
                if len(PLZ) > 0:
                    change['PLZ'] = PLZ[:19]
                if len(Stadt) > 0:
                    change['Stadt'] = Stadt[:19]
                if len(Telefon_1) > 0:
                    change['Telefon 1'] = Telefon_1[:19]
                if len(Telefon_2) > 0:
                    change['Telefon 2'] = Telefon_2[:19]
                if len(Email) > 0:
                    change['Email'] = Email[:19]
                kontakte[aus - 1] = change
                print("\n~~~~Änderung erfolgreich~~~~\n")
            else:
                print("\n~~~~Fehlerhafte Eingabe~~~~\n")
        else:
            print("\n~~~~Fehlerhafte Eingabe~~~~\n")
    else:
        print("\n~~~~Die Kontaktliste ist leer~~~~\n")


def loeschenEintrag():
    if len(kontakte)>0:
        alleAnzeigen(kontakte)
        auswahl = input("Bitte geben Sie die Listennummer des Eintrags an, den Sie löschen wollen:\n")
        if auswahl.isnumeric():
            aus = int(auswahl)
            if aus > 0 and aus <= len(kontakte):
                delete = kontakte[aus - 1]
                show = []
                show.append(delete)
                alleAnzeigen(show)
                ruckfrage = input("Wollen Sie den angezeigten Kontakt wirklich löschen? (ja/nein):")
                if ruckfrage == "ja":
                    del kontakte[aus - 1]
                    print("\n~~~~Löschen erfolgreich~~~~\n")
                else:
                    print("\n~~~~Löschen verworfen~~~~\n")
            else:
                print("\n~~~~Fehlerhafte Eingabe~~~~\n")
        else:
            print("\n~~~~Fehlerhafte Eingabe~~~~\n")
    else:
        print("\n~~~~Die Kontaktliste ist leer~~~~\n")


def loadAdressbuch():
    fragenstatus = True
    while fragenstatus:
        csv = AdresslisteCRUD.getAllCSV()
        auswahl = input("Welche CSV-Datei wollen Sie laden? ('0' für Abbrechen)\n")
        if auswahl.isnumeric():
            t = int(auswahl)
            if t == 0:
                return
            elif t > 0 and t <= len(csv):
                global dateiname
                dateiname = csv[t-1]
                global kontakte
                kontakte = AdresslisteCRUD.read(dateiname)
                print("\n~~~~Die Datei wurde geladen~~~~\n")
                return
            else:
                print("\n~~~~Fehlerhafte Eingabe~~~~\n")
        else:
            print("\n~~~~Fehlerhafte Eingabe~~~~\n")


def saveAdressbuch():
    global dateiname
    if len(dateiname) > 0:
        auswahl = input("Sie haben die Adressliste '" + dateiname + "' geöffnet. Wollen Sie die Änderungen in dieser Datei speichern? (ja/nein)")
        if auswahl == "ja":
            AdresslisteCRUD.write(dateiname, kontakte)
            print("\n~~~~Speichern erfolgreich~~~~\n")
        else:
            name = input("Bitte geben Sie einen Dateinamen ein: \n")
            dateiname = name + ".csv"
            AdresslisteCRUD.write(dateiname, kontakte)
            print("\n~~~~Speichern erfolgreich~~~~\n")
    else:
        name = input("Bitte geben Sie einen Dateinamen ein:\n")
        dateiname = name + ".csv"
        AdresslisteCRUD.write(dateiname, kontakte)
        print("\n~~~~Speichern erfolgreich~~~~\n")


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
                aendernEintrag()
            elif auswahl_index == 4:
                loeschenEintrag()
            elif auswahl_index == 5:
                alleAnzeigen(kontakte)
            elif auswahl_index == 6:
                loadAdressbuch()
            elif auswahl_index == 7:
                saveAdressbuch()
        else:
            print("Bitte geben Sie eine gültige Ziffer aus der Liste ein!")
    else:
        print("Bitte geben Sie eine gültige Ziffer aus der Liste ein!")
