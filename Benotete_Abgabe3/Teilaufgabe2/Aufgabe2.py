from blitzdb import Document
from blitzdb import FileBackend
from lxml import etree


db = FileBackend("../my-db")


class Proceedings(Document):
        pass


class Inproceedings(Document):
    pass


# 1. Jedes Inproceeding-Objekt durchgehen
# 2. Entpsrechendes Proceedings-Objekt suchen
# 3. Proceedings Attribute dem Inproceedings-Objekt hinzufügen

def add_proceedings_to_inproceedings():
    # Alle Inproceedings in der DB (Nur der PK)
    inproceedings = db.filter(Inproceedings, {})

    # Jeden Crossref Verweis auslesen und hinzufügen
    counter = 0
    for item in inproceedings:
        counter = counter + 1
        # Inproceeding mit dem pk aus der DB holen
        inproceeding = db.get(Inproceedings, {'pk': str(item.pk)})

        # Mit dem crossref zutreffendes Proceeding Objekt suchen
        try:
            crossref = inproceeding.crossref
        except AttributeError:
            print("No Crossref found")

        try:
            proceeding = db.get(Proceedings, {'key': crossref})

            # Proceeding-Attribute zum Inproceeding hinzufügen
            for key in proceeding:
                inproceeding["proc:" + key] = proceeding[key]

            inproceeding.save()
            db.commit()

        except Proceedings.DoesNotExist:
            print("There is no Proceeding with the crossref: " + crossref)
        except Proceedings.MultipleDocumentsReturned:
            print("More than one Proceeding with the crossref: " + crossref)




add_proceedings_to_inproceedings()
