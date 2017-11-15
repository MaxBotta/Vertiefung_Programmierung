'''
In dieser Datei sollen die Lese- und Schreibzugriffe unseres Programms auf und in CSV-Dateien implementiert werden.
'''

import csv


feldnamen=['Schluessel', 'Straftat', 'Gemeindeschluessel', 'Stadt-/Landkreis', 'Kreisart', 'erfasste Faelle', 'HZ nach Zensus;Versuche - Anzahl', 'Versuche - Anteil in %', 'mit Schusswaffe gedroht', 'mit Schusswaffe geschossen', 'aufgeklaerte Faelle', 'Aufklaerungsquote', 'Tatverdaechtige insgesamt', 'Tatverdaechtige - maennlich', 'Tatverdaechtige - weiblich', 'Nichtdeutsche Tatverdaechtige - Anzahl', 'Nichtdeutsche Tatverdaechtige - Anteil in %']


def read(dateiname):
    with open(dateiname, "r", newline='', encoding="utf8") as file:
        reader = csv.DictReader(file, delimiter=';')
        list_of_dicts = []
        for v in reader:
            list_of_dicts.append(v)
        return list_of_dicts


def write(dateiname, list_of_dicts, feldnamen):
    with open(dateiname, "w", newline='',) as file:
        writer = csv.DictWriter(file, feldnamen, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(list_of_dicts)



#print(read("tb01_FaelleGrundtabelleKreise_csv.csv")[0])
#print(read("/Users/maxbotta/PycharmProjects/Vertiefung_Programmierung/BenoteteAufgabe1/tb01_FaelleGrundtabelleKreise_csv.csv"))
