from blitzdb import Document
from blitzdb import FileBackend
import csv
from lxml import etree


db = FileBackend("../my-db")


class Inproceedings(Document):
    pass


def get_all_authors_and_inproceedings():
    # Alle Inproceedings in der DB (Nur der PK)
    inproceedings = db.filter(Inproceedings, {})
    list_of_inproceedings = []
    list_of_authors = []

    # Alle inproceedings durchgehen und Autoren eintragen
    count = 0
    for inproceeding in inproceedings:
        count = count + 1
        print(count)
        # Alle Authoren durchgehen
        # Exception Handling falls ein inproceeding kein "author" Attribut besitzt
        try:
            # Autoren aus Inproceeding lesen
            for author in inproceeding.author:
                # Überprüfen, ob der Autor schon in der Liste ist, ansonsten eintragen
                # Falls die Liste noch leer ist, wird der erste Eintrag vorgenommen
                if len(list_of_authors) == 0:
                    list_of_authors.append({"author": author, "inproceedings": 1})

                else:
                    # Überprüfen, ob ein solcher Autor bereits existiert.
                    # Sollte der Autor ncoh nicht in der Liste sein, wird er angelegt
                    # Ist der Autor bereits eingetragen, werden seine Aufsätze um 1 erhöht
                    for item in list_of_authors:

                        #  Autor ist noch nicht angelegt
                        if item["author"] == author:
                            item["inproceedings"] = item["inproceedings"] + 1

                        # Ist der Autor bereits in der Liste, wird die Anzahl der Inproceedings um 1 erhöht
                        else:
                            list_of_authors.append({"author": author, "inproceedings": 1})


        except AttributeError:
            print("No Author Attribute")

    return list_of_authors


def get_all_authors():
    # Alle Inproceedings in der DB (Nur der PK)
    inproceedings = db.filter(Inproceedings, {})
    list_of_inproceedings = []
    list_of_authors = []

    # Alle inproceedings durchgehen und Autoren eintragen
    count = 0
    for inproceeding in inproceedings:
        count = count + 1
        print(count)
        # Alle Authoren durchgehen
        # Exception Handling falls ein inproceeding kein "author" Attribut besitzt
        try:
            # Autoren aus Inproceeding lesen
            for author in inproceeding.author:
                # Überprüfen, ob der Autor schon in der Liste ist, ansonsten eintragen
                if not author in list_of_authors:
                    list_of_authors.append(author)

        except AttributeError:
            print("No Author Attribute")

    return list_of_authors


def add_inproceedings_to_authors(authors):
    inproceedings = db.filter(Inproceedings, {})
    authors_and_inproceedings = []

    # authors in ein dict überführen
    for author in authors:
        authors_and_inproceedings.append({"author": author, "count": 0})

    # Für alle Autoren die Inproceedings zählen
    for author in authors_and_inproceedings:
        for inproceeding in inproceedings:
            # Überprüfen, ob der Autor in diesem Inproceeding genannt wird
            # Exception Handling falls ein inproceeding kein author Attribut besitzt
            try:
                if author["author"] in inproceeding["author"]:
                    # Falls der Autor genannt wird, wird die Anzahl der Aufsätze erhöht
                    author["count"] = author["count"] + 1
                    print("added!")

            except AttributeError:
                #print("No Author Attribute")
                pass

            except KeyError:
                #print("No Author Attribute")
                pass

    # List sortieren
    sorted_list = sorted(authors_and_inproceedings, key=lambda k: k['count'], reverse=True)

    return sorted_list


def save_as_csv(filename, data):
    try:
        with open(filename + ".csv", "w", newline='', encoding="utf8") as file:
            fieldnames = ['author', 'count']
            writer = csv.DictWriter(file, fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(data)

    except IOError:
        print('An error occured trying to write the file.')


list_of_authors = get_all_authors()
authors_and_inproceedings = add_inproceedings_to_authors(list_of_authors)
#print(list_of_authors)
print(authors_and_inproceedings)

save_as_csv("authors_and_count", authors_and_inproceedings)
