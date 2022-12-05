import xml.etree.ElementTree as ET

# example: affiliationExtraction("test.xml")

def affiliationExtraction(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    res = []
    for affiliation in root.iter("{http://www.tei-c.org/ns/1.0}affiliation"):
        affiliation_list = []
        for author_affiliation in affiliation:
            if author_affiliation.text.strip() != '':
                affiliation_list.append(author_affiliation.text)
        print(affiliation_list)
        res.append(affiliation_list)
    return res
