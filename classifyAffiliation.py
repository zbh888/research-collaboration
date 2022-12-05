from affiliationExtraction import affiliationExtraction, getDOI
import os
import csv

def getSet(affiliations):
    affSet = set()
    for aff in affiliations:
        c_string = " ".join(aff).lower()
        affSet.add(c_string)

    return affSet

'''
This functions return '0' only if all the authors belong to academia. If not it returns '1'. '1' means either it is only
industry or hybrid. We need to manually classify them later.
'''
def isAcademia(affiliations):
    keywords = ['institute', 'university', 'school', 'college', 'department']
    for aff in affiliations:
        c_string = " ".join(aff).lower()
        check = False
        for k in keywords:
            if k in c_string:
                check = True
                break

        if not check:
            return '1'

    return '0'

def writeCSV(result, csvFilename):

    header = ['Title', 'DOI', 'Affiliations', 'Tag']
    filename = csvFilename

    with open(filename, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(result)

'''

xmlDirPath: is the relative path of the directory where you have all your XML files
csvFilename: name of the csv file name you want to write to

'''
def classifyAffiliations(xmlDirPath, csvFilename):

    result = []
    #A Formalization of the Security Features of Physical Functions.tei.xml
    for filename in os.listdir(xmlDirPath):

        complete_path_xml = xmlDirPath + filename

        affiliations = affiliationExtraction(complete_path_xml)
        doi = getDOI(complete_path_xml)
        title = filename[:-8]

        unique_affs = "-----".join(list(getSet(affiliations)))
        academia = isAcademia(affiliations)
        result.append([title, doi, unique_affs, academia])

    writeCSV(result,csvFilename)


classifyAffiliations('./testXML/', 'new.csv')


