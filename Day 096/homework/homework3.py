def is_vow(inp):
    res = []
    
    for i in inp:
        if i == 111:
            res.append("o")
        elif i == 105:
            res.append("i")
        elif i == 97:
            res.append("a")
        elif i == 117:
            res.append("u")
        elif i == 101:
            res.append("e")
        else:
            res.append(i)
    return res
        