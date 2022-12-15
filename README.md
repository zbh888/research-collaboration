# 848Final

[google doc](https://docs.google.com/document/d/1UbA1VX7uknfJQgKIziQlXUtxr1hfiIAStH54WKf0IOM/edit)

# DOI Collection

Based on Qlever

# Paper Collection

[PyPaperBot](https://github.com/ferru97/PyPaperBot) is a useful crawler. We didn't use it though since ACL has provided download API.

# Citation Impact Collection

[Semantic Scholar](https://www.semanticscholar.org) provided useful API.

# Affiliation Extraction

1. Follow the [link](https://grobid.readthedocs.io/en/latest/Install-Grobid/) to build grobid (I used gradle option)

2. Follow the [link](https://github.com/kermitt2/grobid_client_python) to install Python client server usage

3. In the directory from step-1, you should be able to use gradle to run the application. (Intellij would help).

4. After you run the application from step-3, the server should start locally. Check out http://localhost:8070

5. Go to the directory from step-2, run `python3 example.py`, the output would be in `resources/test_out`

We used NLP tool [Grobid](https://grobid.readthedocs.io/en/latest/) to extract information from pdf files.

# Classification

We provided two lists of affiliations, `industry.txt` and `academia.txt`

For academia affiliations, we also use keywords as filter [univerity, school, college]
