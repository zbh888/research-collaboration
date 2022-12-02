import requests
def downloadPDF_ACM(DOIs, path):
    failures = []
    headers = {
        "User-Agent": "Chrome/51.0.2704.103",
    }
    url = "https://dl.acm.org/doi/pdf/"
    for doi in DOIs:
        url_doi = url + doi
        response = requests.get(url_doi, headers=headers)
        if response.status_code == 200:
            with open(path + str(hash(doi))+'.pdf', "wb") as f:
                f.write(response.content)
            print('Success: ', url_doi)
        else:
            print('Error: ', url_doi)
            failures.append(doi)
    return failures
