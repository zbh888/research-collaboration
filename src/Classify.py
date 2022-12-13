def findUnknown(data, academia_set, industry_set):
    unknown = set()
    for each in data:
        aff = each[3]
        for name in aff:
            if not know(name, academia_set, industry_set):
                unknown.add(name)
    return unknown
        
def know(string, academia_set, industry_set):
    if string.lower() in academia_set or string.lower() in industry_set:
        return True
    else:
        return False
