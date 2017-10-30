import os


def new_entry(item, value):
    with open("./Max/files/list.csv", "a") as f:
        f.write(item + ";" + value + "\n")


def delete_entry(i):
    result = []
    with open("./Max/files/list.csv", "r") as file:
        # Text in Lines speichern
        lines = file.readlines()
        for v in lines:
            v = v.rstrip()
            entry = v.split(";")
            result.append(entry)

    with open("./Max/files/list.csv", "w") as file:
        # Zeile aus Array löschen und file überschreiben
        del result[i]
        for v in result:
            file.write(v[0] + ";" + v[1] + "\n")


def change_entry(i, item, value):
    result = []
    with open("./Max/files/list.csv", "r") as file:
        # Text in Lines speichern
        lines = file.readlines()
        for v in lines:
            v = v.rstrip()
            entry = v.split(";")
            result.append(entry)

    with open("./Max/files/list.csv", "w") as file:
        # Zeile an Stelle i ändern und file überschreiben
        result1[i] = [item, value]
        for v in result:
            file.write(v[0] + ";" + v[1] + "\n")


def get_entry(i):
    result = []
    with open("./Max/files/list.csv", "r") as file:
        # Text in Lines speichern
        lines = file.readlines()
        for v in lines:
            v = v.rstrip()
            entry = v.split(";")
            result.append(entry)

    return result[i]


def get_all_entries():
    result = []
    with open("./Max/files/list.csv", "r") as file:

        # Text in Array speichern
        lines = file.readlines()
        for v in lines:
            v = v.rstrip()
            entry = v.split(";")
            result.append(entry)

    return result


def open_file():
    os.system("open " + "./Max/files/list.csv")
