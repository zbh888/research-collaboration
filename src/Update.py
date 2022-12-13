import os

def getSet():
    industry_set = set()
    academia_set = set()
    fileIndustry = open('industry.txt', 'r')
    for line in fileIndustry:
        industry_set.add(line.strip().lower())
    fileAcademia = open('academia.txt', 'r')
    for line in fileAcademia:
        academia_set.add(line.strip().lower())
    if '' in industry_set:
        industry_set.remove('')
    if '' in academia_set:
        academia_set.remove('')
    return industry_set, academia_set

def writeSet(industry_set, academia_set):
    original_in, original_ac = getSet()
    new_in = original_in.union(industry_set)
    new_ac = original_ac.union(academia_set)
    if len(new_in.intersection(new_ac)) != 0:
        print("CANNOT MERGE")
    else:
        os.remove("industry.txt")
        os.remove("academia.txt")
        with open('industry.txt', 'a') as industry:
            for each in new_in:
                industry.write(each + '\n')
        with open('academia.txt', 'a') as academia:
            for each in new_ac:
                academia.write(each + '\n')
