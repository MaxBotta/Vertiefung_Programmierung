import xml.etree.ElementTree as ET
import os


def check_if_file_exists(filename):
    dir_list = os.listdir('.')
    for file in dir_list:
        if file == filename:
            return True
    return False


def check_if_xml(filename):
    if filename.find(".xml") > -1:
        return True
    return False


def load_file():
    while True:
        filename = input("Geben Sie einen Dateinamen ein: ")
        try:
            if check_if_file_exists(filename):
                if check_if_xml(filename):
                    tree = ET.parse(filename)
                    root = tree.getroot()
                    print("Datei geladen!")
                    return tree
                else:
                    print("Die angegebene Datei ist kein XML!")
            else:
                print("Die angegebene Datei existiert nicht!")

        except IOError:
            print('Beim lesen der Datei ist ein Fehler aufgetreten!')


def print_data(root):
    while True:
        xpath = input("\nGeben Sie einen X-Path ein: ")
        try:
            for item in root.findall(xpath):
                print(item.tag + ": " + item.text)

        except IOError:
            print("Falsche Syntax")





tree = load_file()
print_data(tree)
