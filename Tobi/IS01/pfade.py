def writerelativepath(string):
    with open("..\Anderer Ordner\Datei.txt", "a+") as file:
        writestring = string+"\n"
        file.write(writestring)


def writeabsolutepath(string):
    with open("D:\Übungsdownloads\Anderer Ordner\Datei.txt", "a+") as file:
        writestring = string+"\n"
        file.write(writestring)


writerelativepath("relativ")
writeabsolutepath("absolut")
