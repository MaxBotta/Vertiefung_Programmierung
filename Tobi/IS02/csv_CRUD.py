#Einen String als neue Zeile am Ende der Textdatei hinzufügen
def writefile(line):
    with open("einkaufsliste.csv", "a+") as file:
        if len(line) <= 2:
            anzahl = line[0]+";"
            bezeichnung = line[1]+"\n"
            file.write(anzahl)
            file.write(bezeichnung)
        else:
            return



'''#Eine Zeile der Textdatei als String zurückgeben.
def readline(l):
    with open(".\einkaufszettel.txt") as file:
        lines = []
        for line in file:
            line = line.rstrip()
            lines.append(line)
    if l>=0 and l < len(lines):
        result = lines[l]
        return result
    else:
        return
        '''


#Alle Zeilen der Textdatei als mehrdimensionale Liste zurückgeben.
def readfile():
    with open("einkaufsliste.csv") as file:
        lines = []
        for line in file:
            line = line.rstrip()
            spalten = line.split(";")
            lines.append(spalten)
    return lines


#Die Werte einer spezifischen Zeile abändern.
def changefile(index, anzahl, bezeichnung):
    lines = readfile()
    if index > 0 and index < len(lines):
        zeile = lines[index]
        zeile[0] = anzahl
        zeile[1] = bezeichnung
        lines[index] = zeile
        with open("einkaufsliste.csv", "w") as file:
            for v in lines:
                if len(v[1])<=15:
                    file.write(str(v[0])+";")
                    file.write(v[1]+"\n")
                    print("~~~Bearbeiten erfolgreich~~~")
                else:
                    print("Bitte weniger als 16 Zeichen eingeben")


#Eine spezifische Zeile aus der csv-datei löschen.
def deletefile(index):
    lines = readfile()
    if index > 0 and index < len(lines):
        del lines[index]
        with open("einkaufsliste.csv", "w") as file:
            for v in lines:
                file.write(str(v[0])+";")
                file.write(v[1]+"\n")


'''
def input_validation(item):
    valid_item = True
    if item.isalpha():
        if item.isdigit():
            valid_item = False
        elif item == "":
            valid_item = False
        return valid_item


def amount_input_validation(amount):
    valid_item = True
    if amount.isdigit() is False:
        valid_item = False
    return valid_item
'''
