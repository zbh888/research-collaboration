import xml.etree.ElementTree as ET

# example: doiExtraction('test.xml)
def doiExtraction(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    res = []
    for affiliation in root.iter("{http://www.tei-c.org/ns/1.0}idno"):
        try:
            if affiliation.attrib['type'] == 'DOI':
                res.append(affiliation.text)
        except:
            print("ERROR: ", xml_file)
    return res
