# Open a file


def set_line(text):
    with open("list.txt", "a") as f:
        f.write(text + "\n")


def delete_line(i):
    lines = []
    with open("list.txt", "r") as file:

        # Text in Array speichern
        text = file.readlines()
        for v in text:
            v = v.rstrip()
            lines.append(v)

        print(lines)

    with open("list.txt", "w") as file:
        # Zeile aus Array löschen und file überschreiben
        del lines[i]
        for v in lines:
            file.write(v + "\n")


def get_line(i):
    lines = []
    with open("list.txt", "r") as file:
        text = file.readlines()
        for v in text:
            v = v.rstrip()
            lines.append(v)

    return lines[i-1]


set_line("Hallo")
set_line("Tschüss")
#delete_line(0)
