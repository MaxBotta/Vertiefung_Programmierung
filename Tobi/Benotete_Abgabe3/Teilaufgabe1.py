import json
from lxml import etree




#datei = './test.xml'
# Die XML-Datenbasis
datei = './dblp-2017-05-02.xml'
# die DTD-Datei der XML-Datenbasis, sie ermöglicht ein Validieren von XML-Elementen z.B. während des Parsens.
dtd = etree.DTD('./dblp-2017-03-29.dtd')


# TEILAUFGABE 1, NR. 1:
def count_inproceedings_proceedings_journals(datei):
    summe_inproceedings = 0
    summe_proceedings = 0
    summe_journals = 0
    # iterparser zum Einlesen der Datei unter Berücksichtigung ausschließlich der "End"-Events
    context = etree.iterparse(datei, events=('end', ), load_dtd=True, encoding='ISO-8859-1', huge_tree=True)
    # Iterieren über alle Elemente des Iterparser
    for event, elem in context:
        # das Auftreten der gesuchten Tags wird gezählt.
        if elem.tag == 'inproceedings':
            summe_inproceedings = summe_inproceedings + 1
        elif elem.tag == 'proceedings':
            summe_proceedings = summe_proceedings + 1
        elif elem.tag == 'journal':
            summe_journals = summe_journals + 1
        # anschließend wird der Inhalt des gelesenen Element aus dem Speicher gelöscht
        elem.clear()
        # danach werden die Referenzen auf das besuchte Elementes gelöscht
        while elem.getprevious() is not None:
            del elem.getparent()[0]
    print("inproceedings: " + str(summe_inproceedings) + ", proceedings: " + str(summe_proceedings) + ", journals: " + str(summe_journals))


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


# TEILAUFGABE 1, NR. 3:
def convert_the_first_3_inproceedings_and_proceedings_into_dict_and_save_as_readable_json(datei):
    counter_inproceedings = 0
    counter_proceedings = 0

    inproceedings = []
    proceedings = []

    # iterparser zum Einlesen der Datei unter Berücksichtigung ausschließlich der "End"-Events
    context = etree.iterparse(datei, events=('end', ), load_dtd=True, encoding='ISO-8859-1')
    # Iterieren über alle Elemente des Iterparser
    for event, elem in context:
        # die ersten drei inproceeding-elemente werden als subelemente des root elements hinzugefügt.
        if elem.tag == 'inproceedings' and counter_inproceedings < 3:
            counter_inproceedings = counter_inproceedings + 1
            jsn = convert_elements_into_dict(elem)
            inproceedings.append(jsn)
        elif elem.tag == "proceedings" and counter_proceedings < 3:
            counter_proceedings = counter_proceedings + 1
            jsn = convert_elements_into_dict(elem)
            proceedings.append(jsn)
        elif counter_inproceedings >= 3 and counter_proceedings >= 3:
            # sobald jeweils 3 Elemente zu den jeweiligen Listen hinzugefügt wurden, werden diese als JSON gespeichert.
            try:
                with open('sample_inproceedings.json', 'w') as outfile:
                    json.dump(inproceedings, outfile, indent=3)

            except IOError:
                print('An error occured trying to write the JSON file.')

            try:
                with open('sample_proceedings.json', 'w') as outfile:
                    json.dump(proceedings, outfile, indent=3)

            except IOError:
                print('An error occured trying to write the JSON file.')
            return





def convert_elements_into_dict(element):
    element_dict = {}
    child_elements = {}

    author = []
    editor = []

    # zunächst werden die Attribute des XML-Elements durchgegangen und jedes als Wertepaar in das Dictionary "child-elements" übernommen.
    # TODO klären ob die attribute in eine extra liste müssen...und ebenso mehrfach auftretende autoren/editor
    for attribut in element.items():
        child_elements[attribut[0]] = attribut[1]

    # anschließend werden alle Tags unter dem Element-Tag durchlaufen und zum "child-elements"-Dictionary hinzugefügt.
    for child in element.iterchildren():
        if child.getnext() is not None and child.getprevious() is None:
            if child.tag == child.getnext().tag:
                if element.tag == "inproceedings":
                    author.append(child.text)
                elif element.tag == "proceedings":
                    editor.append(child.text)
            else:
                child_elements[child.tag] = child.text
        elif child.getnext() is not None and child.getprevious() is not None:
            if child.tag == child.getnext().tag or child.tag == child.getprevious().tag:
                if element.tag == "inproceedings":
                    author.append(child.text)
                elif element.tag == "proceedings":
                    editor.append(child.text)
            else:
                child_elements[child.tag] = child.text
        elif child.getnext() is None and child.getprevious() is not None:
            if child.tag == child.getprevious().tag:
                if element.tag == "inproceedings":
                    author.append(child.text)
                elif element.tag == "proceedings":
                    editor.append(child.text)
            else:
                child_elements[child.tag] = child.text
    if len(author) > 0:
        child_elements['author'] = author
    if len(editor) > 0:
        child_elements['editor'] = editor

    # zuletzt wird das child-dictionary selbst zum value des element-dictionary, dieses repräsentiert ein inproceeding/proceeding-Element
    element_dict[element.tag] = child_elements
    return element_dict



#convert_the_first_3_inproceedings_and_proceedings_into_dict_and_save_as_readable_json(datei)
