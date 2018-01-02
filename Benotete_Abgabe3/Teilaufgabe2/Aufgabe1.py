from blitzdb import Document
from blitzdb import FileBackend
from lxml import etree
from ..Teilaufgabe1.Aufgabe3 import *


db = FileBackend("./my-db")


class Proceedings(Document):
        pass


class Inproceedings(Document):
    pass


# Die XML-Datenbasis
#datei = './test.xml'
#datei = "./dblp-2017-05-02.xml"



# Teilaufgabe 2, Nr. 1
def get_inproceedings_by_year(datei, year):
    inproceedings = []
    # iterparser zum Einlesen der Datei unter Berücksichtigung ausschließlich der "End"-Events
    context = etree.iterparse(datei, events=('end', ), load_dtd=True, encoding='ISO-8859-1')
    # Iterieren über alle Elemente des Iterparser
    for event, elem in context:
        # Nochmals überprüfen, ob es sich um ein inproceedings handelt
        if elem.tag == "inproceedings":
            # Nur die inproceedings von 1980 hinzufügen
            if elem.find("year").text == year:
                jsn = convert_elements_into_dict(elem)
                inproceedings.append(jsn)

            # Aus dem Speicher entfernen, um diesen zu entlasten
            elem.clear()
            # danach werden die Referenzen auf das besuchte Elementes gelöscht
            while elem.getprevious() is not None:
                del elem.getparent()[0]

    return inproceedings


def get_all_proceedings(datei):
    proceedings = []
    context = etree.iterparse(datei, events=('end', ), load_dtd=True, encoding='ISO-8859-1')
    for event, elem in context:
        if elem.tag == "proceedings":
            jsn = convert_elements_into_dict(elem)
            proceedings.append(jsn)

            elem.clear()
            # danach werden die Referenzen auf das besuchte Elementes gelöscht
            while elem.getprevious() is not None:
                del elem.getparent()[0]

    return proceedings


def write_inproceedings_into_db(list_of_dicts):
    # Jeden Eintrag der übergebenen Liste in ein Object umwandeln und in die DB schreiben
    counter = 1
    for item in list_of_dicts:
        counter = counter + 1
        new_object = Inproceedings(item["inproceedings"])
        db.save(new_object)
    db.commit()
    print("Inproceedings eingetragen!")


def write_proceedings_into_db(list_of_dicts):
    # Jeden Eintrag der übergebenen Liste in ein Object umwandeln und in die DB schreiben
    counter = 1
    for item in list_of_dicts:
        counter = counter + 1
        new_object = Proceedings(item["proceedings"])
        db.save(new_object)
    db.commit()
    print("Proceedings eingetragen!")


# Proceedings und inproceedings von 1980 auslesen und hinterlegen
inproceedings_1980 = get_inproceedings_by_year(datei, "1980")
all_proceedings = get_all_proceedings(datei)

print("Inproceedings: " + str(len(inproceedings_1980)))
print("Proceedings: " + str(len(all_proceedings)))


# Die Listen in die DB eintragen
write_inproceedings_into_db(inproceedings_1980)
write_proceedings_into_db(all_proceedings)


