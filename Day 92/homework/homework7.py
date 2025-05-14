def string_expansion(s):
    repeat = 1
    final = ''
    if not s:
        return ""
    for i in s:
        if '0' <= i <= '9':
            repeat = int(i)
       # final += repeat * i 
        else:
            final += repeat * i
    return final
        