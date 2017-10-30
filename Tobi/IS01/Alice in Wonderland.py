def countinglines():
    with open(".\Alice.txt", encoding="utf8") as file:
        print("Zeilen: ")
        print(sum(1 for _ in file))


def countingcharacters():
    with open(".\Alice.txt", encoding="utf8") as file:
        print("Zeichen: ")
        zeichen = 0
        for line in file:
            #words ist eine liste der in einer zeile enthaltenen wörter
            words = line.split()
            #die länge eines jeden wortes ergibt die anzahl zeichen je zeile, dieser wert wird je zeile ausummiert und zur summe der zeichen hinzu addiert
            zeichen += sum(len(word) for word in words)
        print(zeichen)


countinglines()
countingcharacters()
