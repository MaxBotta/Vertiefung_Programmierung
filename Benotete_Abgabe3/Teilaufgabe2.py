from blitzdb import Document
from blitzdb import FileBackend
from lxml import etree
from Benotete_Abgabe3.Teilaufgabe1 import *


db = FileBackend("./my-db")


class Inproceedings(Document):
    pass


class Proceedings(Document):
    pass


# Die XML-Datenbasis
datei = './test.xml'
# die DTD-Datei der XML-Datenbasis, sie ermöglicht ein Validieren von XML-Elementen z.B. während des Parsens.
dtd = etree.DTD('./dblp-2017-03-29.dtd')


# Teilaufgabe 2, Nr. 1
def get_inproceedings_by_year(datei, year):
    inproceedings = []
    # iterparser zum Einlesen der Datei unter Berücksichtigung ausschließlich der "End"-Events
    context = etree.iterparse(datei, events=('end', ), load_dtd=True, encoding='ISO-8859-1')
    # Iterieren über alle Elemente des Iterparser
    for event, elem in context:
        # Die inproceeding-elemente werden als subelemente des root elements hinzugefügt.
        if elem.tag == 'inproceedings':

            # Nur die inproceedings von 1980 hinzufügen
            if elem.find("year").text == year:
                jsn = convert_elements_into_dict(elem)
                inproceedings.append(jsn)

    return inproceedings


def get_proceedings_by_year(datei, year):
    proceedings = []
    # iterparser zum Einlesen der Datei unter Berücksichtigung ausschließlich der "End"-Events
    context = etree.iterparse(datei, events=('end', ), load_dtd=True, encoding='ISO-8859-1')
    # Iterieren über alle Elemente des Iterparser
    for event, elem in context:
        # Die proceeding-elemente werden als subelemente des root elements hinzugefügt.
        if elem.tag == 'proceedings':

            # Nur die proceedings von 1980 hinzufügen
            if elem.find("year").text == year:
                jsn = convert_elements_into_dict(elem)
                proceedings.append(jsn)

    return proceedings


def write_inproceedings_into_db(list_of_dicts):
    # Jeden Eintrag der übergebenen Liste in ein Object umwandeln und in die DB schreiben
    for item in list_of_dicts:
        new_object = Inproceedings(item["inproceedings"])
        db.save(new_object)
        db.commit()


def write_proceedings_into_db(list_of_dicts):
    # Jeden Eintrag der übergebenen Liste in ein Object umwandeln und in die DB schreiben
    for item in list_of_dicts:
        new_object = Proceedings(item["proceedings"])
        db.save(new_object)
        db.commit()

# Proceedings und inproceedings von 1980 auslesen und hinterlegen
proceedings_1980 = get_proceedings_by_year(datei, "1980")
inproceedings_1980 = get_inproceedings_by_year(datei, "1980")

# Die Listen in die DB eintragen
write_inproceedings_into_db(inproceedings_1980)
write_proceedings_into_db(proceedings_1980)


