import BenoteteAufgabe1.Teilaufgabe2 as aufgabe2
import BenoteteAufgabe1.Teilaufgabe1 as aufgabe1


def execute():
    welcome = True
    while True:
        if welcome:
            print("-------------------------------------------------------------------------------------------")
            print("      0000  0000  0     000  0000  0000       0000  0  0  ")
            print("      0  0  0  0  0      0   0     0          0  0  0  0  ")
            print("      0000  0  0  0      0   0     0000       0000  0000  ")
            print("      0     0  0  0      0   0     0             0     0  ")
            print("      0     0000  0000  000  0000  0000          0     0  ")
            print("-------------------------------------------------------------------------------------------")
            welcome = False

        dateiname = ""
        if aufgabe2.path == "":
            dateiname = "Keine Datei ausgewählt!"
        else:
            dateiname = aufgabe2.path

        print("\nMENÜ")
        print("------------------------------------------------------------------------------------------")

        print("Datei: " + dateiname + "    Einträge: " + str(len(aufgabe2.data)))
        print("------------------------------------------------------------------------------------------")
        print("1: CSV-Datei Laden    2: Liste anzeigen    3: Suchen von Daten    4: Filtern von Daten")
        print("5: Landkreise mit Aufklärungsquote < 50%   6: Summen aller erfassten Fälle je Straftat")
        print("7: Absteigend sortierte Summen aller erfassten Fälle je Straftat")
        print("8: Beenden")

        x = input("\nIhre Eingabe: ")
        print("")

        if x == "1":
            aufgabe2.get_files()
        elif x == "2":
            aufgabe2.show_result(aufgabe2.data)
        elif x == "3":
            aufgabe2.suchen_von_daten(aufgabe2.data)
        elif x == "4":
            aufgabe2.filtern_von_daten(aufgabe2.data)
        elif x == "5":
            aufgabe1.landkreiseAufklärung(aufgabe2.data)
        elif x == "6":
            aufgabe1.summeStraftaten(aufgabe2.data)
        elif x == "7":
            aufgabe1.sortiertSummeStraftaten(aufgabe2.data)
        elif x == "8":
            exit()
        else:
            print("Falsche Eingabe")


execute()
