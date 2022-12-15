def findUnknown(data, academia_set, industry_set, hybrid_set):
    unknown = set()
    for each in data:
        aff = each[3]
        aff = aff.split('-----')
        for name in aff:
            if not know(name, academia_set, industry_set, hybrid_set):
                unknown.add(name)
    return unknown
        
def know(string, academia_set, industry_set, hybrid_set):
    if string.lower() in academia_set or string.lower() in industry_set or string.lower() in hybrid_set:
        return True
    # academic
    for keyword in ['Nara Institute of Science and Technology','Harbin Institute of Technology','Karlsruhe Institut of Technology','Karlsruhe Institute of Technology', 'dept.','Department','Univ.','HKUST','LMU Munich','Universitat','campus', 'university', 'college', 'school', 'Université', 'Universität', 'Université','Massachusetts Institute of Technology']:
        if string.lower().find(keyword.lower())!=-1:
            return True
    for keyword in ['Raytheon','Hitachi','youdao','alibaba','Samsung','Huawei','xiaomi', 'facebook', 'amazon', 'google', 'microsoft']:
        if string.lower().find(keyword.lower())!=-1:
            return True
    for keyword in ['LORIA','RIKEN','NTT Communication Science Laboratories','Romanian Academy','Chinese Academy of Sciences','Fondazione Bruno Kessler','peng cheng']:
        if string.lower().find(keyword.lower())!=-1:
            return True
    return False
    
def isAcademia(aff, academia_set):
    if aff.lower() in academia_set:
        return True
    for keyword in ['Nara Institute of Science and Technology','Harbin Institute of Technology','Karlsruhe Institut of Technology','Karlsruhe Institute of Technology', 'dept.','Department','Univ.','HKUST','LMU Munich','Universitat','campus', 'university', 'college', 'school', 'Université', 'Universität', 'Université','Massachusetts Institute of Technology']:
        if aff.lower().find(keyword.lower())!=-1:
            return True
    return False

def isIndustry(aff, industry_set):
    if aff.lower() in industry_set:
        return True
    for keyword in ['Raytheon','Hitachi','youdao','alibaba','Samsung','Huawei','xiaomi', 'facebook', 'amazon', 'google', 'microsoft']:
        if aff.lower().find(keyword.lower())!=-1:
            return True
    return False

def isHybrid(aff, hybrid_set):
    if aff.lower() in hybrid_set:
        return True
    for keyword in ['LORIA','RIKEN','NTT Communication Science Laboratories','Romanian Academy','Chinese Academy of Sciences','Fondazione Bruno Kessler','peng cheng']:
        if aff.lower().find(keyword.lower())!=-1:
            return True
    return False
    
def classify(data, academia_set, industry_set, hybrid_set):
    finaldata = []
    for each in data:
        value = 0
        count = 0
        for aff in each[3].split('-----'):
            count += 1
            if isAcademia(aff, academia_set):
                value += 0
            elif isIndustry(aff, industry_set):
                value += 2
            elif isHybrid(aff, hybrid_set):
                value += 1
            else:
                print(aff)
        if value == 0:
            each.append(0)
        if value == 2*count:
            each.append(2)
        else:
            each.append(1)
        finaldata.append(each)
    return finaldata
