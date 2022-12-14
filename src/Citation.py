import requests
import difflib
from collections import defaultdict
import random


def getCitationPublication(data, dateFunction):
    finaldata = []
    missing = []
    for each in data:
        citation = -1
        title = each[1]
        filename = each[0]
        doi = each[2]
        if len(title) != 0:
            paperID, temp_title = getPaperID(title[0])
            diff = difflib.SequenceMatcher(None, title[0], temp_title)
            if diff.ratio() > 0.85:
                dictionary = getCitationsByYear(paperID)
                total_c = getTotalCitations(paperID)
                if len(dictionary) != 0:
                    c,p = citation_publication(dictionary, dateFunction, filename)
                    each.append(c)
                    each.append(p)
                    each.append(total_c)
                    finaldata.append(each)
                    continue;
        if len(doi) != 0:
            dictionary = getCitationsByYear(doi[0])
            total_c = getTotalCitations(paperID)
            if len(dictionary) != 0:
                c,p = citation_publication(dictionary, dateFunction, filename)
                each.append(c)
                each.append(p)
                each.append(total_c)
                finaldata.append(each)
                continue;
        missing.append(each[0])
    return finaldata, missing

def getCitationsByYear(DOI):

    URL = 'https://api.semanticscholar.org/graph/v1/paper/'
    QUERY = '/citations?fields=year'
    S2_API_KEY = 'zr4963tPjdahwSmGYlhPJZKbAz9gigE5IOeQD8Lj'
    headers = {'User-Agent': getUserAgent(),
               'x-api-key': S2_API_KEY}
    offset_string = '&offset=0&limit=999'
    offset = 0
    hash_map = defaultdict(int)

    while (offset >= 0):

        complete_url = URL + DOI + QUERY + offset_string
        response = requests.get(complete_url, headers=headers)
        print(response.status_code, DOI)

        if response.status_code != 200:
            return hash_map

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

def getTotalCitations(paperID):

    URL = 'https://api.semanticscholar.org/graph/v1/paper/'
    QUERY = '?fields=citationCount'
    S2_API_KEY = 'zr4963tPjdahwSmGYlhPJZKbAz9gigE5IOeQD8Lj'
    headers = {'User-Agent': getUserAgent(),
               'x-api-key': S2_API_KEY}

    response = requests.get(URL + paperID + QUERY, headers=headers)
    print(response.status_code, paperID)

    if response.status_code != 200:
        return -1

    JSON = response.json()

    if 'citationCount' in JSON:
        return JSON['citationCount']

    return -1



def getPaperID(title):

    URL = 'https://api.semanticscholar.org/graph/v1/paper/search'
    QUERY = '?query=' + title
    S2_API_KEY = 'zr4963tPjdahwSmGYlhPJZKbAz9gigE5IOeQD8Lj'

    headers = {'User-Agent': getUserAgent(),
               'x-api-key': S2_API_KEY}

    response = requests.get(URL + QUERY,headers = headers)
    print(response.status_code, title)

    if response.status_code != 200:
        return ("", "")

    JSON = response.json()

    if JSON['total'] == 0:
        return ("", "")

    return (JSON['data'][0]['paperId'], JSON['data'][0]['title'] )

def citation_publication(s, function, filename):

    l = sorted(s)
    date = function(filename)

    three_year_count = 0
    for year in l:
        if year > date + 2:
            break
        three_year_count += s[year]
    return three_year_count, date

def getUserAgent():

    user_agent_list = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    ]

    user_agent = random.choice(user_agent_list)

    return user_agent



