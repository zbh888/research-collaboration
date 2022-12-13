import requests

def getDoi(filename):

    URL = 'https://aclanthology.org/'
    extension = '.bib'
    finalURL = URL + filename + extension

    page = requests.get(finalURL)
    print(page.status_code, filename)
    index = -1
    try:
        index = page.text.index('doi')
    except:
        print("not found", filename)
        return ""

    text = page.text
    string = ""

    while text[index] != ',':
        string += text[index]
        index += 1

    return string.split('=')[1].strip('" ')
  
  # example usage
  # getDoi('D13-1107.bib ')
