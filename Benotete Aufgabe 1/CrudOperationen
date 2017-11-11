'''
In dieser Datei sollen die Lese- und Schreibzugriffe unseres Programms auf und in CSV-Dateien implementiert werden.
'''

import csv


dateiname = "tb01_FaelleGrundtabelleKreise_csv.csv"


def read(dateiname):
    with open(dateiname, newline='') as file:
        reader = csv.DictReader(file, skipinitialspace=True)
        list_of_dicts = []
        for v in reader:
            list_of_dicts.append(v)
        return list_of_dicts


def write(dateiname, list_of_dicts):
    with open(dateiname, "w", newline='',) as file:
        feldnamen=['Schluessel', 'Straftat', 'Gemeindeschluessel', 'Stadt-/Landkreis;Kreisart', 'erfasste Faelle', 'HZ nach Zensus;Versuche - Anzahl', 'Versuche - Anteil in %', 'mit Schusswaffe gedroht', 'mit Schusswaffe geschossen', 'aufgeklaerte Faelle', 'Aufklaerungsquote', 'Tatverdaechtige insgesamt', 'Tatverdaechtige - maennlich', 'Tatverdaechtige - weiblich', 'Nichtdeutsche Tatverdaechtige - Anzahl', 'Nichtdeutsche Tatverdaechtige - Anteil in %']
        writer = csv.DictWriter(file, feldnamen, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(list_of_dicts)
