import CrudOperationen
from operator import itemgetter


#Der Name der einzulesenden Datei
dateiname = "tb01_FaelleGrundtabelleKreise_csv.csv"

#Die Datei wird eingelesen und als Liste mehrerer Dictionaries im Speicher vorgehalten.
read = CrudOperationen.read(dateiname)

#Die Ergebnisliste der Aufgabe1-1
aufgabe1_1 = []

#Die Ergebnisliste der Aufgabe1-2
aufgabe1_2 = []


def landkreiseAufklärung():
    global aufgabe1_1
    #Die Schlüssel der Datensätze, die in der Ergebnisdatei gespeichert werden sollen.
    feldnamen=['Straftat', 'Stadt-/Landkreis', 'Aufklaerungsquote']
    for i in read:
        #Zunächst werden alle Landkreise ('LK') aus dem Gesamtdatensatz gefiltert...
        if i['Kreisart'] == "LK":
            #...und anschließend jene, mit einer Aufklärungsquote von über '50.0'.
            if float(i['Aufklaerungsquote']) >= 50.0:
                aufgabe1_1.append(i)
    #Die Ergebnisliste wird als Datei 'aufgabe1-1.csv' abgespeichert.
    CrudOperationen.write("aufgabe1-1.csv", aufgabe1_1, feldnamen)
    print("\n~~~~Speichern erfolgreich~~~~\n")


#landkreiseAufklärung()


def summeStraftaten():
    global aufgabe1_2
    '''ggf. Liste zunächst nach den Schluesseln sortieren
    sortiert = sorted(aufgabe1_2, key=itemgetter('Schluessel')) '''
    Summe = 0
    #Die Schlüssel der Datensätze, die in der Ergebnisdatei gespeichert werden sollen.
    feldnamen=['Straftat', 'Summe']
    #Der zuletzt ausgewertete Datensatz
    letzterDatensatz = {'Schluessel':''}
    for i in read:
        #Alle Straftaten, jedoch nicht die bereits kummulierten Werte.
        if i['Schluessel'] != "------":
            #Wenn die Straftat des betrachteten Eintrags die selbe ist, wie die des vorangegangen Datensatzes...
            if i['Schluessel'] == letzterDatensatz['Schluessel']:
                #...wird die Summe der Falldaten zu des bisherigen Summe addiert...
                Summe = Summe + int(i['erfasste Faelle'])
                #...und der aktuell betrachtete Datensatz als der zuletzt betrachtete abgespeichert.
                letzterDatensatz = i
            #Wenn die Straftat jedoch nicht die selbe ist...
            else:
                #...wird aus der bisher aufaddierten Summe ein neuer Summeneintrag erstellt und der Ergebnisliste hinzugefügt.
                neuerEintrag = {'Straftat': letzterDatensatz['Straftat'], 'Summe': Summe}
                aufgabe1_2.append(neuerEintrag)
                Summe = i['erfasste Faelle']
                letzterDatensatz = i
    #Am Ende der Datensätze muss noch die zuletzt erfasste Summe erfasst werden.
    neuerEintrag = {'Straftat': letzterDatensatz['Straftat'], 'Summe': Summe}
    aufgabe1_2.append(neuerEintrag)
    #Die Ergebnisliste wird als Datei 'aufgabe1-1.csv' abgespeichert.
    CrudOperationen.write("aufgabe1-2.csv", aufgabe1_2, feldnamen)
    print("\n~~~~Speichern erfolgreich~~~~\n")


summeStraftaten()


def sortiertSummeStraftaten():
    return


'''
while True:
    user_auswahl = input(
            "Bitte geben Sie Ziffer einer der nachfolgenden Optionen ein: \n1. Landkreise mit Aufklärungsquote < 50%, \n2. Summe aller erfassten Fälle je Straftat, \n3. Sortierte Summe aller erfassten Fälle je Straftat \n")
    if user_auswahl.isnumeric():
        auswahl_index = int(user_auswahl)
        if auswahl_index > 0 < 8:
            if auswahl_index == 1:
                landkreiseAufklärung()
            elif auswahl_index == 2:
                summeStraftaten()
            elif auswahl_index == 3:
                sortiertSummeStraftaten()
        else:
            print("Bitte geben Sie eine gültige Ziffer aus der Liste ein!")
    else:
        print("Bitte geben Sie eine gültige Ziffer aus der Liste ein!")
'''
