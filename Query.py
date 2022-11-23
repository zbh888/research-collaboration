from SPARQLWrapper import SPARQLWrapper, JSON

# Input: YearLowerBound, YearUpperBound, ConferenceName
# Output: DBLP_ID, PaperTitle, PublishedYear, DOI
# Example: query(2020, 2022 ,"IEEE Symposium on Security and Privacy")
def query(years_low, years_high, conf):
    sparql = SPARQLWrapper("https://qlever.cs.uni-freiburg.de/api/dblp")
    sparql.setReturnFormat(JSON)
    
    sparql.setQuery(f"""
    PREFIX dblps: <https://dblp.org/rdf/schema-2020-07-01#>
    PREFIX dblp: <https://dblp.org/rdf/schema#>
    SELECT ?paper ?title ?year ?doi WHERE {{
      ?paper dblp:publishedIn "{conf}" .
      ?paper dblp:yearOfPublication ?year .
      ?paper dblp:title ?title .
      ?paper dblp:doi ?doi .
      FILTER (?year >= "{years_low}") .
      FILTER (?year <= "{years_high}") .
    }}
    ORDER BY DESC(?year)
    """)
    query_res = sparql.queryAndConvert()
    cols = query_res['head']['vars']
    rows = []
    for res in query_res['results']['bindings']:
        row = []
        for col in cols:
            if col in res:
                row.append(res[col]['value'])
            else:
                print("Something Wrong")
                row.append("")
        rows.append(row)
    return rows


def collectDoi(res):
    DoiSet = set()
    for data in res:
        doi = data[3]
        index = doi.find('.org/')
        if index == -1:
            print('Error in finding .org/: ', doi)
        else:
            DoiSet.add(doi[index+5:])
    return DoiSet
