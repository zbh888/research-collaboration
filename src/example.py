from grobid_client.grobid_client import GrobidClient
from Extraction import *
from Process import *
from Citation import *
import os

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
