import xml.etree.ElementTree as ET


def xml_to_list_of_dicts():
    contacts = []
    tree = ET.parse('adressbuch.xml')
    root = tree.getroot()

    # Die einzelnen Attribute durchgehen und dem Dict hinzufügen.
    for contact in root.iter("Kontakt"):
        new_contact = {}
        new_contact["Anrede"] = contact.find("Anrede").text
        new_contact["Vorname"] = contact.find("Vorname").text
        new_contact["Name"] = contact.find("Name").text
        new_contact["Straße"] = contact.find("Straße").text
        new_contact["hausnummer"] = contact.find("Hausnummer").text
        new_contact["plz"] = contact.find("PLZ").text
        new_contact["stadt"] = contact.find("Stadt").text

        # Rufnummern durchgehen und dem Dict als Liste hinzufügen.
        new_contact["Rufnummern"] = []
        for number in contact.iter("Rufnummer"):
            new_contact["Rufnummern"].append({"Typ": number.get("Typ"), "Nummer": number.text})

        # E-Mail-Adressen durchgehen und dem Dict als Liste hinzufügen.
        new_contact["E-Mail-Adressen"] = []
        for email in contact.iter("Rufnummer"):
            new_contact["E-Mail-Adressen"].append({"Typ": number.get("Typ"), "E-Mail": number.text})

        # Den Kontakt zur Liste "contacts" hinzufügen.
        contacts.append(new_contact)

    return contacts


contacts = xml_to_list_of_dicts()
print(contacts)
