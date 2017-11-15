import xml.etree.ElementTree as ET
tree = ET.parse('movies.xml')
root = tree.getroot()

root.findall("titel")

for node in root.iter("Titel"):
    print(node.text)
