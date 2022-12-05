import xml.etree.ElementTree as ET
import xml.dom.minidom

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
        res.append(affiliation_list)
    return res

def getDOI(xml_file):
    docs = xml.dom.minidom.parse(xml_file)

    idnos = docs.getElementsByTagName("idno")

    for i in idnos:
        if i .getAttribute("type") == "DOI":
            return i.firstChild.nodeValue

    return ""

