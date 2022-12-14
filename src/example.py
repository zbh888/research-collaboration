from grobid_client.grobid_client import GrobidClient
from Extraction import *
from Process import *
from Citation import *
import os

def write_csv(finaldata):
    with open('result.csv', 'a') as the_file:
        the_file.write('File,Title,DOI,AFF,Citation,Date\n')
    for data in finaldata:
        string = []
        string.append(data[0])
        if len(data[1]) == 0:
            string.append('')
        else:
            string.append(str(data[1][0]).replace(',', ' '))
        
        if len(data[2]) == 0:
            string.append('')
        else:
            string.append(str(data[2][0]))
        string.append('-----'.join(data[3]).replace(',', ' '))
        string.append(str(data[4]))
        string.append(str(data[5]))
        ','.join(string)
        with open('result.csv', 'a') as the_file:
            the_file.write(','.join(string) + '\n')

PATH = './CL/'
extractFirstPage(PATH)
firstPagePath = PATH + 'FirstPage'
outputPath = PATH + 'Result/'

if not os.path.exists(outputPath):
    os.makedirs(outputPath)

client = GrobidClient(config_path="./config.json")
client.process("processFulltextDocument", firstPagePath, output=outputPath, consolidate_citations=True, tei_coordinates=True, force=True)

data, missing_affiliation = processXML(outputPath)
finalData, missing_citations = getCitationPublication(data)
write_csv(finalData)
