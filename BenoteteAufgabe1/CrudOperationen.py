'''
In dieser Datei sollen die Lese- und Schreibzugriffe unseres Programms auf und in CSV-Dateien implementiert werden.
'''

import csv



feldnamen=['Schluesse', 'Straftat', 'Gemeindeschluessel', 'Stadt-/Landkreis', 'Kreisart', 'erfasste Faelle', 'HZ nach Zensus;Versuche - Anzahl', 'Versuche - Anteil in %', 'mit Schusswaffe gedroht', 'mit Schusswaffe geschossen', 'aufgeklaerte Faelle', 'Aufklaerungsquote', 'Tatverdaechtige insgesamt', 'Tatverdaechtige - maennlich', 'Tatverdaechtige - weiblich', 'Nichtdeutsche Tatverdaechtige - Anzahl', 'Nichtdeutsche Tatverdaechtige - Anteil in %']


def read(dateiname):
    #Die CSV-Datei wird eingelesen.
    with open(dateiname, "r", newline='', encoding='Windows-1252') as file:
        temp = file.readlines()
        final = []
        #Die Zeilen der Datei werden auf die Zeichenfolge '1;2;3;4' untersucht.
        for line in temp:
            if not "1;2;3;4" in line:
                final.append(line)
        #Alle Zeilen ohne diese Zeichenfolge werden der Erstellung einer DictReader-Instanz übergeben.
        reader = csv.DictReader(final, delimiter=';')
        list_of_dicts = []
        #Die einzelnen Datensätze (Dictionaries) werden zu einer Liste hinzugefügt.
        for v in reader:
                list_of_dicts.append(v)
        return list_of_dicts





def write(dateiname, list_of_dicts, feldnamen):
    with open(dateiname, "w", newline='',) as file:
        writer = csv.DictWriter(file, feldnamen, delimiter=';', extrasaction='ignore')
        writer.writeheader()
        writer.writerows(list_of_dicts)

