def new_entry(item, value):
    with open("./files/list.csv", "a") as f:
        f.write(item + ";" + value + "\n")


def delete_entry(i):
    result = []
    with open("./files/list.csv", "r") as file:
        # Text in Lines speichern
        lines = file.readlines()
        for v in lines:
            v = v.rstrip()
            entry = v.split(";")
            result.append(entry)

    with open("./files/list.csv", "w") as file:
        # Zeile aus Array löschen und file überschreiben
        del result[i]
        for v in result:
            file.write(v[0] + ";" + v[1] + "\n")


def change_entry(i, item, value):
    result = []
    with open("./files/list.csv", "r") as file:
        # Text in Lines speichern
        lines = file.readlines()
        for v in lines:
            v = v.rstrip()
            entry = v.split(";")
            result.append(entry)

    with open("./files/list.csv", "w") as file:
        # Zeile an Stelle i ändern und file überschreiben
        lines[i] = [item, value]
        for v in result:
            file.write(v[0] + ";" + v[1] + "\n")


def get_entry(i):
    result = []
    with open("./files/list.csv", "r") as file:
        # Text in Lines speichern
        lines = file.readlines()
        for v in lines:
            v = v.rstrip()
            entry = v.split(";")
            result.append(entry)

    return result[i-1]


def get_all_entries():
    result = []
    with open("./files/list.csv", "r") as file:

        # Text in Array speichern
        lines = file.readlines()
        for v in lines:
            v = v.rstrip()
            entry = v.split(";")
            result.append(entry)

    return result


print(get_all_entries())
