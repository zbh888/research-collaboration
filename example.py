from Query import query, collectDoi
from scihubDownload import downloadPDF_sci
from acmDownload import downloadPDF_ACM
res = query(2021, 2021 ,"IEEE Symposium on Security and Privacy")
doi = collectDoi(res)
downloadPDF_sci(doi, './papers/')
downloadPDF_ACM(doi, './papers/')
