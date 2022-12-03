import requests
from collections import defaultdict

'''
Input: DOI
Return: total citation count. If paper with DOI is not found, None is returned.
'''
def getTotalCitations(DOI):

    URL = 'https://api.semanticscholar.org/graph/v1/paper/'
    QUERY = '?fields=citationCount'
    response = requests.get(URL + DOI + QUERY)
    JSON = response.json()

    if 'citationCount' in JSON:
        return JSON['citationCount']

    return None


'''

Input: DOI
Return: dictionary where key = year and value = count of number of citations in that year. Dictionary is empty if paper with
DOI is not found

API only allows in total 10000 citations of papers to be retrieved. If a paper has > 10000 citations, then we cannot get the remaining
data. 

'''
def getCitationsByYear(DOI):

    URL = 'https://api.semanticscholar.org/graph/v1/paper/'
    QUERY = '/citations?fields=year'
    offset_string = '&offset=0&limit=999'
    offset = 0
    hash_map = defaultdict(int)

    while (offset >= 0):

        complete_url = URL + DOI + QUERY + offset_string
        response = requests.get(complete_url)
        JSON = response.json()

        if 'data' in JSON:

            for reference in JSON['data']:
                year = reference['citingPaper']['year']
                if year:
                    hash_map[year] += 1

        if ('next' in JSON):
            offset = JSON['next']
        else:
            offset = -1

        offset_string = '&offset=' + str(offset) + '&limit=1000'

    return hash_map

print(getCitationsByYear('10.1145/1148170.1148267'))