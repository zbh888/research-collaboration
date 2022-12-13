import requests
from bs4 import BeautifulSoup
import urllib.request
import time
import random

def getPDFTitles(URL):

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    job_elements = soup.find_all("a", class_="align-middle")
    pdfTitles = []

    for t in job_elements:
        if len(t["class"]) != 1:
            continue
        pdfTitles.append(t.text.strip())

    return pdfTitles

def getPDFurls(URL):

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    job_elements = soup.find_all("a", class_="badge badge-primary align-middle mr-1", href=True)
    pdfURLS = []

    for p in job_elements:
        pdfURLS.append(p['href'])

    return pdfURLS

def download_pdf(URL, dirPath, fileName):
    urllib.request.urlretrieve(URL, dirPath + fileName)

def getFilenames(pdfUrls):

    filenames = []
    for url in pdfUrls:
        index = url.find('.org/')
        filenames.append(url[index + 5:])

    return filenames

'''
urlist: set of urls which contains the pdfs
dirPath: path to your output directory where pdfs will be saved

'''

def main(urlList, dirPath):

    for url in urlList:
        pdfURLs = getPDFurls(url)
        filenames = getFilenames(pdfURLs)

        for i in range(len(pdfURLs)):
            download_pdf(pdfURLs[i], dirPath, filenames[i])
            time.sleep(random.randint(1,5))

if __name__ == '__main__':
    urlList = ['https://aclanthology.org/events/acl-2018/']
    dirPath = './ACL2018/'
    main(urlList, dirPath)
