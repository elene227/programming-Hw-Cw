def expanded_form(num):
    res = ''
    zer = len(str(num)) - 1
    
    for i in str(num):
        if i == "0":
            zer -= 1
        else:
            res += i + zer * '0' + " + "
            zer -= 1
    return res[:-3]
            