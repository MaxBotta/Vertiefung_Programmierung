import os


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
    with open("alice.txt", "r") as file:
        text = file.readlines()
        for v in text:
            v = v.rstrip()
            lines.append(v)

    return lines[i-1]


def get_all_lines():
    lines = []
    with open("alice.txt", "r") as file:

        # Text in Array speichern
        text = file.readlines()
        for v in text:
            v = v.rstrip()
            lines.append(v)

    return lines


def create_file(path, name):
    open(path + "/" + name + ".txt", "w")


def open_file(path):
    os.system("open " + path)


def get_lines_characters_dots():
    lines = 0
    characters = 0
    dots = 0
    with open("alice.txt", "r") as file:
        text = file.readlines()
        lines = len(text)

    with open("alice.txt", "r") as file:
        text = file.read()
        characters = len(text)
        dots = text.count(".")

    return lines, characters, dots


# print(str(len(get_all_lines())))
#result = get_lines_characters_dots()
#print("Zeilen: " + str(result[0]))
#print("Zeichen: " + str(result[1]))
#print("Punkte: " + str(result[2]))

# create_file("/users/maxbotta/PycharmProjects/Vertiefung_Programmierung/files", "beispiel")
# open_file("/users/maxbotta/desktop/beispiel.txt")
open_file("./files/beispiel.txt")
