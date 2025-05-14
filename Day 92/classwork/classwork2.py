def even_chars(st): 
    new_list = []
    if len(st) < 2 or len(st) > 100:
        return "invalid string"
    else:
        for i in range(1, len(st), 2):
            new_list.append (st[i])
    return new_list