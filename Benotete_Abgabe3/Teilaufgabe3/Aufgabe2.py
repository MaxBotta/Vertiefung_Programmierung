from blitzdb import Document
from blitzdb import FileBackend
import csv
from lxml import etree


# FRAGEN:
# 1. Werden auch die Seitenzahlen ausgewertet, die keine genaue Seitenzahl angeben (z.B. 315-330)?


db = FileBackend("../my-db")


class Inproceedings(Document):
    pass


def get_inproceedings_by_pages(article_length):
    # Alle Inproceedings in der DB (Nur der PK)
    inproceedings = db.filter(Inproceedings, {})
    list_of_inproceedings = []

    # Alle inproceedings durchgehen
    for inproceeding in inproceedings:
        try:
            # Seitenzahlen trennen
            pages = inproceeding.pages
            pages = pages.split("-")
            #print(pages)

            # Überprüfen, ob es zwei Angaben sind, wenn ja voneinander abziehen
            # und Anzahl der Seiten ermitteln
            if len(pages) > 1:
                # Überprüfen, ob beide Einträge valide Zahlen sind
                if pages[1].isdigit() and pages[0].isdigit():
                    number_of_pages = (int(pages[1]) - int(pages[0])) + 1

                    # Prüfen, ob es mehr als 10 Seiten sind, wenn ja, zur Liste hinzufügen
                    if number_of_pages >= article_length:
                        list_of_inproceedings.append(inproceeding)

        except AttributeError:
            print("No Pages Attribute")

    return list_of_inproceedings


def save_as_csv(filename, data):
    try:
        with open(filename + ".csv", "w", newline='', encoding="utf8") as file:
            fieldnames = ['author', 'title', 'pages', 'proc:editor', 'proc:title']
            writer = csv.DictWriter(file, fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(data)

    except IOError:
        print('An error occured trying to write the file.')


inproceedings_bigger_10 = get_inproceedings_by_pages(11)
save_as_csv("AufsätzeGroeßer10", inproceedings_bigger_10)

