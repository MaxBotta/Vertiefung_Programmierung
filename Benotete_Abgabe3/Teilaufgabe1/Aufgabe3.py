import json
from lxml import etree

# Die XML-Datenbasis
datei = '../dblp-2017-05-02.xml'


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
            break
    # sobald jeweils 3 Elemente zu den jeweiligen Listen hinzugefügt wurden, werden diese als JSON gespeichert.
    if len(inproceedings) > 0:
        try:
            with open('sample_inproceedings.json', 'w') as outfile:
                json.dump(inproceedings, outfile, indent=3)
        except IOError:
            print('An error occured trying to write the JSON file.')
    if len(proceedings) > 0:
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
    for attribut in element.items():
        child_elements[attribut[0]] = attribut[1]

    # anschließend werden alle Tags unter dem Element-Tag durchlaufen und zum "child-elements"-Dictionary hinzugefügt.
    for child in element.iterchildren():
        # bei inproceedings können die elemente "author" mehrfach auftreten, sie werden daher als liste strukturiert
        if element.tag == "inproceedings":
            if child.tag == "author":
                author.append(child.text)
            else:
                child_elements[child.tag] = child.text
        # bei proceedings können die elemente "editor" mehrfach auftreten, sie werden daher als liste strukturiert
        elif element.tag == "proceedings":
            if child.tag == "editor":
                editor.append(child.text)
            else:
                child_elements[child.tag] = child.text

    # anschließend werden die Listen mit den mehrfach auftretenden elementen zum dictionary der child-elemente hinzugefügt.
    if len(author) > 0:
        child_elements['author'] = author
    if len(editor) > 0:
        child_elements['editor'] = editor

    # zuletzt wird das child-dictionary selbst zum value des element-dictionary, dieses repräsentiert ein inproceeding/proceeding-Element
    element_dict[element.tag] = child_elements
    return element_dict


convert_the_first_3_inproceedings_and_proceedings_into_dict_and_save_as_readable_json(datei)
