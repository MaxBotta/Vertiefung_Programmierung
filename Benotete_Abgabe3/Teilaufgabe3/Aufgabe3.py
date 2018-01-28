from blitzdb import Document
from blitzdb import FileBackend
import csv


db = FileBackend("../my-db")


class Inproceedings(Document):
    pass


def get_authors_and_count():
    # Alle Inproceedings in der DB (Nur der PK)
    inproceedings = db.filter(Inproceedings, {})
    list_of_authors = []

    for inproceeding in inproceedings:
        try:
            for author in inproceeding.author:
                # Überprüfen, ob der Autor existiert
                # Beim ersten mal ist die Liste leer und der Autor wird einfach eingetragen
                if len(list_of_authors) == 0:
                        list_of_authors.append({"author": author, "count": 1})
                else:
                    # Liste durchgehen und schauen ob der Autor schon existiert
                    author_exists = False
                    for item in list_of_authors:
                        if item["author"] == author:
                            item["count"] = item["count"] + 1
                            author_exists = True
                            break

                    # Falls der Autor noch nicht in der Liste ist, wird er hinzugefügt
                    if not author_exists:
                        list_of_authors.append({"author": author, "count": 1})
                        print(author)

        except AttributeError:
            #print("No Author Attribute")
            pass

    # List sortieren
    sorted_list = sorted(list_of_authors, key=lambda k: k['count'], reverse=True)
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


author_and_count = get_authors_and_count()
save_as_csv("author_and_count", author_and_count)
