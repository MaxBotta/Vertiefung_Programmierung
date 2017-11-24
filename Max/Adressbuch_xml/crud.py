import csv
import json
import os
import xml.etree.ElementTree as ET


def read_json(path):
    try:
        with open(path) as file:
            data = json.load(file)
            return data
    except IOError:
        print('An error occured trying to read the JSON file.')


def read_xml(path):
    try:
        contacts = []
        tree = ET.parse(path)
        root = tree.getroot()

        # Die einzelnen Attribute durchgehen und dem Dict hinzufügen.
        for contact in root.iter("Kontakt"):
            new_contact = {}
            new_contact["Anrede"] = contact.find("Anrede").text
            new_contact["Vorname"] = contact.find("Vorname").text
            new_contact["Name"] = contact.find("Name").text
            new_contact["Straße"] = contact.find("Straße").text
            new_contact["Hausnummer"] = contact.find("Hausnummer").text
            new_contact["PLZ"] = contact.find("PLZ").text
            new_contact["Stadt"] = contact.find("Stadt").text

            # Rufnummern durchgehen und dem Dict als Liste hinzufügen.
            new_contact["Rufnummern"] = []
            for number in contact.iter("Rufnummer"):
                new_contact["Rufnummern"].append({"Typ": number.get("Typ"), "Nummer": number.text})

            # E-Mail-Adressen durchgehen und dem Dict als Liste hinzufügen.
            new_contact["E-Mail-Adressen"] = []
            for email in contact.iter("E-Mail"):
                new_contact["E-Mail-Adressen"].append({"Typ": email.get("Typ"), "E-Mail": email.text})

            # Den Kontakt zur Liste "contacts" hinzufügen.
            contacts.append(new_contact)

        return contacts

    except IOError:
        print('An error occured trying to read the XML file.')


def write(path, data):
    try:
        with open(path, 'w') as outfile:
            json.dump(data, outfile, indent=4)

    except IOError:
        print('An error occured trying to write the file.')


def get_all_json_and_xml():
    # Liste mit sämtlichen Dateien ertsellen, die sich im selben Ordner befinden.
    dir_list = os.listdir('.')
    new_list = []
    # Jeden Dateinamen mit der Endung '.csv' oder '.json' der Liste new_list hinzufügen.
    for file in dir_list:
        if file.find(".json") > -1:
            new_list.append(file)
        if file.find(".xml") > -1:
            new_list.append(file)

    index = 0
    for file in new_list:
        index = index + 1
        print("  " + str(index) + ": " + file)
    return new_list

