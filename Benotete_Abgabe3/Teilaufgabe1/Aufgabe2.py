import json
from lxml import etree


# Die XML-Datenbasis
datei = '../dblp-2017-05-02.xml'
# die DTD-Datei der XML-Datenbasis, sie ermöglicht ein Validieren von XML-Elementen z.B. während des Parsens.
dtd = etree.DTD('../dblp-2017-03-29.dtd')


# TEILAUFGABE 1, NR. 2:
def read_the_first_3_proceedings_and_inproceedings(datei):
    counter_inproceedings = 0
    counter_proceedings = 0

    inproceedings_root = etree.Element('dblp')
    proceedings_root = etree.Element('dblp')
    inproceedings_tree = etree.ElementTree(inproceedings_root)
    proceedings_tree = etree.ElementTree(proceedings_root)

    # iterparser zum Einlesen der Datei unter Berücksichtigung ausschließlich der "End"-Events
    context = etree.iterparse(datei, events=('end', ), load_dtd=True, encoding='ISO-8859-1')
    # Iterieren über alle Elemente des Iterparser
    for event, elem in context:
        # die ersten drei inproceeding-elemente werden als subelemente des root elements hinzugefügt.
        if elem.tag == 'inproceedings' and counter_inproceedings < 3:
            counter_inproceedings = counter_inproceedings + 1
            inproceedings_root.append(elem),
        # die ersten drei proceeding-elemente werden als subelemente des root elements hinzugefügt.
        elif elem.tag == "proceedings" and counter_proceedings < 3:
            counter_proceedings = counter_proceedings + 1
            proceedings_root.append(elem)

        elif counter_inproceedings >= 3 and counter_proceedings >= 3:
            break
    # sobald jeweils 3 Elemente zu den jeweiligen ElementTrees hinzugefügt wurden, werden diese gegen die DTD validiert.
    if dtd.validate(inproceedings_tree) and dtd.validate(proceedings_tree):

        # Wenn die Validierungen "True" zurückgeben, werden die Elemente in die jeweiligen xml-Dateien geschrieben.
        # Grundsätzlich sind durch den Parameter "load_dtd=True" beim Parsen schon alle Elemente validiert, hier werden jedoch zusätzlich ggf. vorgenommene Änderungen validiert.
        with open('sample_inproceedings.xml', 'wb') as ausgabe1:
            inproceedings_tree.write(ausgabe1, pretty_print=True, xml_declaration=True, encoding='ISO-8859-1', doctype="<!DOCTYPE dblp SYSTEM 'dblp-2017-03-29.dtd'>")

        with open('sample_proceedings.xml', 'wb') as ausgabe2:
            proceedings_tree.write(ausgabe2, pretty_print=True, xml_declaration=True, encoding='ISO-8859-1', doctype="<!DOCTYPE dblp SYSTEM 'dblp-2017-03-29.dtd'>")
        return
    else:
        print("Validierung fehlgeschlagen!")
        print(dtd.error_log.filter_from_errors())
        return


read_the_first_3_proceedings_and_inproceedings(datei)
