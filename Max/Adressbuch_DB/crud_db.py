from tinydb import TinyDB, Query

datenbank = TinyDB('db.json')


def write_single(anrede, name, vorname, strasse, hausnummer, plz, stadt, rufnummern, emails):
    datenbank.insert({
        "Anrede": anrede,
        "Name": name,
        "Vorname": vorname,
        "Straße": strasse,
        "Hausnummer": hausnummer,
        "PLZ": plz,
        "Stadt": stadt,
        "Rufnummern": rufnummern,
        "E-Mail-Adressen": emails
    })


def get_len():
    try:
        return len(datenbank)
    except IOError:
        print("Fehler beim Suchen eines Kontakts.")


def write(contact):
    try:
        datenbank.insert(contact)
    except IOError:
        print("Fehler beim Hinzufügen eines Kontakts.")


def get_all():
    try:
        return datenbank.all()

    except IOError:
        print("Fehler beim Laden aller Kontakte.")


def search_by_id(id):
    try:
        contact = datenbank.get(doc_id=id)
        if contact is not None:
            return contact
        else:
            return -1
    except IOError:
        print("Fehler beim Suchen eines Kontakts.")


def update(contact):
    try:
        contact_id = [contact.doc_id]
        return datenbank.update(contact, doc_ids=contact_id)
    except IOError:
        print("Fehler beim Ändern eines Kontakts.")


def delete(id):
    try:
        contact_id = [id]
        datenbank.remove(doc_ids=contact_id)
    except IOError:
        print("Fehler beim Löschen des Kontakts.")


def search_by_name(name):
    result_list = []
    kontakte = Query()
    try:
        for kontakt in datenbank.search((kontakte['Vorname'].search(name)) | (kontakte['Name'].search(name))):
            result_list.append(kontakt)
        if len(result_list) > 0:
            return result_list
        else:
            return -1
    except IOError:
        print("Fehler beim Suchen von Kontakten.")



print(search_by_name("Botta"))
