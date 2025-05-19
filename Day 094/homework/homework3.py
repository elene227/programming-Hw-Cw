def vaporcode(s):
    s = s.split()
    res = ''
    for i in s:
        for car in i:
            res += car.upper() + "  "
    return res[:-2]