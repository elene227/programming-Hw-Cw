def convert(st):
    lower = st.lower()
    
    res = ''
    
    for i in lower:
        if i == "a":
            res += "o"
        elif i == "o":
            res += "u"
        else:
            res += i
    return res
