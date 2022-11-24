from Query import query, collectDoi
from scihubDownload import downloadPDF
res = query(2021, 2021 ,"IEEE Symposium on Security and Privacy")
doi = collectDoi(res)
downloadPDF(doi, './papers/')