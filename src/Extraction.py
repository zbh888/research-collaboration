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

from PyPDF2 import PdfFileWriter, PdfFileReader
import os

# example extractFirstPage('./papers/')
def extractFirstPage(path):
    p = path+'FirstPage/'
    os.mkdir(p)
    pdf_files = []
    for filename in os.listdir(path):
        if filename.endswith(".pdf"):
            pdf_files.append(filename)
    pdf_files.sort(key=str.lower)


    for filename in pdf_files:
        try:
            reader = PdfFileReader(path + filename, strict = False)
            writer = PdfFileWriter()
            page = reader.getPage(0)
            writer.addPage(page)

            with open(p + filename, "wb") as fp:
                writer.write(fp)
        except:
            print("ERROR:", path + filename)




