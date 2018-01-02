from lxml import etree


# Die XML-Datenbasis
datei = '../dblp-2017-05-02.xml'


# TEILAUFGABE 1, NR. 1:
def count_inproceedings_proceedings_journals(datei):
    print("Zählung läuft, bitte warten...")
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


count_inproceedings_proceedings_journals(datei)
