#Einen String als neue Zeile am Ende der Textdatei hinzufügen
def writefile(string):
    with open(".\einkaufszettel.txt", "a+") as file:
        writestring = string+"\n"
        file.write(writestring)


#Eine Zeile der Textdatei als String zurückgeben.
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


#Alle Zeilen der Textdatei als Liste zurückgeben.
def readfile():
    with open(".\einkaufszettel.txt") as file:
        lines = []
        for line in file:
            line = line.rstrip()
            lines.append(line)
    return lines


#Den Wert einer spezifischen Zeile abändern.
def changefile(index, string):
    lines = readfile()
    lines[index] = string
    with open(".\einkaufszettel.txt", "w") as file:
        for v in lines:
            file.write(v+"\n")


#Eine spezifische Zeile aus der Textdatei löschen.
def deletefile(index):
    lines = readfile()
    del lines[index]
    with open(".\einkaufszettel.txt", "w") as file:
        for v in lines:
            file.write(v+"\n")

