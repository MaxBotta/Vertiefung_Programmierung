import xml.etree.ElementTree as ET


def read_ddi():
    elements = []
    tree = ET.parse('06551.xml')
    root = tree.getroot()

    # Studientitel:
    titel = {"Titel": root.find("docDscr/citation/titlStmt/titl").text.replace("\n\t\t", "")}
    elements.append(titel)

    # Beschreibung:
    beschreibung = {"Beschreibung": root.find("stdyDscr/stdyInfo/abstract").text.replace("\t\t", "")}
    elements.append(beschreibung)

    AllQuestions = []
    for frage in root.iter("var"):
        SingleQuestion = {}


        for fragetext in frage.iter("qstnLit"):
            t = str(fragetext.text).replace("\n\t\t", "")

            SingleQuestion["Fragetext"] = t

        SingleQuestion["Antworten"] = []
        for antworten in frage.iterfind("catgry/labl"):
            SingleQuestion["Antworten"].append(str(antworten.text).replace("\n\t\t", ""))

        if len(SingleQuestion['Antworten']) > 0:
            AllQuestions.append(SingleQuestion)

    #print(AllQuestions)
    print("--------------------TITEL:-----------------------------------------")
    print(elements[0]['Titel'] + "\n")
    print("--------------------BESCHREIBUNG:----------------------------------")
    print("  " + elements[1]['Beschreibung'] + "\n")
    print("--------------------FRAGEN MIT ANTWORTMÖGLICHKEITEN:---------------")

    counter = 0
    for quest in AllQuestions:
            if counter < 5:
                print("\n" + quest['Fragetext'])
                counter = counter + 1
                for antwort in quest['Antworten']:
                    print("   - " + antwort)








read_ddi()
