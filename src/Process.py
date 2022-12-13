from Extraction import *
import os

def processXML(outputPath):
    # data[0] file name
    # data[1] title
    # data[2] doi
    # data[3] affiliation
    data = []
    missing_affiliation = []
    for filename in os.listdir(outputPath):
        oneData = []
        if filename.endswith(".xml"):
            name = filename[:-8]
            oneData.append(name)
            aff = affiliationExtraction(outputPath + filename)
            doi = doiExtraction(outputPath + filename)
            title = titleExtraction(outputPath + filename)
            if len(aff) == 0:
                missing_affiliation.append(name)
            else:
                if len(title) == 0:
                    oneData.append(title)
                else:
                    if title[0] is not None:
                        oneData.append([title[0]])
                    else:
                        oneData.append([])
                oneData.append(doi)
                oneData.append(aff)
                data.append(oneData)
    return data, missing_affiliation
