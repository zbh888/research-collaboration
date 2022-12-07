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
