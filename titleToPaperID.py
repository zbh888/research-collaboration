import requests
import difflib

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
  
  
  '''
  
  After you get paper ID and title from semantic scholar, check if that title matches with the original title of the paper. You can use this:
  result = getPaperID(original_title)
  temp = difflib.SequenceMatcher(None, original_title, result[1])
  if temp.ratio() > 0.85:
      # it means we can use this paperID because they are the same papers as the titles match.
  
  '''
  
