from blitzdb import Document
from blitzdb import FileBackend
import csv
from lxml import etree


db = FileBackend("../my-db")

class Inproceedings(Document):
    pass


def get_inproceedings_by_editor(wanted_editor):

    # Versuch durch ein Query die Editor Liste durchzugehen, $elemMatch wird nicht supported!
    #inproceedings = db.filter(Inproceedings, {"proc:editor": {"$elemMatch": {wanted_editor}}})
    #print(inproceedings)

    # Gibt alle Inproceedings zurück
    inproceedings = db.filter(Inproceedings, {})
    list_of_inproceedings = []

    for inproceeding in inproceedings:
        #print(inproceeding)

        # Alle Editors durchgehen und prüfen, ob dieser vorhanden ist
        try:
            editors = inproceeding["proc:editor"]
            # Prüfen, ob es eine Liste, wenn ja Liste durchgehen
            if type(editors) == list:
                for editor in editors:
                    if editor == wanted_editor:
                        list_of_inproceedings.append(inproceeding)
            elif editors == wanted_editor:
                list_of_inproceedings.append(inproceeding)

        except KeyError:
            pass
            #print("No editors attribute in inproceeding: " + str(inproceeding.pk))
        except AttributeError:
            pass
            #print("No editors attribute in inproceeding: " + str(inproceeding.pk))

    return list_of_inproceedings


inproceedings_from_MichaelBrodie = get_inproceedings_by_editor("Piotr Dembinski")
print(inproceedings_from_MichaelBrodie)