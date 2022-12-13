import xml.etree.ElementTree as ET

# example: affiliationExtraction("test.xml")

import xml.etree.ElementTree as ET
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

def doiExtraction(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    res = []
    for affiliation in root.iter("{http://www.tei-c.org/ns/1.0}idno"):
        try:
            if affiliation.attrib['type'] == 'DOI':
                res.append(affiliation.text)
        except:
            ;
    return res

def titleExtraction(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    res = []
    for title in root.iter("{http://www.tei-c.org/ns/1.0}title"):
        res.append(title.text)
    return res




