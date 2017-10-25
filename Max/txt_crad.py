def new_entry(text):
    with open("./files/shopping-list.txt", "a") as f:
        f.write(text + "\n")


def delete_entry(i):
    lines = []
    with open("./files/shopping-list.txt", "r") as file:

        # Text in Array speichern
        text = file.readlines()
        for v in text:
            v = v.rstrip()
            lines.append(v)

    with open("./files/shopping-list.txt", "w") as file:
        # Zeile aus Array löschen und file überschreiben
        del lines[i]
        for v in lines:
            file.write(v + "\n")


def change_entry(i, value):
    lines = []
    with open("./files/shopping-list.txt", "r") as file:

        # Text in Array speichern
        text = file.readlines()
        for v in text:
            v = v.rstrip()
            lines.append(v)

    with open("./files/shopping-list.txt", "w") as file:
        # Zeile an Stelle i ändern und file überschreiben
        lines[i] = value
        for v in lines:
            file.write(v + "\n")


def get_entry(i):
    lines = []
    with open("./files/shopping-list.txt", "r") as file:
        text = file.readlines()
        for v in text:
            v = v.rstrip()
            lines.append(v)

    return lines[i-1]


def get_all_entries():
    lines = []
    with open("./files/shopping-list.txt", "r") as file:

        # Text in Array speichern
        text = file.readlines()
        for v in text:
            v = v.rstrip()
            lines.append(v)

    return lines

