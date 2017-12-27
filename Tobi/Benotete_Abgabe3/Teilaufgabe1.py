from lxml import etree


#datei = './test.xml'
datei = './dblp-2017-05-02.xml'

#tag=('inproceedings', 'proceedings', 'journal')


def count_inproceedings_proceedings_journals():
    summe_inproceedings = 0
    summe_proceedings = 0
    summe_journals = 0

    context = etree.iterparse(datei, tag='inproceedings', events=('end', ), load_dtd=True, encoding='ISO-8859-1', huge_tree=True)

    for event, elem in context:
        summe_inproceedings = summe_inproceedings + 1
        print(summe_inproceedings)

        elem.clear()
        while elem.getprevious() is not None:
            del elem.getparent()[0]


            # if element.tag == 'inproceedings':
            #     summe_inproceedings = summe_inproceedings + 1
            #     element.clear()
            # elif element.tag == 'proceedings':
            #     summe_proceedings = summe_proceedings + 1
            #     element.clear()
            # elif element.tag == 'journal':
            #     summe_journals = summe_journals + 1
            #     element.clear()

    #print("inproceedings: " + str(summe_inproceedings) + ", proceedings: " + str(summe_proceedings) + ", journals: " + str(summe_journals))



count_inproceedings_proceedings_journals()
