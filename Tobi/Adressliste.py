import AdresslisteCRUD

while True:
    user_auswahl = input(
            "************************************************\nBitte geben Sie Ziffer einer der nachfolgenden Optionen ein: \n1. Neuer Eintrag, \n2. Kontakte suchen, \n3. Eintrag ändern, \n4. Eintrag löschen, \n5. Alle Kontakte anzeigen, \n6. Adressbuch aus CSV-Datei laden,\n 6. Adressbuch als CSV-Datei speichern:\n")

    if user_auswahl.isnumeric():
        auswahl_index = int(user_auswahl) - 1
        if auswahl_index >= 0 and auswahl_index < len(auswahloptionen):
            if auswahl_index == 0:

            elif auswahl_index == 1:

            elif auswahl_index == 2:

            elif auswahl_index == 3:

            elif auswahl_index == 4:

        else:
            print("Bitte geben Sie eine gültige Ziffer aus der Liste ein!")
    else:
        print("Bitte geben Sie eine gültige Ziffer aus der Liste ein!")
