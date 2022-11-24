from scidownl import scihub_download

def downloadPDF_sci(DOIs, path):
    source = []
    for doi in DOIs:
        source.append((doi, 'doi', path))
    for paper, paper_type, out in source:
        scihub_download(paper, paper_type=paper_type, out=out)
