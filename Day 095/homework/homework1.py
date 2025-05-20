def vaporcode(s):
    s = s.split()
    res = ''
    for i in s:
        for car in i:
            res += car.upper() + "  "
    return res[:-2]

def vaporcode(s):
    s = s.replace(' ','')
    
    sa = ""
    for i in s:
        sa += i.upper() + "  "
    return sa[:-2]
    
def vaporcode(s):
    s = s.replace(' ','')
    
    sa = ""
    for i in s:
        sa += i.upper() + "  "
    return sa[:-2]