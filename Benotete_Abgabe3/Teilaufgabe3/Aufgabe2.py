from blitzdb import Document
from blitzdb import FileBackend
import csv
from lxml import etree


db = FileBackend("../my-db")


class Proceedings(Document):
        pass


class Inproceedings(Document):
    pass


def get_inproceedings_by_pages(pages):
    # Alle Inproceedings in der DB (Nur der PK)
    inproceedings = db.filter(Inproceedings, {})
    list_of_inproceedings = []

    for inproceeding in inproceedings:
        if inproceeding.pages.isdigit():
            if int(inproceeding.pages) >= pages:
                list_of_inproceedings.append(inproceeding)

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
print(inproceedings_bigger_10)
save_as_csv("AufsätzeGroeßer10", inproceedings_bigger_10)
